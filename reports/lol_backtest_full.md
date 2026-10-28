# 英雄联盟世界赛 S1-S15 回测 · 完整模式（看过往届大赛 + 当届小组赛）

- 系列赛预测命中率：**63.6%**（107 场；瞎猜 50%）
- 4 强命中：66.1%　决赛队伍命中：57.1%　冠军命中：**35.7%**（瞎猜 12.5%）
- 对真实冠军给出的平均夺冠概率：20.7%　对数损失：0.639（越低越好，瞎猜 0.693）

### S1 2011 世界赛

训练数据截止：2011-06-19（之后的比赛模型都没见过）  
（特殊赛制）预测冠军：epik gamer，实际：Fnatic ❌

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | against all authority vs team gamed!de | against all authority | 57% | against all authority 2-0 | ✅ |
| R1M2 | Counter Logic Gaming vs Fnatic | Counter Logic Gaming | 66% | Fnatic 1-2 | ❌ |
| R2M1 | TSM vs against all authority | TSM | 53% | against all authority 1-2 | ❌ |
| R2M2 | epik gamer vs Fnatic | epik gamer | 69% | Fnatic 0-2 | ❌ |
| R3M1 | against all authority vs Fnatic | against all authority | 66% | Fnatic 0-2 | ❌ |
| R2M3 | TSM vs epik gamer | epik gamer | 50% | TSM 2-0 | ❌ |
| R3M2 | against all authority vs TSM | TSM | 53% | against all authority 2-0 | ❌ |
| R4M1 | Fnatic vs against all authority | against all authority | 66% | Fnatic 2-1 | ❌ |
| R1M1 | team gamed!de vs Counter Logic Gaming | Counter Logic Gaming | 55% | Counter Logic Gaming 0-1 | ✅ |

### S2 2012 世界赛

训练数据截止：2012-10-05（之后的比赛模型都没见过）  
夺冠概率：najin sword 40%，azubu frost 20%，TSM 11%，moscow five 11%  
**预测冠军：najin sword**　｜　实际冠军：tpa ❌  
预测 4 强命中 1/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | moscow five vs Invictus Gaming | Invictus Gaming | 50% | moscow five 2-0 | ❌ |
| R1M2 | tpa vs najin sword | najin sword | 60% | tpa 2-0 | ❌ |
| R1M3 | TSM vs azubu frost | azubu frost | 70% | azubu frost 0-2 | ✅ |
| R1M4 | Team WE vs counter logic gaming europe | Team WE | 63% | counter logic gaming europe 1-2 | ❌ |
| R2M1 | moscow five vs tpa | moscow five | 63% | tpa 1-2 | ❌ |
| R2M2 | azubu frost vs counter logic gaming europe | azubu frost | 100% | azubu frost 2-1 | ✅ |
| R3M1 | tpa vs azubu frost | azubu frost | 67% | tpa 3-1 | ❌ |

**赛前观点（8 强）：**

- **moscow five vs Invictus Gaming**：我看好 Invictus Gaming（系列赛胜率 50%，最可能比分 Invictus Gaming 2:0）。 主要依据：Invictus Gaming 的职业比赛经验更多（moscow five 14 局 / Invictus Gaming 9 局）。 但是：近期状态：moscow five 最近 8胜2负（状态火热），Invictus Gaming 最近 6胜3负（状态不错）。 总结：基本五五开，谁赢都不奇怪。
- **tpa vs najin sword**：倾向 najin sword（系列赛胜率 60%，最可能比分 najin sword 2:0）。 理由：近期状态：tpa 最近 5胜2负（状态不错），najin sword 最近 8胜2负（状态火热）；综合实力分 najin sword 比 tpa 高约 92 分。 风险点：tpa 的职业比赛经验更多（tpa 7 局 / najin sword 26 局）。 总结：基本五五开，谁赢都不奇怪。
- **TSM vs azubu frost**：倾向 azubu frost（系列赛胜率 70%，最可能比分 azubu frost 2:0）。 主要依据：azubu frost 的职业比赛经验更多（TSM 86 局 / azubu frost 13 局）；azubu frost 最近手感比对手好（TSM 6-4，azubu frost 8-2，比赛结果都好于赛前预期）。 但是：TSM 整体硬实力更强（实力分高 25）。 总结：有一定爆冷可能。
- **Team WE vs counter logic gaming europe**：我的判断：Team WE 晋级（系列赛胜率 63%，最可能比分 Team WE 2:0）。 理由：老牌队伍经验更足：Team WE 打过 5 局，counter logic gaming europe 打过 36 局；Team WE 最近手感比对手好（Team WE 4-1，counter logic gaming europe 5-5，比赛结果都好于赛前预期）。 但是：counter logic gaming europe 整体硬实力更强（实力分高 71）。 总结：有一定爆冷可能。

### S3 2013 世界赛

训练数据截止：2013-09-24（之后的比赛模型都没见过）  
夺冠概率：T1 25%，Oh My God 17%，Royal Never Give Up 15%，Cloud9 14%  
**预测冠军：Royal Never Give Up**　｜　实际冠军：T1 ❌  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | gamania bears vs T1 | T1 | 79% | T1 0-2 | ✅ |
| R1M2 | najin sword vs Gambit Esports | najin sword | 58% | najin sword 2-1 | ✅ |
| R1M3 | Royal Never Give Up vs Oh My God | Royal Never Give Up | 52% | Royal Never Give Up 2-0 | ✅ |
| R1M4 | Cloud9 vs Fnatic | Cloud9 | 53% | Fnatic 1-2 | ❌ |
| R2M1 | T1 vs najin sword | T1 | 73% | T1 3-2 | ✅ |
| R2M2 | Royal Never Give Up vs Fnatic | Royal Never Give Up | 55% | Royal Never Give Up 3-1 | ✅ |
| R3M1 | T1 vs Royal Never Give Up | Royal Never Give Up | 52% | T1 3-0 | ❌ |

**赛前观点（8 强）：**

- **gamania bears vs T1**：倾向 T1（系列赛胜率 79%，最可能比分 T1 2:0）。 主要依据：从长期战绩算出来的实力分看，T1 领先 gamania bears 约 160 分；近期状态：gamania bears 最近 7胜3负（状态不错），T1 最近 9胜1负（状态火热）。 总结：有一定爆冷可能。
- **najin sword vs Gambit Esports**：我的判断：najin sword 晋级（系列赛胜率 58%，最可能比分 najin sword 2:0）。 理由：综合实力分 najin sword 比 Gambit Esports 高约 116 分；najin sword 这批首发最近赢得更多。 不过要注意：Gambit Esports 选手们对线期 KDA 压制更明显。 位置对比：辅助 cain 近期表现优于 voidle；打野 watch 近期表现优于 diamondprox；中单 nagne 近期表现优于 alex ich。 总结：基本五五开，谁赢都不奇怪。
- **Royal Never Give Up vs Oh My God**：倾向 Royal Never Give Up（系列赛胜率 52%，最可能比分 Royal Never Give Up 2:0）。 为什么：近期状态：Royal Never Give Up 最近 6胜4负（状态不错），Oh My God 最近 7胜3负（状态不错）。 风险点：从长期战绩算出来的实力分看，Oh My God 领先 Royal Never Give Up 约 85 分。 总结：基本五五开，谁赢都不奇怪。
- **Cloud9 vs Fnatic**：我的判断：Cloud9 晋级（系列赛胜率 53%，最可能比分 Cloud9 2:0）。 理由：Cloud9 选手们对线期 KDA 压制更明显；Cloud9 整体硬实力更强（实力分高 35）。 不过要注意：Fnatic 这批首发最近赢得更多。 位置对比：中单 xpeke 近期表现优于 hai；下路 puszu 近期表现优于 sneaky；上单 soaz 近期表现优于 balls。 总结：基本五五开，谁赢都不奇怪。

### S4 2014 世界赛

