import gym
from util import mul, preprocess_frame
from DQN import Dqn as DQN
import datetime

MAX_REWARD = 4000

class CartPole():
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
        reward_history = []
        rewards = []
        obs, rew, done, info = self.env.step(self.env.action_space.sample())  # take a random action
        rewards.append(rew)
        while True:
            next_action = self.algo.update(rew, obs)
            obs, rew, done, info = self.env.step(next_action)
            rewards.append(rew)
            if done:
                print("[{}] Reward: {}".format(datetime.datetime.now(), sum(rewards)))
                reward_history.append(sum(rewards))
                if sum(rewards) >= MAX_REWARD:
                    print("Congratulations, your AI wins")
                    break
                rewards = []
                self.env.reset()
        self.env.close()

        csv = "run,reward\n"
        for i, r in enumerate(reward_history):
            csv = csv + "{},{}\n".format(i, r)
        with open('results/result.csv', 'w') as f:
            f.write(csv)

        import matplotlib.pyplot as plt
        plt.plot(reward_history)
        plt.ylabel('Reward')
        plt.xlabel('Run')
        plt.savefig('results/cartpole_runs.png')


if __name__ == '__main__':
    test = CartPole(DQN)
