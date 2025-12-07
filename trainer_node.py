import subprocess
import yaml
import os
from jinja2 import Template

class AiToolkitTrainerNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_path": ("STRING", {"default": "/root/models/Z-Image-Turbo"}),
                "dataset_path": ("STRING", {"default": "/root/ai-toolkit/datasets/zimage1_impastohero1"}),
                "output_name": ("STRING", {"default": "zimage1-test"}),
                "steps": ("INT", {"default": 1500, "min": 1}),
                "batch_size": ("INT", {"default": 16, "min": 1}),
                "lr": ("FLOAT", {"default": 1e-4}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "run_training"
    CATEGORY = "ai-toolkit"

    def run_training(self, model_path, dataset_path, output_name, steps, batch_size, lr):

        template_path = os.path.join(os.path.dirname(__file__), "templates/base_config.yaml.j2")
        with open(template_path, "r") as f:
            template = Template(f.read())

        # 渲染 config
        rendered_yaml = template.render(
            model_path=model_path,
            dataset_path=dataset_path,
            steps=steps,
            batch_size=batch_size,
            lr=lr,
            output_name=output_name
        )

        # 保存 config
        output_config_path = f"/root/ai-toolkit/config/{output_name}.yaml"
        with open(output_config_path, "w") as f:
            f.write(rendered_yaml)

        # 调用训练
        cmd = ["python", "/root/ai-toolkit/run.py", output_config_path]
        subprocess.Popen(cmd)

        return (f"Training started: {output_config_path}", )

NODE_CLASS_MAPPINGS = {
    "AiToolkitTrainerNode": AiToolkitTrainerNode
}
