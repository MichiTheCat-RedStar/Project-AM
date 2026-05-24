from tkinter import *
from TeaCoder_Files2Str import *

root = Tk()
root.title('TeaCoder')
root.geometry('285x150')


def isCheckboxed():
	print('Decode:', isDecode.get())

def start(): # Уже четыре часа ночи, у меня писк в ушах, я забыл ткинтер и у меня открыта документация, за окном либо дождь, либо у меня уже всё плохо со слухом из-за сонливости, но ура, я без подсказок или помощи в соло написал все файлы в репозитории, в том числе и этот за одну ночь, что для меня в рамках очен ограниченных возможностей сейчас - просто огромный проект и очень мне от этого ахх....
	with open(strFilePath.get(), ('rb' if isDecode.get()==0 else 'r')) as fileFile:
		with open(strSavePath.get(), 'wb' if isDecode.get()==1 else 'w') as fileSave:
			if isDecode.get() == 1:
				fileSave.write(tDecode(fileFile.read(), strPassword.get()))
			else:
				fileSave.write(tEncode(fileFile.read(), strPassword.get()))


strFilePath = StringVar()
Label(root, text='File Path:').grid(row=0, column=0)
filePath = Entry(root, textvariable=strFilePath)
filePath.grid(row=0, column=1)

strSavePath = StringVar()
Label(root, text='Save Path:').grid(row=1, column=0)
savePath = Entry(root, textvariable=strSavePath)
savePath.grid(row=1, column=1)

strPassword = StringVar()
Label(root, text='Password:').grid(row=2, column=0)
password = Entry(root, textvariable=strPassword)
password.grid(row=2, column=1)

isDecode = IntVar()
encodeButton = Checkbutton(root, text='Decode?', variable=isDecode, onvalue=1, offvalue=0)
encodeButton.grid(row=3, column=0)

saveButton = Button(root, text='Start', command=start)
saveButton.grid(row=3, column=1)

Label(root, text='☭').grid(row=4, column=0)
Label(root, text='Автор:\nMichiTheCat-RedStar (c) 2026').grid(row=4, column=1)


root.mainloop()
