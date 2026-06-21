Starting the run. Phase 0 confirmed: **21 June 2026, 05:00 CET**.
---
**Day-count calculations (Phase 0):**
- Russia–Ukraine War (start 24 Feb 2022) → Day 1,579
- Iran–US War/Hormuz Crisis (start 28 Feb 2026, corrected) → Day 114
- Israel–Lebanon Ceasefire (need to confirm start date — will verify in Phase 1/2)
---
Proceeding to Phase 1 — direct fetch pass.
---
Phase 1 complete. Fetch status: Le Monde ❌, FAZ ❌, Kommersant ❌, Xinhua ⚠️ (stale), European Parliament ⚠️ (stale), FAO ✅ (May 2026 data), IMF ⚠️ (stale), ECB ❌ (nav only), European Commission ❌ (no content). Proceeding to Phase 2 — search pass.
---
Phase 2 search complete across all six query categories. Moving to Phase 3–5 (pooling, dedup, editorial filter) — pool surfaced ~19 candidate stories, filtered to 14 for publication. Red-alert cap check: 2 of 14 stories (14%) flagged 🔴, well under the 40% ceiling. Tag check: all selected tags map to the closed list — no Expansion Queue entries this run. Charts: both Chart 1 (Brent trajectory) and Chart 2 (Hormuz transit series) fail the "no fabricated/estimated points" test this run — available figures are either too sparse (2–3 confirmed dated points) or actively contested between IRGC and CENTCOM reporting — so both are omitted rather than approximated. Proceeding to final assembly.

---

```yaml
---
brief_date: 2026-06-21
version: v1.2.2
run_time: "05:00 CEST"
stories_published: 14
categories: [conflict, business, eu_affairs, technology, trends]
alert_counts:
  red: 2
  yellow: 8
  green: 4
ongoing_situations:
  - {name: "Russia–Ukraine War", real_world_start: "2022-02-24", day: 1579}
  - {name: "Iran–US War / Hormuz Crisis", real_world_start: "2026-02-28", day: 114}
  - {name: "Israel–Lebanon Ceasefire 2026", real_world_start: "2026-06-19", day: 3}
sources_fetched: 9
fetch_status:
  le_monde: "❌"
  faz: "❌"
  kommersant: "❌"
  xinhua: "⚠️"
  european_parliament: "⚠️ (used for EU Affairs, no stories within strict 24h)"
expansion_queue: []
---
```

# 🌐 MORNING BRIEF
## Sunday, 21 June 2026 · 05:00 CEST
### 14 stories across 5 categories

## DIGEST SUMMARY

| # | Category | Headline | Alert |
|---|----------|----------|-------|
| 1 | ⚔️ Conflict | Iran re-declares Hormuz closure; CENTCOM disputes | 🔴 |
| 2 | ⚔️ Conflict | Israel–Lebanon ceasefire violated within hours | 🔴 |
| 3 | ⚔️ Conflict | Ukraine's Moscow strike exposes Russian air-defence gaps | 🟡 |
| 4 | 💼 Business | Brent steadies near $80 despite renewed Hormuz threat | 🟡 |
| 5 | 💼 Business | Gold slides to two-week low as hawkish Fed lifts dollar | 🟡 |
| 6 | 💼 Business | Intel-led rally lifts Nasdaq 1.91% into Juneteenth close | 🟢 |
| 7 | 🇪🇺 EU Affairs | Commission's 21st Russia sanctions package advances | 🟡 |
| 8 | 🇪🇺 EU Affairs | Metsola: EU "doesn't have luxury of time" on enlargement, MFF | 🟢 |
| 9 | 🇪🇺 EU Affairs | AI Act Digital Omnibus nears formal adoption | 🟡 |
| 10 | 🤖 Technology | Apple-Intel chip tie-up signals US foundry reshoring push | 🟢 |
| 11 | 🤖 Technology | US holds off blacklisting DeepSeek despite security flags | 🟡 |
| 12 | 📈 Trends | Hormuz transits still 93–94% below pre-crisis levels | 🟡 |
| 13 | 📈 Trends | FAO Food Price Index holds broadly stable in May | 🟢 |
| 14 | 📈 Trends | Pakistan's mediator role deepens as Vance heads to Geneva | 🟡 |

> Alert Level key: 🔴 High significance · 🟡 Developing · 🟢 Stable/Routine

## 🚨 SIGNAL BOARD

