Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> nom = "sitovskyi"
>>> prenom = "illia"
>>> math = 18
>>> anglais = 11
>>> info = 20
>>> promotion = 2025
>>> m = (math + anglais + info) / 3
>>> m
16.333333333333332
>>> type()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> type(nom)
<class 'str'>
>>> type(prenom)
<class 'str'>
>>> type(math)
<class 'int'>
>>> type(m)
<class 'float'>
>>> print("L'étudiant", nom, prenom,"de la promotion", promotion, "a une moyenne de", m)
L'étudiant sitovskyi illia de la promotion 2025 a une moyenne de 16.333333333333332
