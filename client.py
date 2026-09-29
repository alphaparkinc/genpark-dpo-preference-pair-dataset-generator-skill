"""DPO Preference Pair Dataset Generator.
100% Python Standard Library.
"""

import json

class DPOPreferenceGenerator:
    """Constructs and validates Direct Preference Optimization (DPO) preference pairs."""
    @staticmethod
    def create_preference_pair(prompt: str, chosen: str, rejected: str, chosen_score: float = 1.0, rejected_score: float = 0.0, metadata: dict = None) -> dict:
        valid_res = DPOPreferenceGenerator.validate_pair(prompt, chosen, rejected, chosen_score, rejected_score)
        margin = round(chosen_score - rejected_score, 4)
        return {
            "prompt": prompt,
            "chosen": chosen,
            "rejected": rejected,
            "chosen_score": chosen_score,
            "rejected_score": rejected_score,
            "margin": margin,
            "is_valid": valid_res["valid"],
            "validation_issues": valid_res["issues"],
            "metadata": metadata or {}
        }

    @staticmethod
    def validate_pair(prompt: str, chosen: str, rejected: str, chosen_score: float, rejected_score: float) -> dict:
        issues = []
        if not prompt.strip():
            issues.append("Prompt is empty")
        if not chosen.strip():
            issues.append("Chosen response is empty")
        if not rejected.strip():
            issues.append("Rejected response is empty")
        if chosen.strip() == rejected.strip():
            issues.append("Chosen and rejected are identical")
        if chosen_score <= rejected_score:
            issues.append("Chosen score must be strictly greater than rejected score")
        return {"valid": len(issues) == 0, "issues": issues}

    @staticmethod
    def to_jsonl(pairs: list) -> str:
        lines = []
        for p in pairs:
            lines.append(json.dumps({"prompt": p["prompt"], "chosen": p["chosen"], "rejected": p["rejected"]}))
        return "\n".join(lines)
