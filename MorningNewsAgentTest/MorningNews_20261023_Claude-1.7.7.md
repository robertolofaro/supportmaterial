Brief is written; sharing the file now.

Your Morning Brief for 23 October 2026 is ready in `morning_brief_2026-10-23.md`: 15 stories across all five categories, 4 🔴, 8 🟡 and 3 🟢.

This was a degraded run on source coverage. I reached 11 of 17 Tier 1 and Tier 2 sources, so the coverage gate wasn't fully met.

- **Not reached:** El País, Handelsblatt, the European Parliament, Eurostat, the World Bank and FAO. I skipped these because the fetches were consuming too much context.
- **Fetched but no usable story:** NPR (its homepage was stale, with February 2026 content), the IMF (latest item 7 October), and the ECB and European Commission (navigational shells only).
- **Searches that found nothing usable:** the outlet-scoped searches for Bloomberg, the Guardian and Euronews.

Reported casualty figures differ between sources, so I recorded both. Xinhua said one person was killed in the Saudi airport attack; Al Jazeera's later headline says two. Iranian claims are attributed throughout and have not been independently verified.

Tier 4 sources were used only as corroboration. The tag `#satellite-comms` is logged as an Expansion Queue candidate, because Story 12 had no fitting tag in the closed list.

```yaml
---
brief_date: 2026-10-23
version: v1.7.7
run_time: "05:16 CET"
stories_published: 15
categories: [conflict, business, eu_affairs, technology, trends]
alert_counts:
  red: 4
  yellow: 8
  green: 3
ongoing_situations:
  - {name: "US–Israel war on Iran", real_world_start: "2026-02-28", day: 238}
sources_fetched: 8
fetch_status:
  kommersant: "✅"
  xinhua: "✅"
  european_parliament: "❌"
  european_council: "✅"
expansion_queue: ["#satellite-comms"]
---
```

# 🌐 MORNING BRIEF
## Friday, 23 October 2026 · 05:16 CET
### 15 stories across 5 categories

## DIGEST SUMMARY

| # | Category | Headline | Alert |
|---|----------|----------|-------|
| 1 | ⚔️ Conflict | US–Israel war on Iran: IRGC declares "offensive" doctrine as strike preparations are reported | 🔴 |
| 2 | ⚔️ Conflict | Strait of Hormuz: Iran says seven vessels hit | 🔴 |
| 3 | ⚔️ Conflict | Saudi Arabia: Houthi strikes on airport and oilfield, US orders staff out | 🔴 |
| 4 | ⚔️ Conflict | Russia–Ukraine: Moscow signals mid-November trilateral talks | 🟡 |
| 5 | 💼 Business | Brent crude above 110 USD/bbl on Hormuz and Saudi disruption | 🔴 |
| 6 | 💼 Business | Global debt explainer: France now pays more to borrow than Italy and Greece | 🟡 |
| 7 | 💼 Business | Moscow Exchange index falls about 1% | 🟡 |
| 8 | 🇪🇺 EU Affairs | Council and Parliament strike deal on securitisation market | 🟢 |
| 9 | 🇪🇺 EU Affairs | ETS market stability reserve: provisional agreement | 🟢 |
| 10 | 🇪🇺 EU Affairs | Ukraine financing and MFF: Costa reports to Parliament, special summit set | 🟡 |
| 11 | 🤖 Technology | Digital Omnibus: Council agrees mandate on GDPR, cookies and incident reporting | 🟡 |
| 12 | 🤖 Technology | Starlink throttling in Ukraine: Rubio attributes decision to Musk | 🟡 |
| 13 | 📈 Trends | France: cost-of-living unrest, curfews and a new protest call | 🟡 |
| 14 | 📈 Trends | Serbia: student movement heads into 25 October snap election | 🟡 |
| 15 | 📈 Trends | Climate: reef extinction warning and UNEP emissions verdict | 🟢 |

> Alert Level key: 🔴 High significance · 🟡 Developing · 🟢 Stable/Routine

## 🚨 SIGNAL BOARD

---
🔴 **Brent crude trades above 110 USD/bbl on 22 October as Iran claims seven vessels hit in and near Hormuz**
---
🔴 **IRGC announces an "offensive" doctrine; US orders non-emergency staff and families out of Saudi Arabia**
---
🟡 **Russia says it is ready to restart US–Russia–Ukraine trilateral talks in mid-November**
---
🟡 **More than 500,000 people marched across France on 17 October; localised curfews now in force**
---
🟢 **Council and Parliament reach two provisional deals in one day: securitisation and the ETS reserve**
---

