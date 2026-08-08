# 内蒙古数字经济安全科技有限公司｜Web 版私有项目备份

本仓库用于保存“密码资源池接口调用统计系统 Web 版”的前端源码、运行脚本、说明文档和正式独立运行版本信息，仅用于项目备份、版本留存和灾难恢复。

## 当前备份版本

- 系统版本：Web v2.0.2
- 版本类型：Windows x64 独立运行版
- 原始包：`密码资源池接口调用统计系统_Web_v2.0.2_独立运行版.zip`
- 原始包大小：2,712,237 bytes（约 2.59 MiB）
- SHA-256：`d97ef98171294f791a9e1ae83777109b00ee9c0ad27f7f735de6f828f34b0b45`
- 仓库可见性：Private

## v2.0.2 包含内容

- `web/index.html`
- `web/styles.css`
- `web/app.js`
- `web/app_icon.png`
- `server/web_server.exe`
- `templates/template.xlsx`
- `START_WEB.cmd`
- `STOP_WEB.cmd`
- `OPEN_WEB.cmd`
- `查看运行日志.cmd`
- `使用说明.txt`
- `版本说明.txt`

## 运行方式

完整独立运行包解压后，双击 `START_WEB.cmd` 启动。默认本机地址：

`http://127.0.0.1:8088`

局域网其他电脑可通过服务器 IP + `8088` 端口访问。

## 当前迁移状态

v2.0.2 已迁移 Web 静态页面、基础服务接口、六资源池接口连通性测试，以及前四个资源池 `getEdsDetail` / `getInterfaceDetail` 采集和基础计数校验。

仍在迁移：SQLite `systems.db` 完整兼容层、后两个政务外网完整统计采集、Excel 模板保格式写入与下载、系统数据库扫描/校对/新增/改名/恢复事件。

## 重要说明

当前原始 ZIP 中包含 Web 前端源码，但 `server/web_server.exe` 对应的后端源代码并未包含在这个包中。因此，本仓库现阶段属于“Web 前端源码 + 独立服务端成品 + 正式运行包备份”，不能把它描述为完整后端源码工程。

运行日志、临时数据、本机 Token、密码、VPN 凭据等不得提交到仓库。

> 本仓库必须始终保持 **Private**。
