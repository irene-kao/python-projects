# This program simulates random walks to determine the probability of reaching 60 steps with 50 dice rolls per walk.

import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(123)
all_walks = []
ends = []

print("Imagine John is walking up a staircase with 60 steps.\n"
      "Each of his moves is determined by a dice you will roll 50 times.\n"
      "If you roll a 1 or 2, John will go down a step. Otherwise, he moves up.\n"
      "This program will determine the probability he will reach the the top of the staircase.\n"
      "It will also plot John's path and show you how many times he reached each step.\n")

def roll_dice():
    return np.random.randint(1,7)

# We will determine the probability using 50 random walks
for test_num in range(50):
    step = 0
    random_walk = []
    # Roll the dice 50 times in each walk
    for rolls in range(50):
        dice = roll_dice()

        if dice < 3 and step >= 1:
            step -= 1
        elif dice < 6:
            step += 1
        else:
            dice = roll_dice()
            step += dice

        clumsy = np.random.rand()
        if clumsy <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)
    ends.append(step)


np_all_walks = np.array(all_walks)
np_ends = np_all_walks[:, -1]

# print(np_all_walks)
# plt.plot(np_all_walks)
# plt.show()

np_all_walks_t = np.transpose(np_all_walks)
print(np_all_walks_t)
plt.plot(np_all_walks_t)
plt.title("Random walk visualization")
plt.xlabel("Roll Number")
plt.ylabel("Steps")
plt.show()

plt.hist(np_ends, 20)
plt.title("Inventory of times final step reached")
plt.xlabel("Final step")
plt.ylabel("Number of times step reached")
plt.show()

match = np_ends[np_ends >= 60]
probability = len(match) / len(all_walks)

print(f"The probability of John reaching 60 steps after 50 dice rolls is {probability}")
