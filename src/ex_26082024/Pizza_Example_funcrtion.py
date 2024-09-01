def making_pizza(*toppings):
    for topping in toppings:
        print(topping)


monika_pizza = making_pizza("Onion", "Tomato")
vaanika_pizza = making_pizza("Onion", "Tomato", "corn")
manjeet_pizza = making_pizza("Onion", "Tomato", "corn", "panner")

#printing

print("Presesnting Monika Pizza:", monika_pizza)
print("Presesnting Vaanika Pizza:", vaanika_pizza)
print("Presesnting Manjeet Pizza:", manjeet_pizza)
