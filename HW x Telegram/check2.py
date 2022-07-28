import zipfile, os, shutil, docx
def img_extract(path,dest):
    doc=zipfile.ZipFile(path)
    for info in doc.infolist():
        if info.filename.endswith((".png",".jpeg",".jpg",".gif")):
            doc.extract(info.filename,dest)
            shutil.copy(dest+"\\"+info.filename,dest+"\\"+path.split("\\")[-1]+info.filename.split("/")[-1])
    doc.close()
def text_exctact(path):
    doc=docx.Document(path)
    fp=str()
    for p in doc.paragraphs:
        fp+=p.text+"\n"
        #print(p.text)
    
    from docx.enum.style import WD_STYLE
    styles = doc.styles
    print(styles)
    #print(styles.name)

    return fp

if __name__=="__main__":
    txt=text_exctact("guides\guide2\ex.docx")
    #print(txt)