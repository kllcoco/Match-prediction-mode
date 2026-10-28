# CS Major 回测 · 严格模式（训练时不看任何世界赛/MSI/Major）

- 系列赛预测命中率：**62.1%**（161 场；瞎猜 50%）
- 4 强命中：62.0%　决赛队伍命中：47.8%　冠军命中：**26.1%**（瞎猜 12.5%）
- 对真实冠军给出的平均夺冠概率：20.6%　对数损失：0.646（越低越好，瞎猜 0.693）

### EMS One Katowice 2014

训练数据截止：2014-03-13（之后的比赛模型都没见过）  
夺冠概率：NiP 22%，Virtus.pro 16%，LGB 15%，Complexity 13%  
**预测冠军：NiP**　｜　实际冠军：Virtus.pro ❌  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | NiP vs Complexity | NiP | 57% | NiP 2-1 | ✅ |
| R1M2 | Dignitas vs HellRaisers | HellRaisers | 51% | Dignitas 2-0 | ❌ |
| R1M3 | Virtus.pro vs LDLC | Virtus.pro | 60% | Virtus.pro 2-0 | ✅ |
| R1M4 | fnatic vs LGB | LGB | 54% | LGB 1-2 | ✅ |
| R2M1 | NiP vs Dignitas | NiP | 65% | NiP 2-0 | ✅ |
| R2M2 | Virtus.pro vs LGB | Virtus.pro | 51% | Virtus.pro 2-1 | ✅ |
| R3M1 | NiP vs Virtus.pro | NiP | 56% | Virtus.pro 0-2 | ❌ |

**赛前观点（8 强）：**

- **NiP vs Complexity**：倾向 NiP（系列赛胜率 57%，最可能比分 NiP 2:0）。 理由：综合实力分 NiP 比 Complexity 高约 33 分。 总结：基本五五开，谁赢都不奇怪。
- **Dignitas vs HellRaisers**：我的判断：HellRaisers 晋级（系列赛胜率 51%，最可能比分 HellRaisers 2:0）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs LDLC**：我看好 Virtus.pro（系列赛胜率 60%，最可能比分 Virtus.pro 2:0）。 主要依据：从长期战绩算出来的实力分看，Virtus.pro 领先 LDLC 约 49 分。 总结：基本五五开，谁赢都不奇怪。
- **fnatic vs LGB**：我看好 LGB（系列赛胜率 54%，最可能比分 LGB 2:0）。 为什么：综合实力分 LGB 比 fnatic 高约 20 分。 总结：基本五五开，谁赢都不奇怪。

### ESL One Cologne 2014

训练数据截止：2014-08-14（之后的比赛模型都没见过）  
夺冠概率：fnatic 27%，Virtus.pro 19%，NiP 14%，Dignitas 13%  
**预测冠军：fnatic**　｜　实际冠军：NiP ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | fnatic vs Natus Vincere | fnatic | 63% | fnatic 2-1 | ✅ |
| R1M2 | Epsilon vs Dignitas | Dignitas | 63% | Dignitas 0-2 | ✅ |
| R1M3 | LDLC vs Virtus.pro | Virtus.pro | 57% | LDLC 2-0 | ❌ |
| R1M4 | Cloud9 vs NiP | NiP | 87% | NiP 1-2 | ✅ |
| R2M1 | fnatic vs Dignitas | fnatic | 63% | fnatic 2-0 | ✅ |
| R2M2 | LDLC vs NiP | LDLC | 55% | NiP 1-2 | ❌ |
| R3M1 | fnatic vs NiP | fnatic | 69% | NiP 1-2 | ❌ |

**赛前观点（8 强）：**

- **fnatic vs Natus Vincere**：我看好 fnatic（系列赛胜率 63%，最可能比分 fnatic 2:0）。 理由：近期状态：fnatic 最近 9胜1负（状态火热），Natus Vincere 最近 5胜5负（状态一般）；综合实力分 fnatic 比 Natus Vincere 高约 54 分。 总结：有一定爆冷可能。
- **Epsilon vs Dignitas**：我看好 Dignitas（系列赛胜率 63%，最可能比分 Dignitas 2:0）。 理由：老牌队伍经验更足：Epsilon 打过 49 局，Dignitas 打过 95 局；近期状态：Epsilon 最近 6胜4负（状态不错），Dignitas 最近 7胜3负（状态不错）；从长期战绩算出来的实力分看，Dignitas 领先 Epsilon 约 62 分。 总结：有一定爆冷可能。
- **LDLC vs Virtus.pro**：我看好 Virtus.pro（系列赛胜率 57%，最可能比分 Virtus.pro 2:0）。 理由：Virtus.pro 的职业比赛经验更多（LDLC 101 局 / Virtus.pro 145 局）；综合实力分 Virtus.pro 比 LDLC 高约 56 分。 总结：基本五五开，谁赢都不奇怪。
- **Cloud9 vs NiP**：倾向 NiP（系列赛胜率 87%，最可能比分 NiP 2:0）。 理由：NiP 的职业比赛经验更多（Cloud9 2 局 / NiP 165 局）；从长期战绩算出来的实力分看，NiP 领先 Cloud9 约 108 分。 不过要注意：近期状态：Cloud9 最近 2胜0负（状态火热），NiP 最近 3胜7负（状态低迷）。 总结：爆冷概率很低。

### DreamHack Winter 2014

训练数据截止：2014-11-27（之后的比赛模型都没见过）  
夺冠概率：Virtus.pro 22%，NiP 21%，fnatic 13%，HellRaisers 13%  
**预测冠军：NiP**　｜　实际冠军：LDLC ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | HellRaisers vs NiP | NiP | 57% | NiP 0-2 | ✅ |
| R1M2 | Virtus.pro vs PENTA | Virtus.pro | 82% | Virtus.pro 2-0 | ✅ |
| R1M3 | LDLC vs fnatic | fnatic | 51% | LDLC 2-1 | ❌ |
| R1M4 | Dignitas vs Natus Vincere | Natus Vincere | 54% | Natus Vincere 0-2 | ✅ |
| R2M1 | NiP vs Virtus.pro | NiP | 55% | NiP 2-1 | ✅ |
| R2M2 | LDLC vs Natus Vincere | LDLC | 54% | LDLC 2-0 | ✅ |
| R3M1 | NiP vs LDLC | NiP | 59% | LDLC 1-2 | ❌ |

**赛前观点（8 强）：**

- **HellRaisers vs NiP**：我的判断：NiP 晋级（系列赛胜率 57%，最可能比分 NiP 2:0）。 主要依据：老牌队伍经验更足：HellRaisers 打过 176 局，NiP 打过 231 局；NiP 整体硬实力更强（实力分高 45）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs PENTA**：倾向 Virtus.pro（系列赛胜率 82%，最可能比分 Virtus.pro 2:0）。 为什么：Virtus.pro 的职业比赛经验更多（Virtus.pro 256 局 / PENTA 42 局）；近期状态：Virtus.pro 最近 8胜2负（状态火热），PENTA 最近 6胜4负（状态不错）；Virtus.pro 整体硬实力更强（实力分高 104）。 总结：爆冷概率很低。
- **LDLC vs fnatic**：我看好 fnatic（系列赛胜率 51%，最可能比分 fnatic 2:0）。 为什么：fnatic 整体硬实力更强（实力分高 98）；老牌队伍经验更足：LDLC 打过 197 局，fnatic 打过 253 局。 不过要注意：近期状态：LDLC 最近 6胜4负（状态不错），fnatic 最近 7胜3负（状态不错）。 总结：基本五五开，谁赢都不奇怪。
- **Dignitas vs Natus Vincere**：倾向 Natus Vincere（系列赛胜率 54%，最可能比分 Natus Vincere 2:0）。 为什么：老牌队伍经验更足：Dignitas 打过 159 局，Natus Vincere 打过 223 局；近期状态：Dignitas 最近 6胜4负（状态不错），Natus Vincere 最近 6胜4负（状态不错）。 风险点：Dignitas 整体硬实力更强（实力分高 55）。 总结：基本五五开，谁赢都不奇怪。

### ESL One Katowice 2015

训练数据截止：2015-03-12（之后的比赛模型都没见过）  
夺冠概率：Virtus.pro 33%，NiP 27%，fnatic 25%，Natus Vincere 8%  
**预测冠军：fnatic**　｜　实际冠军：fnatic ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | fnatic vs PENTA | fnatic | 79% | fnatic 2-0 | ✅ |
| R1M2 | Virtus.pro vs Keyd | Virtus.pro | 98% | Virtus.pro 2-1 | ✅ |
| R1M3 | Envy vs Natus Vincere | Natus Vincere | 63% | Envy 2-1 | ❌ |
| R1M4 | NiP vs TSM | NiP | 78% | NiP 2-1 | ✅ |
| R2M1 | fnatic vs Virtus.pro | fnatic | 51% | fnatic 2-0 | ✅ |
| R2M2 | Envy vs NiP | NiP | 78% | NiP 0-2 | ✅ |
| R3M1 | fnatic vs NiP | fnatic | 52% | fnatic 2-1 | ✅ |

**赛前观点（8 强）：**

- **fnatic vs PENTA**：倾向 fnatic（系列赛胜率 79%，最可能比分 fnatic 2:0）。 主要依据：综合实力分 fnatic 比 PENTA 高约 183 分；老牌队伍经验更足：fnatic 打过 328 局，PENTA 打过 127 局；fnatic 最近手感比对手好（fnatic 6-4，PENTA 2-8，比赛结果都好于赛前预期）。 总结：有一定爆冷可能。
- **Virtus.pro vs Keyd**：倾向 Virtus.pro（系列赛胜率 98%，最可能比分 Virtus.pro 2:0）。 主要依据：Virtus.pro 的职业比赛经验更多（Virtus.pro 349 局 / Keyd 0 局）；综合实力分 Virtus.pro 比 Keyd 高约 144 分；Virtus.pro 最近手感比对手好（Virtus.pro 7-3，Keyd 0-0，比赛结果都好于赛前预期）。 总结：爆冷概率很低。
- **Envy vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 63%，最可能比分 Natus Vincere 2:0）。 理由：Natus Vincere 的职业比赛经验更多（Envy 42 局 / Natus Vincere 269 局）；Natus Vincere 整体硬实力更强（实力分高 91）。 但是：近期状态：Envy 最近 6胜4负（状态不错），Natus Vincere 最近 2胜8负（状态低迷）。 总结：有一定爆冷可能。
- **NiP vs TSM**：倾向 NiP（系列赛胜率 78%，最可能比分 NiP 2:0）。 为什么：老牌队伍经验更足：NiP 打过 282 局，TSM 打过 23 局；从长期战绩算出来的实力分看，NiP 领先 TSM 约 111 分。 风险点：近期状态：NiP 最近 7胜3负（状态不错），TSM 最近 7胜3负（状态不错）。 总结：有一定爆冷可能。

### ESL One Cologne 2015

