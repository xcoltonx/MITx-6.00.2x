"""
Another way to transport the cows is to look at every possible combination of trips and pick the best one. This is an example of a brute force algorithm.

Implement a brute force algorithm to find the minimum number of trips needed to take all the cows across the universe in the function brute_force_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

Notes:

Make sure not to mutate the dictionary of cows!
In order to enumerate all possible combinations of trips, you will want to work with set partitions. We have provided you with a helper function called get_partitions that generates all the set partitions for a set of cows. More details on this function are provided below.
Assumptions:

Assume that order doesn't matter. (1) [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips. (2) [[1,2],[3,4]] and [[2,1],[3,4]] are considered the same partitions of [1,2,3,4].
You can assume that all the cows are between 0 and 100 tons in weight.
All the cows have unique names.
If multiple cows weigh the same amount, break ties arbitrarily.
The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.
Helper function get_partitions in ps1_partitions.py:

To generate all the possibilities for the brute force method, you will want to work with set partitions.

For instance, all the possible 2-partitions of the list [1,2,3,4] are [[1,2],[3,4]], [[1,3],[2,4]], [[2,3],[1,4]], [[1],[2,3,4]], [[2],[1,3,4]], [[3],[1,2,4]], [[4],[1,2,3]].

To help you with creating partitions, we have included a helper function get_partitions(L) that takes as input a list and returns a generator that contains all the possible partitions of this list, from 0-partitions to n-partitions, where n is the length of this list.

You can review more on generators in the Lecture 2 Exercise 1. To use generators, you must iterate over the generator to retrieve the elements; you cannot index into a generator! For instance, the recommended way to call get_partitions on a list [1,2,3] is the following. Try it out in ps1_partitions.py to see what is printed!

for partition in get_partitions([1,2,3]):
    print(partition)
Example:

Suppose the spaceship has a cargo weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The brute force algorithm will first try to fit them on only one trip, ["Jesse", "Maybel", "Callie", "Maggie"]. Since this trip contains 16 tons of cows, it is over the weight limit and does not work. Then the algorithm will try fitting them on all combinations of two trips. Suppose it first tries [["Jesse", "Maggie"], ["Maybel", "Callie"]]. This solution will be rejected because Jesse and Maggie together are over the weight limit and cannot be on the same trip. The algorithm will continue trying two trip partitions until it finds one that works, such as [["Jesse", "Callie"], ["Maybel", "Maggie"]].

The final result is then [["Jesse", "Callie"], ["Maybel", "Maggie"]]. Note that depending on which cow it tries first, the algorithm may find a different, optimal solution. Another optimal result could be [["Jesse", "Maybel"],["Callie", "Maggie"]].
"""

# NOT MY SOLUTIONS

# I didn't get to this problem set in time and wasn't able
# to use the automated grader. I'm saving these solutions to look through later

# SOLUTION 1:

def brute_force_cow_transport(cows, limit=10):
    ans = (len(cows) + 1) * ["X"]       # always longer than any possible ans
    for trial in get_partitions(cows.keys()):
        if len(trial) >= len(ans):      # if it's no shorter than ans, no more checks needed
            continue
        overload = False                # flag for ship over limit
        for ship in trial:
            load = sum([cows[cow] for cow in ship])
            if load > limit:
                overload = True
                break                   # one overload is one too many
        if not overload:
            ans = trial[:]              # new shortest answer
    return ans
  
# SOLUTION 2:

def brute_force_cow_transport(dict_of_cows, cargo_limit):

    #create list_cows, containing all names, for get_partitions helper function
    list_cows = list(dict_of_cows.keys())
    # create dict_cows as a copy of dict_of_cows, to look up weights quickly
    dict_cows = dict_of_cows.copy()

    # define valid_trip function
    def valid_trip(trip, dict_cows, cargo_limit):
        valid = True
        current_cargo = 0
        #iterate over each cow in trip
        for cow in trip:
            #add cow_weight only if current_cargo is less than cargo_limit
            if dict_cows[cow] > (cargo_limit - current_cargo):
                valid = False
                return(valid)
            else:
                current_cargo += dict_cows[cow]
        return(valid)

    # define valid partition
    def valid_partition(partition):
        #a partition is valid if all trips inside are valid
        valid = True
        for trip in partition:
            if not valid_trip(trip, dict_cows, cargo_limit):
                valid = False
                return(valid)
        return(valid)

    # maximum number of minimum_trips is when each cow is transported individually, len(list_cows)
    # can i find a better initialised value - waht would suit? i can assign it to first partition but output of generator function cannot be indexed
    minimum_trips = list_cows[:]

    #iterate through each partition generated by get_partitions
    #each partition is a list of lists 
    for partition in get_partitions(list_cows):

        #reassign minimum_trips if partition is valid and has smaller length than minimum_trips
        if valid_partition(partition) and len(minimum_trips) >= len(partition):
            minimum_trips = partition[:]

    return(minimum_trips)
  
# SOLUTION 3:

def brute_force_cow_transport(cows,limit=10):
    cow_names = cows.keys()
    best_length = len(cows)
    best_list = []
    for transport_list in (get_partitions(cow_names)):
        num_trips_in_list = len(transport_list)
        possible_best_list = True
        if num_trips_in_list > best_length:
            break
        else:
            trip_count = 0
            # check if every trip in the list is within the weight limit
            for trip in transport_list:
                if possible_best_list == False:
                    break
                else:
                    tripWeight = 0
                    for cow in trip:
                        weight = cows[cow]
                        if tripWeight + weight > limit:
                            possible_best_list = False
                            break
                        else:
                            tripWeight += weight
            if possible_best_list:
                best_list = transport_list
                best_length = num_trips_in_list
    return best_list

