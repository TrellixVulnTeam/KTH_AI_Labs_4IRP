#!/usr/bin/env python3
# rewards: [golden_fish, jellyfish_1, jellyfish_2, ... , step]
rewards = [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -1000]
 
# Q learning learning rate
alpha = 0.1

# Q learning discount rate
gamma = 0.3

# Epsilon initial
epsilon_initial = 0

# Epsilon final
epsilon_final = 0

# Annealing timesteps
annealing_timesteps = 1

# threshold
threshold = 1e-3
