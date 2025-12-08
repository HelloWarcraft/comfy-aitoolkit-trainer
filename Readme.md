这是 ComfyUI 插件，用来通过 ai-toolkit 启动训练。

安装依赖：
pip install -r requirements.txt

环境变量（可选）：
设置 `AITK_ROOT` 指向你的 ai-toolkit 根目录（默认 `/root/ai-toolkit`）
例如：
export AITK_ROOT=/home/you/ai-toolkit

如何测试（大致步骤）：
1. 启动 ComfyUI 并确保本仓库被放到 ComfyUI 的 custom nodes 目录中。
2. 在前端加载节点：Model -> Config -> Dataset -> Trainer -> DummyOutput -> LogViewer
3. 点击 Run。若一切正常，Trainer 会生成 config（`$AITK_ROOT/config/<output_name>.yaml`），在 `$AITK_ROOT/output/logs/<output_name>.log` 生成日志，并在 `$AITK_ROOT/output/pids/<output_name>.pid` 写入 PID。
