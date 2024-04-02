import torch
# torch：PyTorch 是一个开源的 Python 机器学习库，主要由 Facebook 的人工智能研究实验室（FAIR）开发。
# 它提供了一个灵活和高效的平台，用于构建和训练神经网络。
from PIL import Image
# PIL：Python Imaging Library（PIL）为 Python 解释器添加了图像处理功能。
# 在这里，它用于处理图像数据，如加载和转换图像。
from torchvision import transforms,utils
# torchvision.transforms：这个模块提供了可以应用于 PIL 图像的常见图像变换，如调整大小、裁剪和归一化。
# 这些变换通常用于在将图像输入神经网络之前对图像进行预处理。
from torch.utils.data import Dataset,DataLoader
# torch.utils.data.Dataset：这是 PyTorch 中表示数据集的抽象类。
# 您可以通过对 Dataset 进行子类化并实现 __len__ 和 __getitem__ 方法来创建自定义数据集。
# torch.utils.data.DataLoader：这用于从 Dataset 对象中批量加载数据。
# 它提供了诸如洗牌和并行数据加载等功能，这些功能对于训练神经网络非常有用。
import matplotlib.pyplot as plt
# matplotlib.pyplot：Matplotlib 是 Python 的一个绘图库。
# 在这里，您可以使用它来可视化图像或绘制模型训练/验证指标。

# transforms.Compose 是 torchvision.transforms 模块中的一个类，用于将多个图像转换操作组合成一个串行的转换操作。
# 这样可以方便地将一系列图像处理步骤应用到图像上，而不需要逐个调用每个转换函数。
train_tf = transforms.Compose([
    transforms.Resize(224),
    # 将输入的图像调整大小为 224x224 像素。
    transforms.CenterCrop((244,224)),
    #  对调整大小后的图像进行中心裁剪，裁剪的尺寸为 244x224 像素。
    transforms.RandomRotation(10),
    # 裁剪后的图像进行随机旋转，旋转角度范围为 -10 度到 10 度。
    transforms.ColorJitter(brightness=(0.9,1.1),contrast=(0.9,1.1)),
    # 随机调整图像的亮度和对比度，亮度调整范围为 0.9 到 1.1，对比度调整范围为 0.9 到 1.1。
    transforms.ToTensor(),
    # 将图像转换为 PyTorch 张量，并将像素值缩放到 0 到 1 之间。
])

val_tf = transforms.Compose([
    transforms.Resize(224),
    #  将输入的图像调整大小为 224x224 像素。
    transforms.CenterCrop((224,224)),
    # 对调整大小后的图像进行中心裁剪，裁剪的尺寸为 224x224 像素。
    transforms.ToTensor(),
    #  将图像转换为 PyTorch 张量，并将像素值缩放到 0 到 1 之间。
])

#自定义数据集
# 这段代码定义了一个自定义的数据集类 Animals_dataset，
# 用于加载和处理动物数据集。该数据集类继承自 PyTorch 的 Dataset 类，
# 并实现了 __init__、__len__ 和 __getitem__ 方法。
class Animals_dataset(Dataset):
    def __init__(self,istrain=True):
        """在 __init__ 方法中，
        根据参数 istrain 的值决定加载训练数据集还是测试数据集的 CSV 文件，
        并将文件内容读取到 self.dataset 中。"""
        if istrain:
            f = open("day1_deeplearn_Alex/train_data.csv",'r')
        else:
            f = open("day1_deeplearn_Alex/test_data.csv",'r')
        self.dataset = f.readlines()
        f.close()
        self.istrain = istrain
    
    def __len__(self):
        """__len__ 方法中，返回数据集的长度。"""
        return len(self.dataset)
    
    def __getitem__(self,index):
        """ __getitem__ 方法中，根据索引 index 获取对应位置的数据，
        并使用 Image.open(ima_path).convert("RGB") 
        打开图像文件，并将其转换为 RGB 格式的图像数据。"""
        data = self.dataset[index]
        ima_path = data.split(",")[0]
        # 在 Python 中，以双下划线 __ 开头和结尾的方法是特殊方法
        # （也称为魔术方法或双下划线方法）。
        # 这些方法有特殊的含义，用于实现对象的特定行为或支持特定的语法。
        cls = int(data.split(",")[1])
        # data.split(",") 将 data 字符串按逗号 , 分割成一个字符串列表。
        img_data = Image.open(ima_path).convert("RGB")
        # 这行代码使用 PIL 库中的 Image.open()
        # 方法打开图像文件，并将其转换为 RGB 模式的图像数据。
        if self.istrain:
            dst = train_tf(img_data)
        
        else:
            dst = val_tf(img_data)
        
        return dst,torch.tensor(cls)


def visulization():
    train_dataset = Animals_dataset(True)
    train_dataloader = DataLoader(train_dataset,batch_size=16,shuffle=True)
    # 创建了一个用于训练的数据加载器 train_dataloader。DataLoader 
    # 用于从数据集中加载数据，并按照指定的批量大小和其他参数对数据进行处理。
    examples = enumerate(train_dataloader)
    batch_index,(data,lable) = next(examples)
    # next(examples) 是 Python 中的一个函数，用于从迭代器中获取下一个元素。
    print(data.shape)

    grid = utils.make_grid(data)
    # utils.make_grid(data) 是 torchvision 库中的一个函数，
    # 用于将多个图像数据组成的张量 data 合并成一个网格形式的图像。
    plt.imshow(grid.numpy().transpose(1,2,0))
    # grid.numpy() 将 PyTorch 张量 grid 转换为 NumPy 数组，以便在 Matplotlib 中处理。
    # transpose(1, 2, 0) 将数组的维度重新排列，将通道维度移动到最后一个位置。
    # 这样做是因为 Matplotlib 要求图像数据的通道维度在最后一个位置。
    # plt.imshow(...) 用于显示转换后的图像网格。
    plt.show()
    # plt.show() 是 Matplotlib 库中的一个函数，用于显示所有通过 plt 绘制的图形。
    # 在调用 plt.show() 之前，所有的绘图操作都只是在内存中进行，并没有实际显示出来。
    # 只有调用了 plt.show()，Matplotlib 才会将这些图形显示在屏幕上。

if __name__ == "__main__":
    visulization()
