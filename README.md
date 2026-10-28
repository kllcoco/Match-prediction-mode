# 电竞赛事预测小模型（LOL + CS）

一个"玩具级"但认真做的电竞预测模型：会**联网同步赛果**、学**英雄联盟 / CS** 的历史比赛，
预测谁赢、几比几、BP 怎么禁，并且**用中文说出理由**。

## 一句话原理（猴子版）

1. **记分牌（Elo）**：每打一局，赢的人加分、输的人扣分；爆冷赢了加得多。队伍分 = 队伍本身 + 5 个选手的分。
2. **赛区水位**：不看世界赛也要比较 LCK 和 LCS 谁强 → 看**选手转会**：一个在韩国打中游的人去北美称霸，说明北美水位低。
3. **小公式（逻辑回归）**：把"实力分差、近期状态、经验、地图熟练度"等因素加权，算出胜率。权重是从几万场比赛里**学**出来的，不是拍脑袋。
4. **BP**：从真实的禁选记录里学"什么英雄会被 ban、会被拿"；CS 模拟地图禁选。
5. **观点**：哪个因素对胜率影响最大，就先说哪个理由；同时说反方风险和爆冷可能。

## 怎么用

```bash
pip install -r requirements.txt
```

预测一场（先联网同步最新赛果，再顺便搜网上新闻）：

```bash
python -m esports predict IG Gen.G --update --news
```

CS：

```bash
python -m esports predict Vitality Falcons --game cs
```

对话模式（本地，不调用任何外部 AI）：

```bash
python -m esports chat
```

可以问：`T1 打 Gen.G 谁赢`、`T1 打 BLG 比分`、`T1 vs BLG BP怎么ban`、`BLG 最近状态`、`切换 cs`。

其他：

```bash
python -m esports update            # 联网同步 LOL + CS 最新赛果
python -m esports search T1 Worlds  # 网页 + Liquipedia 搜索
python -m esports backtest lol      # 回测 S1-S15（严格模式）
python -m esports report            # 生成全部中文报告到 reports/
python -m esports.s16               # 预测今年 S16 并存档
python -m esports.s16 grade         # S16 打完后判卷
```

## 训练方式：先"闭卷考试"，再"开卷"

- **严格模式（闭卷）**：训练时**完全看不到**任何世界赛 / MSI / First Stand / CS Major 的比赛，
  站在每届大赛开打前预测 8 强 → 冠军，然后对答案。
- **完整模式（开卷）**：能看到往届大赛 + 本届小组赛/瑞士轮（就像真实的赛前分析）。
- 所有调参都只用「非大赛」比赛来评估，**不拿世界赛答案调参**。

## 成绩（回测）

| | 系列赛命中 | 4 强命中 | 冠军猜中 |
|---|---|---|---|
| 瞎猜 | 50% | 50% | 12.5% |
| LOL 严格（S1-S15） | 57.9% | 62.5% | 4/14 |
| LOL 完整 | 60.7% | 60.7% | 5/14 |
| CS 严格（23 届 Major） | 62.1% | 62.0% | 6/23 |
| CS 完整 | 62.7% | 62.0% | 7/23 |

逐届预测、每场 8 强的赛前观点、爆冷统计、BP 检验见 `reports/`。

### 说实话的部分

- **S1-S3 基本靠猜**：2011-2013 年能找到的比赛太少（S1 之前几乎没有正式比赛）。
- **T1 魔咒**：2022-2025 模型连续押 Gen.G，结果都是 T1 夺冠。模型专门学了"大赛型选手"特征，
  但国内季后赛数据里这个效应不明显，学出来的权重接近 0。
- **爆冷没法"预测准"**：好模型的标准是"说冷门有 30% 机会时，冷门真的约 30% 会赢"。见 `reports/upsets_and_bp.md`。
- **BP**：模型的 ban 位预测命中率约为随机的 4~5 倍，但没能超过"直接按版本热门猜"——
  世界赛常换新版本，职业队 ban 位主要跟版本走。
- 解说文字是"按模型账本说话"的模板生成，不是会自由聊天的大模型。

## 数据来源

| 数据 | 来源 |
|---|---|
| LOL 2014-2025 每局数据（含 BP、选手） | Oracle's Elixir（HuggingFace / Kaggle 公开镜像） |
| LOL 2011-2015、世界赛对阵、2026 实时赛果 | [Liquipedia](https://liquipedia.net)（CC BY-SA，按其 API 规则限速访问） |
| CS 2013-2026 比赛（含地图、阵容、veto） | Kaggle 公开的 HLTV 数据集（mateusdmachado、camilohernndez、nafisbarizki、ektarr） |

原始数据不进仓库，`python -m esports.sources` 会重新下载；整理好的数据在 `data/processed/`。

## 代码地图

| 文件 | 做什么 |
|---|---|
| `esports/engine.py` | Elo 评分 + 小型逻辑回归 |
| `esports/region.py` | 赛区水位模型（选手转会） |
| `esports/calib.py` | 跨赛区校准（用 IEM / EWC / 亚运等非 Riot 国际赛） |
| `esports/draft.py` / `veto.py` | LOL BP 模型 / CS 地图禁选 |
| `esports/backtest.py` | 回测、淘汰赛模拟 |
| `esports/explain.py` | 中文观点生成 |
| `esports/live.py` / `search.py` | 联网同步赛果 / 搜索 |
| `esports/predict.py` / `chat.py` / `s16.py` | 预测、对话、S16 预测存档与判卷 |
