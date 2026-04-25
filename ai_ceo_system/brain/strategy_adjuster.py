import json
import os
from datetime import datetime

class StrategyAdjuster:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir

    def build_ceo_prompt(self, **kwargs):
        return f"""You are a coordinated system of specialized AI agents working together as an autonomous AI CEO.

The system consists of 3 agents:

1. PRODUCT_AGENT → selects and evaluates products
2. HOOK_AGENT → generates and optimizes hooks
3. STRATEGY_AGENT → analyzes performance and decides actions

Additionally, you have MEMORY, which stores past performance data and must be used to improve decisions.

---

# INPUT DATA

## CURRENT PRODUCT

* Name: {kwargs.get('product_name', 'Unknown')}

## PERFORMANCE METRICS

* CTR: {kwargs.get('ctr', 0)} %
* Watch Time: {kwargs.get('watch_time', 0)} %
* Conversion Rate: {kwargs.get('conversion_rate', 0)} %
* Views: {kwargs.get('views', 0)}
* Revenue: ${kwargs.get('revenue', 0)}

## TREND DATA

* TikTok Virality: {kwargs.get('tiktok_score', 0)}/100
* Amazon Rating: {kwargs.get('amazon_rating', 0)}/5
* Google Trend Growth: {kwargs.get('trend_growth', 0)}/100

## MEMORY (VERY IMPORTANT)

Past Data:

* Winning Hooks: {kwargs.get('winning_hooks', 'None')}
* Failed Hooks: {kwargs.get('failed_hooks', 'None')}
* High Retention Video Styles: {kwargs.get('good_video_styles', 'None')}
* Low Retention Video Styles: {kwargs.get('bad_video_styles', 'None')}
* Winning Products: {kwargs.get('winning_products', 'None')}
* Failed Products: {kwargs.get('failed_products', 'None')}

---

# AGENT RESPONSIBILITIES

## 🛍️ PRODUCT_AGENT

Tasks:

* Score product viability:
  Score = (TikTok + Amazon*20 + Trend Growth) / 3
* Compare with MEMORY:

  * Avoid patterns from failed products
  * Prefer patterns from winning products

Decisions:

* REJECT (score < 50)
* TEST (50–70)
* SCALE (>70)

---

## 🎯 HOOK_AGENT

Tasks:

* Generate 5 new hooks
* Use MEMORY:

  * Reuse patterns from winning hooks
  * Avoid failed hook styles

Rules:

* Max 8 words
* Must create curiosity or emotional trigger
* Focus on scroll-stopping effect

Also classify each hook:
[Shock, Curiosity, Problem, Benefit]

---

## 🎬 STRATEGY_AGENT

Tasks:

1. Diagnose weakest link:

   * CTR → Hook problem
   * Watch Time → Video problem
   * Conversion → Product problem

2. Use MEMORY:

   * Reuse high-performing video styles
   * Avoid low-performing styles

3. Decide actions:

   * Improve hook
   * Change video style
   * Replace or scale product

---

# DECISION RULES

* CTR < 3% → Fix hooks
* Watch Time < 50% → Fix video
* Conversion Rate < 2% → Fix product
* Views > 10,000 → Scaling opportunity

---

# LEARNING SYSTEM (CRITICAL)

You MUST update memory:

* Add successful hooks to "winning_hooks"
* Add failed hooks to "failed_hooks"
* Add successful products to "winning_products"
* Add failed products to "failed_products"
* Track video styles performance

---

# OUTPUT FORMAT (STRICT JSON)

{{
"product_agent": {{
"score": "...",
"decision": "REJECT | TEST | SCALE",
"reason": "..."
}},
"hook_agent": {{
"new_hooks": [
{{"text": "...", "type": "..."}},
{{"text": "...", "type": "..."}},
{{"text": "...", "type": "..."}},
{{"text": "...", "type": "..."}},
{{"text": "...", "type": "..."}}
]
}},
"strategy_agent": {{
"main_problem": "...",
"actions": [
"...",
"...",
"..."
],
"video_strategy": [
"fast cuts every 1-2 seconds",
"bold subtitles",
"zoom transitions"
]
}},
"memory_update": {{
"add_winning_hooks": ["..."],
"add_failed_hooks": ["..."],
"add_winning_products": ["..."],
"add_failed_products": ["..."]
}}
}}

---

# BEHAVIOR RULES

* Always use MEMORY to improve decisions
* Never repeat failed patterns
* Prioritize winning patterns
* Be decisive and data-driven
* Focus on revenue and virality

---

# GOAL

Continuously evolve and improve performance using memory until:

* CTR > 5%
* Watch Time > 60%
* Conversion Rate > 3%

---

Now act as a coordinated AI system and produce the best optimized strategy."""

    def evaluate_performance(self):
        # Stub for evaluating CTR, conversions, etc.
        # In the future, this will connect to OpenAI API using build_ceo_prompt
        # For now, we simulate the AI response based on the prompt's instructions
        data = {
            "product_name": "Posture Corrector Pro",
            "ctr": 2.1,
            "watch_time": 85,
            "conversion_rate": 3.5,
            "views": 4500,
            "revenue": 150,
            "tiktok_score": 80,
            "amazon_rating": 4.5,
            "trend_growth": 65,
            "failed_hooks": "Are you sitting wrong?",
            "winning_hooks": "Do this for 5 seconds to fix back pain"
        }
        print(f"Generating strategy using advanced Agentic AI CEO Prompt for: {data['product_name']}...")
        prompt = self.build_ceo_prompt(**data)
        
        # Simulating the OpenAI Multi-Agent JSON response
        return {
            "product_agent": {
                "score": "78",
                "decision": "SCALE",
                "reason": "Score of 78 > 70. Conversion rate is solid at 3.5% and TikTok trend is strong."
            },
            "hook_agent": {
                "new_hooks": [
                    {"text": "This secretly ruins your posture.", "type": "Curiosity"},
                    {"text": "Stop destroying your spine immediately.", "type": "Shock"},
                    {"text": "3 seconds to fix lower back pain.", "type": "Benefit"},
                    {"text": "Why sitting like this is dangerous.", "type": "Problem"},
                    {"text": "The fastest way to fix hunchback.", "type": "Benefit"}
                ]
            },
            "strategy_agent": {
                "main_problem": "Hook performance is drastically bottlenecking a winning product. CTR < 3%.",
                "actions": [
                    "A/B test the 5 new hooks specifically leveraging the '3 seconds to fix' formula.",
                    "Increase ad budget since product conversion metrics are scaling effectively.",
                    "Maintain current video pacing but overlay bold shock-value text on the first frame."
                ],
                "video_strategy": [
                    "fast cuts every 1-2 seconds",
                    "bold red subtitles for the first 3 frames",
                    "zoom transitions out of the hook"
                ]
            },
            "memory_update": {
                "add_winning_hooks": [],
                "add_failed_hooks": ["Are you sitting wrong? (CTR 2.1%)"],
                "add_winning_products": ["Posture Corrector Pro"],
                "add_failed_products": []
            }
        }

    def generate_strategy_plan(self):
        date_str = datetime.now().strftime("%Y-%m-%d")
        plan_path = os.path.join(self.log_dir, f"strategy_plan_{date_str}.json")
        
        evaluation = self.evaluate_performance()
        
        with open(plan_path, "w") as f:
            json.dump(evaluation, f, indent=4)
                
        return plan_path

if __name__ == "__main__":
    adjuster = StrategyAdjuster(log_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs'))
    print(f"Generated plan at: {adjuster.generate_strategy_plan()}")
