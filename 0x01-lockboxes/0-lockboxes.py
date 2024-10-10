#!/usr/bin/python3
"""
Solution is
"""


def can_unlock_all(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    unlocked = set()  # To keep track of unlocked boxes
    to_unlock = [0]   # Start with box 0, which is unlocked

    while to_unlock:  # While there are boxes to unlock
        box = to_unlock.pop()  # Get a box to unlock
        if box not in unlocked:  # Check if it's already unlocked
            unlocked.add(box)  # Mark it as unlocked
            for key in boxes[box]:  # Use keys in this box
                if key not in unlocked and key < len(boxes):
                    to_unlock.append(key)  # Add it to the list to unlock later

    return len(unlocked) == len(boxes)  # Check if all boxes are unlocked

