**Phase 0 — Timestamp & Day# anchor**

**Phase 0 complete:** Run date confirmed 28 June 2026, 04:59 CET. Day# counters — Russia–Ukraine War: **Day 1586**. Iran–US War/Hormuz Crisis: **Day 121**.

**Phase 1 — Direct fetch pass**

**Phase 1 complete — fetch summary:**
- Le Monde ❌ blocked · FAZ ❌ blocked · Kommersant ❌ 404 → search fallback for all three (no retry)
- Xinhua ⚠️ fetched but stale (latest items dated 24 April 2026 — ~65 days stale) → search fallback mandatory
- European Parliament ✅ substantive (latest item 25 June 2026, 3 days old) → usable as Tier 2 background
- ECB press ⚠️ navigation only → search fallback
- EC presscorner ⚠️ metadata only → search fallback
- FAO ✅ **May 2026 index: 130.8, down 0.2 pts (0.2%) MoM; next release 3 July 2026**
- IMF ⚠️ fetched but no <24h news (latest substantive items April 2026) → search fallback for current WEO/news

**Phase 2 — Search pass**

**Phase 1–2 complete.** Pulled fresh reporting across all five categories plus market data (~25 tool calls): Iran/Hormuz ceasefire collapse and renewed US strikes, the Israel–Lebanon framework deal, Russia–Ukraine frontline pressure at Kostyantynivka, Brent's crash on Hormuz reopening, gold/Fed dynamics, IMF WEO growth revisions, May Eurozone inflation, EU Parliament defence/digital-euro news, Hungary's EU-funds deadline, the EU AI Act Omnibus delay, and China's chip-export retaliation.

**Phase 3–5 — Pooling, dedup, editorial filter**

Pool: ~16 candidate stories surfaced across categories → 14 published after filtering (duplicates merged — e.g., the Fox/CNBC/PBS/CNN/WaPo Iran-strike coverage collapsed into one `[MULTI-SOURCE]` Conflict story). Alert cap check: 2 of 14 stories rated 🔴 (14%) — within the 40% ceiling. Now assembling the full brief.

Brief complete and shared. Highlights: lead Conflict story is the US–Iran ceasefire breach and retaliatory strikes (Day 121 of Hormuz crisis), paired with the new Israel–Lebanon framework deal and continued Russia–Ukraine grinding at Kostyantynivka (Day 1586). Business is dominated by Brent's collapse to $72.95 as Hormuz traffic rebuilds. EUR/USD and Brent 7-day deltas are marked N/A this run — same-source weekly comparison points (June 19/21) weren't available in any tool call, so per the no-substitution rule they're left blank rather than estimated.

```yaml
---
brief_date: 2026-06-28
version: v1.3
run_time: "04:59 CET"
stories_published: 14
categories: [conflict, business, eu_affairs, technology, trends]
alert_counts:
  red: 2
  yellow: 9
  green: 3
ongoing_situations:
  - {name: "Russia–Ukraine War", real_world_start: "2022-02-24", day: 1586}
  - {name: "Iran–US War / Hormuz Crisis", real_world_start: "2026-02-28", day: 121}
sources_fetched: 9
fetch_status:
  le_monde: "❌"
  faz: "❌"
  kommersant: "❌"
  xinhua: "⚠️"
  european_parliament: "✅"
expansion_queue: []
---
```

# 🌐 MORNING BRIEF
## Sunday, 28 June 2026 · 04:59 CET
### 14 stories across 5 categories

## DIGEST SUMMARY

| # | Category | Headline | Alert |
|---|----------|----------|-------|
| 1 | ⚔️ Conflict | US strikes Iran after Hormuz ceasefire violation | 🔴 |
| 2 | ⚔️ Conflict | Israel–Lebanon sign trilateral framework agreement | 🟡 |
| 3 | ⚔️ Conflict | Russia presses Kostyantynivka; Ukraine hits Volgograd | 🟡 |
| 4 | 💼 Business | Brent crashes to $72.95 as Hormuz traffic rebuilds | 🔴 |
| 5 | 💼 Business | Gold rallies on dovish PCE read, Fed path in focus | 🟡 |
| 6 | 💼 Business | US equities steady; Treasury Secretary sees lower fuel prices | 🟢 |
| 7 | 🇪🇺 EU Affairs | MEPs back new EU defence innovation programme | 🟡 |
| 8 | 🇪🇺 EU Affairs | Digital euro: MEPs push sovereignty and privacy safeguards | 🟢 |
| 9 | 🇪🇺 EU Affairs | Hungary races August deadline to unlock €17bn in EU funds | 🟡 |
| 10 | 🇪🇺 EU Affairs | MEPs back EU military mobility plan | 🟢 |
| 11 | 🤖 Technology | EU AI Act high-risk deadline still legally August 2, despite Omnibus deal | 🟡 |
| 12 | 🤖 Technology | China adds 10 US firms to export-control list in chip-war tit-for-tat | 🟡 |
| 13 | 📈 Trends | Hormuz shipping and insurance markets slowly re-normalise | 🟡 |
| 14 | 📈 Trends | FAO Food Price Index holds broadly stable amid diverging trends | 🟢 |

