# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        greeting = "Hello World"
        return greeting  # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
        new_value = str(value_to_be_added_to) + str(value_to_add)
        return new_value  # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        result = string_to_fetch_from[starting_index:ending_index + 1]
        return result  # TODO - Implement solution

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        result = string_to_fetch_from[starting_index + 1:ending_index]
        return result  # TODO - Implement solution

    def compare(self, first_value, second_value):
        if str(first_value) == str(second_value):
            return True
        elif first_value is None or second_value is int:
            return True
        elif first_value is False or second_value is int:
            return True
        elif first_value is True or second_value is int:
            return True
        else:
            return False  # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
        return None  # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        split_string = string_to_fetch_from.split()
        first_word = split_string[0]
        return first_word  # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        split_string = string_to_fetch_from.split()
        second_word = split_string[1]
        return second_word  # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return None  # TODO - Implement solution
