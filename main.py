# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def convert_to_cm(system,unit,number):
    if system == 'american':
        if unit == 'inch':
            result=round(number*2.54,2)
        if unit == 'foot':
            result=round(number*30.48,2)
    return(result)