训练数据截止：2015-08-20（之后的比赛模型都没见过）  
夺冠概率：NiP 18%，Natus Vincere 17%，Envy 16%，Virtus.pro 16%  
**预测冠军：NiP**　｜　实际冠军：fnatic ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Envy vs Natus Vincere | Natus Vincere | 51% | Envy 2-0 | ❌ |
| R1M2 | TSM vs Kinguin | TSM | 66% | TSM 2-0 | ✅ |
| R1M3 | Virtus.pro vs NiP | NiP | 52% | Virtus.pro 2-0 | ❌ |
| R1M4 | fnatic vs Luminosity | fnatic | 67% | fnatic 2-0 | ✅ |
| R2M1 | Envy vs TSM | Envy | 55% | Envy 2-1 | ✅ |
| R2M2 | Virtus.pro vs fnatic | Virtus.pro | 56% | fnatic 1-2 | ❌ |
| R3M1 | Envy vs fnatic | Envy | 56% | fnatic 0-2 | ❌ |

**赛前观点（8 强）：**

- **Envy vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 51%，最可能比分 Natus Vincere 2:0）。 理由：Natus Vincere 的职业比赛经验更多（Envy 230 局 / Natus Vincere 485 局）。 但是：近期状态：Envy 最近 8胜2负（状态火热），Natus Vincere 最近 6胜4负（状态不错）。 总结：基本五五开，谁赢都不奇怪。
- **TSM vs Kinguin**：倾向 TSM（系列赛胜率 66%，最可能比分 TSM 2:0）。 为什么：老牌队伍经验更足：TSM 打过 233 局，Kinguin 打过 73 局；从长期战绩算出来的实力分看，TSM 领先 Kinguin 约 54 分；TSM 最近手感比对手好（TSM 5-5，Kinguin 6-4，比赛结果都好于赛前预期）。 总结：有一定爆冷可能。
- **Virtus.pro vs NiP**：倾向 NiP（系列赛胜率 52%，最可能比分 NiP 2:0）。 为什么：NiP 最近手感比对手好（Virtus.pro 5-5，NiP 7-3，比赛结果都好于赛前预期）。 但是：Virtus.pro 的职业比赛经验更多（Virtus.pro 555 局 / NiP 426 局）。 总结：基本五五开，谁赢都不奇怪。
- **fnatic vs Luminosity**：我看好 fnatic（系列赛胜率 67%，最可能比分 fnatic 2:0）。 为什么：老牌队伍经验更足：fnatic 打过 502 局，Luminosity 打过 118 局；从长期战绩算出来的实力分看，fnatic 领先 Luminosity 约 153 分。 风险点：Luminosity 最近手感比对手好（fnatic 4-6，Luminosity 4-6，比赛结果都好于赛前预期）。 总结：有一定爆冷可能。

### DreamHack Open Cluj-Napoca 2015

训练数据截止：2015-10-28（之后的比赛模型都没见过）  
夺冠概率：NiP 18%，Virtus.pro 17%，TSM 14%，fnatic 13%  
**预测冠军：NiP**　｜　实际冠军：Envy ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Envy vs fnatic | fnatic | 57% | Envy 2-1 | ❌ |
| R1M2 | Virtus.pro vs G2 | Virtus.pro | 54% | G2 0-2 | ❌ |
| R1M3 | TSM vs NiP | NiP | 54% | NiP 0-2 | ✅ |
| R1M4 | Luminosity vs Natus Vincere | Natus Vincere | 51% | Natus Vincere 0-2 | ✅ |
| R2M1 | Envy vs G2 | G2 | 58% | Envy 2-1 | ❌ |
| R2M2 | NiP vs Natus Vincere | NiP | 59% | Natus Vincere 0-2 | ❌ |
| R3M1 | Envy vs Natus Vincere | Natus Vincere | 55% | Envy 2-0 | ❌ |

**赛前观点（8 强）：**

- **Envy vs fnatic**：倾向 fnatic（系列赛胜率 57%，最可能比分 fnatic 2:0）。 理由：老牌队伍经验更足：Envy 打过 283 局，fnatic 打过 569 局；从长期战绩算出来的实力分看，fnatic 领先 Envy 约 30 分。 不过要注意：近期状态：Envy 最近 4胜6负（状态一般），fnatic 最近 4胜6负（状态一般）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs G2**：我的判断：Virtus.pro 晋级（系列赛胜率 54%，最可能比分 Virtus.pro 2:0）。 为什么：老牌队伍经验更足：Virtus.pro 打过 637 局，G2 打过 251 局；Virtus.pro 整体硬实力更强（实力分高 34）。 风险点：G2 最近手感比对手好（Virtus.pro 6-4，G2 6-4，比赛结果都好于赛前预期）。 总结：基本五五开，谁赢都不奇怪。
- **TSM vs NiP**：我看好 NiP（系列赛胜率 54%，最可能比分 NiP 2:0）。 主要依据：NiP 的职业比赛经验更多（TSM 322 局 / NiP 469 局）；NiP 整体硬实力更强（实力分高 33）。 不过要注意：TSM 最近手感比对手好（TSM 6-4，NiP 7-3，比赛结果都好于赛前预期）。 总结：基本五五开，谁赢都不奇怪。
- **Luminosity vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 51%，最可能比分 Natus Vincere 2:0）。 理由：老牌队伍经验更足：Luminosity 打过 197 局，Natus Vincere 打过 545 局；Natus Vincere 整体硬实力更强（实力分高 80）。 风险点：近期状态：Luminosity 最近 7胜3负（状态不错），Natus Vincere 最近 4胜6负（状态一般）。 总结：基本五五开，谁赢都不奇怪。

### MLG Columbus 2016

训练数据截止：2016-03-29（之后的比赛模型都没见过）  
夺冠概率：fnatic 31%，Luminosity 27%，Natus Vincere 17%，NiP 17%  
**预测冠军：fnatic**　｜　实际冠军：Luminosity ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs NiP | Natus Vincere | 50% | Natus Vincere 2-0 | ✅ |
| R1M2 | Astralis vs fnatic | fnatic | 80% | Astralis 2-0 | ❌ |
| R1M3 | Liquid vs CLG | Liquid | 70% | Liquid 2-0 | ✅ |
| R1M4 | Luminosity vs Virtus.pro | Luminosity | 91% | Luminosity 2-1 | ✅ |
| R2M1 | Natus Vincere vs Astralis | Natus Vincere | 76% | Natus Vincere 2-0 | ✅ |
| R2M2 | Liquid vs Luminosity | Luminosity | 69% | Luminosity 0-2 | ✅ |
| R3M1 | Natus Vincere vs Luminosity | Natus Vincere | 59% | Luminosity 0-2 | ❌ |

**赛前观点（8 强）：**

- **Natus Vincere vs NiP**：倾向 Natus Vincere（系列赛胜率 50%，最可能比分 Natus Vincere 0:2）。 为什么：Natus Vincere 选手们对线期 KDA 压制更明显；老牌队伍经验更足：Natus Vincere 打过 632 局，NiP 打过 515 局。 但是：近期状态：Natus Vincere 最近 8胜2负（状态火热），NiP 最近 9胜1负（状态火热）。 位置对比：打野 guardian 近期表现优于 xizt；中单 f0rest 近期表现优于 zeus；辅助 seized 近期表现优于 pyth。 地图BP推演：Natus Vincere禁Cache，NiP禁Train；Natus Vincere选Cobblestone（Natus Vincere胜率51%），NiP选Mirage（Natus Vincere胜率49%）；决胜图 Inferno（Natus Vincere胜率50%）。 总结：基本五五开，谁赢都不奇怪。
- **Astralis vs fnatic**：我的判断：fnatic 晋级（系列赛胜率 80%，最可能比分 fnatic 2:0）。 主要依据：fnatic 的职业比赛经验更多（Astralis 58 局 / fnatic 662 局）；fnatic 整体硬实力更强（实力分高 147）；fnatic 选手们对线期 KDA 压制更明显。 位置对比：辅助 olofmeister 近期表现优于 karrigan；下路 flusha 近期表现优于 dupreeh；中单 device 近期表现优于 dennis。 地图BP推演：Astralis禁Inferno，fnatic禁Mirage；Astralis选Train（Astralis胜率30%），fnatic选Dust2（Astralis胜率28%）；决胜图 Cache（Astralis胜率29%）。 总结：有一定爆冷可能。
- **Liquid vs CLG**：倾向 Liquid（系列赛胜率 70%，最可能比分 Liquid 2:0）。 主要依据：Liquid 选手们对线期 KDA 压制更明显；综合实力分 Liquid 比 CLG 高约 30 分；近期状态：Liquid 最近 7胜3负（状态不错），CLG 最近 4胜6负（状态一般）。 位置对比：下路 nitr0 近期表现优于 reltuc；上单 elige 近期表现优于 fugly；辅助 s1mple 近期表现优于 tarik。 地图BP推演：Liquid禁Overpass，CLG禁Cache；Liquid选Cobblestone（Liquid胜率64%），CLG选Train（Liquid胜率63%）；决胜图 Mirage（Liquid胜率64%）。 总结：有一定爆冷可能。
- **Luminosity vs Virtus.pro**：我看好 Luminosity（系列赛胜率 91%，最可能比分 Luminosity 2:0）。 为什么：Luminosity 选手们对线期 KDA 压制更明显；综合实力分 Luminosity 比 Virtus.pro 高约 144 分；近期状态：Luminosity 最近 8胜2负（状态火热），Virtus.pro 最近 3胜7负（状态低迷）。 风险点：老牌队伍经验更足：Luminosity 打过 300 局，Virtus.pro 打过 707 局。 位置对比：下路 fer 近期表现优于 byali；辅助 fnx 近期表现优于 pashabiceps；中单 coldzera 近期表现优于 taz。 地图BP推演：Luminosity禁Dust2，Virtus.pro禁Overpass；Luminosity选Train（Luminosity胜率82%），Virtus.pro选Cache（Luminosity胜率80%）；决胜图 Inferno（Luminosity胜率81%）。 总结：爆冷概率很低。

### ESL One Cologne 2016

训练数据截止：2016-07-05（之后的比赛模型都没见过）  
夺冠概率：Natus Vincere 34%，fnatic 27%，Virtus.pro 12%，Astralis 9%  
**预测冠军：Natus Vincere**　｜　实际冠军：SK ❌  
预测 4 强命中 3/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Virtus.pro vs Astralis | Virtus.pro | 53% | Virtus.pro 2-0 | ✅ |
| R1M2 | SK vs FlipSid3 | SK | 57% | SK 2-0 | ✅ |
| R1M3 | Natus Vincere vs Liquid | Natus Vincere | 72% | Liquid 1-2 | ❌ |
| R1M4 | Gambit vs fnatic | fnatic | 84% | fnatic 0-2 | ✅ |
| R2M1 | Virtus.pro vs SK | Virtus.pro | 59% | SK 1-2 | ❌ |
| R2M2 | Liquid vs fnatic | fnatic | 65% | Liquid 2-0 | ❌ |
| R3M1 | SK vs Liquid | Liquid | 56% | SK 2-0 | ❌ |

**赛前观点（8 强）：**

