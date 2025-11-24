# Dify Helm Chart Values Generator

> An interactive tool for generating production-ready Helm Chart values files for Dify Enterprise Edition

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Code style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

## 📋 Overview

This project provides a Python script `generate-values-prd.py` that interactively guides users through generating `values-prd.yaml` configuration files. The script uses a modular design and automatically handles relationships between configuration items to ensure consistency and correctness.

[English](README.md) | [中文](README.zh.md)

## ✨ Features

- ✅ **Modular Configuration**: Organized into 6 main modules with clear logic
- ✅ **Automatic Relationship Handling**: Automatically processes mutual exclusions and dependencies
- ✅ **Auto Key Generation**: All keys are automatically generated using `openssl`:
  - `appSecretKey`: 42 bytes
  - `innerApiKey`: 42 bytes
  - `enterprise.appSecretKey`: 42 bytes
  - `enterprise.adminAPIsSecretKeySalt`: 42 bytes
  - `enterprise.passwordEncryptionKey`: 32 bytes (AES-256)
- ✅ **TLS Consistency Check**: Automatically checks TLS configuration consistency with Ingress to avoid CORS issues
- ✅ **RAG Integration**: Automatically handles RAG type and unstructured module relationships
- ✅ **Interactive Guidance**: User-friendly CLI interface with detailed configuration for databases and Redis connections
- ✅ **Progress Preservation**: Supports saving partial configuration after interruption

## 🚀 Quick Start

### Prerequisites

- Python 3.6+
- PyYAML library
- `openssl` (usually pre-installed on systems)
- `ruamel.yaml` (recommended): For preserving YAML file format, comments, and quotes

### Installation

**Using uv (recommended, faster):**

```bash
# 1. Install uv (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Create virtual environment
uv venv

# 3. Activate virtual environment (optional, uv auto-detects)
source .venv/bin/activate

# 4. Install dependencies
uv pip install -r requirements.txt
```

**Or using pip:**

```bash
pip install -r requirements.txt
```

### Usage

```bash
python generate-values-prd.py
```

The script will guide you through the following configuration modules:

1. **Global Configuration** - Affects all services
2. **Infrastructure Configuration** - Database, storage, cache (mutually exclusive choices)
3. **Network Configuration** - Ingress configuration
4. **Mail Configuration** - Email service configuration
5. **Plugin Configuration** - Plugin connector image repository configuration
6. **Service Configuration** - Application service configuration

The generated configuration file will be saved as `values-prd.yaml`.

## 📁 Project Structure

```
.
├── generate-values-prd.py    # Main script file
├── values.yaml               # Base configuration template
├── values-prd.yaml          # Generated production config (gitignored)
├── pyproject.toml           # Python project configuration
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
├── CONTRIBUTING.md          # Contribution guidelines
├── .gitignore              # Git ignore configuration
└── docs/                   # Documentation directory
    ├── README-GENERATOR.md  # Detailed usage guide
    ├── MODULES.md          # Module structure and relationships
    ├── FLOWCHART.md        # Configuration flowcharts
    ├── KIND-NETWORKING.md  # Kind cluster networking guide
    ├── IMPROVEMENTS.md     # Improvement records
    └── CHANGELOG.md        # Changelog
```

## 📚 Documentation

Detailed documentation is available in the `docs/` directory:

- [README-GENERATOR.md](docs/README-GENERATOR.md) - Complete usage guide and examples
- [MODULES.md](docs/MODULES.md) - Module structure and relationship explanations
- [FLOWCHART.md](docs/FLOWCHART.md) - Configuration flowcharts
- [KIND-NETWORKING.md](docs/KIND-NETWORKING.md) - Kind cluster networking guide

## 🔧 Configuration Modules

### Module 1: Global Configuration
- Affects all services
- Includes keys, domains, RAG configuration, etc.

### Module 2: Infrastructure Configuration
- Database selection (PostgreSQL/MySQL)
- Storage selection (MinIO/S3/Azure Blob/etc.)
- Cache selection (Redis)
- Vector database selection (Qdrant/Weaviate/Milvus)

### Module 3: Network Configuration
- Ingress configuration
- TLS settings
- Certificate management (cert-manager support)

### Module 4: Mail Configuration
- SMTP server configuration
- Resend service configuration
- Email service settings

### Module 5: Plugin Configuration
- Image repository type (Docker/ECR)
- Authentication method (IRSA/K8s Secret)
- Protocol selection (HTTPS/HTTP)

### Module 6: Service Configuration
- Enterprise license configuration
- Service enable/disable toggles
- Resource limits

### Relationship Handling

The script automatically handles the following relationships:

- **RAG Integration**: `rag.etlType = "dify"` → `unstructured.enabled = false`
- **RAG Integration**: `rag.etlType = "Unstructured"` → `unstructured.enabled = true`
- **TLS Consistency**: TLS configuration automatically syncs with Ingress to avoid CORS issues
- **Infrastructure Mutex**: Database, storage, and cache selections are mutually exclusive

## 🔒 Security

- Generated `values-prd.yaml` contains sensitive information and is gitignored
- Sensitive files like `email-server.txt` are excluded from the repository
- All keys are generated using `openssl` for security
- Supports IRSA (IAM Roles for Service Accounts) for AWS ECR authentication

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Links

- [Dify Official Documentation](https://docs.dify.ai/)
- [Helm Chart Documentation](https://helm.sh/docs/)
- [Dify Enterprise Documentation](https://enterprise-docs.dify.ai/)

## 🙏 Acknowledgments

- Built for [Dify](https://github.com/langgenius/dify) Enterprise Edition
- Uses [ruamel.yaml](https://yaml.readthedocs.io/) for YAML processing