训练数据截止：2014-10-03（之后的比赛模型都没见过）  
夺冠概率：samsung white 25%，Royal Never Give Up 20%，samsung blue 18%，najin white shield 15%  
**预测冠军：samsung white**　｜　实际冠军：samsung white ✅  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | samsung white vs TSM | samsung white | 66% | samsung white 3-1 | ✅ |
| R1M2 | samsung blue vs Cloud9 | samsung blue | 65% | samsung blue 3-1 | ✅ |
| R1M3 | Royal Never Give Up vs EDward Gaming | Royal Never Give Up | 72% | Royal Never Give Up 3-2 | ✅ |
| R1M4 | najin white shield vs Oh My God | najin white shield | 59% | Oh My God 0-3 | ❌ |
| R2M1 | samsung white vs samsung blue | samsung white | 61% | samsung white 3-0 | ✅ |
| R2M2 | Royal Never Give Up vs Oh My God | Royal Never Give Up | 76% | Royal Never Give Up 3-2 | ✅ |
| R3M1 | samsung white vs Royal Never Give Up | samsung white | 56% | samsung white 3-1 | ✅ |

**赛前观点（8 强）：**

- **samsung white vs TSM**：我的判断：samsung white 晋级（系列赛胜率 66%，最可能比分 samsung white 3:1）。 为什么：samsung white 整体硬实力更强（实力分高 163）；samsung white 最近手感比对手好（samsung white 10-0，TSM 6-4，比赛结果都好于赛前预期）。 不过要注意：TSM 的职业比赛经验更多（samsung white 24 局 / TSM 256 局）。 总结：有一定爆冷可能。
- **samsung blue vs Cloud9**：我的判断：samsung blue 晋级（系列赛胜率 65%，最可能比分 samsung blue 3:1）。 理由：综合实力分 samsung blue 比 Cloud9 高约 160 分；samsung blue 最近手感比对手好（samsung blue 7-3，Cloud9 6-4，比赛结果都好于赛前预期）。 但是：老牌队伍经验更足：samsung blue 打过 43 局，Cloud9 打过 112 局。 总结：有一定爆冷可能。
- **Royal Never Give Up vs EDward Gaming**：我看好 Royal Never Give Up（系列赛胜率 72%，最可能比分 Royal Never Give Up 3:1）。 主要依据：Royal Never Give Up 最近手感比对手好（Royal Never Give Up 8-2，EDward Gaming 6-4，比赛结果都好于赛前预期）；老牌队伍经验更足：Royal Never Give Up 打过 126 局，EDward Gaming 打过 60 局；Royal Never Give Up 整体硬实力更强（实力分高 18）。 总结：有一定爆冷可能。
- **najin white shield vs Oh My God**：我看好 najin white shield（系列赛胜率 59%，最可能比分 najin white shield 3:1）。 理由：najin white shield 最近手感比对手好（najin white shield 7-3，Oh My God 4-6，比赛结果都好于赛前预期）；从长期战绩算出来的实力分看，najin white shield 领先 Oh My God 约 90 分。 风险点：老牌队伍经验更足：najin white shield 打过 36 局，Oh My God 打过 165 局。 总结：基本五五开，谁赢都不奇怪。

### S5 2015 世界赛

训练数据截止：2015-10-01（之后的比赛模型都没见过）  
夺冠概率：T1 52%，EDward Gaming 23%，KT Rolster 9%，ROX Tigers 6%  
**预测冠军：T1**　｜　实际冠军：T1 ✅  
预测 4 强命中 2/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Flash Wolves vs Origen | Origen | 51% | Origen 1-3 | ✅ |
| R1M2 | T1 vs ahq eSports Club | T1 | 82% | T1 3-0 | ✅ |
| R1M3 | Fnatic vs EDward Gaming | EDward Gaming | 75% | Fnatic 3-0 | ❌ |
| R1M4 | KT Rolster vs ROX Tigers | KT Rolster | 56% | ROX Tigers 1-3 | ❌ |
| R2M1 | Origen vs T1 | T1 | 87% | T1 0-3 | ✅ |
| R2M2 | Fnatic vs ROX Tigers | ROX Tigers | 67% | ROX Tigers 0-3 | ✅ |
| R3M1 | T1 vs ROX Tigers | T1 | 88% | T1 3-1 | ✅ |

**赛前观点（8 强）：**

- **Flash Wolves vs Origen**：我的判断：Origen 晋级（系列赛胜率 51%，最可能比分 Origen 3:1）。 理由：近期状态：Flash Wolves 最近 6胜4负（状态不错），Origen 最近 6胜4负（状态不错）。 风险点：Flash Wolves 的职业比赛经验更多（Flash Wolves 77 局 / Origen 35 局）。 总结：基本五五开，谁赢都不奇怪。
- **T1 vs ahq eSports Club**：我看好 T1（系列赛胜率 82%，最可能比分 T1 3:0）。 为什么：T1 整体硬实力更强（实力分高 406）。 不过要注意：近期状态：T1 最近 9胜1负（状态火热），ahq eSports Club 最近 10胜0负（状态火热）。 总结：爆冷概率很低。
- **Fnatic vs EDward Gaming**：我看好 EDward Gaming（系列赛胜率 75%，最可能比分 EDward Gaming 3:1）。 理由：从长期战绩算出来的实力分看，EDward Gaming 领先 Fnatic 约 296 分。 不过要注意：Fnatic 最近手感比对手好（Fnatic 8-2，EDward Gaming 6-4，比赛结果都好于赛前预期）。 位置对比：下路 puszu 近期表现优于 namei；辅助 yellowstar 近期表现优于 fzzf；中单 xpeke 近期表现优于 u。 总结：有一定爆冷可能。
- **KT Rolster vs ROX Tigers**：我看好 KT Rolster（系列赛胜率 56%，最可能比分 KT Rolster 3:1）。 理由：老牌队伍经验更足：KT Rolster 打过 104 局，ROX Tigers 打过 53 局；KT Rolster 整体硬实力更强（实力分高 15）。 总结：基本五五开，谁赢都不奇怪。

### S6 2016 世界赛

训练数据截止：2016-09-29（之后的比赛模型都没见过）  
夺冠概率：ROX Tigers 31%，Samsung Galaxy 21%，EDward Gaming 18%，T1 11%  
**预测冠军：ROX Tigers**　｜　实际冠军：T1 ❌  
预测 4 强命中 4/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | T1 vs Royal Never Give Up | T1 | 61% | T1 3-1 | ✅ |
| R1M2 | ROX Tigers vs EDward Gaming | ROX Tigers | 56% | ROX Tigers 3-1 | ✅ |
| R1M3 | Samsung Galaxy vs Cloud9 | Samsung Galaxy | 63% | Samsung Galaxy 3-0 | ✅ |
| R1M4 | H2k-Gaming vs Albus NoX Luna | H2k-Gaming | 74% | H2k-Gaming 3-0 | ✅ |
| R2M1 | T1 vs ROX Tigers | ROX Tigers | 81% | T1 3-2 | ❌ |
| R2M2 | Samsung Galaxy vs H2k-Gaming | Samsung Galaxy | 71% | Samsung Galaxy 3-0 | ✅ |
| R3M1 | T1 vs Samsung Galaxy | Samsung Galaxy | 63% | T1 3-2 | ❌ |

**赛前观点（8 强）：**

