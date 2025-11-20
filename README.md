# Dify Helm Chart Values Generator

一个交互式工具，用于生成 Dify Enterprise Edition 的 Helm Chart 生产环境配置文件。

## 📋 项目简介

本项目提供了一个 Python 脚本 `generate-values-prd.py`，通过交互式引导帮助用户生成 `values-prd.yaml` 配置文件。脚本采用模块化设计，自动处理配置项之间的联动关系，确保配置的一致性和正确性。

## ✨ 功能特点

- ✅ **模块化配置**: 将配置分为5个主要模块，逻辑清晰
- ✅ **自动处理联动**: 自动处理互斥选择和依赖关系
- ✅ **密钥自动生成**: 所有密钥按注释要求自动生成（使用 openssl）
  - `appSecretKey`: 42字节
  - `innerApiKey`: 42字节
  - `enterprise.appSecretKey`: 42字节
  - `enterprise.adminAPIsSecretKeySalt`: 42字节
  - `enterprise.passwordEncryptionKey`: 32字节（AES-256）
- ✅ **TLS联动检查**: TLS配置与Ingress联动，自动检查一致性避免CORS问题
- ✅ **RAG联动**: 自动处理RAG类型与unstructured模块的联动关系
- ✅ **交互式引导**: 友好的命令行交互界面，详细配置每个数据库和Redis连接
- ✅ **进度保存**: 支持中断后保存部分配置

## 🚀 快速开始

### 前置要求

- Python 3.6+
- PyYAML 库
- openssl（用于生成密钥，通常系统已自带）
- ruamel.yaml（推荐）：用于保留 YAML 文件的格式、注释和引号

### 安装依赖

**使用 uv（推荐，更快）：**

```bash
# 1. 安装 uv（如果未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 创建虚拟环境
uv venv

# 3. 激活虚拟环境（可选，uv 会自动检测）
source .venv/bin/activate

# 4. 安装依赖
uv pip install -r requirements.txt
```

**或使用 pip：**

```bash
pip install -r requirements.txt
```

### 使用方法

```bash
python generate-values-prd.py
```

脚本会引导你完成以下配置模块：

1. **全局配置模块** - 影响所有服务
2. **基础设施模块** - 数据库、存储、缓存（互斥选择）
3. **服务模块** - 应用服务配置
4. **网络模块** - Ingress配置
5. **邮件模块** - 邮件服务配置

生成的配置文件将保存为 `values-prd.yaml`。

## 📁 项目结构

```
.
├── generate-values-prd.py    # 主脚本文件
├── values.yaml               # 基础配置文件模板
├── values-prd.yaml          # 生成的生产环境配置（gitignore）
├── pyproject.toml           # Python 项目配置
├── requirements.txt         # Python 依赖列表
├── .gitignore              # Git 忽略文件配置
└── docs/                   # 文档目录
    ├── README-GENERATOR.md  # 详细使用说明
    ├── MODULES.md          # 模块划分说明
    ├── FLOWCHART.md        # 流程图
    ├── KIND-NETWORKING.md  # Kind 网络配置说明
    ├── IMPROVEMENTS.md     # 改进记录
    └── CHANGELOG.md        # 更新日志
```

## 📚 文档

详细的文档请参考 `docs/` 目录：

- [README-GENERATOR.md](docs/README-GENERATOR.md) - 完整的使用说明和示例
- [MODULES.md](docs/MODULES.md) - 模块划分与联动关系说明
- [FLOWCHART.md](docs/FLOWCHART.md) - 配置流程图
- [KIND-NETWORKING.md](docs/KIND-NETWORKING.md) - Kind 集群网络配置说明

## 🔧 配置说明

### 模块划分

1. **全局配置模块 (global)**
   - 影响所有服务
   - 包括密钥、域名、RAG配置等

2. **基础设施模块**
   - 数据库选择（PostgreSQL/MySQL）
   - 存储选择（MinIO/S3）
   - 缓存选择（Redis）

3. **服务模块**
   - 应用服务配置
   - 资源限制
   - 副本数量

4. **网络模块**
   - Ingress配置
   - TLS设置

5. **邮件模块**
   - SMTP服务器配置
   - 邮件服务设置

### 联动关系

脚本会自动处理以下联动关系：

- **RAG联动**: `rag.etlType = "dify"` → `unstructured.enabled = false`
- **RAG联动**: `rag.etlType = "Unstructured"` → `unstructured.enabled = true`
- **TLS联动**: TLS配置与Ingress自动同步，避免CORS问题
- **基础设施互斥**: 数据库、存储、缓存的选择互斥

## 🔒 安全注意事项

- 生成的 `values-prd.yaml` 包含敏感信息，已添加到 `.gitignore`
- `email-server.txt` 等敏感文件不会被提交到仓库
- 所有密钥使用 `openssl` 自动生成，确保安全性

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📝 许可证

请查看项目根目录的 LICENSE 文件（如有）。

## 🔗 相关链接

- [Dify 官方文档](https://docs.dify.ai/)
- [Helm Chart 文档](https://helm.sh/docs/)

