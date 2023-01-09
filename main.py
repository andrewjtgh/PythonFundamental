# Programming Fundamentals with Python
print("Hello World")


def hello(name):
  greet = "Hi! " + name
  print(greet)
  print(type(greet))


hello("Jonathan")


# Functions
def score(total, correct, wrong):
  print(type(correct))
  return (correct * 2 + wrong) / total / 2 * 100


score(20, 20, 0)

# > score(20, 20, 0)
# 100.0 # because you got perfect score
# > score(20, 15, 0)
# 75.0 # Because you got 75% of them correct and you didn’t show up to the
# 25%
# > score(20, 15, 5) # ( 15 * 2 + 5 * 1 ) / (20 * 2)
# 87.5
# > score(20, 10, 5)
# 62.5
# > score(20, 0, 20)
# 50.0


def score75(total, correct, wrong):
  return ( (min(
    30, 2 * correct) ) +\
        (min (
          max(15 - correct, 0) \
          , wrong) ) ) / 30 * 100


# rint(min(-15,0))
print(score75(20, 20, 0))
print(score75(20, 15, 0))
print(score75(20, 15, 5))
print(score75(20, 10, 5))
print(score75(20, 0, 20))

# > score75(20, 20, 0)
# 100.0 # because you got a perfect score
# > score75(20, 15, 0)
# 100.0 # because you got 75% of the questions correctly, even if you didn't
# show up for 5
# > score75(20, 15, 5) # again we only take your top 75%
# 100.0
# > score75(20, 10, 5)
# 83.33333333333334
# > score75(20, 0, 20)
# 50.0


# Control Flow
def eat_apples(num_of_apples, on_diet):
  apples_remaining = num_of_apples
  while apples_remaining > 0 and not on_diet:
    apples_remaining -= 1
    print("Thank you!")
  print("Done")
  return


eat_apples(5, False)

# Lists
num1 = 2
num2 = 5
num3 = 14
num4 = 17
num5 = 20
num6 = 35

nums = [2, 5, 14, 17, 20, 35]

print(nums)
print(type(nums))
print(nums[-3])
print(nums[1:4])
print(nums.append(4))
print(nums)
print(nums.insert(1, 4))
print(nums)
print(nums.pop(7))
print(nums)
print(len(nums))
nums.insert(len(nums), 4)
print(nums)

# Return the same list, but all numbers squared


def square_list(nums):
  i = 0
  while i < len(nums):
    nums[i] = nums[i] * nums[i]
    i += 1
  return nums


# Return the sum of all the numbers in the list
def sum_list(nums):
  total = 0
  i = 0
  while i < len(nums):
    total += nums[i]
    i += 1
  return total


# Loops
flavours = ["vanilla", "strawberry", "chocolate", "mint", "banana", "rubber"]

print("While Loop Time")
print("===============")
i = 0
while i < len(flavours):
  print(flavours[i])
  i += 1

print("===============")
print("For Loop Time")
print("===============")
for flavour in flavours:
  print(flavour)

print("===============")
print("Price stuff")
print("===============")
price = [4, 5, 6, 7, 10, 20]
sum_prices = 0
i = 0
while sum_prices < 10:
  sum_prices += price[i]
  i += 1
print(sum_prices)
print(i)

print(list(range(4)))
print(list(range(0, 4, 1)))
print(type(range(4)))
print(range(1000))

for a in range(4):
  print(a)

#####
i = 0
while i < 4:
  print(i)
  i += 1

#####
for a in [0, 1, 2, 3]:
  print(a)


# break and continue
def has_even_number(lst):
  has_even = False
  for num in lst:
    print("Now looking at " + str(num))
    if num % 2 == 0:
      has_even = True
      break
    print("has_even: " + str(has_even))
  return has_even


def receive_tips(tips):
  total_tips = 0
  for tip in tips:
    total_tips += tip
    if tip < 5:
      continue
    print("Thanks for $" + str(tip))
  return total_tips


for i in [1, 2, 3]:
  for j in [4, 5, 6]:
    for k in [7, 8, 9]:
      print(str(i) + "-" + str(j) + "-" + str(k))


def print_pyramid(n):
  for i in range(n):
    line_to_print = "o"
    for j in range(i):
      line_to_print += "o"
    print(line_to_print)
  return


