# 脚本改进说明

## 问题描述

用户在使用 `generate-values-prd.py` 生成 `values-prd.yaml` 时发现了以下问题：

1. **双引号丢失**：YAML 中的字符串引号在生成后丢失
2. **注释丢失**：`extraEnv` 等重要注释在生成后丢失
3. **格式错误**：多行字符串（如 `squidConf`）被错误转义

## 解决方案

### 方案 1：使用 ruamel.yaml（推荐）

**优点：**
- 完美保留原始格式、注释和引号
- 支持多行字符串（`|` 格式）
- 保留 YAML 的原始风格

**使用方法：**
```bash
pip install ruamel.yaml
```

脚本会自动检测并使用 ruamel.yaml，如果未安装会回退到标准 yaml 库。

### 方案 2：文本替换方式（回退方案）

如果 ruamel.yaml 未安装，脚本会使用标准 yaml 库，但会丢失注释和格式。

## 改进内容

### 1. 加载阶段

- 尝试使用 `ruamel.yaml` 加载原始文件（保留注释和格式）
- 同时加载为标准字典用于配置逻辑
- 如果 ruamel.yaml 不可用，回退到标准 yaml

### 2. 保存阶段

- 重新加载原始文件（使用 ruamel.yaml）
- 递归更新修改的值
- 保存时保留所有格式、注释和引号

### 3. 关键改进

```python
# 保存时重新加载原始文件
with open(self.source_file, 'r', encoding='utf-8') as f:
    data = yaml_loader.load(f)

# 只更新修改的值，保留其他所有内容
self._update_dict_recursive(data, self.values)

# 保存
yaml_loader.dump(data, f)
```

## 验证方法

运行测试脚本验证 ruamel.yaml 是否正常工作：

```bash
python3 test-ruamel.py
```

然后检查生成的 `values-test-ruamel.yaml` 文件，确认：
1. 注释是否保留
2. 引号是否保留
3. 多行字符串格式是否正确（如 `squidConf`）
4. `extraEnv` 的注释是否保留

## 注意事项

1. **推荐安装 ruamel.yaml**：为了获得最佳体验，建议安装 `ruamel.yaml`
2. **回退机制**：如果未安装 ruamel.yaml，脚本仍可使用，但会丢失注释和格式
3. **兼容性**：脚本与标准 yaml 库完全兼容

## 安装 ruamel.yaml

```bash
pip install ruamel.yaml
```

或使用 requirements.txt：

```
ruamel.yaml>=0.18.0
```

