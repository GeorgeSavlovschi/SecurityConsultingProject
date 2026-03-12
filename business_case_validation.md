# Business Case Validation Playbook

**Last updated:** 2026-03-12
**Purpose:** Validate market demand for automated security guardrail assessment tool before committing development investment
**Related documents:** [vietnam_market_research.md](vietnam_market_research.md) | [security_agent_plan.md](security_agent_plan.md) | [certifications.md](certifications.md)

---

## 1. Validation Philosophy

Product validation follows a two-phase framework:

1. **Demand Validation** — Do they have the problem? Is it painful enough to pay for a solution?
2. **Solution Validation** — Does our specific approach (automated security guardrails) solve it better than their current workaround?

These are fundamentally different questions. Most failed products skip the first and jump straight to building a solution for a problem that doesn't hurt enough. CB Insights data shows 42% of startups fail because they build something nobody wants — making "no market need" the single most common cause of startup death, ahead of running out of cash (29%) and team problems (23%).

The goal of this playbook is to reach a **go/no-go decision in 4-5 months with under $2,000 in direct cost** (excluding founder time). Founder time during validation is not wasted even if the decision is "no-go" — the customer relationships, market knowledge, and consulting revenue generated during validation have standalone value.

**Key principle:** Each phase is a gate. If a phase fails, STOP — do not proceed to the next phase. This prevents sunk-cost-driven product development. The emotional pull to keep going after investing weeks of effort is the single biggest threat to rational decision-making. Define kill criteria before you start, and honor them.

---

## 2. Validation Phases (8-Phase Sequential Framework)

### Phase 1: Customer Discovery Interviews (Weeks 1-3, ~$0)

**Methodology:** Steve Blank Customer Development / Lean B2B (Etienne Garbugli)

**What to do:**
- Recruit 15-20 CTOs/technical leads at Vietnamese software firms (10-150 developers)
- Conduct 30-60 minute problem interviews (NOT solution interviews)
- Spend 90% listening, 10% talking
- Do NOT mention your product concept

**How to recruit in Vietnam:**
- CTO Vietnam Network (Facebook Group) — the single most targeted channel for Vietnamese technical decision-makers
- LinkedIn Sales Navigator targeting CTOs at Vietnamese software firms
- GDG Hanoi and GDG HCMC meetups for in-person conversations
- Viblo platform outreach to active security-interested authors
- Warm introductions through accelerator networks (VIISA, VSV Capital)
- Offer a free 30-minute security mini-assessment as interview incentive

**Interview questions (problem discovery, NOT solution pitching):**
1. "Walk me through the last time a client asked about your security practices"
2. "What happens when your team needs to respond to a security questionnaire?"
3. "How do you currently handle code security review before releases?"
4. "Have you ever lost a deal or had a deal delayed because of security concerns?"
5. "What's your biggest worry about the new PDPL/Decree 356 requirements?"
6. "If you could wave a magic wand and fix one security-related problem, what would it be?"

**Cultural considerations for Vietnam:**
- Relationships first (quan he) — cold outreach underperforms; invest in warm introductions
- Face (the dien) — frame questions neutrally, never imply poor security
- Indirect communication — "maybe" often means "no"; read non-verbal cues
- Business over meals — dinner meetings yield more honest feedback than formal surveys
- Facebook Messenger and Zalo are primary business channels, often more effective than email
- Conduct interviews in Vietnamese if possible

**Go/no-go gate:**
- **PASS:** 8+ of 15 prospects describe security as a top-3 business problem unprompted, have tried workarounds, and express urgency
- **FAIL:** Problem acknowledged but ranked low priority, or "we'll deal with it when we have to"
- **PIVOT SIGNAL:** If the pain is real but centered on a different problem than expected (e.g., compliance documentation rather than vulnerability scanning), adjust the product hypothesis

**Evidence to collect:** Verbatim quotes, recurring pain points (tally them), current workaround costs, budget signals, specific lost-deal stories

---

### Phase 2: Jobs-to-be-Done Mapping (Weeks 2-4, ~$0)

**Methodology:** Clayton Christensen JTBD / Tony Ulwick Opportunity Scoring (Strategyn)

**What to do:**
- From the Phase 1 interviews, map the "jobs" each stakeholder is trying to accomplish
- Identify functional jobs (pass security audit), emotional jobs (feel confident about security posture), social jobs (appear credible to international clients)
- Score each job using Ulwick's formula: **Opportunity Score = Importance + (Importance - Satisfaction)**
- Jobs with score >15 represent strong market gaps

