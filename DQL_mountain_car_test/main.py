import gym
from util import mul, preprocess_frame
from DQN import Dqn as DQN

class MountainCar():
    def __init__(self, algo):
        self.env = gym.make('PongDeterministic-v4')

        self.input_size = mul(self.env.observation_space.shape)/3
        self.num_actions = self.env.action_space.n
        print "num_inputs: {}\nnum_actions: {}".format(self.input_size, self.num_actions)

        self.gamma = 0.5
        self.algo = algo(self.input_size, self.num_actions, self.gamma)

        self.run()

    def run(self):
        self.env.reset()
        self.env.render()
        obs, rew, done, info = self.env.step(self.env.action_space.sample())  # take a random action
        for _ in range(10000):
            self.env.render()
            next_action = self.algo.update(rew, preprocess_frame(obs))
            obs, rew, done, info = self.env.step(next_action)
        self.env.close()


if __name__ == '__main__':
    test = MountainCar(DQN)