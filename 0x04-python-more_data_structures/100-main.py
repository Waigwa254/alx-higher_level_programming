#!/usr/bin/python3
def weight_average(my_list):
    total_weighted_sum = sum(weight * value for weight, value in my_list)
    total_weight = sum(weight for weight, _ in my_list)

    if total_weight == 0:
        return 0  # To avoid division by zero if the list is empty

    return total_weighted_sum / total_weight

# Your code remains the same
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

