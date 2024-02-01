import heapq

def merge_cables(cables):
    heapq.heapify(cables)
    total_cost = 0
    connection_order = [] 

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        connection_cost = cable1 + cable2
        total_cost += connection_cost

        heapq.heappush(cables, connection_cost)
        connection_order.append((cable1, cable2)) 
    return total_cost, connection_order

def main():
    cables = [10, 5, 7, 15, 30, 20, 1]
    total_costs, order = merge_cables(cables)

    print(f"Minimum total costs for merging cables: {total_costs}")
    print("Connection order:")
    for pair in order:
        print(pair)

if __name__ == "__main__":
    main()

