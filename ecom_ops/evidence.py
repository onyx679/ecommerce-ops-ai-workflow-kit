from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


LOCAL_REFERENCE_PATTERN = re.compile(r"`([^`\n]+)`")
REQUIRED_BOUNDARIES = [
    "Do not describe it as a real merchant project.",
    "Do not claim real customer, merchant, or platform export data.",
    "Do not claim production deployment.",
    "Do not imply external adoption or review.",
    "AI output is limited to draft preparation and risk surfacing.",
]


@dataclass(frozen=True)
class EvidenceValidation:
    ok: bool
    checked_references: list[str]
    errors: list[str]


def validate_evidence_file(evidence_path: Path, repo_root: Path | None = None) -> EvidenceValidation:
    repo_root = repo_root or evidence_path.parent
    errors: list[str] = []
    checked_references: list[str] = []

    if not evidence_path.exists():
        return EvidenceValidation(False, [], [f"missing evidence file: {evidence_path}"])

    text = evidence_path.read_text(encoding="utf-8")
    for reference in _local_references(text):
        checked_references.append(reference)
        if not (repo_root / reference).exists():
            errors.append(f"missing referenced evidence path: {reference}")

    for boundary in REQUIRED_BOUNDARIES:
        if boundary not in text:
            errors.append(f"missing safety boundary: {boundary}")

    return EvidenceValidation(ok=not errors, checked_references=checked_references, errors=errors)


def render_pretty(result: EvidenceValidation) -> str:
    lines = [f"STATUS: {'PASS' if result.ok else 'FAIL'}"]
    lines.append(f"Checked references: {len(result.checked_references)}")
    for reference in result.checked_references:
        lines.append(f"REFERENCE: {reference}")
    for error in result.errors:
        lines.append(f"ERROR: {error}")
    return "\n".join(lines)


def _local_references(text: str) -> list[str]:
    references: list[str] = []
    seen: set[str] = set()
    for raw_reference in LOCAL_REFERENCE_PATTERN.findall(text):
        for reference in _split_reference(raw_reference):
            if _is_local_path(reference) and reference not in seen:
                seen.add(reference)
                references.append(reference)
    return references


def _split_reference(reference: str) -> list[str]:
    return [part.strip() for part in reference.split(",") if part.strip()]


def _is_local_path(reference: str) -> bool:
    if reference.startswith(("http://", "https://", "v0.")):
        return False
    return "/" in reference or reference.endswith((".md", ".py", ".csv", ".html", ".yml"))
