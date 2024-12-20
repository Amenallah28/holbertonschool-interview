#!/usr/bin/python3
""" Method to determine if all boxes are unlockable or not. """


def canUnlockAll(boxes):
    """ Code to check if all boxes can be unlocked """
    unlocked = [0]
    keys = boxes[0]

    while keys:
        new_key = keys.pop()

        if new_key not in unlocked and new_key < len(boxes):
            unlocked.append(new_key)
            keys.extend(boxes[new_key])

    return len(unlocked) == len(boxes)
