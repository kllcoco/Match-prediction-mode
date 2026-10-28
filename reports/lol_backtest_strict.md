# 英雄联盟世界赛 S1-S15 回测 · 严格模式（训练时不看任何世界赛/MSI/Major）

- 系列赛预测命中率：**57.9%**（107 场；瞎猜 50%）
- 4 强命中：62.5%　决赛队伍命中：39.3%　冠军命中：**28.6%**（瞎猜 12.5%）
- 对真实冠军给出的平均夺冠概率：19.6%　对数损失：0.712（越低越好，瞎猜 0.693）

### S1 2011 世界赛

训练数据截止：2011-06-18（之后的比赛模型都没见过）  
（特殊赛制）预测冠军：against all authority，实际：Fnatic ❌

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | against all authority vs team gamed!de | against all authority | 50% | against all authority 2-0 | ✅ |
| R1M2 | Counter Logic Gaming vs Fnatic | Counter Logic Gaming | 50% | Fnatic 1-2 | ❌ |
| R2M1 | TSM vs against all authority | TSM | 50% | against all authority 1-2 | ❌ |
| R2M2 | epik gamer vs Fnatic | epik gamer | 50% | Fnatic 0-2 | ❌ |
| R3M1 | against all authority vs Fnatic | against all authority | 50% | Fnatic 0-2 | ❌ |
| R2M3 | TSM vs epik gamer | TSM | 50% | TSM 2-0 | ✅ |
| R3M2 | against all authority vs TSM | against all authority | 50% | against all authority 2-0 | ✅ |
| R4M1 | Fnatic vs against all authority | Fnatic | 50% | Fnatic 2-1 | ✅ |
| R1M1 | team gamed!de vs Counter Logic Gaming | team gamed!de | 50% | Counter Logic Gaming 0-1 | ❌ |

### S2 2012 世界赛

训练数据截止：2012-10-04（之后的比赛模型都没见过）  
夺冠概率：counter logic gaming europe 24%，TSM 17%，najin sword 14%，azubu frost 12%  
**预测冠军：counter logic gaming europe**　｜　实际冠军：tpa ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | moscow five vs Invictus Gaming | moscow five | 55% | moscow five 2-0 | ✅ |
| R1M2 | tpa vs najin sword | najin sword | 56% | tpa 2-0 | ❌ |
| R1M3 | TSM vs azubu frost | TSM | 54% | azubu frost 0-2 | ❌ |
| R1M4 | Team WE vs counter logic gaming europe | counter logic gaming europe | 63% | counter logic gaming europe 1-2 | ✅ |
| R2M1 | moscow five vs tpa | moscow five | 51% | tpa 1-2 | ❌ |
| R2M2 | azubu frost vs counter logic gaming europe | counter logic gaming europe | 59% | azubu frost 2-1 | ❌ |
| R3M1 | tpa vs azubu frost | azubu frost | 59% | tpa 3-1 | ❌ |

**赛前观点（8 强）：**

- **moscow five vs Invictus Gaming**：我看好 moscow five（系列赛胜率 55%，最可能比分 moscow five 2:0）。 理由：moscow five 整体硬实力更强（实力分高 21）。 总结：基本五五开，谁赢都不奇怪。
- **tpa vs najin sword**：倾向 najin sword（系列赛胜率 56%，最可能比分 najin sword 2:0）。 理由：综合实力分 najin sword 比 tpa 高约 26 分。 总结：基本五五开，谁赢都不奇怪。
- **TSM vs azubu frost**：倾向 TSM（系列赛胜率 54%，最可能比分 TSM 2:0）。 主要依据：TSM 整体硬实力更强（实力分高 17）。 总结：基本五五开，谁赢都不奇怪。
- **Team WE vs counter logic gaming europe**：我的判断：counter logic gaming europe 晋级（系列赛胜率 63%，最可能比分 counter logic gaming europe 2:0）。 主要依据：counter logic gaming europe 整体硬实力更强（实力分高 61）。 总结：有一定爆冷可能。

### S3 2013 世界赛

训练数据截止：2013-09-15（之后的比赛模型都没见过）  
夺冠概率：najin sword 27%，Cloud9 17%，Oh My God 16%，Fnatic 11%  
**预测冠军：najin sword**　｜　实际冠军：T1 ❌  
预测 4 强命中 2/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | gamania bears vs T1 | T1 | 63% | T1 0-2 | ✅ |
| R1M2 | najin sword vs Gambit Esports | najin sword | 61% | najin sword 2-1 | ✅ |
| R1M3 | Royal Never Give Up vs Oh My God | Oh My God | 62% | Royal Never Give Up 2-0 | ❌ |
| R1M4 | Cloud9 vs Fnatic | Cloud9 | 56% | Fnatic 1-2 | ❌ |
| R2M1 | T1 vs najin sword | najin sword | 76% | T1 3-2 | ❌ |
| R2M2 | Royal Never Give Up vs Fnatic | Fnatic | 54% | Royal Never Give Up 3-1 | ❌ |
| R3M1 | T1 vs Royal Never Give Up | T1 | 56% | T1 3-0 | ✅ |

**赛前观点（8 强）：**

- **gamania bears vs T1**：倾向 T1（系列赛胜率 63%，最可能比分 T1 2:0）。 主要依据：从长期战绩算出来的实力分看，T1 领先 gamania bears 约 116 分；老牌队伍经验更足：gamania bears 打过 0 局，T1 打过 3 局。 风险点：近期状态：gamania bears 最近 0胜0负（暂无近期数据），T1 最近 0胜3负（状态低迷）。 总结：有一定爆冷可能。
- **najin sword vs Gambit Esports**：我的判断：najin sword 晋级（系列赛胜率 61%，最可能比分 najin sword 2:0）。 理由：综合实力分 najin sword 比 Gambit Esports 高约 148 分。 风险点：近期状态：najin sword 最近 3胜7负（状态低迷），Gambit Esports 最近 5胜5负（状态一般）。 总结：基本五五开，谁赢都不奇怪。
- **Royal Never Give Up vs Oh My God**：倾向 Oh My God（系列赛胜率 62%，最可能比分 Oh My God 2:0）。 为什么：从长期战绩算出来的实力分看，Oh My God 领先 Royal Never Give Up 约 109 分。 风险点：近期状态：Royal Never Give Up 最近 8胜2负（状态火热），Oh My God 最近 7胜3负（状态不错）。 总结：有一定爆冷可能。
- **Cloud9 vs Fnatic**：我的判断：Cloud9 晋级（系列赛胜率 56%，最可能比分 Cloud9 2:0）。 理由：Cloud9 整体硬实力更强（实力分高 88）；近期状态：Cloud9 最近 9胜1负（状态火热），Fnatic 最近 9胜1负（状态火热）。 不过要注意：Fnatic 的职业比赛经验更多（Cloud9 33 局 / Fnatic 108 局）。 总结：基本五五开，谁赢都不奇怪。

### S4 2014 世界赛

训练数据截止：2014-09-18（之后的比赛模型都没见过）  
夺冠概率：samsung white 31%，najin white shield 29%，samsung blue 22%，Royal Never Give Up 6%  
**预测冠军：samsung white**　｜　实际冠军：samsung white ✅  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | samsung white vs TSM | samsung white | 80% | samsung white 3-1 | ✅ |
| R1M2 | samsung blue vs Cloud9 | samsung blue | 79% | samsung blue 3-1 | ✅ |
| R1M3 | Royal Never Give Up vs EDward Gaming | Royal Never Give Up | 60% | Royal Never Give Up 3-2 | ✅ |
| R1M4 | najin white shield vs Oh My God | najin white shield | 72% | Oh My God 0-3 | ❌ |
| R2M1 | samsung white vs samsung blue | samsung white | 59% | samsung white 3-0 | ✅ |
| R2M2 | Royal Never Give Up vs Oh My God | Royal Never Give Up | 74% | Royal Never Give Up 3-2 | ✅ |
| R3M1 | samsung white vs Royal Never Give Up | samsung white | 75% | samsung white 3-1 | ✅ |

