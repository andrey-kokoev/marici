"""Check the aggregate Agda module for the constructive zeta test framework."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
AGDA_ROOT = ROOT / "research" / "voevodsky" / "agda"
TARGET = AGDA_ROOT / "ConstructiveValueModel.agda"
RESULT = ROOT / "research" / "voevodsky" / "results" / "zeta_constructive_framework.json"
DEFAULT_AGDA = Path("C:/Users/andrey/tools/agda-2.8.0.1/agda.exe")
DEFAULT_CUBICAL = Path("C:/Users/andrey/tools/cubical-agda/cubical-0.9")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    agda = Path(os.environ.get("AGDA_EXE", str(DEFAULT_AGDA)))
    cubical = Path(os.environ.get("CUBICAL_AGDA", str(DEFAULT_CUBICAL)))
    command = [
        str(agda),
        "--transliterate",
        "-i",
        str(AGDA_ROOT),
        "-i",
        str(AGDA_ROOT / "generated"),
        "-i",
        str(cubical),
        str(TARGET),
    ]
    missing = [str(path) for path in (agda, cubical, TARGET) if not path.exists()]
    if missing:
        payload = {
            "schema": "marici.zeta-constructive-framework-check.v1",
            "passed": False,
            "failure_kind": "missing_input",
            "missing": missing,
        }
        exit_code = 2
    else:
        completed = subprocess.run(
            command, capture_output=True, text=True, timeout=600, check=False
        )
        with tempfile.TemporaryDirectory(prefix="marici-zeta-negative-") as directory:
            invalid = Path(directory) / "InvalidClaimPromotion.agda"
            invalid.write_text(
                "{-# OPTIONS --safe --cubical --guardedness #-}\n"
                "module InvalidClaimPromotion where\n"
                "open import Cubical.Foundations.Prelude\n"
                "open import Cubical.Data.Empty\n"
                "data Name : Type where name : Name\n"
                "data Zero : Type where zero : Zero\n"
                "NoNamed : Type\n"
                "NoNamed = Name → ⊥\n"
                "invalidPromotion : NoNamed → Zero → ⊥\n"
                "invalidPromotion noName zero = noName zero\n",
                encoding="utf-8",
            )
            negative = subprocess.run(
                [
                    str(agda), "--transliterate",
                    "-i", directory,
                    "-i", str(cubical),
                    str(invalid),
                ],
                capture_output=True,
                text=True,
                timeout=60,
                check=False,
            )
        framework_sources = [
            "ZetaConstructibilityContract.agda",
            "ZetaZeroNamingContract.agda",
            "ZetaSelectorCountermodels.agda",
            "ComplexSeriesCompletion.agda",
            "TriangularComplexSeriesCompletion.agda",
            "ComplexExponentialAssembly.agda",
            "OperationalAnalyticZeroLaws.agda",
            "RationalSineTaylorApproximants.agda",
            "RationalLogTaylorApproximants.agda",
            "RationalLogConvergenceContract.agda",
            "AtanhTermBounds.agda",
            "AtanhPowerDecayContract.agda",
            "AtanhTailBounds.agda",
            "OrderedDifferenceRegularity.agda",
            "ConstructiveDirichletTerm.agda",
            "OperationalDirichletTerm.agda",
            "OperationalDirichletPartialSum.agda",
            "OperationalZetaPrimitives.agda",
            "CanonicalRegularMultiplication.agda",
            "CanonicalComplexRegularMultiplication.agda",
            "CanonicalComplexRegularExponential.agda",
            "CanonicalNegativePowerKernel.agda",
            "CanonicalDirichletRegularPartialSum.agda",
            "CanonicalDirichletTriangularApproximation.agda",
            "ConstructiveZetaTwo.agda",
            "ConstructiveNaturalZeta.agda",
            "NaturalZetaCompletion.agda",
            "RegularCauchyTriangularEmbedding.agda",
            "AbsoluteTaylorSeriesMultiplication.agda",
            "RationalSineSymmetry.agda",
            "SineTermBounds.agda",
            "UniformSineSeedBounds.agda",
            "SineInputDifference.agda",
            "SinePartialSumInputDifference.agda",
            "UniformSineInputStabilityContract.agda",
            "UniformSineStabilityScale.agda",
            "UniformSineLateDifference.agda",
            "CanonicalSineSchedule.agda",
            "CanonicalSineRegularity.agda",
            "CanonicalSineComparisonSchedule.agda",
            "CanonicalSineUniformComparison.agda",
            "OperationalSineMetric.agda",
            "SineTailSchedule.agda",
            "SineSeedCoherence.agda",
            "SineSeedNegation.agda",
            "CanonicalRationalSineSeed.agda",
            "ConstructiveZetaInterfaces.agda",
            "CriticalStripZeroContract.agda",
            "FiniteZetaExactExclusion.agda",
            "FiniteZetaNoSelector.agda",
            "CompletionExponentialMultiplicationLaw.agda",
            "CompletionExponentialNaturalMultiples.agda",
            "CompletedExponentialMultiplication.agda",
            "MetricCompletionEffectiveness.agda",
            "RationalExponentialProductRepresentative.agda",
            "RawProductRefinementTransport.agda",
            "ExponentialProductEventualApproximation.agda",
            "EndpointBoundedProductComparison.agda",
            "SynchronizedExponentialApproximation.agda",
            "ExponentialRationalApproximation.agda",
            "BoundedExponentialModulus.agda",
            "ConstructiveValueModel.agda",
        ]
        source_digests = {
            name: digest(AGDA_ROOT / name) for name in framework_sources
        }
        passed = completed.returncode == 0 and negative.returncode != 0
        payload = {
            "schema": "marici.zeta-constructive-framework-check.v1",
            "passed": passed,
            "failure_kind": None if passed else "aggregate_or_negative_control_failure",
            "exit_code": completed.returncode,
            "target": str(TARGET.relative_to(ROOT)).replace("\\", "/"),
            "target_sha256": digest(TARGET),
            "framework_source_sha256": source_digests,
            "deliberate_failure_observed": negative.returncode != 0,
            "deliberate_failure_exit_code": negative.returncode,
            "deliberate_failure_stdout_tail": negative.stdout[-2000:],
            "deliberate_failure_stderr_tail": negative.stderr[-2000:],
            "agda": str(agda),
            "cubical": str(cubical),
            "command": command,
            "stdout_tail": completed.stdout[-4000:],
            "stderr_tail": completed.stderr[-4000:],
            "verified_scope": [
                "aggregate module type-checks",
                "finite-zeta exclusion control type-checks",
                "selector and naming countermodels type-check",
                "triangular completion contracts type-check",
                "completion-level sine and complex exponential type-check",
                "critical-strip zero contracts type-check",
            ],
            "not_verified": [
                "Riemann zeta implementation",
                "complex logarithm implementation",
                "critical-strip zero constructibility",
                "universal zero unconstructability",
            ],
        }
        exit_code = 0 if passed else 1
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
