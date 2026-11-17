# CREDO GitHub 上传操作指南

目标仓库：`https://github.com/pengchengintelligence/CREDO`（根据用户提供的 GitHub 截图）。

## 推荐方式：Git 命令上传

**GitHub 不会自动将 ZIP 解压为仓库目录。** 请先解压 `CREDO-GitHub.zip`，进入解压后的 `CREDO` 文件夹，再上传其中的内容。

当前远程仓库已有 README.md。为了避免与本压缩包中的完整 README 冲突，建议先 `git clone` 仓库，然后将新文件复制到克隆目录中覆盖原 README。

```bash
git clone https://github.com/pengchengintelligence/CREDO.git
cd CREDO
# 将解压后的 CREDO-GitHub 文件夹内的全部文件和子文件夹复制到此处，替换 README.md
git status
git add README.md .gitignore requirements.txt Supplementary_CREDO.pdf UPLOAD_GUIDE_CN.md assets script src
git commit -m "Add CREDO repository documentation, scripts and supplementary material"
git push origin main
```

如果组织仓库要求 Pull Request 或没有 main 分支直接推送权限，请新建分支、推送，再提交 Pull Request。不要将未发表主论文 PDF、私人数据、模型权重或包含密钥的配置上传。

## 通过网页上传

1. 打开当前 CREDO 仓库，选择 `main` 分支。
2. 点击 `Add file` → `Upload files`。
3. **解压 ZIP 后**，把 `assets/`、`script/`、`src/` 等文件夹及根目录文件一起拖入上传区域。
4. 如 GitHub 网页端不允许覆盖已有的 `README.md`，先打开旧 README，点击右上角铅笔图标，将全文替换为本压缩包中 README.md 的内容并提交；其余文件使用 `Upload files` 上传。
5. 添加提交说明，例如 `Publish CREDO documentation and research code`，点击 `Commit changes`。
6. 检查仓库首页：README 中框架图应正常显示；`Supplementary_CREDO.pdf` 可以打开；`script/` 与 `src/` 子目录正确显示。

## 发布前复核

- 确认主论文未上传：`2026_manuscript_CREDO_JBHI(3).pdf` 不应出现。
- 检查所有脚本中带有 `/data1/haoran_moe/` 的旧服务器路径，将其视为需要配置的环境相关默认值。
- 补充材料可能包含受试者招募、伦理批准、独立队列描述等信息，请自行确认公开权限。
- 本 ZIP 未附带论文出版状态或未核实的许可证声明。
