class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        slowest = 0
        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd
            if time > slowest:
                fleets += 1
                slowest = time
        return fleets 