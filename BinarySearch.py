# Authorized By Danial Sanjabi
# BinarySearch O(nlogn) numbers betwenn 1 to 100000 runs very fast ! (less then 1 seconds...)

import time
start_time = time.time()

def calculate_influence_power_simple(heights):
    if not heights:
        return [], 0

    influence_powers = []
    sorted_heights = []
    total_influence_power = 0
    # [2,5,3,4,7,2,1]
    # ip = [0,1,2,2,...]
    # sh = [1,2,4,7,...]
    for height in reversed(heights): # O(n)
        low = 0
        high = len(sorted_heights)
        while low < high: # O(logn)
            mid = (low + high) // 2
            if sorted_heights[mid] < height: 
                low = mid + 1  
            else:
                high = mid
        pos = low  # or pos = high
        influence_powers.append(pos)
        total_influence_power += pos
        sorted_heights.insert(pos, height)

    influence_powers.reverse()
    return influence_powers, total_influence_power

file_name = "ENTER-YOUR-TXT-PATH"
with open(file_name, 'r') as file:
    n = int(file.readline().strip())
    heights = list(map(int, file.readline().split()))

if n == len(heights):
    influence_powers, total_power = calculate_influence_power_simple(heights)
    print(' '.join(map(str, influence_powers)))
    print(total_power)
else:
    print('n : ', n,end=" | ")
    print('len of heights : ', len(heights))
    print('ERROR => must n == len(heights) and 1 <= n <= 100000')

end_time = time.time()
print("Runtime:", end_time - start_time, "seconds")