EP ⚠️ (generic). FAO and World Bank next.

Brief file is written; sharing it now.

Your Morning Brief for 15 October 2026 is ready as `morning_brief_2026-10-15.md`: 15 stories across 5 categories, with 3 🔴, 10 🟡 and 2 🟢 alerts.

- **Fetch results:** Kommersant, Xinhua, Al Jazeera and the European Council returned usable dated items. NPR returned stale February content. IMF, ECB, Commission, Eurostat, Parliament and the World Bank returned stale or generic pages, so none is cited as a story source. The FAO release is dated 2 October, the latest available.
- **Search-only outlets:** Targeted queries for the Guardian, Bloomberg, Euronews, Handelsblatt and El País returned nothing citable, so the brief rests mainly on Al Jazeera, Kommersant, Xinhua and the Council. No outlet exceeds roughly 30% of citations.
- **Sourcing:** Eight stories are tagged `#single-source` (1, 6, 7, 11, 12, 14, 15). The IEA figures in stories 7 and 15 come through Kommersant, not the IEA page.
- **Headline-only corroboration:** In story 2, the Xinhua link is a headline seen on its world page, not a fetched article. Story 4's second source is Kommersant's headline and subhead only.
- **Format change:** I left `le_monde` and `faz` out of the YAML fetch status, since v1.7.7 removed those sources.

```yaml
---
brief_date: 2026-10-15
version: v1.7.7
run_time: "05:16 CET"
stories_published: 15
categories: [conflict, business, eu_affairs, technology, trends]
alert_counts:
  red: 3
  yellow: 10
  green: 2
ongoing_situations:
  - {name: "US-Israel war on Iran", real_world_start: "2026-02-28", day: 230}
  - {name: "DRC Ebola (Bundibugyo) outbreak", real_world_start: "2026-05-15", day: 154}
sources_fetched: 12
fetch_status:
  kommersant: "✅"
  xinhua: "✅"
  european_parliament: "⚠️"
  european_council: "✅"
expansion_queue: []
---
```

# 🌐 MORNING BRIEF
## Thursday, 15 October 2026 · 05:16 CET
### 15 stories across 5 categories

---

## DIGEST SUMMARY

| # | Category | Headline | Alert |
|---|----------|----------|-------|
| 1 | ⚔️ Conflict | Iran / Strait of Hormuz: two vessels sunk, Tehran vows to fight on | 🔴 |
| 2 | ⚔️ Conflict | Netanyahu presses Trump to resume strikes on Iran before Knesset vote | 🟡 |
| 3 | ⚔️ Conflict | Yemen / Saudi Arabia: Houthi strikes on Aramco, Israel's role blocked | 🔴 |
| 4 | ⚔️ Conflict | Ukraine: Kyiv loses US missile warnings amid pressure over refinery strikes | 🔴 |
| 5 | 💼 Business | IMF lifts 2026 growth to 3.1% but flags Hormuz drag | 🟡 |
| 6 | 💼 Business | US CPI accelerates to 3.7% as Fed hike odds near 50% | 🟡 |
| 7 | 💼 Business | IEA: diesel deficit to persist until H2 2027 | 🟡 |
| 8 | 🇪🇺 EU Affairs | EU opens Ukraine and Moldova talks on internal market and competitiveness | 🟡 |
| 9 | 🇪🇺 EU Affairs | Largest-ever EU listing targets almost 1,600 Russian military-industrial entities | 🟡 |
| 10 | 🇪🇺 EU Affairs | Council gives final approval to €115 million AGILE defence programme | 🟢 |
| 11 | 🤖 Technology | Starshield speed cap hits Ukraine's drone operations | 🟡 |
| 12 | 🤖 Technology | Hackers push hundreds of French supermarket freezers to 50°C | 🟡 |
| 13 | 📈 Trends | FAO Food Price Index edges up to 136.0 in September | 🟡 |
| 14 | 📈 Trends | DRC Ebola outbreak passes 9,000 confirmed cases | 🟡 |
| 15 | 📈 Trends | Gulf crude exports recover via Hormuz bypass; product exports lag | 🟢 |

> Alert Level key: 🔴 High significance · 🟡 Developing · 🟢 Stable/Routine

---

## 🚨 SIGNAL BOARD

