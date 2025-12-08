from PIL import Image

class AiTKDummyOutputNode:
    """
    A required final output node so that ComfyUI does not reject the prompt.
    Returns a status string and a small placeholder PIL.Image so ComfyUI considers
    the prompt as having an output image.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "status": ("STRING", {"default": "Training started."})
            }
        }

    RETURN_TYPES = ("STRING", "IMAGE")
    RETURN_NAMES = ("status", "image")
    FUNCTION = "run"
    CATEGORY = "AiToolKit/Utils"

    def run(self, status):
        # Create a small placeholder image (64x64 black)
        img = Image.new("RGB", (64, 64), (0, 0, 0))
        return (status, img)
