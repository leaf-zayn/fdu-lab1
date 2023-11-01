from datetime import datetime


# 目前一个undo只能对应一个redo
class mdFile:
    def __init__(self, name):
        # 记录md里的文字
        self.text = [" "]
        # 记录每次执行undo的命令
        self.undoCommand = []
        # 需要一个指针记录目前回退到第几次操作
        self.commandIndex = 0
        # 需要记录保存的文件名字
        self.name = name
        # 需要用一个变量记录现在是否是undo状态,如果是undo,那么执行相反操作不需要压入命令栈
        # 这个变量记录了是否压入命令栈,True状态是不压入的
        self.isUndo = False

    # index是行号 str是内容
    def insert(self, index, str):
        # 需要做一个范围控制
        if index > len(self.text):
            self.append_tail(str)
            return
        self.text.insert(index, str)
        if not self.isUndo:
            self.undoCommand.insert(self.commandIndex, ("insert", index, str))
            # commandIndex指针++
            self.commandIndex += 1
        return

    # 在头部插入，调用insert
    def append_head(self, str):
        self.insert(1, str)
        return

    # 在尾部插入，也可以调用insert
    def append_tail(self, str):
        # 要知道长度才能插入尾部
        # 不用append的原因是简化undo函数
        length = len(self.text)
        self.insert(length, str)
        return

    # 根据参数类型删除元素
    def delete(self, textOrIndex):
        if isinstance(textOrIndex, int):
            # 如果输入的是整数，则根据索引删除元素
            if 0 <= textOrIndex < len(self.text):
                text = self.text.pop(textOrIndex)
                if not self.isUndo:
                    self.undoCommand.insert(self.commandIndex, ("delete", textOrIndex, text))
                    self.commandIndex += 1
            else:
                print("索引超出范围")
            return
        else:
            for item in self.text:
                index = item.find(textOrIndex)
                if index != -1:
                    self.text.pop(index)
                    self.undoCommand.insert(self.commandIndex, ("delete", index, item))
                    self.commandIndex += 1
                # if textOrIndex in self.text:
                #index = self.text.index(textOrIndex)
                #self.text.remove(textOrIndex)
                #self.undoCommand.insert(self.commandIndex, ("delete", index, textOrIndex))
                #self.commandIndex += 1
                #else:
                    #print("内容不存在")
            return

    # 弹出命令栈中的上一条命令，执行相反操作
    # 为了实现redo操作,指令不删除
    def undo(self):
        self.isUndo = True
        # 取出上一步的操作
        previousCommand = self.undoCommand[self.commandIndex - 1]
        if previousCommand[0] == 'insert':
            self.delete(previousCommand[1])
            self.commandIndex -= 1
        elif previousCommand[0] == 'delete':
            self.insert(previousCommand[1], previousCommand[2])
            self.commandIndex -= 1
        self.isUndo = False
        return

    def redo(self):
        self.isUndo = True
        # ('insert', 1, '# 你好')
        todoCommand = self.undoCommand[self.commandIndex]
        if (todoCommand[0] == 'insert'):
            self.insert(todoCommand[1], todoCommand[2])
            self.commandIndex += 1
        elif (todoCommand[0] == 'delete'):
            self.delete(todoCommand[1])
            self.commandIndex += 1
        self.isUndo = False
        return

    def list(self):
        print('```markdown', end='\n')
        for t in self.text[1:]:
            print(t)
        print('```', end='\n')

    def list_tree(self):
        print('```markdown', end='\n')
        pre = 0
        for i, element in enumerate(self.text):
            # 跳过第一个元素
            if i == 0:
                continue
            s = ""
            ele1 = element.split()
            count1 = 0
            for word in ele1[0]:
                if word == '#':
                    count1 = count1 + 1
                    pre = count1
                elif word == '*':
                    count1 = pre + 1
                    ele1[1] = '·' + ele1[1]

            if i + 1 < len(self.text):
                next_item = self.text[i + 1]
            else:
                next_item = None
            count2 = 0
            if next_item != None:
                ele2 = next_item.split()
                for word in ele2[0]:
                    if word == '#':
                        count2 = count2 + 1
                    elif word == '*':
                        count2 = pre + 1

            if count1 == count2:
                for c in range(0, count1 - 1):
                    s = s + '    '
                s = s + '├── ' + ele1[1]
            elif count1 != count2:
                for c in range(0, count1 - 1):
                    s = s + '    '
                s = s + '└── ' + ele1[1]
            print(s, end='\n')
        print('```', end='\n')

    def dir_tree(self, root):
        print('```markdown', end='\n')
        pre = 0
        count1 = 0
        flag = 0
        for i, element in enumerate(self.text):
            if i == 0:
                continue
            ele1 = element.split()
            if ele1[1] != root and flag == 0:
                continue

            # 此时element为root
            elif ele1[1] == root and flag == 0:
                s = ""
                for word in ele1[0]:
                    if word == '#':
                        count1 = count1 + 1
                        pre = count1
                s = s + '└── ' + ele1[1]
                if i + 1 < len(self.text):
                    next_item = self.text[i + 1]
                else:
                    next_item = None
                count2 = 0
                if next_item != None:
                    ele2 = next_item.split()
                    for word in ele2[0]:
                        if word == '#':
                            count2 = count2 + 1
                        elif word == '*':
                            count2 = pre + 1
                if count2 > count1:
                    flag = 1
                print(s, end='\n')

            # 开始找次级内容
            elif ele1[1] != root and flag == 1:
                s = ""
                count3 = 0
                for word in ele1[0]:
                    if word in ele1[0]:
                        if word == '#':
                            count3 = count3 + 1
                            pre = count3
                        elif word == '*':
                            count3 = pre + 1
                            ele1[1] = '·' + ele1[1]

                if i + 1 < len(self.text):
                    next_item = self.text[i + 1]
                else:
                    next_item = None
                count4 = 0
                if next_item != None:
                    ele2 = next_item.split()
                    for word in ele2[0]:
                        if word == '#':
                            count4 = count4 + 1
                        elif word == '*':
                            count4 = pre + 1

                if count4 <= count1:
                    flag = 0

                if count3 == count4:
                    for c in range(0, count3 - count1):
                        s = s + '    '
                    s = s + '├── ' + ele1[1]
                elif count3 != count4:
                    for c in range(0, count3 - count1):
                        s = s + '    '
                    s = s + '└── ' + ele1[1]
                print(s, end='\n')

        print('```', end='\n')
