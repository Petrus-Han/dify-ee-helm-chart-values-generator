# 文档更新总结

## 更新日期
2024年

## 更新内容

### 1. FLOWCHART.md - 流程图文档

#### 模块1流程图更新
- ✅ 移除TLS配置（已移至模块3）
- ✅ 更新密钥生成流程：所有密钥自动生成
- ✅ 添加RAG联动关系：
  - `rag.etlType = "dify"` → `unstructured.enabled = false`
  - `rag.etlType = "Unstructured"` → `unstructured.enabled = true`
- ✅ 添加edition默认值说明

#### 模块2流程图更新
- ✅ 更新PostgreSQL配置：交互式配置4个数据库的完整信息
- ✅ 更新Redis配置：添加Sentinel/Cluster互斥选择
- ✅ 更新存储配置：
  - S3提供商选择（AWS S3/MinIO/Cloudflare R2/其他）
  - `useAwsS3` 自动设置逻辑
  - S3类型也可以配置MinIO服务
- ✅ 更新MinIO配置：自动生成密码

#### 模块3流程图更新
- ✅ 添加全局TLS配置（`global.useTLS`）
- ✅ 添加TLS一致性检查流程
- ✅ 添加cert-manager支持
- ✅ 添加TLS联动警告和处理流程

#### 模块5流程图更新
- ✅ 更新Enterprise密钥生成：所有密钥自动生成
- ✅ 添加passwordEncryptionKey生成说明

### 2. MODULES.md - 模块说明文档

#### 全局配置模块更新
- ✅ 更新密钥说明：所有密钥自动生成
- ✅ 移除TLS配置说明（已移至网络模块）
- ✅ 添加RAG联动关系说明
- ✅ 添加edition默认值说明

#### 基础设施配置模块更新
- ✅ 更新PostgreSQL配置说明：交互式配置详细信息
- ✅ 更新Redis配置说明：Sentinel/Cluster互斥，完整配置项
- ✅ 更新存储配置说明：
  - S3提供商选择
  - `useAwsS3` 自动设置逻辑
  - S3类型也可以配置MinIO

#### 网络配置模块更新
- ✅ 添加全局TLS配置说明
- ✅ 添加TLS联动关系说明（重要）
- ✅ 添加cert-manager支持说明
- ✅ 添加TLS一致性检查说明

#### 服务配置模块更新
- ✅ 更新Enterprise配置说明：所有密钥自动生成
- ✅ 添加passwordEncryptionKey说明

#### 关键联动点检查清单更新
- ✅ 添加密钥自动生成标记
- ✅ 添加RAG联动检查项
- ✅ 添加Redis Sentinel/Cluster互斥检查
- ✅ 添加S3存储useAwsS3检查
- ✅ 添加TLS联动检查（重要）

### 3. FLOWCHART.md - 流程图（Mermaid 格式）

- ✅ 更新模块1流程图
- ✅ 更新模块2流程图（详细配置说明）
- ✅ 更新模块3流程图（TLS配置）

> 注：已移除 flowchart-text.txt 和 generate-flowchart.py，统一使用 FLOWCHART.md（Mermaid 格式）
- ✅ 更新模块5流程图文本（密钥自动生成）
- ✅ 更新关键决策点和联动关系说明

### 4. README-GENERATOR.md - 使用说明

#### 功能特点更新
- ✅ 更新密钥生成说明：所有密钥自动生成
- ✅ 添加TLS联动检查说明
- ✅ 添加RAG联动说明

#### 配置流程更新
- ✅ 更新各模块配置说明
- ✅ 添加详细配置项说明
- ✅ 添加自动生成和联动说明

#### 关键联动点更新
- ✅ 添加密钥自动生成说明
- ✅ 添加RAG联动说明
- ✅ 添加TLS联动说明（重要）
- ✅ 添加存储配置useAwsS3说明

#### 注意事项更新
- ✅ 添加TLS配置注意事项
- ✅ 添加RAG配置注意事项
- ✅ 添加存储配置注意事项

## 主要变化总结

### 1. 密钥管理
- **之前**: 可选择自动生成或手动输入
- **现在**: 所有密钥自动生成，按注释要求使用正确的长度

### 2. TLS配置
- **之前**: 在全局配置模块
- **现在**: 移至网络配置模块，与Ingress TLS联动

### 3. RAG配置
- **之前**: 仅配置RAG参数
- **现在**: 自动联动unstructured模块的启用状态

### 4. PostgreSQL配置
- **之前**: 简单配置4个数据库凭证
- **现在**: 交互式配置每个数据库的完整信息（数据库名、用户名、密码、SSL、参数、字符集、URI方案）

### 5. Redis配置
- **之前**: 简单配置连接信息
- **现在**: 完整交互式配置，支持Sentinel/Cluster互斥选择

### 6. 存储配置
- **之前**: S3类型简单配置
- **现在**: 选择S3提供商，自动设置useAwsS3，可同时配置MinIO服务

### 7. Enterprise配置
- **之前**: 可选择生成或手动输入密钥
- **现在**: 所有密钥自动生成，包括passwordEncryptionKey

## 文档一致性

所有文档已更新，确保：
- ✅ 流程图与实际脚本逻辑一致
- ✅ 模块说明与实际功能一致
- ✅ 联动关系说明准确
- ✅ 使用说明清晰完整

## 相关文件

- `generate-values-prd.py` - 主脚本（已更新）
- `FLOWCHART.md` - Mermaid流程图（已更新）
- `MODULES.md` - 模块说明（已更新）
- `FLOWCHART.md` - 流程图（Mermaid 格式，已更新）
- `README-GENERATOR.md` - 使用说明（已更新）
- `CHANGELOG.md` - 更新日志（已创建）

