
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Invalid input" # Return 1
    formated_f_name = f_name.title()
    formated_l_name =  l_name.title()

    return f"{formated_f_name} {formated_l_name}" # Return 2

print(format_name("john", "LEMON"))