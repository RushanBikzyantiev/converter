# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def convert_to_cm(system,unit,number):
    if system == 'american':
        if unit == 'inch':
            result=round(number*2.54,2)
        if unit == 'foot':
            result=round(number*30.48,2)
        if unit == 'mi':
            result=round(number*160934.4,2)
    if system == 'oldrussian':
        if unit=='Elbow':
            result = round(number * 59.37777777777941, 2)
        if unit=='span':
            result = round(number * 17.78, 2)
        if unit=='fathom':
            result = round(number * 213.36, 2)
    return(result)

def convert_from_cm(system, unit, number):
    if system == 'american':
        if unit == 'hand':
            result = round(number / 10.16, 2)
        elif unit == 'yard':
            result = round(number / 91.44, 2)
        elif unit == 'rod':
            result = round(number / 502.92, 2)
    
    elif system == 'oldrussian':
        if unit == 'verst':
            result = round(number / 106680, 2)

    return result 