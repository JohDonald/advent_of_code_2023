import sys
input = open(sys.argv[1]).read().split('\n') 
input = [[int(t) for t in l.split(':')[1].strip().split()] for l in input] 
input_p2 = [[int(''.join(str(e) for e in l))] for l in input] 
time, distance = input
time_p2, distance_p2 = input_p2 

def count_wins(max_hold_t, t, d): 
    l = r = max_hold_t 
    while l >= 0 and (l * (t - l)) > d: l -= 1 
    while r < t and (r * (t - r)) > d: r += 1 
    return (r - 1) - (l + 1) + 1 

def ways_to_win_product(time, distance):
    product_ways_to_win = 1 
    for i in range(len(time)): 
        t = time[i] 
        d = distance[i] 
        max_hold_t = round(t/2) 
        max_dist = max_hold_t * (t - max_hold_t) 
        if max_dist > d: 
            product_ways_to_win *= count_wins(max_hold_t, t, d)
    return product_ways_to_win 

print("Part 1: " + str(ways_to_win_product(time, distance)))
print("Part 2: " + str(ways_to_win_product(time_p2, distance_p2)))