- **Virtus.pro vs Astralis**：倾向 Virtus.pro（系列赛胜率 53%，最可能比分 Virtus.pro 2:0）。 为什么：老牌队伍经验更足：Virtus.pro 打过 774 局，Astralis 打过 107 局；Virtus.pro 最近手感比对手好（Virtus.pro 6-4，Astralis 4-6，比赛结果都好于赛前预期）。 风险点：Astralis 整体硬实力更强（实力分高 73）。 位置对比：中单 device 近期表现优于 taz；上单 kjaerbye 近期表现优于 neo；打野 snax 近期表现优于 xyp9x。 地图BP推演：Virtus.pro禁Cache，Astralis禁Cobblestone；Virtus.pro选Train（Virtus.pro胜率53%），Astralis选Overpass（Virtus.pro胜率50%）；决胜图 Dust2（Virtus.pro胜率53%）。 总结：基本五五开，谁赢都不奇怪。
- **SK vs FlipSid3**：我看好 SK（系列赛胜率 57%，最可能比分 SK 2:0）。 为什么：SK 选手们对线期 KDA 压制更明显；从长期战绩算出来的实力分看，SK 领先 FlipSid3 约 29 分。 但是：FlipSid3 的职业比赛经验更多（SK 328 局 / FlipSid3 491 局）。 位置对比：打野 friis 近期表现优于 shara；下路 gla1ve 近期表现优于 markeloff；中单 worldedit 近期表现优于 moddii。 地图BP推演：SK禁Mirage，FlipSid3禁Inferno；SK选Train（SK胜率58%），FlipSid3选Overpass（SK胜率53%）；决胜图 Cobblestone（SK胜率54%）。 总结：基本五五开，谁赢都不奇怪。
- **Natus Vincere vs Liquid**：我看好 Natus Vincere（系列赛胜率 72%，最可能比分 Natus Vincere 2:0）。 为什么：Natus Vincere 选手们对线期 KDA 压制更明显；综合实力分 Natus Vincere 比 Liquid 高约 134 分；Natus Vincere 的职业比赛经验更多（Natus Vincere 675 局 / Liquid 391 局）。 但是：Liquid 这批首发最近赢得更多。 位置对比：上单 edward 近期表现优于 elige；打野 guardian 近期表现优于 hiko；下路 flamie 近期表现优于 nitr0。 地图BP推演：Natus Vincere禁Cache，Liquid禁Overpass；Natus Vincere选Train（Natus Vincere胜率67%），Liquid选Cobblestone（Natus Vincere胜率64%）；决胜图 Mirage（Natus Vincere胜率65%）。 总结：有一定爆冷可能。
- **Gambit vs fnatic**：倾向 fnatic（系列赛胜率 84%，最可能比分 fnatic 2:0）。 理由：综合实力分 fnatic 比 Gambit 高约 236 分；fnatic 的职业比赛经验更多（Gambit 89 局 / fnatic 713 局）；fnatic 选手们对线期 KDA 压制更明显。 但是：Gambit 这批首发最近赢得更多。 位置对比：辅助 olofmeister 近期表现优于 spaze；中单 dennis 近期表现优于 hooch；上单 adren 近期表现优于 jw。 地图BP推演：Gambit禁Dust2，fnatic禁Train；Gambit选Mirage（Gambit胜率27%），fnatic选Cache（Gambit胜率24%）；决胜图 Cobblestone（Gambit胜率26%）。 总结：爆冷概率很低。

### ELEAGUE Major 2017

训练数据截止：2017-01-22（之后的比赛模型都没见过）  
夺冠概率：Astralis 50%，Virtus.pro 27%，SK 7%，Gambit 5%  
**预测冠军：Astralis**　｜　实际冠军：Astralis ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs Astralis | Astralis | 84% | Astralis 1-2 | ✅ |
| R1M2 | fnatic vs Gambit | Gambit | 55% | fnatic 2-1 | ❌ |
| R1M3 | Virtus.pro vs North | Virtus.pro | 97% | Virtus.pro 2-1 | ✅ |
| R1M4 | FaZe vs SK | SK | 55% | SK 1-2 | ✅ |
| R2M1 | Astralis vs fnatic | Astralis | 84% | Astralis 2-0 | ✅ |
| R2M2 | Virtus.pro vs SK | Virtus.pro | 64% | Virtus.pro 2-0 | ✅ |
| R3M1 | Astralis vs Virtus.pro | Astralis | 69% | Astralis 2-1 | ✅ |

**赛前观点（8 强）：**

- **Natus Vincere vs Astralis**：我看好 Astralis（系列赛胜率 84%，最可能比分 Astralis 2:0）。 为什么：Astralis 选手们对线期 KDA 压制更明显；从长期战绩算出来的实力分看，Astralis 领先 Natus Vincere 约 139 分；Astralis 最近手感比对手好（Natus Vincere 4-6，Astralis 8-2，比赛结果都好于赛前预期）。 不过要注意：老牌队伍经验更足：Natus Vincere 打过 743 局，Astralis 打过 215 局。 位置对比：中单 device 近期表现优于 flamie；上单 kjaerbye 近期表现优于 edward；打野 xyp9x 近期表现优于 guardian。 地图BP推演：Natus Vincere禁Mirage，Astralis禁Overpass；Natus Vincere选Cobblestone（Natus Vincere胜率27%），Astralis选Dust2（Natus Vincere胜率24%）；决胜图 Train（Natus Vincere胜率25%）。 总结：爆冷概率很低。
- **fnatic vs Gambit**：我的判断：Gambit 晋级（系列赛胜率 55%，最可能比分 Gambit 2:0）。 为什么：Gambit 选手们对线期 KDA 压制更明显；Gambit 最近手感比对手好（fnatic 4-6，Gambit 8-2，比赛结果都好于赛前预期）。 风险点：老牌队伍经验更足：fnatic 打过 785 局，Gambit 打过 196 局。 位置对比：中单 hobbit 近期表现优于 disco doplan；辅助 mou 近期表现优于 twist；上单 adren 近期表现优于 krimz。 地图BP推演：fnatic禁Cobblestone，Gambit禁Cache；fnatic选Nuke（fnatic胜率48%），Gambit选Dust2（fnatic胜率45%）；决胜图 Mirage（fnatic胜率46%）。 总结：基本五五开，谁赢都不奇怪。
- **Virtus.pro vs North**：我看好 Virtus.pro（系列赛胜率 97%，最可能比分 Virtus.pro 2:0）。 主要依据：Virtus.pro 的职业比赛经验更多（Virtus.pro 895 局 / North 0 局）；Virtus.pro 整体硬实力更强（实力分高 239）；近期状态：Virtus.pro 最近 8胜2负（状态火热），North 最近 0胜0负（暂无近期数据）。 地图BP推演：Virtus.pro禁Cache，North禁Cobblestone；Virtus.pro选Mirage（Virtus.pro胜率90%），North选Train（Virtus.pro胜率88%）；决胜图 Dust2（Virtus.pro胜率89%）。 总结：爆冷概率很低。
- **FaZe vs SK**：倾向 SK（系列赛胜率 55%，最可能比分 SK 2:0）。 为什么：老牌队伍经验更足：FaZe 打过 202 局，SK 打过 452 局；SK 选手们对线期 KDA 压制更明显；SK 这批首发最近赢得更多。 不过要注意：FaZe 最近手感比对手好（FaZe 8-2，SK 4-6，比赛结果都好于赛前预期）。 位置对比：中单 coldzera 近期表现优于 karrigan；辅助 rain 近期表现优于 fox；打野 allu 近期表现优于 taco。 地图BP推演：FaZe禁Train，SK禁Mirage；FaZe选Nuke（FaZe胜率49%），SK选Cobblestone（FaZe胜率46%）；决胜图 Cache（FaZe胜率46%）。 总结：基本五五开，谁赢都不奇怪。

### PGL Major Krakow 2017

训练数据截止：2017-07-16（之后的比赛模型都没见过）  
夺冠概率：SK 52%，BIG 13%，Astralis 12%，fnatic 7%  
**预测冠军：SK**　｜　实际冠军：Gambit ❌  
预测 4 强命中 0/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Gambit vs fnatic | fnatic | 59% | Gambit 2-0 | ❌ |
| R1M2 | SK vs Astralis | SK | 72% | Astralis 0-2 | ❌ |
| R1M3 | BIG vs Immortals | BIG | 62% | Immortals 1-2 | ❌ |
| R1M4 | North vs Virtus.pro | North | 69% | Virtus.pro 0-2 | ❌ |
| R2M1 | Gambit vs Astralis | Astralis | 73% | Gambit 2-1 | ❌ |
| R2M2 | Immortals vs Virtus.pro | Immortals | 69% | Immortals 2-0 | ✅ |
| R3M1 | Gambit vs Immortals | Immortals | 53% | Gambit 2-1 | ❌ |

**赛前观点（8 强）：**

- **Gambit vs fnatic**：倾向 fnatic（系列赛胜率 59%，最可能比分 fnatic 2:0）。 理由：综合实力分 fnatic 比 Gambit 高约 84 分；fnatic 的职业比赛经验更多（Gambit 269 局 / fnatic 888 局）。 不过要注意：Gambit 选手们对线期 KDA 压制更明显。 位置对比：辅助 mou 近期表现优于 olofmeister；下路 zeus 近期表现优于 flusha；中单 hobbit 近期表现优于 dennis。 地图BP推演：Gambit禁Cache，fnatic禁Train；Gambit选Cobblestone（Gambit胜率48%），fnatic选Inferno（Gambit胜率42%）；决胜图 Nuke（Gambit胜率44%）。 总结：基本五五开，谁赢都不奇怪。
- **SK vs Astralis**：倾向 SK（系列赛胜率 72%，最可能比分 SK 2:0）。 主要依据：综合实力分 SK 比 Astralis 高约 78 分；SK 最近手感比对手好（SK 8-2，Astralis 6-4，比赛结果都好于赛前预期）；老牌队伍经验更足：SK 打过 577 局，Astralis 打过 310 局。 但是：Astralis 这批首发最近赢得更多。 位置对比：辅助 fer 近期表现优于 gla1ve；打野 xyp9x 近期表现优于 taco；上单 fallen 近期表现优于 kjaerbye。 地图BP推演：SK禁Mirage，Astralis禁Cobblestone；SK选Cache（SK胜率68%），Astralis选Overpass（SK胜率62%）；决胜图 Inferno（SK胜率66%）。 总结：有一定爆冷可能。
- **BIG vs Immortals**：我的判断：BIG 晋级（系列赛胜率 62%，最可能比分 BIG 2:0）。 为什么：BIG 最近手感比对手好（BIG 9-1，Immortals 4-6，比赛结果都好于赛前预期）；BIG 选手们对线期 KDA 压制更明显。 不过要注意：Immortals 的职业比赛经验更多（BIG 118 局 / Immortals 263 局）。 位置对比：辅助 tabsen 近期表现优于 steel；上单 hen1 近期表现优于 legija；打野 gob b 近期表现优于 lucas1。 地图BP推演：BIG禁Overpass，Immortals禁Train；BIG选Cache（BIG胜率61%），Immortals选Mirage（BIG胜率56%）；决胜图 Cobblestone（BIG胜率58%）。 总结：有一定爆冷可能。
- **North vs Virtus.pro**：倾向 North（系列赛胜率 69%，最可能比分 North 2:0）。 理由：从长期战绩算出来的实力分看，North 领先 Virtus.pro 约 145 分；North 选手们对线期 KDA 压制更明显。 但是：Virtus.pro 的职业比赛经验更多（North 87 局 / Virtus.pro 982 局）。 位置对比：中单 aizy 近期表现优于 taz；辅助 k0nfig 近期表现优于 pashabiceps；下路 cajunb 近期表现优于 byali。 地图BP推演：North禁Mirage，Virtus.pro禁Overpass；North选Inferno（North胜率65%），Virtus.pro选Train（North胜率61%）；决胜图 Cobblestone（North胜率63%）。 总结：有一定爆冷可能。

