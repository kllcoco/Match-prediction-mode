# CS Major 回测 · 完整模式（看过往届大赛 + 当届小组赛）

- 系列赛预测命中率：**65.2%**（161 场；瞎猜 50%）
- 4 强命中：65.2%　决赛队伍命中：50.0%　冠军命中：**30.4%**（瞎猜 12.5%）
- 对真实冠军给出的平均夺冠概率：21.8%　对数损失：0.627（越低越好，瞎猜 0.693）

### EMS One Katowice 2014

训练数据截止：2014-03-13（之后的比赛模型都没见过）  
夺冠概率：NiP 23%，Virtus.pro 16%，LGB 14%，Complexity 12%  
**预测冠军：NiP**　｜　实际冠军：Virtus.pro ❌  
预测 4 强命中 4/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | NiP vs Complexity | NiP | 59% | NiP 2-1 | ✅ |
| R1M2 | Dignitas vs HellRaisers | Dignitas | 51% | Dignitas 2-0 | ✅ |
| R1M3 | Virtus.pro vs LDLC | Virtus.pro | 60% | Virtus.pro 2-0 | ✅ |
| R1M4 | fnatic vs LGB | LGB | 54% | LGB 1-2 | ✅ |
| R2M1 | NiP vs Dignitas | NiP | 65% | NiP 2-0 | ✅ |
| R2M2 | Virtus.pro vs LGB | Virtus.pro | 51% | Virtus.pro 2-1 | ✅ |
| R3M1 | NiP vs Virtus.pro | NiP | 57% | Virtus.pro 0-2 | ❌ |

**赛前观点（8 强）：**

- **NiP vs Complexity**：倾向 NiP（系列赛胜率 59%，最可能比分 NiP 2:0）。 理由：综合实力分 NiP 比 Complexity 高约 40 分。 总结：基本五五开，谁赢都不奇怪。
- **Dignitas vs HellRaisers**：我的判断：Dignitas 晋级（系列赛胜率 51%，最可能比分 Dignitas 2:0）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs LDLC**：我看好 Virtus.pro（系列赛胜率 60%，最可能比分 Virtus.pro 2:0）。 主要依据：从长期战绩算出来的实力分看，Virtus.pro 领先 LDLC 约 48 分。 总结：基本五五开，谁赢都不奇怪。
- **fnatic vs LGB**：我看好 LGB（系列赛胜率 54%，最可能比分 LGB 2:0）。 为什么：综合实力分 LGB 比 fnatic 高约 18 分。 总结：基本五五开，谁赢都不奇怪。

### ESL One Cologne 2014

训练数据截止：2014-08-16（之后的比赛模型都没见过）  
夺冠概率：fnatic 27%，NiP 16%，Virtus.pro 16%，LDLC 13%  
**预测冠军：fnatic**　｜　实际冠军：NiP ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | fnatic vs Natus Vincere | fnatic | 63% | fnatic 2-1 | ✅ |
| R1M2 | Epsilon vs Dignitas | Dignitas | 59% | Dignitas 0-2 | ✅ |
| R1M3 | LDLC vs Virtus.pro | Virtus.pro | 53% | LDLC 2-0 | ❌ |
| R1M4 | Cloud9 vs NiP | NiP | 83% | NiP 1-2 | ✅ |
| R2M1 | fnatic vs Dignitas | fnatic | 65% | fnatic 2-0 | ✅ |
| R2M2 | LDLC vs NiP | LDLC | 53% | NiP 1-2 | ❌ |
| R3M1 | fnatic vs NiP | fnatic | 66% | NiP 1-2 | ❌ |

**赛前观点（8 强）：**

- **fnatic vs Natus Vincere**：我看好 fnatic（系列赛胜率 63%，最可能比分 fnatic 2:0）。 理由：近期状态：fnatic 最近 9胜1负（状态火热），Natus Vincere 最近 5胜5负（状态一般）；综合实力分 fnatic 比 Natus Vincere 高约 62 分。 总结：有一定爆冷可能。
- **Epsilon vs Dignitas**：我看好 Dignitas（系列赛胜率 59%，最可能比分 Dignitas 2:0）。 理由：老牌队伍经验更足：Epsilon 打过 52 局，Dignitas 打过 107 局；从长期战绩算出来的实力分看，Dignitas 领先 Epsilon 约 69 分。 风险点：近期状态：Epsilon 最近 6胜4负（状态不错），Dignitas 最近 6胜4负（状态不错）。 总结：基本五五开，谁赢都不奇怪。
- **LDLC vs Virtus.pro**：我看好 Virtus.pro（系列赛胜率 53%，最可能比分 Virtus.pro 2:0）。 理由：Virtus.pro 的职业比赛经验更多（LDLC 108 局 / Virtus.pro 157 局）；综合实力分 Virtus.pro 比 LDLC 高约 55 分。 不过要注意：近期状态：LDLC 最近 7胜3负（状态不错），Virtus.pro 最近 7胜3负（状态不错）。 总结：基本五五开，谁赢都不奇怪。
- **Cloud9 vs NiP**：倾向 NiP（系列赛胜率 83%，最可能比分 NiP 2:0）。 理由：NiP 的职业比赛经验更多（Cloud9 4 局 / NiP 185 局）；从长期战绩算出来的实力分看，NiP 领先 Cloud9 约 109 分。 不过要注意：近期状态：Cloud9 最近 4胜0负（状态火热），NiP 最近 4胜6负（状态一般）。 总结：爆冷概率很低。

### DreamHack Winter 2014

训练数据截止：2014-11-28（之后的比赛模型都没见过）  
夺冠概率：Virtus.pro 25%，NiP 19%，fnatic 18%，LDLC 13%  
**预测冠军：fnatic**　｜　实际冠军：LDLC ❌  
预测 4 强命中 2/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | HellRaisers vs NiP | NiP | 62% | NiP 0-2 | ✅ |
| R1M2 | Virtus.pro vs PENTA | Virtus.pro | 85% | Virtus.pro 2-0 | ✅ |
| R1M3 | LDLC vs fnatic | fnatic | 54% | LDLC 2-1 | ❌ |
| R1M4 | Dignitas vs Natus Vincere | Dignitas | 53% | Natus Vincere 0-2 | ❌ |
| R2M1 | NiP vs Virtus.pro | NiP | 50% | NiP 2-1 | ✅ |
| R2M2 | LDLC vs Natus Vincere | LDLC | 58% | LDLC 2-0 | ✅ |
| R3M1 | NiP vs LDLC | NiP | 53% | LDLC 1-2 | ❌ |

**赛前观点（8 强）：**

- **HellRaisers vs NiP**：我的判断：NiP 晋级（系列赛胜率 62%，最可能比分 NiP 2:0）。 为什么：老牌队伍经验更足：HellRaisers 打过 186 局，NiP 打过 262 局；NiP 最近手感比对手好（HellRaisers 7-3，NiP 9-1，比赛结果都好于赛前预期）；NiP 整体硬实力更强（实力分高 55）。 总结：有一定爆冷可能。
- **Virtus.pro vs PENTA**：倾向 Virtus.pro（系列赛胜率 85%，最可能比分 Virtus.pro 2:0）。 为什么：Virtus.pro 的职业比赛经验更多（Virtus.pro 272 局 / PENTA 47 局）；近期状态：Virtus.pro 最近 8胜2负（状态火热），PENTA 最近 4胜6负（状态一般）；Virtus.pro 整体硬实力更强（实力分高 121）。 总结：爆冷概率很低。
- **LDLC vs fnatic**：我看好 fnatic（系列赛胜率 54%，最可能比分 fnatic 2:0）。 为什么：fnatic 整体硬实力更强（实力分高 99）；老牌队伍经验更足：LDLC 打过 211 局，fnatic 打过 277 局。 不过要注意：近期状态：LDLC 最近 8胜2负（状态火热），fnatic 最近 7胜3负（状态不错）。 总结：基本五五开，谁赢都不奇怪。
- **Dignitas vs Natus Vincere**：倾向 Dignitas（系列赛胜率 53%，最可能比分 Dignitas 2:0）。 为什么：Dignitas 整体硬实力更强（实力分高 62）；近期状态：Dignitas 最近 6胜4负（状态不错），Natus Vincere 最近 5胜5负（状态一般）。 风险点：老牌队伍经验更足：Dignitas 打过 178 局，Natus Vincere 打过 235 局。 总结：基本五五开，谁赢都不奇怪。

### ESL One Katowice 2015

训练数据截止：2015-03-12（之后的比赛模型都没见过）  
夺冠概率：Virtus.pro 28%，NiP 26%，fnatic 25%，Natus Vincere 11%  
**预测冠军：fnatic**　｜　实际冠军：fnatic ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | fnatic vs PENTA | fnatic | 73% | fnatic 2-0 | ✅ |
| R1M2 | Virtus.pro vs Keyd | Virtus.pro | 93% | Virtus.pro 2-1 | ✅ |
| R1M3 | Envy vs Natus Vincere | Natus Vincere | 61% | Envy 2-1 | ❌ |
| R1M4 | NiP vs TSM | NiP | 73% | NiP 2-1 | ✅ |
| R2M1 | fnatic vs Virtus.pro | fnatic | 54% | fnatic 2-0 | ✅ |
| R2M2 | Envy vs NiP | NiP | 73% | NiP 0-2 | ✅ |
| R3M1 | fnatic vs NiP | fnatic | 51% | fnatic 2-1 | ✅ |

**赛前观点（8 强）：**

- **fnatic vs PENTA**：倾向 fnatic（系列赛胜率 73%，最可能比分 fnatic 2:0）。 主要依据：综合实力分 fnatic 比 PENTA 高约 192 分；老牌队伍经验更足：fnatic 打过 355 局，PENTA 打过 134 局；fnatic 最近手感比对手好（fnatic 6-4，PENTA 2-8，比赛结果都好于赛前预期）。 总结：有一定爆冷可能。
- **Virtus.pro vs Keyd**：倾向 Virtus.pro（系列赛胜率 93%，最可能比分 Virtus.pro 2:0）。 主要依据：Virtus.pro 的职业比赛经验更多（Virtus.pro 374 局 / Keyd 0 局）；综合实力分 Virtus.pro 比 Keyd 高约 142 分。 风险点：Keyd 最近手感比对手好（Virtus.pro 7-3，Keyd 0-0，比赛结果都好于赛前预期）。 总结：爆冷概率很低。
- **Envy vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 61%，最可能比分 Natus Vincere 2:0）。 理由：Natus Vincere 的职业比赛经验更多（Envy 42 局 / Natus Vincere 286 局）；Natus Vincere 整体硬实力更强（实力分高 94）。 但是：近期状态：Envy 最近 6胜4负（状态不错），Natus Vincere 最近 2胜8负（状态低迷）。 总结：基本五五开，谁赢都不奇怪。
- **NiP vs TSM**：倾向 NiP（系列赛胜率 73%，最可能比分 NiP 2:0）。 为什么：老牌队伍经验更足：NiP 打过 322 局，TSM 打过 23 局；从长期战绩算出来的实力分看，NiP 领先 TSM 约 113 分。 风险点：近期状态：NiP 最近 7胜3负（状态不错），TSM 最近 7胜3负（状态不错）。 总结：有一定爆冷可能。

### ESL One Cologne 2015

