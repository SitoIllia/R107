Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> j = int(input("Jour: "))
Jour: 3
>>> h = int(input("Heure: "))
Heure: 09
>>> m = int(input("Minute: "))
Minute: 41
>>> total_minutes = (j - 1) * 24*60 + h * 60 + m
>>> print(total_minutes)
3461
>>> total_minutes = j * 24*60 + h * 60 + m
>>> print(total_minutes)
4901
