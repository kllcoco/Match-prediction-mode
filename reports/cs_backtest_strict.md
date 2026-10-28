# CS Major 回测 · 严格模式（训练时不看任何世界赛/MSI/Major）

- 系列赛预测命中率：**62.1%**（161 场；瞎猜 50%）
- 4 强命中：62.0%　决赛队伍命中：45.7%　冠军命中：**26.1%**（瞎猜 12.5%）
- 对真实冠军给出的平均夺冠概率：20.3%　对数损失：0.655（越低越好，瞎猜 0.693）

### EMS One Katowice 2014

训练数据截止：2014-03-13（之后的比赛模型都没见过）  
夺冠概率：NiP 22%，Virtus.pro 16%，LGB 15%，Complexity 13%  
**预测冠军：NiP**　｜　实际冠军：Virtus.pro ❌  
预测 4 强命中 4/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | NiP vs Complexity | NiP | 58% | NiP 2-1 | ✅ |
| R1M2 | Dignitas vs HellRaisers | Dignitas | 51% | Dignitas 2-0 | ✅ |
| R1M3 | Virtus.pro vs LDLC | Virtus.pro | 60% | Virtus.pro 2-0 | ✅ |
| R1M4 | fnatic vs LGB | LGB | 55% | LGB 1-2 | ✅ |
| R2M1 | NiP vs Dignitas | NiP | 64% | NiP 2-0 | ✅ |
| R2M2 | Virtus.pro vs LGB | Virtus.pro | 51% | Virtus.pro 2-1 | ✅ |
| R3M1 | NiP vs Virtus.pro | NiP | 57% | Virtus.pro 0-2 | ❌ |

**赛前观点（8 强）：**

- **NiP vs Complexity**：倾向 NiP（系列赛胜率 58%，最可能比分 NiP 2:0）。 理由：综合实力分 NiP 比 Complexity 高约 35 分。 总结：基本五五开，谁赢都不奇怪。
- **Dignitas vs HellRaisers**：我的判断：Dignitas 晋级（系列赛胜率 51%，最可能比分 Dignitas 2:0）。 理由：Dignitas 整体硬实力更强（实力分高 5）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs LDLC**：我看好 Virtus.pro（系列赛胜率 60%，最可能比分 Virtus.pro 2:0）。 主要依据：从长期战绩算出来的实力分看，Virtus.pro 领先 LDLC 约 48 分。 总结：基本五五开，谁赢都不奇怪。
- **fnatic vs LGB**：我看好 LGB（系列赛胜率 55%，最可能比分 LGB 2:0）。 为什么：综合实力分 LGB 比 fnatic 高约 23 分。 总结：基本五五开，谁赢都不奇怪。

### ESL One Cologne 2014

训练数据截止：2014-08-14（之后的比赛模型都没见过）  
夺冠概率：fnatic 27%，Virtus.pro 19%，NiP 15%，Dignitas 14%  
**预测冠军：fnatic**　｜　实际冠军：NiP ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | fnatic vs Natus Vincere | fnatic | 62% | fnatic 2-1 | ✅ |
| R1M2 | Epsilon vs Dignitas | Dignitas | 65% | Dignitas 0-2 | ✅ |
| R1M3 | LDLC vs Virtus.pro | Virtus.pro | 58% | LDLC 2-0 | ❌ |
| R1M4 | Cloud9 vs NiP | NiP | 87% | NiP 1-2 | ✅ |
| R2M1 | fnatic vs Dignitas | fnatic | 63% | fnatic 2-0 | ✅ |
| R2M2 | LDLC vs NiP | LDLC | 53% | NiP 1-2 | ❌ |
| R3M1 | fnatic vs NiP | fnatic | 68% | NiP 1-2 | ❌ |

**赛前观点（8 强）：**

- **fnatic vs Natus Vincere**：我看好 fnatic（系列赛胜率 62%，最可能比分 fnatic 2:0）。 理由：近期状态：fnatic 最近 9胜1负（状态火热），Natus Vincere 最近 5胜5负（状态一般）；综合实力分 fnatic 比 Natus Vincere 高约 53 分。 总结：有一定爆冷可能。
- **Epsilon vs Dignitas**：我看好 Dignitas（系列赛胜率 65%，最可能比分 Dignitas 2:0）。 理由：老牌队伍经验更足：Epsilon 打过 50 局，Dignitas 打过 98 局；近期状态：Epsilon 最近 5胜5负（状态一般），Dignitas 最近 7胜3负（状态不错）；从长期战绩算出来的实力分看，Dignitas 领先 Epsilon 约 70 分。 总结：有一定爆冷可能。
- **LDLC vs Virtus.pro**：我看好 Virtus.pro（系列赛胜率 58%，最可能比分 Virtus.pro 2:0）。 理由：Virtus.pro 的职业比赛经验更多（LDLC 101 局 / Virtus.pro 145 局）；综合实力分 Virtus.pro 比 LDLC 高约 57 分。 总结：基本五五开，谁赢都不奇怪。
- **Cloud9 vs NiP**：倾向 NiP（系列赛胜率 87%，最可能比分 NiP 2:0）。 理由：NiP 的职业比赛经验更多（Cloud9 2 局 / NiP 170 局）；从长期战绩算出来的实力分看，NiP 领先 Cloud9 约 112 分。 不过要注意：近期状态：Cloud9 最近 2胜0负（状态火热），NiP 最近 3胜7负（状态低迷）。 总结：爆冷概率很低。

### DreamHack Winter 2014

训练数据截止：2014-11-27（之后的比赛模型都没见过）  
夺冠概率：Virtus.pro 23%，NiP 21%，fnatic 14%，HellRaisers 12%  
**预测冠军：NiP**　｜　实际冠军：LDLC ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | HellRaisers vs NiP | NiP | 57% | NiP 0-2 | ✅ |
| R1M2 | Virtus.pro vs PENTA | Virtus.pro | 84% | Virtus.pro 2-0 | ✅ |
| R1M3 | LDLC vs fnatic | fnatic | 52% | LDLC 2-1 | ❌ |
| R1M4 | Dignitas vs Natus Vincere | Natus Vincere | 53% | Natus Vincere 0-2 | ✅ |
| R2M1 | NiP vs Virtus.pro | NiP | 55% | NiP 2-1 | ✅ |
| R2M2 | LDLC vs Natus Vincere | LDLC | 54% | LDLC 2-0 | ✅ |
| R3M1 | NiP vs LDLC | NiP | 59% | LDLC 1-2 | ❌ |

**赛前观点（8 强）：**

- **HellRaisers vs NiP**：我的判断：NiP 晋级（系列赛胜率 57%，最可能比分 NiP 2:0）。 主要依据：老牌队伍经验更足：HellRaisers 打过 176 局，NiP 打过 236 局；NiP 整体硬实力更强（实力分高 46）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs PENTA**：倾向 Virtus.pro（系列赛胜率 84%，最可能比分 Virtus.pro 2:0）。 为什么：Virtus.pro 的职业比赛经验更多（Virtus.pro 256 局 / PENTA 44 局）；近期状态：Virtus.pro 最近 8胜2负（状态火热），PENTA 最近 4胜6负（状态一般）；Virtus.pro 整体硬实力更强（实力分高 114）。 总结：爆冷概率很低。
- **LDLC vs fnatic**：我看好 fnatic（系列赛胜率 52%，最可能比分 fnatic 2:0）。 为什么：fnatic 整体硬实力更强（实力分高 98）；老牌队伍经验更足：LDLC 打过 197 局，fnatic 打过 256 局。 不过要注意：近期状态：LDLC 最近 6胜4负（状态不错），fnatic 最近 7胜3负（状态不错）。 总结：基本五五开，谁赢都不奇怪。
- **Dignitas vs Natus Vincere**：倾向 Natus Vincere（系列赛胜率 53%，最可能比分 Natus Vincere 2:0）。 为什么：老牌队伍经验更足：Dignitas 打过 163 局，Natus Vincere 打过 225 局；近期状态：Dignitas 最近 6胜4负（状态不错），Natus Vincere 最近 6胜4负（状态不错）。 风险点：Dignitas 整体硬实力更强（实力分高 59）。 总结：基本五五开，谁赢都不奇怪。

### ESL One Katowice 2015

训练数据截止：2015-03-12（之后的比赛模型都没见过）  
夺冠概率：NiP 29%，Virtus.pro 28%，fnatic 27%，Natus Vincere 9%  
**预测冠军：fnatic**　｜　实际冠军：fnatic ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | fnatic vs PENTA | fnatic | 79% | fnatic 2-0 | ✅ |
| R1M2 | Virtus.pro vs Keyd | Virtus.pro | 97% | Virtus.pro 2-1 | ✅ |
| R1M3 | Envy vs Natus Vincere | Natus Vincere | 63% | Envy 2-1 | ❌ |
| R1M4 | NiP vs TSM | NiP | 78% | NiP 2-1 | ✅ |
| R2M1 | fnatic vs Virtus.pro | fnatic | 55% | fnatic 2-0 | ✅ |
| R2M2 | Envy vs NiP | NiP | 77% | NiP 0-2 | ✅ |
| R3M1 | fnatic vs NiP | fnatic | 52% | fnatic 2-1 | ✅ |

**赛前观点（8 强）：**

