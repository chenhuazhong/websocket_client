import datetime
from tkinter.scrolledtext import ScrolledText
from tkinter import END


class MessageScrolledText(ScrolledText):

    def __init__(self, *args, **kwargs):
        self.log_level = kwargs.get("log_level", 'info')
        super(MessageScrolledText, self).__init__(*args, **kwargs)

    def insert(self, message="", index='end',  *args, **kwargs):

        now_date = datetime.datetime.now()
        message = """{}: {}\n""".format(now_date.strftime('%Y-%m-%d %H:%M:%S'), message)
        print("发送的消息:{}".format(message))
        return super(MessageScrolledText, self).insert(index, message, *args)

    def DEBUG(self, message="", index='end',  *args, **kwargs):
        """调试 多打印日志"""
        if self.log_level =='debug':
            self.insert(message)
            self.see(END)

    def INFO(self, message="", index='end',  *args, **kwargs):
        """
        正常打印业务日志
        :param message:
        :param index:
        :param args:
        :param kwargs:
        :return:
        """
        self.insert(message)
        self.see(END)
