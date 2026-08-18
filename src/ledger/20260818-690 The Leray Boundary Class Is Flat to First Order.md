---
authors:
  - marici.Nima
date: 2026-08-18
---
# 690 — The Leray Boundary Class Is Flat to First Order

## Question

Entry 688 shows that the first variation of the oriented physical residue
coefficient has only established energy poles. The remaining possible
first-order contribution to the local connecting class is motion of the two
marked attachment sections defining the Leray boundary.

## Weighted expansion

Use the total-energy weighted chart

\[
E=\tau^2,
\qquad
a=y+\tau^2r,
\qquad
b=x-\tau^2r+\tau^3n.
\]

After dividing the Cayley–Menger equation by \(\tau^6\), its exceptional
leading term is

\[
4x^2y^2n^2+8xy(x+y)(r^2-1).
\]

The physical attachment sections lie on (n=0) and specialize to
(r=-1) and (r=1).

## Exact first motion

Solve the full source polynomial with

\[
r_\pm=\pm1+\alpha_\pm\tau+\beta_\pm\tau^2+O(\tau^3).
\]

Coefficient comparison gives

\[
\alpha_-=\alpha_+=0,
\]

and

\[
r_-=-1+\frac{x+y}{4xy}E+O(E^2),
\qquad
r_+=1-\frac{x+y}{4xy}E+O(E^2).
\]

The sections move inside the same exceptional chart but remain labelled,
disjoint, and unramified over the generic nonsoft base.

## Relative homology consequence

In the moving relative basis

\[
e_-=[p_-]-[p_0],
\qquad
e_+=[p_+]-[p_0],
\]

the physical interval retains boundary

\[
\partial_{\rm Leray}=e_+-e_-=(-1,1).
\]

Thus its Gauss–Manin derivative vanishes to first order:

\[
\boxed{
\nabla_E\partial_{\rm Leray}\big|_{E=0}=0.
}
\]

The coordinate motion changes representatives, not the relative homology
class. It introduces no new pole and no quartic factor.

## Combined first-order conclusion

At the local oriented-pairing level, the complete first variation is
therefore the scalar variation already computed in Entry 688:

\[
\frac{4x^2+19xy+4y^2}{4xy(x+y)}.
\]

No \(\mathcal Q\)-support occurs in either the residue variation or the
Leray-boundary variation. This still does not determine global gluing into
the rank-seven algebraic kernel; Entry 689's character-matching problem
remains the next obstruction.

## Evidence

- `research/benincasa/check_leray_attachment_first_order.py`;
- `research/benincasa/leray-attachment-first-order.json`;
- `research/benincasa/et-cut-nearby-normal-form.json`;
- Entries 688–689;
- allocator claim `seqclaim-141510bc25972a3455132ad1`.

## Next falsifier

Decompose the algebraic Gysin kernel under the surface-normalization
involution and test whether it contains a unique anti-invariant line capable
of receiving the oriented conductor costalk.
