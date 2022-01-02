'''
EXCEPTION IN PYTHON

TRY - test a block of code for error
Except -  block handle the errors
Finally - execute code regardless of the result of the Try and Except block code.

compile time error is refer to the syntax and semantics which means when we break the rules of program paradigm that's occurred.
run time error are those that are detected when program execute zero to divide the number it's not worked make zero divisible error.
raise keyword is used to raise an exception.
else keyword is used to executed if no error

'''

#Types of Exception in python
print(dir(locals()['__builtins__']))

'''
OUPUT

['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError',
 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 
 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 
 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 
 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 
 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 
 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 
 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 
 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', 
 '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 
 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 
 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 
 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 
 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 
 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 
 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

'''

#Count of Exception in python
print("Total Exception in python : ", len(dir(locals()['__builtins__'])))
'''
OUTPUT
Total Exception in python :  153
'''

try:
    x="TRY AND EXCEPTION"
    print(x)
except:
    print("An error occurred")

#OUTPUT
'''
+define the variable (execute the try block of code)
TRY AND EXCEPTION

+does not define the variable (execute the exception)
An error occurred
'''

try:
    # x=3
    print(2+x)
except:
    print("Exception part please check it !")
finally:
    print("FINALLY - TRY and EXCEPT part is completed !")

'''
OUTPUT
+when we give initialize value correctly
5
FINALLY - TRY and EXCEPT part is completed !


+when we not give initialize value correctly

Exception part please check it !
FINALLY - TRY and EXCEPT part is completed !
'''