weather="sunny"
time="night"
if weather=="sunny":
    if time=="day":
        print("play with car")
    else:
        print("it's night go and sleep")
elif weather=="rainy":
    print("play with boat")
elif weather=="snowy":
    if time=="night":
        print("play with teddy bear")
    else:
        print("stay home...it's sunny")

else:
    print("stay inside and read book")