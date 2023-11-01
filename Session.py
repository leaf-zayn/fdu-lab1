from Date import getCurrentTime,timeDiff
class Session:
    def __init__(self):
        self.logName = 'md.log'
        self.start()
        self.mdDict={}
        self.current=""
    #一个session开始时输入日志的内容
    def start(self):
        string="session start at "+getCurrentTime()
        self.write(string)
    #需要记录现在正在操作哪个文件
    def setCurrent(self,str):
        self.current=str
    #记录当前session下md文件的load时间
    def record(self,str):
        self.mdDict[str]=getCurrentTime()
    #操作写入日志
    def command(self,str):
        string=getCurrentTime()+" "+str
        self.write(string)

    #写入文件
    def write(self,str):
        file = open(self.logName, "a")
        file.seek(0, 2)  # 将文件指针移动到文件的末尾
        file.write(str+'\n')
        file.close()
    #展示当前session下文件的执行时间
    #param参数控制是all还是current
    def stats(self,param):
        if(param=='all'):
            for key in self.mdDict:
                print(f'{key} {timeDiff(self.mdDict[key],getCurrentTime())}')
        elif(param=='current'):
            key=self.current
            print(f'{key} {timeDiff(self.mdDict[key], getCurrentTime())}')

