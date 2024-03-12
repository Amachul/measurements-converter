from converter import temperature
from converter import distance

DEGREE = 'Â°'

def get_digit_from_str(in_str:str)->str:
    res = ''
    for i in in_str:
        if i.isdigit() or i == '.':
            res = res + i
    return res

# [{"date":date, "temperature":temp, "system":'°C'\'°F'}]
def read_csv(file_name:str) -> list:
    content = []
    with open(f'{file_name}.csv', 'r') as file:
        file.readline()
        for line in file.readlines():
            item = line.strip().split(',')
            content.append(dict(Date=item[0], Distance=get_digit_from_str(item[1]), Temperature=get_digit_from_str(item[2]), Tem_Sys='C' if item[2].find("C")>0 else 'F', Dis_Sys='m' if item[1].find("m")>0 else 'ft'))
    return content

def convert_distance(input_:list, mode:str):
    for item in input_:
        temp_ = item['Distance']
        match mode:
            case "FM":
                if item['Dis_Sys'] == 'ft':
                    item['Distance'] = distance.feets_to_meters(float(temp_))
                    item['Dis_Sys'] = 'm'
            case "MF":
                if item['Dis_Sys'] == 'm':
                    item['Distance'] = distance.meters_to_feets(float(temp_))
                    item['Tem_Sys'] = 'ft'

def convert_temperature(input_:list, mode:str):
    for item in input_:
        temp_ = item['Temperature']
        match mode:
            case "FC":
                if item['Tem_Sys'] == 'F':
                    item['Temperature'] = temperature.farenheit_to_celsius(float(temp_))
                    item['Tem_Sys'] = 'C'
            case "CF":
                if item['Tem_Sys'] == 'C':
                    item['Temperature'] = temperature.celsius_to_farenheit(float(temp_))
                    item['Tem_Sys'] = 'F'


def save_output_csv(input_:list, file_name:str):
    with open(f'{file_name}.csv', 'w') as file:
        file.write('Date,Distance,Temperature\n')
        for item in input_:
            file.write(f'{item['Date']},{item['Distance']}{item['Dis_Sys']},{item['Temperature']}{DEGREE}{item['Tem_Sys']}\n')

in_dict = read_csv("input")
convert_temperature(in_dict, 'CK')
save_output_csv(in_dict,'output_CK')
convert_temperature(in_dict, 'FC')
save_output_csv(in_dict,'output_FC')
convert_temperature(in_dict, 'CF')
save_output_csv(in_dict,'output_CF')

convert_distance(in_dict, 'FD')
save_output_csv(in_dict,'output_FD')
convert_distance(in_dict, 'FM')
save_output_csv(in_dict,'output_FM')
convert_distance(in_dict, 'MF')
save_output_csv(in_dict,'output_MF')

