

from random import random, randrange, randint


class OX:
    def __init__(self, post_selection_pop, chance_to_ox: float):
        self.pop = post_selection_pop
        self.chance_to_ox = chance_to_ox

    def pair(self) -> list:
        indexes = [item for item in range(0, len(self.pop))]
        pairs_pn = {}

        for p in range(len(indexes) // 2):
            pairs_pn[p + 1] = (indexes.pop(randrange(len(indexes))),
                               indexes.pop(randrange(len(indexes))))

        pairs = []
        for x in pairs_pn:
            pairs.append((self.pop[pairs_pn[x][0]], self.pop[pairs_pn[x][1]]))

        return pairs 



    def ox(self) -> list:
        # This is an OX crossover

        pairs=self.pair()
        new_pop = []
        no_cross = []
        for x in pairs:
            if random() >= self.chance_to_ox:
                parent1 = x[0]
                parent2 = x[1]

                first_cross_point = randint(0, len(parent1) - 2)
                second_cross_point = randint(first_cross_point + 1, len(parent1) - 1)

                parent1_middle_cross = parent1[first_cross_point:second_cross_point]
                parent2_middle_cross = parent2[first_cross_point:second_cross_point]

                substitution_elements_1 = parent1[second_cross_point:] + parent1[:first_cross_point] + parent1_middle_cross
                substitutions_elements_2 = parent2[second_cross_point:] + parent2[:first_cross_point] + parent2_middle_cross

                temp_substitution1 = []
                temp_substitution2 = []

                for i in substitution_elements_1:
                    if i not in parent2_middle_cross:
                        temp_substitution1.append(i)
                    else:
                        pass

                for i in substitutions_elements_2:
                    if i not in parent1_middle_cross:
                        temp_substitution2.append(i)
                    else:
                        pass

                crosspoint1_len = len(parent1[:first_cross_point])

                crosspoint1 = temp_substitution1[:crosspoint1_len]
                [temp_substitution1.pop(0) for _ in range(crosspoint1_len)]
                crosspoint2 = temp_substitution1

                child1 = crosspoint1 + parent2_middle_cross + crosspoint2

                crosspoint1_len = len(parent1[second_cross_point:])

                crosspoint1 = temp_substitution2[:crosspoint1_len]
                [temp_substitution2.pop(0) for _ in range(crosspoint1_len)]
                crosspoint2 = temp_substitution2

                child2 = crosspoint1 + parent1_middle_cross + crosspoint2

                new_pop.append(child1)
                new_pop.append(child2)
            else:

                no_cross.append(x[0])
                no_cross.append(x[1])

        return new_pop + no_cross
