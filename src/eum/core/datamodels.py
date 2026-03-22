"""Unified data object boundaries for the evidence unit pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Document:
    """Placeholder full-text document container."""

    identifier: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Section:
    """Placeholder section container."""

    title: str = ""
    text: str = ""


@dataclass(slots=True)
class TextUnit:
    """Placeholder paragraph or sentence-level text unit."""

    text: str = ""


@dataclass(slots=True)
class CandidateUnit:
    """Placeholder candidate evidence span."""

    text: str = ""


@dataclass(slots=True)
class EvidenceUnit:
    """Placeholder shared evidence unit with scenario-specific extensions deferred to tasks."""

    core_claim: dict[str, Any] = field(default_factory=dict)
    biological_context: dict[str, Any] = field(default_factory=dict)
    methodological_conditions: dict[str, Any] = field(default_factory=dict)
    provenance: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class NormalizedEvidenceUnit:
    """Placeholder normalized evidence unit."""

    evidence: EvidenceUnit | None = None
    normalized_fields: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ValidationReport:
    """Placeholder validation report."""

    is_valid: bool = False
    messages: list[str] = field(default_factory=list)
