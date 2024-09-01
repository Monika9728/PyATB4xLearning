def making_pizza(*toppings, base):
    for topping in toppings:
        print(topping, base)


monika_pizza = making_pizza("Onion", "Tomato", base="Wheat")
vaanika_pizza = making_pizza("Onion", "Tomato", "corn", base="Wheat")
print("Presesnting Monika Pizza:", monika_pizza)
print("Presesnting Vaanika Pizza:", vaanika_pizza)