- **fnatic vs PENTA**：倾向 fnatic（系列赛胜率 79%，最可能比分 fnatic 2:0）。 主要依据：综合实力分 fnatic 比 PENTA 高约 187 分；老牌队伍经验更足：fnatic 打过 331 局，PENTA 打过 129 局；fnatic 最近手感比对手好（fnatic 6-4，PENTA 2-8，比赛结果都好于赛前预期）。 总结：有一定爆冷可能。
- **Virtus.pro vs Keyd**：倾向 Virtus.pro（系列赛胜率 97%，最可能比分 Virtus.pro 2:0）。 主要依据：Virtus.pro 的职业比赛经验更多（Virtus.pro 353 局 / Keyd 0 局）；综合实力分 Virtus.pro 比 Keyd 高约 138 分。 风险点：Keyd 最近手感比对手好（Virtus.pro 7-3，Keyd 0-0，比赛结果都好于赛前预期）。 总结：爆冷概率很低。
- **Envy vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 63%，最可能比分 Natus Vincere 2:0）。 理由：Natus Vincere 的职业比赛经验更多（Envy 42 局 / Natus Vincere 271 局）；Natus Vincere 整体硬实力更强（实力分高 91）。 但是：近期状态：Envy 最近 6胜4负（状态不错），Natus Vincere 最近 2胜8负（状态低迷）。 总结：有一定爆冷可能。
- **NiP vs TSM**：倾向 NiP（系列赛胜率 78%，最可能比分 NiP 2:0）。 为什么：老牌队伍经验更足：NiP 打过 290 局，TSM 打过 23 局；从长期战绩算出来的实力分看，NiP 领先 TSM 约 113 分。 风险点：近期状态：NiP 最近 7胜3负（状态不错），TSM 最近 7胜3负（状态不错）。 总结：有一定爆冷可能。

### ESL One Cologne 2015

训练数据截止：2015-08-20（之后的比赛模型都没见过）  
夺冠概率：NiP 18%，Natus Vincere 16%，Envy 16%，Virtus.pro 16%  
**预测冠军：NiP**　｜　实际冠军：fnatic ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Envy vs Natus Vincere | Natus Vincere | 50% | Envy 2-0 | ❌ |
| R1M2 | TSM vs Kinguin | TSM | 65% | TSM 2-0 | ✅ |
| R1M3 | Virtus.pro vs NiP | NiP | 52% | Virtus.pro 2-0 | ❌ |
| R1M4 | fnatic vs Luminosity | fnatic | 67% | fnatic 2-0 | ✅ |
| R2M1 | Envy vs TSM | Envy | 55% | Envy 2-1 | ✅ |
| R2M2 | Virtus.pro vs fnatic | Virtus.pro | 56% | fnatic 1-2 | ❌ |
| R3M1 | Envy vs fnatic | Envy | 56% | fnatic 0-2 | ❌ |

**赛前观点（8 强）：**

- **Envy vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 50%，最可能比分 Natus Vincere 2:0）。 理由：Natus Vincere 的职业比赛经验更多（Envy 233 局 / Natus Vincere 487 局）。 但是：近期状态：Envy 最近 8胜2负（状态火热），Natus Vincere 最近 6胜4负（状态不错）。 总结：基本五五开，谁赢都不奇怪。
- **TSM vs Kinguin**：倾向 TSM（系列赛胜率 65%，最可能比分 TSM 2:0）。 为什么：老牌队伍经验更足：TSM 打过 233 局，Kinguin 打过 73 局；从长期战绩算出来的实力分看，TSM 领先 Kinguin 约 54 分；TSM 最近手感比对手好（TSM 5-5，Kinguin 6-4，比赛结果都好于赛前预期）。 总结：有一定爆冷可能。
- **Virtus.pro vs NiP**：倾向 NiP（系列赛胜率 52%，最可能比分 NiP 2:0）。 为什么：NiP 最近手感比对手好（Virtus.pro 5-5，NiP 7-3，比赛结果都好于赛前预期）。 但是：Virtus.pro 的职业比赛经验更多（Virtus.pro 562 局 / NiP 436 局）。 总结：基本五五开，谁赢都不奇怪。
- **fnatic vs Luminosity**：我看好 fnatic（系列赛胜率 67%，最可能比分 fnatic 2:0）。 为什么：老牌队伍经验更足：fnatic 打过 505 局，Luminosity 打过 118 局；从长期战绩算出来的实力分看，fnatic 领先 Luminosity 约 154 分。 风险点：Luminosity 最近手感比对手好（fnatic 4-6，Luminosity 4-6，比赛结果都好于赛前预期）。 总结：有一定爆冷可能。

### DreamHack Open Cluj-Napoca 2015

训练数据截止：2015-10-28（之后的比赛模型都没见过）  
夺冠概率：NiP 18%，Virtus.pro 16%，TSM 13%，fnatic 13%  
**预测冠军：NiP**　｜　实际冠军：Envy ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Envy vs fnatic | fnatic | 56% | Envy 2-1 | ❌ |
| R1M2 | Virtus.pro vs G2 | Virtus.pro | 54% | G2 0-2 | ❌ |
| R1M3 | TSM vs NiP | NiP | 54% | NiP 0-2 | ✅ |
| R1M4 | Luminosity vs Natus Vincere | Natus Vincere | 52% | Natus Vincere 0-2 | ✅ |
| R2M1 | Envy vs G2 | G2 | 57% | Envy 2-1 | ❌ |
| R2M2 | NiP vs Natus Vincere | NiP | 59% | Natus Vincere 0-2 | ❌ |
| R3M1 | Envy vs Natus Vincere | Natus Vincere | 54% | Envy 2-0 | ❌ |

**赛前观点（8 强）：**

- **Envy vs fnatic**：倾向 fnatic（系列赛胜率 56%，最可能比分 fnatic 2:0）。 理由：老牌队伍经验更足：Envy 打过 286 局，fnatic 打过 572 局；从长期战绩算出来的实力分看，fnatic 领先 Envy 约 30 分。 不过要注意：近期状态：Envy 最近 4胜6负（状态一般），fnatic 最近 4胜6负（状态一般）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs G2**：我的判断：Virtus.pro 晋级（系列赛胜率 54%，最可能比分 Virtus.pro 2:0）。 为什么：老牌队伍经验更足：Virtus.pro 打过 644 局，G2 打过 254 局；Virtus.pro 整体硬实力更强（实力分高 32）。 风险点：G2 最近手感比对手好（Virtus.pro 6-4，G2 6-4，比赛结果都好于赛前预期）。 总结：基本五五开，谁赢都不奇怪。
- **TSM vs NiP**：我看好 NiP（系列赛胜率 54%，最可能比分 NiP 2:0）。 主要依据：NiP 的职业比赛经验更多（TSM 322 局 / NiP 479 局）；NiP 整体硬实力更强（实力分高 34）。 不过要注意：TSM 最近手感比对手好（TSM 6-4，NiP 7-3，比赛结果都好于赛前预期）。 总结：基本五五开，谁赢都不奇怪。
- **Luminosity vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 52%，最可能比分 Natus Vincere 2:0）。 理由：老牌队伍经验更足：Luminosity 打过 197 局，Natus Vincere 打过 547 局；Natus Vincere 整体硬实力更强（实力分高 80）。 风险点：近期状态：Luminosity 最近 7胜3负（状态不错），Natus Vincere 最近 4胜6负（状态一般）。 总结：基本五五开，谁赢都不奇怪。

### MLG Columbus 2016

训练数据截止：2016-03-29（之后的比赛模型都没见过）  
夺冠概率：fnatic 32%，NiP 25%，Luminosity 21%，Natus Vincere 14%  
**预测冠军：fnatic**　｜　实际冠军：Luminosity ❌  
预测 4 强命中 2/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs NiP | NiP | 58% | Natus Vincere 2-0 | ❌ |
| R1M2 | Astralis vs fnatic | fnatic | 80% | Astralis 2-0 | ❌ |
| R1M3 | Liquid vs CLG | Liquid | 67% | Liquid 2-0 | ✅ |
| R1M4 | Luminosity vs Virtus.pro | Luminosity | 82% | Luminosity 2-1 | ✅ |
| R2M1 | Natus Vincere vs Astralis | Natus Vincere | 74% | Natus Vincere 2-0 | ✅ |
| R2M2 | Liquid vs Luminosity | Luminosity | 70% | Luminosity 0-2 | ✅ |
| R3M1 | Natus Vincere vs Luminosity | Natus Vincere | 61% | Luminosity 0-2 | ❌ |

**赛前观点（8 强）：**

- **Natus Vincere vs NiP**：倾向 NiP（系列赛胜率 58%，最可能比分 NiP 2:0）。 为什么：近期状态：Natus Vincere 最近 8胜2负（状态火热），NiP 最近 9胜1负（状态火热）。 但是：老牌队伍经验更足：Natus Vincere 打过 634 局，NiP 打过 525 局。 地图BP推演：Natus Vincere禁Cache，NiP禁Train；Natus Vincere选Cobblestone（Natus Vincere胜率46%），NiP选Mirage（Natus Vincere胜率43%）；决胜图 Inferno（Natus Vincere胜率45%）。 总结：基本五五开，谁赢都不奇怪。
- **Astralis vs fnatic**：我的判断：fnatic 晋级（系列赛胜率 80%，最可能比分 fnatic 2:0）。 主要依据：fnatic 的职业比赛经验更多（Astralis 58 局 / fnatic 665 局）；fnatic 整体硬实力更强（实力分高 147）；近期状态：Astralis 最近 6胜4负（状态不错），fnatic 最近 8胜2负（状态火热）。 地图BP推演：Astralis禁Inferno，fnatic禁Mirage；Astralis选Train（Astralis胜率30%），fnatic选Dust2（Astralis胜率28%）；决胜图 Cache（Astralis胜率29%）。 总结：有一定爆冷可能。
- **Liquid vs CLG**：倾向 Liquid（系列赛胜率 67%，最可能比分 Liquid 2:0）。 主要依据：综合实力分 Liquid 比 CLG 高约 30 分；近期状态：Liquid 最近 7胜3负（状态不错），CLG 最近 4胜6负（状态一般）。 地图BP推演：Liquid禁Overpass，CLG禁Cache；Liquid选Cobblestone（Liquid胜率63%），CLG选Train（Liquid胜率61%）；决胜图 Mirage（Liquid胜率61%）。 总结：有一定爆冷可能。
- **Luminosity vs Virtus.pro**：我看好 Luminosity（系列赛胜率 82%，最可能比分 Luminosity 2:0）。 为什么：综合实力分 Luminosity 比 Virtus.pro 高约 143 分；近期状态：Luminosity 最近 8胜2负（状态火热），Virtus.pro 最近 3胜7负（状态低迷）。 风险点：老牌队伍经验更足：Luminosity 打过 300 局，Virtus.pro 打过 714 局。 地图BP推演：Luminosity禁Dust2，Virtus.pro禁Overpass；Luminosity选Train（Luminosity胜率74%），Virtus.pro选Cache（Luminosity胜率72%）；决胜图 Inferno（Luminosity胜率73%）。 总结：爆冷概率很低。

