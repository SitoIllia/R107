Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x = "Sa"
>>> print(y)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(y)
NameError: name 'y' is not defined
>>> y = x+"Iut"
>>> print(y)
SaIut
>>> y = y+"\n\tCesar"
>>> print(y)
SaIut
	Cesar
>>> x+= "lut "+"Jules"
>>> print(y)
SaIut
	Cesar
>>> y = len(x)
>>> print(y)
11
>>> y = len("BonjourJuju")
>>> print(y)
11
>>> y = "Salut! "*2
>>> print(y)
Salut! Salut! 
>>> x = len(y)
>>> print(y)
Salut! Salut! 
>>> y.strip()
'Salut! Salut!'
>>> print(y)
Salut! Salut! 
>>> y= y.strip()
>>> print(y)
Salut! Salut!
