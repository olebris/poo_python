passdict= {"alecouture":"Huz4","lmartin":"monty","fsincere":"gnugpl"}
print (passdict)
login=input("tape ton login ")
pwd=input("tape ton pwd ")
for lgin,ppwd in passdict.items():
    #print(lgin,ppwd)
    if lgin==login and ppwd==pwd:
        bool_log= True
        break
    else: bool_log = False
print(bool_log)
