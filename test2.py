Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtie
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import turtie
ModuleNotFoundError: No module named 'turtie'
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> tao1 = {'color':'green','dis':100}
>>> tao.color(tao1['color'])
>>> def rect(tao_object,tdict):
...     for i in range(4):
...         tao_object.forward(tdict['dis'])
...         tao_object.left(90)
... 
...         
>>> rect(tao,tao1)
>>> tao2 = turtle.Pen()
>>> tao2dicet = {'color':'green','dis':50}
>>> tao2.color(tao2dicet['color'])
>>> rect(tao2,tao2dicet)
>>> tao2dicet = {'color':'red','dis':50}
>>> rect(tao2,tao2dicet)