> Alert Level key: 🔴 High significance · 🟡 Developing · 🟢 Stable/Routine

## 🚨 SIGNAL BOARD

🔴 **US strikes Iran after Tehran drones hit a cargo ship in the Strait of Hormuz, the first vessel attack since the ceasefire MoU (Day 121)**
---
🔴 **Brent crude falls to $72.95/bbl (−3.07% on the day, >10% on the week) as Hormuz tanker traffic hits its highest level since early June**
---
🟡 **Israel, Lebanon and the US sign a trilateral framework on Hezbollah disarmament — Rubio calls it "the beginning of the beginning"**
---
🟡 **IMF's April reference forecast still puts 2026 global growth at 3.1%, a 0.2pp downgrade from January, with the war seen as the dominant drag**
---
⚡ **Eurozone inflation jumped to 3.2% in May — the highest since September 2023 — driven by a 10.9% surge in energy prices**

---

> 🔎 **CONFLICT ANALYST** · 3 updates today

### 1. Iran / Strait of Hormuz: US strikes Tehran after ceasefire violation 🔴
**Alert:** 🔴
**Summary:** Iran's IRGC struck the Singapore-flagged container ship *Ever Lovely* with a one-way attack drone in the Strait of Hormuz on 25 June, the first vessel attack since the 17 June US–Iran memorandum of understanding. US Central Command retaliated on 26–27 June, striking Iranian missile and drone storage sites, coastal radar and minelaying capabilities; Iran's IRGC said it hit "US terrorist army" positions in response. Trump warned Iran "will no longer exist" if strikes continue. The exchange is the most serious test yet of the interim ceasefire.
**Significance:** Day 121 of the Hormuz crisis shows the reopening remains contested rather than reversed — tanker traffic has rebuilt sharply even as both sides trade fire, leaving the central channel still mined and the IMO's seafarer-evacuation effort paused.
**Sources:**
- [PBS/AP — U.S. strikes Iran in response to drone attack on cargo ship](https://www.pbs.org/newshour/world/u-s-strikes-iran-in-response-to-drone-attack-on-cargo-ship-that-trump-says-violated-ceasefire) · 26 June 2026
- [CNN — Live: Gulf nations under fire again as US-Iran exchanges escalate](https://www.cnn.com/2026/06/27/world/live-news/iran-war-strikes-trump) · 27 June 2026
**Trend:** ⚡ Reversal
**Tags:** #Iran #Hormuz #naval-blockade #missile-strike #MULTI-SOURCE

### 2. Israel–Lebanon: trilateral framework signed in Washington 🟡
**Alert:** 🟡
**Summary:** Israel, Lebanon and the US signed a trilateral framework agreement on 26 June after five rounds of talks in Washington, establishing pilot zones in which the Lebanese Armed Forces take exclusive control from Israeli troops and a structured process to disarm Hezbollah. A new Military Coordination Group for Lebanon (MCG4L) will oversee implementation; the US pledged $100 million in humanitarian aid. Hezbollah was not a party to the deal and its compliance is untested. No durable ceasefire has yet been established — Israel continued limited strikes in southern Lebanon a day after signing.
**Significance:** Rubio called it "the beginning of the beginning"; both Israeli and Lebanese officials stressed the deal does not force a full IDF withdrawal, leaving Hezbollah disarmament and territorial questions unresolved.
**Sources:**
- [NBC News — Israel and Lebanon sign framework agreement with U.S.](https://www.nbcnews.com/world/israel/israel-lebanon-sign-framework-agreement-us-first-step-peace-rubio-says-rcna351973) · 26 June 2026
- [Times of Israel — Israel and Lebanon ink framework deal for ending conflict](https://www.timesofisrael.com/israel-and-lebanon-ink-framework-deal-for-minor-idf-withdrawal-after-4-days-of-dc-talks/) · 27 June 2026
**Trend:** ↘ De-escalating
**Tags:** #Israel #Lebanon #Hezbollah #ceasefire #peace-talks #MULTI-SOURCE

### 3. Russia–Ukraine: Kostyantynivka under pressure, Ukraine hits Volgograd 🟡
**Alert:** 🟡
**Summary:** Russian forces continued grinding assaults toward Kostyantynivka in Donetsk Oblast, with ISW assessing gains as limited infiltrations rather than consolidated control, even as Russian milbloggers claim momentum. Over the past week Russia fired roughly 1,400 attack drones, 1,500 guided bombs and 19 missiles at Ukraine, killing and wounding civilians in Sumy, Kharkiv and Zaporizhzhia. Ukraine struck back with FP-5 "Flamingo" missiles against the Titan-Barikady military-industrial facility in Volgograd. France separately seized a Russian shadow-fleet oil tanker on 25 June.
**Significance:** Day 1586. DeepState data shows Russia's net territorial gains slowing (12 sq mi over the past four weeks vs 21 sq mi the prior period), even as Putin claims Kostyantynivka is nearly encircled.
**Sources:**
- [Critical Threats/ISW — Russian Offensive Campaign Assessment, June 25, 2026](https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-june-25-2026) · 25 June 2026
- [Ukrinform — War](https://www.ukrinform.net/rubric-ato) · 27 June 2026
**Trend:** → Stable
**Tags:** #Russia #Ukraine #frontline #missile-strike #day-1586

📚 *Background reading:* [Russia Matters — The Russia-Ukraine War Report Card](https://www.russiamatters.org/news/russia-ukraine-war-report-card/russia-ukraine-war-report-card-june-24-2026) · [Al Jazeera — What's next in the Strait of Hormuz crisis?](https://www.aljazeera.com/video/inside-story/2026/6/21/whats-next-in-the-strait-of-hormuz-crisis)

---

> 💼 **BUSINESS ANALYST** · 3 updates today

### 1. Brent crashes to $72.95 as Hormuz traffic surges 🔴
**Alert:** 🔴
**Summary:** Brent crude fell to $72.95/bbl on 26 June, down 3.07% on the day and over 10% for the week — its largest weekly drop in a month and the lowest level since 27 February, the day before the war began. Kpler recorded 70 vessel crossings through Hormuz on 24 June (+105% day-on-day, 53 commercial), the highest since early June, as Saudi Arabia resumed loading at Ras Tanura and Gulf producers ramp output. The drone strike on the *Ever Lovely* briefly reversed the slide before the broader de-escalation trend resumed.
**Market signal:** Bearish for oil — the war-risk premium has now fully unwound, with traders pricing supply normalisation over residual conflict risk.
**Sources:**
- [Trading Economics — Brent crude oil](https://tradingeconomics.com/commodity/brent-crude-oil) · 26 June 2026
**Trend:** ↘ De-escalating
**Tags:** #Brent #oil-price #Hormuz #commodities
📎 See also: Conflict § Story 1 — US-Iran ceasefire violation and retaliatory strikes

### 2. Gold rallies on dovish PCE print, Fed path back in focus 🟡
**Alert:** 🟡
**Summary:** Gold rose 1.49% to $4,087/oz on 26 June, a second straight session of gains after May's PCE inflation reading came in broadly as expected, easing fears of additional near-term Fed tightening. Gold remains down roughly 8% over the past month and well below January's record highs reached before the Iran war, with Goldman Sachs cutting its year-end target from $5,400 to $4,900 on 20 June, citing fading ETF inflows and a fully hawkish 2026 rate path.
**Market signal:** Neutral-to-bullish near term — rate-cut repricing offsets a stronger dollar, but the broader trend remains a cooling of the 2026 gold rally.
**Sources:**
- [Trading Economics — Gold](https://tradingeconomics.com/commodity/gold) · 26 June 2026
**Trend:** → Stable
**Tags:** #gold #Fed #interest-rates #commodities

### 3. US equities steady; Treasury Secretary flags falling fuel prices 🟢
**Alert:** 🟢
**Summary:** The S&P 500 closed at 7,354 (−0.05%) and the Dow at 51,876 (−0.09%) on 26 June, with the VIX easing to 18.41. Treasury Secretary Scott Bessent told a conservative policy conference that crude oil is already trading below pre-conflict levels and gasoline prices "are going to come back down," crediting US economic resilience through the war.
**Market signal:** Bullish-to-neutral — calm equity tape and falling energy costs support the soft-landing narrative even as geopolitical risk remains live.
**Sources:**
- [CNBC — U.S. strikes Iran after Trump accuses Tehran of ceasefire violation](https://www.cnbc.com/amp/2026/06/26/us-strikes-iran-strait-of-hormuz-ceasefire.html) · 26 June 2026
**Trend:** → Stable
**Tags:** #SP500 #equity-rally #oil-price

📚 *Background reading:* [CSIS — The Limits of Chip Export Controls in Meeting the China Challenge](https://www.csis.org/analysis/limits-chip-export-controls-meeting-china-challenge)

---

> 🇪🇺 **EU AFFAIRS ANALYST** · 4 updates today

### 1. MEPs back new EU defence innovation programme 🟡
**Alert:** 🟡
**Summary:** Parliament's ITRE and SEDE committees backed a draft law on 24 June to fund fast, low-cost defence innovation cycles, framed explicitly as a response to "the new security environment shaped by Russia's war of aggression against Ukraine."
**Legislative/policy stage:** Committee vote completed; awaiting plenary and Council positions.
**Sources:**
- [European Parliament — MEPs back new EU defence innovation programme](https://www.europarl.europa.eu/news/en/press-room/20260622IPR45932/meps-back-new-eu-defence-innovation-programme) · 25 June 2026
**Trend:** ↗ Escalating
**Tags:** #EU-defence #EU-institutions #institutional

### 2. Digital euro: MEPs push sovereignty and privacy safeguards 🟢
**Alert:** 🟢
**Summary:** Parliament's ECON committee advanced its position on the digital euro on 23 June, emphasising sovereignty, privacy and financial stability, and framing the project as reducing reliance on non-EU payment providers.
**Legislative/policy stage:** Committee position adopted; trilogue negotiations with Council ongoing.
**Sources:**
- [European Parliament — Digital euro: MEPs want to ensure sovereignty, privacy and financial stability](https://www.europarl.europa.eu/news/en/press-room/20260622IPR45912/digital-euro-meps-want-to-ensure-sovereignty-privacy-and-financial-stability) · 23 June 2026
**Trend:** → Stable
**Tags:** #ECB #EU-institutions #FX #digital-regulation

### 3. Hungary races August deadline to unlock €17bn in EU funds 🟡
**Alert:** 🟡
**Summary:** Prime Minister-elect Péter Magyar's Tisza government must satisfy all remaining rule-of-law conditions by end-August to access €10.4bn in Recovery and Resilience Facility funds, plus further cohesion financing, after April's landslide election ended Viktor Orbán's 16-year rule. Magyar has pledged anti-corruption and judicial-independence reforms; one cohesion tranche is conditional on reversing prior anti-LGBTQ+ and asylum legislation.
**Legislative/policy stage:** Political agreement with Commission President von der Leyen reached in late May; revised national recovery plan and reform milestones due before the August deadline.
**Sources:**
- [Euronews — Hungary's Magyar heads to Brussels to reset EU ties and unlock frozen funds](https://www.euronews.com/my-europe/2026/05/27/hungarys-magyar-heads-to-brussels-to-reset-eu-ties-and-unlock-frozen-funds) · 27 May 2026
**Trend:** ↗ Escalating
**Tags:** #Hungary #Magyar #EU-funds #rule-of-law

### 4. MEPs back EU military mobility plan 🟢
**Alert:** 🟢
**Summary:** The SEDE and TRAN committees gave a first green light on 23 June to plans easing cross-border transport of military equipment and troops across the EU, intended to improve deterrence against possible aggression.
**Legislative/policy stage:** First committee approval; full Parliament vote pending.
**Sources:**
- [European Parliament — MEPs in favour of facilitating military mobility](https://www.europarl.europa.eu/news/en/press-room/20260622IPR45908/meps-in-favour-of-facilitating-military-mobility) · 23 June 2026
**Trend:** ↗ Escalating
**Tags:** #EU-defence #EU-institutions #institutional

📚 *Background reading:* [ECFR — Tisza's foreign policy offer: Plans for a post-Orban Hungary](https://ecfr.eu/article/tiszas-foreign-policy-offer-plans-for-a-post-orban-hungary/) · [Bruegel — EU economics coverage]

---

> 🤖 **TECHNOLOGY ANALYST** · 2 updates today

### 1. EU AI Act: high-risk deadline still legally 2 August despite Omnibus deal 🟡
**Alert:** 🟡
**Summary:** Although EU lawmakers reached a 7 May political agreement to push the AI Act's high-risk compliance deadline from August 2026 to December 2027, that deal has not yet been enacted into law. As of this week, 2 August 2026 remains the operative date on which Articles 9–17 and Article 26 become enforceable for deployers of Annex III high-risk systems, with penalties up to €15m or 3% of global turnover. Separately, Article 50 transparency duties (chatbot disclosure, deepfake labelling) take effect on schedule regardless of the Omnibus outcome.
**Analyst note:** Enterprises betting on the delay materialising risk a compliance gap if formal adoption — expected around July — slips past the original deadline; legal advisers are uniformly telling clients to keep building toward August.
**Sources:**
- [Kiteworks — EU AI Act August 2, 2026 Deadline Is Six Weeks Away](https://www.kiteworks.com/regulatory-compliance/eu-ai-act-deadline-compliance/) · 23 June 2026
**Trend:** → Stable
**Tags:** #AI-regulation #digital-regulation #institutional
📎 See also: EU Affairs § Story 2 — Digital euro sovereignty debate

### 2. China adds 10 US firms to export-control list in chip-war tit-for-tat 🟡
**Alert:** 🟡
**Summary:** Beijing's Commerce Ministry added 10 US firms, including a rare-earth miner, to its export-control list on 22 June, in retaliation for the Pentagon's early-June designation of roughly 80 Chinese firms — including Alibaba, Baidu and BYD — as "Chinese military companies." Separately, the US Bureau of Industry and Security clarified on 1 June that advanced AI chip licensing requirements apply to all China-headquartered firms' subsidiaries worldwide, closing a loophole Nvidia said it was already complying with.
**Analyst note:** Both moves are largely symbolic for now, but analysts say the parallel escalation in entity-listing breadth signals further controls are likely over the next 12–24 months regardless of diplomatic optics at recent Trump–Xi talks.
**Sources:**
- [Al Jazeera — China adds 10 US firms, including rare-earth miner, to export control list](https://www.aljazeera.com/news/2026/6/22/china-adds-10-us-firms-including-rare-earth-miner-to-export-control-list) · 22 June 2026
**Trend:** ↗ Escalating
**Tags:** #semiconductor #sanctions #AI-regulation

📚 *Background reading:* [CNAS — The Export Control Loophole Fueling China's Chip Production](https://www.cnas.org/publications/cnas-insights/cnas-insights-the-export-control-loophole-fueling-chinas-chip-production)

---

> 📈 **TRENDS ANALYST** · 2 updates today

### 1. Hormuz shipping and insurance markets slowly re-normalise 🟡
**Alert:** 🟡
**Summary:** Four months into the crisis, tanker traffic through Hormuz remains well below the pre-war baseline of 125–140 vessels/day even as flows rebuild — Kpler counted 70 crossings on 24 June, still a fraction of normal. Iran has mandated specific IRGC-designated transit corridors, and the IMO paused its seafarer-evacuation programme after the 25 June projectile strike on a vessel off Oman. War-risk insurance premiums, which jumped from 0.125% to 0.2–0.4% of vessel value per transit, have not fully reverted, and shipping lines remain reluctant to resume full schedules pending a firmer security guarantee.
**Horizon:** Medium-term — full normalisation of shipping confidence and insurance pricing is likely to lag the headline ceasefire by months, contingent on a durable US–Iran peace agreement.
**Sources:**
- [CNBC — Oil tanker traffic in Strait of Hormuz jumps after U.S. and Iran implement deal](https://www.cnbc.com/2026/06/19/iran-oil-tanker-traffic-strait-hormuz-gulf-vlcc.html) · 19 June 2026
**Trend:** ↗ Escalating
**Tags:** #shipping #Hormuz #naval-blockade #supply-shock
📎 See also: Business § Story 1 — Brent crash on Hormuz reopening

### 2. FAO Food Price Index holds broadly stable amid diverging trends 🟢
**Alert:** 🟢
**Summary:** The FAO Food Price Index averaged 130.8 points in May 2026, down 0.2 points (0.2%) from April but 2.9% above a year earlier. Cereal and sugar prices rose — wheat for a fourth straight month on weak US winter-wheat conditions and higher fuel/fertiliser costs — while vegetable oil and dairy prices declined. The next release, covering June data, is due 3 July 2026.
**Horizon:** Short-to-medium-term — sugar's 7.5% monthly jump on tightening Brazilian and Indian supply expectations is the component to watch into Q3.
**Sources:**
- [FAO — FAO Food Price Index](https://www.fao.org/worldfoodsituation/foodpricesindex/en) · 5 June 2026 (May 2026 data — latest available)
**Trend:** → Stable
**Tags:** #food-prices #food-security #commodities

📚 *Background reading:* [Al Jazeera — Israel and Lebanon agreement coverage] · [Kyiv Independent — Ukraine/Russia frontline analysis]

---

## 📊 KEY DATA OF THE DAY

📊 **DATA OFFICER** · 7 indicators

| Indicator | Value | Δ vs prior session | Δ vs 7 days ago | Note | Source | URL |
|-----------|-------|-------------------|-----------------|------|--------|-----|
| EUR/USD | 1.1390 | +0.11% | N/A | Close 26 June; dollar firm on hawkish Fed repricing | Yahoo Finance / Trading Economics | [link](https://finance.yahoo.com/quote/EURUSD=X/) |
| Brent Crude (USD/bbl) | 72.95 | −3.07% | N/A | Lowest since 27 Feb 2026, pre-war close; Hormuz traffic rebuilding | Trading Economics | [link](https://tradingeconomics.com/commodity/brent-crude-oil) |
| Gold (XAU/USD) | 4,087.01 | +1.49% | N/A | Second straight gain on in-line May PCE print | Trading Economics | [link](https://tradingeconomics.com/commodity/gold) |
| IMF Global Growth 2026 | 3.1% | vs Jan WEO: −0.2pp | vs Oct WEO: 0.0pp | April reference forecast; war seen as dominant drag | IMF WEO | [link](https://www.imf.org/en/publications/weo/issues/2026/04/14/world-economic-outlook-april-2026) |
| EU CPI YoY (latest) | 3.2% | vs prior month: +0.2pp | vs 3 months ago: +1.3pp | May 2026; highest since Sep 2023, energy +10.9% YoY | Eurostat | [link](https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-17062026-ap) |
| FAO Food Price Index | 130.8 | vs prior month: −0.2% | May 2026 (latest available) | Cereals/sugar up, oils/dairy down | FAO | [link](https://www.fao.org/worldfoodsituation/foodpricesindex/en) |
| Strait of Hormuz daily transits (Kpler) | 70 vessels (24 Jun) | +105% | N/A | 53/70 commercial; still well below 125–140/day pre-war baseline | Kpler (via CNBC) | [link](https://www.cnbc.com/2026/06/19/iran-oil-tanker-traffic-strait-hormuz-gulf-vlcc.html) |

**Data commentary:** Oil's de-escalation is the day's dominant signal — Brent has erased the entire war premium as Hormuz throughput rebuilds, directly easing the inflation and growth pressures the IMF flagged in April. But the move is not yet a clean "all clear": EU inflation just hit a three-year high on lagged energy effects, Hormuz transit volumes remain a fraction of normal, and Friday's drone-and-strike exchange shows the ceasefire underpinning the oil rally is still fragile. Gold's modest rebound reflects markets pricing a calmer rate path even as the conflict's macro scars (IMF's 3.1% growth call, still 0.2pp below January) persist.

---

## ⚙️ AGENT METADATA

| Field | Value |
|-------|-------|
| Agent version | MORNING BRIEF v1.3 |
| Run timestamp | 2026-06-28T04:59:06+02:00 |
| Fetch status | Le Monde ❌ · FAZ ❌ · Kommersant ❌ · Xinhua ⚠️ (stale, 24 Apr) · EP ✅ |
| Sources queried | 9 / 11 |
| Stories surfaced | 18 (before editorial filter) |
| Stories published | 14 |
| Languages processed | EN |
| Output language | English (British) |
| Date validated | ✅ Confirmed 28 June 2026 |
| Expansion Queue | None |

---

MORNING BRIEF is an AI-assisted digest. All summaries are paraphrased from original sources.
Verify time-sensitive information at the linked URLs before acting.
Output language: British English.
