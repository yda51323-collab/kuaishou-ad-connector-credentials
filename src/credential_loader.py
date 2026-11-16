# -*- coding: utf-8 -*-
# 广告投放对接凭据装载
import json
import os

SERVICE_NAME = "快手"
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "connector_credentials.json")
SENSITIVE = ("token", "signer_key", "password", "secret_key", "dsn")


class KuaishouConnector(object):
    """%s 开放平台与结算库的连接配置。""" % SERVICE_NAME

    def __init__(self, env="prod", path=CONFIG_PATH):
        self.env = env
        with open(path, encoding="utf-8") as f:
            self.cfg = json.load(f)

    def get(self, dotted, default=None):
        cur = self.cfg
        for part in dotted.split("."):
            if not isinstance(cur, dict) or part not in cur:
                return default
            cur = cur[part]
        return cur

    def keys(self):
        out = []

        def walk(node, prefix=""):
            for k, v in node.items():
                key = prefix + ("." if prefix else "") + k
                if isinstance(v, dict):
                    walk(v, key)
                else:
                    out.append(key)

        walk(self.cfg)
        return out

    def masked(self):
        res = {}
        for k in self.keys():
            v = self.get(k)
            res[k] = "***" if k.split(".")[-1] in SENSITIVE else v
        return res


if __name__ == "__main__":
    c = KuaishouConnector()
    print(c.cfg["service"], c.env)
    for k, v in c.masked().items():
        print(" ", k, "=", v)
