# PocketClaw Quick Start

## 1. 主机端（服务端）

```bash
cd /Users/zhangboshi/Downloads/py7cpp/PocketClaw

python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .

python -m pocketclaw serve \
  --host 0.0.0.0 \
  --port 8787 \
  --token your-secret
```

## 2. 客户端（手机/浏览器）

```text
http://<主机IP>:8787
```

1. 在 `Access token` 输入 `your-secret`。
2. 新建 SSH Target（Host/Port/Username/Password 或 SSH key）。
3. 点击 `Save target` -> `Test SSH` -> `Load tmux state`，然后发送命令。

## 3. 被控远端机器（首次）

在远端 SSH 里执行：

```bash
tmux new -s codex
codex
```

完成后回到客户端页面，选择 pane 即可使用。
