import subprocess
import os
from jinja2 import Template
import threading
import time

class AiTKTrainerNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dataset_path": ("STRING", {}),
                "model_path": ("STRING", {}),
                "assistant_lora": ("STRING", {}),
                "output_name": ("STRING", {}),
                "steps": ("INT", {}),
                "batch_size": ("INT", {}),
                "lr": ("FLOAT", {}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")  # config_path, log_path
    FUNCTION = "run_training"
    CATEGORY = "ai-toolkit/train"

    def run_training(self, dataset_path, model_path, assistant_lora,
                     output_name, steps, batch_size, lr):

        # Load template
        template_path = os.path.join(os.path.dirname(__file__), "templates/base_config.yaml.j2")
        with open(template_path, "r") as f:
            template = Template(f.read())

        # Render config
        rendered_yaml = template.render(
            dataset_path=dataset_path,
            model_path=model_path,
            assistant_lora=assistant_lora,
            output_name=output_name,
            steps=steps,
            batch_size=batch_size,
            lr=lr
        )

        # Write config file
        config_path = f"/root/ai-toolkit/config/{output_name}.yaml"
        with open(config_path, "w") as f:
            f.write(rendered_yaml)

        # Log file
        log_path = f"/root/ai-toolkit/output/logs/{output_name}.log"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        # Run training
        def run_and_log():
            with open(log_path, "w") as log:
                process = subprocess.Popen(
                    ["python", "/root/ai-toolkit/run.py", config_path],
                    stdout=log,
                    stderr=log
                )
                process.wait()

        threading.Thread(target=run_and_log, daemon=True).start()

        return (config_path, log_path)


NODE_CLASS_MAPPINGS = {
    "AiTKTrainerNode": AiTKTrainerNode
}