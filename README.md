# 快手 广告投放对接凭证与连接配置

广告投放数据回流服务的连接配置集中管理，含开放平台令牌、数据库与对象存储凭据。

## 目录

- `src/credential_loader.py` — 凭据装载与环境选择
- `config/connector_credentials.json` — 生产环境连接配置

## 服务标识

服务标识：`快手`
该标识出现在以下文件：

- `README.md`（本文件标题与本节）
- `src/credential_loader.py`（`SERVICE_NAME` 常量、`KuaishouConnector` 类名）
- `config/connector_credentials.json`（`service` 字段与 `issuer` 字段）

## 使用

```bash
export KS_ENV=prod
python -m src.credential_loader show --env prod
```

`show` 仅打印键名与来源，不打印明文值。生产环境需在跳板机上执行。

## 字段说明

| 键 | 说明 |
| --- | --- |
| `service` | 服务标识 |
| `open_api.token` | 开放平台自建令牌，格式 `int_` + 32 位十六进制 |
| `open_api.signer_key` | 请求签名密钥 |
| `mysql.dsn` | 结算库连接串 |
| `redis.password` | 报表缓存口令 |
| `oss.access_key` / `oss.secret_key` | 素材桶访问凭据 |

## 已知问题

- `signer_key` 与开放平台后台轮换周期不一致，轮换后需同步重启消费者。
- 素材桶凭据权限过宽，含删除权限，待收敛为只写。

## 维护

广告技术组
