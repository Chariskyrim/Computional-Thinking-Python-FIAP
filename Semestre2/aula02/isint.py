def isint(v: str) -> bool:
    if v[0] == '-' or v[0] == '+':
        v = v.replace('-','',1)
        v = v.replace('+','',1)
    return v.isdigit()

valor = "+345"
print(isint[valor])