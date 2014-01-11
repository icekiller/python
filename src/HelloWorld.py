from ctypes import *
msvcrt = cdll.msvcrt
message_string = "HelloWorld!\n"
msvcrt.printf("Testing:%s",message_string)

class barley_amount(Union):
    _fields_ = [
               ("barley_long",c_long),
               ("barley_int",c_int),
               ("barley_char",c_char * 8),
               ]
value = raw_input("put some num:")
myBarley = barley_amount(int(value))
print myBarley.barley_long
print myBarley.barley_int
print myBarley.barley_char