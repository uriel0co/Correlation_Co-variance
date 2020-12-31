def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2) # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values)%2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)

#This function returns the covariance of two lists of values
def covariance(first_list_of_values, second_list_of_values):
    result = 0
    first_mean = mean(first_list_of_values)
    second_mean = mean(second_list_of_values)
    result = sum((x - first_mean)*(y-second_mean) for x, y in zip(first_list_of_values, second_list_of_values))
    return result / (len(first_list_of_values)-1)

#This function returns the correlation of two lists of values
def correlation(first_list, second_list):
    result = 0
    covariance_value = covariance(first_list, second_list)
    first_mean = mean(first_list)
    second_mean = mean(second_list)
    std_dev_1 = (sum([(val - first_mean) ** 2 for val in first_list]) / (len(first_list) - 1)) ** (1.0/2)
    std_dev_2 = (sum([(val - second_mean) ** 2 for val in second_list]) / (len(second_list) - 1)) ** (1.0/2)
    return covariance_value / ((std_dev_1) * (std_dev_2))