### ELEAGUE Major 2018

训练数据截止：2018-01-12（之后的比赛模型都没见过）  
夺冠概率：SK 33%，FaZe 20%，mousesports 19%，Natus Vincere 12%  
**预测冠军：SK**　｜　实际冠军：Cloud9 ❌  
预测 4 强命中 4/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | FaZe vs mousesports | FaZe | 50% | FaZe 2-0 | ✅ |
| R1M2 | Natus Vincere vs Quantum Bellator Fire | Natus Vincere | 88% | Natus Vincere 2-0 | ✅ |
| R1M3 | G2 vs Cloud9 | Cloud9 | 62% | Cloud9 0-2 | ✅ |
| R1M4 | SK vs fnatic | SK | 72% | SK 2-1 | ✅ |
| R2M1 | FaZe vs Natus Vincere | FaZe | 67% | FaZe 2-0 | ✅ |
| R2M2 | Cloud9 vs SK | SK | 72% | Cloud9 2-1 | ❌ |
| R3M1 | FaZe vs Cloud9 | FaZe | 68% | Cloud9 1-2 | ❌ |

**赛前观点（8 强）：**

- **FaZe vs mousesports**：倾向 FaZe（系列赛胜率 50%，最可能比分 FaZe 0:2）。 为什么：FaZe 整体硬实力更强（实力分高 63）；FaZe 这批首发最近赢得更多。 但是：mousesports 选手们对线期 KDA 压制更明显。 位置对比：下路 s1mple 近期表现优于 olofmeister；中单 ropz 近期表现优于 karrigan；上单 guardian 近期表现优于 styko。 地图BP推演：FaZe禁Cobblestone，mousesports禁Overpass；FaZe选Inferno（FaZe胜率54%），mousesports选Nuke（FaZe胜率47%）；决胜图 Train（FaZe胜率50%）。 总结：基本五五开，谁赢都不奇怪。
- **Natus Vincere vs Quantum Bellator Fire**：倾向 Natus Vincere（系列赛胜率 88%，最可能比分 Natus Vincere 2:0）。 理由：综合实力分 Natus Vincere 比 Quantum Bellator Fire 高约 189 分；Natus Vincere 选手们对线期 KDA 压制更明显；老牌队伍经验更足：Natus Vincere 打过 899 局，Quantum Bellator Fire 打过 171 局。 但是：Quantum Bellator Fire 这批首发最近赢得更多。 位置对比：辅助 s1mple 近期表现优于 waterfallz；中单 electronic 近期表现优于 balblna；打野 kvik 近期表现优于 zeus。 地图BP推演：Natus Vincere禁Mirage，Quantum Bellator Fire禁Overpass；Natus Vincere选Train（Natus Vincere胜率80%），Quantum Bellator Fire选Inferno（Natus Vincere胜率77%）；决胜图 Nuke（Natus Vincere胜率78%）。 总结：爆冷概率很低。
- **G2 vs Cloud9**：倾向 Cloud9（系列赛胜率 62%，最可能比分 Cloud9 2:0）。 理由：Cloud9 选手们对线期 KDA 压制更明显；Cloud9 整体硬实力更强（实力分高 41）。 但是：G2 这批首发最近赢得更多。 位置对比：辅助 tarik 近期表现优于 shox；打野 skadoodle 近期表现优于 apex；下路 kennys 近期表现优于 autimatic。 地图BP推演：G2禁Train，Cloud9禁Nuke；G2选Inferno（G2胜率43%），Cloud9选Overpass（G2胜率41%）；决胜图 Cobblestone（G2胜率41%）。 总结：有一定爆冷可能。
- **SK vs fnatic**：我的判断：SK 晋级（系列赛胜率 72%，最可能比分 SK 2:0）。 主要依据：从长期战绩算出来的实力分看，SK 领先 fnatic 约 82 分；SK 选手们对线期 KDA 压制更明显；近期状态：SK 最近 8胜2负（状态火热），fnatic 最近 5胜5负（状态一般）。 但是：fnatic 这批首发最近赢得更多。 位置对比：上单 fallen 近期表现优于 golden；下路 coldzera 近期表现优于 lekr0；辅助 flusha 近期表现优于 fer。 地图BP推演：SK禁Inferno，fnatic禁Overpass；SK选Cobblestone（SK胜率68%），fnatic选Nuke（SK胜率62%）；决胜图 Mirage（SK胜率66%）。 总结：有一定爆冷可能。

### FACEIT Major 2018

训练数据截止：2018-09-05（之后的比赛模型都没见过）  
夺冠概率：Astralis 54%，Natus Vincere 17%，Liquid 10%，Complexity 7%  
**预测冠军：Astralis**　｜　实际冠军：Astralis ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Complexity vs MIBR | Complexity | 62% | MIBR 0-2 | ❌ |
| R1M2 | BIG vs Natus Vincere | Natus Vincere | 72% | Natus Vincere 0-2 | ✅ |
| R1M3 | Liquid vs HellRaisers | Liquid | 67% | Liquid 2-1 | ✅ |
| R1M4 | Astralis vs FaZe | Astralis | 80% | Astralis 2-0 | ✅ |
| R2M1 | MIBR vs Natus Vincere | Natus Vincere | 73% | Natus Vincere 0-2 | ✅ |
| R2M2 | Liquid vs Astralis | Astralis | 79% | Astralis 0-2 | ✅ |
| R3M1 | Natus Vincere vs Astralis | Astralis | 76% | Astralis 0-2 | ✅ |

**赛前观点（8 强）：**

- **Complexity vs MIBR**：我看好 Complexity（系列赛胜率 62%，最可能比分 Complexity 2:0）。 理由：老牌队伍经验更足：Complexity 打过 594 局，MIBR 打过 27 局；从长期战绩算出来的实力分看，Complexity 领先 MIBR 约 32 分；Complexity 选手们对线期 KDA 压制更明显。 但是：近期状态：Complexity 最近 6胜4负（状态不错），MIBR 最近 8胜2负（状态火热）。 位置对比：中单 coldzera 近期表现优于 dephh；辅助 yay 近期表现优于 tarik；打野 shahzam 近期表现优于 stewie2k。 地图BP推演：Complexity禁Overpass，MIBR禁Mirage；Complexity选Cache（Complexity胜率60%），MIBR选Dust2（Complexity胜率56%）；决胜图 Inferno（Complexity胜率58%）。 总结：有一定爆冷可能。
- **BIG vs Natus Vincere**：我看好 Natus Vincere（系列赛胜率 72%，最可能比分 Natus Vincere 2:0）。 为什么：Natus Vincere 整体硬实力更强（实力分高 133）；老牌队伍经验更足：BIG 打过 304 局，Natus Vincere 打过 1053 局；Natus Vincere 选手们对线期 KDA 压制更明显。 风险点：BIG 最近手感比对手好（BIG 6-4，Natus Vincere 4-6，比赛结果都好于赛前预期）。 位置对比：辅助 s1mple 近期表现优于 tizian；打野 nex 近期表现优于 zeus；中单 electronic 近期表现优于 smooya。 地图BP推演：BIG禁Train，Natus Vincere禁Dust2；BIG选Cache（BIG胜率37%），Natus Vincere选Mirage（BIG胜率31%）；决胜图 Nuke（BIG胜率36%）。 总结：有一定爆冷可能。
- **Liquid vs HellRaisers**：我的判断：Liquid 晋级（系列赛胜率 67%，最可能比分 Liquid 2:0）。 为什么：从长期战绩算出来的实力分看，Liquid 领先 HellRaisers 约 96 分；Liquid 最近手感比对手好（Liquid 6-4，HellRaisers 2-8，比赛结果都好于赛前预期）；Liquid 这批首发最近赢得更多。 不过要注意：HellRaisers 选手们对线期 KDA 压制更明显。 位置对比：辅助 woxic 近期表现优于 nitr0；中单 issaa 近期表现优于 taco；打野 naf 近期表现优于 deadfox。 地图BP推演：Liquid禁Nuke，HellRaisers禁Inferno；Liquid选Mirage（Liquid胜率63%），HellRaisers选Overpass（Liquid胜率60%）；决胜图 Dust2（Liquid胜率62%）。 总结：有一定爆冷可能。
- **Astralis vs FaZe**：我看好 Astralis（系列赛胜率 80%，最可能比分 Astralis 2:0）。 主要依据：从长期战绩算出来的实力分看，Astralis 领先 FaZe 约 143 分；Astralis 选手们对线期 KDA 压制更明显。 风险点：FaZe 这批首发最近赢得更多。 位置对比：中单 device 近期表现优于 karrigan；辅助 gla1ve 近期表现优于 rain；下路 dupreeh 近期表现优于 olofmeister。 地图BP推演：Astralis禁Cache，FaZe禁Nuke；Astralis选Train（Astralis胜率73%），FaZe选Mirage（Astralis胜率70%）；决胜图 Inferno（Astralis胜率72%）。 总结：爆冷概率很低。

### IEM Katowice 2019

训练数据截止：2019-02-13（之后的比赛模型都没见过）  
夺冠概率：Astralis 46%，Liquid 23%，ENCE 10%，Renegades 6%  
**预测冠军：Astralis**　｜　实际冠军：Astralis ✅  
预测 4 强命中 2/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs FaZe | Natus Vincere | 53% | Natus Vincere 2-0 | ✅ |
| R1M2 | Liquid vs ENCE | Liquid | 62% | ENCE 0-2 | ❌ |
| R1M3 | MIBR vs Renegades | Renegades | 53% | MIBR 2-0 | ❌ |
| R1M4 | Astralis vs NiP | Astralis | 81% | Astralis 2-0 | ✅ |
| R2M1 | Natus Vincere vs ENCE | ENCE | 66% | ENCE 1-2 | ✅ |
| R2M2 | MIBR vs Astralis | Astralis | 79% | Astralis 0-2 | ✅ |
| R3M1 | ENCE vs Astralis | Astralis | 74% | Astralis 0-2 | ✅ |

**赛前观点（8 强）：**

