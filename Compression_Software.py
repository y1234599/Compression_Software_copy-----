# coding=utf8
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
import os
import re
import zipfile


'''用户界面绘制'''


class Interface(Frame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.var = IntVar()

        self.page()
        self.assembly1()
        self.assembly_path()
        self.assembly_text()
        self.check_box()
        #self.start_path = ''
        self.target_path = ''
        self.starting_path = ''

    def page(self):
        '''创建页面上的文本'''

        # 标题
        self.label = Label(self.root, text='简易压缩软件')
        self.label.pack()

        # 创建“起始路径”字样
        self.start_word = Label(self.root, text='起始路径: ', padx=4, pady=4)
        self.start_word.place(x=60, y=50)

        # 创建“目标路径”字样
        self.end_word = Label(self.root, text='目标路径: ', padx=4, pady=4)
        self.end_word.place(x=60, y=125)

        # 创建“选择文件类型”字样
        self.check = Label(self.root, text='选择文件类型: ', padx=4, pady=4)
        self.check.place(x=60, y=165)

    def assembly1(self):
        '''创建组件'''

        # 退出
        self.btnQUIT = Button(self.root, text='退 出', padx=2, pady=2, command=self.root.destroy)
        self.btnQUIT.place(x=220, y=240)

        # 压缩
        self.btn_compress = Button(self.root, text=' 压 缩 ', command=self.zip_compression)
        self.btn_compress.place(x=150, y=200)

        # 解压
        self.btn_decompress = Button(self.root, text=' 解 压 ', command=self.zip_decompression)
        self.btn_decompress.place(x=280, y=200)

    def assembly_path(self):
        '''创建组件“查看文件”'''
        self.btnFIND = Button(self.root, text=' 查看文件  ', padx=1, pady=1, command=self.get_start_path)
        self.btnFIND.place(x=380, y=35)

        '''创建组件“查看文件夹”'''
        self.btnFINDFA = Button(self.root, text='查看文件夹', padx=1, pady=1, command=self.get_start_pathFA)
        self.btnFINDFA.place(x=380, y=70)

        '''创建组件“选择路径”'''
        self.btnTARGET = Button(self.root, text='选择路径', command=self.get_target_path)
        self.btnTARGET.place(x=380, y=125)

    def check_box(self):
        '''创建单选框'''
        # var = IntVar()
        # zip
        check_zip = Radiobutton(self.root, text='zip', value=1, variable=self.var, command=test1)
        check_zip.place(x=150, y=165)

        # rar
        check_rar = Radiobutton(self.root, text='rar', value=2, variable=self.var, command=test)
        check_rar.place(x=230, y=165)

        # 7z
        check_7z = Radiobutton(self.root, text='7z', value=3, variable=self.var, command=test)
        check_7z.place(x=310, y=165)

    def assembly_text(self):
        '''创建选择路径的文本框'''
        self.start_txt = tkinter.StringVar()
        self.start_entry = tkinter.Entry(self.root, textvariable=self.start_txt, width=30, font=('FangSong', 12))
        self.start_path = self.start_txt.get()
        self.start_entry.place(x=120, y=55)
        #print(self.start_path)

        '''创建目标路径文本框'''
        self.target_txt = tkinter.StringVar()
        target_entry = tkinter.Entry(self.root, textvariable=self.target_txt, width=30, font=('FangSong', 12))
        self.target_path = self.target_txt.get()
        target_entry.place(x=120, y=130)

    def get_start_path(self):
        '''获取到源文件的路径。'''
        self.starting_path = filedialog.askopenfilename()
        self.start_txt.set(self.starting_path)
        #self.starting_path = self.start_txt.get()
        #print(self.starting_path)
        # print(self.starting_path)
        #return self.starting_path

    def get_start_pathFA(self):
        '''获取源文件夹路径'''
        self.starting_path = filedialog.askdirectory()
        self.start_txt.set(self.starting_path)
        #self.starting_path = self.start_txt.get()
        #print(self.starting_path)
        # print(starting_pathFA)
        #return self.starting_pathFA

    def get_target_path(self):
        '''获取到目标文件路径'''
        #self.target_path = filedialog.askdirectory()
        self.target_path = filedialog.askopenfilename()
        self.target_txt.set(self.target_path)
        #self.target_path = self.target_txt.get()
        #print(self.target_path)
        # print(target_path)
        #return self.target_path

    def zip_compression(self):
        self.starting_path = path_filter(self.start_txt.get())
        self.target_path = path_filter(self.target_txt.get())
        try:
            #print(self.starting_path)
            file_list = os.listdir(f'{self.starting_path}')
            file_list = os.walk(f'{self.starting_path}')
            for f1 in file_list:
                for f2 in f1[-1]:
                    with zipfile.ZipFile(f'{self.target_path}', 'a') as zf:
                        zf.write(f"{os.path.join(f1[0], f2)}")
                        print(os.path.join(f1[0], f2))

        except Exception as error:
            with zipfile.ZipFile(f'{self.target_path}', 'w') as zf:
                zf.write(f"{self.starting_path}")
                #print(error)


    def zip_decompression(self):
        self.starting_path = path_filter(self.start_txt.get())
        self.target_path = path_filter(self.target_txt.get())
        try:
            with zipfile.ZipFile(f'{self.starting_path}', 'r') as zf:
                zf.extractall(path=f'{self.target_path}')
            #print(f'已从路径: {self.starting_path}\n解压到路径: {self.target_path}')

        except Exception as error:
            pass

def path_filter(path):
    '''路径过滤'''
    path = re.sub(f'[\'*?"<>|]', '', path)
    path = re.sub(f':+', ':', path, )
    path = re.sub(f'^\s+', '', path)
    path = re.sub(f'\s+$', '', path)
    path = re.sub(f'\\\\+', '\\\\', path)
    path = re.sub(f'(\s+)\\\\', '\\\\', path)
    path = re.sub(f'\\\\(\s+)', '\\\\', path)
    path = re.sub(f':(?=\w)', '', path)
    #print(f'确认你的路径: ', path, '\n')
    return path


def test1():
    print('1')


def test():
    root1 = Tk()
    root1.geometry('200x100+650+330')
    root1.title('乱点')
    la = Label(root1, text='都说了没写还点干嘛')
    la.place(x=40, y=30)
    root1.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.title('简易压缩软件')
    root.geometry('480x280+600+300')
    interface = Interface(root)
    interface.mainloop()
