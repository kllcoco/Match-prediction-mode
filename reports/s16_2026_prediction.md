# S16（2026 英雄联盟全球总决赛）预测

- 生成时间：2026-10-28 18:32 UTC；数据截至：2026-10-26 20:55（已包含本届入围赛和瑞士轮已赛结果）
- 方法：完整模式模型（看过所有往届大赛）+ 蒙特卡洛模拟剩余瑞士轮和淘汰赛 20000 次
- **预测冠军：Gen.G**（夺冠概率 43%）

| 队伍 | 赛区 | 瑞士轮战绩 | 进8强 | 进4强 | 进决赛 | 夺冠 |
|---|---|---|---|---|---|---|
| Gen.G | LCK | 3-0 | 100% | 75% | 57% | 43.2% |
| DWG KIA | LCK | 3-0 | 100% | 68% | 41% | 16.0% |
| T1 | LCK | 2-1 | 87% | 58% | 24% | 11.4% |
| Bilibili Gaming | LPL | 2-1 | 83% | 40% | 18% | 8.1% |
| Hanwha Life Esports | LCK | 1-2 | 45% | 30% | 12% | 4.8% |
| Top Esports | LPL | 2-1 | 75% | 30% | 12% | 4.2% |
| Invictus Gaming | LPL | 2-1 | 72% | 26% | 9% | 3.1% |
| Karmine Corp | LEC | 1-2 | 34% | 12% | 6% | 2.5% |
| Movistar KOI | LEC | 2-1 | 68% | 24% | 8% | 2.3% |
| G2 Esports | LEC | 1-2 | 31% | 11% | 5% | 2.0% |
| LYON | LCS | 2-1 | 66% | 20% | 6% | 1.9% |
| Team Liquid | LCS | 1-2 | 19% | 5% | 2% | 0.4% |
| LOS | CBLOL | 1-2 | 15% | 3% | 1% | 0.2% |
| CTBC Flying Oyster | PCS | 1-2 | 6% | 0% | 0% | 0.0% |
| Anyone's Legend | LPL | 0-3 | 0% | 0% | 0% | 0.0% |
| Secret Whales | PCS | 0-3 | 0% | 0% | 0% | 0.0% |

## 模型观点

夺冠热门前四：Gen.G、DWG KIA、T1、Bilibili Gaming。下面是热门之间的假想对决：

- **Gen.G vs DWG KIA**：我的判断：Gen.G 晋级（系列赛胜率 76%，最可能比分 Gen.G 3:1）。 为什么：Gen.G 整体硬实力更强（实力分高 122）；Gen.G 选手对位输出更高。 但是：DWG KIA 这批首发最近赢得更多。 位置对比：下路 ruler 近期表现优于 smash；上单 kiin 近期表现优于 siwoo；打野 canyon 近期表现优于 lucid。 BP预测：Gen.G 的招牌英雄 Ezreal、Lee Sin、Seraphine；DWG KIA 的招牌英雄 Jarvan IV、Viktor、Jayce。Gen.G 应优先禁 Tryndamere、aurora、tristana，DWG KIA 大概率禁 nami、hwei、sylas。 按当前版本强势英雄算，Gen.G 的 BP 更占便宜。 总结：有一定爆冷可能。

