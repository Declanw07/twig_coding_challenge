import math
import logging

logger = logging.getLogger(__name__)


def group_list_elements(list_to_chunk, chunk_value):
    """
    Function which splits a list (array) into a list of length chunk_value
    containing sub-lists of equal length, if the list cannot be split equally
    then the last sub-list contains the remaining elements.

    :param list_to_chunk:       :list: list to be split into sub-lists.
    :param chunk_value:         :int: desired length of the chunked list.
    :return:                    :list: list of length chunk_value containing
                                equally sized lists.

    Note: If the chunk_value is greater than the length of list_to_chunk then
          the list will be split into single elements.
    """
    # Check that the chunk_value is an int and the list_to_chunk is a list,
    # if they aren't, a warning is logged.
    try:
        if not isinstance(chunk_value, int):
            logger.error('Passed chunk_value is not an integer, please pass'
                         'an integer')
            return []
        if not isinstance(list_to_chunk, list):
            logger.error('Passed list_to_chunk value is not a list, please'
                         'pass a list')
            return []
        # Need the chunk size so that we can iterate over the list in
        # steps of chunk_size. chunk_size can't be less than 1.
        chunk_size = round((len(list_to_chunk)) / chunk_value) or 1
        chunked_list = []
        count = 0
        # Loop through in steps of chunk_size.
        for i in range(0, len(list_to_chunk), chunk_size):
            # If we're on the last iteration, add the rest of the
            # list_to_chunk as the last element of the chunked list
            # and then break.
            if count == chunk_value - 1:
                chunked_list.append(list_to_chunk[i:])
                break
            # Add a list to the chunked list which contains elements
            # between i and i+chunk_size, then add 1 to the count.
            chunked_list.append(list_to_chunk[i:i + chunk_size])
            count += 1
        return chunked_list
    except ZeroDivisionError:
        logger.error('Cannot divide list into a new list of 0 elements,'
                     ' please enter a non-zero integer character')
        return []