训练数据截止：2015-08-22（之后的比赛模型都没见过）  
夺冠概率：Envy 22%，fnatic 21%，NiP 16%，Virtus.pro 13%  
**预测冠军：Envy**　｜　实际冠军：fnatic ❌  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Envy vs Natus Vincere | Envy | 61% | Envy 2-0 | ✅ |
| R1M2 | TSM vs Kinguin | TSM | 52% | TSM 2-0 | ✅ |
| R1M3 | Virtus.pro vs NiP | NiP | 53% | Virtus.pro 2-0 | ❌ |
| R1M4 | fnatic vs Luminosity | fnatic | 69% | fnatic 2-0 | ✅ |
| R2M1 | Envy vs TSM | Envy | 66% | Envy 2-1 | ✅ |
| R2M2 | Virtus.pro vs fnatic | fnatic | 54% | fnatic 1-2 | ✅ |
| R3M1 | Envy vs fnatic | Envy | 52% | fnatic 0-2 | ❌ |

**赛前观点（8 强）：**

- **Envy vs Natus Vincere**：我的判断：Envy 晋级（系列赛胜率 61%，最可能比分 Envy 2:0）。 理由：近期状态：Envy 最近 8胜2负（状态火热），Natus Vincere 最近 5胜5负（状态一般）；Envy 整体硬实力更强（实力分高 40）。 但是：Natus Vincere 的职业比赛经验更多（Envy 242 局 / Natus Vincere 511 局）。 总结：基本五五开，谁赢都不奇怪。
- **TSM vs Kinguin**：倾向 TSM（系列赛胜率 52%，最可能比分 TSM 2:0）。 为什么：老牌队伍经验更足：TSM 打过 241 局，Kinguin 打过 76 局；从长期战绩算出来的实力分看，TSM 领先 Kinguin 约 42 分。 不过要注意：Kinguin 最近手感比对手好（TSM 5-5，Kinguin 7-3，比赛结果都好于赛前预期）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs NiP**：倾向 NiP（系列赛胜率 53%，最可能比分 NiP 2:0）。 为什么：NiP 最近手感比对手好（Virtus.pro 6-4，NiP 7-3，比赛结果都好于赛前预期）。 但是：Virtus.pro 的职业比赛经验更多（Virtus.pro 592 局 / NiP 481 局）。 总结：基本五五开，谁赢都不奇怪。
- **fnatic vs Luminosity**：我看好 fnatic（系列赛胜率 69%，最可能比分 fnatic 2:0）。 为什么：老牌队伍经验更足：fnatic 打过 540 局，Luminosity 打过 121 局；从长期战绩算出来的实力分看，fnatic 领先 Luminosity 约 164 分。 风险点：Luminosity 最近手感比对手好（fnatic 5-5，Luminosity 4-6，比赛结果都好于赛前预期）。 总结：有一定爆冷可能。

### DreamHack Open Cluj-Napoca 2015

训练数据截止：2015-10-28（之后的比赛模型都没见过）  
夺冠概率：Envy 17%，NiP 15%，Virtus.pro 15%，fnatic 13%  
**预测冠军：Envy**　｜　实际冠军：Envy ✅  
预测 4 强命中 2/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Envy vs fnatic | Envy | 54% | Envy 2-1 | ✅ |
| R1M2 | Virtus.pro vs G2 | Virtus.pro | 54% | G2 0-2 | ❌ |
| R1M3 | TSM vs NiP | NiP | 53% | NiP 0-2 | ✅ |
| R1M4 | Luminosity vs Natus Vincere | Luminosity | 52% | Natus Vincere 0-2 | ❌ |
| R2M1 | Envy vs G2 | Envy | 56% | Envy 2-1 | ✅ |
| R2M2 | NiP vs Natus Vincere | NiP | 60% | Natus Vincere 0-2 | ❌ |
| R3M1 | Envy vs Natus Vincere | Envy | 64% | Envy 2-0 | ✅ |

**赛前观点（8 强）：**

- **Envy vs fnatic**：倾向 Envy（系列赛胜率 54%，最可能比分 Envy 2:0）。 风险点：fnatic 的职业比赛经验更多（Envy 302 局 / fnatic 614 局）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs G2**：我的判断：Virtus.pro 晋级（系列赛胜率 54%，最可能比分 Virtus.pro 2:0）。 为什么：老牌队伍经验更足：Virtus.pro 打过 679 局，G2 打过 254 局；Virtus.pro 整体硬实力更强（实力分高 41）。 风险点：G2 最近手感比对手好（Virtus.pro 6-4，G2 6-4，比赛结果都好于赛前预期）。 总结：基本五五开，谁赢都不奇怪。
- **TSM vs NiP**：我看好 NiP（系列赛胜率 53%，最可能比分 NiP 2:0）。 主要依据：NiP 的职业比赛经验更多（TSM 335 局 / NiP 526 局）；NiP 整体硬实力更强（实力分高 34）。 不过要注意：TSM 最近手感比对手好（TSM 6-4，NiP 7-3，比赛结果都好于赛前预期）。 总结：基本五五开，谁赢都不奇怪。
- **Luminosity vs Natus Vincere**：我的判断：Luminosity 晋级（系列赛胜率 52%，最可能比分 Luminosity 2:0）。 理由：近期状态：Luminosity 最近 7胜3负（状态不错），Natus Vincere 最近 4胜6负（状态一般）。 风险点：老牌队伍经验更足：Luminosity 打过 202 局，Natus Vincere 打过 573 局。 总结：基本五五开，谁赢都不奇怪。

### MLG Columbus 2016

训练数据截止：2016-04-01（之后的比赛模型都没见过）  
夺冠概率：Luminosity 34%，fnatic 23%，Natus Vincere 20%，Liquid 8%  
**预测冠军：fnatic**　｜　实际冠军：Luminosity ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs NiP | Natus Vincere | 62% | Natus Vincere 2-0 | ✅ |
| R1M2 | Astralis vs fnatic | fnatic | 69% | Astralis 2-0 | ❌ |
| R1M3 | Liquid vs CLG | Liquid | 67% | Liquid 2-0 | ✅ |
| R1M4 | Luminosity vs Virtus.pro | Luminosity | 87% | Luminosity 2-1 | ✅ |
| R2M1 | Natus Vincere vs Astralis | Natus Vincere | 68% | Natus Vincere 2-0 | ✅ |
| R2M2 | Liquid vs Luminosity | Luminosity | 69% | Luminosity 0-2 | ✅ |
| R3M1 | Natus Vincere vs Luminosity | Natus Vincere | 51% | Luminosity 0-2 | ❌ |

**赛前观点（8 强）：**

- **Natus Vincere vs NiP**：倾向 Natus Vincere（系列赛胜率 62%，最可能比分 Natus Vincere 2:0）。 为什么：Natus Vincere 选手们对线期 KDA 压制更明显；Natus Vincere 最近手感比对手好（Natus Vincere 9-1，NiP 7-3，比赛结果都好于赛前预期）；综合实力分 Natus Vincere 比 NiP 高约 20 分。 位置对比：打野 guardian 近期表现优于 threat；辅助 seized 近期表现优于 friberg。 地图BP推演：Natus Vincere禁Cache，NiP禁Train；Natus Vincere选Cobblestone（Natus Vincere胜率59%），NiP选Mirage（Natus Vincere胜率58%）；决胜图 Inferno（Natus Vincere胜率58%）。 总结：有一定爆冷可能。
- **Astralis vs fnatic**：我的判断：fnatic 晋级（系列赛胜率 69%，最可能比分 fnatic 2:0）。 主要依据：fnatic 的职业比赛经验更多（Astralis 60 局 / fnatic 718 局）；fnatic 整体硬实力更强（实力分高 130）；fnatic 选手们对线期 KDA 压制更明显。 风险点：近期状态：Astralis 最近 6胜4负（状态不错），fnatic 最近 8胜2负（状态火热）。 位置对比：辅助 olofmeister 近期表现优于 karrigan；下路 flusha 近期表现优于 dupreeh；中单 device 近期表现优于 dennis。 地图BP推演：Astralis禁Inferno，fnatic禁Mirage；Astralis选Train（Astralis胜率38%），fnatic选Cobblestone（Astralis胜率36%）；决胜图 Cache（Astralis胜率37%）。 总结：有一定爆冷可能。
- **Liquid vs CLG**：倾向 Liquid（系列赛胜率 67%，最可能比分 Liquid 2:0）。 主要依据：Liquid 选手们对线期 KDA 压制更明显；近期状态：Liquid 最近 7胜3负（状态不错），CLG 最近 5胜5负（状态一般）；综合实力分 Liquid 比 CLG 高约 38 分。 位置对比：上单 elige 近期表现优于 fugly；中单 jdm64 近期表现优于 adren；辅助 s1mple 近期表现优于 tarik。 地图BP推演：Liquid禁Overpass，CLG禁Cache；Liquid选Dust2（Liquid胜率62%），CLG选Train（Liquid胜率61%）；决胜图 Inferno（Liquid胜率61%）。 总结：有一定爆冷可能。
- **Luminosity vs Virtus.pro**：我看好 Luminosity（系列赛胜率 87%，最可能比分 Luminosity 2:0）。 为什么：Luminosity 选手们对线期 KDA 压制更明显；综合实力分 Luminosity 比 Virtus.pro 高约 150 分；近期状态：Luminosity 最近 9胜1负（状态火热），Virtus.pro 最近 4胜6负（状态一般）。 风险点：老牌队伍经验更足：Luminosity 打过 311 局，Virtus.pro 打过 755 局。 位置对比：中单 coldzera 近期表现优于 taz；辅助 fnx 近期表现优于 pashabiceps；下路 fer 近期表现优于 byali。 地图BP推演：Luminosity禁Dust2，Virtus.pro禁Overpass；Luminosity选Mirage（Luminosity胜率78%），Virtus.pro选Cache（Luminosity胜率77%）；决胜图 Cobblestone（Luminosity胜率78%）。 总结：爆冷概率很低。

### ESL One Cologne 2016

训练数据截止：2016-07-08（之后的比赛模型都没见过）  
夺冠概率：Natus Vincere 27%，fnatic 24%，SK 21%，Virtus.pro 12%  
**预测冠军：Natus Vincere**　｜　实际冠军：SK ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Virtus.pro vs Astralis | Virtus.pro | 63% | Virtus.pro 2-0 | ✅ |
| R1M2 | SK vs FlipSid3 | SK | 69% | SK 2-0 | ✅ |
| R1M3 | Natus Vincere vs Liquid | Natus Vincere | 67% | Liquid 1-2 | ❌ |
| R1M4 | Gambit vs fnatic | fnatic | 80% | fnatic 0-2 | ✅ |
| R2M1 | Virtus.pro vs SK | SK | 58% | SK 1-2 | ✅ |
| R2M2 | Liquid vs fnatic | fnatic | 60% | Liquid 2-0 | ❌ |
| R3M1 | SK vs Liquid | SK | 58% | SK 2-0 | ✅ |

**赛前观点（8 强）：**

