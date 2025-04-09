# Shortest Path Problem in the Paris Subway System

## Description

Imagine you're navigating the Paris Subway, one of the most intricate and dense subway networks in the world. Your goal is to travel from a starting station to a destination station using the shortest possible travel time, not necessarily the fewest stops.

## Problem Definition

Given:

- A graph representing the subway network, where:
    - Nodes are subway stations.
    - Edges represent direct train connections between stations.
    - Each edge is labeled with:
        - Travel time between connected stations.
        - Subway line identifier (e.g., Line 1, Line 4, RER A).

You need to:

Find the fastest route (i.e., with the least total time) from a start station S to a goal station G.

## Constraints and Considerations

- Transfers between lines (e.g., from Line 1 to Line 4) incur a time penalty, typically modeled as an additional transfer cost (e.g., 4 minutes).
- Heuristic: Use the straight-line (Euclidean) distance between stations (using their geographic coordinates) as an estimate of remaining time to the goal.
- Greedy strategy: Always choose the next station that appears closest to the goal based on the heuristic, even if it doesn’t lead to the global optimum.

## Greedy Algorithm with Heuristic

At each step:

1. From the current station, look at all reachable neighboring stations.
2. For each neighbor:
    - Add travel time.
    - If switching lines, add transfer penalty.
    - Estimate remaining time to goal using the straight-line distance.
3. Choose the neighbor with the lowest estimated remaining time and move forward.

Note: The greedy approach does not guarantee the optimal path, but can produce a fast approximate solution with lower computational cost than algorithms like Dijkstra or A*.

## Transfer Time Penalty Example

Let’s say you're at Châtelet, and you can:

- Continue on Line 1 to Hôtel de Ville (2 minutes),
- Or switch to Line 4 toward Les Halles (3 minutes travel + 4 minutes transfer penalty = 7 minutes).

Even if Les Halles is geographically closer to your goal, the transfer cost might make Hôtel de Ville the better choice, depending on the heuristic.

## Use Case

This greedy heuristic-based algorithm could be used in:

- Mobile subway apps for fast route suggestions.
- Emergency evacuation planning where real-time optimization is less critical than speed of decision.
- On-device navigation with limited processing power.
