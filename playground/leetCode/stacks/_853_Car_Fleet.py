"""
There are n cars going to the same destination along a one-lane road.
The destination is target miles away.

You are given two integer array position and speed, both of length n,
where position[i] is the position of the ith car and speed[i] is the
speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and
drive bumper to bumper at the same speed. The faster car will slow down to
match the slower car's speed. The distance between these two cars is
ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and
same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still
be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.


Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.


Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106

"""

from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    new_pair = []  # sorted_arr = [(0 , 1), (3 , 3), (5 , 1), (8 , 4), (10 , 2)]

    for i in range(len(position)):
        new_pair.append((position[i], speed[i]))

    new_pair.sort()
    new_pair.reverse()

    stack = []

    for p, s in new_pair:
        arrival_time = (target - p) / s
        stack.append(arrival_time)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


def carFleet2(target: int, position: List[int], speed: List[int]) -> int:
    ps = {}

    for i in range(len(position)):
        ps[position[i]] = speed[i]

    position.sort()

    stack = []

    j = len(position) - 1
    while j >= 0:
        arrival_time = (target - position[j]) / ps[position[j]]
        stack.append(arrival_time)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
        j -= 1

    return len(stack)


if __name__ == '__main__':
    # position = [10, 8, 0, 5, 3];
    # speed =    [ 2, 4, 1, 1, 3];

    # sorted_arr = [(0 , 1), (3 , 3), (5 , 1), (8 , 4), (10 , 2)]

    #     12 - 10 / 2 =  1
    #     12 -  8 / 4 =  1
    #     12 -  5 / 1 =  7
    #     12 -  3 / 3 =  3
    #     12 -  0 / 1 = 12

    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    target = 12  # destination

    result = carFleet2(target, position, speed)
    print(result)
