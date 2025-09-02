temperature = int(input("Enter the temperature in Celsius: "))

if 30 <= temperature < 55:
    print("It's a hot day! Stay hydrated, a7la darbt shams 3lek ya sa7by.")
elif 20 <= temperature < 30:
    print("It's a warm day. Enjoy the nice weather!, el donya rabe3 el gaw bde3 ")
elif 10 <= temperature < 20:
    print("It's a cold day. Grab a jacket and some hot coffee!, eh el talg da ya 3m")
elif temperature <= 10:
    print("It's very cold. Stay warm!, hwa el 8seel mblol wa 3aml nafso bared wla el 8seel bared wa 3aml nafso mblol")
else :
    print ("Invalid temperature input.")