**赛前观点（8 强）：**

- **samsung white vs TSM**：我的判断：samsung white 晋级（系列赛胜率 80%，最可能比分 samsung white 3:0）。 为什么：samsung white 整体硬实力更强（实力分高 357）；samsung white 最近手感比对手好（samsung white 7-3，TSM 6-4，比赛结果都好于赛前预期）。 不过要注意：TSM 的职业比赛经验更多（samsung white 18 局 / TSM 201 局）。 总结：爆冷概率很低。
- **samsung blue vs Cloud9**：我的判断：samsung blue 晋级（系列赛胜率 79%，最可能比分 samsung blue 3:1）。 理由：综合实力分 samsung blue 比 Cloud9 高约 322 分；samsung blue 最近手感比对手好（samsung blue 6-4，Cloud9 7-3，比赛结果都好于赛前预期）。 但是：老牌队伍经验更足：samsung blue 打过 37 局，Cloud9 打过 102 局。 总结：有一定爆冷可能。
- **Royal Never Give Up vs EDward Gaming**：我看好 Royal Never Give Up（系列赛胜率 60%，最可能比分 Royal Never Give Up 3:1）。 主要依据：Royal Never Give Up 最近手感比对手好（Royal Never Give Up 8-2，EDward Gaming 6-4，比赛结果都好于赛前预期）；老牌队伍经验更足：Royal Never Give Up 打过 99 局，EDward Gaming 打过 53 局。 但是：EDward Gaming 整体硬实力更强（实力分高 92）。 总结：基本五五开，谁赢都不奇怪。
- **najin white shield vs Oh My God**：我看好 najin white shield（系列赛胜率 72%，最可能比分 najin white shield 3:1）。 理由：从长期战绩算出来的实力分看，najin white shield 领先 Oh My God 约 230 分；najin white shield 最近手感比对手好（najin white shield 9-1，Oh My God 4-6，比赛结果都好于赛前预期）。 风险点：老牌队伍经验更足：najin white shield 打过 29 局，Oh My God 打过 140 局。 总结：有一定爆冷可能。

### S5 2015 世界赛

训练数据截止：2015-10-01（之后的比赛模型都没见过）  
夺冠概率：T1 65%，EDward Gaming 11%，KT Rolster 9%，ROX Tigers 7%  
**预测冠军：T1**　｜　实际冠军：T1 ✅  
预测 4 强命中 2/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Flash Wolves vs Origen | Origen | 69% | Origen 1-3 | ✅ |
| R1M2 | T1 vs ahq eSports Club | T1 | 91% | T1 3-0 | ✅ |
| R1M3 | Fnatic vs EDward Gaming | EDward Gaming | 64% | Fnatic 3-0 | ❌ |
| R1M4 | KT Rolster vs ROX Tigers | KT Rolster | 54% | ROX Tigers 1-3 | ❌ |
| R2M1 | Origen vs T1 | T1 | 85% | T1 0-3 | ✅ |
| R2M2 | Fnatic vs ROX Tigers | ROX Tigers | 69% | ROX Tigers 0-3 | ✅ |
| R3M1 | T1 vs ROX Tigers | T1 | 88% | T1 3-1 | ✅ |

**赛前观点（8 强）：**

- **Flash Wolves vs Origen**：我的判断：Origen 晋级（系列赛胜率 69%，最可能比分 Origen 3:1）。 理由：Origen 整体硬实力更强（实力分高 198）；近期状态：Flash Wolves 最近 6胜4负（状态不错），Origen 最近 6胜4负（状态不错）。 风险点：Flash Wolves 的职业比赛经验更多（Flash Wolves 77 局 / Origen 35 局）。 总结：有一定爆冷可能。
- **T1 vs ahq eSports Club**：我看好 T1（系列赛胜率 91%，最可能比分 T1 3:0）。 主要依据：T1 整体硬实力更强（实力分高 575）。 但是：近期状态：T1 最近 9胜1负（状态火热），ahq eSports Club 最近 10胜0负（状态火热）。 总结：爆冷概率很低。
- **Fnatic vs EDward Gaming**：我看好 EDward Gaming（系列赛胜率 64%，最可能比分 EDward Gaming 3:1）。 理由：从长期战绩算出来的实力分看，EDward Gaming 领先 Fnatic 约 173 分。 风险点：Fnatic 最近手感比对手好（Fnatic 8-2，EDward Gaming 6-4，比赛结果都好于赛前预期）。 总结：有一定爆冷可能。
- **KT Rolster vs ROX Tigers**：我看好 KT Rolster（系列赛胜率 54%，最可能比分 KT Rolster 3:1）。 主要依据：KT Rolster 的职业比赛经验更多（KT Rolster 104 局 / ROX Tigers 53 局）；KT Rolster 整体硬实力更强（实力分高 12）。 但是：ROX Tigers 最近手感比对手好（KT Rolster 5-5，ROX Tigers 7-3，比赛结果都好于赛前预期）。 总结：基本五五开，谁赢都不奇怪。

### S6 2016 世界赛

训练数据截止：2016-09-29（之后的比赛模型都没见过）  
夺冠概率：ROX Tigers 30%，EDward Gaming 20%，Samsung Galaxy 18%，T1 10%  
**预测冠军：ROX Tigers**　｜　实际冠军：T1 ❌  
预测 4 强命中 4/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | T1 vs Royal Never Give Up | T1 | 60% | T1 3-1 | ✅ |
| R1M2 | ROX Tigers vs EDward Gaming | ROX Tigers | 54% | ROX Tigers 3-1 | ✅ |
| R1M3 | Samsung Galaxy vs Cloud9 | Samsung Galaxy | 60% | Samsung Galaxy 3-0 | ✅ |
| R1M4 | H2k-Gaming vs Albus NoX Luna | H2k-Gaming | 70% | H2k-Gaming 3-0 | ✅ |
| R2M1 | T1 vs ROX Tigers | ROX Tigers | 82% | T1 3-2 | ❌ |
| R2M2 | Samsung Galaxy vs H2k-Gaming | Samsung Galaxy | 65% | Samsung Galaxy 3-0 | ✅ |
| R3M1 | T1 vs Samsung Galaxy | Samsung Galaxy | 67% | T1 3-2 | ❌ |

**赛前观点（8 强）：**

