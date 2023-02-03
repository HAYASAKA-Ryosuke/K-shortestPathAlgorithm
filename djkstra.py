import heapq


def find_cheapest_price(flights, src, dst):
    pq = [(0, src)]
    min_cost = {}
    prevs = {}
    for flight in flights:
        min_cost[flight[0]] = float('inf')
        min_cost[flight[1]] = float('inf')
        prevs[flight[0]] = None
        prevs[flight[1]] = None

    min_cost[src] = 0
    
    while pq:
        cost, city = heapq.heappop(pq)
        if city == dst:
            return cost, prevs
        for flight in flights:
            if flight[0] == city:
                new_cost = cost + flight[2]
                if new_cost < min_cost[flight[1]]:
                    min_cost[flight[1]] = new_cost
                    heapq.heappush(pq, ((new_cost, flight[1],)))
                    prevs[flight[1]] = flight[0]
    return -1, prevs

def restore_route(src, dst, prevs):
    result = [dst]
    while True:
        dst = prevs[dst]
        result.append(dst)
        if dst == src:
            break
    return list(reversed(result))

# flights[i] = [fromi, toi, pricei]

flights = [
  ['a', 'b', 5],
  ['b', 'a', 5],
  ['a', 'c', 4],
  ['c', 'a', 4],
  ['a', 'd', 2],
  ['d', 'a', 2],
  ['b', 'c', 6],
  ['c', 'b', 6],
  ['b', 'e', 6],
  ['e', 'b', 6],
  ['b', 'h', 9],
  ['h', 'b', 9],
  ['c', 'e', 4],
  ['e', 'c', 4],
  ['c', 'd', 3],
  ['d', 'c', 3],
  ['d', 'e', 5],
  ['e', 'd', 5],
  ['d', 'f', 9],
  ['f', 'd', 9],
  ['e', 'h', 6],
  ['h', 'e', 6],
  ['e', 'f', 2],
  ['f', 'e', 2],
  ['f', 'h', 3],
  ['h', 'f', 3],
]


src = 'a'
dst = 'h'
# 都市aから都市hまで進む場合の最小値は12になる
cost, prevs = find_cheapest_price(flights, src, dst)


print(f'cost: {cost}, route: {restore_route(src, dst, prevs)}')
