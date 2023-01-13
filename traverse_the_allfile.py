import os

def BasicTransfer(OldPath, NewPath):
    index = 205
    for root, dirs, names in os.walk(OldPath):
        # root 当前访问的路径
        # dirs 当前文件夹下的子目录名
        # name 当前文件夹下的子文件名
        for name in names:
            try:
                # 遍历所有文件名称
                RecourseName = os.path.join(root, name)
                # 包含相对路径的文件路径
                prefix = os.path.splitext(name)[0]
                suffix = os.path.splitext(name)[1]
                DestinationName = NewPath + '\\' +'image_%d'%index+suffix
                os.rename(RecourseName, DestinationName)
                index += 1
            except FileExistsError as e:
                print("有相同文件名的文件存在")
                print(e)
                pass

a = input('请输入文件路径')
b = input('请输入移动目标路径')
BasicTransfer(a, b)