- **T1 vs Royal Never Give Up**：倾向 T1（系列赛胜率 61%，最可能比分 T1 3:1）。 为什么：从长期战绩算出来的实力分看，T1 领先 Royal Never Give Up 约 132 分；T1 选手们对线期 KDA 压制更明显。 但是：Royal Never Give Up 选手对位输出更高。 位置对比：上单 looper 近期表现优于 duke；下路 uzi 近期表现优于 bang；辅助 mata 近期表现优于 wolf。 BP预测：T1 的招牌英雄 Sivir、Alistar、Trundle；Royal Never Give Up 的招牌英雄 Braum、Karma、Rek'Sai。T1 应优先禁 Rek'Sai、Sivir、Trundle，Royal Never Give Up 大概率禁 Ekko、Gangplank、Tahm Kench。 总结：基本五五开，谁赢都不奇怪。
- **ROX Tigers vs EDward Gaming**：我的判断：ROX Tigers 晋级（系列赛胜率 56%，最可能比分 ROX Tigers 3:1）。 理由：ROX Tigers 整体硬实力更强（实力分高 58）。 风险点：老牌队伍经验更足：ROX Tigers 打过 162 局，EDward Gaming 打过 285 局。 位置对比：打野 peanut 近期表现优于 clearlove；上单 mouse 近期表现优于 smeb；辅助 meiko 近期表现优于 gorilla。 BP预测：ROX Tigers 的招牌英雄 Trundle、Ashe、Elise；EDward Gaming 的招牌英雄 Braum、Sivir、Gragas。ROX Tigers 应优先禁 Rek'Sai、Gragas、Sivir，EDward Gaming 大概率禁 Karma、Trundle、Jhin。 总结：基本五五开，谁赢都不奇怪。
- **Samsung Galaxy vs Cloud9**：我的判断：Samsung Galaxy 晋级（系列赛胜率 63%，最可能比分 Samsung Galaxy 3:1）。 主要依据：从长期战绩算出来的实力分看，Samsung Galaxy 领先 Cloud9 约 127 分；Samsung Galaxy 选手们对线期 KDA 压制更明显；Samsung Galaxy 最近手感比对手好（Samsung Galaxy 6-4，Cloud9 6-4，比赛结果都好于赛前预期）。 不过要注意：Cloud9 的职业比赛经验更多（Samsung Galaxy 179 局 / Cloud9 270 局）。 位置对比：中单 jensen 近期表现优于 crown；打野 meteos 近期表现优于 ambition；上单 impact 近期表现优于 cuvee。 BP预测：Samsung Galaxy 的招牌英雄 Sivir、Viktor、Rek'Sai；Cloud9 的招牌英雄 Rek'Sai、Gragas、Ashe。Samsung Galaxy 应优先禁 Sivir、Gragas、Rek'Sai，Cloud9 大概率禁 Gangplank、Ekko、Vladimir。 总结：有一定爆冷可能。
- **H2k-Gaming vs Albus NoX Luna**：我的判断：H2k-Gaming 晋级（系列赛胜率 74%，最可能比分 H2k-Gaming 3:1）。 理由：H2k-Gaming 整体硬实力更强（实力分高 262）；H2k-Gaming 的职业比赛经验更多（H2k-Gaming 161 局 / Albus NoX Luna 22 局）。 不过要注意：Albus NoX Luna 选手对位输出更高。 位置对比：打野 jankos 近期表现优于 pvpstejos；上单 smurf 近期表现优于 odoamne；辅助 likkrit 近期表现优于 vander。 BP预测：H2k-Gaming 的招牌英雄 Braum、Viktor、Karma；Albus NoX Luna 的招牌英雄 Rek'Sai、Bard、Trundle。H2k-Gaming 应优先禁 Rek'Sai、Sivir、Gragas，Albus NoX Luna 大概率禁 Vladimir、Shen、Gnar。 按当前版本强势英雄算，H2k-Gaming 的 BP 更占便宜。 总结：有一定爆冷可能。

### S7 2017 世界赛

训练数据截止：2017-09-23（之后的比赛模型都没见过）  
夺冠概率：Longzhu Gaming 22%，Fnatic 19%，T1 18%，Samsung Galaxy 12%  
**预测冠军：Longzhu Gaming**　｜　实际冠军：Samsung Galaxy ❌  
预测 4 强命中 1/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | T1 vs Misfits Gaming | T1 | 67% | T1 3-2 | ✅ |
| R1M2 | Royal Never Give Up vs Fnatic | Fnatic | 57% | Royal Never Give Up 3-1 | ❌ |
| R1M3 | Longzhu Gaming vs Samsung Galaxy | Longzhu Gaming | 59% | Samsung Galaxy 0-3 | ❌ |
| R1M4 | Team WE vs Cloud9 | Cloud9 | 54% | Team WE 3-2 | ❌ |
| R2M1 | T1 vs Royal Never Give Up | T1 | 57% | T1 3-2 | ✅ |
| R2M2 | Samsung Galaxy vs Team WE | Samsung Galaxy | 60% | Samsung Galaxy 3-1 | ✅ |
| R3M1 | T1 vs Samsung Galaxy | Samsung Galaxy | 51% | Samsung Galaxy 0-3 | ✅ |

**赛前观点（8 强）：**

- **T1 vs Misfits Gaming**：倾向 T1（系列赛胜率 67%，最可能比分 T1 3:1）。 主要依据：从长期战绩算出来的实力分看，T1 领先 Misfits Gaming 约 406 分；T1 的职业比赛经验更多（T1 437 局 / Misfits Gaming 119 局）。 不过要注意：Misfits Gaming 最近手感比对手好（T1 5-5，Misfits Gaming 6-4，比赛结果都好于赛前预期）。 位置对比：下路 bang 近期表现优于 hans sama；中单 powerofevil 近期表现优于 faker；打野 blank 近期表现优于 maxlore。 BP预测：T1 的招牌英雄 Ashe、Lulu、Alistar；Misfits Gaming 的招牌英雄 Varus、Orianna、Jarvan IV。T1 应优先禁 Jarvan IV、Kalista、Thresh，Misfits Gaming 大概率禁 Tristana、Cassiopeia、Taliyah。 总结：有一定爆冷可能。
- **Royal Never Give Up vs Fnatic**：倾向 Fnatic（系列赛胜率 57%，最可能比分 Fnatic 3:1）。 理由：近期状态：Royal Never Give Up 最近 5胜5负（状态一般），Fnatic 最近 7胜3负（状态不错）；Fnatic 资源控制更强（推塔、小龙、大龙拿得更多）。 但是：Royal Never Give Up 整体硬实力更强（实力分高 123）。 位置对比：中单 xiaohu 近期表现优于 caps；下路 rekkles 近期表现优于 uzi；打野 mlxg 近期表现优于 broxah。 BP预测：Royal Never Give Up 的招牌英雄 Gragas、Taliyah、Thresh；Fnatic 的招牌英雄 Gragas、Elise、Kennen。Royal Never Give Up 应优先禁 Jarvan IV、Gragas、Elise，Fnatic 大概率禁 Kalista、Cho'Gath、Taliyah。 总结：基本五五开，谁赢都不奇怪。
- **Longzhu Gaming vs Samsung Galaxy**：我看好 Longzhu Gaming（系列赛胜率 59%，最可能比分 Longzhu Gaming 3:1）。 为什么：Longzhu Gaming 选手对位输出更高；Longzhu Gaming 整体硬实力更强（实力分高 23）；Longzhu Gaming 最近手感比对手好（Longzhu Gaming 6-4，Samsung Galaxy 6-4，比赛结果都好于赛前预期）。 不过要注意：Samsung Galaxy 资源控制更强（推塔、小龙、大龙拿得更多）。 位置对比：中单 bdd 近期表现优于 crown；上单 khan 近期表现优于 cuvee；下路 pray 近期表现优于 ruler。 BP预测：Longzhu Gaming 的招牌英雄 Thresh、Ashe、Taliyah；Samsung Galaxy 的招牌英雄 Varus、Gragas、Karma。Longzhu Gaming 应优先禁 Jarvan IV、Kalista、Gragas，Samsung Galaxy 大概率禁 Thresh、Elise、Taliyah。 总结：基本五五开，谁赢都不奇怪。
- **Team WE vs Cloud9**：我的判断：Cloud9 晋级（系列赛胜率 54%，最可能比分 Cloud9 3:1）。 主要依据：Cloud9 选手对位输出更高。 但是：从长期战绩算出来的实力分看，Team WE 领先 Cloud9 约 94 分。 位置对比：中单 jensen 近期表现优于 xiye；打野 contractz 近期表现优于 condi；辅助 smoothie 近期表现优于 ben。 BP预测：Team WE 的招牌英雄 Jarvan IV、Gragas、Xayah；Cloud9 的招牌英雄 Orianna、Thresh、Syndra。Team WE 应优先禁 Gragas、Jarvan IV、Tristana，Cloud9 大概率禁 Kalista、Thresh、Maokai。 总结：基本五五开，谁赢都不奇怪。

