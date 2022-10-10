# First fit heuristic for the bin packing algorithm.

def first_fit(list_items, bin_capacity):
    
    # start with one empty bin
    bins = [0]


    # for loop over the list_items:
    for item in list_items:

        placed = False

        # for loop over the bins:
        for b in bins:
            # does it fit?
            # if it fits:
            if item <= bin_capacity - b:
                # place item in bin
                b += item
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
    return bins





## Testing
list_items = [2, 1, 3, 2, 1, 2, 3, 1]
bin_capacity = 4
expected_bins = [4, 4, 4, 3]

bins = first_fit(list_items, bin_capacity)

assert bins == expected_bins, 'Wrong result, try again!'