"""
One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. This is an example of a greedy algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons and another that's 1 ton, the 1 ton cow will get put onto the spaceship.

Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

Note: Make sure not to mutate the dictionary of cows that is passed in!

Assumptions:

The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips.
All the cows are between 0 and 100 tons in weight.
All the cows have unique names.
If multiple cows weigh the same amount, break ties arbitrarily.
The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.
Example:

Suppose the spaceship has a weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The greedy algorithm will first pick Jesse as the heaviest cow for the first trip. There is still space for 4 tons on the trip. Since Maggie will not fit on this trip, the greedy algorithm picks Maybel, the heaviest cow that will still fit. Now there is only 1 ton of space left, and none of the cows can fit in that space, so the first trip is [Jesse, Maybel].

For the second trip, the greedy algorithm first picks Maggie as the heaviest remaining cow, and then picks Callie as the last cow. Since they will both fit, this makes the second trip [[Maggie], [Callie]].

The final result then is [["Jesse", "Maybel"], ["Maggie", "Callie"]].
"""

# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # create an empty list to return
    cow_list = []
    
    # create a copy of the dictionary to mutate as needed
    cows_copy = cows.copy()
    
    # created a sorted list of tuples sorted by highest value (weight) first
    sorted_cows = sorted(cows_copy.items(), key = lambda x: x[1], reverse = True)
    
    # initialize a while loop that will continue while there are still values
    # in the copied dictionary that aren't zero
    while sum(cows_copy.values()) > 0:
      
        # create an empty list to store in cow_list
        list_of_list = []
        # initialize a variable to keep track of the total weight of cows so far
        total_weight = 0
        # for each cow in sorted_cows
        for cow, weight in sorted_cows:
            # if the cow's weight is zero and the limit hasn't been reached
            if cows_copy != 0 and weight + total_weight <= limit:
                # add the cow to the list
                list_of_list.append(cow)
                # add its weight to total weight
                total_weight += weight
                # subtract its weight (value) from the dictionary
                cows_copy[cow] = 0
        # add list_of_list to cow_list
        cow_list.append(list_of_list)
    
    # return the list of lists
    return cow_list

 # CORRECT
 
 # below is the code I initially made to help me work through the problem
 # it didn't take long for me to realize I needed to start from scratch
 # creating a copy of the dict and subtracting cows from it as needed as
 # well as sorting the cows by weight vastly improved my code.
  
    """
    for k in cows:
        cow_trip = []
        l = limit
        if cows.get(k) > l:
            cow_list.append(cow_trip)
        elif cows.get(k) == limit:
            cow_trip.append(k)
            cow_list.append(cow_trip)
        else:
            cow_list.append(k)
            l = l - cows.get(k)
            """
 # INCORRECT
