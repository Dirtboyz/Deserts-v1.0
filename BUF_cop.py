import pyperclip
mail=('xxx@mail.by')
des=''
while True:
    s=str(pyperclip.paste())
    if s != des:
        print (s)
        des = s
    


           

    