# go2py
Calling go functions in python,Automatically generate intermediate code

# Useage
```
python go2py.py xxx.go
```
it will generate libxxx.go,libxxx.so,and xxx.py.Then you can call go function as this:

```
import xxx
xxx.func1()
```
