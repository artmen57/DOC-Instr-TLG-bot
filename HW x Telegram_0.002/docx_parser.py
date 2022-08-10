from lib2to3.pytree import convert
import os, re, docx2python as d2p
from telegram import InputMediaPhoto
from itertools import zip_longest
def img_extract(path,dest):
    doc=d2p.docx2python(path,dest) 

def text_extract(path):
    patt={}
    doc=d2p.docx2python(path).text
    s=str(doc)
    s=os.linesep.join([s for s in doc.splitlines() if s]) 
    result=re.findall(r"----\S{5,}S{,4}----", s)          
    num_res=re.findall(r'\d+',"".join(result))
    patt=dict(zip(result,num_res))                        
    for word, replace in patt.items():                    
        s=s.replace(word,f"")
    step=re.findall(r"[0-9]+\)+.*(?:\n(?![0-9]+\)).*)*", s)

    return s, step

def img_sender(path,step):
    img_list=[];srt=[] 
    for img in os.listdir(path+"\img\\"):
        if (img.endswith(".png") or img.endswith(".jpeg") or img.endswith(".jpg")):
            srt.append(img)
            srt.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) 
    #print(srt)

    for img,st in zip_longest(range(len(srt)),step):
        img_list.append(InputMediaPhoto(open(path+"\img\\"+str(srt[img]),"rb"),caption=f"{st}"))
        #   ---     Добавлять или сразу ставить в основном коде?
        #print(srt[img])
        #print(st)
    return img_list

if __name__=="__main__":
    path="D:\HW x Telegram\guides\guide2"
    img_extract(path+"\\bot.docx",path+"\\img")
    txt,step=text_extract(path+"\\bot.docx")
    img_list=img_sender(path,step)
    #print(txt,step,sep="\n") 
    #print(img_list)
    #img_extract(path+"\\botwe.DOCX",path+"\img")
