

def convert(rates, value, current, to):
    for list_row in rates:
        if current == to:
           return value 

        if current == list_row[0] and to == list_row[1]:
            return value * list_row[2]
            
        if current == list_row[1] and to == list_row[0]:
            return value / list_row[2]

        raise ValueError(f"{current} to {to} cannot be converted with the data available, sorry!")