from docx2python import docx2python
def txt_extr(path):
    doc=docx2python(path)
    print(doc.text.replace("---*---", "NONE"))
    return doc.text.replace("---*---", "NONE")
if __name__=="__main__":
    txt 