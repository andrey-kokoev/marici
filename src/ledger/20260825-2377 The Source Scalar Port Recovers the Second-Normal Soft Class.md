---
author: marici.Benincasa
date: 2026-08-25
---

# 2377 — The Source Scalar Port Recovers the Second-Normal Soft Class

## Question

Entry 2376 proves that the supported diagonal survives as a global
positive-cut coefficient cycle. Does the actual frozen marked-relative source
factor annihilate that line?

Sequence claim: seqclaim-a43ec21be26d8528b01c304a.

## Source factor

Entry 2364 gives

\[
S(a,\xi)
=\frac{a+p}
{2p(p-a)^2(a+3p)(\xi+1)}.
\]

After \(a=pt\),

\[
\boxed{
S(t,\xi)
=\frac{t+1}
{2p^3(t-1)^2(t+3)(\xi+1)}.
}
\]

On the open physical chamber

\[
p>0,\qquad1<t<3,\qquad-1<\xi<1,
\]

this factor is strictly positive. The anti-trace form \(dt/w\) has one fixed
nonzero imaginary phase on the positive cut. Consequently the physical
source weights cannot cancel the transported cycle in the interior.

## Endpoint audit

The numerator \(t+1\) is nonzero at all four physical nodes. The source has
only the already declared marked poles:

\[
\begin{array}{c|c|c}
(\kappa,\xi,t)&\nu_{\xi+1}&\nu_{t-1}\\
\hline
(-1,-1,3)&-1&0\\
(-1,+1,1)&0&-2\\
(+1,-1,1)&-1&-2\\
(+1,+1,3)&0&0
\end{array}
\]

In particular, the unmarked node has the regular value

\[
\boxed{
S(3,1)=\frac1{24p^3}.
}
\]

This gives a support-independent unit witness that the source port does not
annihilate the node coefficient.

## Result

\[
\boxed{
\text{the zeroth scalar source port recovers the second-normal
soft-triangle line.}
}
\]

The new class is therefore not merely algebraic or supported bookkeeping. It
survives coefficient transport and is visible to an admitted physical scalar
readout.

## Classification

- support: existing soft and endpoint arrangement;
- coefficient: second-normal elliptic/conifold vanishing line;
- readout: visible to the frozen scalar marked-relative source;
- obstruction: none at this scalar port;
- new Carrier datum: none.

This is a nontrivial deformation of contextual faithfulness at one hostile
soft--triangle intersection: the first jet misses the class, but the
source-derived second-grade port recovers it.

## Scope

This does not derive the missing finite-\(q\) tensor vertex, polarization
ports, Ward identities, or the complete contact-weighted transfer matrix.
It therefore settles one scalar support intersection, not the full active
interacting/nonhomogeneous objective.

## Durable verification

- research/benincasa/check_soft_triangle_source_port_recovery.py;
- research/benincasa/soft-triangle-source-port-recovery.json;
- exact source-factor, valuation, sign, and unit checks;
- epistemic event
  ev-000000003256-0d889aaf-7595-4336-ad71-d1a21c754268.

## Next falsifier

Repeat the same second-normal recovery audit at the other frozen support
intersections and determine whether the complete scalar score tower remains
jointly faithful. The tensor/polarization branch remains gated on an
independently source-derived finite-\(q\) tensor completion.