### S8 2018 世界赛

训练数据截止：2018-10-01（之后的比赛模型都没见过）  
夺冠概率：Fnatic 20%，KT Rolster 19%，Invictus Gaming 19%，Royal Never Give Up 16%  
**预测冠军：Invictus Gaming**　｜　实际冠军：Invictus Gaming ✅  
预测 4 强命中 2/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Kwangdong Freecs vs Cloud9 | Kwangdong Freecs | 55% | Cloud9 0-3 | ❌ |
| R1M2 | Fnatic vs EDward Gaming | Fnatic | 66% | Fnatic 3-1 | ✅ |
| R1M3 | Royal Never Give Up vs G2 Esports | Royal Never Give Up | 65% | G2 Esports 2-3 | ❌ |
| R1M4 | KT Rolster vs Invictus Gaming | Invictus Gaming | 50% | Invictus Gaming 2-3 | ✅ |
| R2M1 | Cloud9 vs Fnatic | Fnatic | 63% | Fnatic 0-3 | ✅ |
| R2M2 | G2 Esports vs Invictus Gaming | Invictus Gaming | 70% | Invictus Gaming 0-3 | ✅ |
| R3M1 | Fnatic vs Invictus Gaming | Invictus Gaming | 53% | Invictus Gaming 0-3 | ✅ |

**赛前观点（8 强）：**

- **Kwangdong Freecs vs Cloud9**：我的判断：Kwangdong Freecs 晋级（系列赛胜率 55%，最可能比分 Kwangdong Freecs 3:1）。 理由：综合实力分 Kwangdong Freecs 比 Cloud9 高约 200 分。 但是：Cloud9 选手对位输出更高。 位置对比：打野 blaber 近期表现优于 spirit；中单 jensen 近期表现优于 kuro；上单 kiin 近期表现优于 licorice。 BP预测：Kwangdong Freecs 的招牌英雄 Alistar、Shen、Gragas；Cloud9 的招牌英雄 Braum、Zilean、Ornn。Kwangdong Freecs 应优先禁 Aatrox、Tahm Kench、Braum，Cloud9 大概率禁 Varus、Rakan、Gragas。 总结：基本五五开，谁赢都不奇怪。
- **Fnatic vs EDward Gaming**：我看好 Fnatic（系列赛胜率 66%，最可能比分 Fnatic 3:1）。 但是：EDward Gaming 最近手感比对手好（Fnatic 7-3，EDward Gaming 6-4，比赛结果都好于赛前预期）。 位置对比：中单 caps 近期表现优于 scout；下路 iboy 近期表现优于 rekkles；辅助 meiko 近期表现优于 hylissang。 BP预测：Fnatic 的招牌英雄 Pyke、Trundle、Sejuani；EDward Gaming 的招牌英雄 Kai'Sa、Tahm Kench、Varus。Fnatic 应优先禁 Tahm Kench、Ryze、Varus，EDward Gaming 大概率禁 Trundle、Gragas、Braum。 总结：有一定爆冷可能。
- **Royal Never Give Up vs G2 Esports**：我的判断：Royal Never Give Up 晋级（系列赛胜率 65%，最可能比分 Royal Never Give Up 3:1）。 为什么：Royal Never Give Up 整体硬实力更强（实力分高 242）；老牌队伍经验更足：Royal Never Give Up 打过 831 局，G2 Esports 打过 264 局。 不过要注意：G2 Esports 选手对位输出更高。 位置对比：下路 uzi 近期表现优于 hjarnan；辅助 ming 近期表现优于 wadid；打野 jankos 近期表现优于 mlxg。 BP预测：Royal Never Give Up 的招牌英雄 Shen、Tahm Kench、Kai'Sa；G2 Esports 的招牌英雄 Tahm Kench、Varus、Heimerdinger。Royal Never Give Up 应优先禁 Aatrox、Tahm Kench、Varus，G2 Esports 大概率禁 Trundle、Zoe、Kai'Sa。 总结：有一定爆冷可能。
- **KT Rolster vs Invictus Gaming**：我的判断：Invictus Gaming 晋级（系列赛胜率 50%，最可能比分 Invictus Gaming 3:1）。 理由：Invictus Gaming 选手对位输出更高。 风险点：近期状态：KT Rolster 最近 8胜2负（状态火热），Invictus Gaming 最近 5胜5负（状态一般）。 位置对比：中单 rookie 近期表现优于 ucal；下路 deft 近期表现优于 jackeylove；辅助 baolan 近期表现优于 mata。 BP预测：KT Rolster 的招牌英雄 Shen、Tahm Kench、Sejuani；Invictus Gaming 的招牌英雄 Tahm Kench、Alistar、Lucian。KT Rolster 应优先禁 Tahm Kench、Camille、Varus，Invictus Gaming 大概率禁 Rakan、Taliyah、Trundle。 总结：基本五五开，谁赢都不奇怪。

### S9 2019 世界赛

训练数据截止：2019-10-02（之后的比赛模型都没见过）  
夺冠概率：T1 24%，G2 Esports 24%，FunPlus Phoenix 23%，Fnatic 13%  
**预测冠军：FunPlus Phoenix**　｜　实际冠军：FunPlus Phoenix ✅  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | DWG KIA vs G2 Esports | G2 Esports | 70% | G2 Esports 1-3 | ✅ |
| R1M2 | T1 vs Splyce | T1 | 76% | T1 3-1 | ✅ |
| R1M3 | Griffin vs Invictus Gaming | Griffin | 63% | Invictus Gaming 1-3 | ❌ |
| R1M4 | FunPlus Phoenix vs Fnatic | FunPlus Phoenix | 57% | FunPlus Phoenix 3-1 | ✅ |
| R2M1 | G2 Esports vs T1 | G2 Esports | 52% | G2 Esports 3-1 | ✅ |
| R2M2 | Invictus Gaming vs FunPlus Phoenix | FunPlus Phoenix | 80% | FunPlus Phoenix 1-3 | ✅ |
| R3M1 | G2 Esports vs FunPlus Phoenix | FunPlus Phoenix | 52% | FunPlus Phoenix 0-3 | ✅ |

**赛前观点（8 强）：**

