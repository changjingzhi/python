import torch
import torch.nn as nn

# 假设这是一个批量大小为 4，类别数量为 3 的二维张量
tensor = torch.tensor([[1.0, 2.0, 3.0],
                        [0.5, 1.5, 2.5],
                        [2.0, 1.0, 0.0],
                        [3.0, 3.0, 3.0]])

# 创建 Softmax 模块，指定 dim=1
softmax = nn.Softmax(dim=1)

# 对张量进行 Softmax 归一化
output = softmax(tensor)

# 输出结果
print(output)
