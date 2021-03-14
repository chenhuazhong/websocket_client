
from tkinter import *
from tkinter.scrolledtext import  ScrolledText

import tkinter.font as tf

from utils import MessageScrolledText
from websocket_client import run, DummyClient, run_client


class APP(object):

    def __init__(self, master=None, *args, **kwargs):
        self.master = master
        self.current_window = None

    def swith_window(self, window, *args, **kwargs):

        if self.current_window:
            self.current_window.place_forget()
        window.place(*args, **kwargs)
        self.current_window = window

    def menu(self):
        # 在大窗口下定义一个菜单实例
        menubar = Menu(self.master)
        # 给菜单实例增加菜单项
        for each in ['系统(X)', '设置(Y)', '关于(Z)']:
            menubar.add_command(label=each)
        self.master['menu'] = menubar

#     def init_start_window(self):
#
#         start_f = Frame(self.main_f)
#
#         ft = tf.Font(family='微软雅黑', size=10)
#         user_agreement = Text(start_f, bg="#ffffe1", font=ft)
#         user_agreement.place(width=640, height=280, y=10, x=20)
#         USER_TEXT = """
#
# """
#         # user_agreement.insert(END, "\n")
#         user_agreement.insert(END, USER_TEXT)
#         user_input_f = Frame(start_f)
#         CheckVar1 = IntVar()
#         CheckVar2 = IntVar()
#
#         def client_run():
#             passwd = self.passwd.get()
#             if passwd is None or passwd == "":
#                 from tkinter.messagebox import showinfo
#                 showinfo(message="卡介质密码不能为空，请到《设置》中设置卡介质密码")
#             else:
#                 self.swith_window(self.context_f, width=700, height=499, y=15, x=10)
#                 from threading import Thread
#
#                 if passwd == '' or passwd is None:
#                     passwd = "88888888"
#
#                 server_addr = self.server_adder.get()
#                 self.start_button.configure(state="disabled")
#
#         self.start_button = Button(user_input_f, text="启动", command=client_run)
#
#         def check_start():
#             if CheckVar1.get() and CheckVar2.get():
#                 self.start_button.configure(state="active")
#             else:
#                 self.start_button.configure(state="disabled")
#
#         check_start()
#
#         user_input1 = Checkbutton(user_input_f, text="您同意以上述《用户协议》，才能继续运行", onvalue=1, offvalue=0, variable=CheckVar1,
#                                   command=check_start)
#         user_input2 = Checkbutton(user_input_f, text="登陆成功后，以正常模式运行RPA操作（显示操作页面）", onvalue=1, offvalue=0,
#                                   variable=CheckVar2, command=check_start)
#         line_ = Frame(user_input_f, relief="ridge", borderwidth=1)
#         line_.place(width=580, height=2, x=4, y=60)
#         user_input_f.place(x=30, y=330, width=650, height=200)
#         user_input1.place(x=0, y=0)
#         user_input2.place(x=0, y=30)
#
#         self.start_button.place(x=475, y=80, width=120, height=35)
#         self.start_f = start_f
#         start_f.place(width=700, height=600, y=15, x=10)
#         self.current_window = start_f

    def init_run_window(self):
        self.context_f = Frame(self.main_f)
        # div_1 = Frame(self.context_f)
        self.ccode = StringVar()
        ccode_lable = StringVar()
        ccode_lable.set("websocket地址:")
        self.cname = StringVar()
        cname_lable = StringVar()
        cname_lable.set("企业名称:")
        c_f = Frame(self.context_f)
        c_f.place(width=600, height=150, x=50, y=2)
        line_ = Frame(self.context_f, relief="ridge", borderwidth=1)
        line_.place(width=615, height=2, x=40, y=145)
        f_code = Frame(c_f)
        f_code.place(width=600, height=40, y=0)
        t1 = Entry(f_code, textvariable=self.ccode)
        l1 = Label(f_code, textvariable=ccode_lable)
        self.b_link = StringVar()
        self.b_link.set("链接")
        self.b = Button(f_code, textvariable=self.b_link, command=self.link_server)
        l1.place(width=100, height=35)
        t1.place(width=400, height=35, x=110)
        self.b.place(width=70, height=35, x=510)
        # t1.grid(row=1, column=2)
        # l1.grid(row=1, column=1)
        # b.grid(row=1, column=3)
        frame_1 = Frame(self.context_f, relief="groove", borderwidth=2)
        frame_1.place(width=634, height=394, x=40, y=60)
        label_message = Label(self.context_f, text="运行记录")
        label_message.place(width=77, height=11, x=53, y=55)
        self.message = MessageScrolledText(frame_1)
        self.message.place(width=630, height=280, x=0, y=10)
        self.client_input = Text(frame_1)
        ft = tf.Font(family='微软雅黑', size=10)  ###有很多参数
        self.client_input.tag_add('tag', END)  # 申明一个tag,在a位置使用
        self.client_input.tag_config('tag', foreground='red', font=ft)  # 设置tag即插入文字的大小,颜色等
        self.client_input.place(width=630, height=100, x=0, y=290)
        send_b = Button(frame_1, text="发送", command=self.client_send_to_server)
        send_b.place(width=70, height=30, x=550, y=350)

    def client_send_to_server(self):
        text = self.client_input.get(1.0, "end")
        self.client_input.delete(1.0, "end")

        self.message.INFO(text, "tag")
        self.ws.send(text)

    def link_server(self):
        if self.b_link.get() == "链接":
            from threading import Thread
            self.ws = DummyClient(self.message, 'ws://123.207.136.134:9010/ajaxchattest')
            self.ws.connect()
            # self.ws._th.join()
            # task = Thread(target=run, args=(self.ws,))
            # task.start()
            self.b_link.set("关闭")
        else:
            self.b_link.set("链接")
            self.ws.close()
        # self.ws.send("hahah")

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if len(value_if_allowed) <= 8:
            return True
        else:
            print("密码超长")
            return False

    def init_settings_window(self):
        self.context_settings = Frame(self.main_f)
        frame_1 = Frame(self.context_settings)
        frame_1.place(width=680, height=200)
        self.app_settings = Frame(frame_1, relief="groove", borderwidth=2)
        self.app_settings.place(width=600, height=100, x=50, y=4)
        label_settings = Label(frame_1, text="应用设置")
        label_settings.place(width=55, height=11, x=59, y=0)


    def init_info_window(self):
        #
        self.context_info_f = Frame(self.main_f)
        self.logo_f = Frame(self.context_info_f)
        self.logo_f.place(width=300, height=222, y=33, x=233)

        # label1 = Label(self.logo_f, image=iamgeq)
        # self.context_info_f.place(width=700, height=600, y=15, x=10)
        # label1.place(width=122, height=132, y=15, x=10)
        logo_name = Label(self.logo_f, text="websocket-client v1.0", font=("微软雅黑", 11))
        # logo_version = Label(self.logo_f, text="v1.0", font=("微软雅黑", 10))
        # logo_version = Label(self.logo_f, text="v1.0", font=("微软雅黑", 10))
        logo_name.place(width=181, height=33, y=50, x=13)
        # logo_version.place(width=111, height=30, y=180, x=47)

        logo_info = Text(self.context_info_f, bg="#f0f0f0")
        info_value = """  github地址：https://github.com/chenhuazhong/websocket_client
          
"""
        # logo_info.place(width=585, height=116, y=340, x=30)
        logo_info.place(width=585, height=216, y=200, x=30)
        logo_info.insert(END, info_value)
        # self.current_window = self.context_info_f

        pass

    def init_window(self):
        self.menu()
        tool_f = Frame(self.master, highlightthickness=1)
        self.main_f = Frame(self.master, relief="ridge", borderwidth=1)
        # 边框样式，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
        self.main_f.place(width=740, height=499, x=94, y=0)
        width = 834
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()

        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        context_f = Frame(root, borderwidth=2, background='light blue')
        # self.init_start_window()
        self.init_run_window()
        self.init_settings_window()
        self.init_info_window()
        self.swith_window(self.context_f, width=700, height=600, y=15, x=10)
        self.context_info = Frame(self.main_f)
        bb2 = Button(self.context_info, text="sdaf")
        bb2.pack()

        def client_passd():
            self.swith_window(self.context_settings, width=700, height=600, y=15, x=10)

        def client_run():
            self.swith_window(self.context_f, width=700, height=600, y=15, x=10)
            #
            # p = Thread(target=task.run, args=(self.message, passwd, self.cname, self.ccode, self.ttkp))
            # p.start()

        def client_info():
            self.swith_window(self.context_info_f, width=700, height=600, y=15, x=10)
            # context_f.pack_forget()

            # context_info.pack()
            pass

        def client_start():
            self.swith_window(self.start_f, width=700, height=600, y=15, x=10)
            pass

        # start = Button(tool_f, text="开始", width=12, height=2, command=client_start)
        b2 = Button(tool_f, text="开始", width=12, height=2, command=client_run)
        b1 = Button(tool_f, text="设置", width=12, height=2, command=client_passd)
        info = Button(tool_f, text="关于", width=12, height=2, command=client_info)

        # start.grid(row=1, column=1)
        b1.grid(row=3, column=1)
        b2.grid(row=2, column=1)
        info.grid(row=4, column=1)

        tool_f.place(width=93, height=834)


def load_args(args):
    args.remove('-w')
    args_dict = {}
    for i in args[1:]:
        t = i.split("=", 1)
        if "-h" == t[0]:
            args_dict["host"] = t[1]
    return args_dict


if __name__ == '__main__':
    import sys
    args = sys.argv
    if "-w" in args:
        args_dict = load_args(args)
        run_client(args_dict['host'])
    else:
        root = Tk()
        app = APP(master=root)
        # iamgeq = PhotoImage(file="./logo2.png")
        app.init_window()
        root.resizable(0, 0)  # 禁止 调整窗口大小
        root.title("websocket-client")
        # root.iconbitmap('tool.ico')
        root.mainloop()