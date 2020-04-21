a = 1

try:
    b = 5/a
    raise IndexError("My message")
except ZeroDivisionError:
    print("ZDE")    
except (NameError, ValueError):
    print("NE")
    exit()
except Exception as e:
    print(e)
except:
    print("ddd")
else:
    print("b = ", b)
finally:
    print("finally")

print("THE End")



