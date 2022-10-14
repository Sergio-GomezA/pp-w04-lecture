# First fit heuristic for the bin packing algorithm.

def first_fit(list_items, bin_capacity):
    pass
    # Sort the list in decreasing
    list_items.sort(reverse=True)
    bins = [0]
    # loop through all itemps
    for item in list_items:
        # flag to signal if item has been placed
        placed = False        
        # loop through all bins
        for i in range(len(bins)):
            if item + bins[i] <= bin_capacity:
                bins[i] += item
                placed = True
                break
        # if we didn't find a bin with enough capacity
        if not placed:
            bins.append(item)
    return bins


## Testing
list_items = [2, 1, 3, 2, 1, 2, 3, 1]
bin_capacity = 4
expected_bins = [4, 4, 4, 3]

# assert := nothing if argument true ; raises error + message if argument false
# good for testing

bins = first_fit(list_items, bin_capacity)
# print(bins)
# assert bins == expected_bins, 'Doesn\'t match expected result'

# sort them first
