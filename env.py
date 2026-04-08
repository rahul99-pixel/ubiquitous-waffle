class SimpleEnv:
    def __init__(self):
        self.state = 0

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        if action == 1:
            self.state += 1
        elif action == 2:
            self.state -= 1

        reward = 1 if self.state == 5 else 0
        done = self.state == 5

        return self.state, reward, done, {}
