def collatz(x, steps):
  if x == 1:
    return steps
  if x % 2 == 0:
    return collatz(x//2,steps+1)
  else:
    return collatz(3*x+1,steps+1)

def find_max_collatz(limit):
    max_steps = 0
    number_with_max_steps = 0

    for i in range(1, limit + 1):
        steps = collatz(i, 0)
        if steps > max_steps:
            max_steps = steps
            number_with_max_steps = i

    return number_with_max_steps, max_steps

result_number, result_steps = find_max_collatz(500)
print(result_number, result_steps)