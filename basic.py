import gym
import time
from gym import wrappers

# 0 = move cart left, 1 = right

env = gym.make('CartPole-v0')
#env = wrappers.Monitor(env, f'./vids/{time.time()}')

for i_episode in range(20):
    ob = env.reset()
    for t in range(100):
        env.render()
        print(ob)
        action = env.action_space.sample()
        ob, reward, done, info = env.step(action)
        if done:
            print(f"Episode finished after {t+1} timesteps")
            break
env.close()

