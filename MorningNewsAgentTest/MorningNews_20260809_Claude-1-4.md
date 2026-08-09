**Phase 0 — Date anchor confirmed**
📅 Run date: **09 August 2026**, 04:51 CET
📌 Day counters: Russia–Ukraine War = **Day 1628** · Iran–US/Hormuz Crisis = **Day 163**

Moving into Phase 1 (direct fetch pass).

**Phase 1 — Direct fetch results**

| Outlet | Status |
|---|---|
| Le Monde | ❌ blocked |
| FAZ | ❌ blocked |
| Kommersant `/en/` | ❌ 404 (confirmed again — flag for registry) |
| Xinhua | ⚠️ fetched, content stale (6 Aug) |
| European Parliament | ⚠️ fetched, no dated 24h items |
| FAO | ✅ July 2026 FFPI = 131.1, released 07/08/2026 |
| IMF | ⚠️ fetched, latest substantive item 27 July |
| ECB | ❌ nav/metadata only |
| European Commission | ❌ nav/metadata only |

Moving to Phase 2 search pass.

Good — strong multi-source corroboration on Hormuz. Now Ukraine/Russia and Israel-Lebanon.

Good multi-source corroboration on Israel-Lebanon. Now Business, EU Affairs, Technology, Trends, and data indicators.

Now EUR/USD, IMF growth, EU CPI, and EU Affairs / Technology / Trends stories.

Good context. Now Technology and Trends stories.

Well-corroborated (Bloomberg, Reuters via CryptoBriefing, Neowin, MarkTechPost). Now Trends section.

Extremely well corroborated, breaking today (AP-sourced across multiple outlets). This will be the lead conflict story. Now compiling the full brief.

Now assembling the full brief.

Today's brief is done — 13 stories, run completed at 04:56 CET.

Headline you'll want to flag to Roberto: the lead Hormuz story flipped overnight. Rubio/Araghchi were signalling a deal was days away through 4–7 Aug, but Iran's Supreme National Security Council issued new hardline demands and the UAE reported a missile strike on an ADNOC tanker on 8 Aug — so Wall Street's record-high rally and the week's oil slide are both premised on optimism that got contradicted right before this run. That's the `⚡ Reversal` on the signal board.

A few housekeeping notes for the taxonomy review:
- **Kommersant `/en/`** hit its hard 404 again — third+ consecutive run, worth actioning at the end-of-August revision.
- **`#war-risk-insurance`** appeared for a third consecutive brief (tagged with `#single-source` since the underlying figures trace to a Tier 4 aggregator, corroborated only partially by Reuters/Bloomberg/Kpler citations within that source) — one more consecutive appearance and it's expansion-queue eligible.
- Two Tier 4 sources came up this run (Bloomberg and the shipping-tracker aggregator) — Bloomberg isn't in your Tier 1–3 registry despite being a mainstream outlet, which is worth a look at your next taxonomy pass.

```yaml
---
brief_date: 2026-08-09
version: v1.4
run_time: "04:55 CET"
stories_published: 13
categories: [conflict, business, eu_affairs, technology, trends]
alert_counts:
  red: 4
  yellow: 8
  green: 1
ongoing_situations:
  - {name: "Russia–Ukraine War", real_world_start: "2022-02-24", day: 1628}
  - {name: "Iran–US War / Hormuz Crisis", real_world_start: "2026-02-28", day: 163}
  - {name: "Israel–Lebanon", real_world_start: "N/A — no durable ceasefire established", day: null}
sources_fetched: 9
fetch_status:
  le_monde: "❌"
  faz: "❌"
  kommersant: "❌"
  xinhua: "⚠️"
  european_parliament: "⚠️"
expansion_queue: ["#war-risk-insurance (3rd consecutive brief)", "#tariffs (monitoring, below threshold)"]
---
```

# 🌐 MORNING BRIEF
## Sunday, 09 August 2026 · 04:55 CET
### 13 stories across 5 categories

## DIGEST SUMMARY

