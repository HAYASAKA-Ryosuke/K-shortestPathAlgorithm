
def find_cheapest_price(flights, src, dst):
    pq = [(0, src)]
    min_cost = {i: float('inf') for i in range(len(flights))}
    min_cost[src] = 0
    
    while pq:
        cost, city = pq.pop()
        if city == dst:
            return cost
        for f in flights:
            if f[0] == city:
                new_cost = cost + f[2]
                if new_cost < min_cost[f[1]]:
                    min_cost[f[1]] = new_cost
                    pq.append((new_cost, f[1],))
    return -1

# flights[i] = [fromi, toi, pricei]
flights = [
  [0, 1, 2],
  [0, 2, 4],
  [1, 3, 3],
  [1, 4, 7],
  [3, 4, 3],
  [2, 5, 2],
  [4, 5, 1],
  [4, 6, 2],
  [5, 6, 3],
]

# 都市0から都市5まで進む場合の最小値は6になる
print(find_cheapest_price(flights, 0, 5))
