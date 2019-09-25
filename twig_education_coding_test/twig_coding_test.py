import logging

logger = logging.getLogger(__name__)


def group_list_elements(list_to_chunk, chunk_value):
    """
    Function which splits a list (array) into sub-lists of length chunk_value,
    if the length cannot be split equally by the chunk value the final sub-list
    will have length equal to list_to_chunk % chunk_value.

    This method follows the pseudo-code example and answer which suggests that
    the chunk_value should have 1 taken away from it. If that is not the
    desired behaviour then any reference to chunk_value-1 could be replaced
    with just chunk_value.

    :param list_to_chunk:       :list: list to be split into sub-lists.
    :param chunk_value:         :int: desired length of sub-lists.
    :return:                    :list: list containing sub-lists of length
                                chunk_value.
    """
    # Check that the chunk_value is an int and the list_to_chunk is a list,
    # if they aren't, a warning is logged.
    if isinstance(chunk_value, int) and isinstance(list_to_chunk, list):
        # If the chunk_value is 0 or 1 we know that there is no splitting
        # needing, therefor we save time by returning the list_to_chunk
        # (inside a list). Also keeping in-line with pseudo-code by
        # doing this.
        if chunk_value == 0 or chunk_value == 1:
            return [list_to_chunk]
        chunked_list = []
        # Loop through a range from 0 to the length of the chunk stepping
        # by chunk_value - 1 for each iteration. The chunk_value - 1 is
        # to keep in-line with the pseudo-code, not sure if this is needed.
        for i in range(0, len(list_to_chunk), chunk_value-1):
            # Add elements between i and i+chunk_value-1 (not inclusive) to the
            # chunked list (elements are added to the chunked_list as a list)
            chunked_list.append(list_to_chunk[i:i + chunk_value-1])
        return chunked_list
    # The chunk_value passed is not an int, therefore it can't be split by that
    # value so log a warning, depending on the severity this could instead,
    # raise a TypeError instead of logging a warning.
    logger.warning('chunk value passed is not an int, please enter an int')
    return []
