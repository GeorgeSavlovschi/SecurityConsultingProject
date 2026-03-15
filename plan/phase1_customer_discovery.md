# Phase 1: Customer Discovery — Operational Playbook

**Last updated:** 2026-03-15
**Purpose:** Step-by-step field manual for validating whether Vietnamese software firms will pay for automated security assessments
**Duration:** Weeks 1-10 (2.5 months, weekends only)
**Budget:** $111-320
**Related documents:** [business_case_validation.md](../business_case_validation.md) | [vietnam_market_research.md](../vietnam_market_research.md) | [security_agent_plan.md](../security_agent_plan.md) | [certifications.md](../certifications.md)

---

## Part 1: Mission and Objectives

### 1.1 Hypothesis to Validate

**Primary hypothesis:**
> Vietnamese software firms (10-150 developers) with international clients experience security as a top-3 business pain point and will pay $60-120/month for automated security guardrail assessments.

**Secondary hypotheses:**
- Software outsourcing firms (serving Japanese, Korean, US, Australian clients) are the right entry segment
- The PDPL (Personal Data Protection Law) / Decree 356 (effective January 2026) creates regulatory urgency that unlocks security budgets
- Free/open-source tools (OWASP ZAP, Semgrep, Trivy) are insufficient for these firms because they lack the expertise to run, interpret, and act on them
- A foreign founder can build sufficient trust ("quan he") to sell security services in Vietnam

### 1.2 Key Assumptions to Test

Each assumption maps to specific interview questions. Rate your confidence BEFORE starting interviews, then update AFTER.

| # | Assumption | Category | Pre-Interview Confidence (1-5) | Interview Question That Tests It | What "PASS" Looks Like | What "FAIL" Looks Like |
|---|-----------|----------|-------------------------------|----------------------------------|----------------------|----------------------|
| A1 | Security is painful enough to prioritize over feature development | Value | ___ | Q4 (lost deals), Q6 (magic wand) | 8+ of 15 rank it top-3 unprompted; describe specific incidents with emotional weight | Acknowledged when asked but never comes up organically; "important but not urgent" |
| A2 | International client questionnaires are the primary trigger for security investment | Value | ___ | Q1 (client asked about security), Q2 (security questionnaire) | 10+ interviewees describe scrambling to respond to questionnaires; 3+ have lost or delayed deals | Questionnaires are rare or handled easily without external help |
| A3 | Budget exists at $60-120/month for automated scanning | Viability | ___ | Follow-up to Q6: "What would you pay to solve that?" | 5+ interviewees name a price range overlapping $60-120; 3+ have current security spending | Universal response: "We would not pay for this" or budget caps at <$20/month |
| A4 | Free tools (ZAP, Semgrep, Trivy) are insufficient — firms lack expertise | Value | ___ | Q3 (code review process) | Most firms have never heard of these tools, or tried and abandoned them | Firms already use these tools effectively and don't need a managed layer |
| A5 | PDPL/Decree 356 creates actionable urgency | GTM | ___ | Q5 (PDPL worry) | 5+ describe specific compliance anxiety; at least 2 have begun planning | "We haven't looked into it" or "Our lawyer handles it" |
| A6 | Outsourcing firms are the right beachhead (higher pain than domestic-only firms) | Strategy | ___ | Compare interview intensity across segments | Outsourcing firms consistently show stronger pain, clearer budgets, more urgency | Domestic SaaS firms or fintech show equal or stronger pain signals |
| A7 | Foreign founder trust deficit is manageable | GTM | ___ | Observe: are they comfortable? Do they share openly? Do they follow up? | Interviewees engage openly, offer referrals, add you on Zalo | Guarded responses, no follow-up, preference for "local" providers stated |

### 1.3 Success Metrics and Kill Criteria

**Primary go/no-go gate (after 15+ interviews):**

| Metric | PASS | FAIL | KILL |
|--------|------|------|------|
| Security ranked top-3 problem (unprompted) | 8+ of 15 (>53%) | 5-7 of 15 (iterate) | <5 of 15 — market education cost too high |
| Specific incident stories (lost deal, breach scare, scrambled questionnaire) | 5+ concrete stories | 2-4 stories | 0-1 — pain is theoretical, not felt |
| Budget signal (discussed pricing, named a number, has current spending) | 5+ interviewees | 3-4 interviewees | <3 — willingness to pay unvalidated |
| Referrals offered (unprompted) | 3+ referrals | 1-2 referrals | 0 — not interesting enough to share |
| CyStack awareness + unmet needs | 3+ aware but describe gaps | 1-2 aware | All satisfied with CyStack — no room for differentiation |

**Kill the project if:** <5 of 15 rank security as top-3, AND <3 have budget signals, AND CyStack already covers their needs. Do not spend 12 months educating a market that does not feel pain.

### 1.4 Timeline: 10-Week Calendar

| Week | Saturday | Sunday Evening / Weekday Evenings | Target |
|------|----------|----------------------------------|--------|
| **1** | Set up Zalo, join CTO Vietnam Network (Facebook), prepare business cards, order gifts | Draft outreach messages, begin sending (10-15 messages) | 0 interviews, 10+ messages sent |
| **2** | Continue outreach, attend GDG meetup if available | Schedule first 2-3 meetings, refine scripts | 0-1 interviews, 5+ meetings scheduled |
| **3** | Interview 1-2 | Transfer notes, rate pain points, send thank-yous | 1-2 total interviews |
| **4** | Interview 3-4 | Notes, tally tracker, identify emerging patterns | 3-4 total interviews |
| **5** | Interview 5-6 | **Mid-point check:** on track for 15? Any segment performing better? Adjust targeting | 5-6 total interviews |
| **6** | Interview 7-8 | First pattern analysis: which pain points are dominant? | 7-8 total interviews |
| **7** | Interview 9-10 | Update persona drafts, check assumption confidence ratings | 9-10 total interviews |
| **8** | Interview 11-12 | Deeper analysis: are outsourcing firms showing stronger pain than domestic? | 11-12 total interviews |
| **9** | Interview 13-15 | Begin synthesizing: draft personas, update all trackers | 13-15 total interviews |
| **10** | Final interviews 16-20 (if pipeline allows) | **Final analysis:** score go/no-go gate, draft value proposition, decide | 15-20 total interviews |