### ESL One Cologne 2016

训练数据截止：2016-07-05（之后的比赛模型都没见过）  
夺冠概率：fnatic 30%，Natus Vincere 28%，Virtus.pro 12%，Liquid 8%  
**预测冠军：Natus Vincere**　｜　实际冠军：SK ❌  
预测 4 强命中 3/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Virtus.pro vs Astralis | Virtus.pro | 54% | Virtus.pro 2-0 | ✅ |
| R1M2 | SK vs FlipSid3 | SK | 53% | SK 2-0 | ✅ |
| R1M3 | Natus Vincere vs Liquid | Natus Vincere | 66% | Liquid 1-2 | ❌ |
| R1M4 | Gambit vs fnatic | fnatic | 84% | fnatic 0-2 | ✅ |
| R2M1 | Virtus.pro vs SK | Virtus.pro | 60% | SK 1-2 | ❌ |
| R2M2 | Liquid vs fnatic | fnatic | 63% | Liquid 2-0 | ❌ |
| R3M1 | SK vs Liquid | Liquid | 62% | SK 2-0 | ❌ |

**赛前观点（8 强）：**

- **Virtus.pro vs Astralis**：倾向 Virtus.pro（系列赛胜率 54%，最可能比分 Virtus.pro 2:0）。 为什么：老牌队伍经验更足：Virtus.pro 打过 781 局，Astralis 打过 107 局；Virtus.pro 最近手感比对手好（Virtus.pro 6-4，Astralis 4-6，比赛结果都好于赛前预期）。 风险点：Astralis 整体硬实力更强（实力分高 73）。 地图BP推演：Virtus.pro禁Cache，Astralis禁Cobblestone；Virtus.pro选Train（Virtus.pro胜率54%），Astralis选Overpass（Virtus.pro胜率51%）；决胜图 Dust2（Virtus.pro胜率53%）。 总结：基本五五开，谁赢都不奇怪。
- **SK vs FlipSid3**：我看好 SK（系列赛胜率 53%，最可能比分 SK 2:0）。 为什么：从长期战绩算出来的实力分看，SK 领先 FlipSid3 约 30 分。 但是：FlipSid3 的职业比赛经验更多（SK 332 局 / FlipSid3 496 局）。 地图BP推演：SK禁Mirage，FlipSid3禁Inferno；SK选Train（SK胜率54%），FlipSid3选Overpass（SK胜率50%）；决胜图 Cobblestone（SK胜率51%）。 总结：基本五五开，谁赢都不奇怪。
- **Natus Vincere vs Liquid**：我看好 Natus Vincere（系列赛胜率 66%，最可能比分 Natus Vincere 2:0）。 理由：综合实力分 Natus Vincere 比 Liquid 高约 134 分；老牌队伍经验更足：Natus Vincere 打过 677 局，Liquid 打过 397 局；近期状态：Natus Vincere 最近 8胜2负（状态火热），Liquid 最近 5胜5负（状态一般）。 地图BP推演：Natus Vincere禁Cache，Liquid禁Overpass；Natus Vincere选Train（Natus Vincere胜率63%），Liquid选Cobblestone（Natus Vincere胜率59%）；决胜图 Mirage（Natus Vincere胜率61%）。 总结：有一定爆冷可能。
- **Gambit vs fnatic**：倾向 fnatic（系列赛胜率 84%，最可能比分 fnatic 2:0）。 理由：综合实力分 fnatic 比 Gambit 高约 237 分；fnatic 的职业比赛经验更多（Gambit 89 局 / fnatic 716 局）；近期状态：Gambit 最近 3胜7负（状态低迷），fnatic 最近 7胜3负（状态不错）。 地图BP推演：Gambit禁Dust2，fnatic禁Train；Gambit选Mirage（Gambit胜率27%），fnatic选Cache（Gambit胜率24%）；决胜图 Cobblestone（Gambit胜率26%）。 总结：爆冷概率很低。

### ELEAGUE Major 2017

训练数据截止：2017-01-22（之后的比赛模型都没见过）  
夺冠概率：Astralis 48%，Virtus.pro 21%，FaZe 9%，SK 8%  
**预测冠军：Astralis**　｜　实际冠军：Astralis ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs Astralis | Astralis | 82% | Astralis 1-2 | ✅ |
| R1M2 | fnatic vs Gambit | fnatic | 57% | fnatic 2-1 | ✅ |
| R1M3 | Virtus.pro vs North | Virtus.pro | 98% | Virtus.pro 2-1 | ✅ |
| R1M4 | FaZe vs SK | FaZe | 52% | SK 1-2 | ❌ |
| R2M1 | Astralis vs fnatic | Astralis | 78% | Astralis 2-0 | ✅ |
| R2M2 | Virtus.pro vs SK | Virtus.pro | 54% | Virtus.pro 2-0 | ✅ |
| R3M1 | Astralis vs Virtus.pro | Astralis | 71% | Astralis 2-1 | ✅ |

**赛前观点（8 强）：**

- **Natus Vincere vs Astralis**：我看好 Astralis（系列赛胜率 82%，最可能比分 Astralis 2:0）。 为什么：从长期战绩算出来的实力分看，Astralis 领先 Natus Vincere 约 140 分；Astralis 最近手感比对手好（Natus Vincere 4-6，Astralis 8-2，比赛结果都好于赛前预期）。 不过要注意：老牌队伍经验更足：Natus Vincere 打过 745 局，Astralis 打过 215 局。 地图BP推演：Natus Vincere禁Mirage，Astralis禁Overpass；Natus Vincere选Cobblestone（Natus Vincere胜率28%），Astralis选Dust2（Natus Vincere胜率26%）；决胜图 Train（Natus Vincere胜率27%）。 总结：爆冷概率很低。
- **fnatic vs Gambit**：我的判断：fnatic 晋级（系列赛胜率 57%，最可能比分 fnatic 2:0）。 为什么：老牌队伍经验更足：fnatic 打过 788 局，Gambit 打过 196 局；fnatic 整体硬实力更强（实力分高 30）。 风险点：Gambit 最近手感比对手好（fnatic 4-6，Gambit 8-2，比赛结果都好于赛前预期）。 地图BP推演：fnatic禁Cobblestone，Gambit禁Cache；fnatic选Nuke（fnatic胜率56%），Gambit选Dust2（fnatic胜率54%）；决胜图 Mirage（fnatic胜率55%）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs North**：我看好 Virtus.pro（系列赛胜率 98%，最可能比分 Virtus.pro 2:0）。 主要依据：Virtus.pro 的职业比赛经验更多（Virtus.pro 902 局 / North 0 局）；Virtus.pro 整体硬实力更强（实力分高 239）；近期状态：Virtus.pro 最近 8胜2负（状态火热），North 最近 0胜0负（暂无近期数据）。 地图BP推演：Virtus.pro禁Cache，North禁Cobblestone；Virtus.pro选Mirage（Virtus.pro胜率92%），North选Train（Virtus.pro胜率91%）；决胜图 Dust2（Virtus.pro胜率91%）。 总结：爆冷概率很低。
- **FaZe vs SK**：倾向 FaZe（系列赛胜率 52%，最可能比分 FaZe 2:0）。 为什么：FaZe 最近手感比对手好（FaZe 8-2，SK 4-6，比赛结果都好于赛前预期）。 不过要注意：老牌队伍经验更足：FaZe 打过 202 局，SK 打过 456 局。 地图BP推演：FaZe禁Train，SK禁Mirage；FaZe选Nuke（FaZe胜率53%），SK选Cobblestone（FaZe胜率50%）；决胜图 Cache（FaZe胜率51%）。 总结：基本五五开，谁赢都不奇怪。

### PGL Major Krakow 2017

训练数据截止：2017-07-16（之后的比赛模型都没见过）  
夺冠概率：SK 56%，BIG 13%，fnatic 9%，Astralis 9%  
**预测冠军：SK**　｜　实际冠军：Gambit ❌  
预测 4 强命中 0/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Gambit vs fnatic | fnatic | 70% | Gambit 2-0 | ❌ |
| R1M2 | SK vs Astralis | SK | 77% | Astralis 0-2 | ❌ |
| R1M3 | BIG vs Immortals | BIG | 62% | Immortals 1-2 | ❌ |
| R1M4 | North vs Virtus.pro | North | 69% | Virtus.pro 0-2 | ❌ |
| R2M1 | Gambit vs Astralis | Astralis | 76% | Gambit 2-1 | ❌ |
| R2M2 | Immortals vs Virtus.pro | Immortals | 69% | Immortals 2-0 | ✅ |
| R3M1 | Gambit vs Immortals | Immortals | 63% | Gambit 2-1 | ❌ |

**赛前观点（8 强）：**

