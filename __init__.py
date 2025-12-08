# __init__.py — Safe Version (recommended)

# ---- Import all node classes safely ----
# Each node module MUST define a class e.g. AiTKDatasetNode, etc.

from .dataset_node import AiTKDatasetNode
from .model_node import AiTKModelSelectNode
from .config_node import AiTKTrainConfigNode
from .trainer_node import AiTKTrainerNode
from .dummy_output_node import AiTKDummyOutputNode
from .log_viewer_node import AiTKLogViewerNode


# ---- Register classes here ----
NODE_CLASS_MAPPINGS = {
    "AiTKDatasetNode": AiTKDatasetNode,
    "AiTKModelSelectNode": AiTKModelSelectNode,
    "AiTKTrainConfigNode": AiTKTrainConfigNode,
    "AiTKTrainerNode": AiTKTrainerNode,
    "AiTKDummyOutputNode": AiTKDummyOutputNode,
    "AiTKLogViewerNode": AiTKLogViewerNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AiTKDatasetNode": "AiTK Dataset Loader",
    "AiTKModelSelectNode": "AiTK Model Selector",
    "AiTKTrainConfigNode": "AiTK Training Config",
    "AiTKTrainerNode": "AiTK Trainer",
    "AiTKDummyOutputNode": "AiTK Dummy Output",
    "AiTKLogViewerNode": "AiTK Log Viewer",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