- **T1 vs Royal Never Give Up**：倾向 T1（系列赛胜率 60%，最可能比分 T1 3:1）。 为什么：从长期战绩算出来的实力分看，T1 领先 Royal Never Give Up 约 113 分；T1 选手们对线期 KDA 压制更明显。 但是：Royal Never Give Up 选手对位输出更高。 位置对比：上单 looper 近期表现优于 duke；下路 uzi 近期表现优于 bang；辅助 mata 近期表现优于 wolf。 BP预测：T1 的招牌英雄 Sivir、Alistar、Trundle；Royal Never Give Up 的招牌英雄 Braum、Karma、Rek'Sai。T1 应优先禁 Rek'Sai、Sivir、Trundle，Royal Never Give Up 大概率禁 Ekko、Gangplank、Tahm Kench。 总结：基本五五开，谁赢都不奇怪。
- **ROX Tigers vs EDward Gaming**：我的判断：ROX Tigers 晋级（系列赛胜率 54%，最可能比分 ROX Tigers 3:1）。 理由：ROX Tigers 整体硬实力更强（实力分高 31）。 风险点：老牌队伍经验更足：ROX Tigers 打过 145 局，EDward Gaming 打过 246 局。 位置对比：打野 peanut 近期表现优于 clearlove；上单 mouse 近期表现优于 smeb；辅助 meiko 近期表现优于 gorilla。 BP预测：ROX Tigers 的招牌英雄 Trundle、Ashe、Elise；EDward Gaming 的招牌英雄 Braum、Sivir、Gragas。ROX Tigers 应优先禁 Rek'Sai、Gragas、Sivir，EDward Gaming 大概率禁 Karma、Trundle、Jhin。 总结：基本五五开，谁赢都不奇怪。
- **Samsung Galaxy vs Cloud9**：我的判断：Samsung Galaxy 晋级（系列赛胜率 60%，最可能比分 Samsung Galaxy 3:1）。 主要依据：从长期战绩算出来的实力分看，Samsung Galaxy 领先 Cloud9 约 87 分；Samsung Galaxy 选手们对线期 KDA 压制更明显；Samsung Galaxy 最近手感比对手好（Samsung Galaxy 6-4，Cloud9 6-4，比赛结果都好于赛前预期）。 不过要注意：Cloud9 的职业比赛经验更多（Samsung Galaxy 179 局 / Cloud9 249 局）。 位置对比：中单 jensen 近期表现优于 crown；打野 meteos 近期表现优于 ambition；上单 impact 近期表现优于 cuvee。 BP预测：Samsung Galaxy 的招牌英雄 Sivir、Viktor、Rek'Sai；Cloud9 的招牌英雄 Rek'Sai、Gragas、Ashe。Samsung Galaxy 应优先禁 Sivir、Gragas、Rek'Sai，Cloud9 大概率禁 Gangplank、Ekko、Vladimir。 总结：基本五五开，谁赢都不奇怪。
- **H2k-Gaming vs Albus NoX Luna**：我的判断：H2k-Gaming 晋级（系列赛胜率 70%，最可能比分 H2k-Gaming 3:1）。 理由：H2k-Gaming 整体硬实力更强（实力分高 210）；H2k-Gaming 的职业比赛经验更多（H2k-Gaming 155 局 / Albus NoX Luna 22 局）；H2k-Gaming 这批首发最近赢得更多。 不过要注意：Albus NoX Luna 选手对位输出更高。 位置对比：打野 jankos 近期表现优于 pvpstejos；上单 smurf 近期表现优于 odoamne；辅助 likkrit 近期表现优于 vander。 BP预测：H2k-Gaming 的招牌英雄 Braum、Viktor、Karma；Albus NoX Luna 的招牌英雄 Rek'Sai、Bard、Trundle。H2k-Gaming 应优先禁 Rek'Sai、Sivir、Gragas，Albus NoX Luna 大概率禁 Vladimir、Shen、Gnar。 按当前版本强势英雄算，H2k-Gaming 的 BP 更占便宜。 总结：有一定爆冷可能。

### S7 2017 世界赛

训练数据截止：2017-09-23（之后的比赛模型都没见过）  
夺冠概率：Fnatic 21%，Longzhu Gaming 20%，T1 14%，Samsung Galaxy 12%  
**预测冠军：Longzhu Gaming**　｜　实际冠军：Samsung Galaxy ❌  
预测 4 强命中 1/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | T1 vs Misfits Gaming | T1 | 62% | T1 3-2 | ✅ |
| R1M2 | Royal Never Give Up vs Fnatic | Fnatic | 57% | Royal Never Give Up 3-1 | ❌ |
| R1M3 | Longzhu Gaming vs Samsung Galaxy | Longzhu Gaming | 59% | Samsung Galaxy 0-3 | ❌ |
| R1M4 | Team WE vs Cloud9 | Cloud9 | 54% | Team WE 3-2 | ❌ |
| R2M1 | T1 vs Royal Never Give Up | T1 | 53% | T1 3-2 | ✅ |
| R2M2 | Samsung Galaxy vs Team WE | Samsung Galaxy | 57% | Samsung Galaxy 3-1 | ✅ |
| R3M1 | T1 vs Samsung Galaxy | Samsung Galaxy | 55% | Samsung Galaxy 0-3 | ✅ |

**赛前观点（8 强）：**

- **T1 vs Misfits Gaming**：倾向 T1（系列赛胜率 62%，最可能比分 T1 3:1）。 主要依据：从长期战绩算出来的实力分看，T1 领先 Misfits Gaming 约 318 分；T1 的职业比赛经验更多（T1 325 局 / Misfits Gaming 119 局）。 不过要注意：Misfits Gaming 这批首发最近赢得更多。 位置对比：下路 bang 近期表现优于 hans sama；中单 powerofevil 近期表现优于 faker；打野 blank 近期表现优于 maxlore。 BP预测：T1 的招牌英雄 Ashe、Lulu、Alistar；Misfits Gaming 的招牌英雄 Varus、Orianna、Jarvan IV。T1 应优先禁 Jarvan IV、Kalista、Thresh，Misfits Gaming 大概率禁 Tristana、Cassiopeia、Taliyah。 总结：有一定爆冷可能。
- **Royal Never Give Up vs Fnatic**：倾向 Fnatic（系列赛胜率 57%，最可能比分 Fnatic 3:1）。 理由：近期状态：Royal Never Give Up 最近 5胜5负（状态一般），Fnatic 最近 7胜3负（状态不错）；Fnatic 资源控制更强（推塔、小龙、大龙拿得更多）。 但是：Royal Never Give Up 整体硬实力更强（实力分高 109）。 位置对比：中单 xiaohu 近期表现优于 caps；下路 rekkles 近期表现优于 uzi；打野 mlxg 近期表现优于 broxah。 BP预测：Royal Never Give Up 的招牌英雄 Gragas、Taliyah、Thresh；Fnatic 的招牌英雄 Gragas、Elise、Kennen。Royal Never Give Up 应优先禁 Jarvan IV、Gragas、Elise，Fnatic 大概率禁 Kalista、Cho'Gath、Taliyah。 总结：基本五五开，谁赢都不奇怪。
- **Longzhu Gaming vs Samsung Galaxy**：我看好 Longzhu Gaming（系列赛胜率 59%，最可能比分 Longzhu Gaming 3:1）。 为什么：Longzhu Gaming 选手对位输出更高；Longzhu Gaming 整体硬实力更强（实力分高 28）；Longzhu Gaming 最近手感比对手好（Longzhu Gaming 6-4，Samsung Galaxy 6-4，比赛结果都好于赛前预期）。 不过要注意：Samsung Galaxy 资源控制更强（推塔、小龙、大龙拿得更多）。 位置对比：中单 bdd 近期表现优于 crown；上单 khan 近期表现优于 cuvee；下路 pray 近期表现优于 ruler。 BP预测：Longzhu Gaming 的招牌英雄 Thresh、Ashe、Taliyah；Samsung Galaxy 的招牌英雄 Varus、Gragas、Karma。Longzhu Gaming 应优先禁 Jarvan IV、Kalista、Gragas，Samsung Galaxy 大概率禁 Thresh、Elise、Taliyah。 总结：基本五五开，谁赢都不奇怪。
- **Team WE vs Cloud9**：我的判断：Cloud9 晋级（系列赛胜率 54%，最可能比分 Cloud9 3:1）。 主要依据：Cloud9 选手对位输出更高。 但是：从长期战绩算出来的实力分看，Team WE 领先 Cloud9 约 93 分。 位置对比：中单 jensen 近期表现优于 xiye；打野 contractz 近期表现优于 condi；辅助 smoothie 近期表现优于 ben。 BP预测：Team WE 的招牌英雄 Jarvan IV、Gragas、Xayah；Cloud9 的招牌英雄 Orianna、Thresh、Syndra。Team WE 应优先禁 Gragas、Jarvan IV、Tristana，Cloud9 大概率禁 Kalista、Thresh、Maokai。 总结：基本五五开，谁赢都不奇怪。

### S8 2018 世界赛