- **Virtus.pro vs Astralis**：倾向 Virtus.pro（系列赛胜率 63%，最可能比分 Virtus.pro 2:0）。 为什么：老牌队伍经验更足：Virtus.pro 打过 830 局，Astralis 打过 118 局；Virtus.pro 最近手感比对手好（Virtus.pro 6-4，Astralis 3-7，比赛结果都好于赛前预期）；Virtus.pro 选手们对线期 KDA 压制更明显。 风险点：Astralis 整体硬实力更强（实力分高 42）。 位置对比：下路 byali 近期表现优于 karrigan；上单 xyp9x 近期表现优于 neo；辅助 pashabiceps 近期表现优于 zonic。 地图BP推演：Virtus.pro禁Overpass，Astralis禁Cobblestone；Virtus.pro选Train（Virtus.pro胜率61%），Astralis选Cache（Virtus.pro胜率57%）；决胜图 Inferno（Virtus.pro胜率60%）。 总结：有一定爆冷可能。
- **SK vs FlipSid3**：我看好 SK（系列赛胜率 69%，最可能比分 SK 2:0）。 为什么：SK 选手们对线期 KDA 压制更明显；从长期战绩算出来的实力分看，SK 领先 FlipSid3 约 133 分。 但是：FlipSid3 这批首发最近赢得更多。 位置对比：上单 fallen 近期表现优于 b1ad3；辅助 fnx 近期表现优于 waylander；打野 taco 近期表现优于 shara。 地图BP推演：SK禁Mirage，FlipSid3禁Inferno；SK选Train（SK胜率65%），FlipSid3选Overpass（SK胜率62%）；决胜图 Dust2（SK胜率63%）。 总结：有一定爆冷可能。
- **Natus Vincere vs Liquid**：我看好 Natus Vincere（系列赛胜率 67%，最可能比分 Natus Vincere 2:0）。 为什么：综合实力分 Natus Vincere 比 Liquid 高约 127 分；Natus Vincere 选手们对线期 KDA 压制更明显；Natus Vincere 的职业比赛经验更多（Natus Vincere 724 局 / Liquid 411 局）。 但是：Liquid 这批首发最近赢得更多。 位置对比：打野 guardian 近期表现优于 hiko；上单 edward 近期表现优于 elige；下路 flamie 近期表现优于 nitr0。 地图BP推演：Natus Vincere禁Cache，Liquid禁Overpass；Natus Vincere选Train（Natus Vincere胜率63%），Liquid选Cobblestone（Natus Vincere胜率60%）；决胜图 Mirage（Natus Vincere胜率60%）。 总结：有一定爆冷可能。
- **Gambit vs fnatic**：倾向 fnatic（系列赛胜率 80%，最可能比分 fnatic 2:0）。 理由：综合实力分 fnatic 比 Gambit 高约 214 分；fnatic 的职业比赛经验更多（Gambit 96 局 / fnatic 775 局）；fnatic 选手们对线期 KDA 压制更明显。 不过要注意：Gambit 这批首发最近赢得更多。 位置对比：辅助 olofmeister 近期表现优于 spaze；中单 dennis 近期表现优于 hooch；上单 adren 近期表现优于 jw。 地图BP推演：Gambit禁Inferno，fnatic禁Train；Gambit选Overpass（Gambit胜率30%），fnatic选Cache（Gambit胜率28%）；决胜图 Dust2（Gambit胜率29%）。 总结：有一定爆冷可能。

### ELEAGUE Major 2017

训练数据截止：2017-01-22（之后的比赛模型都没见过）  
夺冠概率：Astralis 50%，Virtus.pro 26%，SK 7%，Gambit 6%  
**预测冠军：Astralis**　｜　实际冠军：Astralis ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs Astralis | Astralis | 83% | Astralis 1-2 | ✅ |
| R1M2 | fnatic vs Gambit | Gambit | 56% | fnatic 2-1 | ❌ |
| R1M3 | Virtus.pro vs North | Virtus.pro | 95% | Virtus.pro 2-1 | ✅ |
| R1M4 | FaZe vs SK | SK | 54% | SK 1-2 | ✅ |
| R2M1 | Astralis vs fnatic | Astralis | 83% | Astralis 2-0 | ✅ |
| R2M2 | Virtus.pro vs SK | Virtus.pro | 63% | Virtus.pro 2-0 | ✅ |
| R3M1 | Astralis vs Virtus.pro | Astralis | 70% | Astralis 2-1 | ✅ |

**赛前观点（8 强）：**

- **Natus Vincere vs Astralis**：我看好 Astralis（系列赛胜率 83%，最可能比分 Astralis 2:0）。 为什么：Astralis 选手们对线期 KDA 压制更明显；从长期战绩算出来的实力分看，Astralis 领先 Natus Vincere 约 131 分；Astralis 最近手感比对手好（Natus Vincere 4-6，Astralis 8-2，比赛结果都好于赛前预期）。 不过要注意：老牌队伍经验更足：Natus Vincere 打过 795 局，Astralis 打过 228 局。 位置对比：中单 device 近期表现优于 flamie；上单 kjaerbye 近期表现优于 edward；打野 xyp9x 近期表现优于 guardian。 地图BP推演：Natus Vincere禁Mirage，Astralis禁Cobblestone；Natus Vincere选Overpass（Natus Vincere胜率28%），Astralis选Cache（Natus Vincere胜率25%）；决胜图 Train（Natus Vincere胜率26%）。 总结：爆冷概率很低。
- **fnatic vs Gambit**：我的判断：Gambit 晋级（系列赛胜率 56%，最可能比分 Gambit 2:0）。 为什么：Gambit 选手们对线期 KDA 压制更明显；Gambit 最近手感比对手好（fnatic 4-6，Gambit 8-2，比赛结果都好于赛前预期）。 风险点：老牌队伍经验更足：fnatic 打过 851 局，Gambit 打过 205 局。 位置对比：中单 hobbit 近期表现优于 disco doplan；辅助 mou 近期表现优于 twist；上单 adren 近期表现优于 krimz。 地图BP推演：fnatic禁Dust2，Gambit禁Cache；fnatic选Nuke（fnatic胜率47%），Gambit选Cobblestone（fnatic胜率44%）；决胜图 Train（fnatic胜率46%）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs North**：我看好 Virtus.pro（系列赛胜率 95%，最可能比分 Virtus.pro 2:0）。 主要依据：Virtus.pro 的职业比赛经验更多（Virtus.pro 956 局 / North 0 局）；Virtus.pro 整体硬实力更强（实力分高 240）；近期状态：Virtus.pro 最近 8胜2负（状态火热），North 最近 0胜0负（暂无近期数据）。 地图BP推演：Virtus.pro禁Cache，North禁Cobblestone；Virtus.pro选Mirage（Virtus.pro胜率88%），North选Overpass（Virtus.pro胜率86%）；决胜图 Dust2（Virtus.pro胜率87%）。 总结：爆冷概率很低。
- **FaZe vs SK**：倾向 SK（系列赛胜率 54%，最可能比分 SK 2:0）。 为什么：老牌队伍经验更足：FaZe 打过 210 局，SK 打过 467 局；SK 选手们对线期 KDA 压制更明显；SK 这批首发最近赢得更多。 不过要注意：FaZe 最近手感比对手好（FaZe 8-2，SK 4-6，比赛结果都好于赛前预期）。 位置对比：中单 coldzera 近期表现优于 karrigan；辅助 rain 近期表现优于 fox；打野 allu 近期表现优于 taco。 地图BP推演：FaZe禁Train，SK禁Mirage；FaZe选Nuke（FaZe胜率49%），SK选Cobblestone（FaZe胜率46%）；决胜图 Dust2（FaZe胜率47%）。 总结：基本五五开，谁赢都不奇怪。

### PGL Major Krakow 2017

训练数据截止：2017-07-21（之后的比赛模型都没见过）  
夺冠概率：SK 41%，BIG 18%，Astralis 12%，Gambit 8%  
**预测冠军：SK**　｜　实际冠军：Gambit ❌  
预测 4 强命中 1/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Gambit vs fnatic | Gambit | 54% | Gambit 2-0 | ✅ |
| R1M2 | SK vs Astralis | SK | 68% | Astralis 0-2 | ❌ |
| R1M3 | BIG vs Immortals | BIG | 66% | Immortals 1-2 | ❌ |
| R1M4 | North vs Virtus.pro | North | 63% | Virtus.pro 0-2 | ❌ |
| R2M1 | Gambit vs Astralis | Astralis | 60% | Gambit 2-1 | ❌ |
| R2M2 | Immortals vs Virtus.pro | Immortals | 61% | Immortals 2-0 | ✅ |
| R3M1 | Gambit vs Immortals | Gambit | 60% | Gambit 2-1 | ✅ |

**赛前观点（8 强）：**

- **Gambit vs fnatic**：倾向 Gambit（系列赛胜率 54%，最可能比分 Gambit 2:0）。 理由：Gambit 选手们对线期 KDA 压制更明显；近期状态：Gambit 最近 7胜3负（状态不错），fnatic 最近 5胜5负（状态一般）。 但是：综合实力分 fnatic 比 Gambit 高约 59 分。 位置对比：辅助 mou 近期表现优于 olofmeister；中单 hobbit 近期表现优于 dennis；上单 adren 近期表现优于 jw。 地图BP推演：Gambit禁Cache，fnatic禁Train；Gambit选Cobblestone（Gambit胜率55%），fnatic选Mirage（Gambit胜率50%）；决胜图 Nuke（Gambit胜率52%）。 总结：基本五五开，谁赢都不奇怪。
- **SK vs Astralis**：倾向 SK（系列赛胜率 68%，最可能比分 SK 2:0）。 为什么：综合实力分 SK 比 Astralis 高约 67 分；SK 选手们对线期 KDA 压制更明显；老牌队伍经验更足：SK 打过 605 局，Astralis 打过 340 局。 但是：Astralis 这批首发最近赢得更多。 位置对比：辅助 fer 近期表现优于 gla1ve；中单 coldzera 近期表现优于 device；打野 xyp9x 近期表现优于 taco。 地图BP推演：SK禁Overpass，Astralis禁Cobblestone；SK选Train（SK胜率64%），Astralis选Mirage（SK胜率60%）；决胜图 Inferno（SK胜率63%）。 总结：有一定爆冷可能。
- **BIG vs Immortals**：我的判断：BIG 晋级（系列赛胜率 66%，最可能比分 BIG 2:0）。 为什么：BIG 最近手感比对手好（BIG 9-1，Immortals 5-5，比赛结果都好于赛前预期）；BIG 选手们对线期 KDA 压制更明显；BIG 整体硬实力更强（实力分高 24）。 不过要注意：Immortals 的职业比赛经验更多（BIG 121 局 / Immortals 268 局）。 位置对比：辅助 tabsen 近期表现优于 steel；上单 hen1 近期表现优于 legija；下路 nex 近期表现优于 kngv-。 地图BP推演：BIG禁Mirage，Immortals禁Train；BIG选Cache（BIG胜率63%），Immortals选Overpass（BIG胜率59%）；决胜图 Nuke（BIG胜率61%）。 总结：有一定爆冷可能。
- **North vs Virtus.pro**：倾向 North（系列赛胜率 63%，最可能比分 North 2:0）。 理由：从长期战绩算出来的实力分看，North 领先 Virtus.pro 约 136 分；North 选手们对线期 KDA 压制更明显。 但是：Virtus.pro 的职业比赛经验更多（North 99 局 / Virtus.pro 1059 局）。 位置对比：辅助 k0nfig 近期表现优于 pashabiceps；中单 aizy 近期表现优于 taz；下路 cajunb 近期表现优于 byali。 地图BP推演：North禁Train，Virtus.pro禁Overpass；North选Inferno（North胜率61%），Virtus.pro选Mirage（North胜率57%）；决胜图 Cobblestone（North胜率58%）。 总结：有一定爆冷可能。

