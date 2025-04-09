import heapq

# Estado objetivo
goal_state = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))  # 0 representa o espaço vazio

# Direções possíveis: cima, baixo, esquerda, direita
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan(state):
    """Calcula a distância de Manhattan para o estado atual"""
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = (val - 1) // 3, (val - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def find_zero(state):
    """Encontra a posição do espaço vazio (0)"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def swap(state, i1, j1, i2, j2):
    """Retorna novo estado após trocar duas posições"""
    new_state = [list(row) for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return tuple(tuple(row) for row in new_state)

def reconstruct_path(came_from, current):
    """Reconstrói o caminho do início até o objetivo"""
    path = []
    while current:
        path.append(current)
        current = came_from.get(current)
    return path[::-1]

def a_star(start_state):
    frontier = []
    heapq.heappush(frontier, (manhattan(start_state), 0, start_state))
    came_from = {start_state: None}
    cost_so_far = {start_state: 0}

    while frontier:
        _, cost, current = heapq.heappop(frontier)

        if current == goal_state:
            return reconstruct_path(came_from, current)

        zero_i, zero_j = find_zero(current)

        for di, dj in directions:
            ni, nj = zero_i + di, zero_j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                next_state = swap(current, zero_i, zero_j, ni, nj)
                new_cost = cost + 1
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    priority = new_cost + manhattan(next_state)
                    heapq.heappush(frontier, (priority, new_cost, next_state))
                    came_from[next_state] = current

    return None  # Sem solução

# Exemplo de uso:
start = ((0, 6, 3),
         (7, 2, 1),
         (4, 5, 8))

goal = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

path = a_star(start)

if path:
    print("Solução encontrada em", len(path) - 1, "movimentos.")
    for state in path:
        for row in state:
            print(row)
        print("--------")
else:
    print("Sem solução.")
