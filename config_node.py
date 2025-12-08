class AiTKTrainConfigNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "output_name": ("STRING", {"default": "train_run_01"}),
                "steps": ("INT", {"default": 1500, "min": 1}),
                "batch_size": ("INT", {"default": 16, "min": 1}),
                "lr": ("FLOAT", {"default": 1e-4}),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "INT", "FLOAT")
    FUNCTION = "out"
    CATEGORY = "ai-toolkit/config"

    def out(self, output_name, steps, batch_size, lr):
        return (output_name, steps, batch_size, lr)


NODE_CLASS_MAPPINGS = {
    "AiTKTrainConfigNode": AiTKTrainConfigNode
}