import os

class AiTKModelSelectNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_path": ("STRING", {"default": "/root/models/Z-Image-Turbo"}),
                "assistant_lora": ("STRING", {"default": "/root/models/zimage_turbo_training_adapter/adapter.safetensors"})
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    FUNCTION = "out"
    CATEGORY = "ai-toolkit/model"

    def out(self, model_path, assistant_lora):
        return (model_path, assistant_lora)


NODE_CLASS_MAPPINGS = {
    "AiTKModelSelectNode": AiTKModelSelectNode
}