**无畏征召 BP 推演**（用过的英雄后面不能再选；英雄池深度 Gen.G 14 个英雄 vs DWG KIA 14 个英雄）：
- 第1局：Gen.G Ezreal/Lee Sin/Seraphine/Jhin/Ryze　vs　DWG KIA Jarvan IV/Viktor/Jayce/K'Sante/Xin Zhao
- 第2局：Gen.G Ambessa/Karma/Rumble/Galio/Shen　vs　DWG KIA Lucian/Syndra/Vi/Milio/Orianna
- 第3局：Gen.G Skarner/Olaf/Ashe/Anivia/Lulu　vs　DWG KIA Gnar/Yunara/Bard/Caitlyn/Taliyah
- 第4局：Gen.G Annie/Rakan/Wukong/Sion/Nocturne　vs　DWG KIA Naafiri/Cassiopeia/Camille/Sivir/Ahri
- 第5局：Gen.G Pantheon/Nautilus/Renata Glasc/Kalista/Akali　vs　DWG KIA Trundle/Aurora/Twisted Fate/Jax/Miss Fortune
- **Gen.G vs T1**：我的判断：Gen.G 晋级（系列赛胜率 79%，最可能比分 Gen.G 3:1）。 理由：综合实力分 Gen.G 比 T1 高约 162 分；Gen.G 选手对位输出更高；近期状态：Gen.G 最近 8胜2负（状态火热），T1 最近 5胜5负（状态一般）。 不过要注意：T1 这批首发最近赢得更多。 位置对比：打野 canyon 近期表现优于 oner；中单 chovy 近期表现优于 faker；上单 kiin 近期表现优于 doran。 BP预测：Gen.G 的招牌英雄 Ezreal、Lee Sin、Seraphine；T1 的招牌英雄 Vi、Jayce、Xin Zhao。Gen.G 应优先禁 Tryndamere、aurora、tristana，T1 大概率禁 nami、hwei、sylas。 总结：有一定爆冷可能。

**无畏征召 BP 推演**（用过的英雄后面不能再选；英雄池深度 Gen.G 14 个英雄 vs T1 14 个英雄）：
- 第1局：Gen.G Ezreal/Lee Sin/Ryze/Jhin/Ambessa　vs　T1 Vi/Jayce/Jarvan IV/Rumble/Orianna
- 第2局：Gen.G Seraphine/Karma/Galio/Shen/Anivia　vs　T1 Xin Zhao/Milio/Lucian/Camille/Caitlyn
- 第3局：Gen.G Olaf/Syndra/Nocturne/Skarner/Ashe　vs　T1 Lulu/Cassiopeia/Akali/Gnar/Wukong
- 第4局：Gen.G Pantheon/Naafiri/Sion/Bard/Rakan　vs　T1 Renata Glasc/K'Sante/Alistar/Kalista/Taliyah
- 第5局：Gen.G Annie/Nautilus/Varus/Ziggs/Mel　vs　T1 Yorick/Yunara/Renekton/Neeko/Sivir
- **Gen.G vs Bilibili Gaming**：我看好 Gen.G（系列赛胜率 67%，最可能比分 Gen.G 3:1）。 理由：综合实力分 Gen.G 比 Bilibili Gaming 高约 251 分；Gen.G 选手对位输出更高。 不过要注意：pool。 位置对比：中单 knight 近期表现优于 chovy；上单 kiin 近期表现优于 bin；下路 ruler 近期表现优于 viper (korean player)。 BP预测：Gen.G 的招牌英雄 Ezreal、Lee Sin、Seraphine；Bilibili Gaming 的招牌英雄 Jarvan IV、Lee Sin、Jayce。Gen.G 应优先禁 Tryndamere、aurora、tristana，Bilibili Gaming 大概率禁 nami、hwei、sylas。 按当前版本强势英雄算，Gen.G 的 BP 更占便宜。 总结：有一定爆冷可能。