---
🔴 **Two vessels sank near Hormuz on 14–15 October and Tehran vows to fight until Washington accepts its demands — day 230 of the war**
---
🔴 **Kyiv hit by ballistic missiles for a second night (at least 9 dead) without usual Western warnings; Starshield speed cap restricts Ukrainian drones**
---
🟡 **US CPI 3.7% y/y in September (3.4% in August); petrol +34.2% y/y; CME FedWatch puts the chance of a late-October hike at 47.1%**
---
🟡 **IMF lifts 2026 world growth to 3.1% (+0.1 pp vs July) yet puts the Hormuz drag at 0.9 pp; 2026 oil average pegged at USD 95.74/bbl**
---
⚡ **EU opens Ukraine and Moldova talks on the internal-market and competitiveness clusters while adopting its largest-ever Russia listings: 826 companies, 743 individuals**
---

---

> ⚔️ **CONFLICT ANALYST** · 4 updates today

### 1. Iran / Strait of Hormuz 🔴
**Alert:** 🔴
**Summary:** Two vessels sank near the Strait of Hormuz, one hit by a projectile and the other by a sea mine, as continuing attacks slow maritime traffic. Iranian Parliament Speaker Mohammad Bagher Ghalibaf stated that Tehran does not seek an endless war or prolonged negotiations with the United States but will keep fighting until Washington accepts Iran's demands. Al Jazeera reported oil prices rising as Houthi strikes hit Saudi Aramco and Tehran vowed new tactics against shipping in the strait. The war began on 28 February 2026.
**Significance:** Open-ended Iranian maritime attrition keeps Hormuz transit capacity impaired; the IMF's 13 October outlook estimates the closure could cost 0.9 percentage points of 2026 world growth (see Business § Story 5).
**Sources:**
- [Al Jazeera — Iran war live: Tehran vows to fight until US yields as ships sink in Hormuz](https://www.aljazeera.com/news/liveblog/2026/10/15/iran-war-live-tehran-vows-to-fight-until-us-yields-as-ships-sink-in-hormuz) · 15 October 2026
**Trend:** ↗ Escalating
**Tags:** #Iran #Hormuz #day-230 #single-source

### 2. Netanyahu presses Trump to resume strikes on Iran 🟡
**Alert:** 🟡
**Summary:** Israeli Prime Minister Benjamin Netanyahu has urged President Donald Trump on several calls to resume the joint military operation against Iran, ideally before Israel's Knesset election on 27 October, citing signs of Tehran restarting nuclear work, according to Axios and Israel's Channel 12 as relayed by Kommersant. A senior US official told Axios that Trump replied "go ahead and prepare" without concrete commitments. The White House is weighing the effect on the 3 November midterms. Speaking in Alaska on 13 October, Trump said the Gulf conflict would end "very soon".
**Significance:** Two electoral clocks (Israel 27 October, US 3 November) now shape the timing of any renewed campaign; Washington's reluctance is driven by domestic politics rather than the nuclear case Israel is pressing.
**Sources:**
- [Kommersant — «Israel wants to repeat "Lion's Roar"» (Израиль хочет повторить «Львиный рык»)](https://www.kommersant.ru/doc/9026593) · 14 October 2026
- [Xinhua — «Israeli media: Netanyahu and Trump discuss possibility of restarting war on Iran» (以媒：内塔尼亚胡与特朗普讨论重启对伊战争可能性)](https://www.news.cn/world/20261014/6f69ebd55e2e400fba4bd14f96fd051f/c.html) · 14 October 2026
**Trend:** ↗ Escalating
**Tags:** #Iran #Israel #escalation #MULTI-SOURCE

### 3. Yemen / Saudi Arabia: Houthi offensive 🔴
**Alert:** 🔴
**Summary:** Houthi forces have pressed an offensive against Yemen's central-government troops since early September and are striking Saudi oil and transport infrastructure, Kommersant reported. Al Jazeera's 14–15 October coverage recorded Houthi strikes hitting Saudi Aramco and Saudi-led coalition strikes on Houthi sites, with oil prices rising on the attacks. Per Haaretz sources cited by Kommersant, Netanyahu has sought Riyadh's consent for the Israeli air force to join strikes on the Houthis; Crown Prince Mohammed bin Salman refuses, fearing domestic backlash.
**Significance:** Saudi refusal caps Israel's role for now, while Aramco exposure ties the Yemen front directly to oil pricing; the IMF projects a 3.3% contraction for Saudi Arabia in 2026 (Xinhua, 13 October).
**Sources:**
- [Kommersant — «Israel wants to repeat "Lion's Roar"» (Израиль хочет повторить «Львиный рык»)](https://www.kommersant.ru/doc/9026593) · 14 October 2026
- [Al Jazeera — Iran war live: Tehran vows to fight until US yields as ships sink in Hormuz](https://www.aljazeera.com/news/liveblog/2026/10/15/iran-war-live-tehran-vows-to-fight-until-us-yields-as-ships-sink-in-hormuz) · 15 October 2026
**Trend:** ↗ Escalating
**Tags:** #missile-strike #energy-markets #escalation #MULTI-SOURCE

### 4. Ukraine: missile warnings lost amid US pressure 🔴
**Alert:** 🔴
**Summary:** Russian ballistic missiles struck Kyiv for a second consecutive night, killing at least nine people and damaging electricity and heating infrastructure, Al Jazeera reported. President Volodymyr Zelensky stated that Ukraine again received none of its usual warnings from Western allies. Sources told Reuters and other media that the US threatened to cut early-warning intelligence to force Kyiv to halt strikes on Russian oil refineries; Trump said on Tuesday that the US has not stopped sharing intelligence. Kommersant reported Kyiv stopped receiving signals from the US missile early-warning system.
**Significance:** Trump lifted sanctions on Russian diesel last week and told Kyiv to stop hitting refineries (Al Jazeera). The Kyiv Independent reported on 12 October, citing two Ukrainian officials, that Washington had threatened to suspend intelligence sharing: [Kyiv Independent — Explosions heard in Kyiv before air raid alert issued](https://kyivindependent.com/explosions-heard-in-kyiv-before-air-raid-alert-issued/).
**Sources:**
- [Al Jazeera — Musk says US military controls Starlink's limits after Ukraine outcry](https://www.aljazeera.com/news/2026/10/14/ukraine-accuses-elon-musks-spacex-of-throttling-starlink-terminals) · 14 October 2026
- [Kommersant — «Ukraine does not see ballistics» (Украина не видит баллистики)](https://www.kommersant.ru/doc/9026560) · 15 October 2026
**Trend:** ↗ Escalating
**Tags:** #Ukraine #missile-strike #air-defense #MULTI-SOURCE

---

> 💼 **BUSINESS ANALYST** · 3 updates today

### 5. IMF lifts 2026 growth to 3.1% but flags Hormuz drag 🟡
**Alert:** 🟡
**Summary:** The IMF's October World Economic Outlook, released in Bangkok on 13 October, raised 2026 world growth by 0.1 percentage points to 3.1% (3.4% in 2027), as AI-investment strength offsets Middle East war damage. Advanced economies are forecast at 2.1% (+0.4 pp), emerging markets at 3.7% (−0.1 pp); the US grows 2.3% and the euro area 1.1%. Hormuz disruption could subtract 0.9 pp from world growth; oil averages USD 95.74/bbl in 2026, about 41% above 2025. Global inflation is projected at 4.7%. Al Jazeera noted sharp Middle East and Central Asia downgrades.
**Market signal:** Bearish for energy-importing economies and their currencies, with AI-hardware supply chains the main offset.
**Sources:**
- [Xinhua — «IMF raises 2026 world growth forecast to 3.1%» (IMF上调2026年世界经济增长预期至3.1%)](https://www.news.cn/world/20261013/e8ced5fb852d4ab6be645b75dfa62fd5/c.html) · 13 October 2026
- [Al Jazeera — Iran war live: Tehran vows to fight until US yields as ships sink in Hormuz](https://www.aljazeera.com/news/liveblog/2026/10/15/iran-war-live-tehran-vows-to-fight-until-us-yields-as-ships-sink-in-hormuz) · 15 October 2026
**Trend:** → Stable
**Tags:** #IMF #GDP-forecast #inflation #MULTI-SOURCE
📎 See also: Conflict § Story 1 — Two ships sunk near Hormuz as Tehran vows to fight on

### 6. US CPI accelerates to 3.7% 🟡
**Alert:** 🟡
**Summary:** US annual inflation rose to 3.7% in September from 3.4% in August, with prices up 0.6% month on month, in the last CPI report before the 3 November midterms. Petrol rose 9.1% on the month, accounting for over half the monthly increase, and is 34.2% higher year on year. The Fed raised rates by 25 bp last month to 3.75–4.00%, its first hike in three years. CME FedWatch shows 52.9% odds of a hold and 47.1% of a hike at the late-October meeting. The Nasdaq fell 0.8% and the S&P 500 0.6% in midday trading.
**Market signal:** Bearish for US equities and duration, because energy-led inflation keeps a second Fed hike close to a coin-flip.
**Sources:**
- [Al Jazeera — US inflation rises before midterm elections, fuelling rate hike fears](https://www.aljazeera.com/economy/2026/10/14/us-inflation-rises-before-midterm-elections-fuelling-rate-hike-fears) · 14 October 2026
**Trend:** ↗ Escalating
**Tags:** #inflation #Fed #interest-rates #single-source
📎 See also: Conflict § Story 1 — Hormuz attacks and Houthi strikes on Aramco underpin the oil and petrol price surge

### 7. IEA: diesel deficit to persist until H2 2027 🟡
**Alert:** 🟡
**Summary:** The IEA's October report, published 14 October, shows Gulf product exports at 1.9 mb/d in September versus 4.7 mb/d before the war, after Middle East refinery damage. Global gasoil output fell 1.7 mb/d year on year to 27.2 mb/d in Q3, and combined Russian and Middle East gasoil exports dropped over 60% to 820 kb/d. Diesel in Europe and the US hit a record USD 220/bbl in September, nearly double crude. Q3 fuel demand fell 750 kb/d to 28.7 mb/d. The IEA sees no diesel stock rebuild before H2 2027.
**Market signal:** Bullish for diesel prices and refining margins, because the IEA projects no stock recovery before the second half of 2027.
**Sources:**
- [Kommersant — «Diesel is short of capacity» (Дизелю не хватает мощности)](https://www.kommersant.ru/doc/9026683) · 14 October 2026
**Trend:** → Stable
**Tags:** #energy-markets #supply-shock #oil-price #single-source
📎 See also: Conflict § Story 1 — Hormuz disruption is the driver of the product-supply shortfall

---

> 🇪🇺 **EU AFFAIRS ANALYST** · 3 updates today

### 8. EU opens Ukraine and Moldova talks on internal market and competitiveness 🟡
**Alert:** 🟡
**Summary:** On 13 October the EU opened accession negotiations with Ukraine and with Moldova on the acquis covering internal market, competitiveness and inclusive growth. The same day Albania and the EU provisionally closed negotiations on enterprise and industrial policy (chapter 20). The steps come ahead of the European Council meeting of 15–16 October, where leaders are due to take stock of enlargement and Ukraine.
**Legislative/policy stage:** Negotiating clusters opened with Ukraine and Moldova on 13 October 2026; chapter 20 provisionally closed with Albania; European Council meets 15–16 October 2026.
**Sources:**
- [Council of the EU — Enlargement: EU opens accession negotiations with Ukraine on internal market, competitiveness and inclusive growth](https://www.consilium.europa.eu/en/press/press-releases/2026/10/13/enlargement-eu-opens-accession-negotiations-with-ukraine-on-internal-market-competitiveness-and-inclusive-growth/) · 13 October 2026
- [Council of the EU — Enlargement: EU and Moldova start negotiations on internal market, competitiveness and inclusive growth](https://www.consilium.europa.eu/en/press/press-releases/2026/10/13/enlargement-eu-and-moldova-start-negotiations-on-internal-market-competitiveness-and-inclusive-growth/) · 13 October 2026
- [Council of the EU — Enlargement: Albania and EU provisionally close negotiations on enterprise and industrial policy](https://www.consilium.europa.eu/en/press/press-releases/2026/10/13/enlargement-albania-and-eu-provisionally-close-negotiations-on-enterprise-and-industrial-policy/) · 13 October 2026
**Trend:** ↗ Escalating
**Tags:** #EU-enlargement #Ukraine #institutional

### 9. Largest-ever EU listing targets almost 1,600 Russian military-industrial entities 🟡
**Alert:** 🟡
**Summary:** On 12 October the Council adopted restrictive measures against 826 Russian companies and 743 individuals active in Russia's military-industrial complex, the single largest set of listings since the start of the war. Separately, it listed 77 individuals involved in the illegal Russian State Duma "elections" held in September 2026 in occupied Ukrainian territories. The Council also added three individuals and four entities to its DPRK list over nuclear and missile programmes and Russia ties.
**Legislative/policy stage:** Restrictive measures adopted by the Council on 12 October 2026.
**Sources:**
- [Council of the EU — Russia's war of aggression against Ukraine: EU agrees largest-ever package of listings targeting almost 1600 individuals and entities in Russia's military-industrial complex](https://www.consilium.europa.eu/en/press/press-releases/2026/10/12/russia-s-war-of-aggression-against-ukraine-eu-agrees-largest-ever-package-of-listings-targeting-almost-1600-individuals-and-entities-in-russia-s-military-industrial-complex/) · 12 October 2026
- [Council of the EU — Ukraine's territorial integrity: Council lists 77 individuals over the illegal Russian State Duma 'elections' in the temporarily occupied territories of Ukraine](https://www.consilium.europa.eu/en/press/press-releases/2026/10/12/ukraine-s-territorial-integrity-council-lists-77-individuals-over-the-illegal-russian-state-duma-elections-in-the-temporarily-occupied-territories-of-ukraine/) · 12 October 2026
**Trend:** ↗ Escalating
**Tags:** #EU-sanctions #Russia #institutional

### 10. Council gives final approval to AGILE defence programme 🟢
**Alert:** 🟢
**Summary:** The Council formally adopted the regulation establishing the programme for agile and rapid defence innovation (AGILE) on 12 October. The new €115 million programme is designed to support small and medium-sized enterprises developing emerging and disruptive defence products.
**Legislative/policy stage:** Regulation formally adopted by the Council on 12 October 2026 (final step of the legislative procedure).
**Sources:**
- [Council of the EU — Programme for agile and rapid defence innovation: Council gives final green light](https://www.consilium.europa.eu/en/press/press-releases/2026/10/12/programme-for-agile-and-rapid-defence-innovation-council-gives-final-green-light/) · 12 October 2026
**Trend:** → Stable
**Tags:** #EU-defence #institutional

---

> 🤖 **TECHNOLOGY ANALYST** · 2 updates today

### 11. Starshield speed cap hits Ukraine's drone operations 🟡
**Alert:** 🟡
**Summary:** Ukrainian officials accused SpaceX of throttling Starlink and its military variant Starshield overnight, limiting service for terminals travelling above 100 mph, according to an adviser to President Zelensky. The cap restricts satellite-piloted drones and Ukraine's ability to counter Shahed drones. Elon Musk wrote on X that speed and usage limits are set by the US military and ultimately the president; the White House neither confirmed nor denied this. Poland, which pays for Ukrainian Starlink subscriptions, and US Senator Jeanne Shaheen demanded the restrictions end.
**Analyst note:** Within 12–24 months, expect European defence budgets to prioritise redundant, sovereign satellite connectivity for drone command-and-control, removing dependence on a US-controlled throttle.
**Sources:**
- [Al Jazeera — Musk says US military controls Starlink's limits after Ukraine outcry](https://www.aljazeera.com/news/2026/10/14/ukraine-accuses-elon-musks-spacex-of-throttling-starlink-terminals) · 14 October 2026
**Trend:** ↗ Escalating
**Tags:** #autonomous-systems #drone-warfare #Ukraine #single-source
📎 See also: Conflict § Story 4 — Kyiv loses US missile warnings amid pressure over refinery strikes

### 12. Hackers push hundreds of French supermarket freezers to 50°C 🟡
**Alert:** 🟡
**Summary:** Hundreds of French supermarkets were hit by a cyberattack overnight on 11–12 October, French broadcaster BFM Business reported, according to Xinhua. Attackers remotely manipulated refrigeration controllers made by Denmark's Danfoss, forcing continuous defrost and raising set temperatures to 50°C, destroying fresh and frozen stock. Losses nationwide could reach millions of euros. The head of Coopérative U confirmed the attack and called it unprecedented and extremely serious. France's ANSSI confirmed a vulnerability in the vendor's software and is coordinating with European counterparts.
**Analyst note:** Within 12–24 months, expect tighter scrutiny of operational-technology vendors under the EU's NIS2 and Cyber Resilience Act regimes, and insurers repricing food-retail cold-chain cyber risk.
**Sources:**
- [Xinhua — «Cyberattack hits refrigeration systems at hundreds of French supermarkets» (法国数百家超市制冷系统遭网络攻击)](https://www.news.cn/world/20261013/41ca848b7a5848ab8332f39850137d75/c.html) · 13 October 2026
**Trend:** ↗ Escalating
**Tags:** #cyber #single-source

---

> 📈 **TRENDS ANALYST** · 3 updates today

### 13. FAO Food Price Index edges up to 136.0 in September 🟡
**Alert:** 🟡
**Summary:** The FAO Food Price Index averaged 136.0 points in September, up 1.5% on August and 5.8% above a year earlier, driven by cereals, vegetable oils and sugar. The cereal index rose 5.1%, with wheat at its highest since August 2023 and maize at a three-year-plus high; FAO cited Black Sea logistics constraints and uncertainty over Hormuz shipping, which keeps fuel, fertiliser and freight costs elevated. Sugar reached its highest since April 2025. Meat and dairy indices declined. Latest available release (2 October); next due 6 November.
**Horizon:** Medium-term: crop-led price pressure persists through the northern winter wheat season while Hormuz-linked input costs stay elevated.
**Sources:**
- [FAO — FAO Food Price Index edges up in September on higher sugar, cereal and vegetable oil prices](https://www.fao.org/worldfoodsituation/foodpricesindex/en/) · 02 October 2026
**Trend:** ↗ Escalating
**Tags:** #food-prices #food-security #institutional

### 14. DRC Ebola outbreak passes 9,000 confirmed cases 🟡
**Alert:** 🟡
**Summary:** The Democratic Republic of the Congo's health ministry reported 9,066 confirmed Ebola cases and 4,381 deaths as of 13 October, with 2,389 recoveries and a fatality rate of about 48.3%; the outbreak, declared on 15 May, has reached seven provinces. It is caused by the Bundibugyo strain, for which no approved vaccine or specific therapy exists. The Coalition for Epidemic Preparedness Innovations said a Phase 2/3 vaccine trial is in final preparation and expected to start within weeks, with Ervebo the first candidate.
**Horizon:** Medium-term: absent an effective countermeasure, the outbreak is likely to extend into 2027; trial results are the key inflection.
**Sources:**
- [Xinhua — «Current Ebola outbreak in DR Congo exceeds 9,000 confirmed cases» (刚果（金）本轮埃博拉疫情确诊病例超9000例)](https://www.news.cn/world/20261013/ea81f628f6e74cd6bdb5ef04b9f35301/c.html) · 13 October 2026
**Trend:** ↗ Escalating
**Tags:** #humanitarian #day-154 #single-source

### 15. Gulf crude exports recover via Hormuz bypass; product exports lag 🟢
**Alert:** 🟢
**Summary:** Gulf crude exports rose 4.4 mb/d in September to 13.9 mb/d, mainly through reworked maritime logistics and shipments bypassing the Strait of Hormuz, according to the IEA's October report cited by Kommersant. Recovery was described as "in full swing". Refined-product exports from the region remain more than halved against pre-war levels. Russian oil and product supply edged down 10 kb/d to 6.52 mb/d, while export revenue rose USD 3.6 billion to USD 17.67 billion on higher Urals prices.
**Horizon:** Medium-term: bypass routing is becoming a durable feature of Gulf trade flows, while damaged refining capacity sets the pace of product-market normalisation.
**Sources:**
- [Kommersant — «Diesel is short of capacity» (Дизелю не хватает мощности)](https://www.kommersant.ru/doc/9026683) · 14 October 2026
**Trend:** ↘ De-escalating
**Tags:** #Hormuz #shipping #energy-markets #single-source
📎 See also: Business § Story 7 — IEA: diesel deficit to persist until H2 2027

---

## ⚙️ AGENT METADATA

| Field | Value |
|-------|-------|
| Agent version | MORNING BRIEF v1.7.7 |
| Run timestamp | 2026-10-15T05:16:27+02:00 |
| Sources queried | 17 / 17 |
| Stories surfaced | 24 |
| Stories published | 15 |
| Languages processed | EN, RU, ZH, DE, FR |
| Output language | English (British) |
| Date validated | ✅ Confirmed 15 October 2026 |
| Expansion Queue | None |
| Coverage pass | 17 / 17 sources touched (light or deep) |
| Deep-dive calls by category | Conflict 6, Business 5, EU Affairs 4, Technology 1, Trends 1 |

---

MORNING BRIEF is an AI-assisted digest. All summaries are paraphrased from original sources.
Verify time-sensitive information at the linked URLs before acting.
Output language: British English.