| # | Category | Headline | Alert |
|---|----------|----------|-------|
| 1 | ⚔️ Conflict | Iran issues new Hormuz demands, UAE reports missile strike on ADNOC tanker | 🔴 |
| 2 | ⚔️ Conflict | Ukraine strikes Russian refineries as Zelensky visits Serbia | 🟡 |
| 3 | ⚔️ Conflict | Lebanon cites "positive progress" in Rome talks even as Israeli strikes resume | 🟡 |
| 4 | ⚔️ Conflict | Yemeni government forces attack Houthis as Red Sea risk widens | 🟡 |
| 5 | 💼 Business | Wall Street hits record highs on Hormuz-deal optimism, oil slides | 🟡 |
| 6 | 💼 Business | Gold surges past $4,270 as Hormuz uncertainty persists | 🟡 |
| 7 | 🇪🇺 EU Affairs | Hungary's parliament passes reforms to unlock €16.4bn in frozen EU funds | 🟢 |
| 8 | 🇪🇺 EU Affairs | EU and Ukraine launch defence-industrial partnership, disburse €1bn for drones | 🟡 |
| 9 | 🤖 Technology | Alibaba's Qwen3.8-Max claims benchmark parity with Anthropic's Fable 5 | 🟡 |
| 10 | 📈 Trends | Saudi Arabia joins Cape of Good Hope reroute as war-risk premiums hit 30× | 🔴 |
| 11 | 📈 Trends | Euro-area inflation reaccelerates to 2.9% on energy costs | 🟡 |
| 12 | 📈 Trends | FAO Food Price Index edges up on Black Sea wheat disruption | 🟡 |
| 13 | 📈 Trends | Global growth held at 3.0% for 2026 as war and AI boom offset each other | 🟢 |

> Alert Level key: 🔴 High significance · 🟡 Developing · 🟢 Stable/Routine

---

## 🚨 SIGNAL BOARD

🔴 **Hormuz transit collapsed to 3% of pre-crisis volume (2 vessels vs 73/day typical, IMF PortWatch, 2 Aug) — and Iran just added new demands rather than closing a deal**
---
🔴 **War-risk insurance on VLCC transits through Hormuz now runs ~30× pre-crisis, ~$10m per voyage**
---
🟡 **Gold up 4.6% in seven days to $4,270.62/oz; Brent down 9.7% over the same window to $83.64/bbl — markets still pricing de-escalation odds that Saturday's news undercuts**
---
🟢 **Euro-area inflation ticked up to 2.9% in July, driven by a jump in energy inflation to 10.0%**
---
⚡ **Reversal: Iran's Supreme National Security Council rejected the "deal is close" framing from Rubio and Araghchi just 24–48 hours after both sides signalled imminent agreement**
---

## ⚔️ CONFLICT ANALYST

> 🔎 **CONFLICT ANALYST** · 4 updates today

