"""
src/process_group_4.py
"""

import torch.distributed as dist

dist.init_process_group(backend="nccl")
group = dist.new_group([_ for _ in range(dist.get_world_size())])
print(f"{group} - rank: {dist.get_rank()}\n")