---

> ⚔️ **CONFLICT ANALYST** · 4 updates today

### 1. US–Israel war on Iran — Day 238 🔴
**Alert:** 🔴
**Summary:** The IRGC announced on 21 October an "offensive and asymmetrical" doctrine, threatening to invade countries that launch attacks on Iran. IRGC spokesman Hossein Mohebi said Iran's missile stockpile has grown 1.5 times since the June 2025 war, without giving figures. President Trump said the US is no longer negotiating and that events would come "fairly soon"; he previously pledged no attack before the 3 November midterms. Netanyahu reiterated his pledge to topple Iran's government. Xinhua reported dozens of Israeli aircraft approaching the Iranian border in a simulated strike and several explosions in southern Iran.
**Significance:** Both sides are positioning for another round, with the US midterms and Israel's 27 October election likely to shape timing. Analyst Negar Mortazavi told Al Jazeera that Tehran is seeking to raise the cost of any future attack, including through its leverage over Hormuz.
**Sources:**
- [Al Jazeera — Iran reveals 'offensive' doctrine, US issues alert: Is war imminent?](https://www.aljazeera.com/news/2026/10/22/iran-reveals-offensive-doctrine-us-issues-alert-is-war-imminent) · 22 October 2026
- [Kommersant — «Iran threatens neighbours with a land war» (Иран угрожает соседям войной на суше)](https://www.kommersant.ru/doc/9044995) · 22 October 2026
- [Xinhua — «Dozens of Israeli warplanes approach Iranian border, simulating strike on Iran» (数十架以军战机飞近伊朗边境 模拟对伊打击)](https://www.news.cn/world/20261022/309095206a5243bc921481da1fdeea55/c.html) · 22 October 2026
**Trend:** ↗ Escalating
**Tags:** #Iran #Israel #escalation #day-238

### 2. Strait of Hormuz 🔴
**Alert:** 🔴
**Summary:** The IRGC Navy said four vessels it accused of illegal oil transfers were struck and caught fire in the northern Persian Gulf, and three others hit naval mines west of the strait. Iranian state TV reported seven ships hit in total; the IRGC warned the US of a wider response against American bases. Iran has offered a seven-day plan to restore shipping in return for an end to the US blockade of Iranian ports, sanctions relief and unfrozen assets. Xinhua reported on 20 October that Iran had placed 122 vessels on a Hormuz "violation list".
**Significance:** Regional exporters have rebuilt volumes via pipelines and alternative routes, but the new attacks reopen the insurance and security premium on the waterway.
**Sources:**
- [Al Jazeera — Iran says seven ships hit in Hormuz Strait, warns US of wider response](https://www.aljazeera.com/news/2026/10/22/iran-says-seven-ships-hit-in-hormuz-strait-warns-us-of-wider-response) · 22 October 2026
- [The Hill — Iran claims 7 oil tankers struck in the Strait of Hormuz](https://thehill.com/policy/defense/6164731-iran-navy-hits-oil-tankers/) · 22 October 2026
- [Xinhua — «Iran says 122 vessels placed on Hormuz Strait "violation list"» (伊朗称122艘船只被列入霍尔木兹海峡“违规名单”)](https://www.news.cn/world/20261020/cbf43b16057c4556828dcc6bbbd597aa/c.html) · 20 October 2026
**Trend:** ↗ Escalating
**Tags:** #Hormuz #Iran #shipping #MULTI-SOURCE

### 3. Saudi Arabia — Houthi strikes and US staff drawdown 🔴
**Alert:** 🔴
**Summary:** The US State Department ordered non-emergency government employees and their families to leave Saudi Arabia on 21 October after Houthi attacks; it said the order covers Saudi Arabia only. Xinhua reported an attack on Dammam's international airport that killed one and injured eight, and a drone attack on an eastern oilfield in which interception debris killed two and injured two. Al Jazeera's later headline on the airport attack puts the death toll at two. Yemen's Houthis claimed six strikes on Saudi targets in 48 hours, per Xinhua's 20 October report.
**Significance:** Houthi pressure on Saudi infrastructure undermines Riyadh's pipeline bypass of Hormuz, linking the Yemen and Gulf theatres.
**Sources:**
- [Xinhua — «US orders non-emergency government employees and families to evacuate Saudi Arabia» (美国下令驻沙特“非紧急”政府雇员及家属撤离)](https://www.news.cn/world/20261022/3de1a0f95a254129989ab70e1130cb3f/c.html) · 22 October 2026
- [Xinhua — «Attack on Saudi Dammam international airport kills one, injures eight» (沙特达曼国际机场遭袭致一死8伤)](https://www.news.cn/world/20261022/0fbcd2a4756244a298dd62d8fe6432a0/c.html) · 22 October 2026
- [Xinhua — «Drone attack on Saudi eastern oilfield; interception debris kills two, injures two» (沙特东部油田遭无人机袭击 拦截碎片坠落致2死2伤)](https://www.news.cn/world/20261022/fa7954fdf40944b58f8b0c3c1bd57586/c.html) · 22 October 2026
- [Al Jazeera — Attack on Saudi Arabia's King Fahd airport kills two people](https://www.aljazeera.com/news/2026/10/22/one-killed-eight-injured-in-attack-on-saudi-arabias-king-fahd-airport-2) · 22 October 2026
**Trend:** ↗ Escalating
**Tags:** #missile-strike #drone-warfare #humanitarian #MULTI-SOURCE

### 4. Russia–Ukraine — diplomacy 🟡
**Alert:** 🟡
**Summary:** Kremlin aide Yuri Ushakov said on 21 October that Putin told US envoy Steve Witkoff that Russia is ready to restart US–Russia–Ukraine trilateral talks in mid-November. Xinhua separately reported that Zelensky agreed to a "freeze of the current status" to open talks. Kommersant reported on 22 October that the EU is again searching for an envoy to talk to Putin.
**Significance:** Moscow's offer arrives after Witkoff's talks in Oslo with Zelensky and Norway's prime minister, where Article 5-like security guarantees were discussed ([Kyiv Independent — Witkoff to visit St. Petersburg after Zelensky talks, Norway's PM says](https://kyivindependent.com/witkoff-to-visit-st-petersburg-after-zelensky-talks-norways-pm-says/) · 20 October 2026). A territorial freeze remains the core unresolved issue.
**Sources:**
- [Xinhua — «Russian presidential aide: Russia ready to restart Russia-US-Ukraine trilateral talks in November» (俄总统助理：俄方准备在11月重启俄美乌三方会谈)](https://www.news.cn/world/20261021/23803b51c09f454dab8ff0792a3f1db3/c.html) · 21 October 2026
- [Xinhua — «Zelensky says he agrees to "freeze status quo" to start peace talks» (泽连斯基说同意“冻结现状”开启和谈)](https://www.news.cn/world/20261021/e9ce7103f07e4fbfb604c668b688c159/c.html) · 21 October 2026
- [Kommersant — «Russia is being offered an interlocutor» (России подбирают собеседника)](https://www.kommersant.ru/doc/9044963) · 22 October 2026
**Trend:** → Stable
**Tags:** #Russia #Ukraine #peace-talks #MULTI-SOURCE

> 💼 **BUSINESS ANALYST** · 3 updates today

### 5. Brent crude above 110 USD/bbl 🔴
**Alert:** 🔴
**Summary:** Brent climbed above 110 USD/bbl on 22 October, according to Al Jazeera, as the IRGC claimed seven vessels hit near Hormuz and Houthi attacks on Saudi Arabia hit energy infrastructure. The Hill reported Brent above 111 USD/bbl on Thursday morning. Al Jazeera noted that oil shipments from the region returned to pre-war levels last month through alternative routes, yet prices have surged again.
**Market signal:** Bullish — the supply-risk premium is re-expanding on shipping and infrastructure attacks despite rerouted flows.
📎 See also: Conflict § Story 2 — Iran claims seven vessels hit in and near the Strait of Hormuz.
**Sources:**
- [Al Jazeera — Iran reveals 'offensive' doctrine, US issues alert: Is war imminent?](https://www.aljazeera.com/news/2026/10/22/iran-reveals-offensive-doctrine-us-issues-alert-is-war-imminent) · 22 October 2026
- [The Hill — Iran claims 7 oil tankers struck in the Strait of Hormuz](https://thehill.com/policy/defense/6164731-iran-navy-hits-oil-tankers/) · 22 October 2026
**Trend:** ↗ Escalating
**Tags:** #Brent #oil-price #Hormuz #MULTI-SOURCE

### 6. Global debt: France now pays more to borrow than Italy and Greece 🟡
**Alert:** 🟡
**Summary:** Al Jazeera's 22 October explainer reports the world is 365 trillion USD in debt with the interest bill climbing. It says protests in Europe have highlighted the debt squeeze, and that France now pays more to borrow than Italy and Greece. Specific yield levels were not retrievable in this run (N/A).
**Market signal:** Bearish for French government bonds — the borrowing-cost ranking has inverted against Paris relative to Rome and Athens.
📎 See also: Trends § Story 13 — France cost-of-living unrest and curfews.
**Sources:**
- [Al Jazeera — The world is $365 trillion in debt, and the interest bill is climbing](https://www.aljazeera.com/news/2026/10/22/the-world-is-365-trillion-in-debt-and-the-interest-bill-is-climbing) · 22 October 2026
**Trend:** ↗ Escalating
**Tags:** #eurozone #interest-rates #data-point #single-source

### 7. Moscow Exchange index falls about 1% 🟡
**Alert:** 🟡
**Summary:** Kommersant reported that the Moscow Exchange index fell about 1%, under a headline framing the move as a retreat tied to negotiations. Kommersant's site ticker at the time of fetch showed IMOEX at 2,433.70, USD/RUB at 81.97 and EUR/RUB at 91.93. The claim rests on a single outlet.
**Market signal:** Bearish — Russian equities pulled back as the negotiation backdrop weighed on sentiment, per Kommersant.
**Sources:**
- [Kommersant — «Negotiating retreat: Moscow Exchange index rolls back 1%» (Переговорное отступление)](https://www.kommersant.ru/doc/9044215) · 22 October 2026
**Trend:** → Stable
**Tags:** #equity-selloff #Russia #single-source

> 🇪🇺 **EU AFFAIRS ANALYST** · 3 updates today

### 8. Savings and investments union — securitisation deal 🟢
**Alert:** 🟢
**Summary:** On 21 October the Council and Parliament agreed new rules to revitalise the EU's securitisation market, described as an integral part of the savings and investments union and the "One Europe, One Market" roadmap to boost growth.
**Legislative/policy stage:** Provisional agreement reached 21 October 2026; formal adoption by Parliament and Council pending.
**Sources:**
- [Council of the EU — Savings and investments union: Council and Parliament strike deal to revitalise the EU's securitisation market](https://www.consilium.europa.eu/en/press/press-releases/2026/10/21/savings-and-investments-union-council-and-parliament-strike-deal-to-revitalise-the-eu-s-securitisation-market/) · 21 October 2026
**Trend:** → Stable
**Tags:** #EU-institutions #single-market #institutional

### 9. ETS market stability reserve — provisional agreement 🟢
**Alert:** 🟢
**Summary:** The Council and Parliament reached a provisional agreement on a targeted amendment to the rules on invalidating allowances in the ETS market stability reserve, aimed at increasing long-term market liquidity and predictability.
**Legislative/policy stage:** Provisional agreement reached 21 October 2026; formal adoption by Parliament and Council pending.
**Sources:**
- [Council of the EU — ETS market stability reserve: Council and Parliament reach provisional agreement on targeted amendment](https://www.consilium.europa.eu/en/press/press-releases/2026/10/21/ets-market-stability-reserve-council-and-parliament-reach-provisional-agreement-on-targeted-amendment/) · 21 October 2026
**Trend:** → Stable
**Tags:** #climate-policy #EU-institutions #institutional

### 10. Ukraine financing and the MFF — summit track 🟡
**Alert:** 🟡
**Summary:** European Council President António Costa reported to the Parliament plenary on 21 October on the 15–16 October European Council. A Special European Council is set for 26–27 November in Brussels. Kommersant reported that Brussels does not know where to find funds to meet Ukraine's growing requests. On 19 October the Council agreed a partial negotiating position on the common market organisation for agricultural products under the 2028–2034 MFF.
**Legislative/policy stage:** Special European Council scheduled 26–27 November 2026; MFF 2028–2034 negotiations ongoing at Council working level.
**Sources:**
- [European Council — Report by President António Costa to the European Parliament plenary session](https://www.consilium.europa.eu/en/press/press-releases/2026/10/21/report-by-president-antonio-costa-to-the-european-parliament-plenary-session/) · 21 October 2026
- [European Council — Media advisory: Accreditation for the Special European Council, 26 and 27 November 2026](https://www.consilium.europa.eu/en/press/press-releases/2026/10/19/media-advisory-accreditation-for-the-special-european-council-26-and-27-november-2026/) · 19 October 2026
- [Council of the EU — MFF 2028-2034: Council agrees position on the common market organisation for agricultural products](https://www.consilium.europa.eu/en/press/press-releases/2026/10/19/mff-2028-2034-council-agrees-position-on-the-common-market-organisation-for-agricultural-products/) · 19 October 2026
- [Kommersant — «EU looks for money for Kyiv in other people's pockets» (ЕС ищет деньги для Киева в чужих карманах)](https://www.kommersant.ru/doc/9044727) · 22 October 2026
**Trend:** → Stable
**Tags:** #Ukraine-aid #EU-funds #MFF #institutional

> 🤖 **TECHNOLOGY ANALYST** · 2 updates today

### 11. Digital Omnibus — Council mandate on data, privacy and cyber reporting 🟡
**Alert:** 🟡
**Summary:** On 21 October the Council agreed its position on the digital simplification proposal (Omnibus VII). The mandate amends the GDPR, keeps the current definition of personal data and adds a pseudonymisation provision. It also extends the personal data breach notification deadline, updates e-privacy cookie rules to reduce banners, and replaces the proposed EU single entry point for incident reporting with a national entry point in each member state. The AI-related part of the package was adopted on 29 June 2026.
**Analyst note:** With the roadmap targeting completion of all simplification files by end-2027, changes to GDPR, cookie and incident-reporting obligations are unlikely to bind companies before 2028, and the national-entry-point model will keep cross-border reporting fragmented in the interim.
**Legislative stage:** Council negotiating mandate agreed 21 October 2026; trilogues start once Parliament adopts its own position.
**Sources:**
- [Council of the EU — Digital rulebook: Council agrees position to simplify data protection, privacy and cyber reporting rules](https://www.consilium.europa.eu/en/press/press-releases/2026/10/21/digital-rulebook-council-agrees-position-to-simplify-data-protection-privacy-and-cyber-reporting-rules/) · 21 October 2026
**Trend:** → Stable
**Tags:** #digital-regulation #cyber #EU-institutions #institutional

### 12. Starlink throttling in Ukraine — Rubio blames Musk 🟡
**Alert:** 🟡
**Summary:** US Secretary of State Marco Rubio said on 21 October that the decision to throttle Ukraine's Starlink use was taken by SpaceX chief Elon Musk, not the White House, which had no advance knowledge. Rubio said on 17 October that Ukraine never had access to the military Starshield version. Musk has said Starshield is US government-owned and any restrictions are set by the US military, ultimately the president. The Wall Street Journal reported on 20 October that Musk made the decision last week and discussed it with Trump, per Xinhua. Xinhua also reported on 19 October that Ukraine wants to use Starshield for deep strikes in Russia and that Rubio said it cannot.
**Analyst note:** Contested accounts of who controls battlefield connectivity strengthen, over the next 12–24 months, the case for sovereign or multi-vendor satellite communications in European defence planning.
📎 See also: Conflict § Story 4 — Russia–Ukraine diplomacy.
**Sources:**
- [Xinhua — «US secretary of state says Ukraine's Starlink speed limit was Musk's doing» (美国务卿称乌“星链”限速系马斯克所为)](https://www.news.cn/world/20261021/28b88d19ce1c4a16973b2d9a782fff69/c.html) · 21 October 2026
- [Xinhua — «Ukraine wants to use US "Starshield" for deep strikes on Russia; Rubio: cannot» (乌欲借美“星盾”打击俄纵深 鲁比奥：用不了)](https://www.news.cn/world/20261019/ea5e838779304677851f87455306aa56/c.html) · 19 October 2026
**Trend:** ↗ Escalating
**Tags:** #Ukraine #diplomacy #single-source

> 📈 **TRENDS ANALYST** · 3 updates today

### 13. France — cost-of-living unrest 🟡
**Alert:** 🟡
**Summary:** More than half a million people protested across France on 17 October, combining students demanding better school conditions with groups rejecting the cost of living, after four weeks of school protests. Xinhua reported more than 2,000 arrests. Prime Minister Sébastien Lecornu ordered localised curfews, which brought a calmer night. Al Jazeera reported that the main trade unions did not back a new protest call for this Saturday and were due to meet Lecornu on Wednesday.
**Horizon:** Medium-term — social strain over living costs and borrowing costs is likely to persist for months, with a French election cycle approaching.
📎 See also: Business § Story 6 — France's borrowing costs versus Italy and Greece.
**Sources:**
- [Al Jazeera — France to impose new curfews where required after calm night](https://www.aljazeera.com/amp/news/2026/10/20/france-to-impose-new-curfews-where-required-after-calm-night) · 20 October 2026
- [Xinhua — «Several French cities impose partial curfews to prevent repeat of unrest» (法国多城实施局部宵禁防止骚乱重演)](https://www.news.cn/world/20261020/82043bab7d364688bae2dd32dded1c9d/c.html) · 20 October 2026
- [Xinhua — «Protests erupt across several European countries; over 2,000 arrested in France» (欧洲多国爆发示威活动 法国2000多人被捕)](https://www.news.cn/world/20261018/2a66022f0846465690d6fc58463d6811/c.html) · 18 October 2026
**Trend:** → Stable
**Tags:** #public-opinion #social-contract #MULTI-SOURCE

### 14. Serbia — student movement and the 25 October election 🟡
**Alert:** 🟡
**Summary:** Serbia holds snap elections on 25 October. Al Jazeera reports that students arrived in central Belgrade on 21 October after walking for several days for the movement's final major rally on 22 October, and that the system they have built poses a threat to President Aleksandar Vučić's grip on power.
**Horizon:** Short-term — the vote is days away; the result will set the medium-term direction of domestic politics and relations with Brussels.
**Sources:**
- [Al Jazeera — From the streets to the ballot box: Serbia's students hope for election win](https://www.aljazeera.com/news/2026/10/22/from-the-streets-to-the-ballot-box-serbias-students-hope-for-election-win) · 22 October 2026
**Trend:** ↗ Escalating
**Tags:** #election #public-opinion #single-source

### 15. Climate — reef extinction warning and UNEP emissions verdict 🟢
**Alert:** 🟢
**Summary:** Al Jazeera reported on 22 October that a study warns almost all shallow-water coral reefs now face extinction risk. Xinhua reported on 21 October that the UN Environment Programme found global emissions cuts are working but remain insufficient.
**Horizon:** Long-term — a multi-year structural trend; mitigation is showing effect but not at the pace needed to ease pressure on ecosystems.
**Sources:**
- [Al Jazeera — Almost all shallow-water coral reefs now face extinction risk, study warns](https://www.aljazeera.com/news/2026/10/22/almost-all-shallow-water-coral-reefs-now-face-extinction-risk-study-warns) · 22 October 2026
- [Xinhua — «UNEP: global emissions cuts effective but efforts still insufficient» (联合国环境署：全球减排有成效但力度仍不足)](https://www.news.cn/world/20261021/755c4e32097e4106be0aca94a790f6ed/c.html) · 21 October 2026
**Trend:** ↗ Escalating
**Tags:** #climate #single-source

## ⚙️ AGENT METADATA

| Field | Value |
|-------|-------|
| Agent version | MORNING BRIEF v1.7.7 |
| Run timestamp | 2026-10-23T05:16:29+02:00 |
| Sources queried | 11 / 17 |
| Stories surfaced | 24 |
| Stories published | 15 |
| Languages processed | EN, RU, ZH |
| Output language | English (British) |
| Date validated | ✅ Confirmed 23 October 2026 |
| Expansion Queue | #satellite-comms (Technology; used #Ukraine #diplomacy as nearest tags in Story 12) |
| Coverage pass | 11 / 17 sources touched. Deep: Kommersant, Xinhua, Al Jazeera, European Council. Light/empty: NPR (stale February 2026 content), IMF (latest item 7 October), ECB and European Commission (navigational shell only), Bloomberg, The Guardian and Euronews (outlet-scoped searches returned no usable dated items). Not reached: El País, Handelsblatt, European Parliament, Eurostat, World Bank, FAO. |
| Deep-dive calls by category | Conflict 4, Business 2, EU Affairs 2, Technology 2, Trends 1 |

---

MORNING BRIEF is an AI-assisted digest. All summaries are paraphrased from original sources.
Verify time-sensitive information at the linked URLs before acting.
Output language: British English.
