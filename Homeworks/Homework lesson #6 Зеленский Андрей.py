## TASK №1 ######################################################

my_list = [45, 30, 58, 120, 78, 168, -40, -160, 0, 3]
for number in my_list:
    if number > 100:
        print(number)

## TASK №2 ######################################################
my_list = [45, 30, 58, 120, 78, 168, -40, -160, 0, 3]
my_results = []
for number in my_list:
    if number > 100:
        my_results.append(number)
print(my_results)

## TASK №3 ######################################################

my_list = [45, 30, 58, 120, 78, 168, -40, -160, 0, 3]
if len(my_list) < 2:
    my_list.append(0)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])