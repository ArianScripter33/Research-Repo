"""Evaluation metric stubs for reasoning and planning benchmarks.

This file intentionally ships as a scaffold to signal planned, reproducible
benchmark instrumentation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class EvaluationResult:
    name: str
    score: float
    notes: str = ""


def groundedness_score(payload: Dict) -> EvaluationResult:
    """TODO: compute evidence-groundedness ratio."""
    return EvaluationResult(name="groundedness", score=0.0, notes="stub")


def planning_horizon_score(payload: Dict) -> EvaluationResult:
    """TODO: assess long-horizon plan stability."""
    return EvaluationResult(name="planning_horizon", score=0.0, notes="stub")


def cot_verification_score(payload: Dict) -> EvaluationResult:
    """TODO: score chain-of-thought verification checkpoints."""
    return EvaluationResult(name="cot_verification", score=0.0, notes="stub")


def self_correction_score(payload: Dict) -> EvaluationResult:
    """TODO: measure self-correction loop effectiveness."""
    return EvaluationResult(name="self_correction", score=0.0, notes="stub")
