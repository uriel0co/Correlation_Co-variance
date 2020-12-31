from statistics import mean, median, variance, correlation
import csv


def load_data(path):
    """
    Loads data from given csv
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                for i, column_name in enumerate(row):  # enumerate generates index together with value
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    current_column_name = index_to_column_name[i]  # reproducing column name
                    data[current_column_name].append(float(value))
    return data


# This function prints the mean, median and variance of every feature in the data
# and prints the pairs of features that have the lowest and highest correlation and their values
def run_analysis():
    file_path = './winequality.csv'
    data = load_data(file_path)

    # first way of printing. Everything casted to string, and spaces put automatically between passed values.
    print('Number of features:', len(data))
    total_max_correlation = 0
    total_min_correlation = 1
    for feature_name, list_of_values in sorted(data.items()):
        # second way of printing. We print single string after format function.
        # Format function fills {} with values passed as arguments. It has nice applications for better printing,
        # like limiting number of digits for floats or other formatting tools.
        print('"{}". Mean: {:3.2f}, Median: {:0.2f}, Std: {:0.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values)**0.5))
        temp_max_correlation = 0
        temp_min_correlation = 1
        for another_feature, another_list in sorted(data.items()):
            if another_feature != feature_name:
                correlation_value = abs(correlation(list_of_values, another_list))
                if correlation_value < total_min_correlation:
                    temp_min_correlation = correlation_value
                    min_feature_2 = another_feature
                if correlation_value > total_max_correlation:
                    temp_max_correlation = correlation_value
                    max_feature_2 = another_feature
        if temp_max_correlation > total_max_correlation:
            total_max_correlation = temp_max_correlation
            max_feature_1 = feature_name
        if total_min_correlation > temp_min_correlation:
            total_min_correlation = temp_min_correlation
            min_feature_1 = feature_name
    # here you should compute correlations. Be careful, pair should be sorted before printing

    strongest_pair = sorted([max_feature_1, max_feature_2])
    high_correlation = correlation(data[max_feature_1], data[max_feature_2])
    print('The strongest linear relationship is between: "{}","{}". ''The value is: {:0.4f}'.format(strongest_pair[0], strongest_pair[1], high_correlation))

    weakest_pair = sorted([min_feature_1, min_feature_2])
    low_correlation = correlation(data[min_feature_1], data[min_feature_2])
    print('The weakest linear relationship is between: "{}","{}". '
          'The value is: {:0.4f}'.format(*weakest_pair, low_correlation))  # * converts list to arguments.
    # Line 53 is equivalent to line 48, this is just other way to use list as arguments


if __name__ == '__main__':
    run_analysis()