训练数据截止：2018-10-01（之后的比赛模型都没见过）  
夺冠概率：Fnatic 25%，Invictus Gaming 19%，KT Rolster 18%，Royal Never Give Up 13%  
**预测冠军：Fnatic**　｜　实际冠军：Invictus Gaming ❌  
预测 4 强命中 2/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Kwangdong Freecs vs Cloud9 | Kwangdong Freecs | 53% | Cloud9 0-3 | ❌ |
| R1M2 | Fnatic vs EDward Gaming | Fnatic | 69% | Fnatic 3-1 | ✅ |
| R1M3 | Royal Never Give Up vs G2 Esports | Royal Never Give Up | 61% | G2 Esports 2-3 | ❌ |
| R1M4 | KT Rolster vs Invictus Gaming | Invictus Gaming | 51% | Invictus Gaming 2-3 | ✅ |
| R2M1 | Cloud9 vs Fnatic | Fnatic | 66% | Fnatic 0-3 | ✅ |
| R2M2 | G2 Esports vs Invictus Gaming | Invictus Gaming | 68% | Invictus Gaming 0-3 | ✅ |
| R3M1 | Fnatic vs Invictus Gaming | Fnatic | 51% | Invictus Gaming 0-3 | ❌ |

**赛前观点（8 强）：**

- **Kwangdong Freecs vs Cloud9**：我的判断：Kwangdong Freecs 晋级（系列赛胜率 53%，最可能比分 Kwangdong Freecs 3:1）。 主要依据：综合实力分 Kwangdong Freecs 比 Cloud9 高约 130 分；Kwangdong Freecs 这批首发最近赢得更多。 不过要注意：Cloud9 选手对位输出更高。 位置对比：打野 blaber 近期表现优于 spirit；中单 jensen 近期表现优于 kuro；上单 kiin 近期表现优于 licorice。 BP预测：Kwangdong Freecs 的招牌英雄 Alistar、Shen、Gragas；Cloud9 的招牌英雄 Braum、Zilean、Ornn。Kwangdong Freecs 应优先禁 Aatrox、Tahm Kench、Braum，Cloud9 大概率禁 Varus、Rakan、Gragas。 总结：基本五五开，谁赢都不奇怪。
- **Fnatic vs EDward Gaming**：我看好 Fnatic（系列赛胜率 69%，最可能比分 Fnatic 3:1）。 理由：从长期战绩算出来的实力分看，Fnatic 领先 EDward Gaming 约 110 分；Fnatic 选手对位输出更高。 不过要注意：EDward Gaming 最近手感比对手好（Fnatic 7-3，EDward Gaming 6-4，比赛结果都好于赛前预期）。 位置对比：中单 caps 近期表现优于 scout；辅助 meiko 近期表现优于 hylissang。 BP预测：Fnatic 的招牌英雄 Pyke、Trundle、Sejuani；EDward Gaming 的招牌英雄 Kai'Sa、Tahm Kench、Varus。Fnatic 应优先禁 Tahm Kench、Ryze、Varus，EDward Gaming 大概率禁 Trundle、Gragas、Braum。 总结：有一定爆冷可能。
- **Royal Never Give Up vs G2 Esports**：我的判断：Royal Never Give Up 晋级（系列赛胜率 61%，最可能比分 Royal Never Give Up 3:1）。 主要依据：Royal Never Give Up 整体硬实力更强（实力分高 115）；Royal Never Give Up 的职业比赛经验更多（Royal Never Give Up 733 局 / G2 Esports 224 局）；Royal Never Give Up 最近手感比对手好（Royal Never Give Up 7-3，G2 Esports 6-4，比赛结果都好于赛前预期）。 但是：G2 Esports 选手对位输出更高。 位置对比：下路 uzi 近期表现优于 hjarnan；辅助 ming 近期表现优于 wadid；中单 perkz 近期表现优于 xiaohu。 BP预测：Royal Never Give Up 的招牌英雄 Shen、Tahm Kench、Kai'Sa；G2 Esports 的招牌英雄 Tahm Kench、Varus、Heimerdinger。Royal Never Give Up 应优先禁 Aatrox、Tahm Kench、Varus，G2 Esports 大概率禁 Trundle、Zoe、Kai'Sa。 总结：基本五五开，谁赢都不奇怪。
- **KT Rolster vs Invictus Gaming**：我的判断：Invictus Gaming 晋级（系列赛胜率 51%，最可能比分 Invictus Gaming 3:1）。 理由：Invictus Gaming 选手对位输出更高。 不过要注意：近期状态：KT Rolster 最近 8胜2负（状态火热），Invictus Gaming 最近 5胜5负（状态一般）。 位置对比：中单 rookie 近期表现优于 ucal；下路 deft 近期表现优于 jackeylove；辅助 baolan 近期表现优于 mata。 BP预测：KT Rolster 的招牌英雄 Shen、Tahm Kench、Sejuani；Invictus Gaming 的招牌英雄 Tahm Kench、Alistar、Lucian。KT Rolster 应优先禁 Tahm Kench、Camille、Varus，Invictus Gaming 大概率禁 Rakan、Taliyah、Trundle。 总结：基本五五开，谁赢都不奇怪。

### S9 2019 世界赛

训练数据截止：2019-10-02（之后的比赛模型都没见过）  
夺冠概率：T1 27%，FunPlus Phoenix 23%，G2 Esports 19%，Fnatic 12%  
**预测冠军：FunPlus Phoenix**　｜　实际冠军：FunPlus Phoenix ✅  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | DWG KIA vs G2 Esports | G2 Esports | 65% | G2 Esports 1-3 | ✅ |
| R1M2 | T1 vs Splyce | T1 | 76% | T1 3-1 | ✅ |
| R1M3 | Griffin vs Invictus Gaming | Griffin | 64% | Invictus Gaming 1-3 | ❌ |
| R1M4 | FunPlus Phoenix vs Fnatic | FunPlus Phoenix | 58% | FunPlus Phoenix 3-1 | ✅ |
| R2M1 | G2 Esports vs T1 | T1 | 53% | G2 Esports 3-1 | ❌ |
| R2M2 | Invictus Gaming vs FunPlus Phoenix | FunPlus Phoenix | 79% | FunPlus Phoenix 1-3 | ✅ |
| R3M1 | G2 Esports vs FunPlus Phoenix | FunPlus Phoenix | 55% | FunPlus Phoenix 0-3 | ✅ |

**赛前观点（8 强）：**

