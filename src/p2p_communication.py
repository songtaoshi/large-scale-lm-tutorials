import torch
import torch.distributed as dist

a_tensor = torch.tensor([1, 2, 3, 4], dtype=torch.float).to("cuda:0")
dist.send(a_tensor, )