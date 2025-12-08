# __init__.py — 正确加载所有节点

# 导入所有节点模块
from .dataset_node import NODE_CLASS_MAPPINGS as DATASET_NODES
from .model_node import NODE_CLASS_MAPPINGS as MODEL_NODES
from .config_node import NODE_CLASS_MAPPINGS as CONFIG_NODES
from .trainer_node import NODE_CLASS_MAPPINGS as TRAINER_NODES

# 合并所有节点
NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(DATASET_NODES)
NODE_CLASS_MAPPINGS.update(MODEL_NODES)
NODE_CLASS_MAPPINGS.update(CONFIG_NODES)
NODE_CLASS_MAPPINGS.update(TRAINER_NODES)

#（可选）描述插件信息
__all__ = ["NODE_CLASS_MAPPINGS"]
