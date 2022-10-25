def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduciton to Python")
    display_main_menu()
    num_list = get_user_input()

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
#    for i in range(0, len(list)):
#        list[i] = float(list[i])
#        print(i)
#    print(list)

def calc_average():
    print("calc_average")

if (__name__ == "__main__"):
    main()