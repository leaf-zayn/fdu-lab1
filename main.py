
# Press the green button in the gutter to run the script.
from fileOperation import save, load
from mdFile import mdFile
from History import History
from Session import Session

tmpFile = mdFile("")
history = History()
session = Session()

if __name__ == '__main__':
    while True:
        user_input = input("请输入指令：")
        command = user_input.split()
        command_name = command[0]
        session.command(user_input)
        if command_name != 'history':
            history.insert2History(user_input)
        if command_name == 'load':
            tmpFile = load(command[1])
            session.record(command[1])
            session.setCurrent(command[1])
        elif command_name == 'save':
            save(tmpFile)
        elif command_name == 'insert':
            index = int(command[1])
            tmpFile.insert(index, user_input.split(maxsplit=2)[-1])
            print(tmpFile.text)
        elif command_name == 'append-head':
            tmpFile.append_head(user_input.split(maxsplit=1)[-1])
            print(tmpFile.text)
        elif command_name == 'append-tail':
            tmpFile.append_tail(user_input.split(maxsplit=1)[-1])
            print(tmpFile.text)
        elif command_name == 'delete':
            indexOrText = command[1]
            if indexOrText.isdigit():
                number = int(indexOrText)
                tmpFile.delete(number)
            else:
                tmpFile.delete(user_input.split(maxsplit=1)[-1])
            print(tmpFile.text)
        elif command_name == 'undo':
            tmpFile.undo()
            print(tmpFile.text)
        elif command_name == 'redo':
            tmpFile.redo()
            print(tmpFile.text)
        elif command_name == 'list':
            tmpFile.list()
        elif command_name == 'list-tree':
            tmpFile.list_tree()
        elif command_name == 'dir-tree':
            tmpFile.dir_tree(command[1])
        elif command_name == 'history':
            if (len(command) == 1):
                history.showHistory(history.getHistoryLength())
            else:
                n = int(command[1])
                history.showHistory(n)
        elif command_name == 'stats':
            session.stats(command[1])
