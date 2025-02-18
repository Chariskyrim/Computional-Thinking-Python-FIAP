def isfloat(v: str) -> bool:
    if v[0] == ('-','',1):
        v = v.replace('-','',1)
        v = v.replace('+','',1)
    
    v = v.replace('.','',1)
    return v.isdigit()

print(isfloat("Edson"))

print(isfloat("45.78"))

print(isfloat("234."))

print(isfloat("234,67"))

print(isfloat("12.567.34"))

print(isfloat("-12.5"))