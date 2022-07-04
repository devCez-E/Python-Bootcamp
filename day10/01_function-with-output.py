#def my_function(something):
    #Do this with something
    #Then do this
    #Finally do this

#def my_function():
    #result = 3 * 2
    #return result

def format_name(f_name, l_name):
    if f_name =="" or l_name== "":
        return "You didn't provide valid inputs."

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    #print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"

format_string = format_name("cezanne", "CEZANNE")
print(format_string)

format_string = format_name("", "CEZANNE")
print(format_string)

print(format_name(input("What is your first name? "), input("What is your last name? ")))