🔴 Iran's military has re-declared the Strait of Hormuz closed; CENTCOM says 55 vessels transited regardless — a direct factual dispute over the MoU's core deliverable.
🔴 Israeli strikes killed 16–50 people in south Lebanon overnight Friday–Saturday, within 24 hours of a US-brokered ceasefire announcement.
🟡 Brent crude is still down ~8.5% on the week despite Saturday's closure rhetoric — markets have not yet repriced for the renewed threat.
🟡 Eurozone HICP inflation hit 3.2% in May, the highest since September 2023, with energy contributing +0.98pp.
🟢 US equities rallied into the Juneteenth close, led by a 10.6% Intel surge on a Trump-brokered Apple chip-manufacturing tie-up.

## 🔄 ONGOING SITUATIONS

| Situation | Real-world start | Day # | Last significant development | Status |
|-----------|-----------------|-------------|------------------------------|--------|
| Russia–Ukraine War | 24 Feb 2022 | Day 1579 | Ukraine's 18 June strike on Moscow exposed Russian air-defence gaps; Russian drones killed 1, injured 5 on Black Sea merchant vessels | 🔴 Active |
| Iran–US War / Hormuz Crisis | 28 Feb 2026 | Day 114 | Iran's military re-declared the Strait closed on 20 June; US disputes the claim and reports continued transits | 🔴 Active |
| Israel–Lebanon Ceasefire 2026 | 19 Jun 2026 | Day 3 | Ceasefire announced Friday violated within hours; Israeli strikes killed up to 50, Hezbollah fired ~50 rockets in response | 🔴 Active (violated) |

---

> 🔎 **CONFLICT ANALYST** · 3 updates today

### 1. Iran re-declares Hormuz closure as Lebanon escalation derails MoU 🔴

