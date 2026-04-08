from env import SimpleEnv

env = SimpleEnv()

for episode in range(5):
    state = env.reset()
    done = False

    while not done:
        action = 1
        state, reward, done, _ = env.step(action)

print("Training done")
