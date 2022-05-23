# Generates random scores for surfers in the WSL using pandas

import random
import pandas

names = ["John John Florence", "Kanoa Igarashi", "Kelly Slater", "Lakey Peterson", "Carissa Moore", "Tyler Wright"]
surfer_scores = {name: [random.randint(0, 10)] for name in names}
# print(surfer_scores)

index_label = ["heat 1", "heat 2", "heat 3"]

for name, score_list in surfer_scores.items():
    score_list = score_list.extend([random.randint(0, 10), random.randint(0, 10)])
# print(surfer_scores)

surfer_pd = pandas.DataFrame(surfer_scores, index=index_label)
surfer_pd = surfer_pd.transpose()
print(surfer_pd)

# for (index, row) in surfer_pd.iterrows():
    # if row["heat 2"] > 5:
        # print(f"{index}:\n{row}")

# new_dictionary = {name:score for (name,score) in surfer_pd.iterrows()}
# print(new_dictionary)
#
# new_dictionary2 = surfer_pd.to_dict()
# print(new_dictionary2)