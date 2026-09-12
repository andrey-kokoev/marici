# A Green Gram extension is local breakpoint recollement

## Inserting one context

Let \(S\subset\mathbb R\) be finite and insert a new point \(x\notin S\). The new state direction is the Green-orthogonal innovation

\[
r_{x\mid S}=k_x-P_Sk_x.
\]

It satisfies

\[
\langle r_{x\mid S},k_s\rangle=0
\quad(s\in S),
\]

or equivalently, by the reproducing property,

\[
r_{x\mid S}(s)=0
\quad(s\in S).
\]

Its squared norm is the positive Schur complement

\[
\|r_{x\mid S}\|^2
=1-K_{x,S}K_S^{-1}K_{S,x}>0.
\]

Thus each new context contributes exactly one independent interpolation defect.

## Nearest-neighbor locality

Suppose \(a<x<b\) are the nearest old context points around \(x\). Set

\[
\alpha=e^{-(x-a)},
\qquad
\beta=e^{-(b-x)}.
\]

The projection depends only on those two neighbors:

\[
P_Sk_x=c_ak_a+c_bk_b,
\]

where

\[
c_a=\frac{\alpha(1-\beta^2)}{1-\alpha^2\beta^2},
\qquad
c_b=\frac{\beta(1-\alpha^2)}{1-\alpha^2\beta^2}.
\]

The innovation norm is

\[
\|r_{x\mid S}\|^2
=
\frac{(1-\alpha^2)(1-\beta^2)}
     {1-\alpha^2\beta^2}.
\]

For every \(t\le a\), exponential multiplicativity gives

\[
k_x(t)=c_ak_a(t)+c_bk_b(t),
\]

and the same identity holds for every \(t\ge b\). Therefore

\[
\operatorname{supp}r_{x\mid S}\subseteq[a,b].
\]

The added Gram direction is a local Green spline confined to the newly refined interval.

## Recollement interpretation

For an interior insertion, the finite realization extension is

\[
0\to E_S\to E_{S\cup\{x\}}
\to\mathbb C\,r_{x\mid S}\to0.
\]

This is the Hilbert/Gram counterpart of the broken-Sobolev breakpoint extension

\[
0\to\mathcal D_S\to\mathcal D_{S\cup\{x\}}
\to\mathbb C_x\to0.
\]

The quotient cells have the same locality and rank:

```text
broken-domain side: new seam jump at x
Green-state side:   new interpolation innovation at x
```

They are not literally the same functional: one is a trace jump and the other is a Green-orthogonal spline. But the massive operator sends the spline to a distribution supported at the three local breakpoints \(a,x,b\), providing the comparison bridge between them.

## Boundary insertions

If \(x\) lies outside the convex hull of \(S\), only one nearest neighbor participates and the innovation has a half-line tail. Hence compact locality is specific to interior refinement. Endpoint growth must remain distinguished from internal breakpoint recollement.

## Verification

```text
python research/coherence/check_green_innovation_local_recollement.py
```

The exact-rational checker verifies the projection identities and positive Schur complement for 100 independently sampled pairs \((\alpha,\beta)\).

Artifacts:

- `check_green_innovation_local_recollement.py`
- `green-innovation-local-recollement.v1.json`
