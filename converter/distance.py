# meters to feets
def meters_to_feets(meters:float)->float:
    return meters/0.3048

# feets to meters
def feets_to_meters(feets:float)->float:
    return feets * 0.3048

# modes = [MF, FM]
def convert(in_dist:float, mode:str)->float:
    match mode:
        case "FM":
            converted = feets_to_meters(in_dist)
        case "MF":
            converted = meters_to_feets(in_dist)
        case _:
            converted = in_dist
    return converted