# First fit heuristic for the bin packing algorithm.

<<<<<<< HEAD
def first_fit_decreasing(list_items, bin_capacity):
    
    # start with one empty bin
    bins = [0]

    # sort the list in decreasing order
    list_items.sort(reverse=True)

    # for loop over the list_items:
    for item in list_items:

        placed = False

        # for loop over the bins:
        for i in range(len(bins)):
            # does it fit?
            # if it fits:
            if item <= bin_capacity - bins[i]:
                # place item in bin
                bins[i] = bins[i] + item
                # raise the flag
                placed = True
                # break the loop
                break

        # if it's not placed in any bins:
        if not placed:
        # if placed == False:
            bins.append(item)
            # # open a new bin
            # bins.append(0)
            # # place the item in new bin
            # bins[-1] = item
    
    # return list of bins
=======
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
>>>>>>> 1d617c1 (my solution)
    return bins


## Testing
list_items = [2, 1, 3, 2, 1, 2, 3, 1]
bin_capacity = 4
expected_bins = [4, 4, 4, 3]

<<<<<<< HEAD
bins = first_fit_decreasing(list_items, bin_capacity)
print(bins)

assert bins == expected_bins, f'Wrong result: obtained {bins}, expected {expected_bins}'
=======
# assert := nothing if argument true ; raises error + message if argument false
# good for testing

bins = first_fit(list_items, bin_capacity)
# print(bins)
# assert bins == expected_bins, 'Doesn\'t match expected result'

# sort them first
>>>>>>> 1d617c1 (my solution)
