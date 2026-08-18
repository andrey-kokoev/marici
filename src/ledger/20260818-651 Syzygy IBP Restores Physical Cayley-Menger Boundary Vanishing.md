---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 651 — Syzygy IBP Restores Physical Cayley--Menger Boundary Vanishing

## Correction

Entry 649 tested the boundary behavior of the bare twist $K^\gamma$. That
is the correct test for a generic integration-by-parts vector field, but it
is not the test for the dimension-preserving IBP system used by the primary
source.

The source imposes the syzygy condition

\[
\sum_e n_e\,\partial_{y_e}K=n_0K.
\]

Thus the IBP vector field $V=\sum_en_e\partial_{y_e}$ is logarithmic along
the Cayley--Menger divisor:

\[
V(K)\in(K).
\]

At a generic smooth point of $K=0$, use $K$ as a normal coordinate.
The syzygy says that the normal component of $V$ is divisible by $K$.
Therefore the boundary flux of the primitive is not $K^\gamma$, but

\[
\boxed{K^{\gamma+1}}.
\]

## Physical exponent

For the homogeneous one-loop three-site sector,

\[
\gamma=\epsilon-\frac12.
\]

Hence the logarithmic-syzygy flux has normal order

\[
K^{\epsilon+1/2}.
\]

It vanishes whenever

\[
\operatorname{Re}\epsilon>-\frac12,
\]

and in particular at the physical value $\epsilon=0$:

\[
\boxed{K^{1/2}\longrightarrow0.}
\]

The dimension-preserving source IBP identities therefore do admit literal
boundary vanishing on a generic smooth Cayley--Menger face at physical
dimension. Meromorphic continuation is not needed for this local boundary
term.

## What remains from Entry 649

Entry 649 remains valid for unrestricted IBP numerators whose normal
component is not divisible by $K$. Its conclusion must not be applied to
the source's syzygy-loaded, dimension-preserving IBP subcomplex.

The correction does not by itself construct a canonical lift of Entry 650's
physical wall cocycle. Boundary vanishing proves that a source syzygy
primitive defines a legitimate relative homotopy. It does not prove that:

1. every required wall-cocycle representative is reached by that syzygy
   subcomplex;
2. two syzygy primitives differ by a relative-exact primitive;
3. the primitive remains logarithmic at intersections of $K=0$ with the
   marked denominator divisors or singular Cayley--Menger faces; or
4. the resulting class chooses an origin in the (mathcal T_7)-torsor.

## Classification

- existing carrier: the Cayley--Menger boundary (K=0);
- coefficient/chain datum: logarithmic tangent vector fields and their
  relative primitives;
- new carrier datum: none.

## Surviving frontier

Construct the actual source syzygy primitive for the closed three-wall
cocycle of Entry 648 and compute its class in the relative localization
complex. The finite falsifier is primitive independence: if two admissible
syzygy lifts differ nontrivially in (mathcal T_7), the lift torsor remains
unbased. If the difference is relative exact, the source IBP subcomplex
canonically selects the lift.

## Evidence

- Paolo Benincasa et al., arXiv:2408.16386, `method.tex`, equations
  `eq:IBP` and `eq:condition`;
- `research/benincasa/three-site-syzygy-ibp-boundary-audit.json`;
- epistemic event `ev-000000000250-dc37df19-7f11-4483-bec6-5f83376f6208`;
- Entries 648--650.

## Outcome contract

~~~json
{
  "claim": "The dimension-preserving source IBP primitive has nonvanishing Cayley-Menger boundary flux at the physical dimension.",
  "status": "falsified",
  "syzygy_condition": "V(K)=n_0 K",
  "physical_flux_order": "K^(1/2)",
  "generic_smooth_boundary_flux_vanishes": true,
  "canonical_T7_lift": "not yet constructed",
  "next_experiment": "Construct the source syzygy primitive for the Entry 648 cocycle and test primitive independence in the relative localization complex."
}
~~~
