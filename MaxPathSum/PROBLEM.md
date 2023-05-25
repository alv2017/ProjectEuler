# Maximum Path Sum 1

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the max total from top to bottom is 23:

```
3
7 4
2 4 6
8 5 9 3
```

Max_Path_Sum = 3 + 7 + 4 + 9 = 23

Find the maximum total from top to bottom of the triangle given in input.

## Hacker Rank: 

https://www.hackerrank.com/contests/projecteuler/challenges/euler018/

## Solution Idea

Step 1: We will create a triangle class

Step 2: We will add the method .max_total_sum() that returns the required result.

## Calculation Algorithm

**Step 1:**

Start from the bottom row and calculate the adjacent sums.

Bottom row is (8, 5, 9, 3). 

Adjacent maximum calculation: 

m1 = max(8, 5) = 8

m2 = max(5, 9) = 9

m3 = max(9, 3) = 9

Calculated adjacent maximums (8, 9, 9)


**Step 2:**

Add adjacent maximums to the values of the subsequent row.

Subsequent row: (2, 4, 6)

Adj. maximums added to the values of the row: (10, 13, 15)

Repeat Step 1.

Adjacent maximums calculation:

m1 = max(10, 13) = 13

m2 = max(13, 15) = 15

Adjacent maximums: (13, 15)


**Next Steps:**

Repeat step 2 till the top of the triangle is reached. The result you will get at the top of the triangle is the 
required max total sum.


**Step 3:**

Subsequent row: (7, 4)

Adjacent maximums added to the values of the row: (20, 19)

Adjacent maximums: (20)


**Step 4:**

Top row: (3)

Adjacent maximum added to the value of the top row: 23


**Max. Total Sum is 23.**