- **Gambit vs fnatic**：倾向 fnatic（系列赛胜率 70%，最可能比分 fnatic 2:0）。 理由：综合实力分 fnatic 比 Gambit 高约 84 分；fnatic 的职业比赛经验更多（Gambit 269 局 / fnatic 891 局）。 地图BP推演：Gambit禁Cache，fnatic禁Train；Gambit选Cobblestone（Gambit胜率39%），fnatic选Inferno（Gambit胜率35%）；决胜图 Nuke（Gambit胜率36%）。 总结：有一定爆冷可能。
- **SK vs Astralis**：倾向 SK（系列赛胜率 77%，最可能比分 SK 2:0）。 主要依据：综合实力分 SK 比 Astralis 高约 78 分；SK 最近手感比对手好（SK 8-2，Astralis 6-4，比赛结果都好于赛前预期）；老牌队伍经验更足：SK 打过 581 局，Astralis 打过 310 局。 地图BP推演：SK禁Mirage，Astralis禁Cobblestone；SK选Cache（SK胜率71%），Astralis选Overpass（SK胜率67%）；决胜图 Inferno（SK胜率70%）。 总结：有一定爆冷可能。
- **BIG vs Immortals**：我的判断：BIG 晋级（系列赛胜率 62%，最可能比分 BIG 2:0）。 为什么：BIG 最近手感比对手好（BIG 9-1，Immortals 4-6，比赛结果都好于赛前预期）。 不过要注意：Immortals 的职业比赛经验更多（BIG 118 局 / Immortals 263 局）。 地图BP推演：BIG禁Overpass，Immortals禁Train；BIG选Cache（BIG胜率60%），Immortals选Mirage（BIG胜率57%）；决胜图 Cobblestone（BIG胜率58%）。 总结：有一定爆冷可能。
- **North vs Virtus.pro**：倾向 North（系列赛胜率 69%，最可能比分 North 2:0）。 理由：从长期战绩算出来的实力分看，North 领先 Virtus.pro 约 145 分。 但是：Virtus.pro 的职业比赛经验更多（North 87 局 / Virtus.pro 989 局）。 地图BP推演：North禁Mirage，Virtus.pro禁Overpass；North选Inferno（North胜率64%），Virtus.pro选Train（North胜率62%）；决胜图 Cobblestone（North胜率63%）。 总结：有一定爆冷可能。

### ELEAGUE Major 2018

训练数据截止：2018-01-12（之后的比赛模型都没见过）  
夺冠概率：SK 29%，FaZe 23%，mousesports 16%，Natus Vincere 12%  
**预测冠军：SK**　｜　实际冠军：Cloud9 ❌  
预测 4 强命中 4/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | FaZe vs mousesports | FaZe | 55% | FaZe 2-0 | ✅ |
| R1M2 | Natus Vincere vs Quantum Bellator Fire | Natus Vincere | 89% | Natus Vincere 2-0 | ✅ |
| R1M3 | G2 vs Cloud9 | Cloud9 | 61% | Cloud9 0-2 | ✅ |
| R1M4 | SK vs fnatic | SK | 67% | SK 2-1 | ✅ |
| R2M1 | FaZe vs Natus Vincere | FaZe | 68% | FaZe 2-0 | ✅ |
| R2M2 | Cloud9 vs SK | SK | 68% | Cloud9 2-1 | ❌ |
| R3M1 | FaZe vs Cloud9 | FaZe | 66% | Cloud9 1-2 | ❌ |

**赛前观点（8 强）：**

- **FaZe vs mousesports**：倾向 FaZe（系列赛胜率 55%，最可能比分 FaZe 2:0）。 为什么：FaZe 整体硬实力更强（实力分高 63）。 但是：老牌队伍经验更足：FaZe 打过 427 局，mousesports 打过 994 局。 地图BP推演：FaZe禁Cobblestone，mousesports禁Overpass；FaZe选Inferno（FaZe胜率56%），mousesports选Nuke（FaZe胜率51%）；决胜图 Train（FaZe胜率54%）。 总结：基本五五开，谁赢都不奇怪。
- **Natus Vincere vs Quantum Bellator Fire**：倾向 Natus Vincere（系列赛胜率 89%，最可能比分 Natus Vincere 2:0）。 理由：综合实力分 Natus Vincere 比 Quantum Bellator Fire 高约 190 分；老牌队伍经验更足：Natus Vincere 打过 901 局，Quantum Bellator Fire 打过 171 局；近期状态：Natus Vincere 最近 8胜2负（状态火热），Quantum Bellator Fire 最近 5胜5负（状态一般）。 地图BP推演：Natus Vincere禁Mirage，Quantum Bellator Fire禁Overpass；Natus Vincere选Train（Natus Vincere胜率80%），Quantum Bellator Fire选Inferno（Natus Vincere胜率79%）；决胜图 Nuke（Natus Vincere胜率79%）。 总结：爆冷概率很低。
- **G2 vs Cloud9**：倾向 Cloud9（系列赛胜率 61%，最可能比分 Cloud9 2:0）。 为什么：Cloud9 整体硬实力更强（实力分高 41）；近期状态：G2 最近 5胜5负（状态一般），Cloud9 最近 7胜3负（状态不错）。 地图BP推演：G2禁Train，Cloud9禁Nuke；G2选Inferno（G2胜率43%），Cloud9选Overpass（G2胜率42%）；决胜图 Cobblestone（G2胜率43%）。 总结：基本五五开，谁赢都不奇怪。
- **SK vs fnatic**：我的判断：SK 晋级（系列赛胜率 67%，最可能比分 SK 2:0）。 主要依据：从长期战绩算出来的实力分看，SK 领先 fnatic 约 82 分；近期状态：SK 最近 8胜2负（状态火热），fnatic 最近 5胜5负（状态一般）。 但是：老牌队伍经验更足：SK 打过 696 局，fnatic 打过 986 局。 地图BP推演：SK禁Inferno，fnatic禁Overpass；SK选Cobblestone（SK胜率64%），fnatic选Nuke（SK胜率59%）；决胜图 Mirage（SK胜率62%）。 总结：有一定爆冷可能。

### FACEIT Major 2018

训练数据截止：2018-09-05（之后的比赛模型都没见过）  
夺冠概率：Astralis 48%，Natus Vincere 16%，Liquid 15%，FaZe 8%  
**预测冠军：Astralis**　｜　实际冠军：Astralis ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Complexity vs MIBR | Complexity | 65% | MIBR 0-2 | ❌ |
| R1M2 | BIG vs Natus Vincere | Natus Vincere | 68% | Natus Vincere 0-2 | ✅ |
| R1M3 | Liquid vs HellRaisers | Liquid | 73% | Liquid 2-1 | ✅ |
| R1M4 | Astralis vs FaZe | Astralis | 76% | Astralis 2-0 | ✅ |
| R2M1 | MIBR vs Natus Vincere | Natus Vincere | 75% | Natus Vincere 0-2 | ✅ |
| R2M2 | Liquid vs Astralis | Astralis | 73% | Astralis 0-2 | ✅ |
| R3M1 | Natus Vincere vs Astralis | Astralis | 75% | Astralis 0-2 | ✅ |

**赛前观点（8 强）：**

- **Complexity vs MIBR**：我看好 Complexity（系列赛胜率 65%，最可能比分 Complexity 2:0）。 理由：老牌队伍经验更足：Complexity 打过 598 局，MIBR 打过 27 局；从长期战绩算出来的实力分看，Complexity 领先 MIBR 约 31 分。 但是：近期状态：Complexity 最近 6胜4负（状态不错），MIBR 最近 8胜2负（状态火热）。 地图BP推演：Complexity禁Overpass，MIBR禁Mirage；Complexity选Cache（Complexity胜率62%），MIBR选Dust2（Complexity胜率58%）；决胜图 Train（Complexity胜率60%）。 总结：有一定爆冷可能。
- **BIG vs Natus Vincere**：我看好 Natus Vincere（系列赛胜率 68%，最可能比分 Natus Vincere 2:0）。 为什么：Natus Vincere 整体硬实力更强（实力分高 133）；老牌队伍经验更足：BIG 打过 304 局，Natus Vincere 打过 1060 局。 风险点：BIG 最近手感比对手好（BIG 6-4，Natus Vincere 4-6，比赛结果都好于赛前预期）。 地图BP推演：BIG禁Train，Natus Vincere禁Dust2；BIG选Cache（BIG胜率40%），Natus Vincere选Mirage（BIG胜率35%）；决胜图 Nuke（BIG胜率39%）。 总结：有一定爆冷可能。
- **Liquid vs HellRaisers**：我的判断：Liquid 晋级（系列赛胜率 73%，最可能比分 Liquid 2:0）。 为什么：从长期战绩算出来的实力分看，Liquid 领先 HellRaisers 约 96 分；Liquid 最近手感比对手好（Liquid 6-4，HellRaisers 2-8，比赛结果都好于赛前预期）。 风险点：HellRaisers 的职业比赛经验更多（Liquid 897 局 / HellRaisers 1100 局）。 地图BP推演：Liquid禁Nuke，HellRaisers禁Inferno；Liquid选Mirage（Liquid胜率67%），HellRaisers选Overpass（Liquid胜率65%）；决胜图 Dust2（Liquid胜率66%）。 总结：有一定爆冷可能。
- **Astralis vs FaZe**：我看好 Astralis（系列赛胜率 76%，最可能比分 Astralis 2:0）。 主要依据：从长期战绩算出来的实力分看，Astralis 领先 FaZe 约 143 分。 地图BP推演：Astralis禁Cache，FaZe禁Nuke；Astralis选Train（Astralis胜率69%），FaZe选Mirage（Astralis胜率67%）；决胜图 Inferno（Astralis胜率68%）。 总结：有一定爆冷可能。

### IEM Katowice 2019

训练数据截止：2019-02-13（之后的比赛模型都没见过）  
夺冠概率：Astralis 45%，Liquid 24%，ENCE 8%，Renegades 6%  
**预测冠军：Astralis**　｜　实际冠军：Astralis ✅  
预测 4 强命中 2/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs FaZe | Natus Vincere | 58% | Natus Vincere 2-0 | ✅ |
| R1M2 | Liquid vs ENCE | Liquid | 65% | ENCE 0-2 | ❌ |
| R1M3 | MIBR vs Renegades | Renegades | 54% | MIBR 2-0 | ❌ |
| R1M4 | Astralis vs NiP | Astralis | 79% | Astralis 2-0 | ✅ |
| R2M1 | Natus Vincere vs ENCE | ENCE | 58% | ENCE 1-2 | ✅ |
| R2M2 | MIBR vs Astralis | Astralis | 80% | Astralis 0-2 | ✅ |
| R3M1 | ENCE vs Astralis | Astralis | 75% | Astralis 0-2 | ✅ |

