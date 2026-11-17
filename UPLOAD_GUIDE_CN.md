# CREDO GitHub 上传指南

目标仓库：https://github.com/pengchengintelligence/CREDO

本版本保留原有的四个非训练脚本、缓存数据加载代码、模块说明、依赖和补充材料；不包含 `train_*.py` 训练脚本，也不包含主论文 PDF 或框架主图。README 不提供训练流程，说明完整实现将在论文被接受后发布。

## 上传

1. 解压 ZIP，直接选中解压后根目录中的所有文件和 `script/`、`src/` 文件夹上传；不要再额外包一层 `CREDO/` 文件夹。
2. 在仓库根目录替换旧版 `README.md`，并删除之前上传版本中的 `assets/` 目录以及 `script/train_cv5_shared_clens_confidence_routed_v2_fixed.py`。
3. 点击 GitHub 仓库主页 `Add file` → `Upload files`；上传新版文件并提交。
4. 检查根目录能够直接看到 `README.md`、`Supplementary_CREDO.pdf`、`script/`、`src/` 和 `requirements.txt`。

注意：从仓库最新版本删除文件不等于从 Git 历史记录中彻底移除；之前公开过的训练脚本或主图仍可能通过旧提交访问。如需要使其从历史中不可访问，应清理 Git 历史或采用其他适当的仓库处理方式。

公开前请自行确认补充材料的公开授权以及脚本中服务器路径等信息是否适宜发布。
