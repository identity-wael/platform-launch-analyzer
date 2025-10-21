# Platform Coring Checklist

Based on Azoulay & Tucker's Platform Strategy Framework

## The Five Essential Coring Questions

### 1. What sides should be brought on board?

**Key Decisions:**
- Number of sides at launch (typically 2, max 3)
- Clear definition of each side's role
- Future sides to add post-launch

**Red Flags:**
- Starting with 3+ sides (too complex)
- Vague side definitions ("users")
- Assuming sides will naturally appear

**Examples:**
- ✓ AirBnB: Hosts and Guests (clear 2-sided)
- ✗ Failed platform: "Connect everyone" (unclear)

### 2. What is the unit of value?

**Definition:** The atomic unit of exchange on your platform

**Common Units:**
- Listing (AirBnB, eBay)
- Profile (LinkedIn, dating apps)
- Project (Kickstarter, Upwork)
- Transaction (Uber, payment platforms)
- Post/Content (social media)

**Validation Questions:**
- Can you price based on this unit?
- Does it define the interaction boundary?
- Is it neither too narrow nor too broad?

### 3. What is the pricing architecture?

**Core Decisions:**
- Who pays? (which side)
- How much? (pricing level)
- When? (timing/frequency)
- How? (mechanism)

**Common Models:**

| Model | Best For | Risks |
|-------|----------|-------|
| Rake (%) | Transactions | Disintermediation |
| Subscription | Recurring use | High initial barrier |
| Freemium | Consumer platforms | Conversion challenges |
| Access fee | Professional platforms | Chicken-egg intensifies |
| Ads | High traffic | User experience degradation |

**Side Selection Principles:**
- Charge the less price-elastic side
- Charge the side extracting more value
- Charge the side that's easier to acquire

### 4. How will the platform be governed?

**Access Rules:**
- Open vs. Curated
- Verification requirements
- Quality standards
- Geographic restrictions

**Behavioral Rules:**
- Prohibited actions
- Communication restrictions
- Transaction guidelines
- Dispute resolution

**Information Rules:**
- Rating systems (one-sided vs. 360)
- Transparency requirements
- Privacy policies
- Data ownership

**Trust & Safety Mechanisms:**

1. **Reputation Systems Design:**
   - Mandatory vs. Optional rating
   - Anonymous vs. Attributed
   - Granularity (binary vs. 5-star)
   - Review verification

2. **Dispute Resolution:**
   - Automated vs. Manual
   - Escalation paths
   - Money-back guarantees
   - Insurance/protection programs

3. **Quality Control:**
   - Pre-screening
   - Ongoing monitoring
   - Probation periods
   - Removal criteria

### 5. How to maintain control?

**Control Mechanisms:**

**Technical Control:**
- Proprietary algorithms
- Unique data assets
- API restrictions
- Integration depth

**Legal Control:**
- Terms of service
- Intellectual property
- Exclusive agreements
- Regulatory compliance

**Economic Control:**
- Switching costs
- Data portability barriers
- Network effect strength
- Subsidy dependencies

**Strategic Control:**
- Brand strength
- Marquee user lock-in
- Ecosystem orchestration
- Market timing

## Platform Core Coherence Test

All elements must work together as a coherent system:

```
Sides Definition
    ↓
Value Unit (defines interaction)
    ↓
Governance Rules (shape behavior)
    ↓
Pricing Architecture (captures value)
    ↓
Control Mechanisms (maintains position)
```

**Coherence Examples:**

**eHarmony (Coherent):**
- Sides: Marriage-minded singles
- Value unit: Detailed profile
- Governance: Strict screening, guided communication
- Pricing: High subscription (filters casual users)
- Control: Proprietary matching algorithm
→ All elements reinforce "serious dating" positioning

**Failed Dating App (Incoherent):**
- Sides: "Everyone looking for connection"
- Value unit: Simple swipe
- Governance: No verification
- Pricing: Ads + premium features
- Control: None
→ Mixed signals, no clear value proposition

## The Stickiness Test

Once launched, changing core elements is extremely difficult:

**Can Change (Peripheral):**
- Feature additions
- UI improvements
- Geographic expansion
- Promotional tactics

**Cannot Change (Core):**
- Number of sides
- Value unit definition
- Basic governance philosophy
- Fundamental pricing model

**Historical Examples:**
- Uber adding tipping: User backlash (core violation)
- Twitter limiting API: Killed developer ecosystem
- Facebook adding marketplace: Success (peripheral addition)

## Pre-Launch Core Validation

Before launching, validate your core through:

1. **Paper Prototype Testing:**
   - Mock the interaction without technology
   - Test with 10-20 potential users per side
   - Identify friction points

2. **"Wizard of Oz" Testing:**
   - Manually facilitate interactions
   - Measure actual willingness to pay
   - Test governance rules in practice

3. **Coherence Stress Test:**
   - Write 1-page description of platform
   - Have 5 people independently identify:
     - The sides
     - Value proposition
     - Why it's better than alternatives
   - If answers vary significantly = incoherent core

## Common Coring Failures

1. **The Kitchen Sink:** Including every possible feature/side
2. **The Pivot Trap:** Assuming core can be easily changed
3. **The Democracy Fallacy:** Letting users define governance
4. **The Free-for-All:** No governance ("the market will decide")
5. **The Extraction Machine:** Pricing both sides aggressively
6. **The Commodity Core:** No differentiation from competitors

## Coring Decision Framework

For each core decision, evaluate:

1. **Necessity:** Is this essential for launch?
2. **Differentiation:** Does this distinguish us?
3. **Scalability:** Does this work at 100x scale?
4. **Defensibility:** Can competitors easily copy?
5. **Coherence:** Does this align with other decisions?

Score each element 1-5. Elements scoring <15 total need rework.