**赛前观点（8 强）：**

- **Natus Vincere vs FaZe**：倾向 Natus Vincere（系列赛胜率 58%，最可能比分 Natus Vincere 2:0）。 主要依据：综合实力分 Natus Vincere 比 FaZe 高约 53 分；老牌队伍经验更足：Natus Vincere 打过 1140 局，FaZe 打过 676 局。 但是：近期状态：Natus Vincere 最近 5胜5负（状态一般），FaZe 最近 6胜4负（状态不错）。 地图BP推演：Natus Vincere禁Inferno，FaZe禁Train；Natus Vincere选Mirage（Natus Vincere胜率58%），FaZe选Dust2（Natus Vincere胜率53%）；决胜图 Nuke（Natus Vincere胜率55%）。 总结：基本五五开，谁赢都不奇怪。
- **Liquid vs ENCE**：我的判断：Liquid 晋级（系列赛胜率 65%，最可能比分 Liquid 2:0）。 理由：从长期战绩算出来的实力分看，Liquid 领先 ENCE 约 60 分；老牌队伍经验更足：Liquid 打过 1002 局，ENCE 打过 435 局；近期状态：Liquid 最近 7胜3负（状态不错），ENCE 最近 9胜1负（状态火热）。 地图BP推演：Liquid禁Train，ENCE禁Inferno；Liquid选Cache（Liquid胜率62%），ENCE选Nuke（Liquid胜率59%）；决胜图 Mirage（Liquid胜率60%）。 总结：有一定爆冷可能。
- **MIBR vs Renegades**：我看好 Renegades（系列赛胜率 54%，最可能比分 Renegades 2:0）。 主要依据：老牌队伍经验更足：MIBR 打过 118 局，Renegades 打过 695 局。 不过要注意：MIBR 整体硬实力更强（实力分高 25）。 地图BP推演：MIBR禁Cache，Renegades禁Overpass；MIBR选Mirage（MIBR胜率49%），Renegades选Nuke（MIBR胜率45%）；决胜图 Dust2（MIBR胜率48%）。 总结：基本五五开，谁赢都不奇怪。
- **Astralis vs NiP**：倾向 Astralis（系列赛胜率 79%，最可能比分 Astralis 2:0）。 为什么：从长期战绩算出来的实力分看，Astralis 领先 NiP 约 208 分。 不过要注意：老牌队伍经验更足：Astralis 打过 658 局，NiP 打过 1093 局。 地图BP推演：Astralis禁Train，NiP禁Inferno；Astralis选Nuke（Astralis胜率73%），NiP选Cache（Astralis胜率68%）；决胜图 Dust2（Astralis胜率71%）。 总结：有一定爆冷可能。

### StarLadder Major Berlin 2019

训练数据截止：2019-08-23（之后的比赛模型都没见过）  
夺冠概率：Liquid 56%，Astralis 12%，Vitality 10%，ENCE 10%  
**预测冠军：Liquid**　｜　实际冠军：Astralis ❌  
预测 4 强命中 1/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | ENCE vs Renegades | ENCE | 78% | Renegades 0-2 | ❌ |
| R1M2 | Vitality vs AVANGAR | Vitality | 74% | AVANGAR 1-2 | ❌ |
| R1M3 | NRG vs Natus Vincere | NRG | 50% | NRG 2-0 | ✅ |
| R1M4 | Astralis vs Liquid | Liquid | 75% | Astralis 2-0 | ❌ |
| R2M1 | Renegades vs AVANGAR | AVANGAR | 56% | AVANGAR 0-2 | ✅ |
| R2M2 | NRG vs Astralis | Astralis | 64% | Astralis 0-2 | ✅ |
| R3M1 | AVANGAR vs Astralis | Astralis | 86% | Astralis 0-2 | ✅ |

**赛前观点（8 强）：**

- **ENCE vs Renegades**：我的判断：ENCE 晋级（系列赛胜率 78%，最可能比分 ENCE 2:0）。 理由：ENCE 整体硬实力更强（实力分高 138）；近期状态：ENCE 最近 6胜4负（状态不错），Renegades 最近 1胜9负（状态低迷）。 但是：老牌队伍经验更足：ENCE 打过 522 局，Renegades 打过 763 局。 地图BP推演：ENCE禁Inferno，Renegades禁Train；ENCE选Overpass（ENCE胜率71%），Renegades选Vertigo（ENCE胜率69%）；决胜图 Dust2（ENCE胜率69%）。 总结：有一定爆冷可能。
- **Vitality vs AVANGAR**：倾向 Vitality（系列赛胜率 74%，最可能比分 Vitality 2:0）。 为什么：从长期战绩算出来的实力分看，Vitality 领先 AVANGAR 约 188 分。 但是：AVANGAR 最近手感比对手好（Vitality 4-6，AVANGAR 8-2，比赛结果都好于赛前预期）。 地图BP推演：Vitality禁Train，AVANGAR禁Overpass；Vitality选Nuke（Vitality胜率68%），AVANGAR选Mirage（Vitality胜率65%）；决胜图 Inferno（Vitality胜率67%）。 总结：有一定爆冷可能。
- **NRG vs Natus Vincere**：我看好 NRG（系列赛胜率 50%，最可能比分 NRG 2:0）。 主要依据：NRG 最近手感比对手好（NRG 8-2，Natus Vincere 7-3，比赛结果都好于赛前预期）。 但是：老牌队伍经验更足：NRG 打过 714 局，Natus Vincere 打过 1199 局。 地图BP推演：NRG禁Mirage，Natus Vincere禁Dust2；NRG选Overpass（NRG胜率51%），Natus Vincere选Train（NRG胜率49%）；决胜图 Inferno（NRG胜率51%）。 总结：基本五五开，谁赢都不奇怪。
- **Astralis vs Liquid**：我看好 Liquid（系列赛胜率 75%，最可能比分 Liquid 2:0）。 理由：Liquid 整体硬实力更强（实力分高 100）；近期状态：Astralis 最近 7胜3负（状态不错），Liquid 最近 9胜1负（状态火热）；老牌队伍经验更足：Astralis 打过 714 局，Liquid 打过 1136 局。 地图BP推演：Astralis禁Overpass，Liquid禁Nuke；Astralis选Train（Astralis胜率33%），Liquid选Dust2（Astralis胜率32%）；决胜图 Vertigo（Astralis胜率33%）。 总结：有一定爆冷可能。

### PGL Major Stockholm 2021

训练数据截止：2021-10-26（之后的比赛模型都没见过）  
夺冠概率：Natus Vincere 27%，Gambit 18%，Heroic 15%，NiP 14%  
**预测冠军：Natus Vincere**　｜　实际冠军：Natus Vincere ✅  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs Vitality | Natus Vincere | 60% | Natus Vincere 2-0 | ✅ |
| R1M2 | FURIA vs Gambit | Gambit | 70% | Gambit 0-2 | ✅ |
| R1M3 | Heroic vs Virtus.pro | Heroic | 62% | Heroic 2-1 | ✅ |
| R1M4 | NiP vs G2 | NiP | 64% | G2 0-2 | ❌ |
| R2M1 | Natus Vincere vs Gambit | Natus Vincere | 60% | Natus Vincere 2-0 | ✅ |
| R2M2 | Heroic vs G2 | Heroic | 65% | G2 1-2 | ❌ |
| R3M1 | Natus Vincere vs G2 | Natus Vincere | 78% | Natus Vincere 2-0 | ✅ |

**赛前观点（8 强）：**

- **Natus Vincere vs Vitality**：我的判断：Natus Vincere 晋级（系列赛胜率 60%，最可能比分 Natus Vincere 2:0）。 理由：从长期战绩算出来的实力分看，Natus Vincere 领先 Vitality 约 55 分；Natus Vincere 的职业比赛经验更多（Natus Vincere 1625 局 / Vitality 635 局）。 风险点：近期状态：Natus Vincere 最近 8胜2负（状态火热），Vitality 最近 7胜3负（状态不错）。 地图BP推演：Natus Vincere禁Overpass，Vitality禁Nuke；Natus Vincere选Mirage（Natus Vincere胜率59%），Vitality选Vertigo（Natus Vincere胜率54%）；决胜图 Ancient（Natus Vincere胜率57%）。 总结：基本五五开，谁赢都不奇怪。
- **FURIA vs Gambit**：倾向 Gambit（系列赛胜率 70%，最可能比分 Gambit 2:0）。 为什么：综合实力分 Gambit 比 FURIA 高约 146 分。 风险点：FURIA 最近手感比对手好（FURIA 8-2，Gambit 8-2，比赛结果都好于赛前预期）。 地图BP推演：FURIA禁Overpass，Gambit禁Inferno；FURIA选Ancient（FURIA胜率37%），Gambit选Vertigo（FURIA胜率34%）；决胜图 Mirage（FURIA胜率36%）。 总结：有一定爆冷可能。
- **Heroic vs Virtus.pro**：我的判断：Heroic 晋级（系列赛胜率 62%，最可能比分 Heroic 2:0）。 理由：从长期战绩算出来的实力分看，Heroic 领先 Virtus.pro 约 77 分；近期状态：Heroic 最近 6胜4负（状态不错），Virtus.pro 最近 4胜6负（状态一般）。 不过要注意：Virtus.pro 的职业比赛经验更多（Heroic 1156 局 / Virtus.pro 1902 局）。 地图BP推演：Heroic禁Inferno，Virtus.pro禁Overpass；Heroic选Vertigo（Heroic胜率59%），Virtus.pro选Dust2（Heroic胜率57%）；决胜图 Mirage（Heroic胜率58%）。 总结：有一定爆冷可能。
- **NiP vs G2**：我看好 NiP（系列赛胜率 64%，最可能比分 NiP 2:0）。 理由：NiP 整体硬实力更强（实力分高 97）。 不过要注意：G2 最近手感比对手好（NiP 7-3，G2 7-3，比赛结果都好于赛前预期）。 地图BP推演：NiP禁Nuke，G2禁Overpass；NiP选Ancient（NiP胜率61%），G2选Inferno（NiP胜率59%）；决胜图 Vertigo（NiP胜率60%）。 总结：有一定爆冷可能。