- **Natus Vincere vs FaZe**：倾向 Natus Vincere（系列赛胜率 53%，最可能比分 Natus Vincere 2:0）。 主要依据：综合实力分 Natus Vincere 比 FaZe 高约 52 分；老牌队伍经验更足：Natus Vincere 打过 1133 局，FaZe 打过 672 局。 但是：近期状态：Natus Vincere 最近 5胜5负（状态一般），FaZe 最近 6胜4负（状态不错）。 位置对比：辅助 s1mple 近期表现优于 rain；打野 guardian 近期表现优于 zeus；中单 niko 近期表现优于 electronic。 地图BP推演：Natus Vincere禁Inferno，FaZe禁Train；Natus Vincere选Mirage（Natus Vincere胜率55%），FaZe选Dust2（Natus Vincere胜率49%）；决胜图 Nuke（Natus Vincere胜率52%）。 总结：基本五五开，谁赢都不奇怪。
- **Liquid vs ENCE**：我的判断：Liquid 晋级（系列赛胜率 62%，最可能比分 Liquid 2:0）。 理由：从长期战绩算出来的实力分看，Liquid 领先 ENCE 约 59 分；Liquid 这批首发最近赢得更多；老牌队伍经验更足：Liquid 打过 988 局，ENCE 打过 434 局。 但是：ENCE 选手们对线期 KDA 压制更明显。 位置对比：中单 allu 近期表现优于 stewie2k；打野 naf 近期表现优于 aleksib；下路 sergej 近期表现优于 twistzz。 地图BP推演：Liquid禁Train，ENCE禁Inferno；Liquid选Cache（Liquid胜率60%），ENCE选Nuke（Liquid胜率56%）；决胜图 Mirage（Liquid胜率57%）。 总结：基本五五开，谁赢都不奇怪。
- **MIBR vs Renegades**：我看好 Renegades（系列赛胜率 53%，最可能比分 Renegades 2:0）。 主要依据：老牌队伍经验更足：MIBR 打过 118 局，Renegades 打过 685 局；Renegades 选手们对线期 KDA 压制更明显。 不过要注意：MIBR 整体硬实力更强（实力分高 23）。 位置对比：辅助 jks 近期表现优于 tarik；中单 coldzera 近期表现优于 liazz；打野 gratisfaction 近期表现优于 stewie2k。 地图BP推演：MIBR禁Cache，Renegades禁Overpass；MIBR选Mirage（MIBR胜率51%），Renegades选Nuke（MIBR胜率45%）；决胜图 Dust2（MIBR胜率49%）。 总结：基本五五开，谁赢都不奇怪。
- **Astralis vs NiP**：倾向 Astralis（系列赛胜率 81%，最可能比分 Astralis 2:0）。 为什么：从长期战绩算出来的实力分看，Astralis 领先 NiP 约 212 分；Astralis 选手们对线期 KDA 压制更明显。 不过要注意：NiP 这批首发最近赢得更多。 位置对比：上单 magisk 近期表现优于 get_right；打野 xyp9x 近期表现优于 lekr0；辅助 gla1ve 近期表现优于 f0rest。 地图BP推演：Astralis禁Train，NiP禁Inferno；Astralis选Nuke（Astralis胜率75%），NiP选Cache（Astralis胜率69%）；决胜图 Dust2（Astralis胜率73%）。 总结：爆冷概率很低。

### StarLadder Major Berlin 2019

训练数据截止：2019-08-23（之后的比赛模型都没见过）  
夺冠概率：Liquid 55%，Astralis 14%，ENCE 9%，Natus Vincere 9%  
**预测冠军：Liquid**　｜　实际冠军：Astralis ❌  
预测 4 强命中 0/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | ENCE vs Renegades | ENCE | 77% | Renegades 0-2 | ❌ |
| R1M2 | Vitality vs AVANGAR | Vitality | 68% | AVANGAR 1-2 | ❌ |
| R1M3 | NRG vs Natus Vincere | Natus Vincere | 60% | NRG 2-0 | ❌ |
| R1M4 | Astralis vs Liquid | Liquid | 72% | Astralis 2-0 | ❌ |
| R2M1 | Renegades vs AVANGAR | AVANGAR | 60% | AVANGAR 0-2 | ✅ |
| R2M2 | NRG vs Astralis | Astralis | 73% | Astralis 0-2 | ✅ |
| R3M1 | AVANGAR vs Astralis | Astralis | 86% | Astralis 0-2 | ✅ |

**赛前观点（8 强）：**

- **ENCE vs Renegades**：我的判断：ENCE 晋级（系列赛胜率 77%，最可能比分 ENCE 2:0）。 理由：ENCE 整体硬实力更强（实力分高 147）；ENCE 选手们对线期 KDA 压制更明显；近期状态：ENCE 最近 6胜4负（状态不错），Renegades 最近 1胜9负（状态低迷）。 但是：Renegades 这批首发最近赢得更多。 位置对比：中单 allu 近期表现优于 liazz；辅助 jks 近期表现优于 xseven；上单 aerial 近期表现优于 azr。 地图BP推演：ENCE禁Inferno，Renegades禁Train；ENCE选Overpass（ENCE胜率70%），Renegades选Vertigo（ENCE胜率68%）；决胜图 Mirage（ENCE胜率69%）。 总结：有一定爆冷可能。
- **Vitality vs AVANGAR**：倾向 Vitality（系列赛胜率 68%，最可能比分 Vitality 2:0）。 为什么：从长期战绩算出来的实力分看，Vitality 领先 AVANGAR 约 187 分；Vitality 这批首发最近赢得更多。 但是：AVANGAR 选手们对线期 KDA 压制更明显。 位置对比：打野 jame 近期表现优于 nbk-；辅助 qikert 近期表现优于 apex；中单 sanji 近期表现优于 rpk。 地图BP推演：Vitality禁Train，AVANGAR禁Overpass；Vitality选Dust2（Vitality胜率63%），AVANGAR选Mirage（Vitality胜率61%）；决胜图 Inferno（Vitality胜率63%）。 总结：有一定爆冷可能。
- **NRG vs Natus Vincere**：我看好 Natus Vincere（系列赛胜率 60%，最可能比分 Natus Vincere 2:0）。 主要依据：Natus Vincere 选手们对线期 KDA 压制更明显；老牌队伍经验更足：NRG 打过 710 局，Natus Vincere 打过 1192 局。 但是：NRG 最近手感比对手好（NRG 8-2，Natus Vincere 7-3，比赛结果都好于赛前预期）。 位置对比：辅助 s1mple 近期表现优于 tarik；中单 electronic 近期表现优于 ethan；打野 cerq 近期表现优于 zeus。 地图BP推演：NRG禁Mirage，Natus Vincere禁Dust2；NRG选Overpass（NRG胜率44%），Natus Vincere选Train（NRG胜率42%）；决胜图 Nuke（NRG胜率44%）。 总结：基本五五开，谁赢都不奇怪。
- **Astralis vs Liquid**：我看好 Liquid（系列赛胜率 72%，最可能比分 Liquid 2:0）。 理由：Liquid 整体硬实力更强（实力分高 99）；Liquid 选手们对线期 KDA 压制更明显；近期状态：Astralis 最近 7胜3负（状态不错），Liquid 最近 9胜1负（状态火热）。 风险点：Astralis 这批首发最近赢得更多。 位置对比：辅助 nitr0 近期表现优于 gla1ve；下路 twistzz 近期表现优于 dupreeh；打野 naf 近期表现优于 xyp9x。 地图BP推演：Astralis禁Overpass，Liquid禁Nuke；Astralis选Train（Astralis胜率35%），Liquid选Dust2（Astralis胜率34%）；决胜图 Mirage（Astralis胜率35%）。 总结：有一定爆冷可能。

### PGL Major Stockholm 2021

训练数据截止：2021-10-26（之后的比赛模型都没见过）  
夺冠概率：Gambit 26%，Natus Vincere 21%，Heroic 15%，NiP 13%  
**预测冠军：Natus Vincere**　｜　实际冠军：Natus Vincere ✅  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Natus Vincere vs Vitality | Natus Vincere | 59% | Natus Vincere 2-0 | ✅ |
| R1M2 | FURIA vs Gambit | Gambit | 77% | Gambit 0-2 | ✅ |
| R1M3 | Heroic vs Virtus.pro | Heroic | 60% | Heroic 2-1 | ✅ |
| R1M4 | NiP vs G2 | NiP | 60% | G2 0-2 | ❌ |
| R2M1 | Natus Vincere vs Gambit | Natus Vincere | 50% | Natus Vincere 2-0 | ✅ |
| R2M2 | Heroic vs G2 | Heroic | 62% | G2 1-2 | ❌ |
| R3M1 | Natus Vincere vs G2 | Natus Vincere | 71% | Natus Vincere 2-0 | ✅ |

**赛前观点（8 强）：**

- **Natus Vincere vs Vitality**：我的判断：Natus Vincere 晋级（系列赛胜率 59%，最可能比分 Natus Vincere 2:0）。 理由：从长期战绩算出来的实力分看，Natus Vincere 领先 Vitality 约 55 分；Natus Vincere 的职业比赛经验更多（Natus Vincere 1618 局 / Vitality 622 局）。 风险点：近期状态：Natus Vincere 最近 8胜2负（状态火热），Vitality 最近 7胜3负（状态不错）。 位置对比：打野 zywoo 近期表现优于 perfecto；辅助 s1mple 近期表现优于 shox；中单 b1t 近期表现优于 apex。 地图BP推演：Natus Vincere禁Overpass，Vitality禁Nuke；Natus Vincere选Mirage（Natus Vincere胜率59%），Vitality选Vertigo（Natus Vincere胜率53%）；决胜图 Ancient（Natus Vincere胜率56%）。 总结：基本五五开，谁赢都不奇怪。
- **FURIA vs Gambit**：倾向 Gambit（系列赛胜率 77%，最可能比分 Gambit 2:0）。 为什么：综合实力分 Gambit 比 FURIA 高约 146 分；Gambit 选手们对线期 KDA 压制更明显；Gambit 这批首发最近赢得更多。 风险点：FURIA 最近手感比对手好（FURIA 8-2，Gambit 8-2，比赛结果都好于赛前预期）。 位置对比：下路 nafany 近期表现优于 guerri；辅助 sh1ro 近期表现优于 yuurih；中单 art 近期表现优于 interz。 地图BP推演：FURIA禁Overpass，Gambit禁Inferno；FURIA选Ancient（FURIA胜率33%），Gambit选Vertigo（FURIA胜率29%）；决胜图 Mirage（FURIA胜率31%）。 总结：有一定爆冷可能。
- **Heroic vs Virtus.pro**：我的判断：Heroic 晋级（系列赛胜率 60%，最可能比分 Heroic 2:0）。 理由：从长期战绩算出来的实力分看，Heroic 领先 Virtus.pro 约 77 分；近期状态：Heroic 最近 6胜4负（状态不错），Virtus.pro 最近 4胜6负（状态一般）。 不过要注意：Virtus.pro 选手们对线期 KDA 压制更明显。 位置对比：上单 jame 近期表现优于 teses；中单 refrezh 近期表现优于 sanji；下路 yekindar 近期表现优于 sjuush。 地图BP推演：Heroic禁Inferno，Virtus.pro禁Overpass；Heroic选Vertigo（Heroic胜率58%），Virtus.pro选Dust2（Heroic胜率56%）；决胜图 Mirage（Heroic胜率57%）。 总结：基本五五开，谁赢都不奇怪。
- **NiP vs G2**：我看好 NiP（系列赛胜率 60%，最可能比分 NiP 2:0）。 理由：NiP 整体硬实力更强（实力分高 96）。 不过要注意：G2 这批首发最近赢得更多。 位置对比：下路 device 近期表现优于 hunter-；上单 amanek 近期表现优于 lnz。 地图BP推演：NiP禁Nuke，G2禁Overpass；NiP选Ancient（NiP胜率58%），G2选Mirage（NiP胜率56%）；决胜图 Vertigo（NiP胜率56%）。 总结：基本五五开，谁赢都不奇怪。

### PGL Major Antwerp 2022

