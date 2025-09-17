# https://leetcode.com/problems/car-pooling/description/
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # Sweep lines
        locations = [0] * 1001  # Max distance in km travelled is 0 to 1000
        # Notice we iterate through the LOCATIONS rather than the trips since it is a much SMALLER number (1001)

        # An array of what are the PASSENGER NUMBER CHANGES as we go on our journey
        for stop in trips:
            passengers = stop[0]
            start_dist = stop[1]
            end_dist = stop[2]
            locations[start_dist] += passengers
            locations[end_dist] -= passengers

        for passengers in locations:
            capacity -= (
                passengers  # (-ve passengers at end_dist points will free up space)
            )
            if capacity < 0:
                return False  # We ran out of capacity!

        return True