### PGL Major Antwerp 2022

训练数据截止：2022-05-09（之后的比赛模型都没见过）  
夺冠概率：Natus Vincere 32%，FaZe 28%，ENCE 13%，Heroic 10%  
**预测冠军：Natus Vincere**　｜　实际冠军：FaZe ❌  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs FURIA | FURIA | 65% | Spirit 2-0 | ❌ |
| R1M2 | FaZe vs NiP | FaZe | 70% | FaZe 2-1 | ✅ |
| R1M3 | ENCE vs Copenhagen Flames | ENCE | 69% | ENCE 2-0 | ✅ |
| R1M4 | Heroic vs Natus Vincere | Natus Vincere | 66% | Natus Vincere 1-2 | ✅ |
| R2M1 | Spirit vs FaZe | FaZe | 82% | FaZe 0-2 | ✅ |
| R2M2 | ENCE vs Natus Vincere | Natus Vincere | 68% | Natus Vincere 0-2 | ✅ |
| R3M1 | FaZe vs Natus Vincere | Natus Vincere | 57% | FaZe 2-0 | ❌ |

**赛前观点（8 强）：**

- **Spirit vs FURIA**：倾向 FURIA（系列赛胜率 65%，最可能比分 FURIA 2:0）。 主要依据：综合实力分 FURIA 比 Spirit 高约 84 分；近期状态：Spirit 最近 3胜7负（状态低迷），FURIA 最近 8胜2负（状态火热）。 风险点：老牌队伍经验更足：Spirit 打过 1208 局，FURIA 打过 864 局。 地图BP推演：Spirit禁Vertigo，FURIA禁Dust2；Spirit选Overpass（Spirit胜率41%），FURIA选Inferno（Spirit胜率39%）；决胜图 Nuke（Spirit胜率40%）。 总结：有一定爆冷可能。
- **FaZe vs NiP**：倾向 FaZe（系列赛胜率 70%，最可能比分 FaZe 2:0）。 为什么：综合实力分 FaZe 比 NiP 高约 109 分；FaZe 最近手感比对手好（FaZe 7-3，NiP 6-4，比赛结果都好于赛前预期）。 但是：老牌队伍经验更足：FaZe 打过 1191 局，NiP 打过 1663 局。 地图BP推演：FaZe禁Overpass，NiP禁Mirage；FaZe选Dust2（FaZe胜率65%），NiP选Ancient（FaZe胜率62%）；决胜图 Vertigo（FaZe胜率64%）。 总结：有一定爆冷可能。
- **ENCE vs Copenhagen Flames**：倾向 ENCE（系列赛胜率 69%，最可能比分 ENCE 2:0）。 为什么：ENCE 整体硬实力更强（实力分高 91）；近期状态：ENCE 最近 6胜4负（状态不错），Copenhagen Flames 最近 5胜5负（状态一般）；老牌队伍经验更足：ENCE 打过 873 局，Copenhagen Flames 打过 595 局。 地图BP推演：ENCE禁Vertigo，Copenhagen Flames禁Dust2；ENCE选Mirage（ENCE胜率65%），Copenhagen Flames选Overpass（ENCE胜率61%）；决胜图 Ancient（ENCE胜率64%）。 总结：有一定爆冷可能。
- **Heroic vs Natus Vincere**：倾向 Natus Vincere（系列赛胜率 66%，最可能比分 Natus Vincere 2:0）。 主要依据：从长期战绩算出来的实力分看，Natus Vincere 领先 Heroic 约 91 分；Natus Vincere 的职业比赛经验更多（Heroic 1214 局 / Natus Vincere 1691 局）。 地图BP推演：Heroic禁Mirage，Natus Vincere禁Overpass；Heroic选Vertigo（Heroic胜率41%），Natus Vincere选Ancient（Heroic胜率38%）；决胜图 Nuke（Heroic胜率39%）。 总结：有一定爆冷可能。

### IEM Rio Major 2022

训练数据截止：2022-10-31（之后的比赛模型都没见过）  
夺冠概率：Natus Vincere 27%，Heroic 26%，Virtus.pro 16%，Cloud9 13%  
**预测冠军：Natus Vincere**　｜　实际冠军：Virtus.pro ❌  
预测 4 强命中 2/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Cloud9 vs mousesports | Cloud9 | 56% | mousesports 1-2 | ❌ |
| R1M2 | fnatic vs Virtus.pro | Virtus.pro | 64% | Virtus.pro 0-2 | ✅ |
| R1M3 | Heroic vs Spirit | Heroic | 74% | Heroic 2-0 | ✅ |
| R1M4 | Natus Vincere vs FURIA | Natus Vincere | 72% | FURIA 1-2 | ❌ |
| R2M1 | mousesports vs Virtus.pro | Virtus.pro | 58% | Virtus.pro 1-2 | ✅ |
| R2M2 | Heroic vs FURIA | Heroic | 70% | Heroic 2-1 | ✅ |
| R3M1 | Virtus.pro vs Heroic | Heroic | 59% | Virtus.pro 2-0 | ❌ |

**赛前观点（8 强）：**

- **Cloud9 vs mousesports**：我看好 Cloud9（系列赛胜率 56%，最可能比分 Cloud9 2:0）。 理由：从长期战绩算出来的实力分看，Cloud9 领先 mousesports 约 57 分。 但是：老牌队伍经验更足：Cloud9 打过 1315 局，mousesports 打过 1904 局。 地图BP推演：Cloud9禁Nuke，mousesports禁Overpass；Cloud9选Ancient（Cloud9胜率56%），mousesports选Inferno（Cloud9胜率53%）；决胜图 Vertigo（Cloud9胜率54%）。 总结：基本五五开，谁赢都不奇怪。
- **fnatic vs Virtus.pro**：我看好 Virtus.pro（系列赛胜率 64%，最可能比分 Virtus.pro 2:0）。 理由：Virtus.pro 整体硬实力更强（实力分高 77）；近期状态：fnatic 最近 6胜4负（状态不错），Virtus.pro 最近 8胜2负（状态火热）。 地图BP推演：fnatic禁Dust2，Virtus.pro禁Overpass；fnatic选Inferno（fnatic胜率42%），Virtus.pro选Nuke（fnatic胜率40%）；决胜图 Mirage（fnatic胜率40%）。 总结：有一定爆冷可能。
- **Heroic vs Spirit**：倾向 Heroic（系列赛胜率 74%，最可能比分 Heroic 2:0）。 为什么：Heroic 整体硬实力更强（实力分高 144）；Heroic 最近手感比对手好（Heroic 9-1，Spirit 7-3，比赛结果都好于赛前预期）。 地图BP推演：Heroic禁Dust2，Spirit禁Inferno；Heroic选Nuke（Heroic胜率68%），Spirit选Ancient（Heroic胜率66%）；决胜图 Overpass（Heroic胜率67%）。 总结：有一定爆冷可能。
- **Natus Vincere vs FURIA**：我的判断：Natus Vincere 晋级（系列赛胜率 72%，最可能比分 Natus Vincere 2:0）。 为什么：综合实力分 Natus Vincere 比 FURIA 高约 139 分；Natus Vincere 的职业比赛经验更多（Natus Vincere 1747 局 / FURIA 914 局）。 地图BP推演：Natus Vincere禁Vertigo，FURIA禁Nuke；Natus Vincere选Dust2（Natus Vincere胜率66%），FURIA选Overpass（Natus Vincere胜率64%）；决胜图 Mirage（Natus Vincere胜率64%）。 总结：有一定爆冷可能。

### BLAST.tv Paris Major 2023

训练数据截止：2023-05-08（之后的比赛模型都没见过）  
夺冠概率：FaZe 28%，Liquid 27%，Vitality 22%，Heroic 20%  
**预测冠军：FaZe**　｜　实际冠军：Vitality ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Heroic vs FaZe | FaZe | 55% | Heroic 2-1 | ❌ |
| R1M2 | GamerLegion vs Monte | GamerLegion | 72% | GamerLegion 2-0 | ✅ |
| R1M3 | Liquid vs Apeks | Liquid | 84% | Apeks 0-2 | ❌ |
| R1M4 | Into The Breach vs Vitality | Vitality | 90% | Vitality 0-2 | ✅ |
| R2M1 | Heroic vs GamerLegion | Heroic | 80% | GamerLegion 1-2 | ❌ |
| R2M2 | Apeks vs Vitality | Vitality | 81% | Vitality 0-2 | ✅ |
| R3M1 | GamerLegion vs Vitality | Vitality | 77% | Vitality 0-2 | ✅ |

**赛前观点（8 强）：**

