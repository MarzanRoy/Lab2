def calculate_bmi (height, weight) :
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("BMI = " + str(bmi))
    if (bmi < 18.5) :
        print("You are Under Weight")
    elif (bmi >= 18.5 and bmi <= 25.0) :
        print("You are Normal Weight")
    else :
        print("You are Over Weight")

calculate_bmi(weight=58, height=1.70)