- **DWG KIA vs G2 Esports**：我的判断：G2 Esports 晋级（系列赛胜率 70%，最可能比分 G2 Esports 3:1）。 主要依据：从长期战绩算出来的实力分看，G2 Esports 领先 DWG KIA 约 101 分；G2 Esports 选手对位输出更高；近期状态：DWG KIA 最近 4胜6负（状态一般），G2 Esports 最近 6胜4负（状态不错）。 但是：DWG KIA 这批首发最近赢得更多。 位置对比：中单 caps 近期表现优于 showmaker；打野 jankos 近期表现优于 canyon；下路 perkz 近期表现优于 nuclear。 BP预测：DWG KIA 的招牌英雄 Kai'Sa、Jayce、Camille；G2 Esports 的招牌英雄 Sylas、Rakan、Xayah。DWG KIA 应优先禁 Sylas、Xayah、Akali，G2 Esports 大概率禁 Corki、Aatrox、Karma。 总结：有一定爆冷可能。
- **T1 vs Splyce**：倾向 T1（系列赛胜率 76%，最可能比分 T1 3:1）。 主要依据：T1 整体硬实力更强（实力分高 234）；T1 选手对位输出更高；T1 最近手感比对手好（T1 9-1，Splyce 6-4，比赛结果都好于赛前预期）。 但是：Splyce 选手们对线期 KDA 压制更明显。 位置对比：下路 teddy 近期表现优于 kobbe；辅助 effort 近期表现优于 tore；打野 clid 近期表现优于 xerxe。 BP预测：T1 的招牌英雄 Aatrox、Varus、Akali；Splyce 的招牌英雄 Gangplank、Kai'Sa、Sylas。T1 应优先禁 Sylas、Akali、Corki，Splyce 大概率禁 Aatrox、Xayah、Rakan。 按当前版本强势英雄算，Splyce 的 BP 更占便宜。 总结：有一定爆冷可能。
- **Griffin vs Invictus Gaming**：我看好 Griffin（系列赛胜率 63%，最可能比分 Griffin 3:1）。 理由：从长期战绩算出来的实力分看，Griffin 领先 Invictus Gaming 约 26 分；Griffin 资源控制更强（推塔、小龙、大龙拿得更多）。 风险点：Invictus Gaming 的职业比赛经验更多（Griffin 271 局 / Invictus Gaming 710 局）。 位置对比：打野 tarzan 近期表现优于 leyan；下路 viper 近期表现优于 jackeylove；中单 chovy 近期表现优于 rookie。 BP预测：Griffin 的招牌英雄 Sejuani、Ezreal、Tahm Kench；Invictus Gaming 的招牌英雄 Sylas、Kai'Sa、Kennen。Griffin 应优先禁 Sylas、Gragas、Akali，Invictus Gaming 大概率禁 Aatrox、Sejuani、Tahm Kench。 总结：有一定爆冷可能。
- **FunPlus Phoenix vs Fnatic**：倾向 FunPlus Phoenix（系列赛胜率 57%，最可能比分 FunPlus Phoenix 3:1）。 为什么：从长期战绩算出来的实力分看，FunPlus Phoenix 领先 Fnatic 约 151 分；FunPlus Phoenix 选手对位输出更高；FunPlus Phoenix 资源控制更强（推塔、小龙、大龙拿得更多）。 但是：老牌队伍经验更足：FunPlus Phoenix 打过 187 局，Fnatic 打过 656 局。 位置对比：打野 tian 近期表现优于 broxah；下路 lwx 近期表现优于 rekkles；中单 doinb 近期表现优于 nemesis。 BP预测：FunPlus Phoenix 的招牌英雄 Nautilus、Sylas、Lucian；Fnatic 的招牌英雄 Aatrox、Rakan、Gragas。FunPlus Phoenix 应优先禁 Aatrox、Gragas、Sylas，Fnatic 大概率禁 Kai'Sa、Nautilus、Tahm Kench。 总结：基本五五开，谁赢都不奇怪。

### S10 2020 世界赛

训练数据截止：2020-09-25（之后的比赛模型都没见过）  
夺冠概率：DWG KIA 43%，Gen.G 16%，Top Esports 15%，G2 Esports 8%  
**预测冠军：DWG KIA**　｜　实际冠军：DWG KIA ✅  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Top Esports vs Fnatic | Top Esports | 63% | Top Esports 3-2 | ✅ |
| R1M2 | Suning vs JD Gaming | Suning | 53% | Suning 3-1 | ✅ |
| R1M3 | Gen.G vs G2 Esports | Gen.G | 60% | G2 Esports 0-3 | ❌ |
| R1M4 | DWG KIA vs DRX | DWG KIA | 90% | DWG KIA 3-0 | ✅ |
| R2M1 | Top Esports vs Suning | Top Esports | 64% | Suning 1-3 | ❌ |
| R2M2 | G2 Esports vs DWG KIA | DWG KIA | 67% | DWG KIA 1-3 | ✅ |
| R3M1 | Suning vs DWG KIA | DWG KIA | 77% | DWG KIA 1-3 | ✅ |

**赛前观点（8 强）：**

- **Top Esports vs Fnatic**：倾向 Top Esports（系列赛胜率 63%，最可能比分 Top Esports 3:1）。 主要依据：从长期战绩算出来的实力分看，Top Esports 领先 Fnatic 约 155 分；近期状态：Top Esports 最近 8胜2负（状态火热），Fnatic 最近 5胜5负（状态一般）；Top Esports 选手对位输出更高。 但是：Fnatic 的职业比赛经验更多（Top Esports 160 局 / Fnatic 723 局）。 位置对比：下路 jackeylove 近期表现优于 rekkles；打野 selfmade 近期表现优于 karsa；上单 369 近期表现优于 bwipo。 BP预测：Top Esports 的招牌英雄 Lee Sin、Syndra、Renekton；Fnatic 的招牌英雄 Senna、Ornn、Gragas。Top Esports 应优先禁 Thresh、Senna、Sett，Fnatic 大概率禁 Renekton、Zoe、Syndra。 按当前版本强势英雄算，Fnatic 的 BP 更占便宜。 总结：有一定爆冷可能。
- **Suning vs JD Gaming**：倾向 Suning（系列赛胜率 53%，最可能比分 Suning 3:1）。 理由：近期状态：Suning 最近 7胜3负（状态不错），JD Gaming 最近 6胜4负（状态不错）。 但是：JD Gaming 整体硬实力更强（实力分高 30）。 位置对比：打野 kanavi 近期表现优于 sofm；辅助 lvmao 近期表现优于 swordart；下路 loken 近期表现优于 huanfeng。 BP预测：Suning 的招牌英雄 Syndra、Renekton、Lee Sin；JD Gaming 的招牌英雄 Ornn、Aphelios、Lee Sin。Suning 应优先禁 Sett、Bard、Zoe，JD Gaming 大概率禁 Renekton、Ashe、Graves。 总结：基本五五开，谁赢都不奇怪。
- **Gen.G vs G2 Esports**：我看好 Gen.G（系列赛胜率 60%，最可能比分 Gen.G 3:1）。 理由：从长期战绩算出来的实力分看，Gen.G 领先 G2 Esports 约 71 分；Gen.G 选手对位输出更高；Gen.G 资源控制更强（推塔、小龙、大龙拿得更多）。 不过要注意：G2 Esports 选手们对线期 KDA 压制更明显。 位置对比：下路 ruler 近期表现优于 perkz；打野 clid 近期表现优于 jankos；辅助 life 近期表现优于 mikyx。 BP预测：Gen.G 的招牌英雄 Azir、Ezreal、Ornn；G2 Esports 的招牌英雄 Sett、Nautilus、Ashe。Gen.G 应优先禁 Sett、Ashe、Zoe，G2 Esports 大概率禁 Renekton、Volibear、Nidalee。 按当前版本强势英雄算，G2 Esports 的 BP 更占便宜。 总结：基本五五开，谁赢都不奇怪。
- **DWG KIA vs DRX**：我的判断：DWG KIA 晋级（系列赛胜率 90%，最可能比分 DWG KIA 3:0）。 为什么：综合实力分 DWG KIA 比 DRX 高约 177 分；DWG KIA 选手对位输出更高；近期状态：DWG KIA 最近 10胜0负（状态火热），DRX 最近 3胜7负（状态低迷）。 但是：DRX 这批首发最近赢得更多。 位置对比：上单 nuguri 近期表现优于 doran；中单 showmaker 近期表现优于 chovy；打野 canyon 近期表现优于 pyosik。 BP预测：DWG KIA 的招牌英雄 Sett、Jayce、Ezreal；DRX 的招牌英雄 Azir、Ezreal、Aatrox。DWG KIA 应优先禁 Sett、Volibear、Ashe，DRX 大概率禁 Renekton、Zoe、Thresh。 总结：爆冷概率很低。

### S11 2021 世界赛

