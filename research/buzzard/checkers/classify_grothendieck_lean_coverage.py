"""Read-only classifier for Grothendieck-facing Lean coverage triage.

This script does not certify mathematics. It identifies packet-level evidence
that a document contains exact/proved material, gated/conjectural material, or
both, and attaches overlapping theorem-family tags. Mixed packets require
manual theorem-level splitting before a coverage claim is admitted.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


EXACT_MARKERS = (
    " is exact",
    " are exact",
    " proves ",
    " proved ",
    " exact formula",
    " exact identity",
    " exact decomposition",
    " exact obstruction",
    " result",
)

GATE_MARKERS = (
    " remains open",
    " remaining gate",
    " not yet proved",
    " no rh conclusion",
    " does not prove",
    " conjecture",
    " prospective",
    " still to be derived",
    " missing theorem",
)

FAMILIES = {
    "theta": r"\btheta\b|^theta-",
    "analytic_certificate": r"certificate|remainder|interval|cauchy|concavity|curvature",
    "eta_gamma": r"\beta\b|\bgamma\b|digamma|stieltjes",
    "finite_group_monodromy": r"monodromy|adams|mackey|finite group|deck|frobenius",
    "boundary_relative": r"boundary|relative|cohomology|cokernel|radical|chain homotopy",
    "prime_euler": r"prime|euler|von mangoldt|dirichlet",
    "completion_descent": r"completion|complete|descent|colimit|dense",
    "determinant_kernel_operator": r"determinant|kernel|operator|resolvent|spectrum|fredholm",
    "positivity_gram": r"positiv|gram|hermite|loewner|herglotz",
    "coherence_transport": r"coherence|transport|cocycle|seam|gluing|sewing",
    "no_go_gate": r"no-go|nogo|obstruction|gate|falsifier",
}


# The theta corpus is large and deliberately repetitive: many packets vary one
# analytic or source convention while reusing the same finite obstruction.  A
# family rule records that reusable core without pretending to discharge the
# packet-specific interface.  Explicit curated entries above always win.
THETA_FAMILY_RULES = (
    {
        "family": "adelic_tate_product",
        "pattern": r"\b(?:adelic|idele|ideles|tate|product-formula|local-tate|all-place)\b",
        "lean_evidence": ["GaussianNormTwo.lean", "IncidenceDivisorRotation.lean", "BoundaryRealStructurePhaseNoGo.lean"],
        "missing_interfaces": [
            "typed restricted product of local source spaces and measures",
            "place-by-place Fourier normalization and product formula",
            "source-canonical adelic comparison map rather than a fitted tensor factorization",
        ],
    },
    {
        "family": "seam_reflection_transport",
        "pattern": r"\b(?:seam|seams|sheet|sheets|reflection|transport|adjoint|reciprocal|quarter-turn)\b",
        "lean_evidence": ["BoundaryAdjointSeam.lean", "MovingSeamCocycle.lean", "ReciprocalSeamFlag.lean", "DirectLimitReflection.lean"],
        "missing_interfaces": [
            "source-defined seam, orientation, and admissible transport groupoid",
            "analytic boundary values and domains of the transported operators",
            "effective descent or coherence beyond the finite cocycle core",
        ],
    },
    {
        "family": "clark_boundary_model",
        "pattern": r"\b(?:clark|debranges|herglotz|pick-kernel|rkhs|characteristic-model)\b",
        "lean_evidence": ["BoundaryCokernel.lean", "ReflectionPositivity.lean", "FiniteObservation.lean", "LocalResidueKrein.lean"],
        "missing_interfaces": [
            "Schur or inner function derived from the undecomposed theta source",
            "Clark measure, boundary evaluation, and derivative theorem",
            "unbounded model operator domain and source-normalized spectral comparison",
        ],
    },
    {
        "family": "cubic_hermite_flow",
        "pattern": r"\b(?:cubic|plucker|transvectant|jensen|laguerre|root-flow|stokes|thimble)\b",
        "lean_evidence": ["CubicHermiteResidual.lean", "ThetaZeroFlowPropagation.lean", "NewmanSpectralHeatSeparation.lean"],
        "missing_interfaces": [
            "analytic polynomial or entire-function flow with convention-fixed coefficients",
            "simple-root continuation, discriminant, and crossing control",
            "passage from finite Hermite algebra to the theta or Xi limit",
        ],
    },
    {
        "family": "heat_gaussian_smoothing",
        "pattern": r"\b(?:heat|gaussian|diffusion|smoothing|fisher|poisson|bernstein|log-concavity|variance|positivity|positive-cone|self-fourier)\b",
        "lean_evidence": ["GaussianNormTwo.lean", "GaussianSmoothingThreshold.lean", "GaussianSeamSewing.lean", "OffAxisHeatOscillation.lean"],
        "missing_interfaces": [
            "analytic theta heat kernel and justified differentiation or convolution",
            "uniform tails and source-certified sign estimates",
            "infinite-dimensional positivity or zero-flow conclusion beyond the finite hostile",
        ],
    },
    {
        "family": "prime_euler_determinant",
        "pattern": r"\b(?:prime|primes|euler|von-mangoldt|dirichlet|schatten|determinant|schur|spectral-shift)\b",
        "lean_evidence": ["PrimeOscillatorIncidence.lean", "PrimeCutoffAnomaly.lean", "AcyclicTailSchur.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "infinite prime-power summability and the stated regularized determinant class",
            "common continuation with gamma and endpoint terms",
            "source-derived coefficient--Betti coupling retaining signs and multiplicities",
        ],
    },
    {
        "family": "moment_jacobi_shell",
        "pattern": r"\b(?:moment|moments|jacobi|shell|shells|radial|band|bands|block|blocks|chart|charts|weyl|sampling|cutoff|modular-tail|tail-envelope)\b",
        "lean_evidence": ["FiniteHausdorffMoments.lean", "FiniteStieltjesMoments.lean", "JacobiDeterminantRatio.lean", "CumulativeShellAllocation.lean"],
        "missing_interfaces": [
            "source moment functional with all required positivity localizers",
            "analytic truncation, tail, or continuum certificate",
            "compatible infinite Jacobi or shell operator and spectral identification",
        ],
    },
    {
        "family": "completion_krein_boundary",
        "pattern": r"\b(?:completion|krein|gns|cokernel|quotient|divisor|jordan|rigged|boundary|topology|riesz|label-accumulation)\b",
        "lean_evidence": ["CompletionKernel.lean", "CompletionNeutrality.lean", "BoundaryCokernel.lean", "LocalResidueKrein.lean"],
        "missing_interfaces": [
            "source topology and dense embedding fixed before completion",
            "closable compatible operator or relation with its exact domain",
            "positive or Krein boundary form and descended source kernel",
        ],
    },
    {
        "family": "incidence_observation_control",
        "pattern": r"\b(?:incidence|readout|observer|control|evans|port|ports|selector|forcing|faithful)\b",
        "lean_evidence": ["FiniteObservation.lean", "RankOneIncidenceFaithfulness.lean", "IncidencePullbackMetric.lean", "ReflectionPairingAmbiguity.lean"],
        "missing_interfaces": [
            "source and target objects for the proposed observation or control map",
            "faithful quotient coordinates and unavailable-versus-zero port typing",
            "physical/source-derived pairing rather than a formal dual completion",
        ],
    },
    {
        "family": "fock_heisenberg_character",
        "pattern": r"\b(?:fock|heisenberg|vacuum|character|comb|zak|dilation|translation)\b",
        "lean_evidence": ["FiniteUnitaryOrbitNoGo.lean", "GaussianValuationTwoLevel.lean", "TranslationReflectionResidual.lean", "BoundaryCommutatorInvariant.lean"],
        "missing_interfaces": [
            "infinite Heisenberg or Fock representation with convention-fixed vacuum",
            "strong continuity, generator domains, and implementability",
            "source-selected character orbit or arithmetic lattice comparison",
        ],
    },
    {
        "family": "mellin_circle_phase",
        "pattern": r"\b(?:mellin|circle|phase|angular|maslov|metaplectic|kahler|projective|winding)\b",
        "lean_evidence": ["LogarithmicChartBoundary.lean", "PhaseICarrierObstructions.lean", "BoundaryRealStructurePhaseNoGo.lean", "PrimeBoundaryCocycle.lean"],
        "missing_interfaces": [
            "Mellin or Fourier transform with fixed Haar, branch, and half-density conventions",
            "source orientation or metaplectic lift fixing the phase",
            "analytic continuation and comparison to the completed theta source",
        ],
    },
    {
        "family": "operator_energy_spectral_gate",
        "pattern": r"\b(?:operator|spectrum|dirac|shear|loewner|energy|zero-freeness|causal|history|polya|outer|flow|passivity|canonical-system|green-transfer|bezoutian|remainder|endpoint-repair|holomorphic-j|first-order|bulk|endpoint)\b",
        "lean_evidence": ["CompletedKernelSectorNoGo.lean", "ReciprocalSlopeCurvature.lean", "BoundaryCommutatorInvariant.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "closed or self-adjoint operator with a convention-fixed domain",
            "source-derived energy or Loewner form with certified sign",
            "compactness, spectral mapping, or zero-free conclusion at the claimed analytic strength",
        ],
    },
    {
        "family": "relative_lattice_integrality",
        "pattern": r"\b(?:lattice|integral|integrality|parity|product-fiber|product-ratio|relative-cycle|relative-haar|half-density|two-label|quadrature|affine|dyadic-refinement)\b",
        "lean_evidence": ["GaussianValuationTwoLevel.lean", "FiniteDifferenceCorrespondence.lean", "IncidencePullbackMetric.lean", "ReciprocalSeamFlag.lean"],
        "missing_interfaces": [
            "source lattice, relative quotient, and coefficient ring fixed before comparison",
            "Haar or half-density normalization and representative independence",
            "integrality or parity transport to the completed theta source",
        ],
    },
    {
        "family": "zero_pairing_factor_gate",
        "pattern": r"\b(?:zero|zeros|pairing|null|spectral-factor|inner-factor|principal-angle|innovation|critical-value|saddle|local-trace|primitive|quarter-centered|scalar-zero)\b",
        "lean_evidence": ["FiniteObservation.lean", "BoundaryCokernel.lean", "RankOneDeterminantNoGo.lean", "ReflectionPairingAmbiguity.lean"],
        "missing_interfaces": [
            "source-normalized pairing or factorization fixed before reference to zeros",
            "analytic divisor multiplicity and boundary-value typing",
            "proof that a pairing null descends to the claimed operator, cohomology, or spectral object",
        ],
    },
    {
        "family": "modular_fold_transform",
        "pattern": r"\b(?:arithmetic-fold|four-transform|modular|grassmannian|transversality)\b",
        "lean_evidence": ["DiagonalCongruencePositivity.lean", "EvenJetObservability.lean", "MovingSeamCocycle.lean", "ReflectionPositivity.lean"],
        "missing_interfaces": [
            "source modular or fold action with generator and normalization conventions",
            "analytic transform or jet sewing theorem on the declared domain",
            "infinite Grassmannian transversality or source-positive conclusion",
        ],
    },
    {
        "family": "finite_rank_hostile",
        "pattern": r"\b(?:finite|rank|two-copy|two-vector|four-channel|six-point|no-finite|no-common|hostile)\b",
        "lean_evidence": ["FiniteObservation.lean", "SymmetricSquareObservationRank.lean", "ReflectionPairingAmbiguity.lean", "FiniteUnitaryOrbitNoGo.lean"],
        "missing_interfaces": [
            "packet-specific finite representation and coefficient convention",
            "identification of the finite hostile with the claimed theta source map",
            "colimit or analytic consequence, if any, beyond the finite countermodel",
        ],
    },
)


THETA_ACTIVE_PATTERNS = (
    r"^# .*\bconjecture\b",
    r"^## .*\bconjecture\b",
    r"\*\*conjecture",
    r"status:\s*active conjecture",
    r"\brh[- ]target\b",
    r"rh-equivalent[^\n]{0,80}\b(?:target|theorem|problem)\b",
)

# Human-reviewed artifact dispositions. These are deliberately separate from
# marker-based packet triage: adding an entry requires a theorem-level source
# read and either concrete Lean evidence or a named missing interface.
CURATED_DISPOSITIONS = {
    "global-prime-adjoint-anomaly-is-extensive-off-the-seam.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeCutoffAnomaly.lean", "PrimeSheetSeamDetector.lean"],
        "missing_interfaces": [
            "complex prime-power coefficients and modulus-ratio calculation",
            "Chebyshev theta or prime-power psi cutoff mass and unboundedness",
            "exponential trichotomy for positive, zero, and negative displacement",
            "fixed archimedean factor comparison and prime-infinity boundary current",
        ],
    },
    "a-scalar-zero-is-a-completion-class-jump-of-the-prime-boundary-current.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeBoundaryCocycle.lean", "AtomicScaleCurrent.lean"],
        "missing_interfaces": [
            "completed half-line source and reciprocal boundary integrals",
            "uniform prime-power tail asymptotics with scalar leading coefficient",
            "prime reciprocal divergence and higher-depth absolute convergence",
            "equivalence between scalar zero and exceptional-current convergence",
            "adjoint comparison of the upgraded reciprocal limits",
        ],
    },
    "theta-primitive-anomaly-completes-as-a-unitary-direct-limit-line.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["DirectLimitReflection.lean"],
        "missing_interfaces": [
            "directed finite-prime cutoff category and one-dimensional Hilbert lines",
            "Euler transition cocycle and seam unitarity",
            "Hilbert direct-limit construction and distinguished transported unit vector",
            "primitive/square affine anomaly coordinates",
            "Fourier-Tate antiunitary or dual-line compatibility",
        ],
    },
    "theta-reciprocal-seam-determinant-ratio-trivial.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "reflection-commuting Friedrichs diffusion and oriented seam operators",
            "heat-sandwiched trace-class compression",
            "Fredholm determinant invariance under unitary conjugacy",
            "nonvanishing denominator for the determinant ratio",
            "source-derived off-diagonal reciprocal crossing block",
        ],
    },
    "theta-direct-and-dual-tail-systems-carry-opposite-incidence-arrows.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["OppositeIncidenceArrows.lean"],
        "missing_interfaces": [
            "differential tail generator from the completed source",
            "Clark observation family on the analytic state",
            "Fourier-Tate adjoint relation between reciprocal sectors",
            "bounded completed sewing map and mixed boundary-supply residual",
            "accumulated path Gramian or cutoff-uniform sewing estimate",
        ],
    },
    "theta-finite-part-extraction-is-not-positive.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FinitePartPositivity.lean"],
        "missing_interfaces": [
            "general eventual-positive family with arbitrary divergence exponent",
            "Hadamard finite-part operator on an asymptotic class",
            "theta bulk and boundary-current covariance",
            "source-derived coupled relative order structure",
        ],
    },
    "theta-relative-euler-finite-part-is-regulator-universal.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FinitePartPositivity.lean"],
        "missing_interfaces": [
            "smooth rapidly decreasing normalized regulator class",
            "Mellin transform and inversion in a common convergence chamber",
            "zeta meromorphic continuation, residue calculation, and contour shift",
            "Hadamard finite-part bookkeeping including exceptional logarithmic parameters",
            "regulator-homotopy coherence theorem",
        ],
    },
    "theta-framed-pencil-symmetrizer-is-exactly-a-port-collocation-metric.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BorderedPencilSymmetrizer.lean"],
        "missing_interfaces": [
            "full iff theorem including invertible Hermitian block metric",
            "fundamental-symmetry specialization and simple-spectrum diagonalization",
            "modular reflection anticommutation on the logarithmic carrier",
            "source-authorized finite theta compression",
        ],
    },
    "theta-primitive-and-square-incidence-are-atomic-scale-currents.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AtomicScaleCurrent.lean"],
        "missing_interfaces": [
            "prime-Fock labels, logarithmic scale map, and von Mangoldt weights",
            "infinite positive atomic measures and prime asymptotics",
            "tempered versus exponential test-space continuity",
            "relative completion of the undamped sine readout",
            "archimedean transport between the two riggings",
        ],
    },
    "adjointness-of-the-boundary-cocycle-characterizes-the-critical-seam.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BoundaryAdjointSeam.lean"],
        "missing_interfaces": [
            "continuous centered half-line boundary integrals",
            "differentiability in interval length and positive source amplitude",
            "equality of reciprocal and Hilbert-adjoint boundary families",
            "zero-induced completion upgrade and star-compatible extension theorem",
        ],
    },
    "theta-moving-seam-projection-cocycle-nonfredholm.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["MovingSeamCocycle.lean", "InfiniteModeRetention.lean"],
        "missing_interfaces": [
            "L2 real-line translation and half-line multiplication projections",
            "indicator formula for the swept interval",
            "infinite-dimensional range and noncompactness of interval multiplication",
            "source-derived Hardy, de Branges, or reproducing-kernel compression",
            "Schatten class and determinant-line transition",
        ],
    },
    "no-natural-section-transfer.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["NaturalSectionNoGo.lean"],
        "missing_interfaces": [
            "finite-group homomorphism typing for the C2xC2 quotient and shear",
            "generality over arbitrary split finite-group surjections",
            "source-derived symmetry-breaking marking or lift",
            "physical coefficient and Betti chain transfer",
        ],
    },
    "li-degree-two-variance-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteLiVariance.lean"],
        "missing_interfaces": [
            "finite positive symmetric Borel measure on the unit circle",
            "trigonometric moment identities and almost-everywhere equality cases",
            "support classification by real phases or one conjugate pair",
            "arithmetic construction of one degree-independent positive moment functional",
        ],
    },
    "inertia-dynamical-euler-factor.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["InertiaGhostFrobenius.lean"],
        "missing_interfaces": [
            "permutation representation trace equals fixed-point count",
            "formal power-series exponential/log-determinant identity",
            "cycle decomposition and powered-cycle gcd splitting",
            "prime-to-inertia attachment and identification of u with p^(-s)",
        ],
    },
    "gaussian-smoothed-prime-adjacency-zero-character-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeTranslationAdjacency.lean"],
        "missing_interfaces": [
            "infinite prime-power von Mangoldt series with Gaussian log cutoff",
            "absolute convergence and bounded self-adjoint convolution operator",
            "Fourier multiplier and norm attainment at the trivial character",
            "inverse-Laplace identification with the prime heat kernel",
            "completed all-character archimedean-minus-prime positivity",
        ],
    },
    "li-finite-unitary-orbit-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteUnitaryOrbitNoGo.lean"],
        "missing_interfaces": [
            "Hilbert-unitary realization of the Li feature sequence",
            "finite unit-circle measure integral formulation",
            "independent theorem establishing unbounded Li growth in the typed realization",
            "renormalized infinite or distributional source alternative",
        ],
    },
    "inertia-ghost-frobenius-system.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["InertiaGhostFrobenius.lean"],
        "missing_interfaces": [
            "inertia groupoid objects and conjugating morphisms",
            "conjugacy invariance of fixed-point ghost coordinates",
            "intrinsic semiring-prime attachment to inertia objects",
            "cycle Euler determinant identity and arithmetic spectral weights",
        ],
    },
    "reciprocal-sewing-makes-the-gaussian-seam-port-an-observable-not-a-barrier.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GaussianSeamSewing.lean"],
        "missing_interfaces": [
            "half-line Fourier-Mellin integrals and Gaussian source amplitude",
            "integration-by-parts number-current formulas",
            "analytic convergence and boundary seam evaluation",
            "source-derived phase or conserved current constraining the symmetric kernel",
        ],
    },
    "theta-rank-one-fredholm-realization-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "Hilbert rank-one operator and Fredholm determinant lemma",
            "holomorphic feature family realizing the theta observation",
            "source-derived energy, transport, index, locality, or determinant-line law",
            "hostile quartet modification within the analytic theta class",
        ],
    },
    "theta-defect-velocity-two-copy-sinh-cosine-form.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["SinhCosineDefectWeight.lean"],
        "missing_interfaces": [
            "completed even theta density and two-copy integral formula",
            "differentiation under the integral and sum-difference change of variables",
            "conditional fixed-sum measures and cosine transforms",
            "boundary curvature identity and modular cross-sum transport inequality",
        ],
    },
    "modular-cyclic-monodromy-adams-spectrum.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CyclicAdamsSpectrum.lean", "GeometricSumSpectrum.lean"],
        "missing_interfaces": [
            "elementary-abelian kernel and faithful cyclic matrix action in characteristic p",
            "nonsemisimple twisted norm matrices and Jordan determinant calculation",
            "global gcd(n,p*m) criterion across every quotient fiber",
            "coefficient fiber-sum and basis-level lift squares",
        ],
    },
    "integral-two-periodic-norm-complex.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TwoPeriodicNormComplex.lean", "FiniteGroupNormDichotomy.lean"],
        "missing_interfaces": [
            "integral regular group ring and norm element",
            "augmentation ideal and kernel identification",
            "homology quotient I/(dI+R(d1-nu_G)) and annihilation by d",
            "localization and bad-characteristic specialization",
            "physical relative-chain realization",
        ],
    },
    "theta-forcing-is-the-exact-parabolic-confinement-residual.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ParabolicForcingResidual.lean"],
        "missing_interfaces": [
            "differentiable transported state and generator family",
            "ODE uniqueness and exponential nonvanishing theorem",
            "moving covector derivative term",
            "source-derived reciprocal theta enlargement and seam sewing",
        ],
    },
    "newman-divided-difference-cocycle.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["DividedDifferenceCocycle.lean"],
        "missing_interfaces": [
            "unordered-pair product for a finite root configuration",
            "absolute value and logarithmic Vandermonde identity",
            "differentiable injective coordinate and root motion",
            "closed Newman flow entropy derivative",
        ],
    },
    "xi-weyl-lattice-tangent-divergence.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["WeylLatticeTangentDivergence.lean"],
        "missing_interfaces": [
            "finite ordered configuration and all unordered-pair slope indexing",
            "log-Vandermonde tangent-plane identity with harmonic boundary field",
            "flattened Xi ordinate map and real-root ordering premise",
            "source-side extension before real-rootedness or Newman-flow monotonicity",
        ],
    },
    "gamma-resolvent-versus-shell-time-phase-type-correction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "even-oscillator self-adjoint operator and regularized resolvent trace",
            "prime Fourier-Mellin phase representation",
            "typed non-diagonal comparison kernel between the two functional calculi",
            "convention-fixed sinc shell-compression formula and aliasing interpretation",
        ],
    },
    "dual-cutoff-xp-weyl-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "measurable positive-quadrant xp region and exact phase-volume integral",
            "symplectic form, Heisenberg commutator, and source-normalized Planck cell",
            "self-adjoint Mellin dilation operator with dual cutoff boundary law",
            "source derivation of the cutoff product rather than fitting to zero data",
        ],
    },
    "de-branges-transfer-kernel-target.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": [],
        "missing_interfaces": [
            "holomorphic operator-valued transfer family derived from the prime-oscillator source",
            "operator-valued de Branges-Rovnyak kernel and Schur criterion",
            "reflection-compatible boundary limits and determinant identification",
            "RH-equivalent positive-real-part or finite-Gram positivity theorem",
        ],
    },
    "finite-place-scaling-colimit-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["LogarithmicChartBoundary.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "weighted L2 spaces and unitary multiplication by a positive density square root",
            "spectral type and noncompact resolvent of the real multiplication operator",
            "directed colimit with scaling-intertwining crossing maps",
            "prime reciprocal divergence and critical-line Euler multiplier limit",
            "canonical renormalized quotient with domain, resolvent, and determinant convergence",
        ],
    },
    "connes-semilocal-scaling-quotient-audit.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "formal statement of the cited CCM propositions and theorem with source-page conventions",
            "Hadamard topological ring quotient and closure of the Hermite-generated span",
            "semilocal Hilbert scaling pair and finite-place spectral measure",
            "typed comparison among topological quotient, ambient self-adjoint operator, and prolate limit",
            "all-places limit preserving domain, self-adjointness, compact resolvent, and determinant convergence",
        ],
    },
    "coprime-cyclic-monodromy-adams-spectrum.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CyclicAdamsSpectrum.lean", "GeometricSumSpectrum.lean"],
        "missing_interfaces": [
            "elementary-abelian kernel and faithful cyclic action",
            "twisted norm matrices on every quotient fiber",
            "semisimple eigenvalue reduction in characteristic p",
            "coefficient fiber-sum and basis-lift compatibility squares",
        ],
    },
    "finite-monodromy-exponent-adams-spectrum.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CyclicAdamsSpectrum.lean", "GeometricSumSpectrum.lean"],
        "missing_interfaces": [
            "arbitrary finite faithful group representation over F_p",
            "group exponent and Cauchy-element reduction",
            "Jordan determinant correction for twisted norm matrices",
            "nonabelian basis-level Mackey correspondence square",
        ],
    },
    "Euler-local-zero-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["LogarithmicChartBoundary.lean"],
        "missing_interfaces": [
            "complex prime-power local-factor nonvanishing on Re(s)>0",
            "gamma-function zero-freeness",
            "locally uniform absolute convergence of an infinite holomorphic product",
            "nonvanishing theorem for the resulting infinite product",
        ],
    },
    "equivariant-transfer-selection-nogo.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["NaturalSectionNoGo.lean"],
        "missing_interfaces": [
            "arbitrary finite surjection with transitive kernel action on each fiber",
            "general weighted-transfer uniqueness from equivariance",
            "source-derived symmetry-breaking section or geometric lift",
            "Betti chain transfer",
        ],
    },
    "difference-correspondence-noncompact-obstruction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteDifferenceCorrespondence.lean"],
        "missing_interfaces": [
            "locally compact abelian group and Haar/Tonelli normalization",
            "noncompact L2 domain and unboundedness theorem",
            "choice among quotient, relative tensor, semifinite trace, weights, or projective limits",
            "canonical physical relative-chain pushforward",
        ],
    },
    "conjugation-graph-determinant-class-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteSwapBlockDeterminant.lean"],
        "missing_interfaces": [
            "infinite orthogonal sum and singular-value computation",
            "trace-class and Hilbert-Schmidt summability equivalences",
            "Fredholm, regularized, or relative determinant construction",
            "source-derived arithmetic decay weights or reference operator",
        ],
    },
    "cohomology-representative-anomaly-class.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RepresentativeAnomaly.lean"],
        "missing_interfaces": [
            "graded source and target chain complexes",
            "defect Bianchi identity and cocycle preservation",
            "Hom-complex anomaly degree and exactness",
            "five-site physical boundary matrices",
        ],
    },
    "degenerate-pairing-radical-repair-obstruction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RadicalRepairObstruction.lean"],
        "missing_interfaces": [
            "graded chain complexes and Hom differential",
            "defect Bianchi identity",
            "source-derived degenerate coefficient-Betti pairing and radical subcomplex",
            "five-site physical boundary matrices",
        ],
    },
    "adams-doubling-aligns-shell-anomaly-channels.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AdamsDoublingShellChannels.lean"],
        "missing_interfaces": [
            "convention-fixed complex prime powers and proof of the second-Adams amplitude law",
            "sinc-exponential shell defect formula with its phase convention",
            "relative mapping cone between the s and 2s channels",
            "canonical finite part at 2s=1 and reflection compatibility",
        ],
    },
    "adjoint-denominator-composition-cancellation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AdjointDenominatorCancellation.lean"],
        "missing_interfaces": [
            "nondegenerate integral pairing lattices and unique rational adjoints",
            "least common denominators and Smith data for rational matrices",
            "localization-prime support under matrix composition",
            "named five-site transfer maps and independent boundary defects",
        ],
    },
    "acyclic-tail-schur-self-energy-mechanism.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AcyclicTailSchur.lean"],
        "missing_interfaces": [
            "finite-dimensional block Schur determinant identity",
            "closed operator domains and auxiliary resolvent",
            "determinant-class or relative-determinant construction",
            "source-derived acyclic coefficient-Betti complex and coupling",
        ],
    },
    "rank-one-parseval-phase-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RankOneParsevalPhaseNoGo.lean"],
        "missing_interfaces": [
            "global analytic phase lifting on a convention-fixed interval",
            "Riemann-Siegel and prime-archimedean scattering phase identities",
            "independent noncircular source derivation of the phase",
        ],
    },
    "finite-cutoff-pfaffian-lift-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FinitePfaffianNoGo.lean"],
        "missing_interfaces": [
            "general even-dimensional Pfaffian determinant-square identity",
            "source symmetry forcing an algebraic square factorization",
            "factorization compatibility under finite-cutoff inclusion",
        ],
    },
    "three-cell-adams-defect-positivity-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ThreeCellAdamsDefect.lean"],
        "missing_interfaces": [
            "Fin-3 Hermitian principal-minor equivalence with matrix PSD",
            "operator-valued Parrott completion with ordered defect operators",
            "source-derived prime-gamma correlations for the first prime tower",
        ],
    },
    "prime-power-translation-adjacency-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "PrimeTranslationAdjacency.lean",
            "SquarefreeWalshSpectrum.lean",
            "AdditivePrimeEdgeBudget.lean",
        ],
        "missing_interfaces": [
            "unitary log-time translation representation and Fourier cosine symbol",
            "finite prime-power cutoff with source-authorized von Mangoldt weights",
            "completed unbounded archimedean-minus-prime comparison with endpoints",
        ],
    },
    "squarefree-prime-cube-walsh-positivity-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "SquarefreeWalshSpectrum.lean",
            "FiniteCharacterCompleteness.lean",
            "FiniteCharacterSynthesis.lean",
            "FiniteCharacterOrthogonality.lean",
            "FiniteConvolutionReconstruction.lean",
            "SpectralCongruencePSD.lean",
            "AdditivePrimeEdgeBudget.lean",
            "MixedPrimeRectangleParity.lean",
        ],
        "missing_interfaces": [
            "source-derived route-independent completed Weil correlation",
        ],
    },
    "finite-euler-cross-weyl-positivity-and-diagonal-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CrossResolventGram.lean", "FiniteEulerGram.lean"],
        "missing_interfaces": [
            "free Green-kernel realization of the finite von Mangoldt source",
            "prime-square diagonal divergence",
            "relative positive quotient and completed Xi identification",
        ],
    },
    "minimal-hilbert-schur-prime-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteEulerGram.lean", "PolarizationQuarterTurn.lean"],
        "missing_interfaces": [
            "Stieltjes representing-measure theorem for positive resolvents",
            "oscillating prime-distance cut-density inversion",
            "canonical positive Krein descent",
        ],
    },
    "orthogonal-prime-penalty-two-prime-no-go.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["MixedPrimeRectangleParity.lean"],
        "missing_interfaces": [
            "replayable interval certificate for the required digamma values",
            "certified logarithm and square-root prime weights",
            "source identification of the diagonal-penalty model",
        ],
    },
    "mixed-prime-rectangle-parity-positivity-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["MixedPrimeRectangleParity.lean"],
        "missing_interfaces": [
            "completed Weil-distribution coefficient extraction",
            "complex and operator-valued adjoint formulation",
            "larger nonchordal mixed-prime cycles",
        ],
    },
    "additive-prime-edge-budget-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AdditivePrimeEdgeBudget.lean"],
        "missing_interfaces": [
            "Walsh diagonalization of the Boolean-cube convolution matrix",
            "completed Weil-form normalization and archimedean energy",
            "infinite prime summability and scale-dependent diagonal",
        ],
    },
    "adams-mackey-kernel-exponent-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CyclicAdamsSpectrum.lean"],
        "missing_interfaces": [
            "finite-abelian invariant-factor reduction",
            "coefficient fiber-sum and Betti fiber-lift squares",
            "physical relative-chain pushforward",
        ],
    },
    "central-extension-power-mackey-spectrum.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CyclicAdamsSpectrum.lean"],
        "missing_interfaces": [
            "finite central extension fibers",
            "power-map translation identity",
            "nonsplit control groups",
        ],
    },
    "finite-abelian-kernel-monodromy-spectrum.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CyclicAdamsSpectrum.lean", "GeometricSumSpectrum.lean"],
        "missing_interfaces": [
            "finite abelian primary decomposition",
            "conjugation-image exponent",
            "twisted norm-word bijectivity",
        ],
    },
    "cumulative-weyl-shell-rank-allocation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CumulativeShellAllocation.lean"],
        "missing_interfaces": ["continuous Weyl counting law", "source-derived Maslov constant"],
    },
    "newman-coordinate-change-anomaly.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["NewmanCoordinateRigidity.lean", "NewmanWeylEntropyBalance.lean"],
        "missing_interfaces": ["differentiable root paths", "constant-derivative integration"],
    },
    "newman-weyl-anomaly-entropy-balance.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["NewmanCoordinateRigidity.lean", "NewmanWeylEntropyBalance.lean"],
        "missing_interfaces": ["root-motion chain rule", "global Weyl-anomaly sign"],
    },
    "newman-symmetric-window-flux-cancellation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["SymmetricWindowFluxCancellation.lean"],
        "missing_interfaces": ["fourth-moment norm bound", "boundary-layer and infinite-window limit"],
    },
    "newman-affine-normalization-rigidity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteHermiteEntropy.lean", "NewmanWeylEntropyBalance.lean"],
        "missing_interfaces": [
            "closed simple-root Newman flow",
            "radius chain rule",
            "uniqueness of ordered Hermite equilibrium",
        ],
    },
    "newman-scale-normalized-discriminant.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteHermiteEntropy.lean", "NewmanWeylEntropyBalance.lean"],
        "missing_interfaces": [
            "Vandermonde derivative along root flow",
            "Hermite equilibrium classification",
            "infinite Xi window limit",
        ],
    },
    "small-theta-windows-have-a-globally-real-divisor.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ThetaZeroFlowPropagation.lean"],
        "missing_interfaces": [
            "compact and remote Rouche arguments",
            "continuous first-bad-parameter bridge",
            "finite collision exclusion",
        ],
    },
    "finite-theta-truncations-have-no-influx-from-infinity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteParameterNoInflux.lean", "ThetaZeroFlowPropagation.lean"],
        "missing_interfaces": ["uniform sine-type estimates", "complex zero exhaustion"],
    },
    "completed-theta-truncations-turn-rh-into-zero-flow.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteParameterNoInflux.lean", "ThetaZeroFlowPropagation.lean"],
        "missing_interfaces": ["continuous zero continuation", "theta collision exclusion"],
    },
    "hurwitz-forbids-zero-creation-by-stable-euler-completion.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["LogarithmicChartBoundary.lean"],
        "missing_interfaces": [
            "connected complex domains and holomorphic sections",
            "locally uniform convergence",
            "Hurwitz zero-free-or-identically-zero theorem",
        ],
    },
    "the-prime-staircase-is-a-logarithmic-chart-not-a-zero-state.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["LogarithmicChartBoundary.lean"],
        "missing_interfaces": ["analytic logarithm chart", "relative determinant through zeros"],
    },
    "the-complete-one-prime-quarter-density-overlap-is-nonvanishing.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ReciprocalGramOrientation.lean"],
        "missing_interfaces": [
            "infinite geometric and Euler-log series",
            "phase-circle reserve",
            "infinite product criterion",
        ],
    },
    "reciprocal-half-form-gram-positivity-does-not-orient-the-cross-kernel.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ReciprocalGramOrientation.lean"],
        "missing_interfaces": ["theta feature construction", "source-derived acute orientation"],
    },
    "the-canonical-quarter-density-lift-recovers-the-rigging-not-orientation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ValuationSquareCurrent.lean", "ReciprocalGramOrientation.lean"],
        "missing_interfaces": ["GNS square-root packet completion", "theta boundary-state coupling"],
    },
    "positive-staircase-curvature-forces-a-quarter-density-lift.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ValuationSquareCurrent.lean"],
        "missing_interfaces": ["source-authorized half-form construction"],
    },
    "exclusion-plus-valuation-degree-renormalizes-to-the-square-current.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ValuationSquareCurrent.lean"],
        "missing_interfaces": ["prime factorization projection sum", "unbounded valuation operators"],
    },
    "the-vacuum-obstructs-zero-state-exclusion-annihilation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeDivisionCurvature.lean"],
        "missing_interfaces": ["Mellin-transported Hilbert packet", "relative boundary balance"],
    },
    "prime-multiplication-division-curvature-is-positive-exclusion.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeDivisionCurvature.lean", "ValuationSquareCurrent.lean"],
        "missing_interfaces": ["Hilbert adjoint projection", "Gaussian sampling realization"],
    },
    "prime-translation-reflection-mixed-square-is-universal.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TranslationReflectionResidual.lean"],
        "missing_interfaces": ["continuous chart domains", "Gaussian-prime source-specific cell"],
    },
    "prime-cutoff-adjoint-anomaly-cocycle-is-exact-and-universal.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeCutoffAnomaly.lean"],
        "missing_interfaces": ["log-prime analytic specialization"],
    },
    "native-prime-sheet-adjoint-matching-occurs-exactly-on-the-seam.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeSheetSeamDetector.lean"],
        "missing_interfaces": ["complex prime powers", "labelled Hilbert adjoint", "zero-state bridge"],
    },
    "higher-contact-hermite-negative-mass-law.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HigherContactEntropyExponent.lean"],
        "missing_interfaces": ["backward heat asymptotics", "Hermite negative-mass integral"],
    },
    "theta-derivative-companion-is-defect-velocity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["DerivativeCompanionVelocity.lean"],
        "missing_interfaces": ["holomorphic derivative bridge", "source-derived orientation sign"],
    },
    "theta-cubic-bilinear-companion.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "ValuationFiniteDifference.lean",
            "FiniteDifferenceCorrespondence.lean",
            "FiniteRefinementCorrespondence.lean",
        ],
        "missing_interfaces": [
            "positive bilinear theta kernel",
            "paired moment unit inequality",
            "regularized seam finite part",
        ],
    },
    "finite-group-norm-characteristic-dichotomy.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteGroupNormDichotomy.lean"],
        "missing_interfaces": [
            "finite-dimensional quotient rank and homology dimension",
            "physical relative-chain pushforward",
        ],
    },
    "integral-norm-homology-smith-form.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteGroupNormDichotomy.lean"],
        "missing_interfaces": [
            "integral augmentation basis",
            "unimodular basis change and Smith normal form",
            "base-change comparison",
        ],
    },
    "arbitrary-finite-surjection-conjugation-spectrum.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite-group extension and conjugation-image exponent",
            "twisted norm-word bijectivity",
            "split and nonsplit control fixtures",
        ],
    },
    "theta-anomaly-line-incidence-closes-but-rank-one-detection-is-unfaithful.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RankOneIncidenceFaithfulness.lean"],
        "missing_interfaces": [
            "finite labelled seam trace and cutoff inclusion specialization",
            "quotient-level induced map rather than scalar composite surjectivity",
            "finite Cauchy-jet or seam-germ faithfulness",
            "completion stability excluding normalized approximate-kernel sequences",
        ],
    },
    "li-rational-cone-endpoint-regularization-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["LiRationalSquareCone.lean"],
        "missing_interfaces": [
            "polynomial degree, endpoint valuation, and exact pole-order theorem",
            "typed meromorphic test algebra and endpoint principal parts",
            "one degree-compatible finite-part distribution preserving reflection",
            "agreement with Li derivatives and compatibility with polarization",
        ],
    },
    "theta-cubic-poisson-hermite-energy.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CubicHermiteResidual.lean"],
        "missing_interfaces": [
            "cubic Hermite matrix and principal-minor identities",
            "discriminant-to-Schur-complement normalization",
            "Poisson-completed carrier and simultaneous integration by parts",
            "theta moment positivity for the final exceptional residual",
        ],
    },
    "theta-cross-transfer-has-a-bordered-determinant-not-a-self-adjoint-pencil.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BorderedPencilSymmetrizer.lean"],
        "missing_interfaces": [
            "bordered determinant Schur-complement identity",
            "full two-port Weyl determinant and divisor-mismatch fixture",
            "chiral double with holomorphic-versus-real-analytic distinction",
            "relative determinant and nowhere-zero unit on the completed source",
        ],
    },
    "prime-oscillator-intertwiner-no-go.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite prime and oscillator diagonal generators",
            "matrix-coefficient consequence of the intertwining equation",
            "Lindemann--Weierstrass exclusion of log-prime/quarter-level coincidences",
            "typed non-diagonal kernel and commutator-defect completion interface",
        ],
    },
    "graded-residue-jet-polarization.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GradedResiduePolarization.lean"],
        "missing_interfaces": [
            "local Xi quotient and maximal-ideal associated graded",
            "complex Hermitian jet form and Weil degree-zero normalization",
            "completed direct sum and compact-resolvent diagonal operator",
            "regularized determinant identity conditional on divisor reality",
        ],
    },
    "relative-complement-incidence-factorization.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RelativeComplementFactorization.lean"],
        "missing_interfaces": [
            "normalized equal-fiber Hilbert incidence specialization",
            "source-derived signed analytic complementary weights",
            "oriented determinant-line torsion for rectangular complement maps",
            "cutoff-compatible archimedean moving boundary",
        ],
    },
    "equivariant-radical-repair-h1-obstruction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "group action on the radical-repair torsor and translation module",
            "canonical displacement one-cocycle modulo coboundaries",
            "equivariant fixed-point iff vanishing H1 class",
            "integral C2 sign-action hostile and localization after inverting two",
        ],
    },
    "fourier-dual-copy-difference-correspondence.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteDifferenceCorrespondence.lean"],
        "missing_interfaces": [
            "finite complex Hilbert spaces and normalized Fourier transform",
            "character orthogonality computation for the conjugation-copy map",
            "operator adjoint identity for unnormalized difference incidence",
            "arithmetic chain-to-divisor unitary bridge",
        ],
    },
    "prime-oscillator-semigroup-incidence-kernel.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeOscillatorIncidence.lean"],
        "missing_interfaces": [
            "prime logarithms and quarter-shift oscillator specialization",
            "infinite Hilbert--Schmidt estimates for incidence and commutator defect",
            "gamma resolvent and endpoint Schur complement",
            "recovery of the unsmoothed prime-power Green term",
        ],
    },
    "li-mobius-coordinate-rigidity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["LiMobiusRigidity.lean"],
        "missing_interfaces": [
            "reduction from a general four-coefficient Mobius transformation",
            "projective endpoint pole and infinity-value predicates",
            "critical-line to unit-circle mapping over the complex numbers",
            "transport of rigidity into the meromorphic rational-square test algebra",
        ],
    },
    "finite-p-group-norm-socle-homology.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteGroupNormDichotomy.lean"],
        "missing_interfaces": [
            "finite group algebra and left/right norm multiplication",
            "image as the invariant norm line and quotient homology dimension",
            "p-group cardinality vanishing in characteristic p",
            "socle and Jacobson-radical identifications plus multiple-fiber direct sums",
        ],
    },
    "paired-polarization-quarter-rotation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PolarizationQuarterTurn.lean"],
        "missing_interfaces": [
            "integral free-module/function-space delta-basis equivalence",
            "real exponential half-rotation and positive path",
            "metaplectic lift and oscillator-vacuum eighth phase",
            "source-derived boundary selection and determinant comparison",
        ],
    },
    "li-gns-multiplicity-obstruction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["MultiplicityAmplification.lean"],
        "missing_interfaces": [
            "finite atomic scalar moment functional and cyclic GNS construction",
            "identical moments for weighted scalar atom and repeated scalar copies",
            "eigenspace-dimension comparison for scalar and amplified models",
            "general integer fiber amplification compatible with the explicit formula",
        ],
    },
    "theta-reflection-hankel-determinant-no-go.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "theta Schwartz kernel and reflection-compressed half-line Hankel operator",
            "self-adjointness and membership in every Schatten class",
            "superpolynomial singular-value decay and reciprocal-zero counting bound",
            "comparison with the Riemann--von Mangoldt zero density under affine scaling",
        ],
    },
    "phase-i-unmarked-assembly-obstruction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["UnmarkedAssemblyObstruction.lean"],
        "missing_interfaces": [
            "full dihedral action extending the cyclic subgroup obstruction",
            "typed marked Carrier objects and connected sewing operation",
            "finite coproduct or additive completion alternative",
            "descent after forgetting a source-derived marking",
        ],
    },
    "newman-hermite-relative-entropy.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteHermiteEntropy.lean"],
        "missing_interfaces": [
            "Hermite root center, second moment, and discriminant formulas",
            "fixed-center fixed-radius Vandermonde extremal theorem and uniqueness",
            "backward-heat root dynamics and derivative identity",
            "infinite Xi-window renormalization and collision-limit control",
        ],
    },
    "theta-cubic-transition-divided-difference.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "completed theta source potential and score-stiffening density",
            "logarithmic divided-difference integral identity",
            "Prekopa preservation theorem with chamber support",
            "seam Taylor expansion proving immediate log-convexity and cross-block typing",
        ],
    },
    "theta-two-by-two-gram-transport-closure.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "weighted theta L2 space and multiplication by the even coordinate",
            "polynomial probes modulo almost-everywhere equality",
            "interval positivity implying polynomial identity from an a.e. relation",
            "linear independence of the full multiplication orbit and transport-closed span",
        ],
    },
    "newman-window-entropy-flux.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["NewmanWeylEntropyBalance.lean"],
        "missing_interfaces": [
            "distinct differentiable root paths and finite-window exterior force",
            "center and radius differentiation for the normalized discriminant",
            "identification of the abstract anomaly with omitted-root boundary flux",
            "canonical infinite-window counterterm or flux estimate",
        ],
    },
    "physical-paired-mackey-obstruction-tower.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RadicalRepairObstruction.lean"],
        "missing_interfaces": [
            "physical relative complexes, boundaries, orientations, and geometric quotient",
            "selector descent and degreewise coefficient--Betti adjunction",
            "repair torsor canonicity and equivariant H1 naturality obstruction",
            "stagewise composition law and Mackey pull--push normalization",
        ],
    },
    "section-torsor-shear-obstruction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["SectionTorsorShear.lean"],
        "missing_interfaces": [
            "finite cyclic prime controls and exact section/shear counts",
            "nonabelian derivation generalization",
            "source-derived marking selecting a torsor point",
            "physical chain lift and compatibility with resonance data",
        ],
    },
    "xi-hermitian-reflection-defect.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "typed nontrivial Xi zero multiset with multiplicities and quartet symmetry",
            "Riemann--von Mangoldt summability of the Hermitian defect",
            "nonnegative infinite-sum vanishing criterion",
            "source-side quadratic correspondence realizing the defect without assuming RH",
        ],
    },
    "two-ray-shell-schur-determinant-falsifier.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TwoRayShellSchurHostile.lean"],
        "missing_interfaces": [
            "unitary height-compression operator and constant/difference basis change",
            "operator-valued kernel Schur complement",
            "Hilbert--Schmidt leakage and regularized determinant typing",
            "source-derived oriented coefficient--Betti double",
        ],
    },
    "initial-semiring-frobenius-rigidity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["InitialSemiringFrobeniusRigidity.lean"],
        "missing_interfaces": [
            "conditional Carrier pi0 identification with the initial commutative semiring",
            "Frobenius congruence modulo each intrinsic prime",
            "prime-indexed enlargement such as symmetric powers or Witt objects",
            "cohomological realization and Euler-factor specialization",
        ],
    },
    "phase-i-connected-sewing-unit-obstruction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PhaseICarrierObstructions.lean"],
        "missing_interfaces": [
            "finite boundary-set pushout realizing the arity formula",
            "framed coefficient-line external product and primitive generator",
            "typed Carrier sewing bifunctor and object-level unit law",
            "authorization for adjoining an unstable two-point interface object",
        ],
    },
    "xi-complex-lattice-divergence-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ComplexLatticeDivergenceNoGo.lean"],
        "missing_interfaces": [
            "general open-mapping theorem exclusion for real-valued holomorphic maps",
            "branch-aware complex logarithm formulation on a connected domain",
            "finite pairwise Xi lattice aggregation",
            "source-derived phase-sensitive Hermitian reflection term",
        ],
    },
    "xi-conjugation-graph-correspondence.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteRefinementCorrespondence.lean"],
        "missing_interfaces": [
            "finite conjugation-stable divisor and graph projection",
            "complex multiplication kernel and graph-trace identity",
            "constant-size free conjugation-orbit specialization",
            "source-side projector and physical relative-chain pushforward",
        ],
    },
    "xi-weyl-multiplicity-repair.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["MultiplicityAmplification.lean"],
        "missing_interfaces": [
            "residue multiplicity extraction from the Xi logarithmic derivative",
            "arbitrary finite-dimensional semisimple fiber amplification",
            "completed self-adjoint direct sum and compact resolvent under RH",
            "regularized determinant and source-boundary realization",
        ],
    },
    "xi-spectral-copy-correspondence.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite atomic complex Hilbert space and conjugation antiunitary",
            "basis-copy isometry and graph-range projection identities",
            "trace cyclicity yielding the conjugation-graph kernel sum",
            "dagger-Frobenius atomic algebra and multiplicity-sensitive refinement",
        ],
    },
    "prime-pick-cutoff-antimonotonicity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PickCutoffAntimonotonicity.lean"],
        "missing_interfaces": [
            "complex finite prime-power Weyl function in the Euler half-plane",
            "Pick-kernel diagonal formula from the Weyl increment",
            "positive-kernel feature-extension theorem",
            "indefinite cutoff system with order-independent archimedean renormalization",
        ],
    },
    "mellin-source-ideal-saturation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["SourceIdealSaturation.lean"],
        "missing_interfaces": [
            "Hadamard ring of entire functions of order at most one",
            "Mellin source range and proof of polynomial-Xi divisibility",
            "localization at maximal ideals and local-length multiplicity",
            "associated-graded polarization and completed boundary construction",
        ],
    },
    "xi-weyl-lattice-fluctuation-entropy.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["WeylLatticeTangentDivergence.lean"],
        "missing_interfaces": [
            "Riemann--von Mangoldt flattening and midpoint zero-count identity",
            "finite log-Vandermonde ratio and Taylor expansion",
            "harmonic boundary-field coefficient formula",
            "symmetric-window renormalization and higher-order control",
        ],
    },
    "physical-readout-congruence.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "family of typed group representations and intersection of normal kernels",
            "commutator-subgroup intersection and quotient universal property",
            "separation from affine invariant-theory quotient",
            "sector fixtures including the radiative-memory D3 commutator detector",
        ],
    },
    "li-prime-transport-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "completed xi logarithmic derivative with coupled endpoint cancellations",
            "meromorphic rational-square residue functional",
            "contour shift from endpoints to an honest Euler half-plane",
            "von Mangoldt kernel, crossed residues, convergence, and reflection partner",
        ],
    },
    "Krein-graph-completion-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "Hilbert direct sum with signed Krein form",
            "bounded coupling graph and induced I-C-star-C form",
            "contractivity, strict positivity, and null-vector equivalences",
            "finite graph Gram determinant and holomorphic off-line family",
        ],
    },
    "resonance-localization-rigidity.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "basis linearization of a finite-set self-map over a commutative ring",
            "nonbijective map yielding repeated columns and a zero row",
            "persistence of noninvertibility under nonzero localization",
            "A4-to-C3 twisted-norm rank-one hostile over several characteristics",
        ],
    },
    "theta-radial-score-quartic-polarization.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RadialScoreQuartic.lean"],
        "missing_interfaces": [
            "completed theta source and derivative identification",
            "ordered four-copy expansion and symmetrized derivative placements",
            "pair-pair polarization formula",
            "reciprocal modular orientation or explicit negative reflected quadruple",
        ],
    },
    "theta-cubic-prime-route-cocycle.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RadialTranslationCocycle.lean"],
        "missing_interfaces": [
            "differentiable translated theta routes and radial-score operator identity",
            "mixed bilinear companion formula and two boundary currents",
            "based-score bundle and physical zero-fiber sewing",
            "modular seam extension and cancellation on the coefficient hyperplane",
        ],
    },
    "transfer-normalization-selector-nogo.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TransferNormalizationNoGo.lean"],
        "missing_interfaces": [
            "finite surjection pullback and fiber-sum transfer maps",
            "delta selector and identity-fiber specialization",
            "averaging projector onto fiber-constant functions",
            "C4-to-C2 rational coordinate fixture and geometrically weighted alternatives",
        ],
    },
    "two-height-pick-scalar-monotonicity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TwoHeightPickFactorization.lean"],
        "missing_interfaces": [
            "theta Laplace transform and logarithmic derivative",
            "positivity and strict monotonicity of the tilted mean",
            "ordered-real sign equivalence with monotonicity of a(y)/y",
            "large-tilt polygamma/Euler estimate and compact-interval certificate",
        ],
    },
    "li-mellin-prime-renormalization-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "piecewise inverse-Mellin principal-part kernels and reflection law",
            "Mellin transform in the fundamental strip",
            "von Mangoldt cutoff asymptotics for every jet index",
            "common gamma/prime/endpoint renormalized limit reproducing completed Xi jets",
        ],
    },
    "quarter-point-jacobi-blind-spectrum.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "exact certified four-by-four Jacobi matrix entries",
            "replayable eigenvalue interval enclosures",
            "interval-safe inverse coordinate transformation",
            "comparison bounds for the first predicted ordinate and order convergence",
        ],
    },
    "prime-valuation-phase-energy-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimePhaseEnergy.lean"],
        "missing_interfaces": [
            "infinite prime-power Dirichlet-chain energy derivation",
            "prime specialization radius p^(-1/2) and logarithmic phase",
            "heat-smoothed prime sum and absolute convergence",
            "two-prime logarithmic independence proving global vanishing only at zero",
        ],
    },
    "prime-diagonal-fredholm-determinant.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "intrinsic-prime l2 space and unbounded positive diagonal operator",
            "complex functional calculus for N^(-s) and trace-class criterion",
            "Fredholm determinant Euler product and logarithmic derivative",
            "trace-norm divergence boundary and holomorphic continuation obstruction",
        ],
    },
    "boundary-real-structure-phase-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BoundaryRealStructurePhaseNoGo.lean"],
        "missing_interfaces": [
            "first-order differential operator and self-adjoint extension domains",
            "antiunitary conjugation and reflected-conjugation actions on functions",
            "domain-invariance derivation of the scalar phase equations",
            "source-derived metaplectic, Maslov, or corner selector for the eighth phase",
        ],
    },
    "finite-norm-torsion-quadratic-exponential-no-go.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite based chain complexes over a rational-function field",
            "acyclic Reidemeister torsion as an alternating product of minors",
            "polynomial-degree proof that exp(plus-or-minus x-squared/2) is not rational",
            "regularized infinite-complex alternatives and quadratic anomaly coefficient",
        ],
    },
    "theta-null-mode-critical-renormalization.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "half-line theta precursor split into null mode and positive remainder",
            "cosh transforms, convergence strip, and entire continuation in the squared coordinate",
            "completion-factor cancellation to the endpoint constant one quarter",
            "threshold angular-current derivative and local Loewner positivity",
        ],
    },
    "theta-adelic-lattice-tangent-collapse.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "adeles, diagonal rational embedding, and discreteness proof",
            "ordinary tangent-cone functor and zero tangent of a discrete subgroup",
            "adelic Heisenberg bicharacter and rational maximal isotropy",
            "Weyl representation, maximal commuting algebra, and Cayley boundary relation",
        ],
    },
    "time-addition-reflection-positivity-stieltjes-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "Laplace--Stieltjes measure representation and differentiated kernel",
            "positive-semidefinite time-addition Gram kernels for arbitrary finite increments",
            "jet differentiation yielding both Hankel hierarchies",
            "converse moment reconstruction with half-plane holomorphy and Xi specialization",
        ],
    },
    "three-height-pick-correlation-triangle-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CorrelationTriangle.lean"],
        "missing_interfaces": [
            "theta-source construction of the three normalized correlations",
            "global correlation-triangle inequality for all positive heights",
            "confluent jet calculation connected to differentiable theta cumulants",
            "sixth-cumulant directed enclosures and positive-height interval certificate",
            "two-zone fourth-cumulant sign and compensation estimates",
        ],
    },
    "radical-repairs-form-hom-torsor.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RadicalRepairObstruction.lean", "RadicalRepairTorsor.lean"],
        "missing_interfaces": [
            "graded chain complexes and the degree-zero Hom differential",
            "typed inclusion of the physical pairing radical",
            "chain-homotopy quotient and H-zero of the Hom complex",
            "equivariant naturality and a source-derived normalization selecting a repair",
        ],
    },
    "quaternionic-square-forcing-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite-dimensional complex inner-product spaces and antiunitary operators",
            "Kramers orthogonality and even eigenspace multiplicity for square-minus-one symmetry",
            "Moore determinant and its square relation to the complex determinant",
            "analytic eigenvalue branches and zero-order divisibility under positivity",
            "source-derived cutoff-compatible quaternionic structure",
        ],
    },
    "quarter-point-multiplicity-interval-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "monic orthogonal polynomials and certified positive squared norms",
            "Christoffel formula for Gaussian quadrature weights",
            "replayable outward evaluation at an interval-valued top node",
            "sound interval division for the residue estimator",
            "typed separation between finite mass estimate, limiting divisor multiplicity, and eigenspace dimension",
        ],
    },
    "eta-naive-tail-certification-no-go.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "real logarithm monotonicity for log(n)^j/n beyond exp(j)",
            "alternating-series remainder theorem instantiated at derivative orders zero through four",
            "exact integer cutoff witnesses for the 10^-12 threshold",
            "replayable replacement of approximate floating cutoffs by directed bounds",
            "accelerated Euler--Maclaurin remainder interface for a usable certifier",
        ],
    },
    "boundary-commutator-basis-invariance.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BoundaryCommutatorInvariant.lean"],
        "missing_interfaces": [
            "matrix-coordinate equivalence with the source-labelled Betti complexes",
            "rank preservation under invertible row and column transformations",
            "integral Smith invariant-factor preservation under unimodular transformations",
            "physical construction of the pairing-forced comparison map",
        ],
    },
    "arbitrary-finite-kernel-monodromy-spectrum.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite-group exponent and the power-map permutation iff theorem",
            "semidirect product by the cyclic subgroup generated by an automorphism",
            "identification of a power-map restriction with the twisted word map on a fiber",
            "Cauchy extraction of prime-order visible monodromy",
            "nonabelian telescoping identity for x-inverse times alpha(x)",
            "basis-level fiber-sum and fiber-lift correspondence typing",
        ],
    },
    "elementary-abelian-p-norm-homology.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteGroupNormDichotomy.lean"],
        "missing_interfaces": [
            "group-algebra equivalence with the truncated polynomial algebra",
            "coordinate-kernel norm as the top socle monomial",
            "kernel modulo image computation for multiplication by that monomial",
            "graded Hilbert-series and Loewy-length calculations",
            "dimension formula p^(n-k) times (p^k-2)",
            "physical relative-chain realization, which the packet does not assert",
        ],
    },
    "canonical-half-line-antipode-is-source-fixed-but-universal.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HalfLineAntipode.lean"],
        "missing_interfaces": [
            "entire half-line transform from super-exponential source decay",
            "source-derived equal-coefficient frame from oriented contour splitting",
            "even-source reciprocity and imaginary-axis conjugacy",
            "explicit off-axis zeros of the modulated Gaussian hostile",
            "labelled theta route packet and modular exclusion theorem",
        ],
    },
    "critical-line-scattering-phase-collapse.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ReciprocalPhaseCollapse.lean"],
        "missing_interfaces": [
            "gamma and zeta meromorphic functions with the completed functional equation",
            "critical-line reflection identification and nonzero honest domain",
            "removable-singularity extension of the reciprocal product across zeros",
            "Fredholm determinant origin of the prime phase",
            "operator-domain defect retaining amplitude multiplicity",
        ],
    },
    "endpoint-zeta-pole-acyclic-mapping-cone.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["EndpointPoleCancellation.lean"],
        "missing_interfaces": [
            "Laurent expansion of the zeta logarithmic derivative at one",
            "gamma-pole cancellation in the reflected chart",
            "squared-coordinate branch identification at x equals one quarter",
            "typed chain complex and mapping-cone homology rather than the identity-map core",
            "positivity of the reduced completed time-addition kernel",
        ],
    },
    "arithmetic-sector-conventions.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "coefficient-neutral Carrier category with finite coproduct and symmetric monoidal product",
            "distributivity and pi-zero quotient yielding a commutative semiring",
            "group completion universal property carrying multiplication",
            "occurrence-resolved and occurrence-forgotten integral boundary matrices",
            "Smith computations under primitive and quarter-enlarged coefficient lattices",
            "typed separation of Carrier, coefficient lens, and readout authority",
        ],
    },
    "forced-betti-boundary-commutator.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BoundaryCommutatorInvariant.lean"],
        "missing_interfaces": [
            "perfect chain-level pairings and construction of the unique adjoint Betti candidate",
            "graded Stokes adjointness including the convention-fixed sign",
            "transpose identification with the coefficient cochain-map defect",
            "the named C4-to-C2 hostile matrices and five-site relative boundaries",
        ],
    },
    "integral-mackey-trace-smith-criterion.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ScalarIntegralTrace.lean"],
        "missing_interfaces": [
            "Smith normal form for arbitrary rectangular integer matrices",
            "full-row-rank equivalence with a finite-index image",
            "cokernel killed-by-d equivalence with all Smith factors dividing d",
            "least norm scalar as the lcm of the nonzero invariant factors",
            "affine solution classification by maps into the matrix kernel",
        ],
    },
    "five-site-branch-chain-lift-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "frozen 32-to-16 sheet census as exact finite Lean data",
            "relative-chain source and branch target with positive integral multiplicities",
            "pairing adjunction distinguishing multiplicity one from multiplicity two",
            "map of relative pairs, boundary compatibility, and endpoint normalization",
            "source authority for the physical adjunction rather than its circular assumption",
        ],
    },
    "five-site-integral-adams-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CyclicAdamsSpectrum.lean"],
        "missing_interfaces": [
            "integral group ring of the five-fold elementary two-group",
            "special lambda-ring and Adams ring-endomorphism construction",
            "composition and Frobenius congruence for arbitrary group-ring elements",
            "dual coefficient-function pullback and selected delta fixture",
            "exact mismatch count separating algebraic Adams operations from physical readout",
        ],
    },
    "five-site-physical-deck-transfer-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteRefinementCorrespondence.lean"],
        "missing_interfaces": [
            "five-fold elementary two-group and its 32 sheet basis",
            "Kronecker coefficient--Betti pairing and simultaneous deck invariance",
            "selected chamber chain versus orbit trace and normalized average",
            "exact 31- and 32-mismatch counts",
            "source-derived geometric map, relative-cycle Gysin trace, and normalization",
        ],
    },
    "gaussian-norm-two-half-rotation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PolarizationQuarterTurn.lean", "GaussianNormTwo.lean"],
        "missing_interfaces": [
            "Smith normal form and cokernel identification as Z modulo 2",
            "Gaussian-integer module structure on the full paired lattice",
            "real scalar extension and normalization by square root of two",
            "exponential half-rotation and metaplectic phase identification",
            "source-derived physical relative-chain and boundary realization",
        ],
    },
    "archimedean-confinement-odd-arithmetic-coupling.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "densely defined self-adjoint operators and relative boundedness below one",
            "Kato--Rellich self-adjointness theorem",
            "compact-resolvent preservation through the resolvent identity",
            "skew-adjoint multiplication by i and discrete spectral consequences",
            "phase-space area integration and boundary correction",
            "source-derived archimedean operator and symmetric prime interaction",
        ],
    },
    "energy-dependent-boundary-linearity-gate.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": [],
        "missing_interfaces": [
            "closed operators with fixed versus spectral-parameter-dependent domains",
            "nonlinear operator-pencil typing",
            "boundary triples and operator-valued Nevanlinna Weyl functions",
            "regularized characteristic determinants and zero multiplicities",
            "affine identification of the real spectral axis with the critical line",
            "source-derived positive measure, compact-resolvent linearization, and xi determinant",
        ],
    },
    "deck-norm-bad-prime-locus.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteGroupNormDichotomy.lean"],
        "missing_interfaces": [
            "integral regular group lattice and base change to localizations of the integers",
            "proof that no integral scalar multiple normalizes a nontrivial norm",
            "scheme-theoretic support as V of the group order",
            "nonzero norm after reduction at every prime divisor",
            "physical relative-chain pushforward, which the packet explicitly withholds",
        ],
    },
    "norm-detection-of-invariant-boundary-defects.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TraceRangeDetection.lean"],
        "missing_interfaces": [
            "chain-complex grading and boundary-defect image submodules",
            "quotient-tower transport and separated-support hypotheses",
            "surjectivity at the preceding quotient stage",
            "source-derived physical trace and pushforward maps",
        ],
    },
    "finite-symmetry-averaging-radical-repair.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["RadicalRepairTorsor.lean"],
        "missing_interfaces": [
            "finite group affine action on the repair torsor",
            "coefficient ring with invertible group order and affine averaging",
            "invariance of the repair equation, radical, and pairings under the action",
            "fixed-point torsor under invariant closed corrections",
            "group-cohomology H-one interpretation and integral bad-prime fixture",
        ],
    },
    "homology-descent-weaker-than-chain-map.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["BoundaryCommutatorInvariant.lean"],
        "missing_interfaces": [
            "graded chain complexes with cycle and boundary submodules",
            "construction of an induced quotient map from the two containment conditions",
            "necessity and sufficiency proof degree by degree",
            "the two-term diagonal integer hostile and its induced identity on homology",
            "physical distinction between a class readout and chain-level Gysin composition",
        ],
    },
    "coprime-adams-tensor-gluing-theorem.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite prime-indexed exponent vectors and product correlation kernel",
            "positive semidefiniteness of geometric Toeplitz blocks and Kronecker products",
            "four-point mixed-prime determinant and eigenvalue calculation",
            "exact one-prime Adams composition and coprime Mackey interchange",
            "actual completed Weil correlations including gamma and endpoint coupling",
            "contractive completion defect controlling mixed-prime holonomy",
        ],
    },
    "norm-resonance-prime-trichotomy.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["NormResonanceTrichotomy.lean"],
        "missing_interfaces": [
            "finite-group derivation that radical degree support divides the resonance label",
            "localization semantics connecting degree divisibility to scalar units",
            "power--Mackey obstruction semantics connecting resonance divisibility to failure",
            "A4-to-C3 action computation beyond the numerical bidegree fixture",
            "physical relative-chain transfer, which localization cannot manufacture",
        ],
    },
    "norm-splitting-versus-defect-detection-regimes.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TraceRangeDetection.lean", "FiniteGroupNormDichotomy.lean"],
        "missing_interfaces": [
            "module-theoretic scalar splitting from an inverse of the degree",
            "proof that regular nonunits admit detection but no scalar splitting",
            "uniform specialization to integers, localizations, and prime fields",
            "five-site power-of-two kernel orders and stagewise trace maps",
            "source-derived physical chain maps",
        ],
    },
    "norm-resonance-bidegree.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteRefinementCorrespondence.lean"],
        "missing_interfaces": [
            "finite-group surjections, kernels, exponents, and visible action images",
            "multiplicativity of kernel cardinality under composable surjections",
            "lcm composition theorem for resonance labels",
            "prime-support inclusion from kernel order to exponent",
            "A4, V4, and C3 group-action fixtures with exact bidegrees",
            "physical Betti pull--push, which the coefficient norm does not supply",
        ],
    },
    "normal-kernel-join-resonance-lcm.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "normal subgroup join as the product KL in a finite group",
            "prime support of finite-group exponents and orders",
            "restriction homomorphism from the join action image to the two factor images",
            "injectivity and surjectivity properties of the action projections",
            "radical-product to lcm identity and survivor-set intersection",
            "S3 times C5 nonabelian control",
        ],
    },
    "perfect-pairing-forces-betti-pushforward.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PerfectPairingAdjointUnique.lean"],
        "missing_interfaces": [
            "linear finite-free coefficient and Betti modules with perfect pairings",
            "deck-labelled dual bases and the forced basis-map formula",
            "matrix transpose construction of the adjoint",
            "degree norm for named quotient fixtures",
            "relative-boundary, support, and geometric realization of the forced assignment",
        ],
    },
    "paired-coefficient-betti-symplectic-double.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PolarizationQuarterTurn.lean", "PerfectPairingAdjointUnique.lean"],
        "missing_interfaces": [
            "arbitrary perfect bilinear pairing rather than the finite evaluation fixture",
            "nondegeneracy and complementary Lagrangian proofs over finite free integer modules",
            "integral Heisenberg central extension",
            "radical quotient for degenerate physical pairings",
            "archimedean central character, Hilbert representation, positivity, and quantization",
        ],
    },
    "paired-deck-mackey-norm.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "FiniteRefinementCorrespondence.lean",
            "FiniteGroupNormDichotomy.lean",
            "PerfectPairingAdjointUnique.lean",
        ],
        "missing_interfaces": [
            "paired finite-set coefficient and free Betti modules with both adjunctions",
            "Beck--Chevalley squares for finite pullbacks",
            "upstairs kernel-norm action on both legs",
            "integral selector-normalization hostile for arbitrary nontrivial kernels",
            "source-derived physical relative-chain pushforward",
        ],
    },
    "nonabelian-terminal-kernel-power-spectrum.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite-group exponent and modular inverse exponentiation",
            "proof that coprime power maps on arbitrary finite groups are mutual inverses",
            "Cauchy theorem extracting a prime-order collision in the converse",
            "fiber-sum and basis-lift compatibility for the terminal quotient",
            "S3 and quaternion-group exact controls",
        ],
    },
    "nonabelian-twisted-norm-mackey-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite group surjection and coset-fiber decomposition",
            "equivalence between fiber-sum commutation and fiberwise bijectivity",
            "nonabelian twisted word map from unique coset factorization",
            "S3-to-C2 transposition-square hostile",
            "abelian C6-to-C2 control separating conjugation from kernel exponent",
        ],
    },
    "primary-filtration-is-not-frobenius.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "primary subgroups of finite integer modules without chosen CRT splitting",
            "scalar multiplication filtration on powers of cyclic p-groups",
            "kernel, image, nilpotence, and successive-layer calculations",
            "comparison with Adams operations and absolute Frobenius",
            "typed criterion separating scalar nilpotence from geometric Frobenius data",
        ],
    },
    "five-site-unit-sieve-physical-activation-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CyclicAdamsSpectrum.lean", "FiberSelectorDescent.lean"],
        "missing_interfaces": [
            "five-fold elementary two-group and all 31 nontrivial branch quotients",
            "frozen delta-zero selector on the exact sheet basis",
            "odd-index Mackey compatibility for every branch kernel",
            "exact 372-compatible and zero-joint-pass census",
            "source-derived physical relative-chain pushforward",
        ],
    },
    "five-site-boundary-matrix-availability-audit.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BoundaryCommutatorInvariant.lean", "PerfectPairingAdjointUnique.lean"],
        "missing_interfaces": [
            "source-derived based relative chain groups in adjacent degrees",
            "signed source and target boundary matrices",
            "coefficient pullback or pairing-adjoint Betti matrices",
            "basis comparison fixing orientations and endpoint normalization",
            "the actual five-site packet, which the inventory reports unavailable",
        ],
    },
    "five-site-mod2-branch-norm-composition.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "five-generator square-zero commutative algebra over ZMod 2",
            "branch norms indexed by nonempty finite subsets",
            "disjoint-union product and overlap-zero theorem",
            "permutation independence and repeated-direction annihilation",
            "exact ordered-pair and flag-profile census",
            "separate geometric-support interface preventing formal activation",
        ],
    },
    "five-site-mod2-branch-norm-filtration.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteGroupNormDichotomy.lean"],
        "missing_interfaces": [
            "group-algebra equivalence with the five-variable square-zero quotient",
            "kernel norm as the subset monomial",
            "nonzero homogeneous-degree and generator-annihilator proofs",
            "Boolean degree profile 5,10,10,5,1",
            "Loewy filtration and separate geometric branch-locus census",
        ],
    },
    "five-site-mod2-frobenius-collapse.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "the five-variable square-zero algebra over ZMod 2",
            "absolute Frobenius as a ring endomorphism",
            "cross-term cancellation and basis-square calculation",
            "identification with augmentation followed by constant inclusion",
            "dimension-one image and 31-dimensional augmentation-ideal kernel",
            "typed separation from geometric Frobenius and Euler data",
        ],
    },
    "selector-data-processing-resonance.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["SelectorDataProcessing.lean"],
        "missing_interfaces": [
            "finite-group right stabilizer as a subgroup",
            "normal-core monotonicity under stabilizer inclusion",
            "resonance-label divisibility and survivor-spectrum antitonicity",
            "injectivity restricted only to the selector image",
            "strict C6 labelled/parity/constant chain",
        ],
    },
    "selected-cocycle-annihilation-readout-descent.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["SelectedCocycleDescent.lean"],
        "missing_interfaces": [
            "graded chain complexes and homology quotient construction",
            "pairing interpretation of the additive scalar readout",
            "strict integer two-complex hostile with nonzero descended readout",
            "comparison to the stronger full homology-map conditions",
            "five-site boundary matrices and frozen selector contraction",
        ],
    },
    "selector-normal-core-terminal-spectrum.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiberSelectorDescent.lean"],
        "missing_interfaces": [
            "finite-group selector stabilizer and normal core",
            "largest-normal-subgroup universal property",
            "equivalence between quotient descent and kernel containment",
            "resonance monotonicity and intersection of admitted spectra",
            "S3 nonnormal transposition-subgroup hostile",
        ],
    },
    "selector-core-complete-quotient-arithmetic-invariant.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiberSelectorDescent.lean"],
        "missing_interfaces": [
            "normal-core classification of all admissible normal kernels",
            "extensional equality of kernel down-sets iff cores agree",
            "transport to decorated quotient lattices and terminal spectra",
            "S3 fully-labelled versus right-coset selector enumeration",
            "explicit proof that equal quotient behavior does not identify selectors",
        ],
    },
    "selector-admissible-resonance-lattice.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiberSelectorDescent.lean", "NormResonanceTrichotomy.lean"],
        "missing_interfaces": [
            "lattice of normal subgroups contained in a selector stabilizer",
            "conjugation action images and resonance decoration",
            "restriction-surjection proof under kernel inclusion",
            "contravariant monotonicity of compatible operation monoids",
            "five-site identity, hyperplane, and constant-selector specializations",
        ],
    },
    "iterated-selector-pullback-resonance.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["SelectorDataProcessing.lean"],
        "missing_interfaces": [
            "composable finite-group surjections and selector pullbacks",
            "preimage resonance theorem for kernels and terminal selector cores",
            "lcm formula across both quotient stages",
            "survivor-spectrum intersection and path independence",
            "strict C12-to-C6-to-C2 control through index 24",
        ],
    },
    "minimal-localization-for-integral-adjoint.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ScalarIntegralTrace.lean", "PerfectPairingAdjointUnique.lean"],
        "missing_interfaces": [
            "Smith normal form with transformed adjunction right-hand side",
            "reduced denominator d_i divided by gcd(d_i,B'_ij)",
            "finite lcm minimality across all matrix entries",
            "localization of the integers and prime-support iff theorem",
            "degreewise physical pairing packet",
        ],
    },
    "radical-resonance-unit-sieve.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CyclicAdamsSpectrum.lean", "NormResonanceTrichotomy.lean"],
        "missing_interfaces": [
            "arbitrary finite-kernel and conjugation-image resonance theorem",
            "radical squarefree modulus and unit-group residue classes",
            "Euler totient count and natural-density proof",
            "the four named nonabelian finite-group examples",
            "typed separation from Euler products and geometric Frobenius",
        ],
    },
    "paired-mackey-five-certificate-stack.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "FiberSelectorDescent.lean",
            "CyclicAdamsSpectrum.lean",
            "TransferNormalizationNoGo.lean",
            "SectionTorsorShear.lean",
            "BoundaryCommutatorInvariant.lean",
        ],
        "missing_interfaces": [
            "one indexed record joining the five independently typed certificates",
            "general finite-group resonance rather than cyclic controls",
            "automorphism action on actual section torsors",
            "source-derived five-site relative-chain pushforward and pairing square",
            "proof fixtures for A4, C4, and the split C2-by-C2 extension",
        ],
    },
    "resonance-enriched-surjection-category.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "category of finite-group surjections and kernel composition",
            "resonance cost as a squarefree divisibility-semilattice enrichment",
            "lcm composition and identity laws",
            "selector object costs and pullback combination",
            "C60-to-C30-to-C6 exact control",
            "separate absent covariant relative-chain functor",
        ],
    },
    "resonance-meet-defect.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite normal-subgroup intersection and join lattice",
            "resonance monotonicity under inclusion",
            "gcd upper bound for intersections and lcm equality for joins",
            "survivor-set union inclusion",
            "Klein-four coordinate-subgroup strict hostile",
        ],
    },
    "norm-module-euler-determinant-obstruction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "torsion norm module H_d and proof that rationalization is zero",
            "determinant convention on the zero-dimensional rational space",
            "primary filtration and associated graded over finite fields",
            "nilpotence of intrinsic multiplication-by-p on the graded module",
            "determinant of one minus a nilpotent operator",
            "typed absence of a source-selected Frobenius index",
        ],
    },
    "odd-source-skew-adjoint-vanishing-mechanism.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["OddInvolutionKernel.lean"],
        "missing_interfaces": [
            "locally compact abelian group convolution and involutive domains",
            "densely defined closed convolution operator and adjoint formula",
            "unitary Fourier transform and imaginary multiplier conclusion",
            "bounded transform of an unbounded skew-adjoint operator",
            "arithmetic logarithmic cocycle transport, confinement, and Xi spectral identification",
        ],
    },
    "quadratic-prime-channel-mackey-anomaly.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "CyclicAdamsSpectrum.lean",
            "TransferNormalizationNoGo.lean",
            "TwoPeriodicNormComplex.lean",
        ],
        "missing_interfaces": [
            "finite-cutoff prime propagation operator and trace-square identity",
            "explicit C2 coefficient fiber-sum square with selected delta",
            "graded analytic two-channel complex",
            "logarithmic torsion matching one-half trace of the square",
            "archimedean pairing and source-derived physical realization",
        ],
    },
    "mod2-norm-homology-hilbert-series.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "five-variable square-zero graded algebra over ZMod 2",
            "multiplication differential by a branch subset monomial",
            "explicit kernel/image quotient basis",
            "graded Hilbert-series calculation and evaluation at one",
            "controls at branch sizes one, two, and five",
            "separate physical filtration comparison",
        ],
    },
    "mod2-norm-homology-loewy-module.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "augmentation ideal and top socle in the square-zero branch algebra",
            "canonical homology equivalence with ideal modulo socle tensor spectators",
            "Loewy filtration and length proof",
            "binomial-rank successive layers",
            "zero and semisimple small-rank controls",
        ],
    },
    "quaternion-monodromy-twisted-power-spectrum.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite semidirect products and exponent bound for the total group",
            "global and quotient power-map permutation theorems",
            "restriction of a power permutation to corresponding fibers",
            "Q8 with the cyclic C3 automorphism action",
            "exhaustive twisted spectrum control and separation from the unproved general converse",
        ],
    },
    "one-prime-adams-tower-positive-gluing-theorem.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": [],
        "missing_interfaces": [
            "arbitrary-size geometric Toeplitz correlation matrices",
            "positive semidefiniteness for absolute correlation at most one",
            "positive definiteness and determinant formula in the strict case",
            "autoregressive Gram realization or Schur recursion",
            "source proof that prime-power Weil correlations obey exact Adams composition",
            "mixed-prime coherence beyond the one-prime tower",
        ],
    },
    "selector-stabilizer-maximal-quotient.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiberSelectorDescent.lean", "SelectorDataProcessing.lean"],
        "missing_interfaces": [
            "finite-group right stabilizer as a subgroup",
            "quotient by a normal subgroup and descent iff kernel containment",
            "largest normal admissible kernel when the stabilizer is nonnormal",
            "five-site delta, constant, and hyperplane selector calculations",
            "separate power--Mackey gate and absent physical Betti transfer",
        ],
    },
    "source-norm-quasi-idempotent.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TwoPeriodicNormComplex.lean", "TraceRangeDetection.lean"],
        "missing_interfaces": [
            "source norm as the composite T S of supplied module maps",
            "localized splitting onto image T along kernel S",
            "integral kernel and finite-index image refinements",
            "explicit one-bit two-by-two matrix over integers and ZMod 2",
            "physical source-chain maps",
        ],
    },
    "separated-support-boundary-defect-detection.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["SeparatedImageCancellation.lean", "OperatorTransportSquare.lean"],
        "missing_interfaces": [
            "graded composite boundary-defect formula",
            "source-labelled support submodules for the two transported terms",
            "surjectivity recovery of the later untransported defect",
            "relative injectivity on the earlier defect image",
            "five-site rank-decreasing branch maps",
        ],
    },
    "selector-surjective-pullback-core-base-change.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiberSelectorDescent.lean"],
        "missing_interfaces": [
            "surjective finite-group homomorphism and selector pullback",
            "stabilizer preimage equality using surjectivity",
            "normal-core commutation with subgroup preimage",
            "terminal-kernel base-change theorem",
            "C4-to-C2 delta-indicator and spectrum control",
        ],
    },
    "semidirect-linear-norm-adams-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "finite vector spaces and cyclic semidirect products",
            "geometric-sum linear part of a fiber power map",
            "fiber compatibility iff invertibility of that linear norm",
            "order-three matrix over ZMod 2 and A4 identification",
            "direct-product control and exhaustive fiber comparison",
        ],
    },
    "surjective-preimage-resonance-lcm.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "preimage of a normal subgroup under a finite-group surjection",
            "prime-support exact sequence for the preimage",
            "conjugation-image map with extension-derivation kernel",
            "center-valued derivation prime bound",
            "lcm and survivor-intersection theorem plus both finite controls",
        ],
    },
    "visible-monodromy-exponent-adams-spectrum.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "elementary-abelian finite kernel and possibly nonfaithful action",
            "factorization through the visible quotient action image",
            "fiber-linear norm dependence only on the visible action",
            "iff power compatibility theorem with p times image exponent",
            "C15-through-C3 and trivial C3 action hostile controls",
        ],
    },
    "small-nonabelian-monodromy-converse-sweep.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "exact finite models of S3, D8, and Q8 automorphism groups",
            "cyclic semidirect product construction for every automorphism",
            "decidable exhaustive fiber-bijectivity test through index twelve",
            "replayable certificate for the complete 38-automorphism census",
            "explicit scope marker separating bounded evidence from the general converse",
        ],
    },
    "edgewise-weil-contractions-do-not-glue-triangles.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CorrelationTriangle.lean"],
        "missing_interfaces": [
            "normalized completed-Weil short-support blocks",
            "prime and prime-square cross-correlation construction",
            "source-derived Adams composition or positive dilation",
            "mixed-prime cycle coherence",
            "finite analytic certificate for the actual prime-two triangle",
        ],
    },
    "phase-i-monoidal-additive-completion.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PhaseICarrierObstructions.lean", "InitialSemiringFrobeniusRigidity.lean"],
        "missing_interfaces": [
            "surface groupoid generated by a connected marked object under geometric disjoint union",
            "component-count normal form and its universal property",
            "intrinsic pair-quotient group completion",
            "source authorization for replacing categorical coproduct by monoidal disjoint union",
            "second distributive monoidal product on the Carrier",
        ],
    },
    "phase-i-three-level-reconciliation-audit.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "PhaseICarrierObstructions.lean",
            "InitialSemiringFrobeniusRigidity.lean",
            "UnmarkedAssemblyObstruction.lean",
        ],
        "missing_interfaces": [
            "typed separation of full Carrier, conditional pi-zero, and abelianized rig levels",
            "endomorphism construction of multiplication on the free pointed commutative monoid",
            "D4 abelianization and labelled finite-component rig groupoid",
            "physical authorization test using a higher-dimensional nonabelian invariant",
            "Burnside--Witt, Frobenius, spectrum, and Euler-product interfaces",
        ],
    },
    "weighted-coefficient-betti-mackey-adjunction-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["WeightedFiberBalance.lean", "PerfectPairingAdjointUnique.lean"],
        "missing_interfaces": [
            "finite weighted complex Hilbert spaces with positive weights",
            "Hilbert adjoint formula for pullback over arbitrary fibers",
            "diagonal weighted degree and fiber-balance iff theorem",
            "reciprocal dual Betti weights and algebraic pairing comparison",
            "von Mangoldt metric descent or measured-groupoid replacement",
        ],
    },
    "symmetric-power-decategorization-collapse.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["InitialSemiringFrobeniusRigidity.lean"],
        "missing_interfaces": [
            "D4-abelianized labelled finite-set rig groupoid",
            "exterior subsets and symmetric multisets as functorial power operations",
            "decategorified binomial generating series",
            "lambda-ring derivation that every Adams operation on component count is identity",
            "wreath-product stabilizers and any Burnside--Witt trace operations",
        ],
    },
    "formal-deck-degree-versus-geometric-branch-support.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "five-variable formal deck algebra and Boolean degree profile",
            "source branch equations and affine-linear difference rank",
            "generic support dimension and real positive-chamber disjointness",
            "Gram discriminant and fifth-point support equations",
            "rank-two affine-consistency Kummer line and even pairing",
            "typed separation of coefficient grade from geometric codimension",
        ],
    },
    "global-zeta-spectrum-typing-obstruction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "local norm modules and proof that every admitted determinant factor is one",
            "infinite Euler product of constant local factors",
            "typed inventory of intrinsic closed points, Frobenius, grading, and signs",
            "restricted product or trace-class global operator",
            "archimedean duality and completed determinant identity",
            "source-derived global operator falsifier without inserted prime labels",
        ],
    },
    "two-channel-cycle-interference-target.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TwoChannelInterference.lean"],
        "missing_interfaces": [
            "height-dependent complex or Hermitian source entries",
            "chiral self-adjoint lift and Gram determinant multiplicity",
            "source-derived independent arithmetic and archimedean routes",
            "noncircular normalization excluding Xi and its zero set",
            "operator-valued extension with determinant-class scalarization",
        ],
    },
    "euler-ray-adjacency-resummation-and-zero-phase-divergence.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GeometricSumSpectrum.lean"],
        "missing_interfaces": [
            "infinite complex geometric series with radius p to minus one half",
            "real-part rational resummation and monotonicity in cosine",
            "extremum formulas at zero and pi",
            "prime-power cutoff Fourier multiplier and norm attainment",
            "divergence of the zero-phase prime subseries",
            "common quadratic-form or relative-resolvent completion",
        ],
    },
    "von-mangoldt-support-falsifies-arithmetic-tensor-interchange.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["MixedPrimeRectangleParity.lean"],
        "missing_interfaces": [
            "von Mangoldt function and prime-power support theorem",
            "positive weights at distinct primes and vanishing at their product",
            "translation from arithmetic support to completed Weil rectangle edges",
            "gamma or endpoint Schur completion preserving the missing direct edge",
            "source-derived contractive Mackey dilation without inserting a mixed atom",
        ],
    },
    "two-prime-mechanisms-audit.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["InitialSemiringFrobeniusRigidity.lean", "FiniteGroupNormDichotomy.lean"],
        "missing_interfaces": [
            "conditional pointed pi-zero construction and intrinsic prime factorization",
            "regular-fiber norm homology H_d with support classification",
            "degree functor identifying a correspondence with the same component class dU",
            "localized nonzero iff divisibility bridge and the d equals two exception",
            "functorial Frobenius attached to intrinsic prime elements",
        ],
    },
    "growing-shell-rank-summability-schedule.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "Taylor remainder bound for polynomial projection on a bounded coordinate",
            "ceil-log-log over log-log-log rank schedule",
            "Stirling asymptotics uniform on compact height sets",
            "summability with fixed derivative losses",
            "distinction between source-vector leakage and full operator leakage",
            "varying-fiber weighted Mackey maps and Schatten/determinant control",
        ],
    },
    "prime-gamma-rank-trace-incompatibility.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "prime-counting and oscillator covariance asymptotics",
            "finite-rank support projections for the two cutoff models",
            "Hilbert--Schmidt projection-distance lower bound by rank difference",
            "divergence under the two incompatible cutoff schedules",
            "Shale--Stinespring or quasi-free equivalence typing",
            "weighted many-to-one replacement preserving the gamma determinant",
        ],
    },
    "two-channel-operator-valued-type-correction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["TwoChannelInterference.lean"],
        "missing_interfaces": [
            "finite conjugation-stable divisor truncations and graph permutation matrices",
            "rank bound for a sum of separable scalar channels",
            "growing internal correspondence modules",
            "two-by-two matrices over a noncommutative operator algebra",
            "valid determinant, Fredholm determinant, or graded torsion scalarization",
            "source copy correspondence independent of the Xi zero basis",
        ],
    },
    "valuation-normalization-derives-von-mangoldt-metric.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["WeightedFiberBalance.lean"],
        "missing_interfaces": [
            "prime-power exponent chains and logarithmic first-difference theorem",
            "valuation-coordinate scaling and pullback of the Euclidean metric",
            "von Mangoldt unit norm and infinite geometric exponent sum",
            "prime-sum logarithmic divergence and finite-part comparison",
            "colored Mackey fibers with dual Betti rescaling",
            "incomplete tensor product and relative covariance completion",
        ],
    },
    "theta-cubic-primitive-scale-susceptibility.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimitiveScaleSusceptibility.lean"],
        "missing_interfaces": [
            "completed theta moments and cubic residual definition",
            "two-scale reciprocal source mixture and differentiation in its weight",
            "derivation of the susceptibility polynomial from moment transport",
            "classification of the full negative-response scale region",
            "nonlinear primitive lattice or heat-equation constraint excluding independent scale weights",
        ],
    },
    "theta-curvature-programme-index.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "RadialScoreQuartic.lean",
            "RadialTranslationCocycle.lean",
            "CorrelationTriangle.lean",
            "PrimitiveScaleSusceptibility.lean",
        ],
        "missing_interfaces": [
            "artifact-by-artifact reconciliation of every theorem linked by the live index",
            "completed theta source and moment/cumulant analytic library",
            "directed interval and tail certificate replay",
            "operator, determinant-line, Grassmannian, and Fock interfaces",
            "all RH-equivalent positivity and faithfulness gates, which remain unproved",
        ],
    },
    "theta-dilation-module-fails-at-arithmetic-diagonal-sampling.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteRefinementCorrespondence.lean"],
        "missing_interfaces": [
            "Haar L2 radial dilation representation",
            "label and centered-difference fiber modules",
            "arithmetic diagonal evaluation and comparison with Haar matrix coefficients",
            "sampling correspondence between positive reals and integer factor pairs",
            "multiplicity-sensitive product fibers including the four factorizations of six",
        ],
    },
    "adams-boundary-relative-finite-part-regulator-invariance.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "prime harmonic asymptotic with the Meissel--Mertens constant",
            "prime-zeta Abel asymptotic and Euler-constant shift",
            "shifted harmonic oscillator sharp and exponential cutoff asymptotics",
            "digamma value at one quarter",
            "common-regulator relative finite-part theorem",
            "nonzero-height reflection-compatible family",
        ],
    },
    "sector-indexed-invariant-record-algebras.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "sector-indexed heterogeneous invariant-record object",
            "sourced equivariant constructors and contravariant algebra pullback",
            "closure on proper observable subalgebras and physical-selection transport",
            "support, chain, framing, and coherence resource transport",
            "radiative-memory and cosmology composition-square fixtures",
            "explicit prohibition on inferring cross-sector bridges from common diagram shape",
        ],
    },
    "deutschian-prime-spectral-explanation-charter.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": [],
        "missing_interfaces": [
            "one source-derived prime--gamma Weil form shared across every finite gate",
            "separated rank-three positivity and finite source Gram identification",
            "source-side Li norm vectors and heat-flow compatibility",
            "positive radical quotient, closability, and source-canonical self-adjoint operator",
            "compact resolvent, completed Xi determinant, exact prime trace, and L-function functoriality",
            "proof that no component imports zero data or assumes RH-equivalent positivity",
        ],
    },
    "log-time-bridge-identifies-weil-form-and-prime-two-gate.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": [],
        "missing_interfaces": [
            "admissible test-function space and centered Weil distribution",
            "convolution-square spectral explicit formula",
            "Weil positivity iff RH theorem",
            "short-support local positive form and completed prime-two cross block",
            "normalized operator contraction inequality",
            "mapping-cone dilation deriving the contraction without assuming global positivity",
        ],
    },
    "theta-prime-shift-laplacian-dilation-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeTranslationAdjacency.lean", "AdditivePrimeEdgeBudget.lean"],
        "missing_interfaces": [
            "Hardy half-line unilateral shifts and Laplace Cauchy features",
            "cross-kernel integration formula",
            "positive edge-Laplacian identity on a common form domain",
            "prime-power weighted cutoff and divergence of the shared degree budget",
            "gamma-endpoint renormalized counterterm and forbidden squarefree fill-in control",
            "cutoff-independent self-adjoint dilation and determinant",
        ],
    },
    "theta-product-ratio-coordinate-is-faithful-with-c2-mackey-norm.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteRefinementCorrespondence.lean"],
        "missing_interfaces": [
            "positive-integer unordered pairs and product--absolute-log-ratio map",
            "real exponential and square-root reconstruction with integer uniqueness",
            "swap quotient with diagonal stabilizers",
            "fiber cardinality two off the diagonal and one on it",
            "normalized isometric pullback and hyperbolic transport",
            "analytic radial sampling correspondence",
        ],
    },
    "theta-rh-prime-transport-lakatos-closeout.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "PrimeTranslationAdjacency.lean",
            "CyclicAdamsSpectrum.lean",
            "MixedPrimeRectangleParity.lean",
            "TwoPeriodicNormComplex.lean",
        ],
        "missing_interfaces": [
            "one labelled prime-power transport object assembling the arithmetic grammar",
            "finite-cutoff completed endpoint--gamma counterterm C_Y",
            "common quadratic-form domain and monotone, bounded-below, or convergent orientation law",
            "adelic rational-lattice self-annihilation and boundary trace",
            "source-derived self-adjoint relation and determinant comparison",
        ],
    },
    "theta-full-germ-detector-is-not-uniformly-faithful-on-discrete-labels.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "completed theta kernel with super-exponential derivative decay",
            "compact-open smooth germ topology and translation continuity",
            "adjacent logarithmic shifts and mean-value derivative bounds",
            "weighted discrete coefficient Hilbert norm with lower-bounded adjacent weights",
            "injective synthesis with nonclosed range",
            "hybrid germ/discrete-type completion and a source coupling differential",
        ],
    },
    "theta-mixed-sheet-green-clifford-obstruction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "two sheared tail-feature flows and integrated mixed Green identity",
            "complex two-sheet Clifford generator with sigma-three",
            "Hermitian metric decomposition into commuting and anticommuting parts",
            "difference-versus-sum spectral denominator theorem",
            "alternating physical cross polarization and analytic divisibility by z plus conjugate w",
            "transverse jet and source-derived modular sewing map",
        ],
    },
    "theta-euler-phase-continuation.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": [],
        "missing_interfaces": [
            "completed xi function and zero-free Euler half-plane",
            "canonical holomorphic logarithm from the absolutely convergent Euler product",
            "holomorphic-logarithm extension iff chamber nonvanishing",
            "functional-equation reflection and integer loop index",
            "branch-independent renormalized theta--prime primitive on the open right chamber",
            "proof of nonvanishing without defining the branch from zeros",
        ],
    },
    "theta-hilbert-schmidt-prime-trace-defect.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": [],
        "missing_interfaces": [
            "prime-indexed Hilbert space and diagonal character operator",
            "prime-series criterion for Hilbert--Schmidt membership exactly right of one half",
            "regularized det-two product, holomorphy, and nonvanishing",
            "Euler-region factorization isolating the completed linear trace channel",
            "chamber continuation and equivalence of its nonvanishing with RH",
            "source-derived holomorphic logarithm of the isolated channel",
        ],
    },
    "eta-jet-certification-reduction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["EtaJetReconstruction.lean"],
        "missing_interfaces": [
            "analytic definitions of eta and zeta near one and cancellation of the zeta pole",
            "proof that Taylor coefficients equal normalized derivatives",
            "identification of the four Laurent parameters with the chosen Stieltjes convention",
            "certified interval values for log two and the eta derivatives through order four",
        ],
    },
    "eta-derivative-euler-tail-bound.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "forward differences and their Mellin--Gamma integral representation",
            "differentiation under the integral sign on the stated real interval",
            "digamma and reciprocal-Gamma bounds with exact domains",
            "summation of the differentiated infinite Euler tail",
        ],
    },
    "eta-euler-tail-certification-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "the derivative-polynomial recurrence and exact coefficient family q_r",
            "machine-checkable positivity certificates for every m and j used",
            "integral representation proving positivity and monotonicity of forward differences",
            "Euler transformation remainder theorem and exact rational bound replay",
        ],
    },
    "eta-high-jet-cauchy-tail-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "complex analytic continuation of the forward-difference integral on the Cauchy disk",
            "reciprocal-Gamma Weierstrass product bound on the stated rectangle",
            "Cauchy derivative estimate with the explicit radius and constants",
            "infinite Euler-tail summation and the order-six numerical inequality",
        ],
    },
    "eta-jet-directed-rounding-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EtaJetReconstruction.lean"],
        "missing_interfaces": [
            "trusted correctly-rounded Decimal logarithm contract or independently replayed log enclosures",
            "typed outward-rounded interval arithmetic for every finite-prefix operation",
            "formal link from the Euler-transform table and remainder box to eta derivatives",
            "import and replay of the emitted interval certificate rather than trust in Python output",
        ],
    },
    "eta-order-six-directed-rounding-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "replayable directed-rounding certificate for logarithms and the 9,999-term prefix",
            "formal Euler-transform remainder through derivative order six",
            "interval truncated-series algebra for the completed logarithmic derivative",
            "typed substitution and inversion from the source coordinate to the moment coordinate",
        ],
    },
    "eta-order-six-tail-extension.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "derivative-polynomial construction through order six",
            "exact positivity replay at m fifteen and sixteen",
            "positive decreasing forward-difference theorem at the chosen prefix",
            "exact Euler remainder comparison with the stated decimal threshold",
        ],
    },
    "eta-order-eight-directed-rounding-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "replayable correctly-rounded logarithm table through the 99,999-term prefix",
            "formal directed interval propagation through derivative order eight",
            "formal eight-transform tail enclosure",
            "typed completed-series engine deriving moments A6 and A7",
        ],
    },
    "eta-order-eight-tail-scaling.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "bounded exhaustive certificate for failure of transform depths through one hundred at the old threshold",
            "exact derivative-polynomial positivity replay at the new threshold",
            "forward-difference monotonicity theorem",
            "exact comparison of the Euler remainder with four times ten to the negative thirty-six",
        ],
    },
    "eta-order-ten-directed-rounding-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "replayable logarithm and directed-arithmetic certificate for 499,999 prefix terms",
            "formal ten-transform remainder enclosure through derivative order ten",
            "certificate-to-eta-derivative soundness theorem",
            "typed degree-nine series composition deriving moments A8 and A9",
        ],
    },
    "eta-order-ten-tail-scaling.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "derivative-polynomial construction through order ten",
            "exact positivity certificate at m ten and eleven",
            "Euler transformation remainder theorem at the half-million prefix",
            "exact rational-to-decimal threshold comparison",
        ],
    },
    "digamma-high-jet-remainder-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "digamma integral representation and Bernoulli asymptotic expansion",
            "holomorphy of the remainder on the stated Cauchy disk",
            "complex denominator bound and first-omitted-term estimate",
            "recurrence transport to the completed source and exact order-six numerical bound",
        ],
    },
    "central-analytic-slope-and-eta-second-tail.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "analytic reduced-source formula and removable-singularity theorem at the central boundary",
            "twice differentiated forward-difference integral with justified differentiation",
            "digamma and trigamma bounds on the full scan interval",
            "replayable outward-rounded nonlinear propagation for all twenty-one chord cells",
        ],
    },
    "central-xi-log-even-series-construction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["EvenJetObservability.lean"],
        "missing_interfaces": [
            "analytic completed Xi logarithmic derivative and reflection identity",
            "formal power-series descent from the odd q-series through t equal q squared",
            "directed coefficient and remainder enclosure for the order-thirteen jet",
            "typed nonlinear inverse-square-root propagation to H and its derivatives",
        ],
    },
    "quarter-point-first-hausdorff-jets.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["EtaJetReconstruction.lean", "QuarterPointJetConversion.lean"],
        "missing_interfaces": [
            "completed Xi logarithmic derivative and its Laurent-free source expansion",
            "formal derivation of l0 through l2 from Stieltjes and polygamma constants",
            "source-fixed convention identifying L before the Jacobian division by one plus two epsilon",
            "rigorous enclosures for gamma0 through gamma2 and zeta three",
            "Hausdorff representation, which remains conditional on RH",
        ],
    },
    "quarter-point-first-localizer-determinants.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["QuarterPointJetConversion.lean"],
        "missing_interfaces": [
            "source-fixed notation resolving whether L is before or after Jacobian division",
            "formal derivation of l3 from the completed zeta factors",
            "rigorous input boxes for the four source coefficients",
            "replayable interval determinant certificate",
            "Hausdorff measure representation and any RH-dependent interpretation",
        ],
    },
    "one-time-stieltjes-moment-reconstruction-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "infinite Stieltjes moment theorem from all ordinary and shifted Hankel matrices",
            "exponential-moment criterion and moment determinacy",
            "absolute Taylor--integral interchange and measure reweighting",
            "real-analytic continuation on the positive half-line",
            "right-half-plane holomorphy of the completed Xi source formula",
        ],
    },
    "order-two-stieltjes-boundary-equivalence.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "positive locally finite Stieltjes measures with the required convergence class",
            "differentiation under the Stieltjes integral",
            "integration of the order-two transform and boundary normalization",
            "measure reweighting and equality of the resulting integral representations",
            "typed identification of the completed Xi boundary source",
        ],
    },
    "xi-stieltjes-moment-equivalence.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "theta-derived completed Xi and its even squared-coordinate logarithmic derivative",
            "symmetric canonical product with multiplicities and convergence normalization",
            "Stieltjes representation theorem and meromorphic atomic-support theorem",
            "pole-to-zero pullback including removable singularities and multiplicities",
            "equivalence with RH stated without importing RH as a premise",
        ],
    },
    "xi-stieltjes-squared-spectral-equivalence.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "completed xi reflection and descent of the odd logarithmic derivative through w squared",
            "Hadamard product and paired logarithmic-derivative convergence",
            "global Stieltjes analytic continuation, growth, pole, and residue conditions",
            "pullback of negative-axis poles to critical-line zeros",
            "trace-regularized squared-operator resolvent realization",
        ],
    },
    "scalar-heat-stieltjes-hankel-variance-hierarchy.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "positive infinite squared-spectral measure and integrability of every moment",
            "differentiation of the Laplace transform under the integral",
            "general finite Hankel matrices as Hilbert-space Gram matrices",
            "normalized tilted measure and variance identity",
            "strictness from the Xi Weyl law and completed arithmetic source formula",
        ],
    },
    "quarter-point-first-localizer-interval-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [
            "EtaJetReconstruction.lean",
            "QuarterPointJetConversion.lean",
            "FiniteStieltjesMoments.lean",
        ],
        "missing_interfaces": [
            "replayable eta-jet directed-rounding certificate and Euler-tail theorem",
            "exact-rational Machin arctangent and Apery zeta-three enclosure proofs",
            "sound outward interval arithmetic for the completed source coefficients",
            "certificate replay for both determinant lower bounds",
        ],
    },
    "quarter-point-order-two-interval-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [
            "QuarterPointJetConversion.lean",
            "FiniteStieltjesMoments.lean",
        ],
        "missing_interfaces": [
            "directed eta derivatives through order six and their tail certificate",
            "generic interval truncated-series quotient, composition, and Catalan inversion through degree five",
            "source derivation and enforcement of the inverse two-s-minus-one normalization",
            "replayable three-by-three determinant interval certificate",
        ],
    },
    "quarter-point-order-three-interval-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "directed eta derivatives and exact tail theorem through order eight",
            "endpoint cancellation and gamma-factor zeta coefficients through weight eight",
            "interval Catalan coordinate inversion and composition through degree seven",
            "replayable four-by-four determinant interval certificate",
        ],
    },
    "quarter-point-order-four-interval-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "directed eta and gamma input certificates through order ten",
            "formal Bernoulli cancellation and Catalan inversion through degree nine",
            "sound adaptive-precision interval composition",
            "replayable five-by-five determinant interval certificate",
        ],
    },
    "quarter-point-extremal-ritz-convergence-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["MomentCompanionCore.lean", "FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "positive measure on the compact interval and nested polynomial subspaces in its L2 space",
            "self-adjoint multiplication operator and finite compression construction",
            "Rayleigh--Ritz variational characterization and monotonicity under subspace inclusion",
            "polynomial density and convergence to the top support point",
            "decreasing square-root coordinate map and interval-certified numerical nodes",
            "conditional identification of the support endpoint with the first Riemann ordinate",
        ],
    },
    "quarter-point-linear-hausdorff-rh-equivalence.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteHausdorffMoments.lean"],
        "missing_interfaces": [
            "infinite Hausdorff moment theorem in signed-difference form",
            "unique positive measure construction on the unit interval",
            "rescaling equivalence between the quarter-point moments and unit-interval moments",
            "replayable interval certificate for all fifty-five finite inequalities",
            "completed-source analytic identification and its RH equivalence",
        ],
    },
    "quarter-point-hausdorff-moment-rh-equivalence.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [
            "FiniteHausdorffMoments.lean",
            "FiniteStieltjesMoments.lean",
            "QuarterPointJetConversion.lean",
        ],
        "missing_interfaces": [
            "completed Xi squared-coordinate resolvent with endpoint-pole cancellation",
            "pushforward and inverse pushforward between Stieltjes and compact Hausdorff measures",
            "infinite compact moment theorem via all three localizer families",
            "Taylor-integral interchange and analytic continuation of the reconstructed resolvent",
            "pole-location equivalence with RH without assuming the desired measure",
        ],
    },
    "quarter-point-blind-multiplicity-estimate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "positive compact moment functional and its Gaussian quadrature construction",
            "Jacobi node and Christoffel weight extraction",
            "replayable interval enclosure of the node-to-weight ratio",
            "typed distinction between scalar atom mass, divisor residue, and eigenspace dimension",
            "source-derived identification of the top atom with the first Xi zero",
        ],
    },
    "quarter-point-pade-jacobi-explanation.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["MomentCompanionCore.lean", "FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "nondegenerate positive moment functional and orthogonal-polynomial Jacobi matrix",
            "Gaussian quadrature exactness through degree two-n-minus-one",
            "resolvent equality with the Stieltjes Pade approximant",
            "identification of Jacobi nodes with rational poles",
            "replayable ten-moment numerical reconstruction and limiting Stieltjes premise",
        ],
    },
    "quarter-point-loewner-diagonal-curvature.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteHausdorffMoments.lean", "QuarterPointJetConversion.lean"],
        "missing_interfaces": [
            "three-times differentiable completed boundary function near the quarter point",
            "Taylor remainder theorem for the two-point Loewner determinant",
            "identification of its first three derivatives with the source moments",
            "replayable directed interval proof that the first Hankel determinant is strictly positive",
            "off-diagonal, higher-contact, and global Pick positivity, none of which follows from this contact",
        ],
    },
    "hausdorff-bivariate-source-generator-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteHausdorffMoments.lean"],
        "missing_interfaces": [
            "formal power series for the univariate moment and bivariate difference generators",
            "coefficientwise derivation of the rational two-branch generating-function identity",
            "domains and convergence for substituting the fractional argument",
            "completed-source resolvent identification and pole cancellation",
            "conditional squared-zero-coordinate expansion and any infinite positivity conclusion",
        ],
    },
    "theta-moment-cumulant-stieltjes-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["MomentCumulantHostiles.lean"],
        "missing_interfaces": [
            "positive normalized theta measure and its entire cosh transform",
            "formal logarithmic power-series derivation of all even cumulants",
            "smooth positive even approximations preserving the strict hostile inequality",
            "directed evaluation of the actual theta moments",
            "source structure sufficient to make the nonlinear transformed measure positive and atomic",
        ],
    },
    "scalar-heat-complete-monotonicity-laguerre-hierarchy.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "generalized Laguerre polynomials with parameter negative one half",
            "all-order differentiation theorem for the log-Gaussian heat atom",
            "absolute convergence and differentiation of the von Mangoldt prime sum",
            "differentiated completed gamma integral with endpoint constants retained",
            "certified Laguerre-weighted tails and an all-order completed cancellation mechanism",
        ],
    },
    "scalar-heat-positivity-is-not-stieltjes-no-go.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["MomentCumulantHostiles.lean"],
        "missing_interfaces": [
            "Bernstein and Stieltjes representation theorems with their measure hypotheses",
            "Laplace transform of the positive oscillatory heat fixture",
            "complex pole calculation proving that the transform is not Stieltjes",
            "complete-monotonicity failure for an explicit admissible epsilon and frequency",
            "completed Xi meromorphy, residue normalization, and RH-equivalent specialization",
        ],
    },
    "positive-even-measure-loewner-curvature-falsifier.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["MomentCumulantHostiles.lean"],
        "missing_interfaces": [
            "derivation of the four cumulants from the stated symmetric probability measure",
            "analytic cumulant-generating function and its square-root coordinate expansion",
            "formal construction of the boundary source F from that expansion",
            "order-two Stieltjes measure representation and covariance-square curvature theorem",
            "any transfer from the hostile fixture to the actual Xi source, which is not claimed",
        ],
    },
    "loewner-kernel-universal-coupled-positivity-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteHausdorffMoments.lean", "FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "fractional-coordinate derivation from the bivariate Hausdorff generator",
            "infinite positive resolvent measure and rank-one kernel summability",
            "Loewner matrix-monotonicity representation theorem on the positive axis",
            "meromorphic Xi continuation and pole identification",
            "source-side gamma--prime Gram factorization, which remains the unproved target",
        ],
    },
    "theta-denominator-free-loewner-kernel.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["DiagonalCongruencePositivity.lean"],
        "missing_interfaces": [
            "analytic theta current C and its derivative kernel",
            "removable extension of the cleared divided difference across diagonal points and real zeros",
            "continuity transfer of kernel positivity to configurations containing zeros",
            "Loewner--Pick representation and angular-flow identity with strictness conditions",
            "source-derived Gram factorization proving global positivity of L_C without assuming real zeros",
        ],
    },
    "loewner-curvature-reciprocal-concavity-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteStieltjesMoments.lean", "MomentCumulantHostiles.lean"],
        "missing_interfaces": [
            "twice differentiable positive source slope and reciprocal-square-root derivative theorem",
            "finite or infinite order-two Stieltjes representation with denominator domains",
            "pairwise covariance-square expansion and strictness criterion",
            "analytic completed-source specialization away from the quarter point",
            "formal completely-monotone exponential hostile and its failure of curvature",
        ],
    },
    "reduced-source-loewner-diagonal-curvature-conditioning.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteHausdorffMoments.lean"],
        "missing_interfaces": [
            "directed interval automatic differentiation through third order",
            "correlated eta and digamma transform remainder bounds",
            "direct integral or covariance formula for source curvature",
            "high-precision ball certificate over a specified positive-axis cover",
            "global diagonal-curvature and Pick conclusions, which the failed scan does not support",
        ],
    },
    "reduced-gamma-prime-pick-target.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ReducedEndpointPick.lean", "FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "principal complex square-root map from the upper t half-plane",
            "completed Xi logarithmic derivative with digamma and zeta logarithmic derivative",
            "analytic equality between the completed source and the reduced formula",
            "infinite resolvent summability and Herglotz--Pick representation theorem",
            "the coupled gamma--prime imaginary-part inequality, which remains unproved",
        ],
    },
    "reduced-source-pick-boundary-slope-scan.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["TwoHeightPickFactorization.lean"],
        "missing_interfaces": [
            "analytic reduced source on an upper-half-plane neighborhood of the positive axis",
            "boundary derivative as the normalized imaginary-part limit",
            "certified eta/digamma evaluator over all fifty-seven sample points",
            "transform-depth and small-height error enclosures",
            "coupled Loewner matrices, which diagonal positivity does not imply",
        ],
    },
    "reduced-source-pick-first-hostile-scan.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "complex interval eta, eta-prime, and digamma evaluator",
            "certified adaptive cover of the declared upper-half-plane region",
            "near-pole and large-height truncation bounds",
            "formal synthetic negative-residue control",
            "a sign certificate between grid points; sparse floating samples provide none",
        ],
    },
    "reduced-source-F-prime-unit-circle-reconnaissance.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean"],
        "missing_interfaces": [
            "reflection-even centered Xi series eliminating the principal-square-root seam",
            "analyticity of the reduced derivative on and inside the unit circle",
            "complex interval derivative evaluation with truncation control",
            "maximum-modulus or boundary-cover theorem turning samples into a uniform bound",
            "rigorous bound stronger than the proposed constant twenty",
        ],
    },
    "central-F-prime-unit-disk-theta-coarse-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean"],
        "missing_interfaces": [
            "positive theta-moment expansion for the centered Xi function",
            "coefficientwise bounds relating derivatives at one to the value at nine",
            "log-convex Gamma, zeta integral-test, and rational pi bounds with exact exponents",
            "replayable directed Rouche lower bound for the denominator m",
            "Cauchy tail theorem and interval propagation to reciprocal-slope concavity on the stated cell",
        ],
    },
    "quarter-centered-angular-modulus-pick-equivalence.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "analytic centered Xi composition and logarithmic derivative away from zeros",
            "polar angular derivative identity with a limiting formulation at zeros",
            "equivalence between upper-half-plane Pick positivity and all-radius modulus monotonicity",
            "theta integral endpoint comparison and decreasing envelope",
            "tilted characteristic-function contraction preventing interior rebound",
            "global angular monotonicity, which is RH-equivalent and is not assumed",
        ],
    },
    "li-caratheodory-half-plane-equivalence.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["FiniteLiVariance.lean"],
        "missing_interfaces": [
            "Li coefficient generating identity for the completed xi function",
            "formal power-series differentiation and second-difference collapse",
            "Herglotz--Caratheodory theorem relating positive-definite integer sequences to positive real part",
            "Möbius equivalence between the unit disk and the right critical half-plane",
            "global positive-real property of xi-prime over xi, which is RH-equivalent and is not assumed",
        ],
    },
    "li-cayley-domain-audit.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CompletionKernel.lean", "CompletionNeutrality.lean"],
        "missing_interfaces": [
            "conditional phase measure with divisor-copy multiplicities",
            "maximal-domain multiplication operator for a real measurable Cayley coordinate",
            "self-adjointness of unbounded multiplication and density of finite-support vectors",
            "divergence proof excluding the constant cyclic vector from the domain",
            "compact-resolvent criterion with finite amplified multiplicity and no finite accumulation",
        ],
    },
    "xi-log-derivative-Herglotz-kernel.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["CompletedKernelSectorNoGo.lean", "DiagonalCongruencePositivity.lean"],
        "missing_interfaces": [
            "centered completed Xi and its meromorphic logarithmic derivative",
            "symmetric canonical product with boundary zeros and convergent regularization",
            "infinite Cauchy-feature Gram kernel and positive-kernel definition on the half-plane",
            "holomorphy-to-zero-exclusion and functional-reflection converse",
            "source-derived completed Gram factorization, which is RH-equivalent and is not assumed",
        ],
    },
    "xi-pick-krein-boundary-preshape.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["RadicalRepairObstruction.lean", "CompletionNeutrality.lean"],
        "missing_interfaces": [
            "source-defined Hermitian Pick kernel from the theta Xi function",
            "free finite span of kernel vectors and quotient by the Hermitian radical",
            "nondegenerate indefinite pre-space and Green identity",
            "choice and comparison of Hilbert majorants or a canonical Krein topology",
            "positive descent, reproducing-kernel completion, boundary triple, and regularized determinant",
            "coefficient--Betti comparison map compatible with cutoff refinement",
        ],
    },
    "completed-source-Herglotz-kernel-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CompletedKernelSectorNoGo.lean", "EndpointPoleCancellation.lean"],
        "missing_interfaces": [
            "centered completed logarithmic derivative and its Euler-region decomposition",
            "von Mangoldt coefficients and convergence of the prime exponential series",
            "analytic cancellation and transport across the s-equals-one boundary",
            "relative or Krein source coupling with an explicit null subspace",
            "positive completed quotient or Schur complement and its vector-valued Gram map",
        ],
    },
    "xi-completed-heat-kernel-reconciliation.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CompletedKernelSectorNoGo.lean"],
        "missing_interfaces": [
            "completed endpoint, gamma, and von Mangoldt heat kernels on one common domain",
            "certified prime-tail and zero-tail estimates for the reconciliation samples",
            "small-time gamma/Weyl asymptotics with exponentially controlled prime terms",
            "finite transition-region interval cover",
            "large-time prime saddle cancellation with a remainder at the first spectral-exponential scale",
        ],
    },
    "xi-gamma-heat-kernel.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "digamma integral representation and removable integrand singularity",
            "square-root inverse-Laplace transform with exact constants",
            "Fubini or dominated-convergence justification for the gamma integral",
            "common Laplace-transform domain for endpoint, gamma, and prime pieces",
            "analytic continuation to the completed squared resolvent",
        ],
    },
    "xi-prime-heat-kernel-and-coupling.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CompletedKernelSectorNoGo.lean", "ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "von Mangoldt series for zeta-prime over zeta in the Euler half-plane",
            "inverse-Laplace transform of the square-root exponential",
            "fixed-time convergence of the infinite log-Gaussian prime sum",
            "common analytic continuation and endpoint zeta-pole cancellation",
            "large-time saddle control and completed pointwise or complete-monotonicity inequality",
        ],
    },
    "xi-heat-weyl-law-and-limit.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [],
        "missing_interfaces": [
            "Riemann--von Mangoldt counting formula with a quantified remainder",
            "Stieltjes integration against the Gaussian heat weight",
            "exact Gaussian and logarithmic Mellin derivative integrals",
            "short-time asymptotic expansion with controlled lower-order terms",
            "operator heat-trace realization and a finite-quartet lower-order perturbation theorem",
        ],
    },
    "xi-newman-zero-velocity-and-heat-flow.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["NewmanSpectralHeatSeparation.lean"],
        "missing_interfaces": [
            "analytic de Bruijn--Newman family satisfying the backward-heat PDE",
            "implicit differentiation of a real simple zero branch",
            "termwise differentiation of the infinite two-parameter spectral heat trace",
            "multiple-zero collision and discriminant analysis",
            "measure-valued comparison principle surviving changes in divisor topology",
        ],
    },
    "xi-spectral-heat-vs-newman-flow.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["NewmanSpectralHeatSeparation.lean"],
        "missing_interfaces": [
            "self-adjoint fixed-spectrum operator and trace-class heat semigroup",
            "Fourier integral definition of the de Bruijn--Newman family",
            "moving-zero branches and their squared spectral measures",
            "two-parameter source object and an intertwining transport theorem",
            "collision or nonreal-bifurcation semantics for failure of positive spectral representation",
        ],
    },
    "xi-stieltjes-heat-trace-bridge.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "OffAxisHeatOscillation.lean",
            "FiniteStieltjesMoments.lean",
            "CompletedKernelSectorNoGo.lean",
        ],
        "missing_interfaces": [
            "positive squared spectral measure with multiplicities and heat integrability",
            "Laplace transform of each resolvent atom and interchange with the infinite spectral sum",
            "all-order differentiation under the heat integral",
            "source arithmetic heat functional with endpoint--gamma--prime coupling",
            "commuting transforms to the Caratheodory and Li moment readouts",
        ],
    },
    "xi-log-derivative-weyl-equivalence.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["CompletedKernelSectorNoGo.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "theta-defined entire Xi and its meromorphic logarithmic derivative",
            "Nevanlinna representation theorem and meromorphic real-pole characterization",
            "symmetric canonical product and convergence of the paired pole expansion",
            "integer residue extraction and multiplicity-amplified self-adjoint realization",
            "compact resolvent, Hilbert--Schmidt inverse, and regularized determinant theorem",
            "source boundary trace or defect map identifying the abstract realization",
            "Nevanlinna positivity, which is RH-equivalent and is not assumed",
        ],
    },
    "xi-complete-bernstein-equivalence.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["OffAxisHeatOscillation.lean", "FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "single-valued centered squared Xi logarithm and analytic continuation",
            "complete Bernstein and Levy--Khintchine representation theorems",
            "Frullani formula and interchange with the infinite spectral sum",
            "Stieltjes derivative with meromorphic positive-integer residues",
            "Möbius transport to Li moments and multiplication-operator realization",
            "source-derived completely monotone Levy density, which is RH-equivalent and is not assumed",
        ],
    },
    "li-abel-renormalized-prime-germ.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EndpointPoleCancellation.lean", "EtaJetReconstruction.lean"],
        "missing_interfaces": [
            "zeta logarithmic derivative in the right half-plane and its Abel family",
            "Laurent theorem at one with a simple pole and analytic finite germ",
            "all-order differentiation proving absence of intermediate negative powers",
            "analytic completed endpoint--gamma--prime germ and Stieltjes coefficient convention",
            "comparison between Abel and sharp-cutoff finite parts",
        ],
    },
    "li-arithmetic-toeplitz-attack.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["FiniteLiVariance.lean", "LiDegreeTwoCoupling.lean"],
        "missing_interfaces": [
            "all-degree arithmetic Li second-difference Toeplitz functional",
            "source derivation of every coefficient from completed zeta without zero phases",
            "uniform endpoint--gamma--prime coupling rule extending across Toeplitz ranks",
            "finite certified falsifier search beyond degree two",
            "global positivity for every complex polynomial, which is RH-equivalent and is not assumed",
        ],
    },
    "li-cayley-hilbert-polya-target.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CompletionKernel.lean", "FiniteLiVariance.lean"],
        "missing_interfaces": [
            "positive arithmetic Toeplitz functional and its GNS construction",
            "unitary descent of the shift through the GNS null space",
            "unbounded Cayley transform with maximal natural domain and self-adjointness",
            "spectral mass treatment at the singular phase one",
            "identification of the GNS measure with the completed-zeta divisor and multiplicity amplification",
        ],
    },
    "li-degree-two-completion-coupling.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["LiDegreeTwoCoupling.lean"],
        "missing_interfaces": [
            "analytic endpoint, gamma, and Abel-renormalized prime germ definitions",
            "identification of their first three Taylor coefficients with the supplied jet vectors",
            "directed enclosures for the six numerical self and cross pieces",
            "an invariant higher-degree coupling rule rather than a fitted degree-two decomposition",
        ],
    },
    "li-degree-two-coupled-positivity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteLiVariance.lean", "LiDegreeTwoCoupling.lean"],
        "missing_interfaces": [
            "three-by-three Toeplitz matrix from the first three Li coefficients",
            "orthogonal reflection-channel basis and exact determinant factorization",
            "completed-zeta jet derivation from Stieltjes and special constants",
            "rigorous interval certification of the two channel signs",
            "uniform source coupling identity extending to every degree",
        ],
    },
    "li-spectral-norm-target.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["LiDegreeTwoCoupling.lean"],
        "missing_interfaces": [
            "complex Mobius phase attached to a nontrivial zero parameter",
            "exact norm-square residual in terms of sigma and gamma",
            "equivalence of inverse and conjugate exactly on the critical line",
            "source-derived vectors and Gram values before zero fibers are known",
            "all-degree identification with Li coefficients",
        ],
    },
    "li-symmetric-principal-part-transport-basis.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["LiDegreeTwoCoupling.lean"],
        "missing_interfaces": [
            "rational-square test associated functorially to an arbitrary polynomial",
            "Laurent principal parts at zero and one with reflection-matched coefficients",
            "vanishing-at-infinity uniqueness theorem for the rational remainder",
            "residue pairing with the completed logarithmic-derivative jet",
            "Laplace or Mellin transport of the universal basis with endpoint and gamma residues",
        ],
    },
    "li-canonical-endpoint-residue-functional.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["LiMobiusCocycle.lean", "EndpointPoleCancellation.lean"],
        "missing_interfaces": [
            "completed entire xi and holomorphic logarithmic derivative at both endpoints",
            "rational-square test with degree-controlled endpoint poles",
            "Laurent residue pairing and reflection equality of endpoint residues",
            "finite-jet dependence theorem for arbitrary polynomial degree",
            "symmetric contour exhaustion and full-divisor identity",
        ],
    },
    "li-cauchy-jet-feature.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["LiMobiusCocycle.lean", "LiDegreeTwoCoupling.lean"],
        "missing_interfaces": [
            "Mellin Cauchy kernel and parameter differentiation through arbitrary jet order",
            "binomial principal-part expansion of every feature V_n",
            "membership and closability in the completed Weil domain",
            "source-derived involution and positive pairing before zero-fiber evaluation",
            "explicit-formula comparison with every Li coefficient",
        ],
    },
    "li-cnd-cocycle-equivalence.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["LiMobiusCocycle.lean", "FiniteLiVariance.lean"],
        "missing_interfaces": [
            "even extension of the full Li sequence to the integers",
            "finite conditional-negative-definiteness forms and anchored Gram equivalence",
            "Schoenberg Hilbert embedding theorem for conditionally negative kernels",
            "convergent positive sum of unit-circle displacement cocycles",
            "arithmetic source construction of the whole anchored kernel",
            "all-order Li positivity, which is RH-equivalent and is not assumed",
        ],
    },
    "li-global-contour-closure.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["LiMobiusCocycle.lean"],
        "missing_interfaces": [
            "all-degree asymptotic expansion of the rational-square test at infinity",
            "completed-zeta zero strip and quantified counting estimate",
            "dyadic absolute-convergence theorem with multiplicities",
            "zero-avoiding rectangular contours and logarithmic-derivative bounds",
            "residue theorem passage to the full-divisor sum",
        ],
    },
    "li-homogeneous-cocycle-target.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["LiMobiusCocycle.lean", "CompletionNeutrality.lean"],
        "missing_interfaces": [
            "homogeneous Hilbert or Dirichlet space quotienting null constants",
            "source-defined positive energy form on completed Cauchy jets",
            "isometric multiplication by the Möbius coordinate descending through the null space",
            "finite energy and closability for every cocycle class",
            "explicit-formula equality between source energy and Li coefficients",
        ],
    },
    "li-increment-spectral-measure-target.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["LiMobiusCocycle.lean", "FiniteLiVariance.lean"],
        "missing_interfaces": [
            "conditional unit-circle phase measure with inverse-square divisor weights",
            "second-difference calculation relating Li pairs to phase Fourier moments",
            "finiteness from the completed zero-counting estimate",
            "positive functional on all trigonometric squares and its GNS construction",
            "noncircular arithmetic derivation of the moment functional",
        ],
    },
    "li-mobius-weil-test-cone.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["LiMobiusCocycle.lean", "LiDegreeTwoCoupling.lean"],
        "missing_interfaces": [
            "arbitrary polynomial evaluation at the Möbius coordinate and inverse",
            "reflection-invariant rational-square test algebra",
            "critical-line conjugation and denominator norm-square theorem",
            "pair-normalized arithmetic explicit-formula functional",
            "positivity on the entire rational-square cone without zero phases",
        ],
    },
    "li-toeplitz-increment-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteLiVariance.lean", "LiMobiusCocycle.lean"],
        "missing_interfaces": [
            "arbitrary-rank anchored Li and Toeplitz increment matrices",
            "lower-triangular cumulative-sum matrix and its inverse difference matrix",
            "all-rank congruence identity K_N equals S_N T_N S_N transpose",
            "positive-semidefinite equivalence under the invertible congruence",
            "Herglotz theorem constructing a positive circle measure from the increment sequence",
        ],
    },
    "li-universal-vandermonde-positivity.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteLiVariance.lean", "DiagonalCongruencePositivity.lean"],
        "missing_interfaces": [
            "finite positive Borel measure on the unit circle and complex Fourier moments",
            "Toeplitz moment matrix as a Gram matrix of monomials",
            "Gram--Andreief determinant identity",
            "complex Vandermonde determinant and product-norm formula",
            "strict positivity iff the measure support has at least N distinct points",
            "conditional specialization to the inverse-square-weighted Li phase measure",
        ],
    },
    "xi-centered-unit-disk-Rouche-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean"],
        "missing_interfaces": [
            "theta integral representation and positivity of the centered Xi kernel",
            "directed Euler-transform lower bound for the zeta value at one half",
            "exact Gamma and pi endpoint inequalities",
            "sound interval comparison proving the stated positive margin",
            "Rouche theorem on the closed centered disk and boundary strictness",
        ],
    },
    "xi-centered-unit-disk-theta-Rouche-reduction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean"],
        "missing_interfaces": [
            "positive theta-kernel cosh integral for centered Xi",
            "complex cosh power-series majorization on the unit disk",
            "integral triangle inequality and strict endpoint comparison",
            "Rouche zero-count invariance against the nonzero constant function",
            "certified real endpoint inequality supplied by the companion packet",
        ],
    },
    "xi-graph-projector-separable-rank-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ScalarIntegralTrace.lean", "RankOneIncidenceFaithfulness.lean"],
        "missing_interfaces": [
            "finite conjugation-stable divisor truncation and graph permutation matrix",
            "full-rank theorem for arbitrary permutation matrices",
            "rank subadditivity for a sum of m separable outer products",
            "nonzero diagonal reflection weighting preserving hostile-sector rank",
            "unbounded-window conclusion excluding every fixed finite channel family",
        ],
    },
    "xi-hermitian-defect-heat-bridge.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["OffAxisHeatOscillation.lean", "NewmanSpectralHeatSeparation.lean"],
        "missing_interfaces": [
            "zero-divisor Hilbert space and maximal normal diagonal operator",
            "real-part defect and positive functional calculus of Z-star-Z",
            "trace finiteness from critical-strip bounds and zero counting",
            "Laplace resolvent identity and one-time vanishing equivalence",
            "source normal operator with conjugation-graph correspondence",
        ],
    },
    "xi-jet-associated-graded-boundary.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CompletionKernel.lean", "GradedResiduePolarization.lean"],
        "missing_interfaces": [
            "Hadamard-ring source range and proof that its saturated ideal equals the Xi principal ideal",
            "one-variable local analytic algebra and intrinsic length equal to vanishing order",
            "maximal-ideal filtration and one-dimensional associated-graded quotients",
            "spectral-coordinate semisimplification and dense entire jet interpolation",
            "conditional self-adjoint diagonal completion, compact resolvent, Hilbert--Schmidt inverse, and det-two formula",
            "source pairing distinguishing scalar evaluation rank from multiplicity-many jet channels",
        ],
    },
    "xi-local-residue-krein-pairing.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["LocalResidueKrein.lean", "GradedResiduePolarization.lean"],
        "missing_interfaces": [
            "local Xi quotient as an Artinian Gorenstein algebra",
            "Grothendieck residue functional with conjugate-real structure",
            "triangular congruence of arbitrary multiplicity to the anti-diagonal metric",
            "comparison with the scalar Weil evaluation form and associated-graded square-sum form",
            "additional source polarization converting the Krein form to positive graded channels",
        ],
    },
    "xi-log-derivative-boundary-skewness.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["OddInvolutionKernel.lean", "ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "completed xi functional equation and real-entire conjugation law",
            "meromorphic logarithmic derivative away from boundary zeros",
            "critical-line reflection equals complex conjugation",
            "unbounded-half-plane harmonic maximum principle with asymptotic control",
            "arithmetic pole exclusion or positive-real representation, which remains RH-sized",
        ],
    },
    "xi-offline-falsifier-latency.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["LiMobiusCocycle.lean"],
        "missing_interfaces": [
            "complex phase-modulus residual for an off-line zero parameter",
            "logarithmic expansion with a quantified error near the critical line",
            "latency comparison k comparable to modulus-squared over displacement",
            "construction showing invisibility below every prescribed finite rank",
            "conditioning theorem for small Gram eigenvalues",
        ],
    },
    "xi-offline-quartet-hostile-factor.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["OffAxisHeatOscillation.lean", "MomentCumulantHostiles.lean"],
        "missing_interfaces": [
            "complex centered quartet polynomial with parameter and conjugate",
            "proof of evenness and real structure for arbitrary complex arguments",
            "critical-boundary modulus-square identity and strictness away from collisions",
            "preservation under finite products of hostile quartet factors",
            "completed arithmetic rigidity that rejects the factor",
        ],
    },
    "xi-prime-heat-large-time-saddle.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CompletedKernelSectorNoGo.lean"],
        "missing_interfaces": [
            "continuum PNT prime-density replacement and logarithmic change of variables",
            "exact half-line Gaussian integral with error function",
            "endpoint cancellation and complementary-error-function asymptotic",
            "comparison with the first-ordinate exponential heat scale",
            "quantified insufficiency of classical PNT errors at the moving saddle",
        ],
    },
    "xi-reflection-defect-operator.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CompletionKernel.lean", "OffAxisHeatOscillation.lean"],
        "missing_interfaces": [
            "zero-divisor l2 space with multiplicities and maximal diagonal normal operator",
            "adjoint real part and bounded functional-calculus defect operator",
            "Hilbert--Schmidt summability from critical-strip and zero-counting bounds",
            "equivalence between zero defect and RH",
            "antiunitary conjugation real structure and quartet spectral calculation",
            "source normal operator independent of the zero divisor",
        ],
    },
    "xi-window-hermite-reference-falsifier.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteLiVariance.lean"],
        "missing_interfaces": [
            "Riemann--von Mangoldt asymptotics for rank and squared radius in growing windows",
            "Stieltjes integration deriving the one-third scaled second moment",
            "weak convergence of scaled ordinates to the uniform interval measure",
            "Hermite-root semicircle limit and affine-rescaling shape obstruction",
            "uniform-reference logarithmic potential and principal-value derivative",
            "Weyl-renormalized entropy with a separately derived Newman-flow law",
        ],
    },
    "quarter-point-canonical-coercivity-reserve.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": [
            "FiniteHausdorffMoments.lean",
            "FiniteStieltjesMoments.lean",
            "DiagonalCongruencePositivity.lean",
        ],
        "missing_interfaces": [
            "Lebesgue reference moment and localizer matrices on the unit interval",
            "generalized minimum eigenvalue and simultaneous-congruence invariance",
            "nested polynomial-space monotonicity of the reserve",
            "equivalence between uniform polynomial coercivity and measure domination by c times Lebesgue measure",
            "singular discrete measure implication that finite reserves are positive but their infimum is zero",
            "directed generalized-eigenvalue certificates and any asymptotic reserve-rate theorem",
        ],
    },
    "quarter-point-degree-nine-truncated-measure-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteHausdorffMoments.lean", "FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "replayable interval positivity for every leading localizer minor through size five",
            "Sylvester criterion for the two exact interval-valued matrices",
            "odd-degree truncated Hausdorff moment theorem on the compact interval",
            "construction of a positive Borel representing measure for moments zero through nine",
            "Gaussian atomic realization and explicit nonuniqueness boundary",
        ],
    },
    "quarter-point-fifth-ritz-edge.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["JacobiDeterminantRatio.lean"],
        "missing_interfaces": [
            "directed determinant-ratio and Lanczos diagonal coefficient boxes through index four",
            "finite symmetric tridiagonal Jacobi matrix construction",
            "certified or exact largest-eigenvalue computation",
            "monotone reciprocal square-root transform to the displayed edge estimate",
            "external comparison with the first ordinate, which is not source evidence",
        ],
    },
    "quarter-point-fifth-ritz-interval-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["JacobiDeterminantRatio.lean"],
        "missing_interfaces": [
            "interval Sturm pivot recurrence with division away from zero",
            "Sturm inertia theorem for a real symmetric tridiagonal matrix",
            "outward bisection preserving certified inertia counts four and five",
            "directed transformation of the top-node interval to the gamma estimate",
            "separation of interval width from finite-rank approximation error",
        ],
    },
    "quarter-point-finite-jacobi-compression.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": [
            "JacobiDeterminantRatio.lean",
            "FiniteStieltjesMoments.lean",
            "MomentCompanionCore.lean",
        ],
        "missing_interfaces": [
            "interval Lanczos orthogonalization from the certified source moments",
            "diagonal Jacobi coefficients and square roots of positive off-diagonal squares",
            "overlap with independent determinant-ratio boxes",
            "compressed quadratic-form bounds zero less than or equal to J less than or equal to four",
            "infinite self-adjoint continuation and conditional spectral identification",
        ],
    },
    "quarter-point-jacobi-coefficient-segment.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["JacobiDeterminantRatio.lean", "FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "Hankel determinants from the first ten interval-certified source moments",
            "outward interval propagation through all four determinant ratios",
            "monic orthogonal polynomial recurrence and norm-ratio theorem",
            "finite Lanczos nonbreakdown interpretation for the complete segment",
            "all-order consistency, multiplicity-sensitive channels, and infinite closure",
        ],
    },
    "central-chord-average-curvature-margin.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ReciprocalSlopeCurvature.lean", "FiniteHausdorffMoments.lean"],
        "missing_interfaces": [
            "twice differentiable real reciprocal-slope function on every chord",
            "triangular-kernel midpoint second-difference integral identity",
            "replayable directed interval for the weakest normalized average curvature",
            "simultaneous nonvanishing and positivity of the source slope on each cell",
        ],
    },
    "central-complex-pick-disk-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReducedEndpointPick.lean", "DiagonalCongruencePositivity.lean"],
        "missing_interfaces": [
            "directed normalized theta coefficients and positive tail majorant",
            "common-denominator interval bounds for C, C-prime, and C-double-prime",
            "certified zero-free unit disk and analytic logarithmic derivative",
            "vertical-segment integration proving the strict Pick sign",
        ],
    },
    "central-complex-pick-radius-three-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "positive normalized theta series and directed first six coefficients",
            "falling-factorial tail inequality from the radius-nine anchor",
            "common-denominator interval lower bound for the real part of F-prime",
            "zero-free radius-nine disk and vertical integration",
        ],
    },
    "central-complex-pick-radius-seven-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "exact elementary pi, Gamma, and zeta bounds at the radius-twenty-five anchor",
            "positive theta coefficient tail bounds through second derivative",
            "directed common-denominator proof that the real part of F-prime exceeds 0.017",
            "analyticity on the radius-nine disk and vertical integration",
        ],
    },
    "central-complex-pick-radius-seventeen-halves-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "exact Gamma recurrence, pi-power, and zeta bounds at the radius-eighty-one anchor",
            "directed normalized theta tail through degree six",
            "common-denominator proof that the real part of F-prime exceeds 0.008",
            "zero-free radius-nine disk and vertical integration",
        ],
    },
    "central-concavity-certification-error-budget.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EtaJetReconstruction.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "Euler-transform eta and differentiated eta tail theorems on the central interval",
            "digamma recurrence and Bernoulli remainder after the declared target shift",
            "correlated nonlinear propagation through the exact source slope",
            "replayable directed certificate replacing the historical finite-difference budget",
        ],
    },
    "central-F-prime-quarter-disk-polynomial-budget.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["EvenJetObservability.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "centered Xi logarithmic jet and coefficient recurrence for F-prime",
            "directed polynomial lower bound on the quarter disk",
            "analytic tail supremum below the residual allowance",
            "nonvanishing conclusion for the full source derivative",
        ],
    },
    "central-F-prime-unit-disk-Cauchy-reduction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean"],
        "missing_interfaces": [
            "analytic F-prime on a neighborhood of the closed unit disk",
            "Cauchy coefficient estimate with the stated uniform bound twenty",
            "geometric tail summation from degree five on the quarter disk",
            "combination with the directed polynomial lower bound",
        ],
    },
    "central-F-prime-unit-disk-theta-moment-reduction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean"],
        "missing_interfaces": [
            "positive theta coefficient theorem for centered Xi",
            "supremum bounds for the first two derivatives from endpoint moments",
            "Rouche denominator lower bound",
            "logarithmic derivative quotient estimates and directed evaluation of four endpoint quantities",
        ],
    },
    "central-F-prime-unit-disk-theta-sharp-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean", "EtaJetReconstruction.lean"],
        "missing_interfaces": [
            "formal recurrence from logarithmic coefficients to normalized theta coefficients",
            "strict interval positivity through coefficient six",
            "radius-nine positive-tail estimates for C and its first two derivatives",
            "common-denominator interval proof of both modulus and positive-real derivative bounds",
        ],
    },
    "central-first-cell-one-circle-cauchy-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "analytic inverse square-root branch from a nonvanishing F-prime disk bound",
            "Cauchy third-derivative estimate on nested disks",
            "triangular-average-to-pointwise oscillation theorem",
            "directed numerical comparison preserving the first-cell margin",
        ],
    },
    "central-h-third-derivative-oscillation-reconnaissance.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "validated high-order derivative evaluator without cancellation amplification",
            "interval rather than finite-difference oscillation bounds on all cells",
            "superseding reflection-even centered Xi series values",
            "formal retraction boundary preventing the obsolete 3.8 estimate from serving as evidence",
        ],
    },
    "central-reciprocal-slope-continuum-concavity-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReciprocalSlopeCurvature.lean", "EvenJetObservability.lean"],
        "missing_interfaces": [
            "directed centered Xi logarithmic jet through the declared order",
            "analytic inverse-square-root branch and Cauchy majorant on the quarter disk",
            "replayable geometric tail for the third derivative",
            "directed Horner evaluation over all seventy-eight chord cells and endpoint sliver",
            "coverage proof that the interval boxes fill the full central interval",
        ],
    },
    "central-reciprocal-slope-interval-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReciprocalSlopeCurvature.lean", "EtaJetReconstruction.lean"],
        "missing_interfaces": [
            "trusted directed Decimal arithmetic or independent certificate replay",
            "eta through second derivative and digamma/trigamma tail theorems",
            "exact rational Bernoulli and pi enclosures",
            "sound nonlinear source differentiation and all seventy-eight midpoint gap boxes",
        ],
    },
    "central-separated-rank-three-loewner-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["DiagonalCongruencePositivity.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "directed centered Xi jet through the required high degree",
            "divided-difference interval arithmetic with analytic tail bounds",
            "three-by-three determinant interval evaluation for the selected triple and full grid",
            "proof that the repaired coefficient dependency preserves the continuum certificate",
            "continuum between-grid positivity, which the finite grid does not imply",
        ],
    },
    "central-source-analytic-fourth-jet.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean", "EtaJetReconstruction.lean"],
        "missing_interfaces": [
            "typed truncated Taylor algebra for the central source operations",
            "separate transported eta composition jet and partial eta-s derivative jet",
            "directed interval coefficients with Euler and polygamma tails",
            "formal supersession of the cancellation-amplified high-derivative estimate",
        ],
    },
    "central-xi-log-boundary-jet-interval-certificate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "directed order-thirteen centered Xi logarithmic jet",
            "descent of the odd q-series through t equals q squared",
            "depth-three-hundred eta and recurrence-one-thousand digamma remainder replay",
            "exact-integer Euler denominators and internal parity certificate",
            "interval propagation through F and the inverse-square-root branch",
        ],
    },
    "central-xi-log-curvature-continuum-reduction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["EvenJetObservability.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "analytic centered Xi logarithm on a specified zero-free domain",
            "formal chain-rule identities through the fourth and fifth logarithmic derivatives",
            "inverse-square-root second and third derivative formulas with positivity domain",
            "outward Taylor models covering the full central interval",
        ],
    },
    "reduced-source-central-decimal-concavity-resolution.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReciprocalSlopeCurvature.lean", "EtaJetReconstruction.lean"],
        "missing_interfaces": [
            "sound arbitrary-precision eta, digamma, and logarithmic-derivative evaluator",
            "explicit Euler-transform, differentiation, and truncation remainder bounds",
            "directed replay of the twenty-one midpoint chord inequalities",
            "continuum coverage beyond the finite sampled chords",
            "global Loewner positivity, which the numerical scan does not establish",
        ],
    },
    "reduced-source-loewner-two-point-conditioning.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteHausdorffMoments.lean", "DiagonalCongruencePositivity.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "correlated interval evaluation of the source value, derivative, and divided difference",
            "analytic diagonal extension of the two-point Loewner determinant",
            "directed enclosure overcoming quadratic near-diagonal cancellation",
            "source-kernel representation avoiding subtraction of nearly equal quantities",
            "continuum and higher-rank Loewner positivity, neither implied by the scan",
        ],
    },
    "reduced-source-reciprocal-slope-broad-boundary-scan.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["ReciprocalSlopeCurvature.lean", "ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "certified boundary-slope evaluator across the fourteen-decade sample range",
            "directed error bounds separating roundoff from genuine negative chord gaps",
            "central-coordinate interval expansion near the zero endpoint",
            "proof connecting the finite endpoint grid to continuum concavity",
            "global Pick positivity, which the scan does not establish",
        ],
    },
    "reduced-source-reciprocal-slope-concavity-scan.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ReciprocalSlopeCurvature.lean", "ReducedEndpointPick.lean"],
        "missing_interfaces": [
            "analytic positive source derivative on the scanned boundary domain",
            "certified normalized imaginary-boundary-value evaluator",
            "directed transform-depth and boundary-height error enclosures",
            "formal replay of all thirty-six midpoint chord comparisons",
            "continuum concavity and the full matrix-valued Loewner hierarchy",
        ],
    },
    "quarter-shift-derives-seven-eighths-boundary-constant.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["QuarterPointJetConversion.lean"],
        "missing_interfaces": [
            "complex logarithmic Gamma branch and Stirling imaginary-part asymptotic",
            "formal substitution of the quarter shift and scaling by one half",
            "argument-principle zero-count formula with its separate topological base term",
            "typed asymptotic remainder arithmetic establishing the seven-eighths constant",
            "zeta-argument fluctuation term, which is deliberately not reconstructed",
        ],
    },
    "quarter-shifted-moment-jacobi-operator.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["MomentCompanionCore.lean", "FiniteStieltjesMoments.lean", "JacobiDeterminantRatio.lean"],
        "missing_interfaces": [
            "orthonormal Legendre recurrence with the stated normalized coefficients",
            "finite prime-shell measure and Gram--Schmidt Jacobi construction",
            "self-adjoint countable direct sum on its maximal weighted domain",
            "compact-resolvent theorem from finite blocks escaping to infinity",
            "source-derived nonlocal transform to completed Xi, which remains absent",
        ],
    },
    "quarter-shifted-prime-shell-trace-class-correspondence.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteStieltjesMoments.lean", "CompletionNeutrality.lean"],
        "missing_interfaces": [
            "prime-number-theorem shell-mass asymptotic with summable weighted error",
            "second-order asymptotic comparison proving uniqueness of the negative quarter shift",
            "Schatten trace-class and Hilbert--Schmidt criteria for diagonal relative covariance",
            "infinite weighted shell-radial isometry and orthogonal fluctuation decomposition",
            "exact Euler cross-functional decomposition retaining individual prime phases",
        ],
    },
    "prime-coupling-spectral-shift-target.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["CompletionKernel.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "source-derived self-adjoint arithmetic perturbation with controlled domain",
            "trace-class or other declared resolvent-difference determinant class",
            "spectral-shift theorem and boundary phase convention",
            "perturbation determinant identity with the zeta boundary factor",
            "the resulting real-axis divisor conclusion, which is a strengthened Hilbert--Polya target",
        ],
    },
    "prime-exponent-divisor-Hilbert-metric.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["IncidencePullbackMetric.lean", "FiniteEulerGram.lean"],
        "missing_interfaces": [
            "finite exponent-chain zeta matrix and first-difference inverse",
            "Kronecker factorization over a finite prime box",
            "identification of the pulled-back inner product with the matrix D-star-D metric",
            "incomplete infinite tensor-product reference data and convergence",
            "physical relative-chain pushforward and Xi reflection-defect identification",
        ],
    },
    "prime-fredholm-determinant-and-critical-line-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["PrimeOscillatorIncidence.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "diagonal operator on ell-two of primes and its trace-class criterion",
            "Fredholm determinant product theorem in the half-plane of convergence",
            "termwise logarithmic differentiation to the von Mangoldt series",
            "divergence of the prime harmonic series proving critical-line Hilbert--Schmidt failure",
            "joint prime--archimedean regularization rather than analytic-continuation-by-transport",
        ],
    },
    "prime-heat-moment-flow-and-variance-dissipation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteStieltjesMoments.lean", "NewmanSpectralHeatSeparation.lean"],
        "missing_interfaces": [
            "summability and all-order termwise differentiation of the damped von Mangoldt series",
            "pushforward positive measure on squared logarithmic displacement",
            "quotient-rule derivation of normalized variance dissipation",
            "all-degree polynomial Hankel quadratic-form differentiation",
            "simultaneous archimedean heat flow needed for completed positivity",
        ],
    },
    "prime-moment-ellipse-double-contact-obstruction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteHausdorffMoments.lean", "FiniteEulerGram.lean"],
        "missing_interfaces": [
            "convergent damped von Mangoldt measure and its first four logarithmic moments",
            "weighted Cauchy--Schwarz and Jensen derivation with equality conditions",
            "typed completed endpoint-plus-gamma contact jets",
            "directed interval enclosures for the exclusion inequalities",
            "fixed-support multiplicative phase constraints beyond moment feasibility",
        ],
    },
    "prime-phase-block-hankel-contact-hierarchy.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteHausdorffMoments.lean", "DiagonalCongruencePositivity.lean", "FiniteEulerGram.lean"],
        "missing_interfaces": [
            "complex finite or summable Gram realization of the block Hankel matrix",
            "Schur-complement equivalence with the normalized contraction condition",
            "all-order character differentiation of twisted moments",
            "positive-semidefinite completion problem for partially specified contact jets",
            "support and multiplicative phase realization, not implied by abstract moment positivity",
        ],
    },
    "prime-ray-incomplete-tensor-sector-obstruction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CompletionNeutrality.lean", "TensorAnnihilationNoGo.lean"],
        "missing_interfaces": [
            "bosonic coherent vectors and their vacuum-overlap formula",
            "divergence of the sum over primes of one over p-minus-one",
            "incomplete infinite tensor products and inequivalent-sector criterion",
            "relative quasi-free implementability or Krein null-quotient replacement",
            "cutoff-compatible preservation of the oriented linear Euler cross channel",
        ],
    },
    "prime-support-inherited-degree-audit.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TwoPeriodicNormComplex.lean", "FiniteGroupNormDichotomy.lean", "PrimePrincipalIndependence.lean"],
        "missing_interfaces": [
            "integral Smith reduction computing the stated regular-fiber homology module",
            "annihilator and scheme-theoretic support of the resulting integer torsion module",
            "primary components recovering exact valuations",
            "factorization-through-cardinality theorem for arbitrary regular correspondences",
            "prime-free compositional source whose loci contain information beyond the supplied degree",
        ],
    },
    "prime-third-determinant-information-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["PrimeOscillatorIncidence.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "Schatten-q membership criterion for the prime diagonal family",
            "third regularized determinant product and holomorphic-family theorem",
            "nonvanishing proof from the factor moduli on the positive half-plane",
            "canonical analytic low-order counterterms C-one and C-two",
            "reflection-compatible completed relative determinant retaining zero information",
        ],
    },
    "prime-trace-offdiagonal-free-resolvent.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CrossResolventGram.lean", "FiniteEulerGram.lean", "MomentCumulantHostiles.lean"],
        "missing_interfaces": [
            "free one-dimensional resolvent kernel with distributional boundary vectors",
            "finite-cutoff prime-source Green matrix-element identity",
            "Stieltjes inversion and sign-changing cut-density proof",
            "cutoff-independent self-adjoint paired block with a common domain",
            "positive completed Schur complement containing gamma and endpoint channels",
        ],
    },
    "prime-trace-zero-resonance-bridge.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["LocalResidueKrein.lean", "PrimeOscillatorIncidence.lean"],
        "missing_interfaces": [
            "Euler logarithmic-derivative identity in the absolute-convergence half-plane",
            "theta completion and meromorphic continuation of the separated prime trace",
            "Hadamard product for completed Xi with its symmetric limiting convention",
            "residue transfer from Xi logarithmic derivative to the continued prime trace",
            "compact-resolvent operator realization, which the resonance statement does not supply",
        ],
    },
    "prime-two-t44-one-fold-rank-one-attack.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["AcyclicTailSchur.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "finite exponential formula and monotonicity for the level-forty-four kernel",
            "directed weighted Schur inequality for the integer comparison barrier",
            "endpoint-regular fixed-cube quadrature with a rigorous remainder",
            "positivity and oscillation ordering identifying the top odd mode",
            "directed even rank-one secular inequality beyond Nyström discovery evidence",
        ],
    },
    "weil-cauchy-euler-domain-map.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CrossResolventGram.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "Fourier transform of the one-sided exponentially decaying half-line mode",
            "smooth compact-support approximation in the Weil test topology",
            "absolute Euler-domain convergence and continuity of archimedean distributions",
            "extended explicit-formula divided-difference kernel identity",
            "density and closability needed to pass from an indefinite preshape to a Hilbert realization",
        ],
    },
    "weil-explicit-formula-global-boundary-morphism.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["RadicalRepairObstruction.lean", "CompletionKernel.lean", "DiagonalCongruencePositivity.lean"],
        "missing_interfaces": [
            "Schwartz or compactly supported logarithmic test algebra with convolution involution",
            "centered Weil explicit formula with prime, gamma, endpoint, and symmetric zero regularization",
            "Hermitian radical quotient and indefinite completion typing",
            "Weil positivity criterion in both directions",
            "global positive descent, equivalent to RH and therefore not introduced as an assumption",
        ],
    },
    "weil-gaussian-character-coercivity-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["GaussianSmoothingThreshold.lean", "OffAxisHeatOscillation.lean"],
        "missing_interfaces": [
            "vertical-strip digamma real-part asymptotic with a uniform integrable remainder",
            "Gaussian translation and dominated-convergence proof of logarithmic character growth",
            "uniform absolute convergence and boundedness of the smoothed von Mangoldt cosine series",
            "continuity and coercive-minimum attainment for the completed source kernel",
            "two-variable uniformity when the smoothing parameter also varies",
        ],
    },
    "weil-gaussian-first-contact-rigidity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HermiteContactProfiles.lean", "GaussianSmoothingThreshold.lean", "NewmanSpectralHeatSeparation.lean"],
        "missing_interfaces": [
            "classical heat solution and Gaussian semigroup on the completed Weil distribution",
            "attainment of the threshold minimum at a finite character",
            "calculus theorem giving zero first derivative and nonnegative second derivative at the minimizer",
            "strict positivity of Gaussian convolution of a nonzero nonnegative function or measure",
            "broad positive regime and coercive tail control for the source specialization",
        ],
    },
    "weil-gaussian-positivity-semigroup-and-threshold.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GaussianSmoothingThreshold.lean", "NewmanSpectralHeatSeparation.lean", "OffAxisHeatOscillation.lean"],
        "missing_interfaces": [
            "Gaussian convolution semigroup and heat equation on the declared distribution space",
            "positive-kernel convolution preserving nonnegativity",
            "analytic substitution from the half-amplitude threshold to sigma equals one over four log two",
            "existence and topology of the completed Weil smoothing threshold",
            "zero-variance distributional limit and its RH-equivalent positivity conclusion",
        ],
    },
    "weil-negative-mass-entropy-and-contact-onset.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HermiteContactProfiles.lean", "GaussianSmoothingThreshold.lean"],
        "missing_interfaces": [
            "integrability of the negative part from character coercivity",
            "Kato convexity inequality for the heat semigroup",
            "moving-boundary differentiation for smooth negative intervals",
            "Taylor remainder and rescaling proof of the three-halves onset coefficient",
            "completed Weil distribution limit connecting entropy vanishing to RH",
        ],
    },
    "gaussian-carrier-gns-kernel-rh-equivalence.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["GaussianSmoothingThreshold.lean", "DiagonalCongruencePositivity.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "source-normalized completed two-variable Gaussian with endpoint, gamma, and prime terms kept coupled",
            "Gaussian product identity as a positive spectral-measure Gram representation",
            "positive-distribution reconstruction from every finite labelled Gram inequality",
            "analytic continuation identifying the reconstructed distribution with the Xi divisor",
            "universal Carrier-kernel positivity, equivalent to RH and therefore not assumed",
            "closable differentiated multiplication operator and self-adjoint realization on the reconstructed measure",
        ],
    },
    "gaussian-endpoint-boundary-spectrum-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GaussianNormTwo.lean", "FiniteUnitaryOrbitNoGo.lean", "BoundaryAdjointSeam.lean"],
        "missing_interfaces": [
            "Sobolev first-derivative operator with unitary endpoint boundary condition",
            "self-adjointness maximality theorem for the endpoint domain",
            "exact shifted arithmetic-progression spectrum from the unitary eigenphases",
            "linear Weyl counting law and finite-exponential-type determinant",
            "comparison with the Riemann--von Mangoldt T-log-T zero count",
        ],
    },
    "gaussian-quadratic-channel-cameron-martin-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GaussianNormTwo.lean", "MomentCumulantHostiles.lean", "TensorAnnihilationNoGo.lean"],
        "missing_interfaces": [
            "finite independent real Gaussian family and its moment-generating identity",
            "typed separation of bilinear second cumulant from Hermitian squared norm",
            "prime harmonic divergence excluding the critical sequence from Cameron--Martin space",
            "Wick exponential and proof that normalization removes the desired quadratic channel",
            "heat-smoothed square summability and a source-derived relative covariance counterterm",
        ],
    },
    "endpoint-centered-gamma-defect-gram-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteEulerGram.lean", "CrossResolventGram.lean"],
        "missing_interfaces": [
            "positive singular gamma log-time measure on the positive half-line",
            "square-integrability of endpoint-centered exponentials at zero and infinity",
            "Bochner integral construction of the finite defect Gram",
            "cancellation identity for the individually divergent Bernstein terms",
            "bounded prime-evaluation map or positive completed Schur complement",
        ],
    },
    "endpoint-negative-energy-atom-shifted-kernel-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteStieltjesMoments.lean", "CompletedKernelSectorNoGo.lean", "DiagonalCongruencePositivity.lean"],
        "missing_interfaces": [
            "bilateral Laplace representation of the completed endpoint heat term",
            "time-addition kernel theorem reconstructing a positive measure",
            "generator differentiation identifying the shifted kernel with support weighting",
            "Stieltjes support theorem requiring both ordinary and shifted kernel positivity",
            "completed gamma--prime coupling that cancels the negative endpoint direction",
        ],
    },
    "euler-cauchy-span-totality.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteObservation.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "positive analytic Xi Pick kernel on the upper half-plane",
            "reproducing-kernel Hilbert space and evaluation-vector theorem",
            "identity theorem for analytic functions in the RKHS",
            "source Mellin-mode isometry on the open Euler subdomain",
            "Pick positivity premise, equivalent to RH and not proved by totality",
            "physical coefficient--Betti boundary map, which remains distinct from analytic density",
        ],
    },
    "euler-gamma-stieltjes-sign-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CompletedKernelSectorNoGo.lean", "FiniteStieltjesMoments.lean", "LocalResidueKrein.lean"],
        "missing_interfaces": [
            "completed Xi logarithmic derivative with fixed gamma and pole conventions",
            "absolute Euler-series identity in the half-plane y greater than one half",
            "joint cancellation of the zeta-pole and polar logarithmic singularities",
            "theta continuation across the Euler boundary",
            "Stieltjes inversion and atomic support identification, whose desired specialization is RH-equivalent",
        ],
    },
    "archimedean-boundary-phase-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GaussianNormTwo.lean", "BoundaryRealStructurePhaseNoGo.lean", "FiniteUnitaryOrbitNoGo.lean"],
        "missing_interfaces": [
            "Stirling expansion for the Riemann--Siegel gamma phase",
            "smoothed counting constant for the first-order endpoint operator",
            "classification of self-adjoint quasi-periodic endpoint domains",
            "independent metaplectic, Maslov, or real-structure derivation selecting the eighth phase",
            "compatibility with the prime-side adjoint involution and compact-resolvent construction",
        ],
    },
    "archimedean-theta-completion-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["LogarithmicChartBoundary.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "real-line embedding of the integral lattice and self-dual Haar normalization",
            "Fourier transform of the self-dual Gaussian and Poisson summation",
            "Mellin transform with convergence in the initial half-plane",
            "split-integral continuation proving entireness and the functional equation",
            "source-derived bridge from finite Carrier data to the admitted archimedean realization",
        ],
    },
    "mellin-cauchy-jet-totality.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean", "LocalResidueKrein.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "one-sided Mellin transform and all normalized Cauchy derivatives",
            "Xi divisor with local multiplicities and square-summable reciprocal-square bound",
            "normal convergence of the vector-valued meromorphic principal-part series",
            "identity theorem and uniqueness of every local principal part",
            "positive polarized jet completion conditional on real divisor support",
            "physical coefficient--Betti pushforward, which is not supplied by analytic totality",
        ],
    },
    "mellin-xi-jet-boundary-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EvenJetObservability.lean", "LocalResidueKrein.lean", "JacobiDeterminantRatio.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "ring of entire functions of order at most one and the CCM Mellin source map",
            "proof that saturation of the source range is exactly the principal Xi ideal",
            "localization lengths, associated-graded jet fibers, and entire Hermite interpolation",
            "canonical positive polarization of the Grothendieck residue form at real zeros",
            "closed normal diagonal operator with compact resolvent and Hilbert--Schmidt inverse",
            "second regularized determinant and paired canonical-product identity with theta normalization",
            "self-adjointness equivalence with RH, stated as a criterion rather than assumed",
        ],
    },
    "sommerfeld-compact-jacobi-quantization-program.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteStieltjesMoments.lean", "JacobiDeterminantRatio.lean", "MomentCompanionCore.lean"],
        "missing_interfaces": [
            "all-order completed source moments and positive compact Jacobi realization",
            "decay of the Jacobi recurrence coefficients to zero",
            "discrete WKB theorem producing the compact-edge T-log-T counting law",
            "source-derived prime boundary phase and self-adjoint boundary condition",
            "trace-class limit, multiplicity convention, and simplicity distinction",
            "directed coefficient certificates beyond the finite numerical scout",
        ],
    },
    "sommerfeld-jacobi-pade-phase-bypass.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["JacobiDeterminantRatio.lean", "FiniteStieltjesMoments.lean", "MomentCompanionCore.lean"],
        "missing_interfaces": [
            "finite tridiagonal continuant recurrence for det of identity plus h times J",
            "spectral theorem locating every positive-Jacobi determinant zero on the negative axis",
            "boundary argument convention and exact pi jump at each pole",
            "replayable five-corner numerical coefficient and residual certificate",
            "strong or resolvent convergence to a canonical infinite self-adjoint Jacobi limit",
            "identification of the limiting Weyl function with the completed Xi resolvent",
        ],
    },
    "sommerfeld-prime-phase-abel-boundary-obstruction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["PrimeOscillatorIncidence.lean", "PrimeCutoffAnomaly.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "Euler-product logarithm and imaginary-part prime-power phase in absolute convergence",
            "divergence or cutoff-instability theorem beyond the boundary sigma equals one",
            "canonical Abel boundary value with fixed approach and logarithm branch",
            "agreement of an explicit-formula regularization with the Jacobi Weyl boundary phase",
            "uniqueness modulo integer multiples of pi across admissible source regularizations",
        ],
    },
    "intrinsic-formal-euler-product.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["PrimePrincipalIndependence.lean", "PrimeOscillatorIncidence.lean"],
        "missing_interfaces": [
            "conditional initial-semiring theorem and its intrinsic irreducible locus",
            "coefficientwise completed multiplicative monoid algebra",
            "finite-factorization support condition for infinite formal sums and products",
            "unique-factorization coefficient proof of the global formal Euler identity",
            "rank-one formal determinant and geometric-series interpretation",
            "analytic character evaluation in the absolute-convergence half-plane",
        ],
    },
    "intrinsic-prime-scattering-continuation-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["PrimeOscillatorIncidence.lean", "PrimeCutoffAnomaly.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "ell-two space on the intrinsic prime locus and its unbounded diagonal number operator",
            "trace-class criterion and Fredholm determinant Euler product for real part greater than one",
            "conjugation-compatible determinant and unitary scattering quotient",
            "logarithmic derivative carrying the complete prime-power trace",
            "critical-line Hilbert--Schmidt obstruction from prime harmonic divergence",
            "noncircular renormalization and boundary quantization converting continued resonances into spectrum",
        ],
    },
    "paired-gluing-determinant-mechanism.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AcyclicTailSchur.lean", "RankOneDeterminantNoGo.lean", "DiagonalCongruencePositivity.lean"],
        "missing_interfaces": [
            "finite positive block square roots and normalized coupling operator",
            "general block Schur determinant and norm-contractivity positivity equivalence",
            "holomorphic reflected operator family with adjoint real structure",
            "determinant-class infinite-dimensional product and domain control",
            "source-derived prime--archimedean coupling with determinant Xi",
            "off-critical invertibility, an RH-strength conclusion not assumed",
        ],
    },
    "paired-selector-refinement-versus-simultaneous-spectrum.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiberSelectorDescent.lean", "SelectorDataProcessing.lean", "CoorientationSelector.lean"],
        "missing_interfaces": [
            "finite group selector stabilizers and their normal cores",
            "normal-core preservation of intersections",
            "operation spectrum associated to a terminal kernel",
            "exact cyclic-six kernels of orders two and three and the index-one-through-twenty-four replay",
            "Betti relative-chain map or physical pairing, which neither selector construction supplies",
        ],
    },
    "logarithmic-degree-prime-green-commutator-is-indefinite.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BoundaryCommutatorInvariant.lean", "PrimePhaseEnergy.lean", "FiniteEulerGram.lean"],
        "missing_interfaces": [
            "explicit complex two-dimensional prime transport and logarithmic-degree matrices",
            "Hermitian eigenvalue calculation for both transport quadratures",
            "Mellin phase covariance of the compressed transport",
            "source derivation of the two-sheet all-prime current before aggregation",
            "equal-coefficient reciprocal sewing needed to cancel the residual phase",
        ],
    },
    "logarithmic-prime-oscillator-covariance-cancellation.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["PrimeCutoffAnomaly.lean", "GaussianNormTwo.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "prime Mertens asymptotic with its finite constant",
            "quarter-shifted harmonic oscillator trace expressed through digamma",
            "floor-logarithm cutoff comparison and asymptotic finite-part limit",
            "digamma value at one quarter with fixed normalization",
            "relative Gaussian or Krein determinant retaining the height-dependent bilinear phase",
        ],
    },
    "shell-kernel-coupled-positivity-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["AcyclicTailSchur.lean", "TwoRayShellSchurHostile.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "Hilbert--Schmidt operator and adjoint block construction on a Hilbert direct sum",
            "trace-class square and second regularized determinant",
            "singular-value product proof of det-two equal to det of identity plus B-star-B",
            "distinguished-source defect estimate versus full operator leakage distinction",
            "source-derived shell leakage operator satisfying the Hilbert--Schmidt premise",
            "completed determinant factorization retaining every discarded diagonal block",
        ],
    },
    "shell-leakage-positive-factor-zero-free-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RankOneDeterminantNoGo.lean", "TwoRayShellSchurHostile.lean", "DiagonalCongruencePositivity.lean"],
        "missing_interfaces": [
            "positive trace-class operator determinant and singular-value product",
            "real-axis strict nonvanishing of the Hilbert--Schmidt leakage Gram factor",
            "analytic-family continuation with no unsupported off-axis zero claim",
            "source factorization separating retained determinant from leakage normalization",
            "canonical self-adjoint retained generator carrying the actual zero spectrum",
        ],
    },
    "rank-three-loewner-vandermonde-continuum-reduction.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["DiagonalCongruencePositivity.lean", "FiniteHausdorffMoments.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "analytic central Loewner kernel with collision derivatives",
            "double Vandermonde divisibility of the symmetric determinant",
            "Newton divided-difference elimination and complete-homogeneous polynomial formula",
            "directed source coefficient and Cauchy-tail certificate on the central box",
            "replay of rank-three through rank-six interval LDL and Taylor transport certificates",
            "rank-uniform or global Loewner positivity, which is not claimed",
        ],
    },
    "rank-five-pivot-coordinate-monotonicity-target.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["DiagonalCongruencePositivity.lean", "FiniteHausdorffMoments.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "typed Newton--LDL recursion for the normalized five-point Loewner matrix",
            "directed Decimal interval arithmetic and centered multivariate Taylor algebra",
            "source degree-thirty-nine jet with one-shot analytic tail propagation",
            "all 3003 anchor derivative and Hessian certificates",
            "six-chart third-tensor cover and mean-value transport proof",
            "independent replay of the terminal global monotonicity certificate",
        ],
    },
    "rank-six-pivot-coordinate-monotonicity-target.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["DiagonalCongruencePositivity.lean", "FiniteHausdorffMoments.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "typed rank-six Newton--LDL pivots with all fifteen inverse floors",
            "directed source coefficients through degree forty-nine and certified Cauchy envelope",
            "versioned replay of 8008 pivot anchors and 48048 derivative intervals",
            "closed binomial source remainder and product-kernel arithmetic",
            "seven-chart third-tensor cover with linf transport geometry",
            "independent replay of the terminal rank-six continuum positivity theorem",
        ],
    },
    "positive-gluing-determinant-square-root-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FinitePfaffianNoGo.lean", "RankOneDeterminantNoGo.lean", "AcyclicTailSchur.lean"],
        "missing_interfaces": [
            "real-analytic nonnegative determinant family and even-order zero theorem",
            "smooth singular-value contact expansion at an interior maximum",
            "general Pfaffian square theorem for real skew-symmetric matrices",
            "determinant-line orientation selecting a signed square root",
            "source-derived metaplectic or Maslov orientation compatible with Xi multiplicities",
        ],
    },
    "positive-self-fourier-poisson-sewing-still-allows-off-critical-mellin-zeros.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["MomentCumulantHostiles.lean", "TensorAnnihilationNoGo.lean", "OffAxisHeatOscillation.lean"],
        "missing_interfaces": [
            "degree-twelve Hermite polynomial and exact Fourier-fixed eigenfunction calculation",
            "global lower bound selecting a strictly positive deformation parameter",
            "Mellin transform to the stated cubic window",
            "small-parameter negative-discriminant theorem and off-critical root transfer",
            "Poisson summation for the labelled positive Schwartz carrier",
            "source vacuum-selection operation rejecting the hostile excitation",
        ],
    },
    "positive-translate-labels-and-complete-moment-tower-do-not-constrain-the-divisor.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteObservation.lean", "EvenJetObservability.lean", "LiMobiusCocycle.lean", "MomentCumulantHostiles.lean"],
        "missing_interfaces": [
            "translated Gaussian Fourier transform and explicit off-axis zero formula",
            "uniform strict log-concavity from the finite slope-variance bound",
            "three-label Vandermonde recovery by moments zero through two",
            "entire-unit translation law preserving the divisor",
            "completed primal--dual labelled Poisson correspondence and boundary current test",
        ],
    },
    "the-doubled-tail-zero-domain-is-universal-and-admits-off-seam-hostiles.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TwoShellSpectralHostile.lean", "RankOneParsevalPhaseNoGo.lean", "TensorAnnihilationNoGo.lean"],
        "missing_interfaces": [
            "half-line tail integrals and differentiation under the integral sign",
            "equivalence of scalar vanishing with the single seam-incidence equation",
            "positive two-shell distributional hostile and smooth-bump perturbation",
            "staircase-augmented integration-by-parts identity on both reciprocal sheets",
            "theta-specific prime-exclusion recursion that would reject the universal hostile",
        ],
    },
    "the-gaussian-derivative-comb-current-reduces-to-one-seam-port.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GaussianNormTwo.lean", "PrimeTranslationAdjacency.lean", "EndpointQueryNormalForm.lean"],
        "missing_interfaces": [
            "scaled Gaussian annihilator and translation commutator",
            "label-paired parity cancellation of the odd derivative current",
            "termwise differentiation of the infinite Gaussian comb",
            "half-Mellin integration by parts with its seam evaluation",
            "reciprocal-sheet sewing deciding the orientation of the two seam ports",
        ],
    },
    "the-gaussian-vacuum-law-is-label-diagonal-and-cannot-orient-comb-cancellation.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TensorAnnihilationNoGo.lean", "FiniteObservation.lean", "EvenJetObservability.lean"],
        "missing_interfaces": [
            "Gaussian ground-state uniqueness for the annihilation differential equation",
            "transported annihilator under half-density dilation",
            "labelwise sampled Ward identity and arbitrary finite coefficient packets",
            "nonclosure of every finite even-moment tower under dilation evolution",
            "mixed oscillator--arithmetic commutator current before augmentation",
        ],
    },
    "the-staircase-green-identity-does-not-turn-a-zero-into-an-adjoint-state.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BoundaryCommutatorInvariant.lean", "TwoShellSpectralHostile.lean", "PrimePhaseEnergy.lean"],
        "missing_interfaces": [
            "right-continuous positive-jump staircase and Stieltjes integration by parts",
            "linear independence of scalar and staircase-weighted source functionals",
            "positive even two-shell off-seam witness with generic nonzero staircase port",
            "smooth narrow-bump stability of the hostile zero and adjoint failure",
            "theta-specific heat--staircase coupling that fails on the hostile source",
        ],
    },
    "one-time-derivative-off-axis-amplification-latency.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["OffAxisHeatOscillation.lean", "NewmanSpectralHeatSeparation.lean"],
        "missing_interfaces": [
            "all-order differentiated two-rate heat model",
            "phase-orbit theorem guaranteeing visits to a negative cosine sector",
            "quantitative derivative-order detection latency with ceiling and phase wait",
            "transfer from an off-critical Xi quartet to the squared complex heat rate",
            "Laguerre turning-region estimates and the expanding arithmetic horizon",
        ],
    },
    "one-time-hankel-jacobi-hilbert-polya-construction.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["FiniteStieltjesMoments.lean", "MomentCompanionCore.lean", "JacobiDeterminantRatio.lean"],
        "missing_interfaces": [
            "complete ordinary and shifted Hankel hierarchy for the one-time Xi heat derivatives",
            "radical quotient of the polynomial moment form and positive symmetric multiplication operator",
            "determinate Stieltjes moment problem from the asserted exponential moment",
            "canonical self-adjoint Jacobi closure and untilting of the measure",
            "completed logarithmic-resolvent identification and positive atomic residues",
            "the hierarchy premise, RH-equivalent and therefore not assumed as a proved source fact",
        ],
    },
    "two-low-order-channel-anomaly-target.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["PrimeOscillatorIncidence.lean", "MomentCumulantHostiles.lean", "AcyclicTailSchur.lean"],
        "missing_interfaces": [
            "third Schatten regularized determinant of the prime diagonal family",
            "finite-cutoff logarithmic series separating repetitions one, two, and at least three",
            "critical-line regularization of the two low-order channels without importing zeta",
            "coupled prime--gamma--endpoint determinant-line anomaly before scalarization",
            "relative complex whose finite torsion has the forced coefficients one and one half",
        ],
    },
    "two-variable-weil-gaussian-kernel-equivalence.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["GaussianSmoothingThreshold.lean", "FiniteEulerGram.lean", "OffAxisHeatOscillation.lean"],
        "missing_interfaces": [
            "centered Weil tempered distribution with fixed Fourier normalization",
            "Gaussian multiplication--convolution theorem on the declared test space",
            "spectral divisor measure formula conditional on RH",
            "source-side endpoint, gamma, and prime character kernels under one transform",
            "Gaussian approximate-identity limit and density of regularized Schwartz squares",
            "all-character positivity, equivalent to RH and therefore not assumed",
        ],
    },
    "phase-i-face-coproduct-idempotence.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PhaseICarrierObstructions.lean"],
        "missing_interfaces": [
            "finite thin category of octagon closed faces and inclusion arrows",
            "least-upper-bound coproduct formula from intersection of dissection constraints",
            "exact enumeration of 132 triangulations and support-excess witness 130",
            "categorical group completion of the idempotent coproduct monoid",
            "source-authorized multiplicity-bearing disjoint coproduct completion",
        ],
    },
    "phase-i-operation-inventory-closure.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PhaseICarrierObstructions.lean", "TensorAnnihilationNoGo.lean", "FiberSelectorDescent.lean"],
        "missing_interfaces": [
            "typed sum and product candidate inventory across Carrier, surface, coefficient, and state loci",
            "six-field admissibility predicate for a distributive Carrier multiplication",
            "exact obstruction vector with separately typed coordinates 130, 2, 1, and 2",
            "realization-invariance comparison across string and cosmology sectors",
            "new authority-bearing Carrier product, component injections, or revised Phase-I requirements",
        ],
    },
    "phase-i-surface-disjoint-union-typing.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PhaseICarrierObstructions.lean", "FiberSelectorDescent.lean"],
        "missing_interfaces": [
            "surface mapping-class groupoid with connected-component invariant",
            "symmetric monoidal disjoint union distinguished from categorical coproduct",
            "typed absence of both component-injection morphism classes",
            "finite component-count audit through eight powers",
            "source-authorized noninvertible component injections and universal mapping property",
        ],
    },
    "jacobi-gaussian-measure-to-weyl-limit-theorem.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["FiniteHausdorffMoments.lean", "FiniteStieltjesMoments.lean", "JacobiDeterminantRatio.lean"],
        "missing_interfaces": [
            "positive Gaussian quadrature measure for every Hausdorff corner",
            "weak compactness of fixed-mass measures on the compact interval",
            "Hausdorff moment determinacy and uniqueness of every subsequential limit",
            "normal-family proof of locally uniform Weyl convergence off the fixed cut",
            "identity-theorem identification with the completed source resolvent",
            "all-order corner positivity premise, not established by the finite certified corners",
        ],
    },
    "jacobi-positive-axis-monotone-resolvent-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AcyclicTailSchur.lean", "JacobiDeterminantRatio.lean", "FiniteStieltjesMoments.lean"],
        "missing_interfaces": [
            "compatible positive Jacobi extension by one row and column at every order",
            "operator block inversion and Loewner-order reversal under inversion",
            "uniform upper bound by the zeroth source moment",
            "pointwise monotone limit and inherited Stieltjes bounds",
            "local uniform convergence and completed source-resolvent identification",
        ],
    },
    "von-mangoldt-divisor-cocycle.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["IncidenceDivisorRotation.lean", "SelectedCocycleDescent.lean", "IncidencePullbackMetric.lean"],
        "missing_interfaces": [
            "positive-integer divisibility locally finite incidence algebra",
            "classical divisor sum of von Mangoldt equals logarithm",
            "common-scaling quotient of integer pairs by rational ratio",
            "Möbius inversion recovering the primitive coefficient with incidence retained",
            "physical relative-chain pushforward and Xi defect-norm identification",
        ],
    },
    "von-mangoldt-metric-divergence-matching-gate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["IncidencePullbackMetric.lean", "WeightedRigging.lean", "PrimeCutoffAnomaly.lean"],
        "missing_interfaces": [
            "PNT asymptotic for weighted prime logarithm sums across all alpha regimes",
            "quarter-shifted oscillator harmonic trace and floor-log cutoff comparison",
            "uniqueness of alpha equals two within the declared log-power metric family",
            "prime-power support restriction avoiding zeros of von Mangoldt",
            "source-derived weighted coefficient--Betti adjunction preserving the linear cross coefficient",
            "relative prime--gamma determinant after matched divergence cancellation",
        ],
    },
    "arithmetic-loewner-kernel-completion-conjecture.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["DiagonalCongruencePositivity.lean", "ReciprocalSlopeCurvature.lean", "MomentCumulantHostiles.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "source-defined Hilbert-space feature map for the completed prime--theta correspondence",
            "global Loewner Gram factorization on the full positive source domain",
            "minimal positive kernel completion and canonical self-adjoint resolvent generator",
            "integer-residue multiplicity amplification and symmetric regularized determinant Xi",
            "prime-power explicit trace identity with gamma and endpoint terms",
            "global positivity and off-central continuation, RH-equivalent and therefore not assumed",
        ],
    },
    "betti-boundary-defect-composition-law.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BoundaryCommutatorInvariant.lean", "TemporalAuthority.lean"],
        "missing_interfaces": [
            "graded chain complexes and degreewise pairing-forced Betti maps",
            "strict coefficient pullback composition implying strict Betti composition",
            "Leibniz expansion for the graded boundary defect",
            "injective and surjective side-condition survival lemmas",
            "explicit rank-one two-term cancellation hostile and five-site stagewise packets",
        ],
    },
    "boundary-defect-chain-homotopy-rigidity.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["BoundaryCommutatorInvariant.lean", "RepresentativeAnomaly.lean", "RadicalRepairObstruction.lean"],
        "missing_interfaces": [
            "graded chain-complex differentials with square-zero laws",
            "degree-raising homotopy and the standard chain-homotopy correction",
            "formal cancellation proving boundary-defect invariance",
            "cycle/cocycle selected-readout invariance",
            "pairing uniqueness obstruction to a non-homotopic repair map",
        ],
    },
    "broad-smoothing-uniform-weil-positivity-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["GaussianSmoothingThreshold.lean", "NewmanSpectralHeatSeparation.lean"],
        "missing_interfaces": [
            "uniform vertical digamma lower bound after Gaussian rescaling",
            "continuity, integrability, and coercivity of the translated log-kernel integral",
            "uniform exponentially small prime-series estimate at broad smoothing",
            "explicit constants and a concrete positive threshold",
            "threshold attainment and double-contact dichotomy using the completed source kernel",
        ],
    },
    "canonical-reserve-spectral-localization-theorem.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["FiniteHausdorffMoments.lean", "FiniteObservation.lean", "MomentCompanionCore.lean"],
        "missing_interfaces": [
            "polynomial Hilbert space with the x-dx reference inner product",
            "existence of the finite-dimensional Rayleigh minimizer",
            "weighted Vandermonde stability constant and positivity proof",
            "annihilator decomposition with quantitative norm bounds",
            "Christoffel or inverse-Hilbert boundary evaluation constants and Rouche root localization",
            "source-only all-order Hausdorff measure needed for the Riemann application",
        ],
    },
    "divisor-pushforward-Hilbert-norm-obstruction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["IncidencePullbackMetric.lean", "FiniteEulerGram.lean", "IncidenceDivisorRotation.lean"],
        "missing_interfaces": [
            "finite divisor zeta matrix and Mobius inverse",
            "exact Euclidean Gram entry floor of N over least common multiple",
            "positive diagonal-weight impossibility from shared multiples",
            "finite polar normalization and its nonlocality in the divisor basis",
            "physical Hilbert adjoint and Xi Hermitian-defect identification",
        ],
    },
    "eighth-phase-metaplectic-source-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GaussianNormTwo.lean", "BoundaryRealStructurePhaseNoGo.lean", "PhaseICarrierObstructions.lean"],
        "missing_interfaces": [
            "Stirling expansion through the one-over-t correction",
            "smooth zero-count extraction of the negative one-eighth phase",
            "mapping-class action on the conditional rank-one group completion",
            "symplectic and metaplectic lifts distinguishing a quarter rotation from the central sign",
            "richer physical coefficient--Betti fiber with a source-selected half-form line",
        ],
    },
    "explicit-two-variable-weil-heat-source-formula.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["GaussianSmoothingThreshold.lean", "FiniteEulerGram.lean", "OffAxisHeatOscillation.lean"],
        "missing_interfaces": [
            "centered Weil explicit formula with declared Fourier convention",
            "shifted Gaussian Schwartz substitution and exact polar endpoint evaluations",
            "digamma Gaussian integral and damped von Mangoldt cosine series",
            "common convergence and cutoff justification for all source terms",
            "all-character nonnegativity, an RH-equivalent target not proved by the identity",
        ],
    },
    "finite-euler-cutoff-selfadjoint-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PrimeOscillatorIncidence.lean", "GeometricSumSpectrum.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "finite prime Euler determinant as an entire exponential-polynomial family",
            "exact local vertical zero lattices and critical-coordinate transformation",
            "meromorphic-versus-entire characteristic determinant distinction",
            "proof that standard completion factors do not cancel nonzero local lattices",
            "uniform source-derived infinite renormalization, which the finite no-go leaves open",
        ],
    },
    "fixed-finite-rank-shell-height-dynamics-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteObservation.lean", "InfiniteModeRetention.lean", "CumulativeShellAllocation.lean"],
        "missing_interfaces": [
            "orthogonal projection error for exponential height vectors in ell-two of an interval",
            "harmonic reciprocal-prime shell-mass asymptotic",
            "linear independence of distinct exponentials via a Vandermonde derivative system",
            "exact first omitted orthogonal-polynomial norm and small-height expansion",
            "growing-rank schedule with locally uniform weighted error and derivative bounds",
        ],
    },
    "formal-euler-zero-free-boundary.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["PrimeOscillatorIncidence.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "conditional intrinsic formal Euler-product theorem",
            "absolutely summable complex character on the completed monoid algebra",
            "absolute logarithmic convergence and nonvanishing infinite-product theorem",
            "archimedean completion and functional-equation duality beyond the zero-free half-plane",
            "global operator or cohomology carrying the completed determinant",
        ],
    },
    "gamma-factor-even-oscillator-determinant.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["GaussianNormTwo.lean", "BoundaryRealStructurePhaseNoGo.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "self-adjoint harmonic oscillator on ell-two of the real line and its parity decomposition",
            "scaled even spectrum k plus one quarter and compact resolvent",
            "Hurwitz spectral zeta and its derivative at zero",
            "zeta-regularized determinant equal to square-root two-pi over Gamma",
            "relative prime interaction determinant retaining endpoint and pi factors",
        ],
    },
    "global-transfer-contractivity-conjecture.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["AcyclicTailSchur.lean", "RankOneDeterminantNoGo.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "canonical determinant-class prime--oscillator transfer family",
            "completed Xi determinant identity and reflection equivalence",
            "critical-line factorization as C-star-C",
            "strict off-line spectral-radius contractivity",
            "multiplicity-compatible unit singular-value crossings",
            "the contractivity clause, an RH-strength conclusion not assumed",
        ],
    },
    "growing-moment-generator-boundary-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["MomentCompanionCore.lean", "CumulativeShellAllocation.lean", "InfiniteModeRetention.lean"],
        "missing_interfaces": [
            "orthonormal Legendre Jacobi recurrence on the shifted unit shell",
            "exact top-boundary leakage coefficient and its one-sixteenth squared limit",
            "reciprocal-prime shell-mass asymptotic and divergence for every hard rank schedule",
            "distinction between one supported phase-vector error and full operator commutator leakage",
            "source-derived soft cutoff, Sobolev damping, or mapping-cone cancellation",
        ],
    },
    "integral-adjoint-pairing-lattice-obstruction.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AdjointDenominatorCancellation.lean", "RadicalRepairObstruction.lean", "BoundaryCommutatorInvariant.lean"],
        "missing_interfaces": [
            "integral pairing matrices and exact adjunction equation P-H times S equals Q-transpose times P-G",
            "column-lattice membership criterion for integral solvability",
            "Smith normal form row-divisibility test",
            "rank-one two-versus-one rational-adjoint hostile",
            "simultaneous physical kernel and cokernel audit for the five-site pairing",
        ],
    },
    "isometric-shell-gluing-identically-zero-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["OperatorTransportSquare.lean", "RankOneDeterminantNoGo.lean", "AcyclicTailSchur.lean"],
        "missing_interfaces": [
            "weighted shell embedding as a Hilbert-space isometry",
            "unitary dressing preserving C-star-C equal to identity",
            "determinant-class interpretation of the identically zero resonance factor",
            "height-independent unnormalized covariance ratio",
            "source-derived nonunitary height-dependent transfer defect before normalization",
        ],
    },
    "latent-log-time-squarefree-completion-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["SquarefreeWalshSpectrum.lean", "FiniteEulerGram.lean", "FiniteHausdorffMoments.lean"],
        "missing_interfaces": [
            "probability-space integral of bounded real latent features",
            "Walsh diagonalization of the squarefree convolution kernel",
            "nonnegative product-integrand proof for every character eigenvalue",
            "cutoff gamma log-time density normalization",
            "common endpoint finite part and negative prime evaluation as a positive Schur compression",
        ],
    },
    "linear-quadratic-shell-resonance-parity-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AdamsDoublingShellChannels.lean", "TwoRayShellSchurHostile.lean", "PrimeCutoffAnomaly.lean"],
        "missing_interfaces": [
            "quarter-shifted unit-shell integrals giving the sinc phase averages",
            "odd-pi evaluation of alternating versus ordinary harmonic shell sums",
            "impossibility of cancellation by a fixed scalar linear combination",
            "operator-valued within-shell moment or mapping-cone repair",
            "separate gamma-resolvent functional calculus, which the shell surrogate does not model",
        ],
    },
    "local-fock-confinement-is-broken-only-by-the-gaussian-boundary-coupling.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GaussianValuationTwoLevel.lean", "GeometricSumSpectrum.lean", "PrimeTranslationAdjacency.lean"],
        "missing_interfaces": [
            "infinite valuation shift and quadratic scale operator with quantum-plane relation",
            "finite geometric augmentation zero-modulus confinement",
            "open-sector infinite completion and zero-freeness",
            "Gaussian valuation weights and exact off-seam two-level zero location",
            "all-prime commuting family and reciprocal boundary compatibility cocycle",
        ],
    },
    "log-time-fourier-bridge-prime-atoms-gamma-resolvent.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["CrossResolventGram.lean", "PrimeOscillatorIncidence.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "half-line Laplace--Fourier integral for the gamma resolvent",
            "summation over quarter-shifted oscillator levels to the continuous digamma density",
            "discrete von Mangoldt log-time measure with critical weights",
            "common distribution/test-function space and endpoint finite part",
            "relative determinant whose logarithmic derivative is the completed Fourier-transformed measure difference",
        ],
    },
    "maximal-defect-annihilating-readout-space.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["RepresentativeAnomaly.lean", "BoundaryCommutatorInvariant.lean", "FiniteObservation.lean"],
        "missing_interfaces": [
            "graded cocycle spaces and adjoint of the next-degree boundary defect",
            "maximality proof for the cocycle annihilator readout subspace",
            "canonical restricted pullback to source cocycles",
            "explicit integral exact-cocycle representative anomaly fixture",
            "stronger exact-to-exact condition needed for cohomological descent",
        ],
    },
    "metaplectic-eighth-phase-candidate.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["GaussianNormTwo.lean", "BoundaryRealStructurePhaseNoGo.lean"],
        "missing_interfaces": [
            "damped Gaussian integral and principal boundary continuation to the Fresnel integral",
            "Maslov signature and metaplectic phase theorem for general real quadratic forms",
            "Xi boundary return map or Lagrangian intersection",
            "source-selected orientation and half-form line",
            "recovery of the full gamma factor rather than only its eighth-phase asymptotic",
        ],
    },
    "mobius-halfline-dilation-spectrum-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteUnitaryOrbitNoGo.lean", "BoundaryRealStructurePhaseNoGo.lean", "CumulativeShellAllocation.lean"],
        "missing_interfaces": [
            "conditional primitive Mobius carrier and orientation local system",
            "self-adjoint compactified dilation generator with periodic or antiperiodic domain",
            "exact arithmetic-progression spectrum and linear Weyl count",
            "Riemann--von Mangoldt comparison proving the T-log-T mismatch",
            "trigonometric determinant classification and richer source replacement",
        ],
    },
    "mod2-fiber-norm-homology-rank.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteGroupNormDichotomy.lean", "TwoPeriodicNormComplex.lean"],
        "missing_interfaces": [
            "finite quotient with uniform even fibers and formal pushforward/trace maps over F-two",
            "rank and kernel dimension of the all-ones fiber matrix",
            "homology dimension d-minus-two per fiber",
            "five-site k-bit census with d equals two-to-k and m equals two-to-five-minus-k",
            "source-derived physical relative-chain specialization",
        ],
    },
    "modulated-gaussian-is-an-exact-off-axis-hostile-source.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["OffAxisHeatOscillation.lean", "MomentCumulantHostiles.lean", "TensorAnnihilationNoGo.lean"],
        "missing_interfaces": [
            "positivity, Schwartz decay, and exact log-concavity derivative of the modulated Gaussian",
            "uniform perturbation bound with a concrete admissible epsilon and frequency",
            "Fourier transform factorization into a Gaussian and hyperbolic-cosine term",
            "explicit off-axis zero classification with reflection and conjugation packets",
            "labelled modular correspondence rejecting the hostile modulation before aggregation",
        ],
    },
    "natural-central-interval-jet-conditioning-no-go.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EtaJetReconstruction.lean", "ReciprocalSlopeCurvature.lean"],
        "missing_interfaces": [
            "directed interval Taylor propagation through the unreduced singular source formula",
            "replay of the first-cell enclosure spanning eleven orders of magnitude",
            "formal conditioning criterion distinguishing representation failure from mathematical negativity",
            "analytic even centered Xi logarithm constructed before interval substitution",
            "reduced source tail bounds for the replacement continuum certificate",
        ],
    },
    "newman-discriminant-lyapunov-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["NewmanSpectralHeatSeparation.lean", "LiDegreeTwoCoupling.lean", "FiniteHausdorffMoments.lean"],
        "missing_interfaces": [
            "differentiable polynomial family solving the backward heat equation",
            "smooth tracking of real simple roots",
            "root-velocity formula and logarithmic Vandermonde differentiation",
            "sum-of-squares Lyapunov identity at arbitrary finite degree",
            "source-canonical renormalized infinite discriminant compatible with Xi density and Newman flow",
        ],
    },
    "no-scalar-weighted-reduced-exclusion-energy-is-both-finite-and-gapped.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteObservation.lean", "WeightedRigging.lean", "CompletionKernel.lean"],
        "missing_interfaces": [
            "prime-indexed exclusion projections after common-vacuum subtraction",
            "diagonal eigenvalue formula as the sum over primes not dividing a label",
            "nonsummable-domain collapse and summable primorial escape proofs",
            "closed-range failure for the infinite-support summable regime",
            "product-valued exclusion profile and exact coupling to logarithmic degree",
        ],
    },
    "offline-quartet-gaussian-negative-lobe-and-latency.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["OffAxisHeatOscillation.lean", "GaussianSmoothingThreshold.lean"],
        "missing_interfaces": [
            "four-ordinate Gaussian divisor contribution from an off-critical zero quartet",
            "moving-character negative-lobe inequality at every positive scale",
            "inverse-time amplification and visibility estimates against a Weyl-size background",
            "tempered zero-density domination needed for eventual background overwhelm",
            "first finite double-contact consequence under continuity and coercivity",
        ],
    },
    "oriented-first-order-factorization-target.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["FinitePfaffianNoGo.lean", "OperatorTransportSquare.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": [
            "source-defined oriented square boundary map between equally ranked spaces",
            "analytic signed determinant and adjoint-square Gram identity",
            "chiral self-adjoint block operator with kernel decomposition",
            "source factorization of identity minus C-star-C as Q-star-Q",
            "relative coefficient--Betti boundary differential fixed before comparison with Xi",
            "the stronger factorization target, not implied by generic contractivity or positivity",
        ],
    },
    "pfaffian-noncircularity-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FinitePfaffianNoGo.lean", "RankOneDeterminantNoGo.lean", "OperatorTransportSquare.lean"],
        "missing_interfaces": [
            "analytic square-root existence and base-sign uniqueness for a nonnegative real-analytic function",
            "source-defined skew lift whose Pfaffian precedes rather than restates the determinant",
            "orientation data fixing the Pfaffian sign",
            "cutoff convergence compatible with the source determinant",
        ],
    },
    "pointed-pi0-self-dual-phase-cell.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["PhaseICarrierObstructions.lean", "LogarithmicChartBoundary.lean", "BoundaryRealStructurePhaseNoGo.lean"],
        "missing_interfaces": [
            "pointed ordered lattice and Pontryagin-dual construction",
            "self-dual Fourier normalization and phase-area quantization",
            "exact logarithmic cell-area integral and Weyl counting transfer",
            "metaplectic or boundary correction capable of producing the seven-eighths constant",
        ],
    },
    "quadratic-shell-phase-resonance-lattice.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AdamsDoublingShellChannels.lean", "TwoRayShellSchurHostile.lean", "PrimeCutoffAnomaly.lean"],
        "missing_interfaces": [
            "quadratic shell integral and exact sinc response",
            "classification of shell-center resonance points",
            "conditional or harmonic-series convergence used by the surrogate lattice",
            "source comparison separating the surrogate resonance set from gamma or Xi zeros",
        ],
    },
    "quartic-logconcave-carrier-is-a-nonperturbative-hostile-source.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["MomentCumulantHostiles.lean", "TensorAnnihilationNoGo.lean"],
        "missing_interfaces": [
            "steepest-descent analysis of the quartic Fourier transform",
            "rigorous real-axis oscillation and zero production",
            "formal statement of the retraction from an RH-hostile to a merely real-zero hostile source",
            "comparison with the modulated-Gaussian off-axis replacement",
        ],
    },
    "reduced-endpoint-finite-coupling-constant.md": {
        "coverage_disposition": "gated_missing_interfaces",
        "lean_evidence": ["EndpointPoleCancellation.lean", "ReducedEndpointPick.lean", "LocalResidueKrein.lean"],
        "missing_interfaces": [
            "Laurent expansion of the zeta logarithmic derivative at one",
            "digamma evaluation at one half and compatible logarithm normalization",
            "certified positivity of one plus half Euler gamma minus log of two square-root pi",
            "reflection-compatible spectral interpretation of the endpoint constant",
        ],
    },
    "reflection-decoder-augmentation-typing-audit.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteGroupNormDichotomy.lean", "TwoPeriodicNormComplex.lean", "ConstructorStableEndpoint.lean"],
        "missing_interfaces": [
            "free-vector-space augmentation kernel over an arbitrary finite constructor alphabet",
            "chain-homology identification with the fiberwise augmentation ideal",
            "naturality under alphabet maps and dimension change under strict refinement",
            "source-derived comparison proving presentation-independent physical support",
        ],
    },
    "relative-difference-quotient-and-arithmetic-weight-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["IncidencePullbackMetric.lean", "FiniteDifferenceCorrespondence.lean", "RelativeInjectivityResidue.lean"],
        "missing_interfaces": [
            "quotient-group isomorphism from diagonal orbits to differences",
            "Haar quotient and induced L-two unitary",
            "finite orbit-representative normalization of incidence pull-push",
            "typed arithmetic coefficient cocycle making representative dependence explicit",
        ],
    },
    "riemann-weyl-law-forces-logarithmic-shell-rank.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CumulativeShellAllocation.lean", "NewmanWeylEntropyBalance.lean", "TwoShellSpectralHostile.lean"],
        "missing_interfaces": [
            "Riemann--von Mangoldt counting asymptotic in the required normalized form",
            "summation theorem converting shell multiplicities to retained spectral count",
            "proof that the minimal Hilbert--Schmidt schedule is little-o of T log T",
            "source coupling moving local quadrature nodes to Riemann ordinates",
        ],
    },
    "scalar-weil-squarefree-determinant-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ReflectionMultiplicity.lean", "RankOneDeterminantNoGo.lean", "DeterminantalProfilePresentation.lean"],
        "missing_interfaces": [
            "Weil-form Hilbert completion conditional on positivity",
            "cyclic multiplication operator and simple point-spectrum theorem",
            "modified determinant product over distinct symmetric zeros",
            "comparison with the Xi divisor including multiplicities and the derivative-enhanced jet branch",
        ],
    },
    "schur-logarithm-unifies-two-prime-channels.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AcyclicTailSchur.lean", "PrimeCutoffAnomaly.lean", "FiniteSwapBlockDeterminant.lean"],
        "missing_interfaces": [
            "trace-class logarithmic determinant expansion with first two coefficients",
            "Schatten-three but non-Schatten-two classification of the critical prime operator",
            "joint relative supertraces of the first and second powers",
            "one reflection-compatible relative Schur family recovering Euler and critical-line regimes",
        ],
    },
    "selector-terminal-kernel-realization.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiberSelectorDescent.lean", "SelectorDataProcessing.lean", "CoorientationSelector.lean"],
        "missing_interfaces": ["arbitrary finite-group quotient selector and stabilizer proof", "core-of-stabilizer terminal-kernel theorem", "normal-subgroup lattice realization", "source admission of the quotient label as a physical observable"],
    },
    "selfadjoint-descent-positive-boundary-gate.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["CompletionKernel.lean", "CompletedKernelSectorNoGo.lean", "BoundaryRealStructurePhaseNoGo.lean"],
        "missing_interfaces": ["native Mellin multiplication model and dense-range theorem", "positive Weil-form radical quotient", "null invariance and closability of the spectral coordinate", "source-side positive factorization equivalent to Weil positivity and RH", "compact-resolvent self-adjoint realization"],
    },
    "semigroup-kernel-schur-weight-mismatch.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["AcyclicTailSchur.lean", "CrossResolventGram.lean", "PrimeCutoffAnomaly.lean"],
        "missing_interfaces": ["semigroup incidence operator and oscillator resolvent", "finite-cutoff coefficient-degree mismatch theorem", "critical-boundary failure of the square-root coupling", "two-boundary-channel resolvent retaining separate source and readout legs"],
    },
    "short-support-weil-block-gluing-gate.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["DiagonalCongruencePositivity.lean", "FiniteEulerGram.lean", "AcyclicTailSchur.lean"],
        "missing_interfaces": ["Burnol short-support positivity theorem", "local Weil Hilbert blocks and null-space quotients", "prime-two cross-operator contraction conjecture", "global compatible positive gluing beyond pairwise block positivity", "essential self-adjointness of the glued Mellin coordinate"],
    },
    "single-radial-shell-height-dynamics-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["TwoRayShellSchurHostile.lean", "CumulativeShellAllocation.lean", "PrimePhaseEnergy.lean"],
        "missing_interfaces": ["reciprocal-prime shell asymptotic measure", "exact sinc overlap and discarded-mass formula", "harmonic divergence of fixed-height leakage", "projective derivative and Berry-gauge minimization", "finite-moment shell residual lower bounds"],
    },
    "six-point-exceptional-readout-duality-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["ReflectionPairingAmbiguity.lean", "FiniteObservation.lean", "FiberSelectorDescent.lean"],
        "missing_interfaces": ["rank-eight dihedral representation fixture", "contragredient invariant-pairing construction", "rank-four bound for a trivial partner", "source-derived cycle representation and normalized physical pairing"],
    },
    "smoothed-prime-Hermitian-norm-gate.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["GaussianSmoothingThreshold.lean", "PrimePhaseEnergy.lean", "IncidencePullbackMetric.lean"],
        "missing_interfaces": ["prime harmonic divergence", "Gaussian log-prime summability for every positive heat time", "height-independence of the diagonal Hermitian norm", "off-diagonal relative kernel with a renormalized diagonal"],
    },
    "soft-moment-cutoff-weyl-tradeoff-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["CumulativeShellAllocation.lean", "NewmanWeylEntropyBalance.lean", "WeylLatticeTangentDivergence.lean"],
        "missing_interfaces": ["Jacobi commutator formula for diagonal tapers", "Cauchy--Schwarz transition lower bound", "weighted harmonic divergence for Weyl-sized taper width", "typed null paired sector removing auxiliary modes from physical counting"],
    },
    "source-gns-quarter-shift-no-shortcut.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["FiniteStieltjesMoments.lean", "FiniteHausdorffMoments.lean", "MomentCompanionCore.lean", "CompletedKernelSectorNoGo.lean"],
        "missing_interfaces": ["completed endpoint-cancelled source functional", "all-degree ordinary and shifted polynomial positivity equivalent to RH", "GNS null quotient and nonnegative multiplication operator", "moment determinacy and canonical self-adjoint realization", "source-derived square identity before spectral interpretation"],
    },
    "spectral-shift-localizes-to-two-channel-anomaly.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["PrimeCutoffAnomaly.lean", "AcyclicTailSchur.lean", "RankOneDeterminantNoGo.lean"],
        "missing_interfaces": ["Schatten-three prime operator and third regularized determinant", "nonvanishing of the regularized background", "joint linear/quadratic relative torsion with coefficients one and one half", "gamma-endpoint renormalization", "self-adjoint perturbation determinant realizing the residual spectral shift"],
    },
    "squarefree-positive-completion-theorem.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["SquarefreeWalshSpectrum.lean", "DiagonalCongruencePositivity.lean", "FiniteEulerGram.lean"],
        "missing_interfaces": ["arbitrary-dimensional Boolean-cube Walsh diagonalization", "product completion iff every edge is contractive", "sparse-kernel ell-one positivity criterion", "canonical source construction of the mixed completion correlations"],
    },
    "translation-invariant-compact-resolvent-no-go.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["FiniteUnitaryOrbitNoGo.lean", "WeylLatticeTangentDivergence.lean", "CompletionKernel.lean"],
        "missing_interfaces": ["Fourier diagonalization of translation-invariant operators on noncompact LCA groups", "noncompactness of nonzero multiplication operators on nonatomic L-two spaces", "resolvent transfer under Fourier equivalence", "source-derived confinement or resonance alternative"],
    },
    "theta-collision-is-stationary-half-transform-phase.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HalfTransformCollision.lean", "ThetaZeroFlowPropagation.lean"],
        "missing_interfaces": [
            "construction of C, S, and M from the completed-theta half-transform integrals",
            "differentiability and logarithmic phase-velocity identity on the non-origin chart",
            "source-specific proof that the cosine-zero locus has S-times-M nonzero",
            "the stronger positive-product sign requested in the graph handoff, which conflicts with the packet's explicit no-common-sign scope",
            "analytic realization of the algebraic odd two-atom endpoint sample at odd multiples of pi over L",
        ],
    },
    "monotone-theta-source-excludes-half-transform-origin-crossings.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HalfTransformCollision.lean", "ThetaZeroFlowPropagation.lean"],
        "missing_interfaces": [
            "formal completed-theta density and proof of strict decrease on the positive half-line",
            "positive layer-cake measure including the endpoint atom and its total-mass identity",
            "Fubini and complex exponential factorization of the truncated half-transform",
            "strict upper-half-plane triangle inequality from mass away from zero",
            "real-axis proof that the sine coordinate is strictly positive for every positive frequency",
            "the remaining source-specific nonvanishing theorem for the position-weighted sine coordinate on the cosine-zero locus",
        ],
    },
    "minimum-phase-monotone-sources-can-have-tangent-cosine-zeros.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HalfTransformCollision.lean", "ThetaZeroFlowPropagation.lean"],
        "missing_interfaces": [
            "formal piecewise monotone source on zero-to-pi-over-two and pi-over-two-to-three-pi-over-two",
            "exact trigonometric integration yielding C equals zero, S equals two, and M equals zero",
            "positive endpoint-bearing layer-cake representation of the step source",
            "upper-half-plane zero-freeness derived from the positive current measure",
            "a completed-theta curvature or labelled-coherence property absent from the hostile source",
        ],
    },
    "strict-log-concavity-does-not-exclude-cosine-collisions.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HalfTransformCollision.lean", "GaussianSmoothingThreshold.lean"],
        "missing_interfaces": [
            "exact integration formula for the exponential cosine transform on the unit interval",
            "reduction of the double-zero equations to the displayed two-equation system",
            "directed sine, cosine, cotangent, and exponential bounds at 5.1 and 5.2",
            "intermediate-value existence of the collision parameter in the fourth quadrant",
            "implicit-function continuation in epsilon with a certified neighborhood",
            "analytic proof that the continued sources remain positive, decreasing, minimum-phase, and tangent at nonzero half-transform value",
            "labelled modular theta coherence excluding the hostile redistribution",
        ],
    },
    "theta-collision-lifts-to-signed-labelled-current-coherence.md": {
        "coverage_disposition": "gated_active_conjecture",
        "lean_evidence": ["LabelledCollisionCoherence.lean", "BoundaryCokernel.lean", "AtomicScaleCurrent.lean"],
        "missing_interfaces": [
            "completed winding-labelled source decomposition with the exact logarithmic translate law",
            "signed derivative-current measure for every label including endpoint atoms",
            "justified differentiation and codiagonal interchange for the countable label family",
            "transport of integral-square orientation through differentiation and oscillatory integration",
            "source-derived cross-label cone, oriented-matroid covector, or constraint operator",
            "the active coherence theorem excluding simultaneous aggregate value and tangent cancellation",
        ],
    },
    "truncated-gaussians-have-an-infinite-exact-collision-family.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HalfTransformCollision.lean", "GaussianNormTwo.lean", "GaussianSeamSewing.lean"],
        "missing_interfaces": [
            "truncated Gaussian cosine and position-weighted sine integrals on the unit interval",
            "integration-by-parts derivation of the boundary identity from the Gaussian differential equation",
            "integer-frequency endpoint phase alignment at two-pi-k",
            "negative parameter derivative at A equals zero with its exact reciprocal-square coefficient",
            "large-A rescaling and dominated-convergence positivity limit",
            "intermediate-value construction of at least one positive collision parameter for every positive winding index",
            "labelled polynomial-Gaussian residual preventing value--tangent proportionality after modular codiagonalization",
        ],
    },
    "seam-matched-gaussian-score-is-the-phase-aligned-transverse-residual.md": {
        "coverage_disposition": "partial_lean_core",
        "lean_evidence": ["HalfTransformCollision.lean", "LogarithmicChartBoundary.lean", "GaussianSeamSewing.lean"],
        "missing_interfaces": [
            "completed-theta seam value and second derivative proving positive matched curvature",
            "analytic definition and first two seam-jet vanishings of the score residual",
            "integration-by-parts derivation of the residual boundary identity",
            "countable labelled residual decomposition with justified differentiation and summation",
            "exact logarithmic translate law identifying the abstract shear coordinate with log n",
            "one modular tail coordinate retaining omitted labels in every finite audit",
            "the active nonvanishing theorem for the residual sine transform on the phase-aligned cosine-zero locus",
        ],
    },
}


def classify(text: str) -> str:
    lowered = " " + re.sub(r"\s+", " ", text.lower()) + " "
    exact = any(marker in lowered for marker in EXACT_MARKERS)
    gated = any(marker in lowered for marker in GATE_MARKERS)
    if exact and gated:
        return "mixed_manual_split"
    if exact:
        return "eligible_exact_packet"
    if gated:
        return "gated_packet"
    return "manual_review"


def title_of(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def tags_for(name: str, text: str) -> list[str]:
    haystack = f"{name}\n{text}".lower()
    return [tag for tag, pattern in FAMILIES.items() if re.search(pattern, haystack)]


def theta_family_disposition(name: str, text: str, packet_status: str) -> dict[str, object] | None:
    """Return a conservative family-level disposition for an uncurated theta packet.

    A matching finite family core yields only ``partial_lean_core``.  It never
    discharges the listed analytic/source interfaces.  Strong conjecture
    markers take precedence, while unmatched packets remain explicitly gated
    instead of inheriting evidence by filename proximity.
    """
    if not name.startswith("theta-"):
        return None

    lowered = text.lower()
    is_active = any(re.search(pattern, lowered, flags=re.MULTILINE) for pattern in THETA_ACTIVE_PATTERNS)
    # Route by the packet's declared title slug, not incidental comparison
    # prose in its body.  Bodies routinely mention seams, Tate, or Schur as
    # rejected alternatives and must not acquire those families by proximity.
    haystack = name.lower()
    rules = [item for item in THETA_FAMILY_RULES if re.search(item["pattern"], haystack)]
    rule = rules[0] if rules else None
    family_candidates = [item["family"] for item in rules]
    family_evidence = list(
        dict.fromkeys(evidence for item in rules for evidence in item["lean_evidence"])
    )
    family_interfaces = list(
        dict.fromkeys(interface for item in rules for interface in item["missing_interfaces"])
    )

    if is_active:
        return {
            "coverage_disposition": "gated_active_conjecture",
            "coverage_basis": "theta_active_marker",
            "coverage_family_candidates": family_candidates,
            "lean_evidence": family_evidence,
            "missing_interfaces": [
                "the packet's explicitly conjectural or RH-equivalent source conclusion",
                *( ["a convention-fixed theorem statement separated from the conjectural conclusion"] if rule is None else family_interfaces ),
            ],
        }

    if rule is not None and packet_status in {"eligible_exact_packet", "mixed_manual_split"}:
        return {
            "coverage_disposition": "partial_lean_core",
            "coverage_basis": f"theta_family:{rule['family']}",
            "coverage_family_candidates": family_candidates,
            "lean_evidence": family_evidence,
            "missing_interfaces": family_interfaces,
        }

    if rule is not None:
        return {
            "coverage_disposition": "gated_missing_interfaces",
            "coverage_basis": f"theta_family:{rule['family']}",
            "coverage_family_candidates": family_candidates,
            "lean_evidence": family_evidence,
            "missing_interfaces": family_interfaces,
        }

    return {
        "coverage_disposition": "gated_missing_interfaces",
        "coverage_basis": "theta_unmatched_conservative_gate",
        "coverage_family_candidates": [],
        "lean_evidence": [],
        "missing_interfaces": [
            "a convention-fixed theorem statement separated from diagnostic or aspirational prose",
            "packet-specific coefficient, domain, normalization, and source-comparison interfaces",
            "a reviewed mapping to an existing Lean core or a new bounded formal theorem",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("research/grothendieck"))
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    records = []
    for path in sorted(args.root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        record = {
            "path": path.as_posix(),
            "title": title_of(text, path.stem),
            "packet_status": classify(text),
            "families": tags_for(path.name, text),
            "coverage_disposition": "unreconciled",
            "lean_evidence": [],
            "missing_interfaces": [],
        }
        record.update(CURATED_DISPOSITIONS.get(path.name, {}))
        if record["coverage_disposition"] == "unreconciled":
            record.update(theta_family_disposition(path.name, text, record["packet_status"]) or {})
        records.append(record)

    status_counts = Counter(record["packet_status"] for record in records)
    family_counts = Counter(tag for record in records for tag in record["families"])
    disposition_counts = Counter(record["coverage_disposition"] for record in records)
    coverage_basis_counts = Counter(
        record.get("coverage_basis", "explicit_curated_entry") for record in records
    )
    evidence_root = Path(__file__).resolve().parents[1] / "marici_formal" / "MariciFormal"
    missing_evidence_files = sorted(
        {
            evidence
            for record in records
            for evidence in record["lean_evidence"]
            if not (evidence_root / evidence).is_file()
        }
    )
    result = {
        "schema": "marici.grothendieck-lean-coverage-triage.v2",
        "certifies_coverage": False,
        "artifact_count": len(records),
        "status_counts": dict(sorted(status_counts.items())),
        "family_counts": dict(sorted(family_counts.items())),
        "disposition_counts": dict(sorted(disposition_counts.items())),
        "coverage_basis_counts": dict(sorted(coverage_basis_counts.items())),
        "curated_artifact_count": len(records) - disposition_counts["unreconciled"],
        "disposition_complete": disposition_counts["unreconciled"] == 0,
        "theta_family_routed_count": sum(
            1 for record in records if str(record.get("coverage_basis", "")).startswith("theta_family:")
        ),
        "theta_active_marker_count": coverage_basis_counts["theta_active_marker"],
        "theta_multi_family_count": sum(
            1 for record in records if len(record.get("coverage_family_candidates", [])) > 1
        ),
        "theta_unmatched_conservative_gate_count": coverage_basis_counts[
            "theta_unmatched_conservative_gate"
        ],
        "missing_evidence_files": missing_evidence_files,
    }
    if not args.summary:
        result["records"] = records
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