### ELEAGUE Major 2018

训练数据截止：2018-01-12（之后的比赛模型都没见过）  
夺冠概率：SK 32%，mousesports 20%，FaZe 20%，Natus Vincere 12%  
**预测冠军：SK**　｜　实际冠军：Cloud9 ❌  
预测 4 强命中 4/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | FaZe vs mousesports | FaZe | 50% | FaZe 2-0 | ✅ |
| R1M2 | Natus Vincere vs Quantum Bellator Fire | Natus Vincere | 87% | Natus Vincere 2-0 | ✅ |
| R1M3 | G2 vs Cloud9 | Cloud9 | 62% | Cloud9 0-2 | ✅ |
| R1M4 | SK vs fnatic | SK | 71% | SK 2-1 | ✅ |
| R2M1 | FaZe vs Natus Vincere | FaZe | 67% | FaZe 2-0 | ✅ |
| R2M2 | Cloud9 vs SK | SK | 72% | Cloud9 2-1 | ❌ |
| R3M1 | FaZe vs Cloud9 | FaZe | 68% | Cloud9 1-2 | ❌ |

**赛前观点（8 强）：**

- **FaZe vs mousesports**：倾向 FaZe（系列赛胜率 50%，最可能比分 FaZe 0:2）。 为什么：FaZe 整体硬实力更强（实力分高 61）；FaZe 这批首发最近赢得更多。 但是：mousesports 选手们对线期 KDA 压制更明显。 位置对比：下路 s1mple 近期表现优于 olofmeister；中单 ropz 近期表现优于 karrigan；上单 guardian 近期表现优于 styko。 地图BP推演：FaZe禁Cobblestone，mousesports禁Overpass；FaZe选Inferno（FaZe胜率53%），mousesports选Nuke（FaZe胜率47%）；决胜图 Train（FaZe胜率49%）。 总结：基本五五开，谁赢都不奇怪。
- **Natus Vincere vs Quantum Bellator Fire**：倾向 Natus Vincere（系列赛胜率 87%，最可能比分 Natus Vincere 2:0）。 理由：综合实力分 Natus Vincere 比 Quantum Bellator Fire 高约 189 分；Natus Vincere 选手们对线期 KDA 压制更明显；老牌队伍经验更足：Natus Vincere 打过 961 局，Quantum Bellator Fire 打过 171 局。 但是：Quantum Bellator Fire 这批首发最近赢得更多。 位置对比：辅助 s1mple 近期表现优于 waterfallz；中单 electronic 近期表现优于 balblna；打野 kvik 近期表现优于 zeus。 地图BP推演：Natus Vincere禁Mirage，Quantum Bellator Fire禁Train；Natus Vincere选Overpass（Natus Vincere胜率79%），Quantum Bellator Fire选Inferno（Natus Vincere胜率77%）；决胜图 Nuke（Natus Vincere胜率77%）。 总结：爆冷概率很低。
- **G2 vs Cloud9**：倾向 Cloud9（系列赛胜率 62%，最可能比分 Cloud9 2:0）。 理由：Cloud9 选手们对线期 KDA 压制更明显；Cloud9 整体硬实力更强（实力分高 43）。 但是：G2 这批首发最近赢得更多。 位置对比：辅助 tarik 近期表现优于 shox；打野 skadoodle 近期表现优于 apex；下路 kennys 近期表现优于 autimatic。 地图BP推演：G2禁Train，Cloud9禁Nuke；G2选Inferno（G2胜率43%），Cloud9选Mirage（G2胜率41%）；决胜图 Cobblestone（G2胜率42%）。 总结：基本五五开，谁赢都不奇怪。
- **SK vs fnatic**：我的判断：SK 晋级（系列赛胜率 71%，最可能比分 SK 2:0）。 主要依据：从长期战绩算出来的实力分看，SK 领先 fnatic 约 83 分；SK 选手们对线期 KDA 压制更明显；近期状态：SK 最近 8胜2负（状态火热），fnatic 最近 5胜5负（状态一般）。 但是：fnatic 这批首发最近赢得更多。 位置对比：上单 fallen 近期表现优于 golden；下路 coldzera 近期表现优于 lekr0；辅助 flusha 近期表现优于 fer。 地图BP推演：SK禁Inferno，fnatic禁Overpass；SK选Cobblestone（SK胜率67%），fnatic选Nuke（SK胜率62%）；决胜图 Mirage（SK胜率65%）。 总结：有一定爆冷可能。

### FACEIT Major 2018

训练数据截止：2018-09-20（之后的比赛模型都没见过）  
夺冠概率：Astralis 45%，Natus Vincere 18%，Liquid 18%，Complexity 9%  
**预测冠军：Astralis**　｜　实际冠军：Astralis ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Complexity vs MIBR | Complexity | 68% | MIBR 0-2 | ❌ |
| R1M2 | BIG vs Natus Vincere | Natus Vincere | 70% | Natus Vincere 0-2 | ✅ |
| R1M3 | Liquid vs HellRaisers | Liquid | 75% | Liquid 2-1 | ✅ |
| R1M4 | Astralis vs FaZe | Astralis | 80% | Astralis 2-0 | ✅ |
| R2M1 | MIBR vs Natus Vincere | Natus Vincere | 77% | Natus Vincere 0-2 | ✅ |
| R2M2 | Liquid vs Astralis | Astralis | 68% | Astralis 0-2 | ✅ |
| R3M1 | Natus Vincere vs Astralis | Astralis | 70% | Astralis 0-2 | ✅ |

**赛前观点（8 强）：**

- **Complexity vs MIBR**：我看好 Complexity（系列赛胜率 68%，最可能比分 Complexity 2:0）。 理由：老牌队伍经验更足：Complexity 打过 625 局，MIBR 打过 34 局；从长期战绩算出来的实力分看，Complexity 领先 MIBR 约 46 分；近期状态：Complexity 最近 8胜2负（状态火热），MIBR 最近 5胜5负（状态一般）。 但是：MIBR 选手们对线期 KDA 压制更明显。 位置对比：中单 coldzera 近期表现优于 dephh；辅助 yay 近期表现优于 tarik；上单 fallen 近期表现优于 android。 地图BP推演：Complexity禁Overpass，MIBR禁Mirage；Complexity选Cache（Complexity胜率65%），MIBR选Dust2（Complexity胜率60%）；决胜图 Train（Complexity胜率62%）。 总结：有一定爆冷可能。
- **BIG vs Natus Vincere**：我看好 Natus Vincere（系列赛胜率 70%，最可能比分 Natus Vincere 2:0）。 为什么：Natus Vincere 整体硬实力更强（实力分高 116）；老牌队伍经验更足：BIG 打过 324 局，Natus Vincere 打过 1132 局；Natus Vincere 这批首发最近赢得更多。 风险点：BIG 最近手感比对手好（BIG 7-3，Natus Vincere 5-5，比赛结果都好于赛前预期）。 位置对比：辅助 s1mple 近期表现优于 tizian；上单 gob b 近期表现优于 edward；下路 tabsen 近期表现优于 flamie。 地图BP推演：BIG禁Train，Natus Vincere禁Dust2；BIG选Cache（BIG胜率39%），Natus Vincere选Mirage（BIG胜率32%）；决胜图 Nuke（BIG胜率38%）。 总结：有一定爆冷可能。
- **Liquid vs HellRaisers**：我的判断：Liquid 晋级（系列赛胜率 75%，最可能比分 Liquid 2:0）。 为什么：从长期战绩算出来的实力分看，Liquid 领先 HellRaisers 约 107 分；Liquid 选手们对线期 KDA 压制更明显；Liquid 最近手感比对手好（Liquid 8-2，HellRaisers 6-4，比赛结果都好于赛前预期）。 不过要注意：HellRaisers 这批首发最近赢得更多。 位置对比：中单 issaa 近期表现优于 taco；打野 naf 近期表现优于 deadfox；下路 twistzz 近期表现优于 bondik。 地图BP推演：Liquid禁Overpass，HellRaisers禁Inferno；Liquid选Mirage（Liquid胜率70%），HellRaisers选Nuke（Liquid胜率65%）；决胜图 Dust2（Liquid胜率67%）。 总结：有一定爆冷可能。
- **Astralis vs FaZe**：我看好 Astralis（系列赛胜率 80%，最可能比分 Astralis 2:0）。 主要依据：从长期战绩算出来的实力分看，Astralis 领先 FaZe 约 136 分；Astralis 选手们对线期 KDA 压制更明显。 不过要注意：FaZe 这批首发最近赢得更多。 位置对比：中单 device 近期表现优于 karrigan；打野 xyp9x 近期表现优于 niko；下路 dupreeh 近期表现优于 olofmeister。 地图BP推演：Astralis禁Mirage，FaZe禁Nuke；Astralis选Train（Astralis胜率73%），FaZe选Cache（Astralis胜率69%）；决胜图 Overpass（Astralis胜率72%）。 总结：爆冷概率很低。

### IEM Katowice 2019

训练数据截止：2019-02-28（之后的比赛模型都没见过）  
夺冠概率：Astralis 47%，Liquid 26%，MIBR 6%，Natus Vincere 6%  
**预测冠军：Astralis**　｜　实际冠军：Astralis ✅  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs FaZe | Natus Vincere | 58% | Natus Vincere 2-0 | ✅ |
| R1M2 | Liquid vs ENCE | Liquid | 73% | ENCE 0-2 | ❌ |
| R1M3 | MIBR vs Renegades | MIBR | 50% | MIBR 2-0 | ✅ |
| R1M4 | Astralis vs NiP | Astralis | 83% | Astralis 2-0 | ✅ |
| R2M1 | Natus Vincere vs ENCE | Natus Vincere | 53% | ENCE 1-2 | ❌ |
| R2M2 | MIBR vs Astralis | Astralis | 78% | Astralis 0-2 | ✅ |
| R3M1 | ENCE vs Astralis | Astralis | 83% | Astralis 0-2 | ✅ |

**赛前观点（8 强）：**

