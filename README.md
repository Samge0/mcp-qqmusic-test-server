# MCP QQ音乐测试服务器

这是一个通过MCP（模块化控制协议）提供QQ音乐搜索功能的测试服务器。该服务器允许您使用关键词搜索音乐曲目，并返回相关歌曲信息。

该demo仅用于测试和学习目的。

## 功能特点

- 支持MCP使用关键词搜索音乐曲目

## 环境要求

- 已安装了[uv](https://github.com/astral-sh/uv)
- Python 3.13

## 安装说明

1. 克隆此仓库
    ```bash
    git clone https://github.com/Samge0/mcp-qqmusic-test-server.git
    ```
2. 安装依赖：
   ```bash
   uv sync
   ```

## 使用方法

配置`mcp`：

```json
{
  "mcpServers": {
    "mcp-qqmusic-test-server": {
        "command": "uv",
        "args": [
            "--directory",
            "{put your local dir here}/mcp-qqmusic-test-server",
            "run",
            "main.py"
        ]
    }
  }
}
```

![image](https://github.com/user-attachments/assets/96a1d8b6-f527-4702-94b5-745287323648)

![image](https://github.com/user-attachments/assets/9826ab69-dbe5-47fd-9ba6-c809315351a3)


### 测试搜索音乐

<details> <summary>使用关键词搜索音乐曲目>></summary>

**函数：** `search_music`

**参数：**

- `keyword` (字符串，必需)：搜索关键词或短语
- `page` (整数，可选)：分页页码（默认值：1）
- `num` (整数，可选)：返回结果的最大数量（默认值：20）

**返回值：**

返回包含以下属性的对象数组：

- `id`：歌曲ID
- `mid`：音乐ID
- `name`：歌曲名称
- `pmid`：播放音乐ID
- `subtitle`：歌曲副标题
- `time_public`：发布时间
- `title`：歌曲标题

**示例响应：**

```json
[
  {
    "id": "123456",
    "mid": "001Qu4I30eVFYb",
    "name": "七里香",
    "pmid": "",
    "subtitle": "",
    "time_public": "2004-08-03",
    "title": "七里香"
  }
]
```

</details>
