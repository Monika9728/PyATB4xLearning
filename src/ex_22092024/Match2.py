user_type = input("User Type:")
user_type = user_type.upper()
match user_type:
    case "ADMIN":
        print("Hello Admin")
    case "GUEST":
        print("Hello Guest User")
    case _:
        print("Hello, There!")
