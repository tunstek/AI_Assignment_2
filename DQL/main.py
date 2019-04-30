import gym
from util import mul, preprocess_frame
from DQN import Dqn as DQN
import datetime

class MountainCar():
    def __init__(self, algo):
        self.env = gym.make('CartPole-v1')
        self.env = gym.wrappers.Monitor(self.env, "videos", force=True)

        self.input_size = mul(self.env.observation_space.shape)
        self.num_actions = self.env.action_space.n
        print "num_inputs: {}\nnum_actions: {}".format(self.input_size, self.num_actions)

        self.gamma = 0.9
        self.algo = algo(self.input_size, self.num_actions, self.gamma)

        self.run()

    def run(self):
        self.env.reset()
        rewards = []
        obs, rew, done, info = self.env.step(self.env.action_space.sample())  # take a random action
        rewards.append(rew)
        while True:
            next_action = self.algo.update(rew, obs)
            obs, rew, done, info = self.env.step(next_action)
            rewards.append(rew)
            if done:
                print("[{}] Reward: {}".format(datetime.datetime.now(), sum(rewards)))
                rewards = []
                if sum(rewards) >= 21:
                    print("Congratulations, your AI wins")
                    break
                self.env.reset()
        self.env.close()


if __name__ == '__main__':
    test = MountainCar(DQN)
