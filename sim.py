import random
import numpy as np
import matplotlib.pyplot as plt

def trial(choice: int, change_prob: float = 0.5) -> bool:
    """Perform a single trial of Monty Hall
    """
    choices = [0, 1, 2]
    correct = np.random.choice(choices)

    # remove a choice
    for i in range(3):
        if i != choice and i != correct:
            choices.remove(i)
            break

    # flip choice?
    flip = np.random.choice([0, 1], p=[1-change_prob, change_prob])
    if flip:
        choices.remove(choice)
        choice = choices[0]

    return choice == correct


def stats(change_prob: float) -> float:
    """Compute winning rate of Monty Hall given probability of switching
    """
    N = 20000
    wrate = 0
    choices = np.random.choice([0, 1, 2], size=N)

    for i in range(N):
        wrate += int(trial(choices[i], change_prob))

    wrate = float(wrate) / float(N)

    return wrate


print(f'Probability for  never switch: {stats(0.0)}')
print(f'Probability for always switch: {stats(1.0)}')
print(f'Probability for random switch: {stats(0.5)}')

N = 10
wrate = np.zeros(N)
p = np.linspace(0.0, 1.0,N)
for i in range(N):
    wrate[i] = stats(p[i])


plt.plot(p, wrate)
plt.xlabel("Strategy - Probability of switching")
plt.ylabel("Win rate")
plt.grid()
plt.show()
