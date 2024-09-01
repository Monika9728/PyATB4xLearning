# match statement
# switch in java
# match the o/p and execute
# only works if Python > 3.10

# syntax

# match variable:
#     case pattern 1:
#         code block
#     case pattern 2:
#         code block

# write a program to ask the browser name he want to run automation

browser_name = input("Enter the browser name: ")
browser_name=browser_name.lower()
match browser_name:
    case "google chrome":
        print("You are using Google Chrome ")
    case "mozilla firefox":
        print("You are using Mozilla Firefox ")
    case "internet explorer":
        print("You are using Internet Explorer ")
    case "safari":
        print("You are using Safari ")
    case _:
        print("Browser not found")
