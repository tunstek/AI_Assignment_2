# AI for Self Driving Car

# Importing the libraries

import numpy as np
import random
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
#optimise stochastic gradient descent
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable

# Creating the architecture of the Neural Network

class Network(nn.Module):
    
    ''' 
    input_size:the number of encoded values(3 signals, +orientation, -orientataion)
    that describe the state of the environment

    nb_action: number of output neurons
    '''
        
    def __init__(self, input_size, nb_action):
        super(Network, self).__init__()
        self.input_size = input_size
        self.nb_action = nb_action
        
        ''' 
        full connections, nerual network with one hidden layer, so two full connections
        one full connection between the input layer and the hidden layer
        another full connection between the hidden layer and the ouput layer
        '''
        
        self.fc1 = nn.Linear(input_size, 30)
        self.fc2 = nn.Linear(30, nb_action)
    
    # activate neuron and return q-values for each possible action depending on the state
    def forward(self, state):
        #apply the rectifier function
        x = F.relu(self.fc1(state))
        #pass the activated neurons to second full connection, hidden layer - output layer 
        q_values = self.fc2(x)
        return q_values


# Implementing Experience Replay
      
class ReplayMemory(object):
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
   
    # Instead of considering the current state, also consider past states place past X transitions into memory. 
    def push(self, event):
        self.memory.append(event)
        if len(self.memory) > self.capacity:
            del self.memory[0]
    
    # Take random batches of past experiences to make next update
    def sample(self, batch_size):
        samples = zip(*random.sample(self.memory, batch_size))
        # make each variable a pytorch variable 
        return map(lambda x: Variable(torch.cat(x, 0)), samples)

# Implementing Deep Q Learning

class Dqn():
    
    def __init__(self, input_size, nb_action, gamma):
        self.gamma = gamma
        # sliding window of the last x rewards
        self.reward_window = []
        # initialise the nerual net
        self.model = Network(input_size, nb_action)
        self.memory = ReplayMemory(100000)
        # connect Adam optimiser to the neural network, learning rate(alpha) = 0.001 
        self.optimizer = optim.Adam(self.model.parameters(), lr = 0.001)
        # add a dimension and index 0
        self.last_state = torch.Tensor(input_size).unsqueeze(0)
        self.last_action = 0
        self.last_reward = 0
    
    # select best action to play while still exploring other states
    # in argmax we are not exploring the other actions
    # softmax returns the probabilities of each of the three actions
    def select_action(self, state):
        # choose which action to play based on the temperature(in this case T=100)
        probs = F.softmax(self.model(Variable(state, volatile = True))*100) # T=100
        action = probs.multinomial()
        return action.data[0,0]
    
    def learn(self, batch_state, batch_next_state, batch_reward, batch_action):
        outputs = self.model(batch_state).gather(1, batch_action.unsqueeze(1)).squeeze(1)
        # detach and get the maximum of all values of next state w.r.t action
        next_outputs = self.model(batch_next_state).detach().max(1)[0]
        target = self.gamma*next_outputs + batch_reward
        # compute Huber loss
        td_loss = F.smooth_l1_loss(outputs, target)
        # re-initialise optimiser
        self.optimizer.zero_grad()
        # backpropagate error
        # retain_variables = True to save up on memory
        td_loss.backward(retain_variables = True)
        self.optimizer.step()
    
    def update(self, reward, new_signal):
        new_state = torch.Tensor(new_signal).float().unsqueeze(0)
        self.memory.push((self.last_state, new_state, torch.LongTensor([int(self.last_action)]), torch.Tensor([self.last_reward])))
        action = self.select_action(new_state)
        if len(self.memory.memory) > 100:
            batch_state, batch_next_state, batch_action, batch_reward = self.memory.sample(100)
            self.learn(batch_state, batch_next_state, batch_reward, batch_action)
        self.last_action = action
        self.last_state = new_state
        self.last_reward = reward
        self.reward_window.append(reward)
        if len(self.reward_window) > 1000:
            del self.reward_window[0]
        return action
    
    def score(self):
        return sum(self.reward_window)/(len(self.reward_window)+1.)
    
    def save(self):
        torch.save({'state_dict': self.model.state_dict(),
                    'optimizer' : self.optimizer.state_dict(),
                   }, 'last_brain.pth')
    
    def load(self):
        if os.path.isfile('last_brain.pth'):
            print("=> loading checkpoint... ")
            checkpoint = torch.load('last_brain.pth')
            self.model.load_state_dict(checkpoint['state_dict'])
            self.optimizer.load_state_dict(checkpoint['optimizer'])
            print("done !")
        else:
            print("no checkpoint found...")