- **Natus Vincere vs FaZe**：倾向 Natus Vincere（系列赛胜率 58%，最可能比分 Natus Vincere 2:0）。 主要依据：综合实力分 Natus Vincere 比 FaZe 高约 62 分；Natus Vincere 这批首发最近赢得更多；老牌队伍经验更足：Natus Vincere 打过 1224 局，FaZe 打过 721 局。 但是：FaZe 选手们对线期 KDA 压制更明显。 位置对比：打野 guardian 近期表现优于 zeus；辅助 s1mple 近期表现优于 rain；中单 niko 近期表现优于 electronic。 地图BP推演：Natus Vincere禁Dust2，FaZe禁Train；Natus Vincere选Overpass（Natus Vincere胜率59%），FaZe选Cache（Natus Vincere胜率54%）；决胜图 Nuke（Natus Vincere胜率55%）。 总结：基本五五开，谁赢都不奇怪。
- **Liquid vs ENCE**：我的判断：Liquid 晋级（系列赛胜率 73%，最可能比分 Liquid 2:0）。 理由：从长期战绩算出来的实力分看，Liquid 领先 ENCE 约 77 分；Liquid 选手们对线期 KDA 压制更明显；老牌队伍经验更足：Liquid 打过 1044 局，ENCE 打过 451 局。 但是：ENCE 这批首发最近赢得更多。 位置对比：打野 naf 近期表现优于 aleksib；中单 allu 近期表现优于 stewie2k；下路 twistzz 近期表现优于 sergej。 地图BP推演：Liquid禁Train，ENCE禁Inferno；Liquid选Cache（Liquid胜率67%），ENCE选Nuke（Liquid胜率64%）；决胜图 Mirage（Liquid胜率66%）。 总结：有一定爆冷可能。
- **MIBR vs Renegades**：我看好 MIBR（系列赛胜率 50%，最可能比分 MIBR 2:0）。 主要依据：MIBR 整体硬实力更强（实力分高 29）；MIBR 这批首发最近赢得更多。 不过要注意：老牌队伍经验更足：MIBR 打过 134 局，Renegades 打过 710 局。 位置对比：中单 coldzera 近期表现优于 liazz；辅助 jks 近期表现优于 fer；下路 jkaem 近期表现优于 felps。 地图BP推演：MIBR禁Cache，Renegades禁Overpass；MIBR选Inferno（MIBR胜率52%），Renegades选Nuke（MIBR胜率48%）；决胜图 Train（MIBR胜率51%）。 总结：基本五五开，谁赢都不奇怪。
- **Astralis vs NiP**：倾向 Astralis（系列赛胜率 83%，最可能比分 Astralis 2:0）。 为什么：从长期战绩算出来的实力分看，Astralis 领先 NiP 约 217 分；Astralis 选手们对线期 KDA 压制更明显。 不过要注意：NiP 这批首发最近赢得更多。 位置对比：上单 magisk 近期表现优于 get_right；下路 dupreeh 近期表现优于 dennis；打野 xyp9x 近期表现优于 lekr0。 地图BP推演：Astralis禁Train，NiP禁Inferno；Astralis选Nuke（Astralis胜率77%），NiP选Cache（Astralis胜率72%）；决胜图 Mirage（Astralis胜率74%）。 总结：爆冷概率很低。

### StarLadder Major Berlin 2019

训练数据截止：2019-09-05（之后的比赛模型都没见过）  
夺冠概率：Liquid 43%，ENCE 15%，NRG 12%，Vitality 11%  
**预测冠军：Liquid**　｜　实际冠军：Astralis ❌  
预测 4 强命中 1/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | ENCE vs Renegades | ENCE | 75% | Renegades 0-2 | ❌ |
| R1M2 | Vitality vs AVANGAR | Vitality | 74% | AVANGAR 1-2 | ❌ |
| R1M3 | NRG vs Natus Vincere | NRG | 59% | NRG 2-0 | ✅ |
| R1M4 | Astralis vs Liquid | Liquid | 70% | Astralis 2-0 | ❌ |
| R2M1 | Renegades vs AVANGAR | Renegades | 55% | AVANGAR 0-2 | ❌ |
| R2M2 | NRG vs Astralis | Astralis | 53% | Astralis 0-2 | ✅ |
| R3M1 | AVANGAR vs Astralis | Astralis | 83% | Astralis 0-2 | ✅ |

**赛前观点（8 强）：**

- **ENCE vs Renegades**：我的判断：ENCE 晋级（系列赛胜率 75%，最可能比分 ENCE 2:0）。 主要依据：ENCE 整体硬实力更强（实力分高 143）；ENCE 选手们对线期 KDA 压制更明显。 不过要注意：Renegades 这批首发最近赢得更多。 位置对比：上单 aerial 近期表现优于 azr；中单 allu 近期表现优于 liazz；打野 aleksib 近期表现优于 gratisfaction。 地图BP推演：ENCE禁Inferno，Renegades禁Train；ENCE选Overpass（ENCE胜率69%），Renegades选Vertigo（ENCE胜率66%）；决胜图 Dust2（ENCE胜率67%）。 总结：有一定爆冷可能。
- **Vitality vs AVANGAR**：倾向 Vitality（系列赛胜率 74%，最可能比分 Vitality 2:0）。 为什么：从长期战绩算出来的实力分看，Vitality 领先 AVANGAR 约 154 分；Vitality 这批首发最近赢得更多。 但是：老牌队伍经验更足：Vitality 打过 267 局，AVANGAR 打过 603 局。 位置对比：上单 alex 近期表现优于 adren；打野 jame 近期表现优于 nbk-；下路 zywoo 近期表现优于 buster。 地图BP推演：Vitality禁Train，AVANGAR禁Overpass；Vitality选Nuke（Vitality胜率67%），AVANGAR选Inferno（Vitality胜率66%）；决胜图 Mirage（Vitality胜率66%）。 总结：有一定爆冷可能。
- **NRG vs Natus Vincere**：我看好 NRG（系列赛胜率 59%，最可能比分 NRG 2:0）。 为什么：NRG 选手们对线期 KDA 压制更明显；从长期战绩算出来的实力分看，NRG 领先 Natus Vincere 约 34 分；NRG 最近手感比对手好（NRG 9-1，Natus Vincere 5-5，比赛结果都好于赛前预期）。 但是：Natus Vincere 这批首发最近赢得更多。 位置对比：打野 cerq 近期表现优于 zeus；上单 brehze 近期表现优于 boombl4；辅助 s1mple 近期表现优于 tarik。 地图BP推演：NRG禁Mirage，Natus Vincere禁Dust2；NRG选Nuke（NRG胜率57%），Natus Vincere选Vertigo（NRG胜率56%）；决胜图 Inferno（NRG胜率56%）。 总结：基本五五开，谁赢都不奇怪。
- **Astralis vs Liquid**：我看好 Liquid（系列赛胜率 70%，最可能比分 Liquid 2:0）。 理由：Liquid 整体硬实力更强（实力分高 93）；Liquid 选手们对线期 KDA 压制更明显；近期状态：Astralis 最近 5胜5负（状态一般），Liquid 最近 8胜2负（状态火热）。 风险点：Astralis 这批首发最近赢得更多。 位置对比：下路 twistzz 近期表现优于 dupreeh；上单 elige 近期表现优于 magisk；辅助 nitr0 近期表现优于 gla1ve。 地图BP推演：Astralis禁Overpass，Liquid禁Nuke；Astralis选Inferno（Astralis胜率37%），Liquid选Mirage（Astralis胜率35%）；决胜图 Vertigo（Astralis胜率36%）。 总结：有一定爆冷可能。

### PGL Major Stockholm 2021

训练数据截止：2021-10-26（之后的比赛模型都没见过）  
夺冠概率：Gambit 26%，Natus Vincere 21%，Heroic 15%，NiP 13%  
**预测冠军：Natus Vincere**　｜　实际冠军：Natus Vincere ✅  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs Vitality | Natus Vincere | 58% | Natus Vincere 2-0 | ✅ |
| R1M2 | FURIA vs Gambit | Gambit | 77% | Gambit 0-2 | ✅ |
| R1M3 | Heroic vs Virtus.pro | Heroic | 60% | Heroic 2-1 | ✅ |
| R1M4 | NiP vs G2 | NiP | 60% | G2 0-2 | ❌ |
| R2M1 | Natus Vincere vs Gambit | Natus Vincere | 50% | Natus Vincere 2-0 | ✅ |
| R2M2 | Heroic vs G2 | Heroic | 61% | G2 1-2 | ❌ |
| R3M1 | Natus Vincere vs G2 | Natus Vincere | 70% | Natus Vincere 2-0 | ✅ |

**赛前观点（8 强）：**

- **Natus Vincere vs Vitality**：我的判断：Natus Vincere 晋级（系列赛胜率 58%，最可能比分 Natus Vincere 2:0）。 理由：从长期战绩算出来的实力分看，Natus Vincere 领先 Vitality 约 55 分；Natus Vincere 的职业比赛经验更多（Natus Vincere 1724 局 / Vitality 653 局）。 风险点：近期状态：Natus Vincere 最近 8胜2负（状态火热），Vitality 最近 7胜3负（状态不错）。 位置对比：打野 zywoo 近期表现优于 perfecto；辅助 s1mple 近期表现优于 shox；中单 b1t 近期表现优于 apex。 地图BP推演：Natus Vincere禁Overpass，Vitality禁Nuke；Natus Vincere选Mirage（Natus Vincere胜率58%），Vitality选Vertigo（Natus Vincere胜率53%）；决胜图 Ancient（Natus Vincere胜率56%）。 总结：基本五五开，谁赢都不奇怪。
- **FURIA vs Gambit**：倾向 Gambit（系列赛胜率 77%，最可能比分 Gambit 2:0）。 为什么：综合实力分 Gambit 比 FURIA 高约 145 分；Gambit 选手们对线期 KDA 压制更明显；Gambit 这批首发最近赢得更多。 风险点：FURIA 最近手感比对手好（FURIA 8-2，Gambit 8-2，比赛结果都好于赛前预期）。 位置对比：下路 nafany 近期表现优于 guerri；辅助 sh1ro 近期表现优于 yuurih；中单 art 近期表现优于 interz。 地图BP推演：FURIA禁Overpass，Gambit禁Inferno；FURIA选Ancient（FURIA胜率33%），Gambit选Vertigo（FURIA胜率29%）；决胜图 Mirage（FURIA胜率32%）。 总结：有一定爆冷可能。
- **Heroic vs Virtus.pro**：我的判断：Heroic 晋级（系列赛胜率 60%，最可能比分 Heroic 2:0）。 理由：从长期战绩算出来的实力分看，Heroic 领先 Virtus.pro 约 77 分；近期状态：Heroic 最近 6胜4负（状态不错），Virtus.pro 最近 4胜6负（状态一般）。 不过要注意：Virtus.pro 选手们对线期 KDA 压制更明显。 位置对比：上单 jame 近期表现优于 teses；中单 refrezh 近期表现优于 sanji；下路 yekindar 近期表现优于 sjuush。 地图BP推演：Heroic禁Inferno，Virtus.pro禁Overpass；Heroic选Vertigo（Heroic胜率58%），Virtus.pro选Dust2（Heroic胜率56%）；决胜图 Mirage（Heroic胜率57%）。 总结：基本五五开，谁赢都不奇怪。
- **NiP vs G2**：我看好 NiP（系列赛胜率 60%，最可能比分 NiP 2:0）。 理由：NiP 整体硬实力更强（实力分高 96）。 不过要注意：G2 这批首发最近赢得更多。 位置对比：下路 device 近期表现优于 hunter-；上单 amanek 近期表现优于 lnz。 地图BP推演：NiP禁Nuke，G2禁Overpass；NiP选Ancient（NiP胜率58%），G2选Mirage（NiP胜率56%）；决胜图 Dust2（NiP胜率56%）。 总结：基本五五开，谁赢都不奇怪。

### PGL Major Antwerp 2022