训练数据截止：2022-05-09（之后的比赛模型都没见过）  
夺冠概率：Natus Vincere 32%，FaZe 25%，ENCE 13%，FURIA 12%  
**预测冠军：Natus Vincere**　｜　实际冠军：FaZe ❌  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs FURIA | FURIA | 73% | Spirit 2-0 | ❌ |
| R1M2 | FaZe vs NiP | FaZe | 70% | FaZe 2-1 | ✅ |
| R1M3 | ENCE vs Copenhagen Flames | ENCE | 70% | ENCE 2-0 | ✅ |
| R1M4 | Heroic vs Natus Vincere | Natus Vincere | 66% | Natus Vincere 1-2 | ✅ |
| R2M1 | Spirit vs FaZe | FaZe | 83% | FaZe 0-2 | ✅ |
| R2M2 | ENCE vs Natus Vincere | Natus Vincere | 69% | Natus Vincere 0-2 | ✅ |
| R3M1 | FaZe vs Natus Vincere | Natus Vincere | 59% | FaZe 2-0 | ❌ |

**赛前观点（8 强）：**

- **Spirit vs FURIA**：倾向 FURIA（系列赛胜率 73%，最可能比分 FURIA 2:0）。 主要依据：FURIA 选手们对线期 KDA 压制更明显；综合实力分 FURIA 比 Spirit 高约 84 分；近期状态：Spirit 最近 3胜7负（状态低迷），FURIA 最近 8胜2负（状态火热）。 风险点：Spirit 这批首发最近赢得更多。 位置对比：上单 kscerato 近期表现优于 patsi；辅助 yuurih 近期表现优于 s1ren；下路 saffee 近期表现优于 magixx。 地图BP推演：Spirit禁Vertigo，FURIA禁Dust2；Spirit选Overpass（Spirit胜率36%），FURIA选Inferno（Spirit胜率33%）；决胜图 Nuke（Spirit胜率34%）。 总结：有一定爆冷可能。
- **FaZe vs NiP**：倾向 FaZe（系列赛胜率 70%，最可能比分 FaZe 2:0）。 主要依据：综合实力分 FaZe 比 NiP 高约 109 分；FaZe 选手们对线期 KDA 压制更明显；FaZe 最近手感比对手好（FaZe 7-3，NiP 6-4，比赛结果都好于赛前预期）。 但是：NiP 这批首发最近赢得更多。 位置对比：辅助 ropz 近期表现优于 hampus；中单 rez 近期表现优于 karrigan；打野 broky 近期表现优于 plopski。 地图BP推演：FaZe禁Overpass，NiP禁Mirage；FaZe选Dust2（FaZe胜率65%），NiP选Ancient（FaZe胜率62%）；决胜图 Vertigo（FaZe胜率64%）。 总结：有一定爆冷可能。
- **ENCE vs Copenhagen Flames**：倾向 ENCE（系列赛胜率 70%，最可能比分 ENCE 2:0）。 为什么：ENCE 整体硬实力更强（实力分高 91）；近期状态：ENCE 最近 6胜4负（状态不错），Copenhagen Flames 最近 5胜5负（状态一般）；ENCE 选手们对线期 KDA 压制更明显。 位置对比：上单 maden 近期表现优于 hooxi；下路 nicoodoz 近期表现优于 dycha；中单 spinx 近期表现优于 jabbi。 地图BP推演：ENCE禁Vertigo，Copenhagen Flames禁Dust2；ENCE选Mirage（ENCE胜率66%），Copenhagen Flames选Overpass（ENCE胜率61%）；决胜图 Ancient（ENCE胜率64%）。 总结：有一定爆冷可能。
- **Heroic vs Natus Vincere**：倾向 Natus Vincere（系列赛胜率 66%，最可能比分 Natus Vincere 2:0）。 为什么：从长期战绩算出来的实力分看，Natus Vincere 领先 Heroic 约 91 分；Natus Vincere 选手们对线期 KDA 压制更明显。 不过要注意：Heroic 这批首发最近赢得更多。 位置对比：辅助 s1mple 近期表现优于 stavn；上单 teses 近期表现优于 boombl4；中单 b1t 近期表现优于 refrezh。 地图BP推演：Heroic禁Mirage，Natus Vincere禁Overpass；Heroic选Vertigo（Heroic胜率42%），Natus Vincere选Ancient（Heroic胜率38%）；决胜图 Nuke（Heroic胜率39%）。 总结：有一定爆冷可能。

### IEM Rio Major 2022

训练数据截止：2022-10-31（之后的比赛模型都没见过）  
夺冠概率：Heroic 27%，Natus Vincere 24%，Virtus.pro 14%，Cloud9 12%  
**预测冠军：Heroic**　｜　实际冠军：Virtus.pro ❌  
预测 4 强命中 2/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Cloud9 vs mousesports | Cloud9 | 56% | mousesports 1-2 | ❌ |
| R1M2 | fnatic vs Virtus.pro | Virtus.pro | 60% | Virtus.pro 0-2 | ✅ |
| R1M3 | Heroic vs Spirit | Heroic | 72% | Heroic 2-0 | ✅ |
| R1M4 | Natus Vincere vs FURIA | Natus Vincere | 69% | FURIA 1-2 | ❌ |
| R2M1 | mousesports vs Virtus.pro | Virtus.pro | 58% | Virtus.pro 1-2 | ✅ |
| R2M2 | Heroic vs FURIA | Heroic | 70% | Heroic 2-1 | ✅ |
| R3M1 | Virtus.pro vs Heroic | Heroic | 62% | Virtus.pro 2-0 | ❌ |

**赛前观点（8 强）：**

- **Cloud9 vs mousesports**：我看好 Cloud9（系列赛胜率 56%，最可能比分 Cloud9 2:0）。 为什么：从长期战绩算出来的实力分看，Cloud9 领先 mousesports 约 56 分。 风险点：mousesports 这批首发最近赢得更多。 位置对比：上单 ax1le 近期表现优于 jdc；下路 torzsi 近期表现优于 nafany；辅助 sh1ro 近期表现优于 xertion。 地图BP推演：Cloud9禁Nuke，mousesports禁Overpass；Cloud9选Ancient（Cloud9胜率56%），mousesports选Inferno（Cloud9胜率52%）；决胜图 Vertigo（Cloud9胜率54%）。 总结：基本五五开，谁赢都不奇怪。
- **fnatic vs Virtus.pro**：我看好 Virtus.pro（系列赛胜率 60%，最可能比分 Virtus.pro 2:0）。 理由：Virtus.pro 整体硬实力更强（实力分高 77）；近期状态：fnatic 最近 6胜4负（状态不错），Virtus.pro 最近 8胜2负（状态火热）。 不过要注意：fnatic 选手们对线期 KDA 压制更明显。 位置对比：中单 mezii 近期表现优于 qikert；辅助 roej 近期表现优于 n0rb3r7。 地图BP推演：fnatic禁Dust2，Virtus.pro禁Overpass；fnatic选Inferno（fnatic胜率45%），Virtus.pro选Nuke（fnatic胜率42%）；决胜图 Mirage（fnatic胜率43%）。 总结：基本五五开，谁赢都不奇怪。
- **Heroic vs Spirit**：倾向 Heroic（系列赛胜率 72%，最可能比分 Heroic 2:0）。 为什么：Heroic 整体硬实力更强（实力分高 143）；Heroic 最近手感比对手好（Heroic 9-1，Spirit 7-3，比赛结果都好于赛前预期）。 位置对比：辅助 w0nderful 近期表现优于 stavn；打野 cadian 近期表现优于 chopper。 地图BP推演：Heroic禁Dust2，Spirit禁Inferno；Heroic选Nuke（Heroic胜率66%），Spirit选Ancient（Heroic胜率64%）；决胜图 Overpass（Heroic胜率65%）。 总结：有一定爆冷可能。
- **Natus Vincere vs FURIA**：我的判断：Natus Vincere 晋级（系列赛胜率 69%，最可能比分 Natus Vincere 2:0）。 为什么：综合实力分 Natus Vincere 比 FURIA 高约 139 分；Natus Vincere 这批首发最近赢得更多；Natus Vincere 的职业比赛经验更多（Natus Vincere 1740 局 / FURIA 902 局）。 但是：FURIA 选手们对线期 KDA 压制更明显。 位置对比：上单 kscerato 近期表现优于 perfecto；下路 s1mple 近期表现优于 saffee；辅助 yuurih 近期表现优于 sdy。 地图BP推演：Natus Vincere禁Vertigo，FURIA禁Nuke；Natus Vincere选Dust2（Natus Vincere胜率65%），FURIA选Overpass（Natus Vincere胜率62%）；决胜图 Mirage（Natus Vincere胜率62%）。 总结：有一定爆冷可能。

### BLAST.tv Paris Major 2023

训练数据截止：2023-05-08（之后的比赛模型都没见过）  
夺冠概率：FaZe 32%，Vitality 22%，Liquid 22%，Heroic 19%  
**预测冠军：FaZe**　｜　实际冠军：Vitality ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Heroic vs FaZe | FaZe | 59% | Heroic 2-1 | ❌ |
| R1M2 | GamerLegion vs Monte | GamerLegion | 70% | GamerLegion 2-0 | ✅ |
| R1M3 | Liquid vs Apeks | Liquid | 77% | Apeks 0-2 | ❌ |
| R1M4 | Into The Breach vs Vitality | Vitality | 92% | Vitality 0-2 | ✅ |
| R2M1 | Heroic vs GamerLegion | Heroic | 80% | GamerLegion 1-2 | ❌ |
| R2M2 | Apeks vs Vitality | Vitality | 74% | Vitality 0-2 | ✅ |
| R3M1 | GamerLegion vs Vitality | Vitality | 77% | Vitality 0-2 | ✅ |

**赛前观点（8 强）：**

- **Heroic vs FaZe**：倾向 FaZe（系列赛胜率 59%，最可能比分 FaZe 2:0）。 理由：从长期战绩算出来的实力分看，FaZe 领先 Heroic 约 34 分；FaZe 选手们对线期 KDA 压制更明显。 位置对比：辅助 ropz 近期表现优于 sjuush；打野 broky 近期表现优于 cadian；中单 jabbi 近期表现优于 karrigan。 总结：基本五五开，谁赢都不奇怪。
- **GamerLegion vs Monte**：我的判断：GamerLegion 晋级（系列赛胜率 70%，最可能比分 GamerLegion 2:0）。 主要依据：GamerLegion 的职业比赛经验更多（GamerLegion 345 局 / Monte 3 局）；综合实力分 GamerLegion 比 Monte 高约 37 分；GamerLegion 选手们对线期 KDA 压制更明显。 不过要注意：Monte 这批首发最近赢得更多。 位置对比：打野 acor 近期表现优于 fessor；辅助 siuhy 近期表现优于 joel；下路 woro2k 近期表现优于 isak。 总结：有一定爆冷可能。
- **Liquid vs Apeks**：倾向 Liquid（系列赛胜率 77%，最可能比分 Liquid 2:0）。 为什么：Liquid 整体硬实力更强（实力分高 211）；老牌队伍经验更足：Liquid 打过 1620 局，Apeks 打过 78 局。 不过要注意：Apeks 这批首发最近赢得更多。 位置对比：辅助 nawwk 近期表现优于 osee；下路 jkaem 近期表现优于 nitr0；上单 elige 近期表现优于 michu。 总结：有一定爆冷可能。
- **Into The Breach vs Vitality**：倾向 Vitality（系列赛胜率 92%，最可能比分 Vitality 2:0）。 理由：Vitality 整体硬实力更强（实力分高 265）；老牌队伍经验更足：Into The Breach 打过 9 局，Vitality 打过 781 局；Vitality 选手们对线期 KDA 压制更明显。 不过要注意：Into The Breach 这批首发最近赢得更多。 位置对比：中单 zywoo 近期表现优于 thomas；辅助 dupreeh 近期表现优于 dobbo；上单 magisk 近期表现优于 adam9130。 总结：爆冷概率很低。

