class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Direction map for each step
        direction_map = {
            'N': (1, 0),
            'S': (-1, 0),
            'E': (0, 1),
            'W': (0, -1)
        }

        # Initial position and log of visited coordinates
        coords = [0, 0]
        log_file = {tuple(coords)}

        # Traverse each step in path
        for step in path:
            dx, dy = direction_map[step]
            coords[0] += dx
            coords[1] += dy

            # Check if the new position has been visited
            if tuple(coords) in log_file:
                return True
            log_file.add(tuple(coords))

        return False

# 1. Why Use Tuples Instead of Lists for Sets?
# Immutability of Tuples

#     Sets in Python require hashable elements, meaning the elements need to be immutable (unchangeable). This is because sets use hashing to quickly check for the existence of elements.
#     Tuples are immutable, meaning once a tuple is created, its contents cannot be changed. This makes them hashable and suitable for use as elements in a set.
#     Lists, on the other hand, are mutable (their contents can be modified), which means they are not hashable. Since a set requires its elements to be hashable, you cannot use a list as an element in a set.

# 2. Why Use Tuples Instead of Lists for Hashmaps (Dictionaries)?
# Tuples as Keys

#     Dictionary keys must also be hashable. Just like with sets, mutable objects (like lists) cannot be used as dictionary keys because they are not hashable.
#     Tuples are immutable and therefore hashable, making them suitable for use as dictionary keys.
#     Lists are mutable and cannot be used as keys in dictionaries because their hash value could change if their contents change. This would break the integrity of the dictionary's hash table.


# Converting coords to a Tuple:

#     tuple(coords) creates a new tuple from the current state of the coords list. This tuple is a new object, independent of the original coords list.
#     This conversion is done on-the-fly, meaning it doesn't modify the original coords list. Instead, it creates a new tuple with the same values that were in coords at that moment.

# Check in the Set:

#     The newly created tuple (which is immutable) is checked against the log_file set to see if this particular coordinate has been visited before.

# Original List (coords) Stays the Same:

#     The original coords list is not modified by this conversion. It still holds the same values it had before the tuple(coords) was created.
#     tuple(coords) does not change coords; it simply takes a snapshot of the list at that point and creates an immutable version of it for use in the set.