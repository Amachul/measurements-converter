# Celsius to Fahrenheit
def celsius_to_farenheit(temp:float)->float:
    return 9 * temp / 5 + 32

# Fahrenheit to Celsius
def farenheit_to_celsius(temp:float)->float:
    return 5 * (temp - 32) / 9

# modes = [CF, FC]
def convert(in_temp:float, mode:str)->float:
    match mode:
        case "FC":
            converted = farenheit_to_celsius(in_temp)
        case "CF":
            converted = celsius_to_farenheit(in_temp)
        case _:
            converted = in_temp
    return converted