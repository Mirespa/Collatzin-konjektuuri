import matplotlib.pyplot as plt

# Collatz Conjecture Implementation
def collatz(x, steps):
  if x == 1:
    return steps
  if x % 2 == 0:
    return collatz(x//2,steps+1)
  else:
    return collatz(3*x+1,steps+1)

# Function to find the number with the maximum steps in the Collatz sequence
def find_max_collatz(limit):
    max_steps = 0
    number_with_max_steps = 0

    for i in range(1, limit + 1):
        steps = collatz(i, 0)
        if steps > max_steps:
            max_steps = steps
            number_with_max_steps = i

    return number_with_max_steps, max_steps

# Main execution
limit = 500
result_number, result_steps = find_max_collatz(limit)
print(f"Number with max steps: {result_number}, Steps: {result_steps}")

# Plotting
x_values = list(range(1, limit + 1))
y_values = [collatz(i, 0) for i in x_values]

plt.plot(x_values, y_values, marker='o')
plt.title("Collatz Conjecture Steps")
plt.xlabel("Number")
plt.ylabel("Steps to reach 1")
plt.grid()
plt.show()