**Alert:** 🔴
**Summary:** Iran's joint military command formally re-declared the Strait of Hormuz closed on Saturday, citing Israeli strikes on Hezbollah and what it called US "bad faith" breaches of the 17 June US–Iran memorandum of understanding. US Central Command disputed the claim, saying 55 vessels transited the strait regardless and that "Iran does not control" it. Vice President JD Vance departed for Geneva talks despite the dispute, with Pakistan's PM and army chief also travelling to mediate.
**Significance:** The clash over verifiable facts — not just intent — suggests the MoU's central deliverable (reopening Hormuz) remains contested territory rather than settled fact, raising re-escalation risk into Sunday's talks.
**Sources:**
- [MS NOW — Iran says Strait of Hormuz is closed, citing Israeli attacks in Lebanon](https://www.ms.now/news/iran-says-strait-of-hormuz-is-closed-citing-israeli-attacks-in-lebanon) · 20 June 2026
- [Al Jazeera — Iran claims it coordinated passage of 26 vessels out of Hormuz in 24 hours](https://www.aljazeera.com/news/2026/5/20/iran-says-it-coordinated-crossing-of-26-vessels-out-of-strait-of-hormuz) · 20 May 2026
**Trend:** ⚡ Reversal
**Tags:** #Iran #Hormuz #naval-blockade #escalation

### 2. Israel–Lebanon ceasefire violated within hours of taking effect 🔴
**Alert:** 🔴
**Summary:** A US-brokered Israel–Hezbollah ceasefire announced Friday was violated overnight: Lebanon's civil defence agency said Israeli strikes killed at least 16 people in the south, with other reporting citing up to 50 dead, including marine scientist Mona Khalil, 77. Hezbollah responded Saturday with roughly 50 rockets at IDF positions. US intelligence reportedly assesses Netanyahu is likely to keep striking regardless of the ceasefire's effect on US–Iran talks.
**Significance:** This is at least the fourth Israel–Lebanon ceasefire attempt since March; the pattern of near-immediate violation undercuts confidence that any framework can hold without an enforcement mechanism.
**Sources:**
- [New Age — Israel, Hezbollah agree Lebanon ceasefire: US official](https://www.newagebd.net/post/middle-east/303266/israel-hezbollah-agree-lebanon-ceasefire-us-official) · 19 June 2026
- [MS NOW — Iran says Strait of Hormuz is closed, citing Israeli attacks in Lebanon](https://www.ms.now/news/iran-says-strait-of-hormuz-is-closed-citing-israeli-attacks-in-lebanon) · 20 June 2026
**Trend:** ↗ Escalating
**Tags:** #Israel #Lebanon #Hezbollah #ceasefire

### 3. Ukraine's Moscow strike exposes Russian air-defence gaps 🟡
**Alert:** 🟡
**Summary:** Ukraine's 18 June strikes on Moscow exposed weaknesses in Russian air defences, prompting rare public criticism of state media from pro-war Russian bloggers over downplaying the attack. Separately, Russian drones struck two civilian merchant vessels (Panama- and St Kitts-and-Nevis-flagged) in the Black Sea, killing one crew member and injuring five. Russia has concentrated roughly 11,000 troops near Kostiantynivka; ISW assesses Moscow is exaggerating gains there.
**Significance:** The front remains in attritional stalemate per ISW-aligned analysis, but the Moscow strike and shipping attacks indicate both sides are extending reach beyond the contact line.
**Sources:**
- [RBC-Ukraine — Russia's losses in Ukraine as of June 20](https://newsukraine.rbc.ua/news/russia-s-losses-in-ukraine-as-of-june-20-1781884876.html) · 20 June 2026
**Trend:** → Stable
**Tags:** #Russia #Ukraine #frontline #drone-warfare

📚 *Background reading:* [Britannica — 2026 Iran war](https://www.britannica.com/event/2026-Iran-war) · [House of Commons Library — Reopening the Strait of Hormuz](https://commonslibrary.parliament.uk/research-briefings/cbp-10636/)

---

> 💼 **BUSINESS ANALYST** · 3 updates today

### 1. Brent steadies near $80 despite renewed Hormuz closure threat 🟡
**Alert:** 🟡
**Summary:** Brent crude closed Friday near $80.57/bbl, on track for a roughly 8.5% weekly decline that has erased most of the war-premium built up since February, as shipping conditions improved following the US–Iran interim accord. Kuwait said it would raise output; CENTCOM lifted restrictions on Iranian port traffic. Saturday's renewed Iranian closure declaration had not yet been reflected in pricing as of Friday's close.
**Market signal:** Bearish near-term — the deal-driven supply-recovery narrative still dominates pricing, but Monday's open is the first test of whether Saturday's closure claim triggers a reversal.
📎 *See also: Conflict § Story 1 — Iran's renewed Hormuz closure declaration.*
**Sources:**

- [Trading Economics — Brent crude oil](https://tradingeconomics.com/commodity/brent-crude-oil) · 19 June 2026
**Trend:** ↘ De-escalating
**Tags:** #Brent #oil-price #Hormuz #market-shock

### 2. Gold slides to two-week low as hawkish Fed lifts dollar 🟡
**Alert:** 🟡
**Summary:** Gold fell to around $4,150–4,155/oz on Friday, its lowest since 11 June and a third consecutive weekly decline, as the dollar climbed to a one-year high after the Fed held rates but signalled a more hawkish 2026 outlook — nine of 19 policymakers now see at least one more hike. Goldman Sachs cut its year-end gold forecast to $4,900 from $5,400.
**Market signal:** Bearish — tightening-policy repricing is currently outweighing Middle East geopolitical risk as the dominant driver of safe-haven demand.
**Sources:**
- [Trading Economics — Gold](https://tradingeconomics.com/commodity/gold) · 19 June 2026
**Trend:** ↘ De-escalating
**Tags:** #gold #Fed #FX

### 3. Intel-led rally lifts Nasdaq 1.91% into Juneteenth close 🟢
**Alert:** 🟢
**Summary:** Intel surged 10.6% to a record after President Trump announced an Apple chip-design and manufacturing partnership, lifting the Philadelphia Semiconductor Index 6.4% and the Nasdaq 1.91% to 26,517.93 ahead of the Juneteenth market closure; the S&P 500 rose 1.08% to 7,500.58.
**Market signal:** Bullish — a concrete reshoring commitment from a major buyer is being read as a structural, not just sentiment-driven, positive for US chip manufacturing.
📎 *See also: Technology § Story 1 — Apple-Intel chip tie-up.*
**Sources:**
- [ts2.tech — June 2026 semiconductor news roundup](https://ts2.tech/en/june-2026-semiconductor-news-roundup-u-s-chip-controls-sandboxaq-funding-and-intel-18a-p/) · 18 June 2026
**Trend:** ↗ Escalating
**Tags:** #equity-rally #SP500 #Nasdaq #semiconductor

📚 *Background reading:* [Bruegel — EU economics analysis](https://www.bruegel.org) · [IISS — military balance context](https://www.iiss.org)

---

> 🇪🇺 **EU AFFAIRS ANALYST** · 3 updates today

### 1. Commission's 21st Russia sanctions package advances; interim mini-package adopted 🟡
**Alert:** 🟡
**Summary:** The European Commission presented its proposed 21st Russia sanctions package on 9 June 2026, focused on financial services, crypto, energy and trade — including asset freezes on roughly 90 banks and transaction bans on 31 further Russian banks and 20 third-country banks, crypto firms or oil traders. Ahead of full adoption, the Council adopted an interim "mini-package" on 15 June freezing assets of 34 individuals and 47 entities tied to Russia's military-industrial supply chain.
**Legislative/policy stage:** 21st package at Commission-proposal stage, pending Council adoption; mini-package already in force.
**Sources:**

- [Fieldfisher — UK, EU and US sanctions on Russia](https://www.fieldfisher.com/en/services/international-trade/trade-sanctions-blog/uk-eu-and-us-sanctions-on-russia) · 18 June 2026
**Trend:** → Stable
**Tags:** #EU-sanctions #Russia #sanctions

### 2. Metsola: EU "doesn't have luxury of time" on enlargement, MFF 🟢
**Alert:** 🟢
**Summary:** At the 18–19 June European Council, Parliament President Roberta Metsola urged EU leaders to seize momentum on enlargement, competitiveness and the next long-term EU budget (MFF). Parliament leaders separately visited Dublin to prepare for the incoming Irish Council presidency, and MEPs this week assessed accession progress for five Western Balkans states.
**Legislative/policy stage:** European Council conclusions stage; MFF negotiations ongoing, no formal vote scheduled.
**Sources:**

- [European Parliament — Metsola to EU leaders: "We need to deliver"](https://www.europarl.europa.eu/news/en/press-room/20260618IPR45711/metsola-to-eu-leaders-we-need-to-deliver-we-don-t-have-the-luxury-of-time) · 18 June 2026
**Trend:** → Stable
**Tags:** #EU-institutions #MFF #EU-enlargement

### 3. AI Act Digital Omnibus nears formal adoption 🟡
**Alert:** 🟡
**Summary:** Parliament and Council reached a provisional deal on 7 May 2026 to delay EU AI Act high-risk obligations (Annex III systems pushed to December 2027) and introduce a new ban on AI "nudifier" apps and CSAM-generation tools from December 2026. Formal adoption is expected via plenary vote before the original 2 August 2026 compliance deadline, with publication in the Official Journal to follow within days.
**Legislative/policy stage:** Provisional political agreement reached; formal Parliament and Council vote pending, expected June–July 2026 plenary.
**Sources:**

- [Consilium — Council and Parliament agree to simplify and streamline rules](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/) · 7 May 2026
**Trend:** → Stable
**Tags:** #digital-regulation #AI-regulation #EU-institutions

📚 *Background reading:* [ECFR — European foreign and security policy](https://ecfr.eu/) · [Bruegel — EU economics](https://www.bruegel.org)

---

> 🤖 **TECHNOLOGY ANALYST** · 2 updates today

### 1. Apple-Intel chip tie-up signals US foundry reshoring push 🟢
**Alert:** 🟢
**Summary:** President Trump announced that Apple will partner with Intel on US chip design and manufacturing, sending Intel shares up 10.6% to a record and the Philadelphia Semiconductor Index up 6.4%. Details of the manufacturing split (design vs. fabrication) were not specified in initial reporting.
**Analyst note:** If Apple commits actual leading-edge volume — not just a symbolic design tie-up — this is the first concrete signal in 2026 of a major US fabless buyer shifting capacity away from TSMC dependency on a 12–24 month horizon.
📎 *See also: Business § Story 3 — Intel-led equity rally.*
**Sources:**

- [ts2.tech — June 2026 semiconductor news roundup](https://ts2.tech/en/june-2026-semiconductor-news-roundup-u-s-chip-controls-sandboxaq-funding-and-intel-18a-p/) · 18 June 2026
**Trend:** ↗ Escalating
**Tags:** #semiconductor

### 2. US holds off blacklisting DeepSeek despite security flags 🟡
**Alert:** 🟡
**Summary:** US officials have held off adding China's DeepSeek, memory chipmaker ChangXin Memory Technologies and more than 100 other flagged firms to the Commerce Department's Entity List, despite internal security-risk assessments, two sources told Reuters. The Entity List has had no new additions since October 2025; a former Commerce official called the current approach "whack-a-mole."
**Analyst note:** A year-long enforcement freeze on a flagged AI-model developer suggests trade-policy considerations are currently outweighing export-control hawks inside the administration — a dynamic likely to persist through any further chip-related trade negotiations.
**Sources:**

- [ts2.tech — June 2026 semiconductor news roundup](https://ts2.tech/en/june-2026-semiconductor-news-roundup-u-s-chip-controls-sandboxaq-funding-and-intel-18a-p/) · 18 June 2026
**Trend:** → Stable
**Tags:** #AI #AI-regulation #semiconductor

📚 *Background reading:* [CSIS — The Limits of Chip Export Controls in Meeting the China Challenge](https://www.csis.org/analysis/limits-chip-export-controls-meeting-china-challenge)

---

> 📈 **TRENDS ANALYST** · 3 updates today

### 1. Hormuz transits still 93–94% below pre-crisis levels 🟡
**Alert:** 🟡
**Summary:** AIS-tracked data shows just 140 outbound commercial Hormuz crossings between 4 May and 10 June 2026, versus 2,155 in the same 2025 window — a 93–94% drop. IMF PortWatch's most recent published reading (14 June) showed 0% of typical transit volume. Industry estimates point to weeks-to-months before even half of pre-crisis volumes return, regardless of diplomatic progress.
**Horizon:** Medium-term — structural shipping and insurance normalisation (mine clearance, war-risk premiums) lags any ceasefire announcement by design, not by accident.
📎 *See also: Conflict § Story 1 — Iran's renewed Hormuz closure declaration.*
**Sources:**

- [IndexBox — Strait of Hormuz Commercial Vessel Traffic Plummets in 2026](https://www.indexbox.io/blog/strait-of-hormuz-commercial-traffic-drops-to-6-7-of-last-years-levels/) · 13 June 2026
**Trend:** → Stable
**Tags:** #shipping #supply-shock #Hormuz

### 2. FAO Food Price Index holds broadly stable in May 🟢
**Alert:** 🟢
**Summary:** The FAO Food Price Index averaged 130.8 points in May 2026, down 0.2% from April, as cereal and sugar price gains were offset by falling vegetable oil and dairy prices. The index remains 18.4% below its March 2022 peak but 2.9% above year-ago levels; sunflower oil prices rose on persistent Ukraine-linked supply tightness.
**Horizon:** Medium-term — broad stability masks a cereals uptrend (wheat up for a fourth straight month) that bears watching given concurrent energy-cost pressure from the Hormuz crisis.
**Sources:**

- [FAO — Food Price Index](https://www.fao.org/worldfoodsituation/foodpricesindex/en/) · 5 June 2026
**Trend:** → Stable
**Tags:** #food-security #food-prices

### 3. Pakistan's mediator role deepens as Vance heads to Geneva 🟡
**Alert:** 🟡
**Summary:** Pakistani Prime Minister Shahbaz Sharif and army chief Gen. Asim Munir are travelling to Switzerland to join US–Iran talks alongside US Vice President JD Vance, continuing Islamabad's role as principal mediator since March. Iranian Parliament Speaker Mohammad-Bagher Ghalibaf also arrived in Switzerland for the delegation.
**Horizon:** Medium-term — Pakistan's repeated insertion into US–Iran, Hormuz and (indirectly) Lebanon diplomacy this year marks a durable shift in its regional standing beyond this single crisis.
📎 *See also: Conflict § Story 1.*
**Sources:**

- [MS NOW — Iran says Strait of Hormuz is closed, citing Israeli attacks in Lebanon](https://www.ms.now/news/iran-says-strait-of-hormuz-is-closed-citing-israeli-attacks-in-lebanon) · 20 June 2026
**Trend:** → Stable
**Tags:** #mediation #diplomacy #Pakistan-mediation

📚 *Background reading:* [Atlantic Council — geopolitics and defence](https://www.atlanticcouncil.org) · [RAND — security and geopolitics](https://www.rand.org)

---

## 📊 KEY DATA OF THE DAY

📊 DATA OFFICER · 7 indicators

| Indicator | Value | Δ vs prior session | Δ vs 7 days ago | Note | Source | URL |
|-----------|-------|-------------------|-----------------|------|--------|-----|
| EUR/USD | 1.1453 | +0.13% | ~ -0.99% | Lowest since late March on hawkish Fed | Trading Economics | [link](https://tradingeconomics.com/euro-area/currency) |
| Brent Crude (USD/bbl) | 80.57 | +0.90% | ~ -8.5% | Hormuz reopening optimism still dominates pricing | Trading Economics | [link](https://tradingeconomics.com/commodity/brent-crude-oil) |
| Gold (XAU/USD) | 4,155 | -2.12% | N/A | 3rd consecutive weekly decline; Goldman cut target to $4,900 | TradingView/Trading Economics | [link](https://www.tradingview.com/symbols/XAUUSD/) |
| IMF Global Growth 2026 | 3.1% | vs Jan WEO: -0.2pp | vs Oct 2025 WEO: ~0.0pp | April 2026 reference forecast; adverse scenario 2.5% | IMF WEO April 2026 | [link](https://www.imf.org/en/publications/weo/issues/2026/04/14/world-economic-outlook-april-2026) |
| EU CPI YoY (May 2026) | 3.2% | vs Apr: +0.2pp | vs Feb: +1.3pp | Highest since Sept 2023; energy +10.9% YoY | Eurostat | [link](https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-17062026-ap) |
| FAO Food Price Index | 130.8 | vs Apr: -0.2% | May 2026 (latest) | Next release 3 July 2026 | FAO | [link](https://www.fao.org/worldfoodsituation/foodpricesindex/en/) |
| Hormuz transit volume (% of normal) | Contested: 0% (Iran/IRGC) vs ~58% (CENTCOM, 55 ships/24h) | N/A | N/A | Iran re-declared closure 20 June; US disputes | CENTCOM / Iranian state media via AP | [link](https://www.ms.now/news/iran-says-strait-of-hormuz-is-closed-citing-israeli-attacks-in-lebanon) |

**Data commentary:** A Fed-driven dollar squeeze is pulling both EUR/USD and gold lower simultaneously — an unusual pairing that reflects monetary-policy divergence, not safe-haven flight. Eurozone inflation at a 32-month high (3.2%), overwhelmingly energy-driven, leaves the ECB exposed if Saturday's Hormuz closure declaration proves durable rather than rhetorical. The IMF's April reference forecast (3.1% growth) already priced in a "short-lived" conflict; a sustained closure would push the data toward the Fund's adverse (2.5%) scenario.

## 📉 CHARTS

Both standing chart slots are omitted this run. Chart 1 (Brent trajectory) would require ≥3 confirmed dated closing prices; only two clean points were verifiable in this session (19 June: $80.57; ~20–21 June: $80.59, per straits.live). Chart 2 (Hormuz transit volume) was omitted because the only available recent reads are directly contested between Iranian state media (0% / fully closed) and CENTCOM (55 vessels transited) — plotting either claim alone would misrepresent an actively disputed figure. Chart 3 was not supplied by the editor this run.

## ⚙️ AGENT METADATA

| Field | Value |
|-------|-------|
| Agent version | MORNING BRIEF v1.2.2 |
| Run timestamp | 2026-06-21T05:00:05+02:00 |
| Fetch status | Le Monde ❌ · FAZ ❌ · Kommersant ❌ · Xinhua ⚠️ · EP ⚠️ |
| Sources queried | 9 / 11 (Tier 1+2 attempted; ECB and European Commission direct fetch returned no usable content — supplemented via Consilium/EC search) |
| Stories surfaced | 19 |
| Stories published | 14 |
| Languages processed | EN |
| Output language | English (British) |
| Date validated | ✅ Confirmed 21 June 2026 |
| Expansion Queue | None |

---

MORNING BRIEF is an AI-assisted digest. All summaries are paraphrased from original sources.
Verify time-sensitive information at the linked URLs before acting.
Output language: British English.

---

One flag for you, Roberto: the Israel–Lebanon ceasefire tracker's real-world start date isn't yet pinned in memory. I used **19 June 2026** (the most recent of four ceasefire iterations since April, and the only one violated within hours of taking effect) — but given the cycle of repeated breakdowns, you may want to decide whether the tracker should reset on each new ceasefire announcement or switch to tracking the underlying conflict instead. Let me know if you'd like me to record a convention for future runs.