训练数据截止：2022-05-19（之后的比赛模型都没见过）  
夺冠概率：Natus Vincere 33%，FaZe 23%，ENCE 13%，Heroic 9%  
**预测冠军：Natus Vincere**　｜　实际冠军：FaZe ❌  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs FURIA | FURIA | 59% | Spirit 2-0 | ❌ |
| R1M2 | FaZe vs NiP | FaZe | 64% | FaZe 2-1 | ✅ |
| R1M3 | ENCE vs Copenhagen Flames | ENCE | 67% | ENCE 2-0 | ✅ |
| R1M4 | Heroic vs Natus Vincere | Natus Vincere | 68% | Natus Vincere 1-2 | ✅ |
| R2M1 | Spirit vs FaZe | FaZe | 74% | FaZe 0-2 | ✅ |
| R2M2 | ENCE vs Natus Vincere | Natus Vincere | 68% | Natus Vincere 0-2 | ✅ |
| R3M1 | FaZe vs Natus Vincere | Natus Vincere | 58% | FaZe 2-0 | ❌ |

**赛前观点（8 强）：**

- **Spirit vs FURIA**：倾向 FURIA（系列赛胜率 59%，最可能比分 FURIA 2:0）。 主要依据：FURIA 选手们对线期 KDA 压制更明显；综合实力分 FURIA 比 Spirit 高约 46 分。 风险点：Spirit 这批首发最近赢得更多。 位置对比：上单 kscerato 近期表现优于 patsi；辅助 yuurih 近期表现优于 s1ren；下路 saffee 近期表现优于 magixx。 地图BP推演：Spirit禁Vertigo，FURIA禁Dust2；Spirit选Nuke（Spirit胜率46%），FURIA选Inferno（Spirit胜率42%）；决胜图 Ancient（Spirit胜率44%）。 总结：基本五五开，谁赢都不奇怪。
- **FaZe vs NiP**：倾向 FaZe（系列赛胜率 64%，最可能比分 FaZe 2:0）。 主要依据：综合实力分 FaZe 比 NiP 高约 79 分；FaZe 选手们对线期 KDA 压制更明显。 但是：NiP 这批首发最近赢得更多。 位置对比：辅助 ropz 近期表现优于 hampus；打野 broky 近期表现优于 plopski；中单 rez 近期表现优于 karrigan。 地图BP推演：FaZe禁Overpass，NiP禁Dust2；FaZe选Mirage（FaZe胜率61%），NiP选Ancient（FaZe胜率58%）；决胜图 Vertigo（FaZe胜率60%）。 总结：有一定爆冷可能。
- **ENCE vs Copenhagen Flames**：倾向 ENCE（系列赛胜率 67%，最可能比分 ENCE 2:0）。 为什么：ENCE 整体硬实力更强（实力分高 89）；ENCE 选手们对线期 KDA 压制更明显；近期状态：ENCE 最近 7胜3负（状态不错），Copenhagen Flames 最近 6胜4负（状态不错）。 风险点：Copenhagen Flames 这批首发最近赢得更多。 位置对比：上单 maden 近期表现优于 hooxi；中单 spinx 近期表现优于 jabbi；打野 zyphon 近期表现优于 snappi。 地图BP推演：ENCE禁Vertigo，Copenhagen Flames禁Dust2；ENCE选Mirage（ENCE胜率65%），Copenhagen Flames选Overpass（ENCE胜率59%）；决胜图 Ancient（ENCE胜率62%）。 总结：有一定爆冷可能。
- **Heroic vs Natus Vincere**：倾向 Natus Vincere（系列赛胜率 68%，最可能比分 Natus Vincere 2:0）。 为什么：从长期战绩算出来的实力分看，Natus Vincere 领先 Heroic 约 112 分；Natus Vincere 选手们对线期 KDA 压制更明显。 不过要注意：Heroic 这批首发最近赢得更多。 位置对比：辅助 s1mple 近期表现优于 stavn；中单 b1t 近期表现优于 refrezh；上单 teses 近期表现优于 boombl4。 地图BP推演：Heroic禁Ancient，Natus Vincere禁Overpass；Heroic选Vertigo（Heroic胜率40%），Natus Vincere选Mirage（Heroic胜率36%）；决胜图 Nuke（Heroic胜率36%）。 总结：有一定爆冷可能。

### IEM Rio Major 2022

训练数据截止：2022-11-10（之后的比赛模型都没见过）  
夺冠概率：Natus Vincere 24%，Cloud9 18%，Virtus.pro 17%，Heroic 17%  
**预测冠军：Natus Vincere**　｜　实际冠军：Virtus.pro ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Cloud9 vs mousesports | Cloud9 | 63% | mousesports 1-2 | ❌ |
| R1M2 | fnatic vs Virtus.pro | Virtus.pro | 67% | Virtus.pro 0-2 | ✅ |
| R1M3 | Heroic vs Spirit | Heroic | 62% | Heroic 2-0 | ✅ |
| R1M4 | Natus Vincere vs FURIA | Natus Vincere | 65% | FURIA 1-2 | ❌ |
| R2M1 | mousesports vs Virtus.pro | Virtus.pro | 60% | Virtus.pro 1-2 | ✅ |
| R2M2 | Heroic vs FURIA | Heroic | 58% | Heroic 2-1 | ✅ |
| R3M1 | Virtus.pro vs Heroic | Heroic | 52% | Virtus.pro 2-0 | ❌ |

**赛前观点（8 强）：**

- **Cloud9 vs mousesports**：我看好 Cloud9（系列赛胜率 63%，最可能比分 Cloud9 2:0）。 理由：从长期战绩算出来的实力分看，Cloud9 领先 mousesports 约 71 分；Cloud9 最近手感比对手好（Cloud9 10-0，mousesports 5-5，比赛结果都好于赛前预期）；Cloud9 选手们对线期 KDA 压制更明显。 但是：mousesports 这批首发最近赢得更多。 位置对比：中单 frozen 近期表现优于 interz；辅助 sh1ro 近期表现优于 xertion；打野 hobbit 近期表现优于 dexter。 地图BP推演：Cloud9禁Nuke，mousesports禁Overpass；Cloud9选Dust2（Cloud9胜率60%），mousesports选Inferno（Cloud9胜率57%）；决胜图 Vertigo（Cloud9胜率59%）。 总结：有一定爆冷可能。
- **fnatic vs Virtus.pro**：我看好 Virtus.pro（系列赛胜率 67%，最可能比分 Virtus.pro 2:0）。 理由：Virtus.pro 整体硬实力更强（实力分高 74）；Virtus.pro 选手们对线期 KDA 压制更明显；近期状态：fnatic 最近 6胜4负（状态不错），Virtus.pro 最近 8胜2负（状态火热）。 不过要注意：fnatic 这批首发最近赢得更多。 位置对比：打野 jame 近期表现优于 krimz；中单 mezii 近期表现优于 qikert；上单 fl1t 近期表现优于 fashr。 地图BP推演：fnatic禁Dust2，Virtus.pro禁Inferno；fnatic选Overpass（fnatic胜率39%），Virtus.pro选Vertigo（fnatic胜率37%）；决胜图 Mirage（fnatic胜率38%）。 总结：有一定爆冷可能。
- **Heroic vs Spirit**：倾向 Heroic（系列赛胜率 62%，最可能比分 Heroic 2:0）。 主要依据：Heroic 整体硬实力更强（实力分高 108）。 但是：Spirit 这批首发最近赢得更多。 位置对比：辅助 w0nderful 近期表现优于 stavn；下路 sjuush 近期表现优于 s1ren；中单 jabbi 近期表现优于 magixx。 地图BP推演：Heroic禁Dust2，Spirit禁Inferno；Heroic选Mirage（Heroic胜率60%），Spirit选Ancient（Heroic胜率56%）；决胜图 Nuke（Heroic胜率58%）。 总结：有一定爆冷可能。
- **Natus Vincere vs FURIA**：我的判断：Natus Vincere 晋级（系列赛胜率 65%，最可能比分 Natus Vincere 2:0）。 为什么：综合实力分 Natus Vincere 比 FURIA 高约 112 分；Natus Vincere 这批首发最近赢得更多；Natus Vincere 的职业比赛经验更多（Natus Vincere 1875 局 / FURIA 941 局）。 风险点：近期状态：Natus Vincere 最近 8胜2负（状态火热），FURIA 最近 9胜1负（状态火热）。 位置对比：辅助 yuurih 近期表现优于 sdy；上单 kscerato 近期表现优于 perfecto；下路 s1mple 近期表现优于 saffee。 地图BP推演：Natus Vincere禁Vertigo，FURIA禁Nuke；Natus Vincere选Dust2（Natus Vincere胜率62%），FURIA选Mirage（Natus Vincere胜率59%）；决胜图 Ancient（Natus Vincere胜率59%）。 总结：有一定爆冷可能。

### BLAST.tv Paris Major 2023

训练数据截止：2023-05-18（之后的比赛模型都没见过）  
夺冠概率：FaZe 32%，Liquid 24%，Vitality 21%，Heroic 18%  
**预测冠军：FaZe**　｜　实际冠军：Vitality ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Heroic vs FaZe | FaZe | 59% | Heroic 2-1 | ❌ |
| R1M2 | GamerLegion vs Monte | GamerLegion | 71% | GamerLegion 2-0 | ✅ |
| R1M3 | Liquid vs Apeks | Liquid | 77% | Apeks 0-2 | ❌ |
| R1M4 | Into The Breach vs Vitality | Vitality | 92% | Vitality 0-2 | ✅ |
| R2M1 | Heroic vs GamerLegion | Heroic | 80% | GamerLegion 1-2 | ❌ |
| R2M2 | Apeks vs Vitality | Vitality | 72% | Vitality 0-2 | ✅ |
| R3M1 | GamerLegion vs Vitality | Vitality | 76% | Vitality 0-2 | ✅ |

**赛前观点（8 强）：**

- **Heroic vs FaZe**：倾向 FaZe（系列赛胜率 59%，最可能比分 FaZe 2:0）。 理由：FaZe 选手们对线期 KDA 压制更明显；从长期战绩算出来的实力分看，FaZe 领先 Heroic 约 19 分。 风险点：Heroic 这批首发最近赢得更多。 位置对比：辅助 ropz 近期表现优于 sjuush；打野 broky 近期表现优于 cadian；上单 twistzz 近期表现优于 teses。 总结：基本五五开，谁赢都不奇怪。
- **GamerLegion vs Monte**：我的判断：GamerLegion 晋级（系列赛胜率 71%，最可能比分 GamerLegion 2:0）。 为什么：GamerLegion 的职业比赛经验更多（GamerLegion 353 局 / Monte 3 局）；综合实力分 GamerLegion 比 Monte 高约 31 分；GamerLegion 选手们对线期 KDA 压制更明显。 但是：Monte 这批首发最近赢得更多。 位置对比：辅助 siuhy 近期表现优于 joel；打野 acor 近期表现优于 fessor；下路 woro2k 近期表现优于 isak。 总结：有一定爆冷可能。
- **Liquid vs Apeks**：倾向 Liquid（系列赛胜率 77%，最可能比分 Liquid 2:0）。 为什么：Liquid 整体硬实力更强（实力分高 199）；老牌队伍经验更足：Liquid 打过 1713 局，Apeks 打过 78 局。 不过要注意：Apeks 这批首发最近赢得更多。 位置对比：辅助 nawwk 近期表现优于 osee；下路 jkaem 近期表现优于 nitr0；打野 naf 近期表现优于 styko。 总结：有一定爆冷可能。
- **Into The Breach vs Vitality**：倾向 Vitality（系列赛胜率 92%，最可能比分 Vitality 2:0）。 理由：Vitality 整体硬实力更强（实力分高 240）；老牌队伍经验更足：Into The Breach 打过 9 局，Vitality 打过 853 局；Vitality 选手们对线期 KDA 压制更明显。 不过要注意：Into The Breach 这批首发最近赢得更多。 位置对比：中单 zywoo 近期表现优于 thomas；辅助 dupreeh 近期表现优于 dobbo；下路 wolfy 近期表现优于 apex。 总结：爆冷概率很低。