### PGL Major Copenhagen 2024

训练数据截止：2024-03-17（之后的比赛模型都没见过）  
夺冠概率：Spirit 28%，G2 16%，Vitality 15%，FaZe 12%  
**预测冠军：Spirit**　｜　实际冠军：Natus Vincere ❌  
预测 4 强命中 3/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs FaZe | Spirit | 63% | FaZe 1-2 | ❌ |
| R1M2 | Vitality vs Cloud9 | Vitality | 63% | Vitality 2-0 | ✅ |
| R1M3 | Eternal Fire vs Natus Vincere | Natus Vincere | 59% | Natus Vincere 0-2 | ✅ |
| R1M4 | G2 vs mousesports | G2 | 56% | G2 2-0 | ✅ |
| R2M1 | FaZe vs Vitality | FaZe | 50% | FaZe 2-1 | ✅ |
| R2M2 | Natus Vincere vs G2 | G2 | 59% | Natus Vincere 2-1 | ❌ |
| R3M1 | FaZe vs Natus Vincere | FaZe | 59% | Natus Vincere 1-2 | ❌ |

**赛前观点（8 强）：**

- **Spirit vs FaZe**：我看好 Spirit（系列赛胜率 63%，最可能比分 Spirit 2:0）。 主要依据：Spirit 选手们对线期 KDA 压制更明显；Spirit 整体硬实力更强（实力分高 52）；近期状态：Spirit 最近 8胜2负（状态火热），FaZe 最近 5胜5负（状态一般）。 风险点：FaZe 这批首发最近赢得更多。 位置对比：上单 donk 近期表现优于 broky；中单 magixx 近期表现优于 karrigan；下路 sh1ro 近期表现优于 rain。 地图BP推演：Spirit禁Inferno，FaZe禁Overpass；Spirit选Mirage（Spirit胜率60%），FaZe选Nuke（Spirit胜率58%）；决胜图 Anubis（Spirit胜率58%）。 总结：有一定爆冷可能。
- **Vitality vs Cloud9**：我的判断：Vitality 晋级（系列赛胜率 63%，最可能比分 Vitality 2:0）。 主要依据：从长期战绩算出来的实力分看，Vitality 领先 Cloud9 约 67 分；Vitality 选手们对线期 KDA 压制更明显；近期状态：Vitality 最近 6胜4负（状态不错），Cloud9 最近 6胜4负（状态不错）。 但是：Cloud9 这批首发最近赢得更多。 位置对比：打野 zywoo 近期表现优于 boombl4；中单 hobbit 近期表现优于 apex；辅助 electronic 近期表现优于 mezii。 地图BP推演：Vitality禁Overpass，Cloud9禁Inferno；Vitality选Vertigo（Vitality胜率61%），Cloud9选Ancient（Vitality胜率57%）；决胜图 Anubis（Vitality胜率58%）。 总结：有一定爆冷可能。
- **Eternal Fire vs Natus Vincere**：我的判断：Natus Vincere 晋级（系列赛胜率 59%，最可能比分 Natus Vincere 2:0）。 为什么：从长期战绩算出来的实力分看，Natus Vincere 领先 Eternal Fire 约 39 分；Natus Vincere 的职业比赛经验更多（Eternal Fire 166 局 / Natus Vincere 1810 局）；Natus Vincere 选手们对线期 KDA 压制更明显。 不过要注意：近期状态：Eternal Fire 最近 5胜5负（状态一般），Natus Vincere 最近 5胜5负（状态一般）。 位置对比：上单 calyx 近期表现优于 aleksib；打野 b1t 近期表现优于 maj3r；辅助 w0nderful 近期表现优于 woxic。 地图BP推演：Eternal Fire禁Nuke，Natus Vincere禁Inferno；Eternal Fire选Vertigo（Eternal Fire胜率45%），Natus Vincere选Mirage（Eternal Fire胜率42%）；决胜图 Overpass（Eternal Fire胜率45%）。 总结：基本五五开，谁赢都不奇怪。
- **G2 vs mousesports**：我的判断：G2 晋级（系列赛胜率 56%，最可能比分 G2 2:0）。 主要依据：综合实力分 G2 比 mousesports 高约 52 分；G2 选手们对线期 KDA 压制更明显。 风险点：mousesports 最近手感比对手好（G2 7-3，mousesports 8-2，比赛结果都好于赛前预期）。 位置对比：下路 m0nesy 近期表现优于 torzsi；上单 brollan 近期表现优于 hooxi；打野 niko 近期表现优于 jimpphat。 地图BP推演：G2禁Mirage，mousesports禁Inferno；G2选Nuke（G2胜率55%），mousesports选Overpass（G2胜率53%）；决胜图 Ancient（G2胜率54%）。 总结：基本五五开，谁赢都不奇怪。

### Perfect World Shanghai Major 2024

训练数据截止：2024-11-30（之后的比赛模型都没见过）  
夺冠概率：Vitality 23%，G2 19%，Spirit 16%，mousesports 11%  
**预测冠军：Vitality**　｜　实际冠军：Spirit ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | The Mongolz vs mousesports | mousesports | 54% | mousesports 0-2 | ✅ |
| R1M2 | Liquid vs Spirit | Spirit | 59% | Spirit 0-2 | ✅ |
| R1M3 | G2 vs Heroic | G2 | 63% | G2 2-1 | ✅ |
| R1M4 | FaZe vs Vitality | Vitality | 65% | FaZe 2-1 | ❌ |
| R2M1 | mousesports vs Spirit | Spirit | 55% | Spirit 1-2 | ✅ |
| R2M2 | G2 vs FaZe | G2 | 62% | FaZe 0-2 | ❌ |
| R3M1 | Spirit vs FaZe | Spirit | 59% | Spirit 2-1 | ✅ |

**赛前观点（8 强）：**

- **The Mongolz vs mousesports**：倾向 mousesports（系列赛胜率 54%，最可能比分 mousesports 2:0）。 为什么：mousesports 的职业比赛经验更多（The Mongolz 415 局 / mousesports 2057 局）；mousesports 这批首发最近赢得更多；综合实力分 mousesports 比 The Mongolz 高约 7 分。 但是：The Mongolz 选手们对线期 KDA 压制更明显。 位置对比：中单 blitz 近期表现优于 siuhy；打野 jimpphat 近期表现优于 techno；辅助 senzu 近期表现优于 xertion。 地图BP推演：The Mongolz禁Mirage，mousesports禁Dust2；The Mongolz选Ancient（The Mongolz胜率49%），mousesports选Inferno（The Mongolz胜率46%）；决胜图 Anubis（The Mongolz胜率48%）。 总结：基本五五开，谁赢都不奇怪。
- **Liquid vs Spirit**：我的判断：Spirit 晋级（系列赛胜率 59%，最可能比分 Spirit 2:0）。 为什么：Spirit 整体硬实力更强（实力分高 52）；Spirit 选手们对线期 KDA 压制更明显。 不过要注意：Liquid 这批首发最近赢得更多。 位置对比：下路 sh1ro 近期表现优于 jks；上单 donk 近期表现优于 naf；打野 twistzz 近期表现优于 chopper。 地图BP推演：Liquid禁Nuke，Spirit禁Inferno；Liquid选Ancient（Liquid胜率46%），Spirit选Dust2（Liquid胜率41%）；决胜图 Vertigo（Liquid胜率44%）。 总结：基本五五开，谁赢都不奇怪。
- **G2 vs Heroic**：我的判断：G2 晋级（系列赛胜率 63%，最可能比分 G2 2:0）。 理由：从长期战绩算出来的实力分看，G2 领先 Heroic 约 122 分。 风险点：Heroic 选手们对线期 KDA 压制更明显。 位置对比：打野 teses 近期表现优于 snax；上单 nertz 近期表现优于 niko；下路 m0nesy 近期表现优于 kyxsan。 地图BP推演：G2禁Mirage，Heroic禁Inferno；G2选Nuke（G2胜率60%），Heroic选Vertigo（G2胜率56%）；决胜图 Dust2（G2胜率59%）。 总结：有一定爆冷可能。
- **FaZe vs Vitality**：倾向 Vitality（系列赛胜率 65%，最可能比分 Vitality 2:0）。 主要依据：Vitality 整体硬实力更强（实力分高 90）；Vitality 选手们对线期 KDA 压制更明显；近期状态：FaZe 最近 6胜4负（状态不错），Vitality 最近 8胜2负（状态火热）。 但是：FaZe 这批首发最近赢得更多。 位置对比：打野 zywoo 近期表现优于 frozen；上单 spinx 近期表现优于 broky；下路 rain 近期表现优于 flamez。 地图BP推演：FaZe禁Nuke，Vitality禁Inferno；FaZe选Anubis（FaZe胜率41%），Vitality选Dust2（FaZe胜率38%）；决胜图 Ancient（FaZe胜率41%）。 总结：有一定爆冷可能。

### BLAST.tv Austin Major 2025

训练数据截止：2025-06-03（之后的比赛模型都没见过）  
夺冠概率：Vitality 47%，mousesports 17%，Spirit 16%，The Mongolz 9%  
**预测冠军：Vitality**　｜　实际冠军：Vitality ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs mousesports | mousesports | 51% | mousesports 1-2 | ✅ |
| R1M2 | Vitality vs Natus Vincere | Vitality | 83% | Vitality 2-0 | ✅ |
| R1M3 | FaZe vs The Mongolz | The Mongolz | 59% | The Mongolz 0-2 | ✅ |
| R1M4 | paiN Gaming vs FURIA | FURIA | 71% | paiN Gaming 2-1 | ❌ |
| R2M1 | mousesports vs Vitality | Vitality | 65% | Vitality 1-2 | ✅ |
| R2M2 | The Mongolz vs paiN Gaming | The Mongolz | 83% | The Mongolz 2-0 | ✅ |
| R3M1 | Vitality vs The Mongolz | Vitality | 84% | Vitality 2-1 | ✅ |

**赛前观点（8 强）：**