# Matrices

matrix = [[1, 2, 8], [3, 4, 3], [5, 6, 6]]

def print_matrix(m):
  if m == []:
    print("Empty Matrix")
    return
  num_rows = len(m)
  num_cols = len(m[0])
  # pint(num_rows)
  # print(num_cols)
  for row in m:
    line_to_print = ""
    for num in row:
      line_to_print += str(num) + " "
    print(line_to_print)
  return

print_matrix(matrix)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def create_matrix(m, n):
  my_matrix = []
  for i in range(m):
    my_row = []
    for j in range(n):
      my_row.append(0)
    my_matrix.append(my_row)
  return my_matrix


# print(create_matrix(3,4))


def add_matrices(m1, m2):
  if m1 == [] or m2 == []:
    return []
  if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    return []  # not same size
  num_rows = len(m1)
  num_cols = len(m1[0])
  m0 = create_matrix(num_rows, num_cols)
  for i in range(num_rows):
    for j in range(num_cols):
      m0[i][j] = m1[i][j] + m2[i][j]
  return m0


print_matrix(add_matrices(matrix, matrix))

# Recursion


def func_r(a):
  print("Start: " + str(a))
  if a == 0:
    res = 0
  else:
    res = func_r(a - 1) + 1
  print("End: " + str(a))
  return res


func_r(3)

# Recursion: Fibonacci


def fib(n):
  # base case
  if n == 0:
    return 0
  elif n == 1:
    return 1

  # recursive case
  else:
    return fib(n - 1) + fib(n - 2)


for i in range(20):
  print(fib(i))

# Recursion: practice


def reverse(str):
  # base case
  if len(str) < 2:
    return str
  #recursive case
  else:
    return reverse(str[1:]) + str[0]


print(reverse("Jonathan is a teacher"))


# print_list([1,2,3])
# 1
# 2
# 3
def print_list(lst):
  if not lst:
    return
  else:
    print(lst[0])
    print_list(lst[1:])


print_list([1, 2, 3, 4, 5, 6, 7])


def is_in_list(n, lst):
  # base case
  if not lst:
    return False
  # recursive case
  else:
    return lst[0] == n or is_in_list(n, lst[1:])


print(is_in_list(5, [1, 2, 3, 4, 5]))

print(3 in [1, 2, 3, 4])

# backtracking

maze = [[".", ".", ".", ".", ".", "x", ".", "."],
        [".", "x", "x", "x", ".", "x", ".", "."],
        [".", ".", ".", "x", ".", ".", ".", "."],
        [".", "x", ".", "x", ".", "x", "x", "x"],
        [".", "x", ".", "x", ".", "x", ".", "."],
        [".", "x", ".", "x", ".", "x", ".", "."],
        [".", "x", ".", "x", "x", "x", ".", "."],
        [".", "x", ".", ".", ".", ".", ".", "."]]


def print_maze(maze):
  for row in maze:
    row_print = ""
    for value in row:
      row_print += value + " "
    print(row_print)


print_maze(maze)


def solve_maze(maze):
  if len(maze) < 1:
    return None
  if len(maze[0]) < 1:
    return None
  return solve_maze_helper(maze, [], 0, 0)


def solve_maze_helper(maze, sol, pos_row, pos_col):
  # Get size of the maze
  num_row = len(maze)
  num_col = len(maze[0])

  # Base Cases

  # Robot is already home
  if pos_row == num_row - 1 and pos_col == num_col - 1:
    return sol

  # Out of bounds
  if pos_row >= num_row or pos_col >= num_col:
    return None
  # Is on an obstacle
  if maze[pos_row][pos_col] == 'x':
    return None

  # Recursive Cases

  # Try going right
  sol.append("r")
  sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col + 1)
  if sol_going_right is not None:
    return sol_going_right

  # Going right doesn't work, Backtrack, try going down

  sol.pop()
  sol.append("d")
  sol_going_down = solve_maze_helper(maze, sol, pos_row + 1, pos_col)
  if sol_going_down is not None:
    return sol_going_down

  # No solution, impossible, Backtrack
  sol.pop()
  return None


print(solve_maze(maze))
