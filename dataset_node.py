import os

class AiTKDatasetNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dataset_path": ("STRING", {"default": "/root/ai-toolkit/datasets/mydata"})
            }
        }

    RETURN_TYPES = ("STRING", )
    FUNCTION = "output_path"
    CATEGORY = "ai-toolkit/dataset"

    def output_path(self, dataset_path):
        if not os.path.exists(dataset_path):
            return (f"[WARN] Dataset path not found: {dataset_path}", )
        return (dataset_path, )


NODE_CLASS_MAPPINGS = {
    "AiTKDatasetNode": AiTKDatasetNode,
}