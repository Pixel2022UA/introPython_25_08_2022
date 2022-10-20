# TASK №1 ####################################################################

value = 30
new_value = value * 0.5 if value < 100 else -value

if value < 100:
    new_value = value * 0.5
else:
    new_value = -value

# TASK №2 ####################################################################

value = 30
new_value = 1 if value < 100 else 0

if value < 100:
    new_value = 1
else:
    new_value = 0

# TASK №3 ####################################################################

value = 30
new_value = True if value < 100 else False

if value < 100:
    new_value = True
else:
    new_value = False

# TASK №4 ####################################################################

my_str = "Lesson #4"
my_str = my_str * 2 if len(my_str) < 5 else my_str

if len(my_str) < 5:
    my_str = my_str * 2
else:
    my_str = my_str

# TASK №5 ####################################################################

my_str = "Lesson #4"
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str

if len(my_str) < 5:
    my_str = my_str + my_str[::-1]
else:
    my_str = my_str

# END ########################################################################