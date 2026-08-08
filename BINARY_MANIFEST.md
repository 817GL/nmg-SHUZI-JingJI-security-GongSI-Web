# Web v2.0.2 二进制完整性清单

以下 SHA-256 均来自用户提供的原始 `Web v2.0.2 独立运行版` ZIP 解包内容。

| 文件 | 大小 | SHA-256 |
|---|---:|---|
| `server/web_server.exe` | 6,305,792 bytes | `7c29ca8dcc316177387b7276fc36406fd5c34c630bed867a034382218dd3dc80` |
| `templates/template.xlsx` | 8,889 bytes | `db91638d123953a1c9816a08179109c088a7694e9c00789b29db8d3779290a4e` |
| `web/app_icon.png` | 1,300 bytes | `6f6d7777f5125e32fd3a9491302534457aaf0dc39658da21e9d62ca783db14fe` |

原始完整 ZIP：

- 大小：2,712,237 bytes
- SHA-256：`d97ef98171294f791a9e1ae83777109b00ee9c0ad27f7f735de6f828f34b0b45`

Windows PowerShell 校验示例：

```powershell
Get-FileHash ".\server\web_server.exe" -Algorithm SHA256
Get-FileHash ".\templates\template.xlsx" -Algorithm SHA256
Get-FileHash ".\web\app_icon.png" -Algorithm SHA256
```
