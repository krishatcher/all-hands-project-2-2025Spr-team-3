"""Analyze data values created from an experiment."""


def calculate_average_values(
    data_list: list[float], data_count: int
) -> list[float]:
    """Calculate the average values for the data in the provided list"""
    data_list_averages = []
    # loop through the input list of lists and process each child list
    for entry in data_list:
        # calculate the average using the sum of the child list
        # and the data_count passed-in
        avg_value = entry / data_count
        # add this result to the output list
        data_list_averages.append(round(avg_value, 6))
    # return the output list as the result of this function
    return data_list_averages
