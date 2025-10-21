# Platform Launch Analyzer 🚀

A comprehensive assessment tool for evaluating platform business ideas based on the Azoulay & Tucker framework. This tool helps entrepreneurs avoid "platform envy" by providing data-driven analysis of whether a platform strategy makes sense for their specific business idea.

## Overview

The Platform Launch Analyzer evaluates platform ideas across 6 critical dimensions to determine viability and provide strategic recommendations. It's designed to catch red flags early and guide strategic decision-making before significant resources are committed.

## Key Features

- **Quick Check (5-minute assessment)** - Rapid evaluation to identify critical red flags
- **Comprehensive Assessment** - Full evaluation across 6 key dimensions with detailed scoring
- **Smart Scoring System** - Numerical scores with specific feedback and recommendations
- **Multiple Usage Modes** - Interactive, batch processing, and JSON output
- **Decision Framework** - Clear go/no-go thresholds based on assessment scores

## Installation

```bash
# Clone the repository
git clone https://github.com/identity-wael/platform-launch-analyzer.git
cd platform-launch-analyzer

# No dependencies required - uses Python standard library only
# Requires Python 3.6+
```

## Quick Start

### 1. Quick Check (5 minutes)
```bash
python3 scripts/quick_check.py
```
Answer 10 yes/no questions for immediate feedback on platform viability.

### 2. Full Interactive Assessment
```bash
python3 scripts/platform_assessment.py --interactive
```
Complete guided assessment with detailed scoring and recommendations.

### 3. Batch Assessment with JSON
```bash
python3 scripts/platform_assessment.py --input assets/example_airbnb.json
```
Process pre-filled assessments for multiple platform ideas.

## Assessment Framework

The analyzer evaluates platforms across 6 dimensions:

### 1. Core Definition (Coring)
- Clear identification of platform sides
- Well-defined value unit
- Designed core interaction
- Governance structure
- Control mechanisms

### 2. Network Effects Potential
- Same-side network effects strength
- Cross-side network effects strength
- Stand-alone value proposition

### 3. Seeding Strategy
- Marquee user attraction
- Subsidization approach
- Chicken-egg problem solution
- Single-side launch capability

### 4. Competitive Dynamics (Tipping)
- Multi-homing costs
- Differentiation from competitors
- User switching costs
- Winner-take-all potential

### 5. Value Creation
- Search cost reduction
- Transaction cost reduction
- Trust and safety mechanisms

### 6. Pricing Strategy
- Revenue model clarity
- Pricing side identification
- Pricing structure selection
- Long-term sustainability

## Scoring Interpretation

- **Green Light (>75%)**: Strong viability - proceed with confidence
- **Yellow Light (60-74%)**: Moderate viability - address weaknesses first
- **Red Light (<60%)**: Weak viability - reconsider platform approach

## Example Output

```
OVERALL VIABILITY SCORE: 515/600 (85.8%)
[██████████████████████████████████████████░░░░░░░░] 85.8%

CATEGORY ASSESSMENTS
----------------------------------------------------------------------
Core Definition (Coring): 100/100 (100.0%)
  ✓ Clear identification of platform sides
  ✓ Value unit well-defined
  ...

KEY STRENGTHS
----------------------------------------------------------------------
• Strong cross-side network effects
• Solid chicken-egg problem solution
...

STRATEGIC RECOMMENDATIONS
----------------------------------------------------------------------
1. STRONG VIABILITY: Platform shows excellent potential
2. Proceed with detailed business plan development
...
```

## File Structure

```
platform-launch-analyzer/
├── scripts/
│   ├── platform_assessment.py    # Main assessment engine
│   └── quick_check.py            # Rapid assessment tool
├── assets/
│   ├── assessment_template.json  # Template for batch processing
│   └── example_airbnb.json      # Example assessment (AirBnB)
├── references/
│   ├── coring_checklist.md      # Platform core design guide
│   ├── seeding_strategies.md    # Tactical launch playbook
│   └── competitive_dynamics.md  # Competition analysis framework
└── SKILL.md                      # Detailed documentation
```

## Usage Examples

### Interactive Assessment
Perfect for evaluating a single platform idea with guided questions:
```bash
python3 scripts/platform_assessment.py --interactive
```

### JSON Batch Processing
Ideal for comparing multiple platform ideas:
```bash
# Create your assessment file based on template
cp assets/assessment_template.json my_platform.json
# Edit my_platform.json with your answers
python3 scripts/platform_assessment.py --input my_platform.json
```

### Generate JSON Report
For data analysis and tracking:
```bash
python3 scripts/platform_assessment.py --input data.json --format json --output report.json
```

## Reference Materials

The `references/` directory contains strategic guides:

- **Coring Checklist**: Essential questions for platform core design
- **Seeding Strategies**: Proven tactics for platform launch
- **Competitive Dynamics**: Framework for analyzing competition and tipping potential

## Real-World Example

The repository includes a real assessment of AirBnB's early-stage platform (circa 2008), demonstrating how a successful platform scores across all dimensions. Run it with:

```bash
python3 scripts/platform_assessment.py --input assets/example_airbnb.json
```

AirBnB scores 85.8% overall, with perfect scores in Core Definition, Value Creation, and Pricing Strategy.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Based On

This tool implements concepts from:
- Azoulay, P., & Tucker, C. (2023). "Platform Strategy" framework
- Research on platform economics and network effects
- Case studies of successful and failed platform launches

## License

MIT License - See LICENSE file for details

## Support

For questions or issues, please open an issue on GitHub: https://github.com/identity-wael/platform-launch-analyzer/issues

---

**Remember**: Not every business needs to be a platform. This tool helps you make that decision with confidence.