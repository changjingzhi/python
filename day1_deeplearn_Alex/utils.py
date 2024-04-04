import os
import csv
import numpy as np

train_path = "day1_deeplearn_Alex/train_data.csv"
val_path = "day1_deeplearn_Alex/test_data.csv"



def create_data_text(path,train_percent = 0.9):
    """建立数据data列表,划分数据集"""
    f_train = open(train_path,"w",newline='') #
    #并将文件对象赋给了变量 f_train。open(train_path, "w", newline='')
    #  的意思是以写入模式打开名为 train_path 的文件，
    # 并且在写入文本时不插入额外的换行符（newline=''）。open是python的内置函数
    f_val = open(val_path,"w",newline='')
    train_writer = csv.writer(f_train)
    # 创建了一个 CSV writer 对象 train_writer，
    # 用于向文件对象 f_train 中写入 CSV 格式的数据。csv.writer() 接受一个文件对象作为参数，
    # 并返回一个 CSV writer 对象，可以使用该对象的方法将数据写入文件。
    val_writer = csv.writer(f_val)

    # enumerate() 是 Python 内置函数，
    # 用于将一个可迭代对象（如列表、元组、字符串等）
    # 组合为一个索引序列，同时列出数据和数据下标。
    # 函数返回一个枚举对象，其中每个元素是一个包含索引和对应元素的元组。
    for cls,dirname in enumerate(os.listdir(path)):
        flist = os.listdir(os.path.join(path,dirname))
        # os.path.join(path, dirname) 是一个函数，用于将多个路径组合成一个完整的路径。
        # 它会根据当前操作系统的规则使用正确的路径分隔符来连接路径。
        np.random.shuffle(flist)
        # np.random.shuffle(flist) 是 NumPy 库中的一个函数，用于随机打乱列表 flist 中的元素顺序。
        # 这个函数会改变原始列表的顺序，使得列表中的元素随机排列。
        fnum = len(flist)
        # len函数返回
        for i,filename in enumerate(flist):
            # 使用了 enumerate() 函数来遍历列表 flist 中的元素，同时获取元素的索引和值。具体来说，
            # enumerate(flist) 返回一个枚举对象，其中每个元素是一个元组，包含元素在列表中的索引和元素的值。
            if i < fnum * train_percent:
                train_writer.writerow([os.path.join(path,dirname,filename),str(cls)])
            # 是将一个包含两个元素的列表写入CSV文件的操作。这个列表包含两个元素：
            # os.path.join(path,dirname,filename) 返回一个完整的文件路径，其中 path 是主目录路径，dirname 是子目录路径，filename 是文件名。这个路径表示要写入CSV文件的文件的完整路径。
            # str(cls) 将整数 cls 转换为字符串，cls 表示类别编号。
            else:
                val_writer.writerow([os.path.join(path,dirname,filename),str(cls)])
    f_train.close()
    # f_train.close() 是关闭文件 f_train 的方法。在使用完文件后，
    # 应该调用这个方法来关闭文件，以释放资源并确保文件被正确关闭。
    f_val.close()

if __name__ == "__main__":
    create_data_text("C:/Users/Administrator/Desktop/deeplearning/data")
    