训练数据截止：2021-10-05（之后的比赛模型都没见过）  
夺冠概率：EDward Gaming 37%，DWG KIA 27%，MAD Lions 20%，Cloud9 5%  
**预测冠军：DWG KIA**　｜　实际冠军：EDward Gaming ❌  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Royal Never Give Up vs EDward Gaming | EDward Gaming | 84% | EDward Gaming 2-3 | ✅ |
| R1M2 | Gen.G vs Cloud9 | Cloud9 | 59% | Gen.G 3-0 | ❌ |
| R1M3 | T1 vs Hanwha Life Esports | T1 | 58% | T1 3-0 | ✅ |
| R1M4 | DWG KIA vs MAD Lions | DWG KIA | 53% | DWG KIA 3-0 | ✅ |
| R2M1 | EDward Gaming vs Gen.G | EDward Gaming | 82% | EDward Gaming 3-2 | ✅ |
| R2M2 | T1 vs DWG KIA | DWG KIA | 81% | DWG KIA 2-3 | ✅ |
| R3M1 | EDward Gaming vs DWG KIA | DWG KIA | 51% | EDward Gaming 3-2 | ❌ |

**赛前观点（8 强）：**

- **Royal Never Give Up vs EDward Gaming**：我看好 EDward Gaming（系列赛胜率 84%，最可能比分 EDward Gaming 3:0）。 主要依据：EDward Gaming 整体硬实力更强（实力分高 152）；EDward Gaming 最近手感比对手好（Royal Never Give Up 5-5，EDward Gaming 8-2，比赛结果都好于赛前预期）；EDward Gaming 选手对位输出更高。 位置对比：下路 viper 近期表现优于 such；中单 scout 近期表现优于 lover11；辅助 lele 近期表现优于 meiko。 BP预测：Royal Never Give Up 的招牌英雄 Gnar、Thresh、Viego；EDward Gaming 的招牌英雄 Lee Sin、Sylas、Leona。Royal Never Give Up 应优先禁 Lee Sin、Renekton、Xin Zhao，EDward Gaming 大概率禁 Viego、Leona、LeBlanc。 总结：爆冷概率很低。
- **Gen.G vs Cloud9**：我看好 Cloud9（系列赛胜率 59%，最可能比分 Cloud9 3:1）。 主要依据：Cloud9 选手对位输出更高；Cloud9 整体硬实力更强（实力分高 18）；Cloud9 资源控制更强（推塔、小龙、大龙拿得更多）。 风险点：Gen.G 这批首发最近赢得更多。 位置对比：下路 zven 近期表现优于 ruler；打野 blaber 近期表现优于 clid；辅助 vulcan 近期表现优于 life。 BP预测：Gen.G 的招牌英雄 Volibear、Lee Sin、Leona；Cloud9 的招牌英雄 Varus、Lee Sin、Nautilus。Gen.G 应优先禁 Lee Sin、Xin Zhao、Viego，Cloud9 大概率禁 Leona、Renekton、Thresh。 按当前版本强势英雄算，Gen.G 的 BP 更占便宜。 总结：基本五五开，谁赢都不奇怪。
- **T1 vs Hanwha Life Esports**：我看好 T1（系列赛胜率 58%，最可能比分 T1 3:1）。 为什么：T1 整体硬实力更强（实力分高 41）；老牌队伍经验更足：T1 打过 927 局，Hanwha Life Esports 打过 351 局。 不过要注意：近期状态：T1 最近 5胜5负（状态一般），Hanwha Life Esports 最近 7胜3负（状态不错）。 位置对比：中单 chovy 近期表现优于 faker；上单 canna 近期表现优于 morgan；下路 deft 近期表现优于 gumayusi。 BP预测：T1 的招牌英雄 Leona、Viego、Ryze；Hanwha Life Esports 的招牌英雄 Varus、Viego、Lee Sin。T1 应优先禁 Lee Sin、Viego、Varus，Hanwha Life Esports 大概率禁 Jayce、Leona、Xin Zhao。 总结：基本五五开，谁赢都不奇怪。
- **DWG KIA vs MAD Lions**：我看好 DWG KIA（系列赛胜率 53%，最可能比分 DWG KIA 3:1）。 主要依据：DWG KIA 选手对位输出更高；DWG KIA 的职业比赛经验更多（DWG KIA 499 局 / MAD Lions 150 局）。 不过要注意：综合实力分 MAD Lions 比 DWG KIA 高约 29 分。 位置对比：打野 canyon 近期表现优于 elyoya；下路 ghost 近期表现优于 carzzy；中单 showmaker 近期表现优于 humanoid。 BP预测：DWG KIA 的招牌英雄 Ryze、Leona、Varus；MAD Lions 的招牌英雄 Leona、Lee Sin、Ezreal。DWG KIA 应优先禁 Lee Sin、Viego、Leona，MAD Lions 大概率禁 LeBlanc、Jayce、Renekton。 总结：基本五五开，谁赢都不奇怪。

### S12 2022 世界赛

训练数据截止：2022-10-20（之后的比赛模型都没见过）  
夺冠概率：Gen.G 45%，JD Gaming 15%，Royal Never Give Up 12%，DWG KIA 8%  
**预测冠军：Gen.G**　｜　实际冠军：DRX ❌  
预测 4 强命中 3/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | JD Gaming vs Rogue | JD Gaming | 72% | JD Gaming 3-0 | ✅ |
| R1M2 | Royal Never Give Up vs T1 | Royal Never Give Up | 54% | T1 0-3 | ❌ |
| R1M3 | DRX vs EDward Gaming | DRX | 54% | DRX 3-2 | ✅ |
| R1M4 | DWG KIA vs Gen.G | Gen.G | 74% | Gen.G 2-3 | ✅ |
| R2M1 | JD Gaming vs T1 | JD Gaming | 58% | T1 1-3 | ❌ |
| R2M2 | DRX vs Gen.G | Gen.G | 78% | DRX 3-1 | ❌ |
| R3M1 | DRX vs T1 | DRX | 55% | DRX 3-2 | ✅ |

**赛前观点（8 强）：**

- **JD Gaming vs Rogue**：我看好 JD Gaming（系列赛胜率 72%，最可能比分 JD Gaming 3:1）。 理由：综合实力分 JD Gaming 比 Rogue 高约 253 分；JD Gaming 最近手感比对手好（JD Gaming 8-2，Rogue 7-3，比赛结果都好于赛前预期）；老牌队伍经验更足：JD Gaming 打过 599 局，Rogue 打过 246 局。 风险点：Rogue 这批首发最近赢得更多。 位置对比：中单 larssen 近期表现优于 yagao；下路 comp 近期表现优于 hope；上单 369 近期表现优于 odoamne。 BP预测：JD Gaming 的招牌英雄 Ahri、Aphelios、Taliyah；Rogue 的招牌英雄 Jarvan IV、Renekton、Azir。JD Gaming 应优先禁 Wukong、Azir、Ahri，Rogue 大概率禁 Zeri、Kalista、Taliyah。 总结：有一定爆冷可能。
- **Royal Never Give Up vs T1**：我看好 Royal Never Give Up（系列赛胜率 54%，最可能比分 Royal Never Give Up 3:1）。 理由：Royal Never Give Up 选手对位输出更高；Royal Never Give Up 资源控制更强（推塔、小龙、大龙拿得更多）。 风险点：T1 整体硬实力更强（实力分高 80）。 位置对比：下路 gala 近期表现优于 gumayusi；打野 wei 近期表现优于 oner；中单 xiaohu 近期表现优于 faker。 BP预测：Royal Never Give Up 的招牌英雄 Nautilus、Viego、Aphelios；T1 的招牌英雄 Lee Sin、Gnar、Azir。Royal Never Give Up 应优先禁 Wukong、Zeri、Azir，T1 大概率禁 Ahri、Vi、Taliyah。 总结：基本五五开，谁赢都不奇怪。
- **DRX vs EDward Gaming**：我的判断：DRX 晋级（系列赛胜率 54%，最可能比分 DRX 3:1）。 主要依据：DRX 整体硬实力更强（实力分高 72）；DRX 选手对位输出更高；DRX 最近手感比对手好（DRX 8-2，EDward Gaming 7-3，比赛结果都好于赛前预期）。 但是：EDward Gaming 这批首发最近赢得更多。 位置对比：中单 zeka 近期表现优于 scout；下路 deft 近期表现优于 viper；辅助 beryl 近期表现优于 meiko。 BP预测：DRX 的招牌英雄 Ahri、Gnar、Viego；EDward Gaming 的招牌英雄 Azir、Gnar、Aphelios。DRX 应优先禁 Wukong、Zeri、Sylas，EDward Gaming 大概率禁 Kalista、Poppy、Sivir。 总结：基本五五开，谁赢都不奇怪。
- **DWG KIA vs Gen.G**：我的判断：Gen.G 晋级（系列赛胜率 74%，最可能比分 Gen.G 3:1）。 主要依据：从长期战绩算出来的实力分看，Gen.G 领先 DWG KIA 约 166 分。 但是：DWG KIA 这批首发最近赢得更多。 位置对比：下路 ruler 近期表现优于 deokdam；上单 doran 近期表现优于 nuguri；辅助 lehends 近期表现优于 kellin。 BP预测：DWG KIA 的招牌英雄 Sejuani、Wukong、Aphelios；Gen.G 的招牌英雄 Gnar、Azir、Wukong。DWG KIA 应优先禁 Wukong、Zeri、Azir，Gen.G 大概率禁 Sylas、Taliyah、Poppy。 总结：有一定爆冷可能。

