# Constructive test of nontrivial-zeta-zero unconstructability, v1

## Question

Can the assertion “nontrivial zeros of the Riemann zeta function are unconstructable” be represented as an executable constructive claim, and what would a negative test establish?

## Claim boundary

The checked development distinguishes four propositions:

1. a certified critical-strip zero exists;
2. such a zero merely exists under propositional truncation;
3. a declared naming system names such a zero;
4. a declared algorithm semantics realizes a total certified selector.

None of these propositions is identified with another without a checked map. In particular, failure to find a name does not imply absence of zeros unless the naming system is point-complete. Failure of one algorithm semantics does not imply absence of a selector unless that semantics represents every selector in the stated class.

The development does not implement the Riemann zeta function on the critical strip and does not decide whether any actual zeta zero is constructible.

## Problem

An unqualified “unconstructable” predicate has no invariant meaning. It can refer to absence of a name, absence of a selector, absence of a certified witness, or absence of mere existence. These have different quantifiers and depend on different interfaces.

## Bold conjecture

A defensible executable version is relative:

> For a specified critical-strip naming system whose denotation and admissibility are fixed, no name denotes a point with certified analytically continued zeta value zero.

An intrinsic promotion requires point-completeness of that naming system. A selector version additionally requires a specified algorithm-code language, realization relation, and completeness for the selector class.

## Named rivals

- A finite numerical search establishes universal unconstructability.
- Nontermination of one zero-search program establishes universal unconstructability.
- Absence of names in an arbitrary language is intrinsic to the zeros.
- Positive finite Dirichlet truncations model analytically continued zeta zeros.
- An overlap-compatible function is automatically the analytic continuation.

## Risky consequences

The relative conjecture predicts all of the following.

- Changing the naming system can change constructibility while leaving the certified zero fixed.
- Changing algorithm semantics can change selector constructibility while leaving a total selector fixed.
- A finite positive Dirichlet surrogate has no zero and therefore no selector, but this result does not transfer to continuation values.
- A negative named-zero decision plus an independently certified zero refutes point-completeness of the naming system.
- Critical-strip testing cannot start from finite Dirichlet sums without a cofinal triangular approximation, certified tail control, an analytic continuation certificate, and an identity theorem.

## Strongest falsification attempt and residual

Checked countermodels establish:

- a certified zero coexists with no named zero for an empty naming system;
- the same problem has a named zero under the identity naming system;
- a total certified selector coexists with no constructible selector under empty-code semantics;
- the same selector is constructible under unit-code semantics.

These countermodels falsify invariant readings of “unconstructable” based only on one name language or algorithm semantics.

The strongest attempted analytic construction reaches the first missing typed object at certified complex negative powers. The required expression is structurally 

\[
(n+1)^{-s}=\exp\!\bigl(-s\log(n+1)\bigr).
\]

The repository now has complex completion arithmetic, checked completion-level real exponential, cosine, and sine, an assembled completion-level complex exponential, and a triangular series-completion interface. The sine construction includes rational Taylor terms, geometric tails, seed coherence, uniform input stability, canonical regularity, metric descent, and the zero law. It does not yet have a checked complex logarithm. Positive-natural logarithm work currently provides exact atanh partial sums, the transform `n/(n+2)`, its nonnegative complement, and a dyadic-gap convergence contract. The first missing proof is construction of a dyadic precision below that complement for every natural input. A direct transparent expansion of the negative-power expression through completion multiplication caused Agda normalization to exceed 240 seconds; that product law remains an explicit interface obligation rather than a theorem.

Acceptance test: finish the positive-natural logarithm tail schedule and metric value, define the checked negative-power expression using the existing complex exponential, prove its approximation bounds, instantiate `CertifiedNegativeSuccessorPowerKernel`, prove cofinal Dirichlet tail bounds on the right half-plane, and then supply analytic continuation plus uniqueness on an overlap reaching the critical-strip domain.

## Disposition

The universal assertion is not verified. Its unqualified form is rejected as underspecified by checked countermodels. The surviving claim is the relative naming-system proposition represented by `ConstructiveCriticalStripZeroTest`; its negative branch has only relative force unless point-completeness is separately proved.

The finite positive Dirichlet model is a negative control: it proves that the exclusion and selector machinery rejects a model whose zero set is empty. It supplies no evidence about zeros of analytically continued zeta.

## Executable evidence

Aggregate module:

- `research/voevodsky/agda/ConstructiveValueModel.agda`

Principal contracts and controls:

- `ZetaConstructibilityContract.agda`
- `ZetaZeroNamingContract.agda`
- `ZetaSelectorCountermodels.agda`
- `ComplexSeriesCompletion.agda`
- `TriangularComplexSeriesCompletion.agda`
- `ConstructiveZetaInterfaces.agda`
- `CriticalStripZeroContract.agda`
- `FiniteZetaExactExclusion.agda`
- `FiniteZetaNoSelector.agda`

Checked command:

```text
agda --transliterate -i research/voevodsky/agda -i research/voevodsky/agda/generated -i <cubical-0.9> research/voevodsky/agda/ConstructiveValueModel.agda
```

Reproducible checker and materialized result:

- `research/voevodsky/checkers/check_zeta_constructive_framework.py`
- `research/voevodsky/results/zeta_constructive_framework.json`

Latest result: `passed: true`, Agda exit status 0. The result file separately lists verified scope and nonverification boundaries.