**Scheduling assumptions:** 75% success rate on scheduling. Not every week yields a meeting. Some weeks you may do 0, some weeks 3 if back-to-back.

---

## Part 2: Target Profile

### 2.1 Ideal Customer Profile

**Firmographic profile:**

| Attribute | Ideal | Acceptable | Reject |
|-----------|-------|------------|--------|
| Company size | 20-80 developers | 10-150 developers | <10 (too small, no budget) or >150 (has in-house security team) |
| Revenue | $1M-5M | $500K-$10M | <$500K (survival mode) |
| Location | HCMC (District 1, 7, Thu Duc, Binh Thanh) | Hanoi, Da Nang | Outside major cities |
| Client mix | 50%+ international (Japan, Korea, US, AU) | Any international clients | 100% domestic with no expansion plans |
| Tech stack | Java, Python, Node.js, React, Docker | .NET, PHP, Vue, Angular | Legacy COBOL, mainframe |
| Founded | 2015-2022 | 2005-2024 | Pre-2005 (likely too established to change) |
| Role of contact | CTO or Tech Lead | Founder/CEO with technical background | HR, sales, non-technical roles |

**Behavioral markers (what makes them "ideal"):**
- Has received a security questionnaire from an international client in the past 12 months
- Uses GitHub or GitLab (indicates modern development practices amenable to CI/CD integration)
- CTO is English-capable (can engage with your product later)
- Has NOT hired a dedicated security person (the gap your product fills)
- Has tried DIY security efforts (ran a free scanner once, Googled "OWASP") but did not sustain them

**Anti-profile (who to exclude):**
- Enterprise firms (>150 devs) with existing security teams or SOC contracts
- Non-software firms (hardware distributors, telcos, IT resellers)
- Firms with no international clients AND no regulatory exposure (no urgency trigger)
- Students, academics, or freelancers (no purchasing authority)

### 2.2 Market Segments

| Segment | Size Estimate | Pain Intensity | Budget Reality | Accessibility | Priority |
|---------|--------------|----------------|----------------|---------------|----------|
| **Software outsourcing** (Japan/Korea/US clients) | ~2,000-4,000 firms | HIGH — client questionnaires create deadline pressure | $2K-15K/year (unlocked by client contracts) | HIGH — concentrated in HCMC/Hanoi, active in CTO Vietnam Network | **PRIMARY** |
| **Fintech software** | ~200-500 firms | HIGH — regulatory mandated (Decree 94/2025, PDPL) | $5K-30K/year (compliance budget) | MEDIUM — smaller community, more cautious about sharing | **SECONDARY** |
| **B2B SaaS** (domestic-first, regional expansion) | ~500-1,000 firms | MEDIUM — feels pain when expanding to international markets | $2K-10K/year | HIGH — active in startup communities | **TERTIARY** |
| **Healthtech** | ~100-300 firms | MEDIUM-HIGH — patient data regulations | $3K-20K/year | LOW — specialized, harder to reach | **FUTURE** |

### 2.3 Beachhead Segment: Software Outsourcing Firms

**Why outsourcing firms are the right entry point (4-criteria evaluation):**

| Criterion | Score (1-5) | Evidence |
|-----------|-------------|----------|
| **Burning pain** | 5/5 | International client questionnaires create hard deadlines. Failure = lost contracts worth $50K-500K+. Pain is immediate, recurring, and has direct revenue impact. |
| **Willingness to pay** | 4/5 | Budget exists because security spending is directly tied to contract preservation. $60-120/month is <1% of typical contract value. ROI story is straightforward: "keep your clients." |
| **Winnable market share** | 4/5 | 2,000-4,000 firms, no dominant SME-focused player (CyStack is closest but not specialized in outsourcing compliance). Fragmented market with no lock-in. |
| **Referral potential** | 5/5 | Vietnamese CTO community is tight-knit. CTO Vietnam Network (Facebook), Viblo, and GDG meetups create natural word-of-mouth channels. One satisfied CTO tells 5 peers. |
| **Total** | **18/20** | Strong beachhead candidate |

**What to validate in interviews:** Is the outsourcing segment truly highest-pain, or does fintech show equal urgency? Track pain intensity by segment to confirm or adjust.

### 2.4 Decision-Maker Map

```
Primary Buyer: CTO / Technical Lead
├── Makes the tool decision for <$2K purchases
├── Evaluates technical fit
├── Pain trigger: client security questionnaire, failed audit
└── Where to find: CTO Vietnam Network, Zalo, GDG meetups, Viblo

Influencer: Project Manager / Account Manager
├── Surfaces the pain ("our client is asking about security")
├── Does NOT make the purchase decision
└── Useful for introductions to CTO

Secondary Buyer: CEO / Founder
├── Involved when cost exceeds ~$2K-3K
├── Cares about: will this help us win/keep clients?
├── Less technical, needs ROI framing
└── Often the same person as CTO in 10-30 person firms
```

**Buying triggers (what activates the purchase decision):**
1. International client sends a security questionnaire (most common)
2. Regulatory audit notice (PDPL/Decree 356)
3. Post-incident response (breach, vulnerability discovered)
4. Competitor wins a contract by demonstrating better security posture

---

## Part 3: Outreach Playbook

### 3.1 Outreach Scripts

#### Zalo/Messenger — Warm Introduction (Highest Success Rate)

