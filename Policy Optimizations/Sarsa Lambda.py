import numpy as np
import matplotlib.pyplot as plt
import tqdm
num_actions = 15


class testEnv:
	def __init__(self):
		self.state = np.random.randint(10)
		self.steps = 0
		self.old_action = 0


	def step(self, action):
		self.steps +=1

		done = False
		if self.steps == 10:
			done = True

		if action >= self.old_action:
			self.state= np.random.randint(10)
			return self.state, 1, done, None
		else:
			self.state= np.random.randint(10)
			return self.state, -1, done, None

		self.old_action = action
	def reset(self):
		self.state = np.random.randint(10)
		self.steps = 0
		return self.state

	def sample(self):
		return np.random.randint(num_actions)


def init_Q(state):
	try:
		temp = Q[state]
	except:
		Q[state] = np.zeros(num_actions)


def init_E(state):
	try:
		temp = E[state]
	except:
		E[state] = np.zeros(num_actions)

def get_action(state):

	if np.random.random() < eps:
		return env.sample()
	
	besta = np.argmax(Q[state])

	return besta


def update_QE(td_error):
	for s in Q.keys():
		for a in range(num_actions):
			Q[s][a] = Q[s][a] + alpha*td_error*E[s][a]
			E[s][a] = gamma*lam*E[s][a]


def play_one():
	s = env.reset()


	init_E(s)
	init_Q(s)

	a = get_action(s)
	rewards =[]
	done = False
	while not done:
		old_s = s
		old_a = a
		s,r,done,info = env.step(old_a)
		
		init_Q(s)
		init_E(s)

		a = get_action(s)
		print(old_s, old_a)
		td_error = r + gamma*Q[s][a] - Q[old_s][old_a]
		E[old_s][old_a] = E[old_s][old_a] + 1

		update_QE(td_error)
		rewards.append(r)

	return np.sum(rewards)

if __name__ == "__main__":
	env = testEnv()
	s = env.reset()
	Q = {}
	alpha = 0.01
	gamma = 0.99
	lam = 0.1
	eps = 0.1
	E = {}
	print(play_one())