### S13 2023 世界赛

训练数据截止：2023-11-03（之后的比赛模型都没见过）  
夺冠概率：Gen.G 37%，JD Gaming 31%，LNG Esports 8%，Weibo Gaming 8%  
**预测冠军：JD Gaming**　｜　实际冠军：T1 ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Bilibili Gaming vs Gen.G | Gen.G | 77% | Bilibili Gaming 3-2 | ❌ |
| R1M2 | NRG Esports vs Weibo Gaming | Weibo Gaming | 67% | Weibo Gaming 0-3 | ✅ |
| R1M3 | JD Gaming vs KT Rolster | JD Gaming | 70% | JD Gaming 3-1 | ✅ |
| R1M4 | LNG Esports vs T1 | LNG Esports | 54% | T1 0-3 | ❌ |
| R2M1 | Bilibili Gaming vs Weibo Gaming | Weibo Gaming | 66% | Weibo Gaming 2-3 | ✅ |
| R2M2 | JD Gaming vs T1 | JD Gaming | 71% | T1 1-3 | ❌ |
| R3M1 | T1 vs Weibo Gaming | T1 | 55% | T1 3-0 | ✅ |

**赛前观点（8 强）：**

- **Bilibili Gaming vs Gen.G**：我的判断：Gen.G 晋级（系列赛胜率 77%，最可能比分 Gen.G 3:1）。 为什么：从长期战绩算出来的实力分看，Gen.G 领先 Bilibili Gaming 约 161 分；Gen.G 选手对位输出更高；近期状态：Bilibili Gaming 最近 4胜6负（状态一般），Gen.G 最近 9胜1负（状态火热）。 不过要注意：Bilibili Gaming 这批首发最近赢得更多。 位置对比：打野 peanut 近期表现优于 xun；辅助 delight 近期表现优于 on；上单 doran 近期表现优于 bin。 BP预测：Bilibili Gaming 的招牌英雄 Aphelios、Annie、K'Sante；Gen.G 的招牌英雄 Jax、Maokai、Kai'Sa。Bilibili Gaming 应优先禁 Maokai、Rakan、Kai'Sa，Gen.G 大概率禁 Neeko、Xayah、Nautilus。 按当前版本强势英雄算，Gen.G 的 BP 更占便宜。 总结：有一定爆冷可能。
- **NRG Esports vs Weibo Gaming**：倾向 Weibo Gaming（系列赛胜率 67%，最可能比分 Weibo Gaming 3:1）。 理由：从长期战绩算出来的实力分看，Weibo Gaming 领先 NRG Esports 约 209 分；Weibo Gaming 选手对位输出更高；近期状态：NRG Esports 最近 6胜4负（状态不错），Weibo Gaming 最近 7胜3负（状态不错）。 不过要注意：NRG Esports 这批首发最近赢得更多。 位置对比：上单 theshy 近期表现优于 dhokla；下路 light 近期表现优于 fbi；辅助 crisp 近期表现优于 ignar。 BP预测：NRG Esports 的招牌英雄 Rell、Kai'Sa、Renekton；Weibo Gaming 的招牌英雄 Aphelios、K'Sante、Azir。NRG Esports 应优先禁 Rakan、Tristana、Maokai，Weibo Gaming 大概率禁 Rell、Renekton、Xayah。 总结：有一定爆冷可能。
- **JD Gaming vs KT Rolster**：我的判断：JD Gaming 晋级（系列赛胜率 70%，最可能比分 JD Gaming 3:1）。 为什么：从长期战绩算出来的实力分看，JD Gaming 领先 KT Rolster 约 75 分；JD Gaming 选手对位输出更高。 位置对比：下路 ruler 近期表现优于 aiming；辅助 missing 近期表现优于 lehends；打野 kanavi 近期表现优于 cuzz。 BP预测：JD Gaming 的招牌英雄 Xayah、Rakan、Ornn；KT Rolster 的招牌英雄 Renekton、Viego、Nautilus。JD Gaming 应优先禁 Rakan、Kai'Sa、Nautilus，KT Rolster 大概率禁 Xayah、Rell、Aphelios。 总结：有一定爆冷可能。
- **LNG Esports vs T1**：我的判断：LNG Esports 晋级（系列赛胜率 54%，最可能比分 LNG Esports 3:1）。 理由：从长期战绩算出来的实力分看，LNG Esports 领先 T1 约 30 分。 不过要注意：T1 选手对位输出更高。 位置对比：下路 gala 近期表现优于 gumayusi；中单 scout 近期表现优于 faker；打野 tarzan 近期表现优于 oner。 BP预测：LNG Esports 的招牌英雄 Xayah、Nautilus、Maokai；T1 的招牌英雄 Xayah、Azir、Maokai。LNG Esports 应优先禁 Xayah、Rakan、Maokai，T1 大概率禁 Neeko、Jax、Jayce。 总结：基本五五开，谁赢都不奇怪。

### S14 2024 世界赛

训练数据截止：2024-10-18（之后的比赛模型都没见过）  
夺冠概率：Gen.G 47%，Bilibili Gaming 22%，Hanwha Life Esports 12%，Top Esports 7%  
**预测冠军：Gen.G**　｜　实际冠军：T1 ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Bilibili Gaming vs Hanwha Life Esports | Bilibili Gaming | 54% | Bilibili Gaming 3-1 | ✅ |
| R1M2 | LNG Esports vs Weibo Gaming | Weibo Gaming | 63% | Weibo Gaming 1-3 | ✅ |
| R1M3 | FlyQuest vs Gen.G | Gen.G | 83% | Gen.G 2-3 | ✅ |
| R1M4 | T1 vs Top Esports | Top Esports | 56% | T1 3-0 | ❌ |
| R2M1 | Bilibili Gaming vs Weibo Gaming | Bilibili Gaming | 79% | Bilibili Gaming 3-0 | ✅ |
| R2M2 | Gen.G vs T1 | Gen.G | 83% | T1 1-3 | ❌ |
| R3M1 | Bilibili Gaming vs T1 | Bilibili Gaming | 68% | T1 2-3 | ❌ |

**赛前观点（8 强）：**

