# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

本文件只是 Claude 的项目指针，不复制规则，也不建立第二个状态面板。

- 规范入口：`AGENTS.md`；冲突时以它为准。项目概览与视觉基线见 `README.md`。
- 状态面板是根目录小写的 `kanban.md`（不是 `KANBAN.md`）；当前方向与下一道人工确认门只读它。
- `提示卡项目/` 是只读归档；新主题放 `图片项目/<主题>/`。产品线目录下的 `插画素材规格.md`
  优先于通用冷钴蓝基线（例如 `图片项目/miniprogram-pic/`）。
- 没有构建、依赖或测试套件；验证是编辑性和素材性的。本机 `identify`（ImageMagick）未安装，
  检查 PNG 格式与尺寸改用：
  `python3 -c "from PIL import Image; im=Image.open('<path>'); print(im.format, im.mode, im.size)"`
  或 `ffprobe -v error -show_entries stream=width,height,pix_fmt <path>`。
- 提交标记：`AGENTS.md` 示例写的是 `[Codex]`；Claude 的提交使用 `[Claude]`（见 `e6598dd`、`c6a65dc`）。
