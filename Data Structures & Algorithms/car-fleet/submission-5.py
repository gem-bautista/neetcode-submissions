class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speed = []
        stack = []

        for i in range(len(position)):
            pos_and_speed.append([position[i], speed[i]])

        sorted_cars = sorted(pos_and_speed)[::-1]

        for ind, value in enumerate(sorted_cars):
            cur_p, cur_v = value
            cur_time = (target - cur_p) / cur_v

            if stack and cur_time <= stack[-1]:
                continue
            else:
                stack.append(cur_time)

        return len(stack)