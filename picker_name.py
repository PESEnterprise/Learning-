names = ["Angela", "Sam", "Ben", "Emma"]
import random
random_num = len(names)
random_names = random.randint(0, random_num - 1)
pay = names[random_names]
print(f"{pay} is going to buy the meal today!")