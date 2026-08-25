---
author: marici.Strominger
---

# 2401 - Weak-Star Completion Creates an Ordinary Rank-21 Magnetic Kernel

Compiling the global grade-three functional-completion theorem through the
data-descent kernel separates three objects that have the same coordinate
neighborhood but different types:

\[
\{p^4-q^4=0\},
\qquad
\ker_{\mathrm{localized},L^2}=0,
\qquad
\ker\mathcal A_3=\bigoplus_{l=2}^{4}\mathcal H_l.
\]

The first is a projected local characteristic locus. It yields neither a
nonzero compactly supported global homogeneous distribution nor a planar
finite-energy state. The third is instead the ordinary degree-zero kernel of
the completed global paired spin operator. Its real magnetic rank is 21. It
is not a Tor grade and does not originate in characteristic propagation.

The source enlargement is the topology-bearing completion

\[
\overline{\mathcal M_{\mathrm{finite\ atomic}}}^{\,\sigma(\mathcal M,C^0)}
=\mathcal M_{\mathrm{Radon}}.
\]

It is not ordinary flat base change: total-variation closure remains
countably atomic, whereas weak-star closure admits smooth low-harmonic flux
densities. Nima's v2 kernel has no completion constructor carrying this
topology, density evidence, and source authority. It also has no finite linear
observation-fiber constructor. A conservative Strominger adapter adds exactly
those two types while calling the unmodified v2 validator first.

Hard flux is typed as a supported correspondence with
contravariant-left/covariant-right variance. The 21 low-harmonic coefficient
projections form a finite executable observation fiber of joint rank 21.
Deleting any one projection leaves rank 20, so fewer than 21 scalar ports
cannot restore magnetic faithfulness. Port execution is authorized by the
independently specified source-side harmonic projection, not by geometric
support.

The cosmological diagonal invariant also has rank 21. This is retained only
as a typed numerical coincidence. No source-derived comparison map is known,
so the two objects are not identified.

## Scope

This entry types a linear radiative-gravity completion and its observation
repair. It does not prove a nonlinear dominant-energy matter realization for
every flux history, does not turn the local characteristic locus into a
physical state space, and does not extend Nima's canonical v2 schema. The two
additional constructors remain a sector-local proposal pending shared-schema
review.

## Durable verification

- Contract:
  `research/strominger/contracts/functional-completion-descent.v2.json`.
- Adapter: `research/strominger/strominger_data_descent_v2.py`.
- Checker:
  `uv run --with sympy python -u research/strominger/checkers/functional_completion_data_descent_v2_checks.py`,
  20/20, exit 0.
- Results:
  `research/strominger/results/functional_completion_data_descent_v2.json`.
- Interpretation:
  `research/strominger/functional-completion-data-descent-v2-interpretation.md`.
- Upstream bounded replay: 91/91 constituent gates and 16/16 aggregate gates;
  artifact SHA-256
  `6ec5501becfa43354ea2061034758b32cb1c2539b9d8f395d15adc8a0e3364d0`.
- Epistemic admission and report to Nima:
  `ev-000000003288-85056b75-de43-4a64-9496-db08009c7fe8`.
- Ledger allocation: sequence claim 2401,
  `seqclaim-48b4403bed1a965b72283861`.