### PGL Major Copenhagen 2024

训练数据截止：2024-03-17（之后的比赛模型都没见过）  
夺冠概率：Spirit 30%，G2 16%，Vitality 14%，FaZe 11%  
**预测冠军：Spirit**　｜　实际冠军：Natus Vincere ❌  
预测 4 强命中 3/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs FaZe | Spirit | 63% | FaZe 1-2 | ❌ |
| R1M2 | Vitality vs Cloud9 | Vitality | 61% | Vitality 2-0 | ✅ |
| R1M3 | Eternal Fire vs Natus Vincere | Natus Vincere | 60% | Natus Vincere 0-2 | ✅ |
| R1M4 | G2 vs mousesports | G2 | 55% | G2 2-0 | ✅ |
| R2M1 | FaZe vs Vitality | FaZe | 51% | FaZe 2-1 | ✅ |
| R2M2 | Natus Vincere vs G2 | G2 | 59% | Natus Vincere 2-1 | ❌ |
| R3M1 | FaZe vs Natus Vincere | FaZe | 60% | Natus Vincere 1-2 | ❌ |

**赛前观点（8 强）：**

- **Spirit vs FaZe**：我看好 Spirit（系列赛胜率 63%，最可能比分 Spirit 2:0）。 主要依据：Spirit 选手们对线期 KDA 压制更明显；Spirit 整体硬实力更强（实力分高 57）；近期状态：Spirit 最近 8胜2负（状态火热），FaZe 最近 5胜5负（状态一般）。 风险点：FaZe 这批首发最近赢得更多。 位置对比：上单 donk 近期表现优于 broky；中单 magixx 近期表现优于 karrigan；下路 sh1ro 近期表现优于 rain。 地图BP推演：Spirit禁Inferno，FaZe禁Overpass；Spirit选Mirage（Spirit胜率60%），FaZe选Nuke（Spirit胜率58%）；决胜图 Vertigo（Spirit胜率59%）。 总结：有一定爆冷可能。
- **Vitality vs Cloud9**：我的判断：Vitality 晋级（系列赛胜率 61%，最可能比分 Vitality 2:0）。 主要依据：从长期战绩算出来的实力分看，Vitality 领先 Cloud9 约 58 分；Vitality 选手们对线期 KDA 压制更明显；近期状态：Vitality 最近 6胜4负（状态不错），Cloud9 最近 6胜4负（状态不错）。 但是：Cloud9 这批首发最近赢得更多。 位置对比：打野 zywoo 近期表现优于 boombl4；中单 hobbit 近期表现优于 apex；辅助 electronic 近期表现优于 mezii。 地图BP推演：Vitality禁Overpass，Cloud9禁Inferno；Vitality选Nuke（Vitality胜率59%），Cloud9选Mirage（Vitality胜率56%）；决胜图 Anubis（Vitality胜率57%）。 总结：基本五五开，谁赢都不奇怪。
- **Eternal Fire vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 60%，最可能比分 Natus Vincere 2:0）。 为什么：从长期战绩算出来的实力分看，Natus Vincere 领先 Eternal Fire 约 38 分；Natus Vincere 的职业比赛经验更多（Eternal Fire 170 局 / Natus Vincere 1948 局）；Natus Vincere 选手们对线期 KDA 压制更明显。 不过要注意：近期状态：Eternal Fire 最近 5胜5负（状态一般），Natus Vincere 最近 5胜5负（状态一般）。 位置对比：上单 calyx 近期表现优于 aleksib；打野 b1t 近期表现优于 maj3r；辅助 w0nderful 近期表现优于 woxic。 地图BP推演：Eternal Fire禁Nuke，Natus Vincere禁Inferno；Eternal Fire选Vertigo（Eternal Fire胜率45%），Natus Vincere选Anubis（Eternal Fire胜率42%）；决胜图 Overpass（Eternal Fire胜率44%）。 总结：基本五五开，谁赢都不奇怪。
- **G2 vs mousesports**：我的判断：G2 晋级（系列赛胜率 55%，最可能比分 G2 2:0）。 主要依据：综合实力分 G2 比 mousesports 高约 50 分；G2 选手们对线期 KDA 压制更明显。 风险点：mousesports 最近手感比对手好（G2 7-3，mousesports 8-2，比赛结果都好于赛前预期）。 位置对比：下路 m0nesy 近期表现优于 torzsi；上单 brollan 近期表现优于 hooxi；打野 niko 近期表现优于 jimpphat。 地图BP推演：G2禁Mirage，mousesports禁Inferno；G2选Nuke（G2胜率55%），mousesports选Vertigo（G2胜率52%）；决胜图 Ancient（G2胜率53%）。 总结：基本五五开，谁赢都不奇怪。

### Perfect World Shanghai Major 2024

训练数据截止：2024-12-12（之后的比赛模型都没见过）  
夺冠概率：Vitality 25%，G2 20%，Spirit 14%，mousesports 11%  
**预测冠军：Vitality**　｜　实际冠军：Spirit ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | The Mongolz vs mousesports | mousesports | 51% | mousesports 0-2 | ✅ |
| R1M2 | Liquid vs Spirit | Spirit | 54% | Spirit 0-2 | ✅ |
| R1M3 | G2 vs Heroic | G2 | 65% | G2 2-1 | ✅ |
| R1M4 | FaZe vs Vitality | Vitality | 70% | FaZe 2-1 | ❌ |
| R2M1 | mousesports vs Spirit | Spirit | 54% | Spirit 1-2 | ✅ |
| R2M2 | G2 vs FaZe | G2 | 66% | FaZe 0-2 | ❌ |
| R3M1 | Spirit vs FaZe | Spirit | 62% | Spirit 2-1 | ✅ |

**赛前观点（8 强）：**

- **The Mongolz vs mousesports**：倾向 mousesports（系列赛胜率 51%，最可能比分 mousesports 2:0）。 为什么：mousesports 这批首发最近赢得更多；mousesports 的职业比赛经验更多（The Mongolz 437 局 / mousesports 2171 局）。 但是：The Mongolz 选手们对线期 KDA 压制更明显。 位置对比：中单 blitz 近期表现优于 siuhy；辅助 senzu 近期表现优于 xertion；上单 910 近期表现优于 brollan。 地图BP推演：The Mongolz禁Mirage，mousesports禁Dust2；The Mongolz选Anubis（The Mongolz胜率51%），mousesports选Nuke（The Mongolz胜率47%）；决胜图 Vertigo（The Mongolz胜率50%）。 总结：基本五五开，谁赢都不奇怪。
- **Liquid vs Spirit**：我的判断：Spirit 晋级（系列赛胜率 54%，最可能比分 Spirit 2:0）。 为什么：Spirit 整体硬实力更强（实力分高 37）；Spirit 这批首发最近赢得更多。 不过要注意：Liquid 选手们对线期 KDA 压制更明显。 位置对比：上单 donk 近期表现优于 naf；打野 twistzz 近期表现优于 chopper；辅助 ultimate 近期表现优于 zont1x。 地图BP推演：Liquid禁Nuke，Spirit禁Inferno；Liquid选Anubis（Liquid胜率50%），Spirit选Dust2（Liquid胜率45%）；决胜图 Mirage（Liquid胜率48%）。 总结：基本五五开，谁赢都不奇怪。
- **G2 vs Heroic**：我的判断：G2 晋级（系列赛胜率 65%，最可能比分 G2 2:0）。 理由：从长期战绩算出来的实力分看，G2 领先 Heroic 约 109 分。 风险点：Heroic 这批首发最近赢得更多。 位置对比：下路 m0nesy 近期表现优于 kyxsan；辅助 malbsmd 近期表现优于 sjuush；打野 teses 近期表现优于 snax。 地图BP推演：G2禁Mirage，Heroic禁Inferno；G2选Nuke（G2胜率62%），Heroic选Vertigo（G2胜率57%）；决胜图 Dust2（G2胜率61%）。 总结：有一定爆冷可能。
- **FaZe vs Vitality**：倾向 Vitality（系列赛胜率 70%，最可能比分 Vitality 2:0）。 主要依据：Vitality 整体硬实力更强（实力分高 107）；Vitality 选手们对线期 KDA 压制更明显；近期状态：FaZe 最近 5胜5负（状态一般），Vitality 最近 9胜1负（状态火热）。 但是：FaZe 这批首发最近赢得更多。 位置对比：打野 zywoo 近期表现优于 frozen；上单 spinx 近期表现优于 broky；辅助 ropz 近期表现优于 mezii。 地图BP推演：FaZe禁Nuke，Vitality禁Inferno；FaZe选Mirage（FaZe胜率38%），Vitality选Dust2（FaZe胜率34%）；决胜图 Anubis（FaZe胜率37%）。 总结：有一定爆冷可能。

### BLAST.tv Austin Major 2025

训练数据截止：2025-06-19（之后的比赛模型都没见过）  
夺冠概率：Vitality 45%，Spirit 23%，FURIA 7%，FaZe 7%  
**预测冠军：Vitality**　｜　实际冠军：Vitality ✅  
预测 4 强命中 1/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs mousesports | Spirit | 65% | mousesports 1-2 | ❌ |
| R1M2 | Vitality vs Natus Vincere | Vitality | 82% | Vitality 2-0 | ✅ |
| R1M3 | FaZe vs The Mongolz | FaZe | 51% | The Mongolz 0-2 | ❌ |
| R1M4 | paiN Gaming vs FURIA | FURIA | 69% | paiN Gaming 2-1 | ❌ |
| R2M1 | mousesports vs Vitality | Vitality | 75% | Vitality 1-2 | ✅ |
| R2M2 | The Mongolz vs paiN Gaming | The Mongolz | 72% | The Mongolz 2-0 | ✅ |
| R3M1 | Vitality vs The Mongolz | Vitality | 83% | Vitality 2-1 | ✅ |

**赛前观点（8 强）：**

