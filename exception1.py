try:
    a=10
    b=0
    c=a/b
    print("value opf c : ",c)

except ZeroDivisionError:
    print("Zero Division Error Occur")

except TypeError:
    print("Type mismatch")


print("Out of try and except")