**无畏征召 BP 推演**（用过的英雄后面不能再选；英雄池深度 Gen.G 14 个英雄 vs Bilibili Gaming 16 个英雄）：
- 第1局：Gen.G Lee Sin/Ezreal/Seraphine/Ambessa/Ryze　vs　Bilibili Gaming Jarvan IV/Rumble/Jayce/Camille/K'Sante
- 第2局：Gen.G Karma/Jhin/Shen/Skarner/Syndra　vs　Bilibili Gaming Bard/Naafiri/Pantheon/Orianna/Vi
- 第3局：Gen.G Galio/Anivia/Ashe/Olaf/Lulu　vs　Bilibili Gaming Akali/Cassiopeia/Gnar/Alistar/Rakan
- 第4局：Gen.G Nautilus/Nocturne/Xin Zhao/Annie/Sion　vs　Bilibili Gaming Renekton/Viktor/Ahri/Milio/Aurora
- 第5局：Gen.G Renata Glasc/Wukong/Caitlyn/Lucian/Mel　vs　Bilibili Gaming Poppy/Yorick/Twisted Fate/Trundle/Qiyana
- **DWG KIA vs T1**：我看好 DWG KIA（系列赛胜率 53%，最可能比分 DWG KIA 3:1）。 理由：从长期战绩算出来的实力分看，DWG KIA 领先 T1 约 40 分；近期状态：DWG KIA 最近 6胜4负（状态不错），T1 最近 5胜5负（状态一般）。 不过要注意：T1 选手对位输出更高。 位置对比：下路 peyz 近期表现优于 smash；上单 doran 近期表现优于 siwoo；中单 showmaker 近期表现优于 faker。 BP预测：DWG KIA 的招牌英雄 Jarvan IV、Viktor、Jayce；T1 的招牌英雄 Vi、Jayce、Xin Zhao。DWG KIA 应优先禁 Tryndamere、aurora、tristana，T1 大概率禁 nami、hwei、Gangplank。 按当前版本强势英雄算，T1 的 BP 更占便宜。 总结：基本五五开，谁赢都不奇怪。

**无畏征召 BP 推演**（用过的英雄后面不能再选；英雄池深度 DWG KIA 14 个英雄 vs T1 14 个英雄）：
- 第1局：DWG KIA Jarvan IV/Viktor/Jayce/K'Sante/Xin Zhao　vs　T1 Vi/Orianna/Ryze/Lee Sin/Jhin
- 第2局：DWG KIA Lucian/Milio/Lulu/Syndra/Ezreal　vs　T1 Ambessa/Caitlyn/Rumble/Camille/Anivia
- 第3局：DWG KIA Karma/Gnar/Yunara/Seraphine/Taliyah　vs　T1 Olaf/Cassiopeia/Bard/Wukong/Naafiri
- 第4局：DWG KIA Ashe/Shen/Skarner/Annie/Rakan　vs　T1 Nocturne/Akali/Pantheon/Renata Glasc/Galio
- 第5局：DWG KIA Sivir/Trundle/Jax/Sion/Ahri　vs　T1 Alistar/Kalista/Renekton/Mel/Lux
- **DWG KIA vs Bilibili Gaming**：倾向 DWG KIA（系列赛胜率 59%，最可能比分 DWG KIA 3:1）。 为什么：综合实力分 DWG KIA 比 Bilibili Gaming 高约 129 分；DWG KIA 最近手感比对手好（DWG KIA 6-4，Bilibili Gaming 6-4，比赛结果都好于赛前预期）；DWG KIA 这批首发最近赢得更多。 风险点：Bilibili Gaming 选手对位输出更高。 位置对比：中单 knight 近期表现优于 showmaker；下路 viper (korean player) 近期表现优于 smash；辅助 on 近期表现优于 career。 BP预测：DWG KIA 的招牌英雄 Jarvan IV、Viktor、Jayce；Bilibili Gaming 的招牌英雄 Jarvan IV、Lee Sin、Jayce。DWG KIA 应优先禁 Tryndamere、aurora、tristana，Bilibili Gaming 大概率禁 nami、hwei、Gangplank。 按当前版本强势英雄算，Bilibili Gaming 的 BP 更占便宜。 总结：基本五五开，谁赢都不奇怪。

