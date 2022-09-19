my_str = "ERggggggggJrtyujhgfwerT$%^#$%&Y"

        ## Вариант решения №1 ##(без учета больших букв)

my_new_list_1 = [element for element in my_str if my_str.count(element) == 1]


        ## Вариант решения №2 ##(с учетом больших букв)

my_new_list_2 = [element for element in my_str if my_str.lower().count(element) == 1]

