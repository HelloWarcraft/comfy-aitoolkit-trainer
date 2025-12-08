#############################
# dummy_output_node.py
#############################

class AiTKDummyOutputNode:
    """
    A required final output node so that ComfyUI does not reject the prompt.
    Does nothing except pass through a status string.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "status": ("STRING", {"default": "Training started."})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("status",)
    FUNCTION = "run"
    CATEGORY = "AiToolKit/Utils"

    def run(self, status):
        return (status,)