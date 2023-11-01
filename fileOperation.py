import pickle
from mdFile import mdFile
#根据文件名来加载文件,如果没有则创建一个空文件
def load(filename):
    # 尝试打开文件
    try:
        with open(filename, "rb") as file:
            # 读取文件内容
            content = pickle.load(file)
            return content
    except FileNotFoundError:
        # 如果文件不存在，创建新文件并写入默认内容
        with open(filename, "wb") as file:
            obj = mdFile(filename)
            pickle.dump(obj,file)
            return obj
#传入类对象,类对象内有name字段存入文件
def save(mdFile):
    with open(mdFile.name, "wb") as file:
        pickle.dump(mdFile, file)
    return