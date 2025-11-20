# Kind 集群网络配置指南

## 概述

在 kind (Kubernetes in Docker) 集群中运行时，访问集群外部（同一主机上）的服务需要特殊配置。

## 访问集群外服务

### 从集群内访问宿主机服务

在 kind 集群中，Pod 需要访问运行在宿主机上的服务时，可以使用以下方式：

#### 1. 使用 `host.docker.internal`（推荐）

`host.docker.internal` 是 Docker 提供的特殊 DNS 名称，指向宿主机。

**示例配置：**
- PostgreSQL: `host.docker.internal`
- Redis: `host.docker.internal`
- Qdrant: `http://host.docker.internal:6333`

**优点：**
- 跨平台兼容（Windows、macOS、Linux）
- 不需要知道宿主机 IP 地址
- 配置简单

#### 2. 使用宿主机 IP 地址

如果 `host.docker.internal` 不可用，可以使用宿主机 IP。

**获取宿主机 IP：**
```bash
# Linux/macOS
ip route show default | awk '/default/ {print $3}'

# 或使用
docker network inspect bridge | grep Gateway
```

**示例配置：**
- PostgreSQL: `172.17.0.1`（Docker 默认网关）
- Redis: `172.17.0.1`

**注意：**
- IP 地址可能因网络配置而变化
- 需要确保防火墙允许访问

#### 3. 使用 `localhost`（不推荐）

`localhost` 在 Pod 内指向 Pod 自身，**不能**用于访问宿主机服务。

**仅在以下情况可以使用：**
- 使用 NodePort 服务并配置了端口映射
- 使用端口转发（port-forward）

## 常见服务配置示例

### PostgreSQL

**集群外（宿主机）PostgreSQL：**
```yaml
externalPostgres:
  enabled: true
  address: host.docker.internal  # 或宿主机IP
  port: 5432
```

**集群内 PostgreSQL：**
```yaml
externalPostgres:
  enabled: true
  address: postgresql.default.svc.cluster.local  # 或 postgresql
  port: 5432
```

### Redis

**集群外（宿主机）Redis：**
```yaml
externalRedis:
  enabled: true
  host: host.docker.internal  # 或宿主机IP
  port: 6379
```

**集群内 Redis：**
```yaml
externalRedis:
  enabled: true
  host: redis.default.svc.cluster.local  # 或 redis
  port: 6379
```

### Qdrant

**集群外（宿主机）Qdrant：**
```yaml
vectorDB:
  useExternal: true
  externalType: qdrant
  externalQdrant:
    endpoint: http://host.docker.internal:6333
```

**集群内 Qdrant：**
```yaml
vectorDB:
  useExternal: true
  externalType: qdrant
  externalQdrant:
    endpoint: http://qdrant.default.svc.cluster.local:6333
```

## Kind 特殊配置

### 启用 host.docker.internal 支持

如果 kind 集群不支持 `host.docker.internal`，可以在创建集群时添加配置：

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  apiServerAddress: "127.0.0.1"
  apiServerPort: 6443
containers:
  - name: kind-control-plane
    extraMounts:
      - hostPath: /var/run/docker.sock
        containerPath: /var/run/docker.sock
```

### 端口映射

如果需要从宿主机访问集群内服务，可以使用：

```bash
# NodePort 服务
kubectl port-forward service/postgresql 5432:5432

# 或使用 Ingress
# 配置 Ingress 并设置端口映射
```

## 验证连接

### 测试 host.docker.internal

在 Pod 内测试：
```bash
kubectl run -it --rm debug --image=busybox --restart=Never -- nslookup host.docker.internal
```

### 测试服务连接

```bash
# 测试 PostgreSQL
kubectl run -it --rm psql-test --image=postgres:15 --restart=Never -- \
  psql -h host.docker.internal -U postgres -d test

# 测试 Redis
kubectl run -it --rm redis-test --image=redis:7 --restart=Never -- \
  redis-cli -h host.docker.internal ping
```

## 故障排查

### 问题1: 无法解析 host.docker.internal

**解决方案：**
1. 检查 Docker 版本（需要 Docker Desktop 或较新版本）
2. 使用宿主机 IP 地址替代
3. 检查 kind 集群网络配置

### 问题2: 连接被拒绝

**可能原因：**
1. 宿主机服务未监听在 `0.0.0.0`（应监听在 `0.0.0.0` 而不是 `127.0.0.1`）
2. 防火墙阻止连接
3. 端口未正确映射

**解决方案：**
```bash
# 检查服务监听地址
netstat -tlnp | grep 5432

# 确保服务监听在 0.0.0.0
# PostgreSQL: listen_addresses = '*' in postgresql.conf
# Redis: bind 0.0.0.0 in redis.conf
```

### 问题3: 使用 localhost 无法连接

**原因：** `localhost` 在 Pod 内指向 Pod 自身，不是宿主机。

**解决方案：** 使用 `host.docker.internal` 或宿主机 IP。

## 最佳实践

1. **优先使用 `host.docker.internal`**：跨平台兼容，配置简单
2. **服务监听地址**：确保宿主机服务监听在 `0.0.0.0` 而不是 `127.0.0.1`
3. **使用服务名访问集群内服务**：更稳定，不依赖 IP
4. **测试连接**：配置后使用测试 Pod 验证连接

## 相关资源

- [Kind 官方文档](https://kind.sigs.k8s.io/)
- [Docker 网络文档](https://docs.docker.com/network/)
- [Kubernetes 服务发现](https://kubernetes.io/docs/concepts/services-networking/service/)