- **DWG KIA vs G2 Esports**：我的判断：G2 Esports 晋级（系列赛胜率 65%，最可能比分 G2 Esports 3:1）。 主要依据：从长期战绩算出来的实力分看，G2 Esports 领先 DWG KIA 约 151 分；G2 Esports 选手对位输出更高；近期状态：DWG KIA 最近 4胜6负（状态一般），G2 Esports 最近 6胜4负（状态不错）。 风险点：DWG KIA 这批首发最近赢得更多。 位置对比：中单 caps 近期表现优于 showmaker；打野 jankos 近期表现优于 canyon；下路 perkz 近期表现优于 nuclear。 BP预测：DWG KIA 的招牌英雄 Kai'Sa、Jayce、Camille；G2 Esports 的招牌英雄 Sylas、Rakan、Xayah。DWG KIA 应优先禁 Sylas、Xayah、Akali，G2 Esports 大概率禁 Corki、Aatrox、Karma。 总结：有一定爆冷可能。
- **T1 vs Splyce**：倾向 T1（系列赛胜率 76%，最可能比分 T1 3:1）。 主要依据：T1 整体硬实力更强（实力分高 152）；T1 最近手感比对手好（T1 9-1，Splyce 6-4，比赛结果都好于赛前预期）；T1 选手对位输出更高。 但是：Splyce 这批首发最近赢得更多。 位置对比：下路 teddy 近期表现优于 kobbe；辅助 effort 近期表现优于 tore；打野 clid 近期表现优于 xerxe。 BP预测：T1 的招牌英雄 Aatrox、Varus、Akali；Splyce 的招牌英雄 Gangplank、Kai'Sa、Sylas。T1 应优先禁 Sylas、Akali、Corki，Splyce 大概率禁 Aatrox、Xayah、Rakan。 按当前版本强势英雄算，Splyce 的 BP 更占便宜。 总结：有一定爆冷可能。
- **Griffin vs Invictus Gaming**：我看好 Griffin（系列赛胜率 64%，最可能比分 Griffin 3:1）。 主要依据：从长期战绩算出来的实力分看，Griffin 领先 Invictus Gaming 约 73 分。 不过要注意：Invictus Gaming 的职业比赛经验更多（Griffin 271 局 / Invictus Gaming 656 局）。 位置对比：打野 tarzan 近期表现优于 leyan；下路 viper 近期表现优于 jackeylove；中单 chovy 近期表现优于 rookie。 BP预测：Griffin 的招牌英雄 Sejuani、Ezreal、Tahm Kench；Invictus Gaming 的招牌英雄 Sylas、Kai'Sa、Kennen。Griffin 应优先禁 Sylas、Gragas、Akali，Invictus Gaming 大概率禁 Aatrox、Sejuani、Tahm Kench。 总结：有一定爆冷可能。
- **FunPlus Phoenix vs Fnatic**：倾向 FunPlus Phoenix（系列赛胜率 58%，最可能比分 FunPlus Phoenix 3:1）。 理由：从长期战绩算出来的实力分看，FunPlus Phoenix 领先 Fnatic 约 41 分；FunPlus Phoenix 选手对位输出更高；FunPlus Phoenix 最近手感比对手好（FunPlus Phoenix 8-2，Fnatic 7-3，比赛结果都好于赛前预期）。 不过要注意：老牌队伍经验更足：FunPlus Phoenix 打过 187 局，Fnatic 打过 522 局。 位置对比：打野 tian 近期表现优于 broxah；下路 lwx 近期表现优于 rekkles；中单 doinb 近期表现优于 nemesis。 BP预测：FunPlus Phoenix 的招牌英雄 Nautilus、Sylas、Lucian；Fnatic 的招牌英雄 Aatrox、Rakan、Gragas。FunPlus Phoenix 应优先禁 Aatrox、Gragas、Sylas，Fnatic 大概率禁 Kai'Sa、Nautilus、Tahm Kench。 总结：基本五五开，谁赢都不奇怪。

### S10 2020 世界赛

训练数据截止：2020-09-25（之后的比赛模型都没见过）  
夺冠概率：DWG KIA 44%，Gen.G 18%，Top Esports 13%，G2 Esports 7%  
**预测冠军：DWG KIA**　｜　实际冠军：DWG KIA ✅  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Top Esports vs Fnatic | Top Esports | 62% | Top Esports 3-2 | ✅ |
| R1M2 | Suning vs JD Gaming | Suning | 53% | Suning 3-1 | ✅ |
| R1M3 | Gen.G vs G2 Esports | Gen.G | 62% | G2 Esports 0-3 | ❌ |
| R1M4 | DWG KIA vs DRX | DWG KIA | 90% | DWG KIA 3-0 | ✅ |
| R2M1 | Top Esports vs Suning | Top Esports | 62% | Suning 1-3 | ❌ |
| R2M2 | G2 Esports vs DWG KIA | DWG KIA | 69% | DWG KIA 1-3 | ✅ |
| R3M1 | Suning vs DWG KIA | DWG KIA | 78% | DWG KIA 1-3 | ✅ |

**赛前观点（8 强）：**

- **Top Esports vs Fnatic**：倾向 Top Esports（系列赛胜率 62%，最可能比分 Top Esports 3:1）。 主要依据：从长期战绩算出来的实力分看，Top Esports 领先 Fnatic 约 40 分；近期状态：Top Esports 最近 8胜2负（状态火热），Fnatic 最近 5胜5负（状态一般）；Top Esports 选手对位输出更高。 但是：Fnatic 的职业比赛经验更多（Top Esports 150 局 / Fnatic 579 局）。 位置对比：下路 jackeylove 近期表现优于 rekkles；打野 selfmade 近期表现优于 karsa；上单 369 近期表现优于 bwipo。 BP预测：Top Esports 的招牌英雄 Lee Sin、Syndra、Renekton；Fnatic 的招牌英雄 Senna、Ornn、Gragas。Top Esports 应优先禁 Thresh、Senna、Sett，Fnatic 大概率禁 Renekton、Zoe、Syndra。 按当前版本强势英雄算，Fnatic 的 BP 更占便宜。 总结：基本五五开，谁赢都不奇怪。
- **Suning vs JD Gaming**：倾向 Suning（系列赛胜率 53%，最可能比分 Suning 3:1）。 理由：近期状态：Suning 最近 7胜3负（状态不错），JD Gaming 最近 6胜4负（状态不错）。 但是：JD Gaming 整体硬实力更强（实力分高 32）。 位置对比：打野 kanavi 近期表现优于 sofm；辅助 lvmao 近期表现优于 swordart；下路 loken 近期表现优于 huanfeng。 BP预测：Suning 的招牌英雄 Syndra、Renekton、Lee Sin；JD Gaming 的招牌英雄 Ornn、Aphelios、Lee Sin。Suning 应优先禁 Sett、Bard、Zoe，JD Gaming 大概率禁 Renekton、Ashe、Graves。 总结：基本五五开，谁赢都不奇怪。
- **Gen.G vs G2 Esports**：我看好 Gen.G（系列赛胜率 62%，最可能比分 Gen.G 3:1）。 理由：从长期战绩算出来的实力分看，Gen.G 领先 G2 Esports 约 52 分；Gen.G 选手对位输出更高；近期状态：Gen.G 最近 9胜1负（状态火热），G2 Esports 最近 7胜3负（状态不错）。 不过要注意：pool。 位置对比：下路 ruler 近期表现优于 perkz；打野 clid 近期表现优于 jankos；辅助 life 近期表现优于 mikyx。 BP预测：Gen.G 的招牌英雄 Azir、Ezreal、Ornn；G2 Esports 的招牌英雄 Sett、Nautilus、Ashe。Gen.G 应优先禁 Sett、Ashe、Zoe，G2 Esports 大概率禁 Renekton、Volibear、Nidalee。 按当前版本强势英雄算，G2 Esports 的 BP 更占便宜。 总结：有一定爆冷可能。
- **DWG KIA vs DRX**：我的判断：DWG KIA 晋级（系列赛胜率 90%，最可能比分 DWG KIA 3:0）。 为什么：综合实力分 DWG KIA 比 DRX 高约 174 分；DWG KIA 选手对位输出更高；近期状态：DWG KIA 最近 10胜0负（状态火热），DRX 最近 3胜7负（状态低迷）。 但是：DRX 这批首发最近赢得更多。 位置对比：上单 nuguri 近期表现优于 doran；中单 showmaker 近期表现优于 chovy；打野 canyon 近期表现优于 pyosik。 BP预测：DWG KIA 的招牌英雄 Sett、Jayce、Ezreal；DRX 的招牌英雄 Azir、Ezreal、Aatrox。DWG KIA 应优先禁 Sett、Volibear、Ashe，DRX 大概率禁 Renekton、Zoe、Thresh。 总结：爆冷概率很低。

### S11 2021 世界赛

