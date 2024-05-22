#!/usr/bin/env python3
'''Description: Learning functions part 2'''

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name 
    return greeting

# You can call the function using "return_text_value()"
text = return_text_value()
print(text)