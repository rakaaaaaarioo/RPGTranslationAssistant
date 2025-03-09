# 贡献指南

感谢您对RPG Maker 翻译助手项目的关注！我们非常欢迎各种形式的贡献，无论是功能请求、错误报告还是代码贡献。

## 如何贡献

### 报告问题

如果您在使用过程中发现任何问题，请在GitHub的Issues页面提交问题报告。提交问题时，请尽可能地提供以下信息：

1. 问题的详细描述
2. 如何重现问题的步骤
3. 您期望的行为是什么
4. 实际出现的行为是什么
5. 截图（如适用）
6. 您的操作系统版本和Python版本（如适用）

### 提交功能请求

如果您有新功能的想法，欢迎在Issues页面提交功能请求。请详细描述您想要的功能以及它将如何改善项目。

### 提交代码

如果您想要直接贡献代码，请按照以下步骤操作：

1. Fork本仓库
2. 创建您的特性分支：`git checkout -b feature/amazing-feature`
3. 提交您的更改：`git commit -m '添加了一些很棒的功能'`
4. 推送到分支：`git push origin feature/amazing-feature`
5. 提交Pull Request

### 开发规范

- 使用清晰的Python代码风格，遵循PEP 8规范
- 为公共方法和类添加文档字符串
- 编写有意义的提交消息
- 保持代码的简洁性和可读性

## 发布流程

本项目使用GitHub Actions自动构建和发布。要创建新版本，请按照以下步骤操作：

1. 确保所有更改都已合并到主分支
2. 更新版本号（遵循[语义化版本](https://semver.org/lang/zh-CN/)）
3. 创建新的版本标签：`git tag v1.0.0`
4. 推送标签：`git push origin v1.0.0`
5. GitHub Actions将自动构建并发布新版本

## 项目结构

```
RPGTranslationAssistant/
├── RPGTranslationAssistant.py   # 主程序文件
├── build_exe.py                # 构建脚本
├── build.bat                   # 批处理文件
├── README.md                   # 使用说明
├── CONTRIBUTING.md             # 贡献指南
├── LICENSE                     # MIT许可证
├── .github/                    # GitHub相关配置
│   └── workflows/              # GitHub Actions工作流
│       └── build.yml           # 自动构建和发布工作流
├── RPGRewriter/                # RPGRewriter程序文件
├── EasyRPG/                    # EasyRPG播放器文件
├── RTPCollection/              # RTP资源包（zip文件）
└── Works/                      # 工作文件夹
```

## 开发环境设置

1. 克隆仓库：
   ```
   git clone https://github.com/SomiaWhiteRing/RPGTranslationAssistant.git
   cd RPGTranslationAssistant
   ```

2. 创建并激活虚拟环境：
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. 安装开发依赖：
   ```
   pip install pyinstaller
   ```

4. 准备必要的文件夹：
   - 确保有RPGRewriter文件夹，包含RPGRewriter.exe和相关文件
   - 确保有EasyRPG文件夹，包含Player.exe和相关文件
   - 确保有RTPCollection文件夹，包含RTP的zip文件

## 许可证

通过贡献您的代码，您同意将其授权在MIT许可证下。请注意，本项目包含使用不同许可证的第三方组件（如GPL-3.0许可的EasyRPG Player）。您贡献的代码应当尊重这些第三方组件的许可证限制，并避免以违反其许可证条款的方式与这些组件集成。详细信息请参阅[THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md)。 