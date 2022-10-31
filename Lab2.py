def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduciton to Python")
    display_main_menu()
    num_list = get_user_input()

    print(calc_average(num_list))
    print(find_min_max(num_list))
    print(sort_temperature(num_list))
    print(calc_median_temperature(num_list))

def display_main_menu():
    print("Enter some number seperated by commas (e.g. 5, 67, 32, ...)")

def get_user_input():
    user_input = input()
    num_list = list()
    input_list = user_input.split(",")
    for items in input_list:
        num_list.append(float(items.strip()))
    #print(input_list)
    #print (num_list)
    return (num_list)

#def get_user_input():
#    list = input().split(",")

#   list = [eval(i) for i in list] #another way

#    for i in range(0, len(list)):
#        list[i] = float(list[i])
#        print(i)
#    print(list)
#    return list

def calc_average(num_list):
    #print("calc_average")
    total = 0
    for items in num_list:
        total += items

    #for i in range(0, len(num_list)):
    #    total += num_list[i]

    return (total / len(num_list))

def find_min_max(num_list):
    min = max = num_list[0]
    for items in num_list:
        min = min if (min < items) else items
        max = max if (max > items) else items
    return ([min, max])

def sort_temperature(num_list):
    num_list.sort()
    return(num_list)

def calc_median_temperature(num_list):
    length = len(num_list)
    num_list = sort_temperature(num_list)

    if length % 2 == 0:
        median1 = num_list[length // 2]
        median2 = num_list[length // 2 - 1]
        return ((median1 + median2) / 2)
    else:
        return (num_list[length // 2])

if (__name__ == "__main__"):
    main()