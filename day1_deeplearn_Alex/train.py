import torch
from torch import optim, nn
# optim：这个模块提供了各种优化算法，如 SGD、Adam 等，
# 用于在训练过程中更新神经网络的权重。
# nn：这个模块提供了各种类和函数，用于构建和训练神经网络。
# 它包括不同类型的层、激活函数、损失函数等。
from torch.utils.data import dataloader
from dataset import *
from torchvision import models
# models：这个模块提供了预训练模型，并允许你构建和训练深度学习模型。
from matplotlib import pyplot as plt

m  = nn.Softmax(dim=1)
# 将nn.softmax，dim=1 表示沿着张量的第二维度进行操作
def train():
    train_dataset = Animals_dataset(True)
    train_dataloader = DataLoader(train_dataset,batch_size=64,shuffle=True)
    val_dataset = Animals_dataset(False)
    val_dataloader = DataLoader(val_dataset,batch_size=32,shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = models.alexnet(num_classes = 10,dropout=0.3).to(device)
    
    print("train on ",device)

    loss_fn = nn.CrossEntropyLoss()

    #优化器
    optimizer = optim.SGD(model.parameters(),lr=0.01,momentum=0.9)

    train_loss_arr = []
    train_acc_arr = []
    val_loss_arr = []
    val_acc_arr = []

    for epoch in range(10):
        train_loss_total = 0
        train_acc_total = 0
        val_loss_total = 0
        val_acc_total = 0
        model.train()
        for i,(train_x,train_y) in enumerate(train_dataloader):
            train_x = train_x.to(device)
            train_y = train_y.to(device)

            train_y_pred = model(train_x)
            train_loss = loss_fn(train_y_pred.squeeze(),train_y)
            train_acc = (m(train_y_pred).max(dim=1)[1] == train_y).sum()/train_y.shape[0]
            train_loss_total += train_loss.data.item()
            train_acc_total += train_acc.data.item()

            train_loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            print("epoch:{} train_loss: {} train_acc: {}".format(epoch,train_loss.data.item(),train_acc.data.item()))
        
        train_loss_arr.append(train_loss_total / len(train_dataloader))
        train_acc_arr.append(train_acc_total / len(train_dataloader))

        model.eval()

        for j, (val_x,val_y) in enumerate(val_dataloader):
            val_x = val_x.to(device)
            val_y = val_y.to(device)

            val_y_pred = model(val_x)
            val_loss = loss_fn(val_y_pred.squeeze(),val_y)
            val_acc = (m(val_y_pred).max(dim=1)[1]==val_y).sum()/val_y.shape[0]
            val_loss_total += val_loss.data.item()
            val_acc_total += val_acc.data.item()

        val_loss_arr.append(val_loss_total / len(val_dataloader))  # 平均值
        val_acc_arr.append(val_acc_total / len(val_dataloader))
        print("epoch:{} val_loss:{} val_acc:{}".format(epoch, val_loss_arr[-1], val_acc_arr[-1]))

    plt.subplot(1, 2, 1)   # 画布一分为二,1行2列，用第一个
    plt.title("loss")
    plt.plot(train_loss_arr, "r", label="train")
    plt.plot(val_loss_arr, "b", label="val")
    plt.legend()

    plt.subplot(1, 2, 2)  # 画布一分为二,1行2列，用第一个
    plt.title("acc")
    plt.plot(train_acc_arr, "r", label="train")
    plt.plot(val_acc_arr, "b", label="val")
    plt.legend()
    plt.savefig("loss_acc-1.png")

    plt.show()

    # 保存模型
    # 1.torch.save()
    # 2.文件的后缀名：.pt、.pth、.pkl
    torch.save(model.state_dict(), r"model/alexnet-animal.pth")
    print("保存模型成功!")


if __name__ == "__main__":
    train()
           
           