time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
TIME_UNITS = ('h', 'm', 's')

def to_minutes(value, unit):
    minutes = 0
    if unit == TIME_UNITS[0]:     
        minutes = value * 60
    else:
        minutes = value / 60        
    return(minutes)

def convert_time_element(element_str):
    element_no_spaces = element_str.replace(' ', '')

    start_index = 0
    end_index = 0

    current_value = ''
    total_minutes = 0
    
    for element in element_no_spaces:
        if element in TIME_UNITS:
            current_value = element_no_spaces[start_index:end_index]
            if element == TIME_UNITS[1]:     
                total_minutes+= int(current_value)
            else:
                total_minutes+= to_minutes(int(current_value), element)
            start_index = end_index + 1
        end_index+= 1      
    return total_minutes  

time_list = time_values.split(',')
total_minutes = 0

for i in time_list:
    total_minutes+= convert_time_element(i)
print(total_minutes)