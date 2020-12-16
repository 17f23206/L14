print("hello this is times table tables")
times_table = 0
answer = 0
print("What times tables do u wish to see")
try:
    times_table = int(input())
except ValueError:
    print("You must enter a number, NOW")
    times_table = int(input())

print("please print your maximum times table here. Please")
max_value = int(input())
print(f"you will be tested on your {times_table} times tables")
for x in range(1,max_value + 1):
    answer = x * times_table
    print(f"{x} times {times_table} is:")
    print("answer:")
    user_answer = int(input())
    if user_answer == answer:
      print("Correct")
    else:
      print("incorrect")