训练数据截止：2021-10-05（之后的比赛模型都没见过）  
夺冠概率：EDward Gaming 31%，DWG KIA 30%，MAD Lions 19%，Cloud9 7%  
**预测冠军：DWG KIA**　｜　实际冠军：EDward Gaming ❌  
预测 4 强命中 3/4，决赛队伍命中 2/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Royal Never Give Up vs EDward Gaming | EDward Gaming | 82% | EDward Gaming 2-3 | ✅ |
| R1M2 | Gen.G vs Cloud9 | Cloud9 | 62% | Gen.G 3-0 | ❌ |
| R1M3 | T1 vs Hanwha Life Esports | T1 | 57% | T1 3-0 | ✅ |
| R1M4 | DWG KIA vs MAD Lions | DWG KIA | 56% | DWG KIA 3-0 | ✅ |
| R2M1 | EDward Gaming vs Gen.G | EDward Gaming | 79% | EDward Gaming 3-2 | ✅ |
| R2M2 | T1 vs DWG KIA | DWG KIA | 81% | DWG KIA 2-3 | ✅ |
| R3M1 | EDward Gaming vs DWG KIA | DWG KIA | 56% | EDward Gaming 3-2 | ❌ |

**赛前观点（8 强）：**

- **Royal Never Give Up vs EDward Gaming**：我看好 EDward Gaming（系列赛胜率 82%，最可能比分 EDward Gaming 3:0）。 主要依据：EDward Gaming 整体硬实力更强（实力分高 121）；EDward Gaming 最近手感比对手好（Royal Never Give Up 5-5，EDward Gaming 8-2，比赛结果都好于赛前预期）；EDward Gaming 选手对位输出更高。 位置对比：下路 viper 近期表现优于 such；中单 scout 近期表现优于 lover11；辅助 lele 近期表现优于 meiko。 BP预测：Royal Never Give Up 的招牌英雄 Gnar、Thresh、Viego；EDward Gaming 的招牌英雄 Lee Sin、Sylas、Leona。Royal Never Give Up 应优先禁 Lee Sin、Renekton、Xin Zhao，EDward Gaming 大概率禁 Viego、Leona、LeBlanc。 总结：爆冷概率很低。
- **Gen.G vs Cloud9**：我看好 Cloud9（系列赛胜率 62%，最可能比分 Cloud9 3:1）。 主要依据：Cloud9 整体硬实力更强（实力分高 176）；Cloud9 选手对位输出更高。 风险点：Gen.G 这批首发最近赢得更多。 位置对比：下路 zven 近期表现优于 ruler；打野 blaber 近期表现优于 clid；辅助 vulcan 近期表现优于 life。 BP预测：Gen.G 的招牌英雄 Volibear、Lee Sin、Leona；Cloud9 的招牌英雄 Varus、Lee Sin、Nautilus。Gen.G 应优先禁 Lee Sin、Xin Zhao、Viego，Cloud9 大概率禁 Leona、Renekton、Thresh。 按当前版本强势英雄算，Gen.G 的 BP 更占便宜。 总结：有一定爆冷可能。
- **T1 vs Hanwha Life Esports**：我看好 T1（系列赛胜率 57%，最可能比分 T1 3:1）。 为什么：T1 整体硬实力更强（实力分高 40）；老牌队伍经验更足：T1 打过 765 局，Hanwha Life Esports 打过 351 局。 不过要注意：近期状态：T1 最近 5胜5负（状态一般），Hanwha Life Esports 最近 7胜3负（状态不错）。 位置对比：中单 chovy 近期表现优于 faker；上单 canna 近期表现优于 morgan；下路 deft 近期表现优于 gumayusi。 BP预测：T1 的招牌英雄 Leona、Viego、Ryze；Hanwha Life Esports 的招牌英雄 Varus、Viego、Lee Sin。T1 应优先禁 Lee Sin、Viego、Varus，Hanwha Life Esports 大概率禁 Jayce、Leona、Xin Zhao。 总结：基本五五开，谁赢都不奇怪。
- **DWG KIA vs MAD Lions**：我看好 DWG KIA（系列赛胜率 56%，最可能比分 DWG KIA 3:1）。 理由：DWG KIA 选手对位输出更高；老牌队伍经验更足：DWG KIA 打过 435 局，MAD Lions 打过 119 局。 不过要注意：综合实力分 MAD Lions 比 DWG KIA 高约 128 分。 位置对比：打野 canyon 近期表现优于 elyoya；下路 ghost 近期表现优于 carzzy；中单 showmaker 近期表现优于 humanoid。 BP预测：DWG KIA 的招牌英雄 Ryze、Leona、Varus；MAD Lions 的招牌英雄 Leona、Lee Sin、Ezreal。DWG KIA 应优先禁 Lee Sin、Viego、Leona，MAD Lions 大概率禁 LeBlanc、Jayce、Renekton。 总结：基本五五开，谁赢都不奇怪。

### S12 2022 世界赛

训练数据截止：2022-09-29（之后的比赛模型都没见过）  
夺冠概率：Gen.G 64%，JD Gaming 14%，EDward Gaming 8%，Rogue 6%  
**预测冠军：Gen.G**　｜　实际冠军：DRX ❌  
预测 4 强命中 3/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | JD Gaming vs Rogue | JD Gaming | 60% | JD Gaming 3-0 | ✅ |
| R1M2 | Royal Never Give Up vs T1 | T1 | 55% | T1 0-3 | ✅ |
| R1M3 | DRX vs EDward Gaming | EDward Gaming | 80% | DRX 3-2 | ❌ |
| R1M4 | DWG KIA vs Gen.G | Gen.G | 94% | Gen.G 2-3 | ✅ |
| R2M1 | JD Gaming vs T1 | JD Gaming | 62% | T1 1-3 | ❌ |
| R2M2 | DRX vs Gen.G | Gen.G | 99% | DRX 3-1 | ❌ |
| R3M1 | DRX vs T1 | T1 | 86% | DRX 3-2 | ❌ |

**赛前观点（8 强）：**

- **JD Gaming vs Rogue**：我看好 JD Gaming（系列赛胜率 60%，最可能比分 JD Gaming 3:1）。 理由：综合实力分 JD Gaming 比 Rogue 高约 12 分；老牌队伍经验更足：JD Gaming 打过 574 局，Rogue 打过 225 局。 风险点：Rogue 选手对位输出更高。 位置对比：下路 comp 近期表现优于 hope；中单 larssen 近期表现优于 yagao；打野 kanavi 近期表现优于 malrang。 BP预测：JD Gaming 的招牌英雄 Ahri、Aphelios、Taliyah；Rogue 的招牌英雄 Jarvan IV、Azir、Ornn。JD Gaming 应优先禁 Wukong、Sylas、Ahri，Rogue 大概率禁 Kalista、Zeri、Taliyah。 总结：基本五五开，谁赢都不奇怪。
- **Royal Never Give Up vs T1**：我看好 T1（系列赛胜率 55%，最可能比分 T1 3:1）。 主要依据：T1 整体硬实力更强（实力分高 232）；pool；T1 这批首发最近赢得更多。 不过要注意：Royal Never Give Up 选手对位输出更高。 位置对比：中单 xiaohu 近期表现优于 faker；上单 breathe 近期表现优于 zeus；下路 gala 近期表现优于 gumayusi。 BP预测：Royal Never Give Up 的招牌英雄 Aphelios、Viego、Nautilus；T1 的招牌英雄 Lee Sin、Gnar、Azir。Royal Never Give Up 应优先禁 Wukong、Zeri、Azir，T1 大概率禁 Taliyah、Gwen、Sivir。 总结：基本五五开，谁赢都不奇怪。
- **DRX vs EDward Gaming**：我的判断：EDward Gaming 晋级（系列赛胜率 80%，最可能比分 EDward Gaming 3:0）。 主要依据：EDward Gaming 选手对位输出更高；老牌队伍经验更足：DRX 打过 308 局，EDward Gaming 打过 909 局。 风险点：DRX 整体硬实力更强（实力分高 37）。 位置对比：中单 scout 近期表现优于 zeka；下路 viper 近期表现优于 deft；辅助 meiko 近期表现优于 beryl。 BP预测：DRX 的招牌英雄 Ahri、Gnar、Viego；EDward Gaming 的招牌英雄 Azir、Gnar、Aphelios。DRX 应优先禁 Wukong、Zeri、Sylas，EDward Gaming 大概率禁 Kalista、Poppy、Sivir。 总结：有一定爆冷可能。
- **DWG KIA vs Gen.G**：我的判断：Gen.G 晋级（系列赛胜率 94%，最可能比分 Gen.G 3:0）。 为什么：从长期战绩算出来的实力分看，Gen.G 领先 DWG KIA 约 252 分；Gen.G 选手对位输出更高；Gen.G 最近手感比对手好（DWG KIA 5-5，Gen.G 8-2，比赛结果都好于赛前预期）。 不过要注意：DWG KIA 这批首发最近赢得更多。 位置对比：下路 ruler 近期表现优于 deokdam；中单 chovy 近期表现优于 showmaker；上单 doran 近期表现优于 burdol。 BP预测：DWG KIA 的招牌英雄 Wukong、Aphelios、Yuumi；Gen.G 的招牌英雄 Gnar、Azir、Wukong。DWG KIA 应优先禁 Wukong、Poppy、Zeri，Gen.G 大概率禁 Yuumi、Taliyah、Kalista。 总结：爆冷概率很低。