- **Spirit vs mousesports**：倾向 mousesports（系列赛胜率 51%，最可能比分 mousesports 0:2）。 理由：mousesports 这批首发最近赢得更多；mousesports 选手们对线期 KDA 压制更明显。 风险点：Spirit 整体硬实力更强（实力分高 35）。 位置对比：上单 donk 近期表现优于 brollan；打野 jimpphat 近期表现优于 chopper；中单 spinx 近期表现优于 magixx。 地图BP推演：Spirit禁Mirage，mousesports禁Dust2；Spirit选Anubis（Spirit胜率50%），mousesports选Inferno（Spirit胜率48%）；决胜图 Train（Spirit胜率49%）。 总结：基本五五开，谁赢都不奇怪。
- **Vitality vs Natus Vincere**：我的判断：Vitality 晋级（系列赛胜率 83%，最可能比分 Vitality 2:0）。 主要依据：从长期战绩算出来的实力分看，Vitality 领先 Natus Vincere 约 223 分；Vitality 选手们对线期 KDA 压制更明显；Vitality 最近手感比对手好（Vitality 8-2，Natus Vincere 7-3，比赛结果都好于赛前预期）。 但是：Natus Vincere 这批首发最近赢得更多。 位置对比：上单 zywoo 近期表现优于 aleksib；打野 b1t 近期表现优于 apex。 地图BP推演：Vitality禁Mirage，Natus Vincere禁Inferno；Vitality选Nuke（Vitality胜率77%），Natus Vincere选Train（Vitality胜率72%）；决胜图 Ancient（Vitality胜率74%）。 总结：爆冷概率很低。
- **FaZe vs The Mongolz**：倾向 The Mongolz（系列赛胜率 59%，最可能比分 The Mongolz 2:0）。 主要依据：从长期战绩算出来的实力分看，The Mongolz 领先 FaZe 约 86 分；The Mongolz 最近手感比对手好（FaZe 4-6，The Mongolz 6-4，比赛结果都好于赛前预期）；The Mongolz 选手们对线期 KDA 压制更明显。 但是：FaZe 这批首发最近赢得更多。 位置对比：辅助 senzu 近期表现优于 skullz；打野 frozen 近期表现优于 techno；下路 s1mple 近期表现优于 mzinho。 地图BP推演：FaZe禁Dust2，The Mongolz禁Inferno；FaZe选Anubis（FaZe胜率45%），The Mongolz选Mirage（FaZe胜率43%）；决胜图 Nuke（FaZe胜率44%）。 总结：基本五五开，谁赢都不奇怪。
- **paiN Gaming vs FURIA**：我看好 FURIA（系列赛胜率 71%，最可能比分 FURIA 2:0）。 主要依据：从长期战绩算出来的实力分看，FURIA 领先 paiN Gaming 约 102 分；FURIA 选手们对线期 KDA 压制更明显；近期状态：paiN Gaming 最近 2胜8负（状态低迷），FURIA 最近 4胜6负（状态一般）。 但是：paiN Gaming 这批首发最近赢得更多。 位置对比：打野 kscerato 近期表现优于 biguzera；下路 molodoy 近期表现优于 dgt；上单 fallen 近期表现优于 snowzin。 地图BP推演：paiN Gaming禁Train，FURIA禁Nuke；paiN Gaming选Mirage（paiN Gaming胜率37%），FURIA选Inferno（paiN Gaming胜率34%）；决胜图 Dust2（paiN Gaming胜率36%）。 总结：有一定爆冷可能。

### StarLadder Budapest Major 2025

训练数据截止：2025-11-24（之后的比赛模型都没见过）  
夺冠概率：FURIA 38%，mousesports 24%，Vitality 15%，Team Falcons 14%  
**预测冠军：FURIA**　｜　实际冠军：Vitality ❌  
预测 4 强命中 1/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs Team Falcons | Team Falcons | 59% | Spirit 2-0 | ❌ |
| R1M2 | The Mongolz vs Vitality | Vitality | 75% | Vitality 0-2 | ✅ |
| R1M3 | mousesports vs FaZe | mousesports | 83% | FaZe 0-2 | ❌ |
| R1M4 | Natus Vincere vs FURIA | FURIA | 83% | Natus Vincere 2-1 | ❌ |
| R2M1 | Spirit vs Vitality | Vitality | 57% | Vitality 0-2 | ✅ |
| R2M2 | FaZe vs Natus Vincere | Natus Vincere | 58% | FaZe 2-1 | ❌ |
| R3M1 | Vitality vs FaZe | Vitality | 84% | Vitality 3-1 | ✅ |

**赛前观点（8 强）：**

- **Spirit vs Team Falcons**：倾向 Team Falcons（系列赛胜率 59%，最可能比分 Team Falcons 2:0）。 为什么：从长期战绩算出来的实力分看，Team Falcons 领先 Spirit 约 65 分；Team Falcons 选手们对线期 KDA 压制更明显；近期状态：Spirit 最近 4胜6负（状态一般），Team Falcons 最近 7胜3负（状态不错）。 但是：Spirit 这批首发最近赢得更多。 位置对比：辅助 m0nesy 近期表现优于 zweih；中单 sh1ro 近期表现优于 teses；打野 niko 近期表现优于 chopper。 地图BP推演：Spirit禁Nuke，Team Falcons禁Dust2；Spirit选Overpass（Spirit胜率46%），Team Falcons选Ancient（Spirit胜率42%）；决胜图 Mirage（Spirit胜率44%）。 总结：基本五五开，谁赢都不奇怪。
- **The Mongolz vs Vitality**：我看好 Vitality（系列赛胜率 75%，最可能比分 Vitality 2:0）。 为什么：Vitality 整体硬实力更强（实力分高 148）；Vitality 的职业比赛经验更多（The Mongolz 592 局 / Vitality 1096 局）；近期状态：The Mongolz 最近 3胜7负（状态低迷），Vitality 最近 4胜6负（状态一般）。 位置对比：打野 techno 近期表现优于 apex；辅助 ropz 近期表现优于 mzinho；中单 flamez 近期表现优于 blitz。 地图BP推演：The Mongolz禁Dust2，Vitality禁Ancient；The Mongolz选Mirage（The Mongolz胜率34%），Vitality选Nuke（The Mongolz胜率30%）；决胜图 Overpass（The Mongolz胜率33%）。 总结：有一定爆冷可能。
- **mousesports vs FaZe**：我的判断：mousesports 晋级（系列赛胜率 83%，最可能比分 mousesports 2:0）。 为什么：从长期战绩算出来的实力分看，mousesports 领先 FaZe 约 175 分；mousesports 选手们对线期 KDA 压制更明显；mousesports 最近手感比对手好（mousesports 5-5，FaZe 4-6，比赛结果都好于赛前预期）。 但是：FaZe 这批首发最近赢得更多。 位置对比：辅助 xertion 近期表现优于 karrigan；中单 spinx 近期表现优于 broky；上单 brollan 近期表现优于 jcobbb。 地图BP推演：mousesports禁Ancient，FaZe禁Train；mousesports选Overpass（mousesports胜率75%），FaZe选Inferno（mousesports胜率73%）；决胜图 Mirage（mousesports胜率73%）。 总结：爆冷概率很低。
- **Natus Vincere vs FURIA**：我的判断：FURIA 晋级（系列赛胜率 83%，最可能比分 FURIA 2:0）。 为什么：综合实力分 FURIA 比 Natus Vincere 高约 185 分；FURIA 选手们对线期 KDA 压制更明显；近期状态：Natus Vincere 最近 2胜8负（状态低迷），FURIA 最近 8胜2负（状态火热）。 风险点：Natus Vincere 这批首发最近赢得更多。 位置对比：下路 molodoy 近期表现优于 makazze；中单 yekindar 近期表现优于 im；打野 kscerato 近期表现优于 b1t。 地图BP推演：Natus Vincere禁Nuke，FURIA禁Train；Natus Vincere选Dust2（Natus Vincere胜率28%），FURIA选Inferno（Natus Vincere胜率24%）；决胜图 Ancient（Natus Vincere胜率27%）。 总结：爆冷概率很低。

### IEM Cologne Major 2026

训练数据截止：2026-06-02（之后的比赛模型都没见过）  
夺冠概率：Vitality 39%，Spirit 35%，FURIA 10%，Aurora Gaming 4%  
**预测冠军：Vitality**　｜　实际冠军：Team Falcons ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Spirit vs G2 | Spirit | 76% | Spirit 2-1 | ✅ |
| R1M2 | Team Falcons vs Vitality | Vitality | 77% | Team Falcons 2-1 | ❌ |
| R1M3 | Aurora Gaming vs BetBoom Team | Aurora Gaming | 54% | Aurora Gaming 2-0 | ✅ |
| R1M4 | 9z Team vs FURIA | FURIA | 73% | FURIA 1-2 | ✅ |
| R2M1 | Spirit vs Team Falcons | Spirit | 75% | Team Falcons 1-2 | ❌ |
| R2M2 | Aurora Gaming vs FURIA | FURIA | 57% | FURIA 0-2 | ✅ |
| R3M1 | Team Falcons vs FURIA | Team Falcons | 50% | Team Falcons 3-0 | ✅ |

**赛前观点（8 强）：**

- **Spirit vs G2**：我的判断：Spirit 晋级（系列赛胜率 76%，最可能比分 Spirit 2:0）。 理由：Spirit 整体硬实力更强（实力分高 130）；Spirit 选手们对线期 KDA 压制更明显；近期状态：Spirit 最近 9胜1负（状态火热），G2 最近 4胜6负（状态一般）。 风险点：G2 这批首发最近赢得更多。 位置对比：中单 sh1ro 近期表现优于 nertz；上单 donk 近期表现优于 heavygod；辅助 zont1x 近期表现优于 hunter-。 地图BP推演：Spirit禁Inferno，G2禁Dust2；Spirit选Anubis（Spirit胜率69%），G2选Nuke（Spirit胜率68%）；决胜图 Mirage（Spirit胜率69%）。 总结：有一定爆冷可能。
- **Team Falcons vs Vitality**：倾向 Vitality（系列赛胜率 77%，最可能比分 Vitality 2:0）。 主要依据：综合实力分 Vitality 比 Team Falcons 高约 154 分；Vitality 选手们对线期 KDA 压制更明显；Vitality 的职业比赛经验更多（Team Falcons 435 局 / Vitality 1176 局）。 但是：Team Falcons 这批首发最近赢得更多。 位置对比：下路 mezii 近期表现优于 karrigan；辅助 m0nesy 近期表现优于 ropz；上单 zywoo 近期表现优于 kyousuke。 地图BP推演：Team Falcons禁Dust2，Vitality禁Ancient；Team Falcons选Anubis（Team Falcons胜率33%），Vitality选Inferno（Team Falcons胜率27%）；决胜图 Mirage（Team Falcons胜率32%）。 总结：有一定爆冷可能。
- **Aurora Gaming vs BetBoom Team**：我的判断：Aurora Gaming 晋级（系列赛胜率 54%，最可能比分 Aurora Gaming 2:0）。 主要依据：Aurora Gaming 整体硬实力更强（实力分高 16）；Aurora Gaming 最近手感比对手好（Aurora Gaming 6-4，BetBoom Team 5-5，比赛结果都好于赛前预期）。 位置对比：打野 fl4mus 近期表现优于 soulfly；下路 xantares 近期表现优于 s1ren；上单 maj3r 近期表现优于 boombl4。 地图BP推演：Aurora Gaming禁Nuke，BetBoom Team禁Mirage；Aurora Gaming选Overpass（Aurora Gaming胜率55%），BetBoom Team选Dust2（Aurora Gaming胜率51%）；决胜图 Ancient（Aurora Gaming胜率52%）。 总结：基本五五开，谁赢都不奇怪。
- **9z Team vs FURIA**：我的判断：FURIA 晋级（系列赛胜率 73%，最可能比分 FURIA 2:0）。 理由：FURIA 整体硬实力更强（实力分高 101）；老牌队伍经验更足：9z Team 打过 283 局，FURIA 打过 1350 局；FURIA 选手们对线期 KDA 压制更明显。 位置对比：下路 molodoy 近期表现优于 max；上单 huasopeek 近期表现优于 fallen；中单 luchov 近期表现优于 yekindar。 地图BP推演：9z Team禁Mirage，FURIA禁Ancient；9z Team选Overpass（9z Team胜率35%），FURIA选Inferno（9z Team胜率33%）；决胜图 Nuke（9z Team胜率34%）。 总结：有一定爆冷可能。