**无畏征召 BP 推演**（用过的英雄后面不能再选；英雄池深度 DWG KIA 14 个英雄 vs Bilibili Gaming 16 个英雄）：
- 第1局：DWG KIA Jarvan IV/Viktor/Jayce/K'Sante/Xin Zhao　vs　Bilibili Gaming Lee Sin/Seraphine/Ambessa/Orianna/Rumble
- 第2局：DWG KIA Milio/Vi/Syndra/Lulu/Karma　vs　Bilibili Gaming Bard/Camille/Ryze/Naafiri/Pantheon
- 第3局：DWG KIA Lucian/Gnar/Jhin/Ezreal/Taliyah　vs　Bilibili Gaming Cassiopeia/Akali/Rakan/Alistar/Renekton
- 第4局：DWG KIA Ashe/Yunara/Skarner/Shen/Caitlyn　vs　Bilibili Gaming Annie/Ahri/Aurora/Sion/Nautilus
- 第5局：DWG KIA Olaf/Wukong/Jax/Trundle/Twisted Fate　vs　Bilibili Gaming Poppy/Mel/Renata Glasc/Yorick/Anivia
- **T1 vs Bilibili Gaming**：倾向 T1（系列赛胜率 60%，最可能比分 T1 3:1）。 理由：从长期战绩算出来的实力分看，T1 领先 Bilibili Gaming 约 89 分；T1 这批首发最近赢得更多；T1 选手对位输出更高。 不过要注意：pool。 位置对比：中单 knight 近期表现优于 faker；上单 doran 近期表现优于 bin；打野 xun 近期表现优于 oner。 BP预测：T1 的招牌英雄 Vi、Jayce、Xin Zhao；Bilibili Gaming 的招牌英雄 Jarvan IV、Lee Sin、Jayce。T1 应优先禁 Tryndamere、aurora、tristana，Bilibili Gaming 大概率禁 nami、hwei、Gangplank。 按当前版本强势英雄算，Bilibili Gaming 的 BP 更占便宜。 总结：基本五五开，谁赢都不奇怪。

**无畏征召 BP 推演**（用过的英雄后面不能再选；英雄池深度 T1 14 个英雄 vs Bilibili Gaming 16 个英雄）：
- 第1局：T1 Vi/Jayce/Ambessa/Lee Sin/Orianna　vs　Bilibili Gaming Jarvan IV/Rumble/Seraphine/Camille/K'Sante
- 第2局：T1 Ryze/Xin Zhao/Milio/Ezreal/Cassiopeia　vs　Bilibili Gaming Naafiri/Bard/Pantheon/Akali/Gnar
- 第3局：T1 Jhin/Lulu/Anivia/Lucian/Caitlyn　vs　Bilibili Gaming Karma/Alistar/Renekton/Viktor/Syndra
- 第4局：T1 Nocturne/Olaf/Wukong/Renata Glasc/Rakan　vs　Bilibili Gaming Shen/Ahri/Sion/Skarner/Annie
- 第5局：T1 Ashe/Taliyah/Yorick/Mel/Galio　vs　Bilibili Gaming Aurora/Nautilus/Poppy/Trundle/Twisted Fate

## 已赛瑞士轮结果

- 10-23 Gen.G 1:0 Invictus Gaming
- 10-23 Hanwha Life Esports 1:0 Top Esports
- 10-23 Bilibili Gaming 0:1 Movistar KOI
- 10-23 Anyone's Legend 0:1 Karmine Corp
- 10-23 DWG KIA 1:0 G2 Esports
- 10-23 CTBC Flying Oyster 1:0 Team Liquid
- 10-23 LOS 0:1 T1
- 10-24 LYON 1:0 Secret Whales
- 10-24 Anyone's Legend 0:1 Top Esports
- 10-24 CTBC Flying Oyster 0:1 Movistar KOI
- 10-24 G2 Esports 1:0 LOS
- 10-24 Karmine Corp 0:1 LYON
- 10-24 Invictus Gaming 1:0 Secret Whales
- 10-24 Gen.G 1:0 Hanwha Life Esports
- 10-24 DWG KIA 1:0 T1
- 10-25 Bilibili Gaming 1:0 Team Liquid
- 10-25 Hanwha Life Esports 0:1 Invictus Gaming
- 10-25 G2 Esports 0:1 Top Esports
- 10-25 DWG KIA 2:0 Movistar KOI
- 10-25 Gen.G 2:1 LYON
- 10-26 CTBC Flying Oyster 0:1 T1
- 10-26 Bilibili Gaming 1:0 Karmine Corp
- 10-26 LOS 2:0 Secret Whales
- 10-26 Anyone's Legend 0:2 Team Liquid

> 存档：`predictions/s16_2026_20261028.json`。世界赛结束后运行 `python -m esports.s16 grade` 判卷。