- **Heroic vs FaZe**：倾向 FaZe（系列赛胜率 55%，最可能比分 FaZe 2:0）。 理由：从长期战绩算出来的实力分看，FaZe 领先 Heroic 约 34 分。 总结：基本五五开，谁赢都不奇怪。
- **GamerLegion vs Monte**：我的判断：GamerLegion 晋级（系列赛胜率 72%，最可能比分 GamerLegion 2:0）。 主要依据：GamerLegion 的职业比赛经验更多（GamerLegion 345 局 / Monte 3 局）；综合实力分 GamerLegion 比 Monte 高约 38 分；近期状态：GamerLegion 最近 4胜6负（状态一般），Monte 最近 0胜3负（状态低迷）。 总结：有一定爆冷可能。
- **Liquid vs Apeks**：倾向 Liquid（系列赛胜率 84%，最可能比分 Liquid 2:0）。 为什么：Liquid 整体硬实力更强（实力分高 210）；老牌队伍经验更足：Liquid 打过 1634 局，Apeks 打过 78 局。 总结：爆冷概率很低。
- **Into The Breach vs Vitality**：倾向 Vitality（系列赛胜率 90%，最可能比分 Vitality 2:0）。 理由：Vitality 整体硬实力更强（实力分高 264）；老牌队伍经验更足：Into The Breach 打过 9 局，Vitality 打过 794 局。 总结：爆冷概率很低。

### PGL Major Copenhagen 2024

训练数据截止：2024-03-17（之后的比赛模型都没见过）  
夺冠概率：Spirit 28%，G2 17%，Vitality 13%，FaZe 13%  
**预测冠军：Spirit**　｜　实际冠军：Natus Vincere ❌  
预测 4 强命中 3/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs FaZe | Spirit | 61% | FaZe 1-2 | ❌ |
| R1M2 | Vitality vs Cloud9 | Vitality | 62% | Vitality 2-0 | ✅ |
| R1M3 | Eternal Fire vs Natus Vincere | Natus Vincere | 60% | Natus Vincere 0-2 | ✅ |
| R1M4 | G2 vs mousesports | G2 | 55% | G2 2-0 | ✅ |
| R2M1 | FaZe vs Vitality | FaZe | 53% | FaZe 2-1 | ✅ |
| R2M2 | Natus Vincere vs G2 | G2 | 62% | Natus Vincere 2-1 | ❌ |
| R3M1 | FaZe vs Natus Vincere | FaZe | 62% | Natus Vincere 1-2 | ❌ |

**赛前观点（8 强）：**

- **Spirit vs FaZe**：我看好 Spirit（系列赛胜率 61%，最可能比分 Spirit 2:0）。 主要依据：Spirit 整体硬实力更强（实力分高 53）；近期状态：Spirit 最近 8胜2负（状态火热），FaZe 最近 5胜5负（状态一般）。 地图BP推演：Spirit禁Inferno，FaZe禁Overpass；Spirit选Mirage（Spirit胜率59%），FaZe选Nuke（Spirit胜率57%）；决胜图 Anubis（Spirit胜率57%）。 总结：基本五五开，谁赢都不奇怪。
- **Vitality vs Cloud9**：我的判断：Vitality 晋级（系列赛胜率 62%，最可能比分 Vitality 2:0）。 主要依据：从长期战绩算出来的实力分看，Vitality 领先 Cloud9 约 66 分；近期状态：Vitality 最近 6胜4负（状态不错），Cloud9 最近 6胜4负（状态不错）。 但是：老牌队伍经验更足：Vitality 打过 840 局，Cloud9 打过 1387 局。 地图BP推演：Vitality禁Overpass，Cloud9禁Inferno；Vitality选Vertigo（Vitality胜率60%），Cloud9选Ancient（Vitality胜率57%）；决胜图 Anubis（Vitality胜率58%）。 总结：有一定爆冷可能。
- **Eternal Fire vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 60%，最可能比分 Natus Vincere 2:0）。 为什么：Natus Vincere 的职业比赛经验更多（Eternal Fire 166 局 / Natus Vincere 1817 局）；从长期战绩算出来的实力分看，Natus Vincere 领先 Eternal Fire 约 40 分。 不过要注意：近期状态：Eternal Fire 最近 5胜5负（状态一般），Natus Vincere 最近 5胜5负（状态一般）。 地图BP推演：Eternal Fire禁Nuke，Natus Vincere禁Inferno；Eternal Fire选Vertigo（Eternal Fire胜率44%），Natus Vincere选Mirage（Eternal Fire胜率41%）；决胜图 Overpass（Eternal Fire胜率43%）。 总结：基本五五开，谁赢都不奇怪。
- **G2 vs mousesports**：我的判断：G2 晋级（系列赛胜率 55%，最可能比分 G2 2:0）。 主要依据：综合实力分 G2 比 mousesports 高约 51 分。 风险点：mousesports 最近手感比对手好（G2 7-3，mousesports 8-2，比赛结果都好于赛前预期）。 地图BP推演：G2禁Mirage，mousesports禁Inferno；G2选Nuke（G2胜率54%），mousesports选Overpass（G2胜率53%）；决胜图 Ancient（G2胜率53%）。 总结：基本五五开，谁赢都不奇怪。

### Perfect World Shanghai Major 2024

训练数据截止：2024-11-30（之后的比赛模型都没见过）  
夺冠概率：G2 26%，Vitality 22%，Spirit 14%，mousesports 13%  
**预测冠军：G2**　｜　实际冠军：Spirit ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | The Mongolz vs mousesports | mousesports | 56% | mousesports 0-2 | ✅ |
| R1M2 | Liquid vs Spirit | Spirit | 58% | Spirit 0-2 | ✅ |
| R1M3 | G2 vs Heroic | G2 | 71% | G2 2-1 | ✅ |
| R1M4 | FaZe vs Vitality | Vitality | 65% | FaZe 2-1 | ❌ |
| R2M1 | mousesports vs Spirit | Spirit | 50% | Spirit 1-2 | ✅ |
| R2M2 | G2 vs FaZe | G2 | 67% | FaZe 0-2 | ❌ |
| R3M1 | Spirit vs FaZe | Spirit | 56% | Spirit 2-1 | ✅ |

**赛前观点（8 强）：**

- **The Mongolz vs mousesports**：倾向 mousesports（系列赛胜率 56%，最可能比分 mousesports 2:0）。 为什么：mousesports 的职业比赛经验更多（The Mongolz 415 局 / mousesports 2080 局）；综合实力分 mousesports 比 The Mongolz 高约 7 分。 地图BP推演：The Mongolz禁Mirage，mousesports禁Dust2；The Mongolz选Ancient（The Mongolz胜率47%），mousesports选Inferno（The Mongolz胜率45%）；决胜图 Anubis（The Mongolz胜率46%）。 总结：基本五五开，谁赢都不奇怪。
- **Liquid vs Spirit**：我的判断：Spirit 晋级（系列赛胜率 58%，最可能比分 Spirit 2:0）。 理由：Spirit 整体硬实力更强（实力分高 53）；近期状态：Liquid 最近 5胜5负（状态一般），Spirit 最近 6胜4负（状态不错）。 地图BP推演：Liquid禁Nuke，Spirit禁Inferno；Liquid选Ancient（Liquid胜率46%），Spirit选Dust2（Liquid胜率42%）；决胜图 Mirage（Liquid胜率45%）。 总结：基本五五开，谁赢都不奇怪。
- **G2 vs Heroic**：我的判断：G2 晋级（系列赛胜率 71%，最可能比分 G2 2:0）。 理由：从长期战绩算出来的实力分看，G2 领先 Heroic 约 122 分。 地图BP推演：G2禁Mirage，Heroic禁Inferno；G2选Nuke（G2胜率66%），Heroic选Vertigo（G2胜率62%）；决胜图 Dust2（G2胜率64%）。 总结：有一定爆冷可能。
- **FaZe vs Vitality**：倾向 Vitality（系列赛胜率 65%，最可能比分 Vitality 2:0）。 主要依据：Vitality 整体硬实力更强（实力分高 90）；近期状态：FaZe 最近 6胜4负（状态不错），Vitality 最近 8胜2负（状态火热）。 但是：老牌队伍经验更足：FaZe 打过 1492 局，Vitality 打过 940 局。 地图BP推演：FaZe禁Nuke，Vitality禁Inferno；FaZe选Anubis（FaZe胜率41%），Vitality选Dust2（FaZe胜率38%）；决胜图 Ancient（FaZe胜率41%）。 总结：有一定爆冷可能。

### BLAST.tv Austin Major 2025

训练数据截止：2025-06-03（之后的比赛模型都没见过）  
夺冠概率：Vitality 51%，Spirit 17%，mousesports 12%，The Mongolz 10%  
**预测冠军：Vitality**　｜　实际冠军：Vitality ✅  
预测 4 强命中 2/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs mousesports | Spirit | 54% | mousesports 1-2 | ❌ |
| R1M2 | Vitality vs Natus Vincere | Vitality | 84% | Vitality 2-0 | ✅ |
| R1M3 | FaZe vs The Mongolz | The Mongolz | 64% | The Mongolz 0-2 | ✅ |
| R1M4 | paiN Gaming vs FURIA | FURIA | 75% | paiN Gaming 2-1 | ❌ |
| R2M1 | mousesports vs Vitality | Vitality | 71% | Vitality 1-2 | ✅ |
| R2M2 | The Mongolz vs paiN Gaming | The Mongolz | 87% | The Mongolz 2-0 | ✅ |
| R3M1 | Vitality vs The Mongolz | Vitality | 85% | Vitality 2-1 | ✅ |

**赛前观点（8 强）：**