### S13 2023 世界赛

训练数据截止：2023-10-10（之后的比赛模型都没见过）  
夺冠概率：Gen.G 32%，JD Gaming 29%，KT Rolster 10%，LNG Esports 9%  
**预测冠军：JD Gaming**　｜　实际冠军：T1 ❌  
预测 4 强命中 1/4，决赛队伍命中 0/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Bilibili Gaming vs Gen.G | Gen.G | 70% | Bilibili Gaming 3-2 | ❌ |
| R1M2 | NRG Esports vs Weibo Gaming | NRG Esports | 58% | Weibo Gaming 0-3 | ❌ |
| R1M3 | JD Gaming vs KT Rolster | JD Gaming | 63% | JD Gaming 3-1 | ✅ |
| R1M4 | LNG Esports vs T1 | LNG Esports | 57% | T1 0-3 | ❌ |
| R2M1 | Bilibili Gaming vs Weibo Gaming | Bilibili Gaming | 62% | Weibo Gaming 2-3 | ❌ |
| R2M2 | JD Gaming vs T1 | JD Gaming | 74% | T1 1-3 | ❌ |
| R3M1 | T1 vs Weibo Gaming | T1 | 60% | T1 3-0 | ✅ |

**赛前观点（8 强）：**

- **Bilibili Gaming vs Gen.G**：我的判断：Gen.G 晋级（系列赛胜率 70%，最可能比分 Gen.G 3:1）。 为什么：从长期战绩算出来的实力分看，Gen.G 领先 Bilibili Gaming 约 242 分；近期状态：Bilibili Gaming 最近 3胜7负（状态低迷），Gen.G 最近 8胜2负（状态火热）。 不过要注意：Bilibili Gaming 这批首发最近赢得更多。 位置对比：打野 peanut 近期表现优于 xun；下路 peyz 近期表现优于 elk；辅助 delight 近期表现优于 on。 BP预测：Bilibili Gaming 的招牌英雄 Aphelios、Annie、Xayah；Gen.G 的招牌英雄 Jax、Maokai、Kai'Sa。Bilibili Gaming 应优先禁 Maokai、Rakan、Kai'Sa，Gen.G 大概率禁 Rell、Neeko、Nautilus。 总结：有一定爆冷可能。
- **NRG Esports vs Weibo Gaming**：倾向 NRG Esports（系列赛胜率 58%，最可能比分 NRG Esports 3:1）。 理由：从长期战绩算出来的实力分看，NRG Esports 领先 Weibo Gaming 约 280 分；近期状态：NRG Esports 最近 6胜4负（状态不错），Weibo Gaming 最近 6胜4负（状态不错）。 不过要注意：Weibo Gaming 选手对位输出更高。 位置对比：上单 theshy 近期表现优于 dhokla；中单 palafox 近期表现优于 xiaohu；打野 contractz 近期表现优于 weiwei。 BP预测：NRG Esports 的招牌英雄 Rell、Kai'Sa、Renekton；Weibo Gaming 的招牌英雄 Aphelios、K'Sante、Azir。NRG Esports 应优先禁 Rell、Tristana、Rakan，Weibo Gaming 大概率禁 Xayah、Renekton、Azir。 总结：基本五五开，谁赢都不奇怪。
- **JD Gaming vs KT Rolster**：我的判断：JD Gaming 晋级（系列赛胜率 63%，最可能比分 JD Gaming 3:1）。 为什么：JD Gaming 最近手感比对手好（JD Gaming 7-3，KT Rolster 6-4，比赛结果都好于赛前预期）。 风险点：从长期战绩算出来的实力分看，KT Rolster 领先 JD Gaming 约 46 分。 位置对比：中单 bdd 近期表现优于 knight；下路 aiming 近期表现优于 ruler。 BP预测：JD Gaming 的招牌英雄 Xayah、Rakan、Ornn；KT Rolster 的招牌英雄 Renekton、Viego、Nautilus。JD Gaming 应优先禁 Rakan、Kai'Sa、Alistar，KT Rolster 大概率禁 Xayah、Tristana、Jayce。 总结：有一定爆冷可能。
- **LNG Esports vs T1**：我的判断：LNG Esports 晋级（系列赛胜率 57%，最可能比分 LNG Esports 3:1）。 理由：LNG Esports 最近手感比对手好（LNG Esports 6-4，T1 3-7，比赛结果都好于赛前预期）。 不过要注意：从长期战绩算出来的实力分看，T1 领先 LNG Esports 约 64 分。 位置对比：中单 scout 近期表现优于 faker；打野 tarzan 近期表现优于 oner；下路 gala 近期表现优于 gumayusi。 BP预测：LNG Esports 的招牌英雄 Xayah、Nautilus、Maokai；T1 的招牌英雄 Xayah、Azir、Maokai。LNG Esports 应优先禁 Xayah、Rell、Rakan，T1 大概率禁 Tristana、Jax、Jayce。 总结：基本五五开，谁赢都不奇怪。

### S14 2024 世界赛

训练数据截止：2024-09-25（之后的比赛模型都没见过）  
夺冠概率：Gen.G 38%，Bilibili Gaming 28%，Hanwha Life Esports 15%，Top Esports 8%  
**预测冠军：Gen.G**　｜　实际冠军：T1 ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Bilibili Gaming vs Hanwha Life Esports | Bilibili Gaming | 55% | Bilibili Gaming 3-1 | ✅ |
| R1M2 | LNG Esports vs Weibo Gaming | Weibo Gaming | 57% | Weibo Gaming 1-3 | ✅ |
| R1M3 | FlyQuest vs Gen.G | Gen.G | 73% | Gen.G 2-3 | ✅ |
| R1M4 | T1 vs Top Esports | Top Esports | 62% | T1 3-0 | ❌ |
| R2M1 | Bilibili Gaming vs Weibo Gaming | Bilibili Gaming | 90% | Bilibili Gaming 3-0 | ✅ |
| R2M2 | Gen.G vs T1 | Gen.G | 88% | T1 1-3 | ❌ |
| R3M1 | Bilibili Gaming vs T1 | Bilibili Gaming | 74% | T1 2-3 | ❌ |

**赛前观点（8 强）：**