### 1. Iran issues new Hormuz demands, UAE reports missile strike on ADNOC tanker 🔴
**Alert:** 🔴
**Summary:** Iran's Supreme National Security Council said Saturday the Strait of Hormuz will not reopen until the US "corrects its behaviour," listing new demands including an end to the naval blockade, sanctions relief and a US troop withdrawal from the region. Hours earlier, Abu Dhabi's state oil firm ADNOC said one of its vessels was struck by an Iranian missile while transiting the strait; no casualties were reported, though ADNOC says over a dozen of its ships have now been hit since February. The announcement contradicts optimistic signals from US and Iranian officials earlier in the week that a transit-route deal with Oman was close.
**Significance:** The reversal undercuts the market's Hormuz de-escalation pricing (Brent and equities have both moved on "deal near" headlines this week) and signals Tehran is hardening its negotiating position even as Iran-Oman technical talks continue.
**Sources:**
- [AP via NBC News — Iran makes new strait demands, the UAE says a ship was targeted](https://www.nbcnews.com/world/iran/iran-says-deal-strait-hormuz-close-will-not-open-waterway-rcna591476) · 8 August 2026
- [CNBC — Iran sets conditions for opening Strait of Hormuz after UAE says one of its ships was targeted by airstrike](https://www.cnbc.com/2026/08/08/uae-ship-targeted-missile-us-iran-tensions-stay-high.html) · 8 August 2026
**Trend:** ⚡ Reversal
**Tags:** #Iran #Hormuz #naval-blockade #missile-strike

### 2. Ukraine strikes Russian refineries as Zelensky visits Serbia 🟡
**Alert:** 🟡
**Summary:** Ukraine's Unmanned Systems Forces struck oil refineries in Russia's Samara Oblast and Krasnodar Krai overnight on 8 August, part of a sustained campaign against Russian export infrastructure; Ukraine's General Staff says Russia has lost roughly 1,190 personnel in the past day alone. Separately, President Zelensky began his first official visit to Serbia, meeting President Vučić. Suspicious drones were also sighted over a German military base days after a similar Leipzig airport incident.
**Significance:** Continued deep strikes on Russian energy infrastructure keep pressure on Moscow's export revenue even as the frontline itself remains largely static; the German drone sightings point to the war's disruptive reach into NATO territory.
**Sources:**
- [Kyiv Independent — Ukraine reportedly strikes Russian oil refineries in Samara Oblast, Krasnodar Krai](https://kyivindependent.com/) · 8 August 2026
- [Ukrinform — War](https://www.ukrinform.net/rubric-ato) · 8 August 2026
**Trend:** → Stable
**Tags:** #Ukraine #Russia #drone-warfare #energy-markets

### 3. Lebanon cites "positive progress" in Rome talks even as Israeli strikes resume 🟡
**Alert:** 🟡
**Summary:** Lebanese President Joseph Aoun described "positive progress" on borders and prisoner exchanges following the latest round of Lebanon–Israel talks in Rome. The claim sits awkwardly against events on the ground: an IED blast killed two Israeli reservists on 5 August, prompting the IDF to resume strikes and issue its first new evacuation order in weeks, while residents of southern Lebanon say the June "ceasefire" has failed to protect them. No durable ceasefire has been established since fighting resumed.
**Significance:** The gap between diplomatic optimism in Rome and continued strikes/casualties on the ground illustrates how fragile the current truce arrangement remains.
**Sources:**
- [Al Jazeera — Lebanon points to 'positive progress' on borders, prisoners in Israel talks](https://www.aljazeera.com/news/2026/8/7/lebanon-points-to-positive-progress-on-borders-prisoners-in-israel-talks) · 7 August 2026
- [Times of Israel — Two reservists killed, four seriously wounded by IED blast in south Lebanon](https://www.timesofisrael.com/idf-strikes-southern-lebanon-town-alleging-ceasefire-violation-by-hezbollah/) · 6 August 2026
**Trend:** → Stable
**Tags:** #Israel #Lebanon #Hezbollah #ceasefire

### 4. Yemeni government forces attack Houthis as Red Sea risk widens 🟡
**Alert:** 🟡
**Summary:** Yemen's internationally recognised military attacked Iran-backed Houthi positions on 8 August, according to AP reporting, as the Houthis' campaign against Saudi Arabia continues following their 20 July declaration of a naval blockade. Saudi Arabia has begun rerouting some tankers around the Cape of Good Hope rather than through the Red Sea/Bab el-Mandeb corridor.
**Significance:** A second active chokepoint crisis alongside Hormuz compounds global shipping disruption; see Trends § Story 10 for the freight and insurance impact.
**Sources:**
- [AP via U.S. News — Iran Makes New Strait Demands, the UAE Says a Ship Was Targeted and Other Middle East News](https://www.usnews.com/news/world/articles/2026-08-08/the-uae-says-iranian-missile-targeted-a-ship-yemen-attacks-houthis-and-other-middle-east-news) · 8 August 2026
**Trend:** ↗ Escalating
**Tags:** #naval-blockade #missile-strike #war-crimes #humanitarian

📚 *Background reading:* [Al Jazeera — Will the US-Iran war and Hormuz deadlock last for months?](https://www.aljazeera.com/news/energy/2026/8/6/will-the-us-iran-war-and-hormuz-deadlock-last-for-months) · [CFR Global Conflict Tracker — War in Ukraine](https://www.cfr.org/global-conflict-tracker/conflict/conflict-ukraine)

---

## 💼 BUSINESS ANALYST

> 💼 **BUSINESS ANALYST** · 2 updates today

### 1. Wall Street hits record highs on Hormuz-deal optimism, oil slides 🟡
**Alert:** 🟡
**Summary:** The S&P 500 (+1.79%) and Dow (+1.71%) closed at fresh record highs on 4 August as hopes grew for a US–Iran deal to reopen the Strait of Hormuz; the Nasdaq jumped 2.59% on a 29% Palantir rally. Oil fell for a second straight session on the same optimism. Saturday's escalation (see Conflict § Story 1) had not yet fed through to markets as of this run.
**Market signal:** Bullish on equities/bearish on oil into the weekend, but the rally's premise — an imminent Hormuz deal — was directly contradicted by Iran's new demands within days.
**Sources:**
- [CNBC — Stock market news for Aug. 4, 2026](https://www.cnbc.com/2026/08/03/stock-market-today-live-updates.html) · 4 August 2026
**Trend:** ⚡ Reversal
**Tags:** #equity-rally #oil-price #Hormuz

### 2. Gold surges past $4,270 as Hormuz uncertainty persists 🟡
**Alert:** 🟡
**Summary:** Gold hit $4,270.62/oz as of 7am ET on 6 August, up 2.4% on the prior session and 4.6% over seven days, extending a record run driven by inflation concerns and Middle East risk. Silver, platinum and palladium also gained.
**Market signal:** Bullish — safe-haven demand is rising in parallel with equity records, an unusual combination that reflects unresolved geopolitical risk rather than a clean risk-on/risk-off signal.
**Sources:**
- [Fortune — Current price of gold as of August 6, 2026](https://fortune.com/article/current-price-of-gold-08-06-2026/) · 6 August 2026
**Trend:** ↗ Escalating
**Tags:** #gold #market-shock #FX

📚 *Background reading:* [Atlantic Council — commentary on Hormuz war-risk pricing](https://www.atlanticcouncil.org)

---

## 🇪🇺 EU AFFAIRS ANALYST

> 🇪🇺 **EU AFFAIRS ANALYST** · 2 updates today

### 1. Hungary's parliament passes reforms to unlock €16.4bn in frozen EU funds 🟢
**Alert:** 🟢
**Summary:** Hungary's National Assembly approved a package of rule-of-law and transparency reforms on a 142–39 vote, fulfilling conditions agreed between PM Péter Magyar and Commission President von der Leyen in late May to release roughly €16.4bn in frozen cohesion and recovery funds — about 13% of the national budget. Budapest must meet all remaining conditions by end-August or forfeit the money; the Commission says 67 reforms and 50 investments under the recovery plan still need updating.
**Legislative/policy stage:** Reforms adopted at national level; Commission review of compliance ongoing ahead of the end-August deadline.
**Sources:**
- [Al Jazeera — EU to release billions in frozen funds for Hungary amid Magyar reforms](https://www.aljazeera.com/news/2026/5/29/eu-to-release-billions-in-frozen-funds-for-hungary-amid-magyar-reforms) · 29 May 2026
**Trend:** ↘ De-escalating
**Tags:** #Hungary #Magyar #EU-funds #rule-of-law

### 2. EU and Ukraine launch defence-industrial partnership, disburse €1bn for drones 🟡
**Alert:** 🟡
**Summary:** The European Commission and Ukraine signed a new defence-industrial partnership in July, formalised with a €1bn disbursement for joint drone and counter-drone production, targeting delivery by end-2026. The move builds on the EU's €90bn Ukraine support loan (finalised 23 April), of which €60bn is earmarked for military assistance and €8.1bn has been disbursed so far. The UK joined the loan mechanism in July.
**Legislative/policy stage:** Partnership signed and operational; anti-ballistic missile joint production targeted for 2028.
**Sources:**
- [European Commission — EU military support to Ukraine](https://commission.europa.eu/topics/eu-solidarity-ukraine/eu-assistance-ukraine/eu-military-support-ukraine_en) · August 2026
**Trend:** → Stable
**Tags:** #Ukraine-aid #EU-defence #EU-institutions

📚 *Background reading:* [Bruegel — EU economics commentary](https://www.bruegel.org) · [ECFR — European foreign and security policy](https://ecfr.eu/)

---

## 🤖 TECHNOLOGY ANALYST

> 🤖 **TECHNOLOGY ANALYST** · 1 update today

### 1. Alibaba's Qwen3.8-Max claims benchmark parity with Anthropic's Fable 5 🟡
**Alert:** 🟡
**Summary:** Alibaba released Qwen3.8-Max on 3 August, a 2.4-trillion-parameter mixture-of-experts model (95bn active parameters) that the company says matches or beats Anthropic's Fable 5 on several coding, agentic and multimodal benchmarks, including Terminal-Bench 2.1 and PaperBench, while trailing on some general reasoning tests. Open weights are due within the week via Hugging Face.
**Analyst note:** The release is the latest sign that Chinese open-weight labs (Alibaba, Moonshot, DeepSeek) are closing the capability gap with US frontier models on agentic and coding tasks specifically over a 12–24 month horizon, intensifying pricing pressure on proprietary API providers.
**Sources:**
- [Bloomberg — Alibaba's Qwen3.8-Max AI Model Claims Benchmark Scores Rivaling Anthropic](https://www.bloomberg.com/news/articles/2026-08-03/alibaba-drops-another-china-ai-model-with-breakthrough-performance) · 3 August 2026
**Trend:** ↗ Escalating
**Tags:** #AI #AI-benchmark #open-source-AI #semiconductor

📚 *Background reading:* [CSIS — Tech and security commentary](https://www.csis.org)

---

## 📈 TRENDS ANALYST

> 📈 **TRENDS ANALYST** · 4 updates today

### 1. Saudi Arabia joins Cape of Good Hope reroute as war-risk premiums hit 30× 🔴
**Alert:** 🔴
**Summary:** Saudi Arabia has begun rerouting tankers around the Cape of Good Hope after Houthi attacks widened Red Sea risk (see Conflict § Story 4), adding to Hormuz-driven diversions already under way. Hormuz war-risk insurance now runs roughly 30× pre-crisis levels — about $10m per VLCC transit — with six P&I clubs having withdrawn cover; four of the world's nine largest container lines have suspended Hormuz/Gulf calls outright. 📎 See also: Business § Story 1 — oil price impact.
**Horizon:** Short-to-medium term: current reroutes add 10–14 days per voyage and are expected to persist as long as both chokepoints remain contested; structurally, this is accelerating capacity investment in Cape-route infrastructure.
**Sources:**
- [Reuters/Bloomberg/Kpler, cited via Mighty Shipping — Red Sea & Hormuz Shipping Crisis 2026 rolling update](https://www.mightyshipping.com/en/blog/2026-07-01-hormuz-reopening-july-freight-outlook) · 8 August 2026 #single-source
**Trend:** ↗ Escalating
**Tags:** #reroute-shipping #war-risk-insurance #shipping #single-source

### 2. Euro-area inflation reaccelerates to 2.9% on energy costs 🟡
**Alert:** 🟡
**Summary:** Eurostat's flash estimate put euro-area annual inflation at 2.9% in July 2026, up from 2.8% in June, driven by energy inflation jumping to 10.0% from 8.5% as US–Iran hostilities resumed. Core inflation (ex food and energy) rose to 2.5% from 2.4%. Germany, France, Spain and the Netherlands all saw inflation accelerate; Italy eased slightly.
**Horizon:** Short-term: the disinflation trend that held through 2024–25 has stalled, consistent with the IMF's July WEO revision (see Data section). Structurally, this ties eurozone price stability directly to Hormuz outcomes.
**Sources:**
- [Eurostat — Euro area annual inflation up to 2.9%](https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-31072026-ap) · 31 July 2026
**Trend:** ↗ Escalating
**Tags:** #inflation #eurozone #energy-markets

### 3. FAO Food Price Index edges up on Black Sea wheat disruption 🟡
**Alert:** 🟡
**Summary:** The FAO Food Price Index rose to 131.1 in July 2026, up 0.6% from June, driven by a 3.4% jump in cereal prices as wheat surged 5.8% amid continued disruption to Black Sea export flows and heatwave damage to crop yields. Vegetable oil prices hit their highest level since June 2022; meat and dairy indices fell.
**Horizon:** Medium-term: cereal price pressure is directly linked to the Russia–Ukraine war's disruption of Black Sea shipping lanes and is compounding separately from the Hormuz-driven energy shock.
**Sources:**
- [FAO — FAO Food Price Index](https://www.fao.org/worldfoodsituation/foodpricesindex/en/) · 7 August 2026
**Trend:** ↗ Escalating
**Tags:** #food-prices #food-security #Ukraine

### 4. Global growth held at 3.0% for 2026 as war and AI boom offset each other 🟢
**Alert:** 🟢
**Summary:** The IMF's July 2026 WEO update kept global growth at 3.0% for 2026 and 3.4% for 2027, broadly unchanged cumulatively from April, as AI-driven investment offsets the drag from the Middle East war. The euro area was revised down to roughly 0.4–0.9% growth (sources vary on the exact figure) on limited AI upside and energy exposure; global headline inflation was revised up to 4.7%.
**Horizon:** Long-term: the IMF frames this as a structural divergence — economies plugged into the AI/semiconductor value chain are decoupling from those exposed mainly to the energy shock.
**Sources:**
- [IMF — World Economic Outlook Update, July 2026: Global Economy in Crosscurrents of War and Technology](https://www.imf.org/en/publications/weo/issues/2026/07/08/world-economic-outlook-update-july-2026) · 8 July 2026
**Trend:** → Stable
**Tags:** #GDP-forecast #IMF #stagflation

📚 *Background reading:* [RAND — Tech, security and geopolitics](https://www.rand.org) · [ECFR — European policy commentary](https://ecfr.eu/)

---

## 📊 KEY DATA OF THE DAY

> 📊 **DATA OFFICER** · 7 indicators

| Indicator | Value | Δ vs prior session | Δ vs 7 days ago | Note | Source | URL |
|-----------|-------|-------------------|-----------------|------|--------|-----|
| EUR/USD | 1.1550 | +0.22% | N/A | ECB left rates unchanged in July; market pricing one more hike by year-end | Trading Economics | [link](https://tradingeconomics.com/euro-area/currency) |
| Brent Crude (USD/bbl) | 83.64 | −0.10% | −9.72% | 7d fall reflects Hormuz-deal optimism (4–6 Aug); Saturday's reversal not yet priced | Fortune (daily snapshot series) | [link](https://fortune.com/article/price-of-oil-08-06-2026/) |
| Gold (XAU/USD) | 4,270.62 | +2.39% | +4.62% | Record run continues alongside equity records — safe-haven demand despite risk-on equities | Fortune (daily snapshot series) | [link](https://fortune.com/article/current-price-of-gold-08-06-2026/) |
| IMF Global Growth 2026 | 3.0% | N/A | N/A | Broadly unchanged cumulatively vs April 2026 WEO; July update cadence, not Jan/Oct | IMF WEO Update, July 2026 | [link](https://www.imf.org/en/publications/weo/issues/2026/07/08/world-economic-outlook-update-july-2026) |
| EU CPI YoY (latest) | 2.9% | +0.1pp | −0.1pp | July 2026 flash estimate; vs June 2026 / vs April 2026 (3.0%) | Eurostat | [link](https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-31072026-ap) |
| FAO Food Price Index | 131.1 | +0.6% | July 2026 | Released 7 August 2026 | FAO | [link](https://www.fao.org/worldfoodsituation/foodpricesindex/en/) |
| Hormuz transit volume (% of normal) | 3% | −33.3% | N/A | 2 vessels vs 73/day typical, 2 Aug (latest published day); 16 tankers running AIS-dark | IMF PortWatch (via straits.live) | [link](https://straits.live/) |

**Data commentary:** The data paints a market that priced in a Hormuz deal that didn't materialise — Brent down nearly 10% over the week and equities at record highs, both premised on de-escalation that Iran's new demands directly contradict. Meanwhile the real-economy indicators (EU CPI, FAO index) show the energy and food shock still working through the system with a lag, and gold's simultaneous rise with equities suggests markets haven't fully resolved which narrative to believe.

---

## ⚙️ AGENT METADATA

| Field | Value |
|-------|-------|
| Agent version | MORNING BRIEF v1.4 |
| Run timestamp | 2026-08-09T04:55:00+02:00 |
| Fetch status | Le Monde ❌ · FAZ ❌ · Kommersant ❌ · Xinhua ⚠️ · EP ⚠️ |
| Sources queried | 9 / 11 (Tier 1: Xinhua ⚠️; Tier 2: FAO ✅, IMF ⚠️, ECB ❌, European Commission ❌, European Parliament ⚠️) |
| Stories surfaced | 22 |
| Stories published | 13 |
| Languages processed | EN |
| Output language | English (British) |
| Date validated | ✅ Confirmed 09 August 2026 |
| Expansion Queue | #war-risk-insurance (3rd consecutive brief — one more for closed-list promotion); #tariffs (monitoring, below threshold) |

---

MORNING BRIEF is an AI-assisted digest. All summaries are paraphrased from original sources.
Verify time-sensitive information at the linked URLs before acting.
Output language: British English.