**Stakeholder map for Vietnamese software firms:**

| Stakeholder | Functional Job | Emotional Job | Social Job |
|---|---|---|---|
| CTO/Tech Lead | Pass client security audits, protect codebase | Feel confident code is secure | Appear competent to international clients |
| Founder/CEO | Win international contracts, comply with PDPL | Avoid reputation damage from breach | Signal maturity to investors/clients |
| Developer | Ship secure code without slowing down | Not feel responsible for security gaps | Be seen as a skilled engineer |
| Account/Project Manager | Respond to security questionnaires quickly | Not lose deals over security gaps | Maintain client trust |

**Go/no-go gate:**
- **PASS:** 2+ jobs with Opportunity Score >15; your product concept addresses them
- **FAIL:** All important jobs are already well-served by existing solutions (DIY tools, existing vendors)
- **KEY INSIGHT:** The most valuable job in Vietnamese outsourcing firms is likely "respond credibly to international client security requirements within 48 hours" — validate this hypothesis

---

### Phase 3: Bottom-Up Market Sizing (Weeks 4-5, ~$0)

**Methodology:** TAM/SAM/SOM with bottom-up unit economics

**What to do:**
- Count the actual addressable firms, don't just cite top-down market reports
- Use real data: VINASA membership data, Clutch.co Vietnam software listings, LinkedIn company search

**Bottom-up calculation template:**

| Metric | Estimate | Source/Validation |
|---|---|---|
| Total digital technology enterprises in Vietnam | 73,788 | MIC 2024 data |
| Software firms with 10-150 developers | ~4,000-6,000 | Estimate from IT park registries, VINASA |
| Firms with international clients (outsourcing) | ~2,000-4,000 | Clutch.co, VINASA export data |
| Firms with active security budget | ~20-30% of above | Validate via Phase 1 interviews |
| Realistic year-1 reachable firms | ~200-500 | HCMC + Hanoi, outsourcing segment only |
| Average annual contract value | $1,200-3,600 | Based on Basic/Standard tier monthly pricing |
| Year-1 SOM (conservative) | 30-50 firms = $36K-180K ARR | Requires 6-10% conversion from reachable |
| Year-2 SOM (growth) | 80-150 firms = $96K-540K ARR | Word-of-mouth + content marketing |
| Year-3 SOM (scaling) | 200-400 firms = $240K-1.44M ARR | Regional expansion potential |

**Go/no-go gate:**
- **PASS:** Year-3 SOM exceeds $500K ARR with reasonable assumptions (validates viable solo/small-team business)
- **FAIL:** SOM requires unrealistic market share (>15% of reachable firms) or unrealistic pricing
- **CROSS-CHECK:** Compare bottom-up estimate with the top-down Vietnam cybersecurity market size ($310M). Your SOM should be <1% of TAM — if it's higher, your assumptions are too aggressive

**Data sources for Vietnam:**
- VINASA (Vietnam Software and IT Services Association) — membership directory
- Clutch.co Vietnam cybersecurity and software development listings
- LinkedIn company search (filter: Vietnam, 11-200 employees, Information Technology and Services)
- B-Company database (900,000+ Vietnamese enterprises)
- VCCI industry reports

---

### Phase 4: Smoke Test / Landing Page (Weeks 5-7, $500-1,500)

**Methodology:** Lean Startup smoke test, reference Buffer's validation approach

**What to do:**
- Build a single landing page (Vietnamese primary, English secondary) describing the product
- Include: value proposition, 3-4 key features, pricing signals (tier names + approximate ranges), "Request Assessment" CTA
- Drive qualified traffic from Vietnamese developer channels
- Measure behavioral signals

**Traffic sources (Vietnam-specific):**
- Facebook Ads targeting Vietnamese software professionals (most cost-effective in Vietnam)
- LinkedIn Ads targeting CTOs at Vietnamese software firms (10-200 employees)
- Posts in CTO Vietnam Network, Vietnam Devs (300K+ members), GDG groups
- Viblo sponsored post or article with CTA
- Zalo community sharing

**What to measure:**

