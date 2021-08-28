import PyPDF2 as p
import os
dir_=input(f'enter your directory')
changedir=os.chdir(dir_)
for j in range(1,20):
    a=p.PdfFileReader(str(j)+'.pdf')
    page=a.numPages
    s=''
    for i in range((page)):
        s+=a.getPage(i).extractText()
        print(s)
    with open(str(j)+'.txt','w') as f1:
        f1.write(s)
