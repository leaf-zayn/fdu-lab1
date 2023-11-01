#!/usr/bin/python3

class mdFile:
    def __init__(self):
        self.text = []
        self.command = []
    
    def list(self):
        print('```markdown',end='\n')
        for t in self.text[1:]:
            print(t)
        print('```',end='\n')

    def list_tree(self):
        print('```markdown',end='\n')
        pre = 0
        for i, element in enumerate(self.text):
            #跳过第一个元素
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

            if i+1 <len(self.text):
                next_item = self.text[i+1]
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
            print(s,end='\n')
        print('```',end='\n')

    def dir_tree(self,root):
        print('```markdown',end='\n')
        pre = 0
        count1 = 0
        flag = 0
        for i, element in enumerate(self.text):
            if i == 0:
                continue
            ele1 = element.split()
            if ele1[1] != root and flag == 0:
                continue

            #此时element为root
            elif ele1[1] == root and flag == 0:
                s = ""
                for word in ele1[0]:
                    if word == '#':
                        count1 = count1 + 1
                        pre = count1
                s = s + '└── ' + ele1[1]
                if i+1 <len(self.text):
                    next_item = self.text[i+1]
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
                print(s,end='\n')

            #开始找次级内容
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

                if i+1 <len(self.text):
                    next_item = self.text[i+1]
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
                print(s,end='\n')
        
        print('```',end='\n')

def test_mdFile():
    # 创建一个mdFile对象
    md = mdFile()

    # 测试__init__方法
    assert md.text == []
    assert md.command == []

    # 添加一些元素到text列表
    md.text.append("")
    md.text.append("# 新的标题")
    md.text.append("# 我的书签")
    md.text.append("## 学习资源")
    md.text.append("### 新的子标题")
    md.text.append("### 编程")
    md.text.append("* Java从入门到入土")

    # 测试list方法
    md.list()  # 这应该在控制台打印出markdown代码块中的text列表的内容

    # 测试list_tree方法
    md.list_tree()  # 这应该在控制台以树形结构打印出text列表的内容

    # 测试dir_tree方法
    md.dir_tree("我的书签")  # 这应该在控制台以树形结构打印出以"Heading1"为根的子树

if __name__ == "__main__":
    test_mdFile()