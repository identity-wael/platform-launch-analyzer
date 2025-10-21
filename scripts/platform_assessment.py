#!/usr/bin/env python3
"""
Platform Launch Analyzer - Core Assessment Engine
Based on Azoulay & Tucker's Platform Strategy Framework
"""

import json
import argparse
from datetime import datetime
from typing import Dict, List, Tuple
import sys


class PlatformAssessment:
    """Evaluates platform ideas against key success criteria"""
    
    def __init__(self):
        self.scores = {}
        self.recommendations = []
        self.risks = []
        self.strengths = []
        
    def assess_core_definition(self, answers: Dict) -> Dict:
        """Evaluate platform core definition quality"""
        score = 0
        max_score = 100
        feedback = []
        
        # Check if sides are clearly defined
        if answers.get('sides_defined', '').lower() == 'yes':
            score += 20
            feedback.append("✓ Clear identification of platform sides")
        else:
            feedback.append("✗ Platform sides need clearer definition")
            self.risks.append("Unclear platform sides - fundamental issue")
        
        # Check value unit clarity
        if answers.get('value_unit_clear', '').lower() == 'yes':
            score += 20
            feedback.append("✓ Value unit well-defined")
        else:
            feedback.append("✗ Value unit needs clarification")
            
        # Check interaction design
        if answers.get('interaction_designed', '').lower() == 'yes':
            score += 20
            feedback.append("✓ Core interaction properly designed")
        else:
            feedback.append("✗ Core interaction needs more work")
        
        # Check governance rules
        if answers.get('governance_defined', '').lower() == 'yes':
            score += 20
            feedback.append("✓ Governance rules established")
        else:
            feedback.append("✗ Governance structure needs development")
            
        # Check control mechanisms
        if answers.get('control_mechanism', '').lower() == 'yes':
            score += 20
            feedback.append("✓ Control mechanisms identified")
        else:
            feedback.append("✗ Need strategy for maintaining control")
            self.risks.append("Lack of platform control strategy")
        
        return {
            'score': score,
            'max_score': max_score,
            'feedback': feedback,
            'category': 'Core Definition (Coring)'
        }
    
    def assess_network_effects(self, answers: Dict) -> Dict:
        """Evaluate network effects potential"""
        score = 0
        max_score = 100
        feedback = []
        
        # Same-side network effects
        same_side_strength = answers.get('same_side_strength', 'none')
        if same_side_strength == 'strong':
            score += 30
            feedback.append("✓ Strong same-side network effects")
            self.strengths.append("Strong same-side network effects")
        elif same_side_strength == 'moderate':
            score += 15
            feedback.append("◐ Moderate same-side network effects")
        else:
            feedback.append("✗ Weak/no same-side network effects")
        
        # Cross-side network effects  
        cross_side_strength = answers.get('cross_side_strength', 'none')
        if cross_side_strength == 'strong':
            score += 40
            feedback.append("✓ Strong cross-side network effects")
            self.strengths.append("Strong cross-side network effects")
        elif cross_side_strength == 'moderate':
            score += 20
            feedback.append("◐ Moderate cross-side network effects")
        else:
            feedback.append("✗ Weak/no cross-side network effects")
            self.risks.append("Weak network effects may limit growth")
        
        # Stand-alone value
        if answers.get('standalone_value', '').lower() == 'yes':
            score += 30
            feedback.append("✓ Platform offers stand-alone value")
            self.strengths.append("Strong stand-alone value proposition")
        else:
            feedback.append("⚠ Limited stand-alone value - harder to seed")
            
        return {
            'score': score,
            'max_score': max_score,
            'feedback': feedback,
            'category': 'Network Effects Potential'
        }
    
    def assess_seeding_strategy(self, answers: Dict) -> Dict:
        """Evaluate platform seeding approach"""
        score = 0
        max_score = 100
        feedback = []
        
        # Marquee users strategy
        if answers.get('marquee_users', '').lower() == 'yes':
            score += 25
            feedback.append("✓ Marquee user strategy identified")
        
        # Subsidy strategy
        subsidy = answers.get('subsidy_strategy', 'none')
        if subsidy == 'strategic':
            score += 25
            feedback.append("✓ Strategic subsidization planned")
        elif subsidy == 'minimal':
            score += 15
            feedback.append("◐ Limited subsidization planned")
        else:
            feedback.append("⚠ No clear subsidization strategy")
        
        # Chicken-egg solution
        if answers.get('chicken_egg_solution', '').lower() == 'yes':
            score += 30
            feedback.append("✓ Clear solution to chicken-egg problem")
            self.strengths.append("Solid chicken-egg problem solution")
        else:
            feedback.append("✗ Chicken-egg problem not addressed")
            self.risks.append("No clear path to overcome chicken-egg problem")
        
        # Single-side focus option
        if answers.get('single_side_start', '').lower() == 'yes':
            score += 20
            feedback.append("✓ Can start with single-side focus")
        
        return {
            'score': score,
            'max_score': max_score,
            'feedback': feedback,
            'category': 'Seeding Strategy'
        }
    
    def assess_competitive_dynamics(self, answers: Dict) -> Dict:
        """Evaluate competitive positioning and tipping potential"""
        score = 0
        max_score = 100
        feedback = []
        
        # Multi-homing costs
        multi_homing = answers.get('multi_homing_costs', 'low')
        if multi_homing == 'high':
            score += 30
            feedback.append("✓ High multi-homing costs favor winner-take-all")
            self.strengths.append("High multi-homing costs create defensibility")
        elif multi_homing == 'moderate':
            score += 15
            feedback.append("◐ Moderate multi-homing costs")
        else:
            feedback.append("⚠ Low multi-homing costs enable competition")
            self.risks.append("Low barriers to multi-platform usage")
        
        # Differentiation
        if answers.get('differentiation', '').lower() == 'yes':
            score += 35
            feedback.append("✓ Clear differentiation from competitors")
        else:
            feedback.append("✗ Weak differentiation")
            self.risks.append("Insufficient differentiation from competitors")
        
        # Switching costs
        switching = answers.get('switching_costs', 'low')
        if switching == 'high':
            score += 35
            feedback.append("✓ High switching costs create lock-in")
        elif switching == 'moderate':
            score += 20
            feedback.append("◐ Moderate switching costs")
        else:
            feedback.append("⚠ Low switching costs increase churn risk")
        
        return {
            'score': score,
            'max_score': max_score,
            'feedback': feedback,
            'category': 'Competitive Dynamics (Tipping)'
        }
    
    def assess_value_creation(self, answers: Dict) -> Dict:
        """Evaluate value creation mechanisms"""
        score = 0
        max_score = 100
        feedback = []
        
        # Search cost reduction
        if answers.get('reduces_search_costs', '').lower() == 'yes':
            score += 35
            feedback.append("✓ Significantly reduces search costs")
            self.strengths.append("Strong search cost reduction")
        else:
            feedback.append("◐ Limited search cost reduction")
        
        # Transaction cost reduction
        if answers.get('reduces_transaction_costs', '').lower() == 'yes':
            score += 35
            feedback.append("✓ Significantly reduces transaction costs")
            self.strengths.append("Strong transaction cost reduction")
        else:
            feedback.append("◐ Limited transaction cost reduction")
        
        # Trust and safety
        if answers.get('trust_mechanisms', '').lower() == 'yes':
            score += 30
            feedback.append("✓ Strong trust and safety mechanisms")
        else:
            feedback.append("✗ Trust and safety needs attention")
            self.risks.append("Insufficient trust and safety mechanisms")
        
        return {
            'score': score,
            'max_score': max_score,
            'feedback': feedback,
            'category': 'Value Creation'
        }
    
    def assess_pricing_strategy(self, answers: Dict) -> Dict:
        """Evaluate pricing and monetization approach"""
        score = 0
        max_score = 100
        feedback = []
        
        # Revenue model clarity
        if answers.get('revenue_model_clear', '').lower() == 'yes':
            score += 30
            feedback.append("✓ Clear revenue model")
        else:
            feedback.append("✗ Revenue model needs clarification")
            self.risks.append("Unclear path to monetization")
        
        # Side to charge identified
        if answers.get('pricing_side_identified', '').lower() == 'yes':
            score += 25
            feedback.append("✓ Correct side identified for pricing")
        else:
            feedback.append("✗ Unclear which side to charge")
        
        # Pricing structure
        pricing_type = answers.get('pricing_structure', 'undefined')
        if pricing_type in ['rake', 'subscription', 'freemium']:
            score += 25
            feedback.append(f"✓ {pricing_type.capitalize()} model selected")
        else:
            feedback.append("✗ Pricing structure undefined")
        
        # Sustainability
        if answers.get('pricing_sustainable', '').lower() == 'yes':
            score += 20
            feedback.append("✓ Pricing model appears sustainable")
        else:
            feedback.append("⚠ Sustainability concerns with pricing")
        
        return {
            'score': score,
            'max_score': max_score,
            'feedback': feedback,
            'category': 'Pricing Strategy'
        }
    
    def generate_recommendations(self, all_scores: List[Dict]) -> List[str]:
        """Generate strategic recommendations based on assessment"""
        recommendations = []
        total_score = sum(s['score'] for s in all_scores)
        max_total = sum(s['max_score'] for s in all_scores)
        percentage = (total_score / max_total) * 100
        
        # Overall viability
        if percentage >= 75:
            recommendations.append("STRONG VIABILITY: Platform shows excellent potential across key dimensions")
        elif percentage >= 60:
            recommendations.append("MODERATE VIABILITY: Platform has promise but needs refinement in key areas")
        elif percentage >= 45:
            recommendations.append("QUESTIONABLE VIABILITY: Significant challenges need addressing")
        else:
            recommendations.append("WEAK VIABILITY: Fundamental issues suggest reconsidering platform approach")
        
        # Category-specific recommendations
        for score_dict in all_scores:
            cat_percentage = (score_dict['score'] / score_dict['max_score']) * 100
            category = score_dict['category']
            
            if cat_percentage < 50:
                if 'Core Definition' in category:
                    recommendations.append(f"PRIORITY: Strengthen {category} - this is foundational")
                elif 'Network Effects' in category:
                    recommendations.append(f"CRITICAL: Weak network effects threaten platform viability")
                elif 'Seeding' in category:
                    recommendations.append(f"IMPORTANT: Develop clearer seeding strategy to achieve launch")
                else:
                    recommendations.append(f"ADDRESS: Improve {category}")
        
        return recommendations
    
    def generate_report(self, answers: Dict, output_format: str = 'text') -> str:
        """Generate comprehensive assessment report"""
        
        # Run all assessments
        scores = []
        scores.append(self.assess_core_definition(answers))
        scores.append(self.assess_network_effects(answers))
        scores.append(self.assess_seeding_strategy(answers))
        scores.append(self.assess_competitive_dynamics(answers))
        scores.append(self.assess_value_creation(answers))
        scores.append(self.assess_pricing_strategy(answers))
        
        # Calculate totals
        total_score = sum(s['score'] for s in scores)
        max_total = sum(s['max_score'] for s in scores)
        overall_percentage = (total_score / max_total) * 100
        
        # Get recommendations
        recommendations = self.generate_recommendations(scores)
        
        if output_format == 'json':
            return json.dumps({
                'timestamp': datetime.now().isoformat(),
                'overall_score': f"{total_score}/{max_total}",
                'overall_percentage': round(overall_percentage, 1),
                'category_scores': scores,
                'strengths': self.strengths,
                'risks': self.risks,
                'recommendations': recommendations
            }, indent=2)
        
        # Generate text report
        report = []
        report.append("=" * 70)
        report.append("PLATFORM LAUNCH ASSESSMENT REPORT")
        report.append("=" * 70)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Overall Score
        report.append(f"OVERALL VIABILITY SCORE: {total_score}/{max_total} ({overall_percentage:.1f}%)")
        report.append("")
        
        # Score visualization
        bar_length = 50
        filled = int((overall_percentage / 100) * bar_length)
        bar = "█" * filled + "░" * (bar_length - filled)
        report.append(f"[{bar}] {overall_percentage:.1f}%")
        report.append("")
        
        # Category breakdowns
        report.append("CATEGORY ASSESSMENTS")
        report.append("-" * 70)
        for score_dict in scores:
            cat_percent = (score_dict['score'] / score_dict['max_score']) * 100
            report.append(f"\n{score_dict['category']}: {score_dict['score']}/{score_dict['max_score']} ({cat_percent:.1f}%)")
            for feedback in score_dict['feedback']:
                report.append(f"  {feedback}")
        
        # Strengths
        if self.strengths:
            report.append("\n" + "=" * 70)
            report.append("KEY STRENGTHS")
            report.append("-" * 70)
            for strength in self.strengths:
                report.append(f"• {strength}")
        
        # Risks
        if self.risks:
            report.append("\n" + "=" * 70)
            report.append("CRITICAL RISKS")
            report.append("-" * 70)
            for risk in self.risks:
                report.append(f"⚠ {risk}")
        
        # Recommendations
        report.append("\n" + "=" * 70)
        report.append("STRATEGIC RECOMMENDATIONS")
        report.append("-" * 70)
        for i, rec in enumerate(recommendations, 1):
            report.append(f"{i}. {rec}")
        
        # Next steps
        report.append("\n" + "=" * 70)
        report.append("SUGGESTED NEXT STEPS")
        report.append("-" * 70)
        
        if overall_percentage >= 75:
            report.append("1. Proceed with detailed business plan development")
            report.append("2. Begin prototype/MVP development")
            report.append("3. Identify and approach marquee users")
        elif overall_percentage >= 60:
            report.append("1. Address identified weaknesses before proceeding")
            report.append("2. Refine platform core and governance model")
            report.append("3. Strengthen network effects mechanisms")
        else:
            report.append("1. Reconsider platform approach vs. traditional business model")
            report.append("2. If proceeding, fundamental redesign recommended")
            report.append("3. Consider pivoting to address stronger pain points")
        
        report.append("\n" + "=" * 70)
        
        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description='Platform Launch Assessment Tool')
    parser.add_argument('--input', '-i', help='JSON file with assessment answers')
    parser.add_argument('--output', '-o', help='Output file for report')
    parser.add_argument('--format', '-f', choices=['text', 'json'], default='text',
                       help='Output format')
    parser.add_argument('--interactive', action='store_true',
                       help='Run interactive assessment')
    
    args = parser.parse_args()
    
    assessor = PlatformAssessment()
    
    if args.interactive:
        # Interactive mode - ask questions
        print("PLATFORM LAUNCH ANALYZER")
        print("=" * 50)
        print("Answer the following questions about your platform idea:")
        print()
        
        answers = {}
        
        # Core Definition Questions
        print("CORE DEFINITION (CORING)")
        print("-" * 30)
        answers['sides_defined'] = input("Have you clearly defined all sides of your platform? (yes/no): ")
        answers['value_unit_clear'] = input("Is the unit of value on your platform clearly defined? (yes/no): ")
        answers['interaction_designed'] = input("Have you designed the core interaction in detail? (yes/no): ")
        answers['governance_defined'] = input("Are governance rules and policies defined? (yes/no): ")
        answers['control_mechanism'] = input("Do you have a strategy to maintain control of the platform? (yes/no): ")
        
        # Network Effects Questions
        print("\nNETWORK EFFECTS")
        print("-" * 30)
        answers['same_side_strength'] = input("Strength of same-side network effects (strong/moderate/weak/none): ")
        answers['cross_side_strength'] = input("Strength of cross-side network effects (strong/moderate/weak/none): ")
        answers['standalone_value'] = input("Does the platform offer stand-alone value? (yes/no): ")
        
        # Seeding Questions
        print("\nSEEDING STRATEGY")
        print("-" * 30)
        answers['marquee_users'] = input("Do you have a strategy to attract marquee users? (yes/no): ")
        answers['subsidy_strategy'] = input("Subsidization strategy (strategic/minimal/none): ")
        answers['chicken_egg_solution'] = input("Do you have a clear solution to the chicken-egg problem? (yes/no): ")
        answers['single_side_start'] = input("Can you start with single-side focus? (yes/no): ")
        
        # Competitive Questions
        print("\nCOMPETITIVE DYNAMICS")
        print("-" * 30)
        answers['multi_homing_costs'] = input("Multi-homing costs for users (high/moderate/low): ")
        answers['differentiation'] = input("Clear differentiation from competitors? (yes/no): ")
        answers['switching_costs'] = input("Switching costs for users (high/moderate/low): ")
        
        # Value Creation Questions
        print("\nVALUE CREATION")
        print("-" * 30)
        answers['reduces_search_costs'] = input("Does platform significantly reduce search costs? (yes/no): ")
        answers['reduces_transaction_costs'] = input("Does platform significantly reduce transaction costs? (yes/no): ")
        answers['trust_mechanisms'] = input("Strong trust and safety mechanisms planned? (yes/no): ")
        
        # Pricing Questions
        print("\nPRICING STRATEGY")
        print("-" * 30)
        answers['revenue_model_clear'] = input("Is the revenue model clearly defined? (yes/no): ")
        answers['pricing_side_identified'] = input("Have you identified which side to charge? (yes/no): ")
        answers['pricing_structure'] = input("Pricing structure (rake/subscription/freemium/ads/undefined): ")
        answers['pricing_sustainable'] = input("Is the pricing model sustainable long-term? (yes/no): ")
        
    elif args.input:
        # Load answers from JSON file
        with open(args.input, 'r') as f:
            answers = json.load(f)
    else:
        print("Error: Provide either --input file or use --interactive mode")
        sys.exit(1)
    
    # Generate report
    report = assessor.generate_report(answers, args.format)
    
    # Output report
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to: {args.output}")
    else:
        print(report)


if __name__ == '__main__':
    main()
