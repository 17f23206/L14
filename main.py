times_table = 0
answer = 0
print("What times tables so u wish to see")
times_table = input()
print(f"Here is the {times_table} times table")
for x in range(1,13):
    answer = x * times_table
    print(f"{x} times {times_table} is {answer}")