- **Spirit vs mousesports**：倾向 Spirit（系列赛胜率 65%，最可能比分 Spirit 2:0）。 主要依据：Spirit 整体硬实力更强（实力分高 81）；Spirit 选手们对线期 KDA 压制更明显；近期状态：Spirit 最近 9胜1负（状态火热），mousesports 最近 6胜4负（状态不错）。 风险点：mousesports 这批首发最近赢得更多。 位置对比：上单 donk 近期表现优于 brollan；中单 spinx 近期表现优于 magixx；打野 jimpphat 近期表现优于 chopper。 地图BP推演：Spirit禁Mirage，mousesports禁Dust2；Spirit选Anubis（Spirit胜率61%），mousesports选Inferno（Spirit胜率59%）；决胜图 Train（Spirit胜率60%）。 总结：有一定爆冷可能。
- **Vitality vs Natus Vincere**：我的判断：Vitality 晋级（系列赛胜率 82%，最可能比分 Vitality 2:0）。 主要依据：从长期战绩算出来的实力分看，Vitality 领先 Natus Vincere 约 214 分；Vitality 选手们对线期 KDA 压制更明显。 风险点：Natus Vincere 这批首发最近赢得更多。 位置对比：上单 zywoo 近期表现优于 aleksib。 地图BP推演：Vitality禁Mirage，Natus Vincere禁Nuke；Vitality选Inferno（Vitality胜率75%），Natus Vincere选Train（Vitality胜率71%）；决胜图 Ancient（Vitality胜率73%）。 总结：爆冷概率很低。
- **FaZe vs The Mongolz**：倾向 FaZe（系列赛胜率 51%，最可能比分 FaZe 2:0）。 主要依据：老牌队伍经验更足：FaZe 打过 1694 局，The Mongolz 打过 533 局；FaZe 最近手感比对手好（FaZe 6-4，The Mongolz 5-5，比赛结果都好于赛前预期）；FaZe 这批首发最近赢得更多。 但是：从长期战绩算出来的实力分看，The Mongolz 领先 FaZe 约 30 分。 位置对比：打野 frozen 近期表现优于 techno；中单 blitz 近期表现优于 karrigan；上单 910 近期表现优于 elige。 地图BP推演：FaZe禁Dust2，The Mongolz禁Anubis；FaZe选Ancient（FaZe胜率51%），The Mongolz选Mirage（FaZe胜率49%）；决胜图 Nuke（FaZe胜率51%）。 总结：基本五五开，谁赢都不奇怪。
- **paiN Gaming vs FURIA**：我看好 FURIA（系列赛胜率 69%，最可能比分 FURIA 2:0）。 为什么：从长期战绩算出来的实力分看，FURIA 领先 paiN Gaming 约 94 分；FURIA 选手们对线期 KDA 压制更明显；FURIA 的职业比赛经验更多（paiN Gaming 559 局 / FURIA 1236 局）。 但是：paiN Gaming 这批首发最近赢得更多。 位置对比：打野 kscerato 近期表现优于 biguzera；下路 molodoy 近期表现优于 dgt。 地图BP推演：paiN Gaming禁Train，FURIA禁Nuke；paiN Gaming选Mirage（paiN Gaming胜率38%），FURIA选Inferno（paiN Gaming胜率34%）；决胜图 Dust2（paiN Gaming胜率38%）。 总结：有一定爆冷可能。

### StarLadder Budapest Major 2025

训练数据截止：2025-12-11（之后的比赛模型都没见过）  
夺冠概率：FURIA 37%，mousesports 20%，Vitality 15%，Spirit 12%  
**预测冠军：FURIA**　｜　实际冠军：Vitality ❌  
预测 4 强命中 2/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs Team Falcons | Spirit | 53% | Spirit 2-0 | ✅ |
| R1M2 | The Mongolz vs Vitality | Vitality | 68% | Vitality 0-2 | ✅ |
| R1M3 | mousesports vs FaZe | mousesports | 74% | FaZe 0-2 | ❌ |
| R1M4 | Natus Vincere vs FURIA | FURIA | 75% | Natus Vincere 2-1 | ❌ |
| R2M1 | Spirit vs Vitality | Vitality | 51% | Vitality 0-2 | ✅ |
| R2M2 | FaZe vs Natus Vincere | Natus Vincere | 59% | FaZe 2-1 | ❌ |
| R3M1 | Vitality vs FaZe | Vitality | 75% | Vitality 3-1 | ✅ |

**赛前观点（8 强）：**

- **Spirit vs Team Falcons**：倾向 Spirit（系列赛胜率 53%，最可能比分 Spirit 2:0）。 为什么：老牌队伍经验更足：Spirit 打过 1674 局，Team Falcons 打过 369 局；Spirit 这批首发最近赢得更多；近期状态：Spirit 最近 7胜3负（状态不错），Team Falcons 最近 5胜5负（状态一般）。 但是：从长期战绩算出来的实力分看，Team Falcons 领先 Spirit 约 21 分。 位置对比：辅助 m0nesy 近期表现优于 zweih；中单 sh1ro 近期表现优于 teses；打野 niko 近期表现优于 chopper。 地图BP推演：Spirit禁Nuke，Team Falcons禁Dust2；Spirit选Overpass（Spirit胜率54%），Team Falcons选Inferno（Spirit胜率51%）；决胜图 Mirage（Spirit胜率52%）。 总结：基本五五开，谁赢都不奇怪。
- **The Mongolz vs Vitality**：我看好 Vitality（系列赛胜率 68%，最可能比分 Vitality 2:0）。 为什么：Vitality 整体硬实力更强（实力分高 130）；Vitality 的职业比赛经验更多（The Mongolz 635 局 / Vitality 1204 局）。 不过要注意：The Mongolz 选手们对线期 KDA 压制更明显。 位置对比：打野 techno 近期表现优于 apex。 地图BP推演：The Mongolz禁Dust2，Vitality禁Ancient；The Mongolz选Mirage（The Mongolz胜率40%），Vitality选Nuke（The Mongolz胜率35%）；决胜图 Train（The Mongolz胜率38%）。 总结：有一定爆冷可能。
- **mousesports vs FaZe**：我的判断：mousesports 晋级（系列赛胜率 74%，最可能比分 mousesports 2:0）。 为什么：从长期战绩算出来的实力分看，mousesports 领先 FaZe 约 138 分；mousesports 这批首发最近赢得更多。 但是：FaZe 最近手感比对手好（mousesports 6-4，FaZe 8-2，比赛结果都好于赛前预期）。 位置对比：辅助 xertion 近期表现优于 karrigan；上单 jcobbb 近期表现优于 brollan；下路 frozen 近期表现优于 torzsi。 地图BP推演：mousesports禁Ancient，FaZe禁Train；mousesports选Overpass（mousesports胜率69%），FaZe选Mirage（mousesports胜率64%）；决胜图 Nuke（mousesports胜率66%）。 总结：有一定爆冷可能。
- **Natus Vincere vs FURIA**：我的判断：FURIA 晋级（系列赛胜率 75%，最可能比分 FURIA 2:0）。 为什么：综合实力分 FURIA 比 Natus Vincere 高约 168 分；FURIA 选手们对线期 KDA 压制更明显；近期状态：Natus Vincere 最近 7胜3负（状态不错），FURIA 最近 9胜1负（状态火热）。 风险点：Natus Vincere 这批首发最近赢得更多。 位置对比：下路 molodoy 近期表现优于 makazze；中单 yekindar 近期表现优于 im；辅助 w0nderful 近期表现优于 yuurih。 地图BP推演：Natus Vincere禁Inferno，FURIA禁Train；Natus Vincere选Ancient（Natus Vincere胜率34%），FURIA选Nuke（Natus Vincere胜率30%）；决胜图 Mirage（Natus Vincere胜率33%）。 总结：有一定爆冷可能。

### IEM Cologne Major 2026

训练数据截止：2026-06-19（之后的比赛模型都没见过）  
夺冠概率：Spirit 33%，Vitality 32%，Aurora Gaming 11%，FURIA 11%  
**预测冠军：Spirit**　｜　实际冠军：Team Falcons ❌  
预测 4 强命中 3/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs G2 | Spirit | 74% | Spirit 2-1 | ✅ |
| R1M2 | Team Falcons vs Vitality | Vitality | 74% | Team Falcons 2-1 | ❌ |
| R1M3 | Aurora Gaming vs BetBoom Team | Aurora Gaming | 66% | Aurora Gaming 2-0 | ✅ |
| R1M4 | 9z Team vs FURIA | FURIA | 72% | FURIA 1-2 | ✅ |
| R2M1 | Spirit vs Team Falcons | Spirit | 74% | Team Falcons 1-2 | ❌ |
| R2M2 | Aurora Gaming vs FURIA | Aurora Gaming | 52% | FURIA 0-2 | ❌ |
| R3M1 | Team Falcons vs FURIA | FURIA | 55% | Team Falcons 3-0 | ❌ |

**赛前观点（8 强）：**

- **Spirit vs G2**：我的判断：Spirit 晋级（系列赛胜率 74%，最可能比分 Spirit 2:0）。 为什么：Spirit 整体硬实力更强（实力分高 123）；Spirit 选手们对线期 KDA 压制更明显。 不过要注意：G2 这批首发最近赢得更多。 位置对比：中单 sh1ro 近期表现优于 nertz；上单 donk 近期表现优于 heavygod；打野 magixx 近期表现优于 matys。 地图BP推演：Spirit禁Inferno，G2禁Dust2；Spirit选Anubis（Spirit胜率68%），G2选Mirage（Spirit胜率65%）；决胜图 Nuke（Spirit胜率66%）。 总结：有一定爆冷可能。
- **Team Falcons vs Vitality**：倾向 Vitality（系列赛胜率 74%，最可能比分 Vitality 2:0）。 为什么：综合实力分 Vitality 比 Team Falcons 高约 148 分；老牌队伍经验更足：Team Falcons 打过 465 局，Vitality 打过 1303 局；Vitality 选手们对线期 KDA 压制更明显。 但是：近期状态：Team Falcons 最近 6胜4负（状态不错），Vitality 最近 6胜4负（状态不错）。 位置对比：下路 mezii 近期表现优于 karrigan；上单 zywoo 近期表现优于 kyousuke；打野 niko 近期表现优于 apex。 地图BP推演：Team Falcons禁Inferno，Vitality禁Anubis；Team Falcons选Ancient（Team Falcons胜率35%），Vitality选Dust2（Team Falcons胜率30%）；决胜图 Nuke（Team Falcons胜率34%）。 总结：有一定爆冷可能。
- **Aurora Gaming vs BetBoom Team**：我的判断：Aurora Gaming 晋级（系列赛胜率 66%，最可能比分 Aurora Gaming 2:0）。 主要依据：Aurora Gaming 选手们对线期 KDA 压制更明显；Aurora Gaming 整体硬实力更强（实力分高 46）；Aurora Gaming 最近手感比对手好（Aurora Gaming 8-2，BetBoom Team 4-6，比赛结果都好于赛前预期）。 风险点：BetBoom Team 这批首发最近赢得更多。 位置对比：辅助 woxic 近期表现优于 zorte；下路 xantares 近期表现优于 d1ledez；中单 wicadia 近期表现优于 magnojez。 地图BP推演：Aurora Gaming禁Nuke，BetBoom Team禁Overpass；Aurora Gaming选Mirage（Aurora Gaming胜率63%），BetBoom Team选Ancient（Aurora Gaming胜率59%）；决胜图 Inferno（Aurora Gaming胜率62%）。 总结：有一定爆冷可能。
- **9z Team vs FURIA**：我的判断：FURIA 晋级（系列赛胜率 72%，最可能比分 FURIA 2:0）。 理由：FURIA 整体硬实力更强（实力分高 71）；FURIA 选手们对线期 KDA 压制更明显；FURIA 的职业比赛经验更多（9z Team 316 局 / FURIA 1451 局）。 但是：9z Team 这批首发最近赢得更多。 位置对比：下路 molodoy 近期表现优于 max；打野 kscerato 近期表现优于 dgt；上单 huasopeek 近期表现优于 fallen。 地图BP推演：9z Team禁Mirage，FURIA禁Ancient；9z Team选Overpass（9z Team胜率36%），FURIA选Nuke（9z Team胜率34%）；决胜图 Inferno（9z Team胜率35%）。 总结：有一定爆冷可能。