| Metric | Target | Meaning |
|---|---|---|
| Visitor-to-signup conversion | >5% | Strong interest |
| "Request Assessment" clicks | >3% | Intent to buy |
| Pricing page visits | >15% of visitors | Price-conscious (good — means they're considering purchase) |
| Email signup for launch | >8% | Moderate interest |
| Contact form submissions | Any | Hot leads for Phase 5 |

**Minimum sample:** 300+ qualified visitors for statistical relevance

**Go/no-go gate:**
- **PASS:** >3% "Request Assessment" conversion from qualified traffic
- **FAIL:** <1% conversion despite well-targeted traffic and clear value proposition
- **ITERATE:** 1-3% — test different value propositions (compliance focus vs. vulnerability focus vs. cost-saving focus)

---

### Phase 5: Concierge MVP — Manual Security Assessments (Weeks 6-12, your time)

**Methodology:** Lean Startup Concierge MVP (not Wizard of Oz — be transparent that it's consultant-delivered)

**This is the most critical validation phase.** You deliver manually what the product would automate. The customer knows it's manual — no deception. This is arguably the best method for this specific product because you can start earning revenue while validating.

**What to do:**
1. Select 5 firms from Phase 1 interview pool who expressed strongest pain
2. Offer a comprehensive security assessment at 50% of planned Basic tier price ($250-600)
3. Manually run OWASP ZAP, Semgrep, Trivy, npm audit / pip-audit against their codebase
4. Write a prioritized findings report in Vietnamese with stack-specific remediation guidance
5. Map findings to PDPL/Decree 356 obligations (the compliance angle)
6. Present findings in a 60-minute walkthrough call
7. Observe: What do they care about? What do they ignore? What follow-up questions do they ask?
8. After delivery, ask: "Would you want this on an ongoing basis? At what price?"

**Tools to use (all free/OSS):**
- OWASP ZAP (web app scanning)
- Semgrep (SAST — static code analysis)
- Trivy (container/dependency scanning)
- npm audit / pip-audit / mvn dependency-check (SCA)
- OWASP Dependency-Track (SBOM)
- Manual OWASP ASVS Level 1 checklist review

**What to observe during delivery:**
- Which findings do they react to most strongly?
- Do they care more about vulnerability counts or compliance status?
- Do they share the report internally? With whom?
- Do they actually fix the findings?
- Do they ask about ongoing monitoring vs. one-time assessment?
- Would they refer you to another firm?

**Go/no-go gate:**
- **PASS:** 3+ of 5 firms willing to pay for a second engagement at full price, or refer you to peers
- **STRONG PASS:** Firms ask "can we get this every month?" or "can you do this for our other projects too?"
- **FAIL:** Firms take the report but show no interest in continuing, fixing issues, or paying more
- **PIVOT SIGNAL:** If they love the compliance mapping but don't care about vulnerability scanning (or vice versa), adjust the product focus

**Revenue validation:** Even at $300/assessment x 5 firms = $1,500 revenue during validation. This covers your Phase 4 ad spend.

---

### Phase 6: Pre-Sales / Letters of Intent (Weeks 10-13, ~$0)

**Methodology:** Y Combinator / Techstars pre-commitment validation

**What to do:**
- Approach 10-15 target firms (mix of Phase 1 contacts and new prospects)
- Present the product concept with mockups showing the automated dashboard
- Ask for a concrete commitment: either a pre-payment deposit or a signed LOI

**Vietnam adaptation:** Formal LOIs may create friction in Vietnamese business culture. Adapt to lighter formats:
- Email confirmation of intent to purchase at a specific price point
- Pre-payment via bank transfer or VNPay for a discounted annual subscription
- Zalo/Messenger commitment with screenshot (surprisingly effective in Vietnamese B2B)
- Verbal commitment from a known contact (relationship-weighted)

**Pre-sale offer structure:**
- "Pre-order annual security assessment subscription at 40% off launch price"
- VND 15-25M (~$600-1,000) for annual Basic tier (vs. $1,200-1,500 at launch)
- Money-back guarantee if product doesn't deliver within 90 days of launch
- Early adopter benefits: priority support, product input, case study co-creation

**Go/no-go gate:**
- **PASS:** 5+ firms commit money (even small deposits) or sign LOIs with budget authority
- **STRONG PASS:** Firms ask to pay immediately or request accelerated timeline
- **FAIL:** Firms say "interesting, let me know when it's ready" but won't commit anything
- **CAUTION:** LOIs are non-binding. Vietnamese verbal commitments may be polite non-commitments. Weight actual money transfer 5x higher than verbal intent.

**Patrick McKenzie benchmark:** "If you can get 10 people to hand you money for a product that doesn't exist yet, you've validated demand better than 99% of startups"

---

### Phase 7: Paid Pilot Program (Weeks 12-20, your time)

**Methodology:** Standard B2B SaaS pilot methodology (SaaStr framework)

**What to do:**
- Structure 6-8 week paid pilots with 3-5 firms
- Define success criteria upfront (agreed with the customer)
- Require executive sponsorship (CTO or founder must be involved)
- Price at a level that maintains commitment: $150-300/month (not free — free attracts tire-kickers)
- Provide dedicated implementation support

**Pilot success criteria (agree with each customer):**

| Metric | Target |
|---|---|
| Critical/high vulnerabilities identified | >5 per project |
| Time from scan to report delivery | <48 hours |
| Remediation guidance rated "actionable" | >80% of findings |
| Compliance gaps mapped to PDPL/Decree 356 | Full coverage |
| Customer satisfaction (1-10) | >7 |
| Would recommend to peer (yes/no) | Yes |

**Go/no-go gate:**
- **PASS:** >50% pilot-to-paid conversion (industry benchmark is 40-60%)
- **STRONG PASS:** >60% conversion + unprompted referrals
- **FAIL:** <30% conversion despite good implementation support
- **KEY METRIC:** Do pilot customers expand scope (add more projects, more frequent scans)? Expansion is stronger signal than initial conversion.

---

### Phase 8: Product-Market Fit Measurement (Week 20+, ~$0)

**Methodology:** Sean Ellis PMF Survey / Superhuman PMF Engine (Rahul Vohra)

**Prerequisites:** You need 20+ users who have experienced core value (used the service at least 2x in last 2 weeks)

**What to do:**
- Survey all users with the core question: "How would you feel if you could no longer use this security assessment service?"
  - Very disappointed
  - Somewhat disappointed
  - Not disappointed
- Follow-up questions:
  - "What is the primary benefit you receive?"
  - "What type of person do you think would benefit most?"
  - "How can we improve the service for you?"

**Go/no-go gate:**
- **PMF ACHIEVED:** >40% "very disappointed" — proceed to full product build
- **ITERATE:** 25-40% — promising but needs refinement. Segment by user type (Superhuman approach): focus on "very disappointed" users, understand WHY they love it, build more of that
- **PIVOT OR KILL:** <25% — insufficient product-market fit. Re-examine assumptions.

**Superhuman extension:** Segment results by firm type (outsourcing vs. fintech vs. SaaS). If outsourcing firms show 50%+ "very disappointed" but fintech shows 15%, double down on outsourcing.

---

## 3. Pricing Validation (Parallel Track)

### Van Westendorp Price Sensitivity Meter

Run this survey alongside Phases 5-7 once you have enough contacts (target 30-50 responses minimum for B2B).

**Four questions (after describing the product clearly):**
1. At what monthly price is this service too expensive — you would never consider it?
2. At what monthly price is it expensive but you would still consider it?
3. At what monthly price is it a good deal — you'd feel you're getting good value?
4. At what monthly price is it so cheap you'd question the quality?

**Analysis:** Plot cumulative frequency distributions. The intersections give you:
- **Optimal Price Point (OPP):** Where "too cheap" and "too expensive" cross
- **Indifference Price Point (IDP):** Where "cheap" and "expensive" cross
- **Acceptable range:** Between the "too cheap/expensive" extremes

**Segment by company size** — firms with 10-30 developers will have very different price sensitivity than firms with 100-150 developers.

---

## 4. Vietnam-Specific Validation Channels

### Primary channels for reaching decision-makers

| Channel | Type | Audience | Best For |
|---|---|---|---|
| CTO Vietnam Network (Facebook) | Community | CTOs, tech leads | Problem interviews, surveys |
| Vietnam Devs (Facebook, 300K+) | Community | Developers | Bottom-up awareness, feature validation |
| LinkedIn Vietnam (4M+ users) | Professional network | Internationally-connected tech leaders | Direct outreach to outsourcing firm CTOs |
| Viblo | Content platform | Vietnamese developers | Content marketing, credibility building |
| GDG Hanoi / GDG HCMC | Meetup | Developers, tech leads | In-person interviews, demos |
| Zalo | Messaging | All Vietnamese professionals | Direct outreach, follow-up |
| Vietnam Information Security Day (VNISA) | Conference | Security professionals, 1000+ attendees | Event validation, networking |
| CyberSecVietnam Conference | Conference | Cybersecurity ecosystem | Competitive intelligence, partnerships |
| WeBuild Community | Developer alliance | Developers, makers | Community engagement |

### Local market research firms (if budget allows)

| Firm | Specialty | Cost Range | Best For |
|---|---|---|---|
| Mekong Research | B2B tech research since 1997 | $5,000-20,000 | Structured decision-maker interviews |
| N-Equals | Tech sector specialist | $5,000-15,000 | Recruiting B2B tech decision-maker panels |
| B-Company | 900K+ enterprise database | $3,000-10,000 | Large-scale survey distribution |
| Cimigo | 120+ researchers, market entry | $10,000-50,000 | Comprehensive market entry studies |

### Accelerator programs for structured validation

| Program | What They Provide | Stage |
|---|---|---|
| VIISA | Pre-acceleration with customer discovery mentorship | Pre-seed |
| VSV Capital | Product/business model validation | Pre-seed/Seed |
| Vietnam Startup Hub | Hypothesis validation with user interviews | Early |
| FastTrack AI Accelerator | Enterprise PoC commitments, GTM grants ($1M+) | Growth |

---

## 5. Secondary Validation Data (Already Available)

Before running primary research, these existing data points provide directional validation.

### Demand signals (positive)

| Signal | Data Point | Source |
|---|---|---|
| Attack volume | 659,000 cyberattacks in Vietnam, 2024 | NCA 2025 |
| Breach severity | 14.5M accounts compromised (12% of global) | Viettel 2024 Report |
| Skills gap | 700,000 professional shortfall through 2028 | Vietnam Security Summit 2025 |
| Maturity gap | Only 11% of Vietnamese firms cybersecurity-mature | Cisco 2025 |
| Staffing gap | 47.72% of organizations have insufficient cybersecurity personnel | NCA 2025 Survey |
| Regulatory deadline | PDPL/Decree 356 effective Jan 2026; Cybersecurity Law Jul 2026 | Government gazette |
| Budget signal | VCCI: 75% of companies prioritize data protection | VCCI Survey |
| Market fragmentation | Top 5 players hold <35% combined share | Mordor Intelligence |

### Risk signals (negative/cautionary)

| Signal | Data Point | Source |
|---|---|---|
| Cost sensitivity | 55.6% of SMEs cite technology cost as biggest limitation | VCCI Survey |
| Low awareness | 27.8% have zero security standards implemented | NCA 2025 |
| DIY preference | Developers self-assess; free OSS tools are the default | Phase 1 interviews will confirm |
| Decision complexity | Vietnamese SMEs average 6.8 stakeholders in purchase decisions | B2B buying research |
| Trust barrier | New entrant in security domain faces trust deficit | Market observation |

### What secondary data tells us

The demand signals are strong on paper. But secondary data cannot tell you:
- Whether firms will **pay** for a solution (vs. continuing to ignore the problem)
- Whether **your specific approach** (automated guardrails) resonates vs. manual consulting
- What **price point** the market will bear
- Whether the **outsourcing segment** is truly the right entry point

This is why primary validation (Phases 1-8) is non-negotiable.

---

## 6. Kill Criteria — When to Walk Away

Be explicit about what would cause you to abandon this business.

| Phase | Kill Signal | What It Means |
|---|---|---|
| 1 | <5 of 15 CTOs rank security as top-3 problem | Market education cost is too high; problem isn't urgent enough |
| 3 | Year-3 SOM < $200K ARR | Market too small for the investment required |
| 4 | <1% landing page conversion from qualified traffic | Value proposition doesn't resonate; messaging problem or deeper demand issue |
| 5 | 0-1 of 5 firms willing to pay for second engagement | Solution doesn't deliver enough value to justify cost |
| 6 | <3 pre-sales from 15 approaches | Willingness to pay is too low |
| 7 | <30% pilot-to-paid conversion | Product doesn't retain after initial curiosity |
| 8 | <25% Sean Ellis "very disappointed" | No product-market fit — pivot or kill |

**The hardest kill decision:** If Phase 5 (concierge) shows firms love the report but won't pay ongoing — the problem may be real but the business model (subscription) is wrong. Consider pivoting to one-time assessment model before killing entirely.

---

## 7. Validation Budget Summary

| Phase | Direct Cost | Time Investment | Cumulative Cost |
|---|---|---|---|
| 1. Customer Discovery | ~$0 | 2-3 weeks (part-time) | $0 |
| 2. JTBD Mapping | ~$0 | 1-2 weeks (analysis) | $0 |
| 3. Market Sizing | ~$0 | 1 week | $0 |
| 4. Smoke Test | $500-1,500 | 2 weeks | $500-1,500 |
| 5. Concierge MVP | ~$0 (your time) | 4-6 weeks | $500-1,500 |
| 6. Pre-Sales | ~$0 | 2-3 weeks | $500-1,500 |
| 7. Paid Pilots | ~$0 (your time) | 6-8 weeks | $500-1,500 |
| 8. PMF Survey | ~$0 | 1 week | $500-1,500 |
| **Total** | **$500-1,500** | **~20 weeks / 5 months** | — |

**Revenue during validation:** Phases 5-7 should generate $3,000-10,000 in consulting revenue, making this validation process cash-flow neutral or positive.

**Optional: Professional market research (Phase 3 enhancement):** $5,000-20,000 via Mekong Research or N-Equals for a structured study of 50-100 decision-makers. Only do this if Phase 1 interviews are inconclusive and you need quantitative confirmation before proceeding.

---

## 8. Decision Framework — The Final Call

After completing all phases, score each dimension:

| Dimension | Weight | Score (1-5) | Weighted |
|---|---|---|---|
| Problem urgency (Phase 1) | 25% | ___ | ___ |
| Market size (Phase 3) | 15% | ___ | ___ |
| Demand signal (Phase 4) | 15% | ___ | ___ |
| Willingness to pay (Phases 5-6) | 25% | ___ | ___ |
| Product-market fit (Phases 7-8) | 20% | ___ | ___ |
| **Total** | **100%** | | ___ |

**Decision thresholds:**
- **Score >3.5:** GREEN — Proceed to full product development
- **Score 2.5-3.5:** YELLOW — Promising but risky. Consider a lean build (automate only the most-validated features) or continue concierge model while iterating
- **Score <2.5:** RED — Do not invest in product development. Either pivot the approach or exit

---

## 9. What "Validated" Looks Like — Concrete Targets

Before committing to building the automated tool, you should have ALL of these:

- [ ] 15+ customer discovery interviews completed (Vietnamese CTOs, 10-150 dev firms)
- [ ] 8+ interviewees confirmed security is a top-3 business problem
- [ ] 2+ high-opportunity JTBD identified with Opportunity Score >15
- [ ] Bottom-up SOM shows >$500K ARR achievable in year 3
- [ ] Landing page conversion >3% from qualified Vietnamese traffic
- [ ] 5+ concierge assessments delivered with 3+ willing to pay for ongoing service
- [ ] 5+ pre-sales or LOIs with actual money committed
- [ ] 50%+ pilot-to-paid conversion from 3+ pilots
- [ ] Sean Ellis score >40% from 20+ users

**If you can check 7+ of these 9 boxes, build the product. If fewer than 5, don't.**

---

## Sources

### Validation Methodologies
- Steve Blank, "The Four Steps to the Epiphany" (2003)
- Eric Ries, "The Lean Startup" (2011)
- Etienne Garbugli, "Lean B2B" (2014)
- Rahul Vohra, "How Superhuman Built an Engine to Find Product-Market Fit" (First Round Review)
- Tony Ulwick / Strategyn, "Jobs-to-be-Done" framework
- Sean Ellis, GrowthHackers — PMF Survey methodology
- Patrick McKenzie (patio11), pre-sales validation principles
- a16z, "A Framework for Finding a Design Partner"
- SaaStr, pilot-to-contract conversion benchmarks (40-60%)
- CB Insights, "Top Reasons Startups Fail" (42% = no market need)

### Vietnam Market Research
- NCA 2025 Organizational Cybersecurity Survey (5,300+ organizations)
- Cisco Cybersecurity Readiness Index 2025 — Vietnam Edition
- VCCI SME Digital Transformation Reports
- Mordor Intelligence, Vietnam Cybersecurity Market Report
- VINASA membership data
- Clutch.co Vietnam cybersecurity vendor directory
- CTO Vietnam Network (Facebook)
- Vietnam Devs community (300,000+ members)
- Viblo platform (viblo.asia)
- Mekong Research (mekongresearch.com)
- N-Equals (n-equals.com)
- B-Company (b-company.jp) — 900,000+ Vietnamese enterprise database
- VIISA accelerator (viisa.vn)
- VSV Capital accelerator (vsvcapital.com.vn)
- Vietnam Information Security Day / VNISA (securityday.vn)
