# Lattice Paths

Starting the top left corner of 2 x 2 grid, and only being able to move right and down,
there are exactly 6 routes to the bottom right corner.

![Lattice Paths 2 x 2 Grid](https://raw.githubusercontent.com/alv2017/ProjectEuler/main/Images/LatticePaths/lattice_paths_routes.gif)

## Hacker Rank: 

https://www.hackerrank.com/contests/projecteuler/challenges/euler015/problem/

## Limitations

- 1 <= N <= 500
- 1 <= M <= 500

## Task

How many such routes are there through a N x M grid?

## Solution Idea

In order to travel from the upper left corner to the lower right corner through the M x N grid 
moving only down and right, we need to make M steps down and N steps to the right. All in all we 
need to find all possible combinations of M down steps and N right steps in the M+N step sequence:

$$ C_{M+N}^N = \frac{(M+N)!}{M!N!} $$