- **Spirit vs mousesports**：倾向 Spirit（系列赛胜率 54%，最可能比分 Spirit 2:0）。 主要依据：Spirit 整体硬实力更强（实力分高 35）。 风险点：mousesports 的职业比赛经验更多（Spirit 1547 局 / mousesports 2167 局）。 地图BP推演：Spirit禁Mirage，mousesports禁Dust2；Spirit选Anubis（Spirit胜率53%），mousesports选Inferno（Spirit胜率51%）；决胜图 Train（Spirit胜率53%）。 总结：基本五五开，谁赢都不奇怪。
- **Vitality vs Natus Vincere**：我的判断：Vitality 晋级（系列赛胜率 84%，最可能比分 Vitality 2:0）。 主要依据：从长期战绩算出来的实力分看，Vitality 领先 Natus Vincere 约 223 分；Vitality 最近手感比对手好（Vitality 8-2，Natus Vincere 7-3，比赛结果都好于赛前预期）。 但是：老牌队伍经验更足：Vitality 打过 1023 局，Natus Vincere 打过 1986 局。 地图BP推演：Vitality禁Mirage，Natus Vincere禁Inferno；Vitality选Nuke（Vitality胜率77%），Natus Vincere选Train（Vitality胜率73%）；决胜图 Ancient（Vitality胜率75%）。 总结：爆冷概率很低。
- **FaZe vs The Mongolz**：倾向 The Mongolz（系列赛胜率 64%，最可能比分 The Mongolz 2:0）。 主要依据：从长期战绩算出来的实力分看，The Mongolz 领先 FaZe 约 87 分；The Mongolz 最近手感比对手好（FaZe 4-6，The Mongolz 6-4，比赛结果都好于赛前预期）。 但是：老牌队伍经验更足：FaZe 打过 1565 局，The Mongolz 打过 502 局。 地图BP推演：FaZe禁Dust2，The Mongolz禁Inferno；FaZe选Anubis（FaZe胜率42%），The Mongolz选Mirage（FaZe胜率40%）；决胜图 Nuke（FaZe胜率41%）。 总结：有一定爆冷可能。
- **paiN Gaming vs FURIA**：我看好 FURIA（系列赛胜率 75%，最可能比分 FURIA 2:0）。 主要依据：从长期战绩算出来的实力分看，FURIA 领先 paiN Gaming 约 102 分；近期状态：paiN Gaming 最近 2胜8负（状态低迷），FURIA 最近 4胜6负（状态一般）；FURIA 的职业比赛经验更多（paiN Gaming 513 局 / FURIA 1165 局）。 地图BP推演：paiN Gaming禁Train，FURIA禁Nuke；paiN Gaming选Mirage（paiN Gaming胜率34%），FURIA选Inferno（paiN Gaming胜率31%）；决胜图 Dust2（paiN Gaming胜率33%）。 总结：有一定爆冷可能。

### StarLadder Budapest Major 2025

训练数据截止：2025-11-24（之后的比赛模型都没见过）  
夺冠概率：FURIA 43%，mousesports 21%，Vitality 15%，Team Falcons 13%  
**预测冠军：FURIA**　｜　实际冠军：Vitality ❌  
预测 4 强命中 1/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs Team Falcons | Team Falcons | 59% | Spirit 2-0 | ❌ |
| R1M2 | The Mongolz vs Vitality | Vitality | 78% | Vitality 0-2 | ✅ |
| R1M3 | mousesports vs FaZe | mousesports | 82% | FaZe 0-2 | ❌ |
| R1M4 | Natus Vincere vs FURIA | FURIA | 85% | Natus Vincere 2-1 | ❌ |
| R2M1 | Spirit vs Vitality | Vitality | 56% | Vitality 0-2 | ✅ |
| R2M2 | FaZe vs Natus Vincere | Natus Vincere | 59% | FaZe 2-1 | ❌ |
| R3M1 | Vitality vs FaZe | Vitality | 84% | Vitality 3-1 | ✅ |

**赛前观点（8 强）：**

- **Spirit vs Team Falcons**：倾向 Team Falcons（系列赛胜率 59%，最可能比分 Team Falcons 2:0）。 为什么：从长期战绩算出来的实力分看，Team Falcons 领先 Spirit 约 65 分；近期状态：Spirit 最近 4胜6负（状态一般），Team Falcons 最近 7胜3负（状态不错）。 但是：老牌队伍经验更足：Spirit 打过 1609 局，Team Falcons 打过 352 局。 地图BP推演：Spirit禁Nuke，Team Falcons禁Dust2；Spirit选Overpass（Spirit胜率46%），Team Falcons选Ancient（Spirit胜率42%）；决胜图 Mirage（Spirit胜率44%）。 总结：基本五五开，谁赢都不奇怪。
- **The Mongolz vs Vitality**：我看好 Vitality（系列赛胜率 78%，最可能比分 Vitality 2:0）。 为什么：Vitality 整体硬实力更强（实力分高 148）；Vitality 的职业比赛经验更多（The Mongolz 592 局 / Vitality 1109 局）；近期状态：The Mongolz 最近 3胜7负（状态低迷），Vitality 最近 4胜6负（状态一般）。 地图BP推演：The Mongolz禁Dust2，Vitality禁Ancient；The Mongolz选Mirage（The Mongolz胜率32%），Vitality选Nuke（The Mongolz胜率29%）；决胜图 Overpass（The Mongolz胜率31%）。 总结：有一定爆冷可能。
- **mousesports vs FaZe**：我的判断：mousesports 晋级（系列赛胜率 82%，最可能比分 mousesports 2:0）。 为什么：从长期战绩算出来的实力分看，mousesports 领先 FaZe 约 175 分；mousesports 最近手感比对手好（mousesports 5-5，FaZe 4-6，比赛结果都好于赛前预期）；mousesports 的职业比赛经验更多（mousesports 2236 局 / FaZe 1638 局）。 地图BP推演：mousesports禁Ancient，FaZe禁Train；mousesports选Overpass（mousesports胜率74%），FaZe选Inferno（mousesports胜率72%）；决胜图 Mirage（mousesports胜率73%）。 总结：爆冷概率很低。
- **Natus Vincere vs FURIA**：我的判断：FURIA 晋级（系列赛胜率 85%，最可能比分 FURIA 2:0）。 为什么：综合实力分 FURIA 比 Natus Vincere 高约 185 分；近期状态：Natus Vincere 最近 2胜8负（状态低迷），FURIA 最近 8胜2负（状态火热）。 风险点：Natus Vincere 的职业比赛经验更多（Natus Vincere 2052 局 / FURIA 1275 局）。 地图BP推演：Natus Vincere禁Nuke，FURIA禁Train；Natus Vincere选Dust2（Natus Vincere胜率26%），FURIA选Inferno（Natus Vincere胜率23%）；决胜图 Ancient（Natus Vincere胜率26%）。 总结：爆冷概率很低。

### IEM Cologne Major 2026

训练数据截止：2026-06-02（之后的比赛模型都没见过）  
夺冠概率：Vitality 41%，Spirit 36%，FURIA 8%，Team Falcons 4%  
**预测冠军：Vitality**　｜　实际冠军：Team Falcons ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs G2 | Spirit | 78% | Spirit 2-1 | ✅ |
| R1M2 | Team Falcons vs Vitality | Vitality | 78% | Team Falcons 2-1 | ❌ |
| R1M3 | Aurora Gaming vs BetBoom Team | Aurora Gaming | 56% | Aurora Gaming 2-0 | ✅ |
| R1M4 | 9z Team vs FURIA | FURIA | 72% | FURIA 1-2 | ✅ |
| R2M1 | Spirit vs Team Falcons | Spirit | 75% | Team Falcons 1-2 | ❌ |
| R2M2 | Aurora Gaming vs FURIA | FURIA | 55% | FURIA 0-2 | ✅ |
| R3M1 | Team Falcons vs FURIA | Team Falcons | 54% | Team Falcons 3-0 | ✅ |

**赛前观点（8 强）：**

- **Spirit vs G2**：我的判断：Spirit 晋级（系列赛胜率 78%，最可能比分 Spirit 2:0）。 理由：Spirit 整体硬实力更强（实力分高 129）；近期状态：Spirit 最近 9胜1负（状态火热），G2 最近 4胜6负（状态一般）。 地图BP推演：Spirit禁Inferno，G2禁Dust2；Spirit选Anubis（Spirit胜率70%），G2选Nuke（Spirit胜率69%）；决胜图 Mirage（Spirit胜率70%）。 总结：有一定爆冷可能。
- **Team Falcons vs Vitality**：倾向 Vitality（系列赛胜率 78%，最可能比分 Vitality 2:0）。 主要依据：综合实力分 Vitality 比 Team Falcons 高约 154 分；Vitality 的职业比赛经验更多（Team Falcons 435 局 / Vitality 1189 局）。 地图BP推演：Team Falcons禁Dust2，Vitality禁Ancient；Team Falcons选Anubis（Team Falcons胜率32%），Vitality选Inferno（Team Falcons胜率27%）；决胜图 Mirage（Team Falcons胜率31%）。 总结：有一定爆冷可能。
- **Aurora Gaming vs BetBoom Team**：我的判断：Aurora Gaming 晋级（系列赛胜率 56%，最可能比分 Aurora Gaming 2:0）。 主要依据：Aurora Gaming 最近手感比对手好（Aurora Gaming 6-4，BetBoom Team 5-5，比赛结果都好于赛前预期）；Aurora Gaming 整体硬实力更强（实力分高 16）。 地图BP推演：Aurora Gaming禁Nuke，BetBoom Team禁Mirage；Aurora Gaming选Overpass（Aurora Gaming胜率55%），BetBoom Team选Dust2（Aurora Gaming胜率52%）；决胜图 Ancient（Aurora Gaming胜率53%）。 总结：基本五五开，谁赢都不奇怪。
- **9z Team vs FURIA**：我的判断：FURIA 晋级（系列赛胜率 72%，最可能比分 FURIA 2:0）。 理由：FURIA 整体硬实力更强（实力分高 101）；FURIA 的职业比赛经验更多（9z Team 283 局 / FURIA 1362 局）。 但是：9z Team 最近手感比对手好（9z Team 5-5，FURIA 6-4，比赛结果都好于赛前预期）。 地图BP推演：9z Team禁Mirage，FURIA禁Ancient；9z Team选Overpass（9z Team胜率36%），FURIA选Inferno（9z Team胜率34%）；决胜图 Nuke（9z Team胜率35%）。 总结：有一定爆冷可能。
