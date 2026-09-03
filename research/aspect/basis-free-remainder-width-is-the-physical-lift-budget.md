# Basis-free remainder width is the physical lift budget

## Question

Are a torsor coefficient radius \(M\) and omitted-route operator bound \(\varepsilon\) separately meaningful physical quantities?

## Coordinate dependence

Write admissible lift displacements as \(Vt\), with \(t\) measured in a chosen coordinate norm. Under a basis change \(V'=VS\), the coordinates become \(t'=S^{-1}t\). The numerical radius and induced operator bound generally change:

\[
M'\ne M,
\qquad
\|RV'\|\ne\|RV\|.
\]

In one dimension, rescaling the basis by \(\alpha\) sends

\[
M'=\frac{M}{|\alpha|},
\qquad
\varepsilon'=|\alpha|\varepsilon,
\]

so only the product \(\varepsilon M\) remains invariant when both quantities are transformed consistently.

## Intrinsic width

Let \(\mathcal A_0\) be the source-admissible set of lift displacements from a declared base lift. The basis-free omitted-route budget is

\[
\omega_R(\mathcal A_0)
=
\sup_{w\in\mathcal A_0}\|Rw\|.
\]

The exact confinement gate is

\[
q_0+\omega_R(\mathcal A_0)<1.
\]

This formulation works for ellipsoids, polytopes, arithmetic subsets, and other admissible sets without imposing an artificial Euclidean ball. If \(\mathcal A_0\) is unbounded in a direction on which \(R\) is nonzero, the width is infinite.

## Hostile coordinate rescaling

For physical displacements \(|w|\le2\) and omitted route \(R(w)=w/10\), the width is \(1/5\). Rescaling the basis by \(1/2,1,2,5\) changes the reported coefficient radius and operator coefficient, but their product remains \(1/5\). Reporting only a small coordinate radius or only a small matrix column can therefore manufacture apparent confinement by basis choice.

## Source requirements

The admissible set must be defined as a subset of the absolute lift space, not as an unexplained coordinate box. The remainder norm must use the physical target inner product. A source may provide a coefficient description, but it must also provide the basis map and the norm or inequalities whose image is \(\mathcal A_0\).

For prime-uniform confinement, one needs

\[
\sup_p\omega_{R_p}(\mathcal A_{0,p})<1-q_{0,p}
\]

with the right side interpreted through a uniform bound. Pointwise finite widths do not supply a global margin.

## Verification

`research/aspect/checkers/check_basis_free_remainder_width.py` verifies exact invariance of the physical width under four rational basis rescalings while the coordinate radius and matrix bound change.

## Disposition

The owner handoff should request the intrinsic admissible lift set and its omitted-route image width. Separate values \(M\) and \(\varepsilon\) are acceptable only with the source basis and coefficient norm that make their product a proved upper bound for that width.
