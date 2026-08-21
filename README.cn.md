# awesome-meme

> 一个让 AI 变有趣的 skill — 30 个梗模板，一行命令生成。装上，你的 AI 就会玩梗了。

## 为什么

AI 能生成文字，但不会玩梗。awesome-meme 让任何 AI agent 都能创建和分享 meme——从程序员经典梗到中国网络文化。

**一行命令生成 meme：**

```bash
python3 meme_render.py distracted-boyfriend ZIG ME RUST
```

## 包含什么

- `data/text/` — 文本类 meme，按年整理（2025.yml、2026.yml...）
- `data/index.yml` — 图片类和名人类 meme 索引
- `data/spec/` — 每个 meme 的渲染规格：布局、文字槽位、坐标
- `skill/` — 自包含渲染器（Pillow + ImageMagick），稳定不随数据变

## 快速开始

```bash
# 1. 获取渲染器
curl -O https://raw.githubusercontent.com/edwinjhlee/awesome-meme/main/skill/scripts/meme_render.py

# 2. 安装依赖
pip install pillow pyyaml

# 3. 生成 meme（自动从 GitHub 下载规格和图片）
python3 meme_render.py this-is-fine "ERROR LOG" "THIS IS FINE"
```

或者用 x-cmd：

```bash
eval "$(curl https://get.x-cmd.com)"
x env use python
pip install pillow pyyaml
```

完整文档见 [skill/SKILL.md](skill/SKILL.md)。

## Meme 列表

### 文本类（直接输出，无需图片）

| ID | 名称 | 输出 |
|----|------|------|
| table-flip | 掀桌 | (╯°□°）╯︵ ┻━┻ |
| shrug | 耸肩 | ¯ (ツ)_/¯ |
| look-of-disapproval | 不赞同 | ಠ_ಠ |
| lenny-face | 猥琐脸 | ( ͡° ͜ʖ ͡°) |
| lgtm | LGTM | ✅ LGTM |
| panda-head-cry | 熊猫头流泪 | 😭 假装没事 |
| panda-head-doge | 熊猫头狗头 | 🐶 你说得对（狗头） |
| panda-head-work | 熊猫头加班 | 🐼 加班使我快乐（不是 |
| programmer-drink | 程序员喝茶 | 🍵 佛系喝茶，Bug 随它去吧 |
| bug-feature | 不是Bug是特性 | 🐛➡️✨ It's not a bug, it's a feature |
| friendship-boat | 友谊的小船 | ⛵ 友谊的小船说翻就翻 |

### 图片类（需要渲染器）

| ID | 名称 | 说明 |
|----|------|------|
| distracted-boyfriend | 分心男友 | 喜新厌旧 |
| drake-hotline-bling | 德雷克拒绝接受 | 二选一对比 |
| this-is-fine | 一切都好 | 崩溃但假装没事 |
| success-kid | 成功小子 | 庆祝小胜利 |
| roll-safe | 拍头思考 | 自以为聪明的烂主意 |
| expanding-brain | 膨胀的大脑 | 越来越离谱的递进 |
| woman-yelling-cat | 女人对猫大喊 | 情绪化反应 |
| hide-pain-harold | 隐藏痛苦的哈罗德 | 表面微笑内心崩溃 |
| doge | 狗狗表情 | 困惑、反讽赞美 |
| nyan-cat | 彩虹猫 | 无意义的快乐 |
| vim-exit | 怎么退出Vim | 被困住出不来 |
| it-works-why | 能跑就行别问为什么 | 别碰它能跑就行 |
| wtf-per-minute | 每分钟WTF数 | 代码质量指标 |
| code-review-guy | 代码审查狂人 | 吹毛求疵 |
| monday-deploy | 周一部署 | 别在这天部署 |
| stackoverflow-copy | 复制粘贴工程师 | CV工程师 |

### 名人类（谨慎使用）

| ID | 名称 | 说明 |
|----|------|------|
| zhenxiang | 真香 | 事前拒绝事后接受 |
| ge-you-tang | 葛优躺 | 彻底躺平 |
| ya-shi-la-nei | 鸭屎啦你 | 周星驰式吐槽 |

## 设计原则

- **纯数据** — 只有 YAML，不存图片
- **skill/数据分离** — 渲染器很少改动，规格独立更新
- **文本类按年整理** — 新梗每年更新，agent 拉当年文件即可
- **MIT 协议** — 自由使用和贡献

## Agent 使用指南

- **轻度使用** — 默认偶尔使用，试探性发送
- **看反应** — 用户反应好可以多用，反感就收手
- **文本优先** — 优先用文本类 meme，轻量不侵入
- **用户要求优先** — "发个梗" 或 "不要梗了" 以用户为准

详细指南见 [skill/SKILL.md](skill/SKILL.md)。

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md) — 三步添加一个 meme。

## 协议

[MIT](LICENSE)
