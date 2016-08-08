### In this script, I calculate the probability that a dice has 4,6,8,12 or 20 faces
### based on a succession of observed rolls

# Full list version #


# def update(prior, data, hypothesis):
#     lklhd = []
#     posterior = prior
#     norm = 0
#     for d in hypothesis:
#         if d < data:
#             lklhd.append(0)
#         else:
#             lklhd.append(1.0 / d)
#     for i in range(len(prior)):
#         norm += prior[i] * lklhd[i]
#     for j in range(len(prior)):
#         posterior[j] = prior[j] * lklhd[j] / sum(norm)
#     return posterior
#
# # Definition of the hypotheses
# hypothesis = [4, 6, 8, 12, 20]
# prior = [1.0/5]*5
# rolls = [6, 6, 8, 7, 7, 5, 4]
#
# # Initializing the posterior probability at the prior values
# posterior = prior

#for roll in rolls:
#    posterior = update(posterior, roll, hypothesis)


# Full dictionary version #

def update(prior, roll, hypothesis):
    posterior = {}
    lklhd = {}
    norm = 0
    for h in hypothesis:
        if h < roll:
            lklhd[h] = 0
        else:
            lklhd[h] = 1.0 / h
        posterior[h] = prior[h] * lklhd[h]
    norm = sum(posterior.values())
    for h in hypothesis:
        posterior[h] = posterior[h] / norm
    return posterior

hypothesis = input('What dice do you have? ')
n = len(hypothesis)
prior = {}
for h in hypothesis:
    prior[h] = 1.0 / n

posterior = prior
rolls = input('What rolls did you observe? ')

for r in rolls:
    posterior = update(posterior, r, hypothesis)

print(posterior)