- **Bilibili Gaming vs Hanwha Life Esports**：我的判断：Bilibili Gaming 晋级（系列赛胜率 54%，最可能比分 Bilibili Gaming 3:1）。 主要依据：Bilibili Gaming 选手对位输出更高。 不过要注意：综合实力分 Hanwha Life Esports 比 Bilibili Gaming 高约 64 分。 位置对比：中单 knight 近期表现优于 zeka；上单 bin 近期表现优于 doran；下路 elk 近期表现优于 viper。 BP预测：Bilibili Gaming 的招牌英雄 Corki、Rell、Renekton；Hanwha Life Esports 的招牌英雄 Sejuani、Alistar、Rell。Bilibili Gaming 应优先禁 Rumble、Rell、Maokai，Hanwha Life Esports 大概率禁 Ezreal、Renekton、Kennen。 总结：基本五五开，谁赢都不奇怪。
- **LNG Esports vs Weibo Gaming**：我看好 Weibo Gaming（系列赛胜率 63%，最可能比分 Weibo Gaming 3:1）。 主要依据：Weibo Gaming 选手对位输出更高；Weibo Gaming 最近手感比对手好（LNG Esports 7-3，Weibo Gaming 7-3，比赛结果都好于赛前预期）；综合实力分 Weibo Gaming 比 LNG Esports 高约 8 分。 位置对比：中单 xiaohu 近期表现优于 scout；下路 gala 近期表现优于 light。 BP预测：LNG Esports 的招牌英雄 Ezreal、K'Sante、Corki；Weibo Gaming 的招牌英雄 Renekton、Ezreal、Brand。LNG Esports 应优先禁 Rell、Rumble、Maokai，Weibo Gaming 大概率禁 Corki、Leona、Lillia。 按当前版本强势英雄算，Weibo Gaming 的 BP 更占便宜。 总结：有一定爆冷可能。
- **FlyQuest vs Gen.G**：我的判断：Gen.G 晋级（系列赛胜率 83%，最可能比分 Gen.G 3:0）。 理由：从长期战绩算出来的实力分看，Gen.G 领先 FlyQuest 约 401 分；Gen.G 选手对位输出更高。 但是：近期状态：FlyQuest 最近 6胜4负（状态不错），Gen.G 最近 6胜4负（状态不错）。 位置对比：下路 peyz 近期表现优于 massu；上单 kiin 近期表现优于 bwipo；中单 chovy 近期表现优于 quad。 BP预测：FlyQuest 的招牌英雄 Renekton、Corki、Leona；Gen.G 的招牌英雄 Corki、K'Sante、Nidalee。FlyQuest 应优先禁 Maokai、Corki、Ashe，Gen.G 大概率禁 Lillia、Rumble、Renekton。 按当前版本强势英雄算，Gen.G 的 BP 更占便宜。 总结：爆冷概率很低。
- **T1 vs Top Esports**：我的判断：Top Esports 晋级（系列赛胜率 56%，最可能比分 Top Esports 3:1）。 但是：pool。 位置对比：中单 creme 近期表现优于 faker；上单 zeus 近期表现优于 369；打野 oner 近期表现优于 tian。 BP预测：T1 的招牌英雄 Sejuani、Corki、Azir；Top Esports 的招牌英雄 Ezreal、Leona、Corki。T1 应优先禁 Corki、Rumble、Lillia，Top Esports 大概率禁 Rell、Ashe、Azir。 总结：基本五五开，谁赢都不奇怪。

### S15 2025 世界赛

训练数据截止：2025-10-28（之后的比赛模型都没见过）  
夺冠概率：Gen.G 36%，Hanwha Life Esports 23%，T1 20%，KT Rolster 7%  
**预测冠军：Gen.G**　｜　实际冠军：T1 ❌  
预测 4 强命中 4/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Gen.G vs Hanwha Life Esports | Gen.G | 58% | Gen.G 3-1 | ✅ |
| R1M2 | CTBC Flying Oyster vs KT Rolster | KT Rolster | 85% | KT Rolster 0-3 | ✅ |
| R1M3 | Anyone's Legend vs T1 | T1 | 69% | T1 2-3 | ✅ |
| R1M4 | G2 Esports vs Top Esports | Top Esports | 53% | Top Esports 1-3 | ✅ |
| R2M1 | Gen.G vs KT Rolster | Gen.G | 84% | KT Rolster 1-3 | ❌ |
| R2M2 | T1 vs Top Esports | T1 | 71% | T1 3-0 | ✅ |
| R3M1 | KT Rolster vs T1 | T1 | 70% | T1 2-3 | ✅ |

**赛前观点（8 强）：**

- **Gen.G vs Hanwha Life Esports**：我看好 Gen.G（系列赛胜率 58%，最可能比分 Gen.G 3:1）。 理由：综合实力分 Gen.G 比 Hanwha Life Esports 高约 73 分。 风险点：Hanwha Life Esports 选手对位输出更高。 位置对比：下路 viper 近期表现优于 ruler；中单 chovy 近期表现优于 zeka；辅助 duro 近期表现优于 delight。 BP预测：Gen.G 的招牌英雄 Gwen、Corki、Xin Zhao；Hanwha Life Esports 的招牌英雄 Rell、Taliyah、Ambessa。Gen.G 应优先禁 Taliyah、Poppy、Rumble，Hanwha Life Esports 大概率禁 Neeko、Rakan、Pantheon。 总结：基本五五开，谁赢都不奇怪。
- **CTBC Flying Oyster vs KT Rolster**：倾向 KT Rolster（系列赛胜率 85%，最可能比分 KT Rolster 3:0）。 理由：KT Rolster 整体硬实力更强（实力分高 432）；近期状态：CTBC Flying Oyster 最近 6胜4负（状态不错），KT Rolster 最近 4胜6负（状态一般）；KT Rolster 的职业比赛经验更多（CTBC Flying Oyster 346 局 / KT Rolster 1213 局）。 但是：CTBC Flying Oyster 选手对位输出更高。 位置对比：下路 doggo 近期表现优于 deokdam；辅助 kaiwing 近期表现优于 peter；中单 hongq 近期表现优于 bdd。 BP预测：CTBC Flying Oyster 的招牌英雄 Kai'Sa、Ezreal、Wukong；KT Rolster 的招牌英雄 Ryze、Trundle、Alistar。CTBC Flying Oyster 应优先禁 Rumble、Wukong、Rakan，KT Rolster 大概率禁 Azir、Neeko、Annie。 总结：爆冷概率很低。
- **Anyone's Legend vs T1**：倾向 T1（系列赛胜率 68%，最可能比分 T1 3:1）。 主要依据：T1 整体硬实力更强（实力分高 212）；T1 选手们对线期 KDA 压制更明显；老牌队伍经验更足：Anyone's Legend 打过 431 局，T1 打过 1573 局。 不过要注意：Anyone's Legend 选手对位输出更高。 位置对比：中单 shanks 近期表现优于 faker；打野 tarzan 近期表现优于 oner；辅助 kael 近期表现优于 keria。 BP预测：Anyone's Legend 的招牌英雄 Sion、Annie、Pantheon；T1 的招牌英雄 Jhin、Xin Zhao、Gwen。Anyone's Legend 应优先禁 Poppy、Rumble、Orianna，T1 大概率禁 Azir、Pantheon、Annie。 总结：有一定爆冷可能。
- **G2 Esports vs Top Esports**：倾向 Top Esports（系列赛胜率 53%，最可能比分 Top Esports 3:1）。 为什么：Top Esports 选手对位输出更高；Top Esports 选手们对线期 KDA 压制更明显；Top Esports 这批首发最近赢得更多。 但是：综合实力分 G2 Esports 比 Top Esports 高约 20 分。 位置对比：辅助 labrov 近期表现优于 hang；打野 skewmond 近期表现优于 kanavi；下路 hans sama 近期表现优于 jackeylove。 BP预测：G2 Esports 的招牌英雄 Alistar、Jax、Taliyah；Top Esports 的招牌英雄 Xin Zhao、Azir、Rumble。G2 Esports 应优先禁 Rumble、Azir、Alistar，Top Esports 大概率禁 Taliyah、Poppy、Yunara。 总结：基本五五开，谁赢都不奇怪。
