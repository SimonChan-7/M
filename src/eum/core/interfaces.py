"""Protocol skeletons for pluggable pipeline modules."""

from __future__ import annotations

from typing import Protocol


class BaseParser(Protocol):
    """Parser interface placeholder."""


class BaseCandidateMiner(Protocol):
    """Candidate miner interface placeholder."""


class BaseExtractor(Protocol):
    """Extractor interface placeholder."""


class BaseValidator(Protocol):
    """Validator interface placeholder."""


class BaseNormalizer(Protocol):
    """Normalizer interface placeholder."""


class BaseAggregator(Protocol):
    """Aggregator interface placeholder."""


class BaseEvaluator(Protocol):
    """Evaluator interface placeholder."""
