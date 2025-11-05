import numpy as np

def aco_tsp(distance_matrix, num_ants=10, alpha=1, beta=2, rho=0.5, iterations=100):
    n = len(distance_matrix)
    pheromone = np.ones((n, n))
    visibility = 1 / (distance_matrix + np.eye(n))  # avoid div by 0
    
    best_route = None
    best_length = float('inf')
    
    for it in range(iterations):
        routes = []
        lengths = []
        
        for ant in range(num_ants):
            unvisited = list(range(n))
            start = np.random.choice(unvisited)
            route = [start]
            unvisited.remove(start)
            
            while unvisited:
                i = route[-1]
                prob = []
                for j in unvisited:
                    tau = pheromone[i][j] ** alpha
                    eta = visibility[i][j] ** beta
                    prob.append(tau * eta)
                prob = np.array(prob) / sum(prob)
                next_city = np.random.choice(unvisited, p=prob)
                route.append(next_city)
                unvisited.remove(next_city)
            
            length = sum(distance_matrix[route[i]][route[i+1]] for i in range(n-1)) + distance_matrix[route[-1]][route[0]]
            routes.append(route)
            lengths.append(length)
            
            if length < best_length:
                best_length = length
                best_route = route
        
        # Update pheromones
        pheromone *= (1 - rho)
        for r, l in zip(routes, lengths):
            for i in range(n-1):
                pheromone[r[i]][r[i+1]] += 1 / l
            pheromone[r[-1]][r[0]] += 1 / l  # return to depot
    
    return best_route, best_length

# Example usage
distance_matrix = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])
route, length = aco_tsp(distance_matrix)
print("Best route:", route)
print("Total distance:", length)
