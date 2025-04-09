# Problem

## Description

The 8-puzzle is a classic problem in artificial intelligence and search algorithms. It consists of a 3x3 grid containing 8 numbered tiles and one empty space. The tiles are numbered from 1 to 8, and the empty space is typically represented by 0 or a blank.

<img src="img/puzzle.png" width="400"/>

## Objective

The goal is to rearrange the tiles by sliding them into the empty space, one move at a time, to reach a predefined goal state.

You can only move tiles that are adjacent (up, down, left, right) to the empty space.

## Actions

- Move up
- Move down
- Move left
- Move right

Each move swaps the blank space with a neighboring tile.

## Search Problem Definition

- **State**: a configuration of the 3x3 board.
- **Initial state**: any valid arrangement of the tiles.
- **Goal state**: the ordered configuration.
- **Actions**: slide a tile into the empty space.
- **Path cost**: usually 1 per move.
- **Solution**: a sequence of moves that transforms the initial state into the goal state.

## Algorithms Commonly Used

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search (with heuristics like Manhattan distance or misplaced tiles)
- Greedy Best-First Search