- **Bilibili Gaming vs Hanwha Life Esports**：我的判断：Bilibili Gaming 晋级（系列赛胜率 55%，最可能比分 Bilibili Gaming 3:1）。 理由：Bilibili Gaming 选手对位输出更高；Bilibili Gaming 最近手感比对手好（Bilibili Gaming 9-1，Hanwha Life Esports 6-4，比赛结果都好于赛前预期）；Bilibili Gaming 资源控制更强（推塔、小龙、大龙拿得更多）。 不过要注意：综合实力分 Hanwha Life Esports 比 Bilibili Gaming 高约 84 分。 位置对比：上单 bin 近期表现优于 doran；中单 knight 近期表现优于 zeka；下路 elk 近期表现优于 viper。 BP预测：Bilibili Gaming 的招牌英雄 Renekton、Rell、Corki；Hanwha Life Esports 的招牌英雄 Zeri、Sejuani、Rell。Bilibili Gaming 应优先禁 Rumble、Ashe、Ezreal，Hanwha Life Esports 大概率禁 Rell、Renekton、Alistar。 总结：基本五五开，谁赢都不奇怪。
- **LNG Esports vs Weibo Gaming**：我看好 Weibo Gaming（系列赛胜率 57%，最可能比分 Weibo Gaming 3:1）。 主要依据：综合实力分 Weibo Gaming 比 LNG Esports 高约 30 分；Weibo Gaming 最近手感比对手好（LNG Esports 4-6，Weibo Gaming 5-5，比赛结果都好于赛前预期）。 不过要注意：LNG Esports 选手对位输出更高。 位置对比：下路 gala 近期表现优于 light；中单 scout 近期表现优于 xiaohu；打野 tarzan 近期表现优于 weiwei。 BP预测：LNG Esports 的招牌英雄 K'Sante、Ezreal、Corki；Weibo Gaming 的招牌英雄 Renekton、Ezreal、Zeri。LNG Esports 应优先禁 Ashe、Ezreal、Rumble，Weibo Gaming 大概率禁 Leona、Sejuani、Maokai。 总结：基本五五开，谁赢都不奇怪。
- **FlyQuest vs Gen.G**：我的判断：Gen.G 晋级（系列赛胜率 73%，最可能比分 Gen.G 3:1）。 理由：从长期战绩算出来的实力分看，Gen.G 领先 FlyQuest 约 215 分；Gen.G 选手对位输出更高。 但是：近期状态：FlyQuest 最近 7胜3负（状态不错），Gen.G 最近 6胜4负（状态不错）。 位置对比：上单 kiin 近期表现优于 bwipo；中单 quad 近期表现优于 chovy；辅助 busio 近期表现优于 lehends。 BP预测：FlyQuest 的招牌英雄 Renekton、Corki、Leona；Gen.G 的招牌英雄 Corki、K'Sante、Zeri。FlyQuest 应优先禁 Ashe、Ezreal、Maokai，Gen.G 大概率禁 Leona、Renekton、Lillia。 总结：有一定爆冷可能。
- **T1 vs Top Esports**：我的判断：Top Esports 晋级（系列赛胜率 62%，最可能比分 Top Esports 3:1）。 但是：pool。 位置对比：中单 creme 近期表现优于 faker；下路 jackeylove 近期表现优于 gumayusi；上单 zeus 近期表现优于 369。 BP预测：T1 的招牌英雄 Azir、Sejuani、Corki；Top Esports 的招牌英雄 Ezreal、Corki、Leona。T1 应优先禁 Ezreal、Rumble、Ashe，Top Esports 大概率禁 Rell、Sejuani、Tristana。 按当前版本强势英雄算，T1 的 BP 更占便宜。 总结：基本五五开，谁赢都不奇怪。

### S15 2025 世界赛

训练数据截止：2025-10-14（之后的比赛模型都没见过）  
夺冠概率：Gen.G 46%，Hanwha Life Esports 19%，T1 13%，G2 Esports 11%  
**预测冠军：Gen.G**　｜　实际冠军：T1 ❌  
预测 4 强命中 3/4，决赛队伍命中 1/2

| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |
|---|---|---|---|---|---|
| R1M1 | Gen.G vs Hanwha Life Esports | Gen.G | 66% | Gen.G 3-1 | ✅ |
| R1M2 | CTBC Flying Oyster vs KT Rolster | KT Rolster | 79% | KT Rolster 0-3 | ✅ |
| R1M3 | Anyone's Legend vs T1 | T1 | 70% | T1 2-3 | ✅ |
| R1M4 | G2 Esports vs Top Esports | G2 Esports | 63% | Top Esports 1-3 | ❌ |
| R2M1 | Gen.G vs KT Rolster | Gen.G | 92% | KT Rolster 1-3 | ❌ |
| R2M2 | T1 vs Top Esports | T1 | 70% | T1 3-0 | ✅ |
| R3M1 | KT Rolster vs T1 | T1 | 74% | T1 2-3 | ✅ |

**赛前观点（8 强）：**

- **Gen.G vs Hanwha Life Esports**：我看好 Gen.G（系列赛胜率 66%，最可能比分 Gen.G 3:1）。 理由：综合实力分 Gen.G 比 Hanwha Life Esports 高约 88 分。 风险点：Hanwha Life Esports 选手对位输出更高。 位置对比：下路 viper 近期表现优于 ruler；辅助 duro 近期表现优于 delight；上单 kiin 近期表现优于 zeus。 BP预测：Gen.G 的招牌英雄 Gwen、Xin Zhao、Corki；Hanwha Life Esports 的招牌英雄 Xin Zhao、Rell、Taliyah。Gen.G 应优先禁 Poppy、Taliyah、Azir，Hanwha Life Esports 大概率禁 Neeko、Pantheon、Rakan。 总结：有一定爆冷可能。
- **CTBC Flying Oyster vs KT Rolster**：倾向 KT Rolster（系列赛胜率 79%，最可能比分 KT Rolster 3:1）。 理由：KT Rolster 整体硬实力更强（实力分高 330）；KT Rolster 这批首发最近赢得更多；KT Rolster 选手们对线期 KDA 压制更明显。 但是：CTBC Flying Oyster 选手对位输出更高。 位置对比：下路 doggo 近期表现优于 deokdam；上单 driver 近期表现优于 perfect；中单 hongq 近期表现优于 bdd。 BP预测：CTBC Flying Oyster 的招牌英雄 Ezreal、Leona、Azir；KT Rolster 的招牌英雄 Ryze、Alistar、Trundle。CTBC Flying Oyster 应优先禁 Neeko、Rumble、Alistar，KT Rolster 大概率禁 Azir、Yunara、Pantheon。 总结：有一定爆冷可能。
- **Anyone's Legend vs T1**：倾向 T1（系列赛胜率 70%，最可能比分 T1 3:1）。 为什么：T1 整体硬实力更强（实力分高 228）；T1 选手们对线期 KDA 压制更明显；T1 这批首发最近赢得更多。 风险点：Anyone's Legend 选手对位输出更高。 位置对比：下路 hope 近期表现优于 gumayusi；中单 shanks 近期表现优于 faker；辅助 kael 近期表现优于 keria。 BP预测：Anyone's Legend 的招牌英雄 Sion、Poppy、Pantheon；T1 的招牌英雄 Jhin、Gwen、Xin Zhao。Anyone's Legend 应优先禁 Poppy、Azir、Pantheon，T1 大概率禁 Neeko、Annie、Orianna。 总结：有一定爆冷可能。
- **G2 Esports vs Top Esports**：倾向 G2 Esports（系列赛胜率 63%，最可能比分 G2 Esports 3:1）。 为什么：综合实力分 G2 Esports 比 Top Esports 高约 175 分；近期状态：G2 Esports 最近 9胜1负（状态火热），Top Esports 最近 5胜5负（状态一般）；G2 Esports 资源控制更强（推塔、小龙、大龙拿得更多）。 但是：Top Esports 选手们对线期 KDA 压制更明显。 位置对比：打野 skewmond 近期表现优于 kanavi；下路 hans sama 近期表现优于 jackeylove；辅助 labrov 近期表现优于 hang。 BP预测：G2 Esports 的招牌英雄 Alistar、Jax、Taliyah；Top Esports 的招牌英雄 Xin Zhao、Azir、Ryze。G2 Esports 应优先禁 Rumble、Alistar、Azir，Top Esports 大概率禁 Taliyah、Yunara、Orianna。 总结：有一定爆冷可能。
