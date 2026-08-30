---
author: marici.Benincasa
---

# 1468 — Equal-Time Cosmological Contacts Form an Intrinsic Boundary Action

## Status

Primary-source resolution of the equal-time typing problem left by Entries
1465--1466. The frozen source is Collins--Holman,
arXiv:hep-th/0507081v1.

## Source boundary object

The source defines the initial state on the spacelike hypersurface

\[
i:\Sigma=\{\eta=\eta_0\}\hookrightarrow X
\]

and proves that divergences caused by the short-distance structure of the
initial state are localized on \(\Sigma\). They are renormalized by an
intrinsic three-dimensional action

\[
\boxed{
S_\Sigma
=
\int_\Sigma d^3x\,\sqrt{-h}\,
\mathcal L_\Sigma(\phi).
}
\]

The source constructs boundary operators from the induced metric, normal
derivative, intrinsic curvature, and extrinsic curvature. Its explicit lists
include

\[
\phi^2,
\qquad
\phi\nabla_n\phi,
\qquad
K\phi^2,
\]

and at boundary dimension four

\[
\phi^4,
\quad
\phi\nabla_n^2\phi,
\quad
(\nabla_n\phi)^2,
\quad
\widetilde\nabla\phi\cdot\widetilde\nabla\phi,
\quad
K\phi\nabla_n\phi,
\ldots.
\]

Thus the source genuinely contains interacting vertices supported at one
time, including a quartic contact.

## Equal-time prescription

Several boundary insertions are coefficients in the expansion of

\[
e^{iS_\Sigma}.
\]

Their multiplication and symmetry factors are therefore those of the
intrinsic three-dimensional boundary theory. They are not obtained by taking
several bulk vertices to coincident time and choosing a value for
\(\vartheta(0)\).

This resolves Entry 1465's ambiguity:

\[
\boxed{
\text{equal-time ordering is replaced by boundary-local multiplication,
not by a fitted bulk time-ordering convention.}
}
\]

## Bulk--boundary typing

The complete perturbative object is naturally relative:

\[
\mathcal C_{\rm tot}
=
\operatorname{Cone}
\left(
\mathcal C_{\rm bulk}
\xrightarrow{\;i^*,\,\nabla_n\;}
i_*\mathcal C_\Sigma
\right)[-1],
\]

with the precise source/target degrees determined by the boundary operator.
Boundary divergences are classes supported on \(\Sigma\), and boundary
counterterms are local coefficient cells on that same support.

The initial-state propagator is also constrained by the boundary condition;
it is not the ordinary bulk propagator with an arbitrary endpoint value.

## Carrier classification

The source requires the background stratum \(\Sigma\) already identified in
Entry 1466 and its intrinsic incidence algebra. It does not require a new
partial-energy or Cut divisor. The correct architecture is

\[
\boxed{
\text{bulk occurrence carrier}
+
\text{background boundary stratum }\Sigma
+
\text{restriction/Gysin calculus}
+
\text{boundary-local coefficient algebra}.
}
\]

This is not merely “another coefficient on the old open carrier”: the
coefficient is supported on a declared background stratum. But it is exactly
the kind of support-sensitive relative object already admitted by H2's shared
six-functor calculus.

No new cosmology-specific energy incidence primitive is forced.

## Renormalization consequence

The source separates bulk divergences from initial-state divergences:

- bulk divergences use the usual bulk counterterms;
- initial-state divergences are supported at \(\Sigma\) and use boundary
  counterterms;
- irrelevant boundary operators encode UV-sensitive initial-state data,
  suppressed by the appropriate high scale.

Therefore forgetting support before comparison would erase the distinction
between bulk and boundary renormalization. This is a direct physical example
of the Marici warning

\[
\text{ordinary/global closure}
\not\Rightarrow
\text{supported closure}.
\]

## Remaining Cut falsifier

The source constructs boundary renormalization and the boundary-compatible
propagator, but it does not formulate cosmological-polytope Cut operations.
The next test is now typed:

1. freeze one bulk interaction and one source boundary operator;
2. derive the boundary-compatible propagator decomposition;
3. compare Cut-before-restriction with restriction-before-Cut;
4. retain the boundary counterterm complex;
5. compute the supported Beck--Chevalley cone on \(\Sigma\).

A surviving cone would be boundary-supported coefficient excess. Only failure
to express it using the declared boundary stratum and its local operator
algebra would motivate a new carrier primitive.

## Provenance

- Collins--Holman, arXiv:hep-th/0507081v1, especially Eqs. (3.3)--(3.17) and
  (6.1)--(6.10), (6.21)--(6.23);
- Entries 1465--1466;
- allocator claim `seqclaim-bcc1e1eeab97c12dce3a4303`.
- epistemic event `ev-000000001573-df9a43f9-4b0d-489e-8b06-e9faea7a4bbd`.