**Vietnamese:**
> Chao anh [Given Name], em la [Your Name]. Anh [Mutual Contact's Name] gioi thieu em lien he voi anh. Em dang tim hieu ve van de bao mat trong cac cong ty phan mem VN. Anh co the danh 30 phut ca phe de em xin y kien cua anh khong a?

**English translation:**
> Hello [Name], I'm [Your Name]. [Mutual Contact] introduced me to reach out to you. I'm researching security challenges in Vietnamese software companies. Could you spare 30 minutes for coffee so I can get your perspective?

#### Zalo/Messenger — Cold (After Engaging with Their Content)

**Vietnamese:**
> Chao anh [Given Name], em doc bai viet cua anh ve [topic] tren [platform] — rat hay. Em dang nghien cuu ve cac thach thuc bao mat trong nganh phan mem VN. Anh co san sang chia se kinh nghiem qua mot buoi ca phe khong a?

**English translation:**
> Hello [Name], I read your article about [topic] on [platform] — very insightful. I'm researching security challenges in the Vietnam software industry. Would you be willing to share your experience over coffee?

#### LinkedIn — Connection Request (English, Formal)

> Hi [Given Name], I'm researching how Vietnamese software companies handle security and compliance challenges, particularly around international client requirements and PDPL. I'd love to hear your perspective as a technical leader at [Company]. Would you be open to a brief 30-minute conversation? I'm also happy to share a free security mini-assessment as a thank-you.

#### Email — Follow-up After Zalo/Messenger Contact

> Subject: Following up — security research conversation
>
> Hi Anh/Chi [Given Name],
>
> Thank you for connecting on [Zalo/LinkedIn]. As mentioned, I'm researching how Vietnamese software firms handle security challenges, especially around international client requirements.
>
> I'd appreciate 30 minutes of your time over coffee. In return, I can offer a free mini-assessment of your application's security posture.
>
> Would [Saturday morning / Saturday afternoon] work for you? I'm flexible on location — happy to come to wherever is convenient for you.
>
> Best regards,
> [Your Name]

#### Key Script Notes

- Use "anh" (for men) or "chi" (for women) + their **given name** (last part of full name: Nguyen Van **Minh** = "Anh Minh")
- Use "em" for yourself if they are older or more senior (safe default)
- Keep initial messages to 2-3 sentences maximum
- Reference something specific about them or their work (shows research effort)
- Always propose coffee (low commitment), never dinner (too high commitment for first contact)
- Have a Vietnamese friend review your Vietnamese messages before sending

### 3.2 Recruitment Channels

| # | Channel | Action Items | Expected Response Rate |
|---|---------|-------------|----------------------|
| 1 | **CTO Vietnam Network** (Facebook Group) | Join group. Spend weeks 1-2 reading and engaging (comments, likes) before any outreach. Do NOT post a "looking for interviews" request — it looks like spam. Instead, engage with posts about security topics, then DM individuals. | 15-25% response to DMs |
| 2 | **Zalo groups** | Find and join Vietnamese tech communities. Search for "CTO Vietnam", "DevOps Vietnam", "Security Vietnam". Same engagement-first approach. | 10-20% response |
| 3 | **LinkedIn** | Search: "CTO" + "Vietnam" + company size 11-200 + IT & Services. Send connection requests with note (script above). | 10-15% response |
| 4 | **GDG Hanoi / GDG HCMC meetups** | Attend in person. Do NOT pitch from the stage. Network during breaks. Collect Zalo contacts. Follow up within 48 hours. | 30-50% conversion from in-person contact |
| 5 | **Viblo** | Find authors who write about security, DevOps, or CI/CD. Comment on their articles thoughtfully. Then reach out via Zalo/LinkedIn. | 15-25% response |
| 6 | **Accelerator networks** (VIISA, VSV Capital) | Request portfolio introductions. Frame as research, not sales. Offer to share findings with the accelerator. | 20-40% if warm intro |
| 7 | **Free security mini-assessment** | Offer a 30-minute review of their public-facing application (basic OWASP ZAP scan + dependency check). This is your incentive — concrete value for their time. | Increases acceptance by ~2x |

**Outreach volume target:** Send 40-60 messages across channels in weeks 1-3 to generate 15-20 interviews by week 10.

### 3.3 Screening Criteria

Before confirming an interview, verify the prospect meets minimum criteria:

**Must have (all required):**
- [ ] Software company (builds software, not IT resale or hardware)
- [ ] 10-150 developers
- [ ] CTO, Tech Lead, or technical founder available (not HR or sales)
- [ ] Based in HCMC, Hanoi, or Da Nang

**Strongly preferred (at least 1):**
- [ ] Has international clients (Japan, Korea, US, Australia, EU)
- [ ] Has received a security questionnaire or audit request in the past 12 months
- [ ] Uses GitHub/GitLab with CI/CD pipelines

**Accept for comparison data:**
- Domestic-only firms (compare pain levels vs. outsourcing firms)
- Fintech firms (test whether regulatory pain is stronger than client-driven pain)

**Reject:**
- Firms with >150 developers and existing security team
- Non-technical contacts (PM or sales without CTO access)
- Students, freelancers, or academics

### 3.4 Vietnamese Business Etiquette — Quick Reference

**Before the meeting:**
- Arrive 5-10 minutes early. Being late is disrespectful
- Have business cards (present and receive with both hands, read theirs, place on table)

**First 5 minutes:**
- Small talk first (5-10 minutes). Do NOT jump to business
- Good topics: their company, food, travel, HCMC life
- Avoid: politics, religion, the war, criticism of Vietnam, salary questions
- Let them signal the transition to business. If they don't after 10 minutes: "I really appreciate your time today. I'm curious about..."

**During the meeting:**
- Order Vietnamese coffee ("ca phe sua da") to show cultural comfort
- If you invited them, offer to pay and insist once
- Do not split the bill — it feels transactional
- 90% listening, 10% talking. You are here to learn, not sell

**After the meeting:**
- Send a thank-you message on Zalo within 4 hours
- If they add you on Zalo = genuine interest signal
- One follow-up message is fine. Three in a week will damage the relationship
- If no response in 2 weeks, move on

**Naming:** Family-Middle-**Given**. Use "Anh" (men) or "Chi" (women) + given name (last part). "Nguyen Van Minh" = "Anh Minh". Never "Anh Nguyen."

**Venue recommendations (HCMC first meetings):**
- The Workshop Coffee (District 1) — popular with tech professionals
- Highlands Coffee (various) — familiar, neutral, inexpensive
- Starbucks (various) — signals international orientation
- Trung Nguyen Legend (various) — Vietnamese premium, shows cultural respect

---

## Part 4: Interview Execution

### 4.1 Full Interview Script

**Total time:** 40-60 minutes
**Core rule:** You are a researcher, not a salesperson. Never pitch. Never describe your product idea. Ask about their past, not your future.

---

#### Opening (5 minutes)

*Follow the Vietnamese meeting protocol from Section 3.4. Small talk first.*

When transitioning to business:

> "Thank you so much for taking the time, Anh/Chi [Name]. I'm doing research on how Vietnamese software companies handle security challenges. There are no right or wrong answers — I'm genuinely trying to understand your experience. Everything you share stays confidential. Would it be okay if I take notes?"

*Wait for confirmation. If they agree to recording (rare in first meetings), even better.*

> "Could you start by telling me a bit about your company? How many developers do you have, and what kind of projects do you work on?"

*Listen. Note: company size, sectors served, domestic vs. international clients, tech stack. This context shapes which questions to emphasize.*

---

#### Core Exploration (25-35 minutes)

Ask these questions in order. For each one, use the probing techniques in Section 4.2 to go deeper. Skip questions that don't apply (e.g., skip Q2 if they have no international clients).

**Q1: International Client Security Pressure**
> "Walk me through the last time a client asked about your security practices. What happened?"

*What you're listening for:* Specific stories about client questionnaires, scrambling to respond, deals delayed or lost. This tests Assumption A2.

*If they have international clients, probe deeper:*
- "How long did it take your team to respond?"
- "Did you have the answers ready, or did you need to figure things out?"
- "Has this ever delayed a contract signing?"

*If they have NO international clients, adapt:*
- "Have any of your domestic clients asked about security? What about when you bid on government projects?"

---

**Q2: Security Questionnaire Process**
> "What happens when your team needs to respond to a security questionnaire?"

*What you're listening for:* The process (or lack thereof). Who handles it? How long does it take? Is it painful or routine? This tests Assumption A2 and Pain Point 2.

*Probing:*
- "Who on your team is responsible for responding?"
- "Do you have a standard document you use, or do you start from scratch each time?"
- "How confident are you in the accuracy of your responses?"

---

**Q3: Current Security Review Process**
> "How do you currently handle code security review before releases?"

*What you're listening for:* Whether they use any tools (SAST, DAST, SCA), whether they do manual code review with security in mind, or whether they do nothing. This tests Assumption A4.

*Probing:*
- "Do your developers use any security scanning tools? Which ones?"
- "Have you tried any free tools like OWASP ZAP or Semgrep?" (Only ask if they mention tools first — don't plant ideas)
- "If you use tools, how do your developers handle the results?"
- "What percentage of your releases go through any kind of security check?"

---

**Q4: Lost Deals or Delayed Business**
> "Have you ever lost a deal or had a deal delayed because of security concerns?"

*What you're listening for:* Concrete revenue impact. Specific stories with dollar amounts, client names (even anonymized), and emotional weight. This tests Assumption A1 and is the strongest pain signal.

*Probing:*
- "Can you tell me roughly how much that deal was worth?"
- "What would you have needed to win it?"
- "After that experience, did anything change in how your team approaches security?"

*If they say "no":*
- "Have you ever been asked about security during a sales process and felt unprepared?"
- "Have any of your competitors won deals by demonstrating better security posture?"

---

**Q5: PDPL / Regulatory Concerns**
> "What's your biggest worry about the new Personal Data Protection Law and Decree 356 requirements?"

*What you're listening for:* Whether they know about PDPL at all, whether they've started planning, whether it creates urgency. This tests Assumption A5.

*Probing:*
- "Has your team started any preparation for PDPL compliance?"
- "Do you know what specific technical requirements apply to your company?"
- "How does your team typically handle new regulatory requirements?"

*If they haven't heard of PDPL:* Note this — it means regulatory urgency is not yet a buying trigger for this segment. Do NOT educate them about PDPL during the interview (you're a researcher, not a consultant).

---

**Q6: Magic Wand**
> "If you could wave a magic wand and fix one security-related problem in your company, what would it be?"

*What you're listening for:* Their #1 priority — which may be different from what you expect. This tests whether your product hypothesis matches their actual need.

*Probing:*
- "Why that problem specifically?"
- "What would it mean for your business if that problem were solved?"
- "How much would you pay to make that problem disappear permanently?"

*The budget question is intentionally last.* By this point, they've described their pain in detail. The price question feels natural, not like a sales pitch.

---

#### Competitor and Workaround Exploration (5 minutes)

> "What do you currently spend on security, if anything? Tools, services, consultants, internal time?"

*Probing:*
- "Have you heard of CyStack?" (Note: if yes, ask what they think of it and what's missing)
- "Have you ever hired a penetration testing company? How was that experience?"
- "Do your developers use any security tools as part of their workflow?"

---

#### Wrap-up (5 minutes)

> "This has been incredibly helpful. Is there anything about security challenges that I didn't ask about but you think is important?"

*Wait. Let them fill the silence. Often the most insightful comments come here.*

> "Who else in your network do you think would have interesting perspectives on this? Would you be comfortable making an introduction?"

*If they offer a referral: accept and follow up within 48 hours.*

> "Thank you so much for your time, Anh/Chi [Name]. I really appreciate your openness. If it would be useful, I'd be happy to do a quick security check on your public-facing application as a thank-you — no strings attached."

*Exchange Zalo contacts if you haven't already.*

### 4.2 Probing Techniques

When an interviewee gives a surface-level answer, use these to go deeper:

| Technique | When to Use | Example |
|-----------|-------------|---------|
| **"Tell me more about that"** | Any interesting statement | "You mentioned your team scrambles — tell me more about that" |
| **"What happened next?"** | After they describe an event | "So the client sent the questionnaire — what happened next?" |
| **"Can you give me a specific example?"** | Vague or general statements | "You said security is important — can you give me a specific example of when it mattered?" |
| **"Why?" (gentle, 2-3 times)** | To find root causes | "Why did your team decide not to invest in security tools?" → "Why was that?" |
| **"How much time/money?"** | Any workaround or process | "How much time does your team spend responding to questionnaires?" |
| **"What did you try?"** | After they describe a problem | "What have you tried to solve that?" |
| **Silence (wait 5-10 seconds)** | After they finish a thought | Say nothing. They will often continue with deeper insights |
| **Reflect back** | To confirm understanding | "So if I understand correctly, the main challenge is [X]?" |

**The Mom Test rules (memorize these):**
1. Ask about **their life**, not your idea
2. Ask about **the past**, not hypothetical futures ("Would you use..." is forbidden)
3. **Talk less, listen more** (80/20 split minimum)
4. **Never pitch** during the interview
5. Look for **strong emotions** — frustration, anger, resignation = real pain
6. **Compliments are noise** — "That sounds great!" means nothing; follow-up actions mean everything

### 4.3 Pain Point Exploration Guide

Use this to map interview moments to the 7 known pain points. When you hear signals matching a pain point, probe deeper using the suggested follow-ups.

| Pain Point | Interview Question That Surfaces It | Signal (What They Might Say) | Follow-Up Probe | Strong Pain (Record This) | Weak Pain (Note But Don't Overweight) |
|-----------|--------------------------------------|------------------------------|-----------------|--------------------------|--------------------------------------|
| **PP1: "Don't know what we don't know"** | Q3 (code review) | "We don't really do security review" / "Our developers are careful" | "Have you ever been surprised by a vulnerability you didn't know about?" | "We had a client discover an SQL injection we missed for 2 years" | "We're pretty confident in our code quality" |
| **PP2: Client demands blocking deals** | Q1, Q2, Q4 | "Our Japanese client sent a 50-page questionnaire" | "How long did it take? Did you have the answers?" | "We lost a $200K contract because we couldn't demonstrate ISO 27001" | "We handled it, it just took some time" |
| **PP3: Regulatory opacity** | Q5 (PDPL) | "We know about PDPL but don't know what to do" | "What specific requirements are you unsure about?" | "We have no idea what technical controls PDPL requires and our lawyer can't help" | "Our lawyer is handling compliance" |
| **PP4: Security as cost** | Q6 (magic wand), budget question | "We'd love to do more security but can't justify the cost" | "What would make the cost justifiable?" | "Our CEO sees security as overhead, not investment — until we lose a client" | "We have other priorities right now" |
| **PP5: Pen tests expensive/stale** | Q3, competitor section | "We did a pen test last year, cost $5K, report was outdated in a month" | "Would you want continuous scanning instead of one-time tests?" | "We pay $5K every year for a report nobody reads after week 2" | "We've never done a pen test" |
| **PP6: No internal champion** | Q2, Q3 | "Nobody on the team really knows security" | "Who handles security decisions when they come up?" | "Our lead developer handles security but has no training — he just Googles things" | "Our CTO has some security background" |
| **PP7: Reputation fear** | End of interview (organic) | References to CIC breach, Vietnam Airlines, or fear of public exposure | "How would a breach affect your business?" | "In Vietnam's market, one breach and your reputation is destroyed — clients talk" | "Breaches happen to big companies, not us" |

### 4.4 Reading Responses — Interest vs. Politeness

**Genuine interest (continue pursuing):**
- Leaning forward, asking follow-up questions
- Taking notes or screenshots
- "You should talk to my colleague [Name], he handles our security" (introduction offer)
- "Let's meet again after I discuss with my team" (suggesting next meeting)
- Adding you on Zalo after the meeting
- Asking about pricing specifics
- Sending follow-up messages unprompted

**Polite but not interested (do not pursue):**
- Sitting back, nodding without questions
- Checking phone frequently
- Short, general answers without specifics
- "It sounds interesting" with no follow-up questions
- No suggestion for a next step

**Response decoder:**

| What They Say | What It Likely Means | Your Response |
|---|---|---|
| "That's very interesting, let me think about it" | Polite no | Thank them. Move on if no follow-up in 2 weeks |
| "I'll discuss with my team and get back to you" | Probably no unless they set a specific date | Ask: "When would be a good time for me to follow up?" Vague answer = no |
| "We're very busy right now, maybe later" | No, with face-saving excuse | Follow up once in 1-2 months. Same response = move on |
| "Can you send me more information?" | Low interest, wants to end meeting politely | Send info, don't expect a response |
| "This is exactly what we need!" | Genuine interest | Follow up within 48 hours with a concrete next step |
| "How much does it cost?" | Genuine interest (price question = purchase consideration) | Give a range. Watch their reaction to the number |
| "We might have budget for this next quarter" | Moderate interest with real timeline | Mark calendar, follow up at start of that quarter |
| "Let me introduce you to [colleague]" | Strong interest | Prepare thoroughly for the introduction |
| "I know someone who might need this" | Genuine referral OR polite deflection | Accept and thank. If no intro materializes in a week, it was deflection |

**The Vietnamese smile:** Smiling does NOT mean agreement. Vietnamese people smile when embarrassed, uncomfortable, nervous, or simply being polite. Look for **actions** (follow-up messages, introductions, price questions), not **expressions**.

**How disagreement is expressed without saying "no":**
1. **Silence** after your statement — they disagree. Don't rush to fill it
2. **Subject change** — uncomfortable with what you proposed
3. **Vague timelines** — "we'll look into it sometime" = not interested
4. **Deferring to absent authority** — "I need to check with someone not here" = likely no
5. **Becoming MORE polite and formal** — they are pulling back. Real comfort looks casual
6. **"Send me materials for review"** — ending the meeting without commitment

### 4.5 Note-Taking Template

Copy this template for each interview. Fill in during or immediately after.

```
═══════════════════════════════════════════════════════════
INTERVIEW #___                          Date: ___________

INTERVIEWEE
Name: _________________  Company: _____________________
Role: _________________  Company Size: ____ developers
Sector: _______________  Clients: Domestic / International / Both
How recruited: ________  International client countries: ___________

COMPANY CONTEXT
Tech stack: ____________________________________________
Products/services: _____________________________________
Revenue range (if shared): _____________________________
Current security tools/processes: _______________________
Current security spending (annual): ____________________

PAIN POINT OBSERVATIONS
Rate each 0-3: (0=not mentioned, 1=mentioned casually,
2=described with frustration, 3=described with urgency + workaround attempted)

[ ] PP1: "Don't know what we don't know"         Rating: ___
[ ] PP2: Client demands blocking deals            Rating: ___
[ ] PP3: Regulatory compliance opacity            Rating: ___
[ ] PP4: Security seen as cost, not value         Rating: ___
[ ] PP5: Pen tests expensive/stale                Rating: ___
[ ] PP6: No internal security champion            Rating: ___
[ ] PP7: Fear of reputation damage                Rating: ___
[ ] Other: ___________________________            Rating: ___

Security ranked in top-3 problems? (unprompted): YES / NO

BUYING SIGNALS
[ ] Asked about pricing
[ ] Suggested next meeting
[ ] Offered to introduce colleague
[ ] Added me on Zalo
[ ] Sent follow-up message after meeting
[ ] Named a specific budget number: $____________

COMPETITOR AWARENESS
[ ] Knows CyStack:  YES / NO    Opinion: __________________
[ ] Uses free tools: YES / NO   Which: ____________________
[ ] Has done pen test: YES / NO  Cost: $___  Satisfaction: ___

INTEREST LEVEL (behavioral, not gut feeling)
1 = Polite but clearly not interested (no actions)
2 = Mild interest (acknowledged problem but no actions)
3 = Moderate interest (asked questions, engaged, but no concrete next step)
4 = Strong interest (suggested next meeting, asked about pricing, or offered intro)
5 = Very strong (wants to continue conversation, named budget, referral offered)

Rating: ___

REFERRALS
Offered referral: YES / NO
Name/company: _________________________________________
Contact info: _________________________________________

VERBATIM QUOTES (the most important section — capture exact words)
1. ____________________________________________________
2. ____________________________________________________
3. ____________________________________________________
4. ____________________________________________________
5. ____________________________________________________

POST-MEETING REFLECTION (fill within 2 hours)
What surprised me: ____________________________________
What I learned: _______________________________________
What I'd do differently: ______________________________
Follow-up actions: _____________________________________
Thank-you sent: [ ] Yes, via: _________________________
═══════════════════════════════════════════════════════════
```

---

## Part 5: Analysis Framework

### 5.1 After-Interview Processing Checklist

Complete within 24 hours of each interview:

- [ ] Transfer raw notes to clean template (if handwritten during meeting)
- [ ] Highlight and capture verbatim quotes
- [ ] Rate each of 7 pain points (0-3 scale)
- [ ] Record whether security was mentioned as a top-3 problem unprompted
- [ ] Classify interest level (1-5 behavioral scale)
- [ ] Update the pain point tally tracker (Section 5.2)
- [ ] Update the contact tracker (Appendix 7.5)
- [ ] Send thank-you Zalo message (within 4 hours of meeting)
- [ ] If referral was offered: send follow-up message to the referred contact within 48 hours
- [ ] Write 3-sentence post-interview reflection

### 5.2 Pain Point Tally Tracker

Update this table after each interview. At the end, totals reveal which pain points are real vs. assumed.

| Pain Point | I1 | I2 | I3 | I4 | I5 | I6 | I7 | I8 | I9 | I10 | I11 | I12 | I13 | I14 | I15 | Total (0-3 avg) | % Mentioned |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PP1: Don't know what we don't know | | | | | | | | | | | | | | | | | |
| PP2: Client demands blocking deals | | | | | | | | | | | | | | | | | |
| PP3: Regulatory opacity | | | | | | | | | | | | | | | | | |
| PP4: Security as cost | | | | | | | | | | | | | | | | | |
| PP5: Pen tests expensive/stale | | | | | | | | | | | | | | | | | |
| PP6: No internal champion | | | | | | | | | | | | | | | | | |
| PP7: Reputation fear | | | | | | | | | | | | | | | | | |
| **Top-3 unprompted** | | | | | | | | | | | | | | | | **Total:** | **%:** |
| **Budget signal** | | | | | | | | | | | | | | | | **Total:** | **%:** |
| **Referral offered** | | | | | | | | | | | | | | | | **Total:** | **%:** |
| **CyStack aware** | | | | | | | | | | | | | | | | **Total:** | **%:** |
| **Interest level (1-5)** | | | | | | | | | | | | | | | | **Average:** | |

**Segment breakdown (fill as you go):**
- Outsourcing firms interviewed: ___ / 15  |  Avg pain: ___ | Avg interest: ___
- Fintech firms interviewed: ___ / 15  |  Avg pain: ___ | Avg interest: ___
- Domestic SaaS interviewed: ___ / 15  |  Avg pain: ___ | Avg interest: ___
- Other: ___ / 15  |  Avg pain: ___ | Avg interest: ___

### 5.3 Persona Synthesis Template

After 8+ interviews, begin drafting 2-3 personas. Update as more data comes in. Use actual interview data, not assumptions.

```
PERSONA: [Archetype Name — e.g., "Minh the Outsourcing CTO"]
═══════════════════════════════════════════════════════════

Demographics:
  Role: _______________
  Company size: _______ developers
  Sector: _____________
  International clients: YES / NO (countries: _________)
  Age range: __________

Primary Job-to-be-Done:
  "When [trigger event], I need to [outcome] so that [business result]"
  Example: "When a Japanese client sends a security questionnaire,
  I need to respond credibly within 1 week so that we don't lose
  the $150K annual contract."

Top 3 Pain Points (from interview data):
  1. _________________ (cited by ___/15 interviewees)
  2. _________________ (cited by ___/15 interviewees)
  3. _________________ (cited by ___/15 interviewees)

Current Workarounds:
  What they do today: ________________________________
  What it costs them: $_______ / year + ______ hours / month
  Why it's insufficient: _____________________________

Budget Reality:
  Current security spending: $_______ / year
  Stated willingness to pay: $_______ / month
  Who controls the budget: __________________________

Buying Trigger:
  What activates the purchase decision: ______________
  How often this trigger occurs: _____________________

Trust Requirements:
  What they need before buying: _____________________
  (e.g., local references, free trial, Vietnamese support)

Unexpected Insight:
  Something that surprised you: _____________________
  Why it matters for the product: ___________________

Supporting Quotes (verbatim from interviews):
  1. "________________________________________________"
  2. "________________________________________________"
  3. "________________________________________________"
```

### 5.4 Pattern Recognition Guide

At weeks 5 and 10, review all interviews for patterns:

**Convergence signals (strong validation):**
- 3+ interviewees describe the same problem in their own words (without prompting)
- Multiple interviewees independently name the same workaround or competitor
- Pain intensity scores cluster around the same 2-3 pain points

**Divergence signals (possible segment split):**
- Outsourcing firms describe different pain than domestic SaaS firms
- Fintech firms have regulatory-driven pain that others don't share
- Firms with <30 devs behave differently than firms with 50-150 devs

**Intensity markers (distinguish "nice to have" from "must have"):**
- **Strong pain:** Emotional language, specific dollar amounts, incident stories, "we're worried about this"
- **Moderate pain:** Acknowledged as important but no concrete stories, "we should probably do something"
- **Weak pain:** Only surfaces when directly asked, generic responses, "it's on our roadmap"

**Bias checklist (review at mid-point):**
- [ ] Am I remembering positive signals more than negative ones? (confirmation bias)
- [ ] Did I accidentally pitch during any interview? Review notes
- [ ] Am I only interviewing people who are already interested? (selection bias)
- [ ] Am I overweighting the most recent interview? (recency bias)
- [ ] Have I interviewed enough domestic-only firms to compare? (comparison bias)

### 5.5 Weekly Analysis Routine

**Every Sunday evening (30 minutes):**
1. Update tally tracker with this week's interview data
2. Re-read all verbatim quotes from the week
3. Write a 3-sentence summary:
   - "This week I learned..."
   - "This surprised me..."
   - "Next week I need to explore..."
4. Check progress: Am I on track for 15 interviews by week 10?
5. Adjust outreach targets if behind schedule

**Week 5 mid-point review (1 hour):**
- Review all tally data so far
- Are any assumptions already clearly validated or invalidated?
- Is the outsourcing segment showing stronger pain than others?
- Do I need to adjust my interview script based on what I've learned?
- Am I reaching the right mix of segments?

**Week 10 final analysis (2-3 hours):**
- Complete all trackers
- Synthesize 2-3 personas
- Score go/no-go gate (Part 6)
- Draft initial value proposition
- Write Phase 1 summary report

---

## Part 6: Decision Gate

### 6.1 Scoring Matrix

After 15+ interviews, score each dimension:

| Dimension | Weight | Score (1-5) | Weighted | What 5 Looks Like | What 1 Looks Like |
|-----------|--------|-------------|----------|--------------------|--------------------|
| **Problem urgency** | 25% | ___ | ___ | 10+ describe security as top-3; 5+ specific incident stories with dollar amounts | <5 rank it top-3; no concrete incident stories |
| **Willingness to pay** | 25% | ___ | ___ | 5+ name price ranges overlapping $60-120/mo; 3+ have current spending | Universal "we would not pay"; budget caps at <$20/mo |
| **Market size signal** | 15% | ___ | ___ | Interviewees easily name 5+ peers with same problem; referrals flow naturally | "I don't know anyone else who cares about this" |
| **Demand signal** | 15% | ___ | ___ | 3+ referrals offered; follow-up messages received; "can you do this for us?" | Zero follow-up; polite smiles only |
| **Competitive differentiation** | 20% | ___ | ___ | CyStack known but 3+ describe gaps; free tools tried and abandoned | All satisfied with CyStack or free tools |
| **TOTAL** | 100% | | **___** | | |

**Decision thresholds:**

| Total Score | Decision | Next Step |
|-------------|----------|-----------|
| **4.0-5.0** | **GO** — proceed to Phase 2 (JTBD Mapping) | Begin JTBD analysis using interview data |
| **3.0-3.9** | **CONDITIONAL GO** — promising but gaps exist | Run 5 more interviews targeting weak areas |
| **2.0-2.9** | **PIVOT** — pain exists but hypothesis needs adjustment | Identify which segment or problem showed strongest signal; redesign hypothesis |
| **<2.0** | **KILL** — insufficient market signal | Stop. Do not proceed to Phase 2. Save your money and time |

**Hard gate (overrides score):** If CyStack covers all identified needs with no gaps, score 1 on competitive differentiation regardless of other scores. This alone drops total below 3.0.

### 6.2 Evidence Package

Before making a go/no-go decision, ensure you have:

- [ ] 15+ completed interview templates with verbatim quotes
- [ ] 5+ specific lost-deal or delayed-deal stories (with approximate dollar amounts)
- [ ] 5+ current workaround descriptions with estimated time/money costs
- [ ] 3+ unprompted mentions of regulatory pressure (PDPL, client audits)
- [ ] Budget ranges from 5+ interviewees
- [ ] CyStack awareness data from all interviewees
- [ ] 2-3 draft personas based on real data
- [ ] Completed pain point tally tracker
- [ ] Segment comparison (outsourcing vs. fintech vs. domestic pain levels)

### 6.3 Pivot Signals

If the primary hypothesis fails, check for alternative paths:

| Signal | Possible Pivot |
|--------|---------------|
| Pain is real but centered on compliance documentation, not scanning | Pivot to compliance-as-a-service (help firms respond to questionnaires, achieve ISO 27001) |
| Fintech segment shows 2x stronger pain than outsourcing | Pivot beachhead to fintech; adjust pricing for higher budgets |
| Budget is $0 — firms won't pay for scanning | Pivot to freemium with premium consulting upsell |
| CyStack satisfies all scanning needs | Pivot to complementary: training, compliance mapping, or specific niche CyStack doesn't cover (e.g., PDPL mapping) |
| Pain exists but only at firms >100 devs | Pivot target segment upmarket |

### 6.4 Value Proposition Draft Template

**Fill this in ONLY AFTER completing all interviews.** Using actual interview data.

```
VALUE PROPOSITION — DRAFT (to be validated in Phase 2-4)

WHO:    [Persona name] at [segment] firms with [size] developers

WHY:    When [trigger event from interviews], they need to
        [job-to-be-done from interviews] so that [business outcome]

BEFORE: Currently they [workaround from interviews], which costs
        [time/money from interviews] and results in [negative outcome]

HOW:    Our product [specific mechanism — keep vague until Phase 4]

AFTER:  They can now [positive outcome] in [timeframe],
        enabling [business result]

ALTERNATIVES:
        - [Alternative 1 from interviews] but [limitation they described]
        - [Alternative 2 from interviews] but [limitation they described]
        - [CyStack] but [gap they described, if any]

ONE-SENTENCE VERSION:
"We help [WHO] [achieve OUTCOME] when [TRIGGER], without [current pain]."
```

---

## Part 7: Appendices

### 7.1 Gift Etiquette Reference Card

| Category | Do | Don't |
|----------|----|-------|
| **Items** | Vietnamese tea/coffee, imported chocolate, fruit baskets, item from your home country | Clocks/watches (death symbol), sharp objects (cutting relationship), handkerchiefs (grief), sets of 4 (death number) |
| **Colors** | Red (luck), yellow (wealth) | White (funerals), black (death) |
| **When** | After a productive meeting (not the first), Tet, first office visit | First meeting (too transactional) |
| **How** | Present with both hands. "A small gift to thank you for your time." | Don't expect them to open it in front of you |
| **Budget** | 200K-500K VND ($8-20) | Too expensive feels like a bribe; too cheap feels careless |

### 7.2 Budget Tracker

| Item | Budgeted | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 | W10 | Total |
|------|----------|----|----|----|----|----|----|----|----|----|----|-------|
| Coffee meetings | $60-160 | | | | | | | | | | | |
| Grab rides | $45-140 | | | | | | | | | | | |
| Business cards | $6-20 | | | | | | | | | | | |
| Gifts | $0-40 | | | | | | | | | | | |
| Phone/Zalo credit | $5-10 | | | | | | | | | | | |
| Miscellaneous | $10-30 | | | | | | | | | | | |
| **Weekly total** | | | | | | | | | | | | **$111-320** |

### 7.3 Contact/CRM Tracker

Maintain this in Google Sheets or Notion for sorting and filtering.

| Name | Company | Role | Size | Sector | Dom/Intl | Source | 1st Contact | Meeting Date | Interest (1-5) | Top Pain Points | Follow-up Status | Referrals | Notes |
|------|---------|------|------|--------|----------|--------|-------------|-------------|----------------|-----------------|-----------------|-----------|-------|
| | | | | | | | | | | | | | |

### 7.4 Competitor Quick-Reference

Use during interviews when competitors come up. Do NOT bring these up proactively.

| Competitor | What They Offer | Gap / Differentiator | Your Response If Asked |
|-----------|----------------|---------------------|----------------------|
| **CyStack** | CREST-certified automated vulnerability scanning for Vietnamese SMEs, platform in Vietnamese | ? (validate in interviews — this is your biggest competitive question) | "I've heard of them — what's been your experience?" |
| **VSEC** | Penetration testing, SOC services, enterprise-focused | Expensive for SMEs, project-based not continuous | "How was the experience? Would you want something more continuous?" |
| **Viettel Cyber Security** | Full-stack SOC, threat intelligence, enterprise CII protection | Enterprise-only, overkill for SMEs | "Interesting — would their services fit your scale?" |
| **Free tools (ZAP, Semgrep, Trivy)** | Free scanning, requires in-house expertise | Expertise gap, no remediation guidance, no compliance mapping | "What happened when you tried them? What stopped you from continuing?" |

### 7.5 Zalo Follow-Up Messages

**Thank you (send within 4 hours of meeting):**
> Cam on anh [Name] da danh thoi gian gap em hom nay. Em hoc duoc rat nhieu tu kinh nghiem cua anh. Chuc anh cuoi tuan vui!
>
> (Thank you [Name] for taking the time to meet today. I learned a lot from your experience. Have a great weekend!)

**Scheduling follow-up (if meeting promised but no date set):**
> Chao anh [Name], hy vong anh khoe. Em muon hoi lai ve buoi gap ma minh da noi. Anh ranh khi nao tuan toi a?
>
> (Hello [Name], hope you're well. I wanted to follow up on the meeting we discussed. When are you free next week?)

**Sharing relevant content (relationship maintenance):**
> Anh [Name] oi, em vua doc bai nay ve [topic] — em nghi anh se thich. [link]
>
> (Hey [Name], I just read this article about [topic] — thought you might find it interesting. [link])

**Gentle check-in after 2+ weeks of silence:**
> Chao anh [Name], hy vong moi viec on. Chi muon hoi tham anh thoi a. Neu anh ranh thi minh hen ca phe nhe!
>
> (Hi [Name], hope everything's going well. Just checking in. If you're free, let's grab coffee!)

### 7.6 Vietnamese Pronunciation Quick-Guide

| Word | Pronunciation | Meaning | When to Use |
|------|-------------|---------|-------------|
| Anh | "Ahn" | Older brother / Mr. | Addressing men (same age or older) |
| Chi | "Chee" | Older sister / Ms. | Addressing women (same age or older) |
| Em | "Em" | Younger sibling / I (humble) | Referring to yourself when speaking to Anh/Chi |
| Ca phe sua da | "Cah feh sua dah" | Iced milk coffee | Ordering at a cafe |
| Cam on | "Kahm uhn" | Thank you | After meetings, receiving gifts |
| Xin chao | "Sin chow" | Hello (formal) | Greeting in business settings |
| Mot, hai, ba, yo! | "Moht, hi, bah, yo!" | 1, 2, 3, cheers! | Toasting during meals |
| Toi khong uong duoc nhieu | "Toy kohng oong dwock nyew" | I can't drink much | Declining heavy drinking politely |

---

## Checklist: Before You Start Week 1

- [ ] Zalo installed and account created
- [ ] Joined CTO Vietnam Network (Facebook Group)
- [ ] Joined 2-3 Vietnamese tech Zalo groups
- [ ] Business cards ordered (English + Vietnamese)
- [ ] Interview script printed (Part 4.1)
- [ ] Note-taking templates printed (Part 4.5, 20 copies)
- [ ] Pain point tally tracker set up (Part 5.2, Google Sheets recommended)
- [ ] Contact/CRM tracker set up (Part 7.3, Google Sheets recommended)
- [ ] Budget tracker set up (Part 7.2)
- [ ] Outreach messages drafted and reviewed by Vietnamese friend
- [ ] Free security mini-assessment process prepared (basic ZAP scan + dependency check)
- [ ] Vietnamese pronunciation practiced (Part 7.6)
- [ ] Gift inventory: 2-3 boxes of imported chocolate, quality tea
- [ ] Read Parts 3.4 and 4.4 one more time (etiquette and response reading)

**You are ready. Go learn. Do not sell.**
