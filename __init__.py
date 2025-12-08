# __init__.py — 正确加载所有节点

# 导入节点模块
from .dataset_node import NODE_CLASS_MAPPINGS as DATASET_NODES, NODE_DISPLAY_NAME_MAPPINGS as DATASET_DISPLAY
from .model_node import NODE_CLASS_MAPPINGS as MODEL_NODES, NODE_DISPLAY_NAME_MAPPINGS as MODEL_DISPLAY
from .config_node import NODE_CLASS_MAPPINGS as CONFIG_NODES, NODE_DISPLAY_NAME_MAPPINGS as CONFIG_DISPLAY
from .trainer_node import NODE_CLASS_MAPPINGS as TRAINER_NODES, NODE_DISPLAY_NAME_MAPPINGS as TRAINER_DISPLAY

from .dummy_output_node import AiTKDummyOutputNode
from .log_viewer_node import AiTKLogViewerNode


# ---------------------------
# 合并所有节点
# ---------------------------
NODE_CLASS_MAPPINGS = {}

# AiTK 自己的两个额外节点
NODE_CLASS_MAPPINGS.update({
    "AiTKDummyOutputNode": AiTKDummyOutputNode,
    "AiTKLogViewerNode": AiTKLogViewerNode,
})

# 其他 4 个主节点
NODE_CLASS_MAPPINGS.update(DATASET_NODES)
NODE_CLASS_MAPPINGS.update(MODEL_NODES)
NODE_CLASS_MAPPINGS.update(CONFIG_NODES)
NODE_CLASS_MAPPINGS.update(TRAINER_NODES)


# ---------------------------
# Display Names
# ---------------------------
NODE_DISPLAY_NAME_MAPPINGS = {
    "AiTKDummyOutputNode": "AiTK Dummy Output",
    "AiTKLogViewerNode": "AiTK Log Viewer",
}

NODE_DISPLAY_NAME_MAPPINGS.update(DATASET_DISPLAY)
NODE_DISPLAY_NAME_MAPPINGS.update(MODEL_DISPLAY)
NODE_DISPLAY_NAME_MAPPINGS.update(CONFIG_DISPLAY)
NODE_DISPLAY_NAME_MAPPINGS.update(TRAINER_DISPLAY)


# 对外导出
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
