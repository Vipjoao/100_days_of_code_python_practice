
def format_name(f_name, l_name):
    """Takes your first and last name, combines and
    formats them into title case version of that name."""
    if f_name == "" or l_name == "":
        return "Invalid input" # Return 1
    formated_f_name = f_name.title()
    formated_l_name =  l_name.title()

    return f"{formated_f_name} {formated_l_name}" # Return 2

print(format_name("john", "LEMON"))