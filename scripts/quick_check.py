#!/usr/bin/env python3
"""
Platform Quick Check - Rapid viability assessment in under 5 minutes
Based on Azoulay & Tucker's Platform Strategy Framework
"""

import sys
from typing import List, Tuple

class QuickCheck:
    """Quick platform viability checker"""
    
    def __init__(self):
        self.red_flags = []
        self.green_flags = []
        self.score = 0
        
    def run(self):
        """Run the quick assessment"""
        print("\n" + "="*60)
        print("PLATFORM QUICK CHECK - 5 Minute Assessment")
        print("="*60)
        print("\nAnswer YES or NO to each question:\n")
        
        questions = [
            # Must-haves (Red flags if NO)
            ("Can you name your platform's sides clearly?", True, "CRITICAL"),
            ("Do you solve a real search OR transaction cost problem?", True, "CRITICAL"),
            ("Is there a clear value exchange between sides?", True, "CRITICAL"),
            ("Can you explain your platform in one sentence?", True, "CRITICAL"),
            
            # Strong indicators (Major concerns if NO)
            ("Will network effects kick in at reasonable scale?", True, "MAJOR"),
            ("Do you have a path to overcome chicken-egg problem?", True, "MAJOR"),
            ("Is there differentiation from existing solutions?", True, "MAJOR"),
            ("Can you start without burning millions in subsidies?", True, "MAJOR"),
            
            # Important factors
            ("Does the platform offer ANY stand-alone value?", False, "IMPORTANT"),
            ("Are multi-homing costs meaningful (not trivial)?", False, "IMPORTANT"),
            ("Do you know which side will pay?", False, "IMPORTANT"),
            ("Can you maintain control of core interactions?", False, "IMPORTANT"),
            
            # Nice-to-haves
            ("Do you have access to marquee users?", False, "BONUS"),
            ("Is the market large enough for VC scale?", False, "BONUS"),
            ("Can you leverage existing assets/relationships?", False, "BONUS"),
        ]
        
        critical_pass = 0
        critical_total = 0
        major_pass = 0
        major_total = 0
        
        for question, is_critical, category in questions:
            answer = self.get_yes_no(question)
            
            if category == "CRITICAL":
                critical_total += 1
                if answer:
                    critical_pass += 1
                    self.green_flags.append(question[:-1])
                else:
                    self.red_flags.append(f"🚨 {question[:-1]}")
                    
            elif category == "MAJOR":
                major_total += 1
                if answer:
                    major_pass += 1
                    self.green_flags.append(question[:-1])
                else:
                    self.red_flags.append(f"⚠️  {question[:-1]}")
                    
            else:
                if answer:
                    self.score += 1
                    if category == "BONUS":
                        self.green_flags.append(f"✨ {question[:-1]}")
                    else:
                        self.green_flags.append(question[:-1])
        
        # Generate verdict
        print("\n" + "="*60)
        print("QUICK ASSESSMENT RESULTS")
        print("="*60)
        
        # Check critical failures
        if critical_pass < critical_total:
            print("\n❌ VERDICT: NOT READY - FUNDAMENTAL ISSUES")
            print(f"\nFailed {critical_total - critical_pass} of {critical_total} critical checks")
            print("\nCritical issues that MUST be resolved:")
            for flag in self.red_flags:
                if "🚨" in flag:
                    print(f"  {flag}")
            print("\nRecommendation: Reconsider if platform model is appropriate")
            
        elif major_pass < major_total - 1:  # Allow 1 major issue
            print("\n⚠️  VERDICT: HIGH RISK - MAJOR CONCERNS")
            print(f"\nPassed all critical checks but has {major_total - major_pass} major concerns")
            print("\nMajor issues to address:")
            for flag in self.red_flags:
                if "⚠️" in flag:
                    print(f"  {flag}")
            print("\nRecommendation: Address major issues before proceeding")
            
        elif len(self.green_flags) >= 10:
            print("\n✅ VERDICT: PROMISING - PROCEED WITH DETAILED ANALYSIS")
            print(f"\nPassed {len(self.green_flags)}/15 checks")
            print("\nKey strengths identified:")
            for flag in self.green_flags[:5]:  # Show top 5
                print(f"  ✓ {flag}")
            print("\nRecommendation: Run full Platform Assessment for detailed insights")
            
        else:
            print("\n🟡 VERDICT: MODERATE POTENTIAL - NEEDS STRENGTHENING")
            print(f"\nPassed {len(self.green_flags)}/15 checks")
            print("\nConsider strengthening these areas before proceeding")
            print("\nRecommendation: Iterate on concept, then run full assessment")
        
        # Quick tips
        print("\n" + "="*60)
        print("QUICK TIPS")
        print("="*60)
        
        if critical_pass < critical_total:
            print("• Focus on fundamentals: clearly define your sides and value proposition")
            print("• Study successful platforms in adjacent spaces")
            print("• Consider starting with a service/product model first")
        elif major_pass < major_total:
            print("• Develop concrete plans for seeding initial users")
            print("• Create detailed mockups of core interactions")
            print("• Interview potential users from both sides")
        else:
            print("• Build a simple prototype to test core assumptions")
            print("• Identify and approach potential marquee users")
            print("• Run the full Platform Assessment for go/no-go decision")
        
        print("\nNext step: Run 'python platform_assessment.py --interactive'")
        print("           for comprehensive analysis")
        print("="*60 + "\n")
    
    def get_yes_no(self, question: str) -> bool:
        """Get yes/no answer from user"""
        while True:
            response = input(f"{question} (y/n): ").lower().strip()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please answer 'y' for yes or 'n' for no")


def main():
    checker = QuickCheck()
    checker.run()


if __name__ == '__main__':
    main()
