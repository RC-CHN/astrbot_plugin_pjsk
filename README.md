# Sekai Stickers

Project Sekai 表情包制作插件 for AstrBot

基于 [nonebot-plugin-pjsk](https://github.com/Agnes4m/nonebot_plugin_pjsk) 移植

## 功能

- 生成 Project Sekai 风格的表情包
- 支持自定义文字、位置、角度、大小、颜色等参数
- 查看所有角色和表情 ID

## 安装

1. 将插件目录复制到 AstrBot 的 `data/plugins/` 目录
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```
3. 重启 AstrBot

## 使用方法

### 生成表情

```
pjsk [文字]              - 使用随机表情生成
pjsk -i <ID> [文字]      - 使用指定 ID 的表情
pjsk -h                  - 查看详细帮助
```

**参数说明：**
- `-i, --id` - 表情 ID
- `-x` - 文字 x 坐标
- `-y` - 文字 y 坐标
- `-r, --rotate` - 旋转角度
- `-s, --size` - 文字大小
- `-c, --color` - 文字颜色 (16进制)

### 查看表情列表

```
pjsk列表                 - 查看所有角色
pjsk列表 <角色名>        - 查看指定角色的表情 ID
```

## 示例

```
pjsk 你好世界
pjsk -i 1 测试文字
pjsk -i 5 -s 30 小字体
pjsk列表
pjsk列表 Miku
```

## 致谢

- 原项目: [nonebot-plugin-pjsk](https://github.com/Agnes4m/nonebot_plugin_pjsk)
- 表情资源: [sekai-stickers](https://github.com/TheOriginalAyaka/sekai-stickers)

## License

MIT License
