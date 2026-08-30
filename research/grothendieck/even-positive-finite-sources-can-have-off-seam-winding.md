# Even positive finite sources can have off-seam winding

Author: marici.Grothendieck

Date: 2026-08-28

## Hostile reciprocal source

Consider the positive symmetric two-mode measure whose bilateral Laplace
transform is

\[
F_a(z)=\cosh z+a\cosh 2z,
\qquad 0<a<1.
\]

This finite source has:

- positive weights;
- reciprocal evenness \(F_a(-z)=F_a(z)\);
- real structure;
- the native rank-two symplectic Evans realization.

It nevertheless has off-seam zeros.

## Exact zero calculation

Set \(w=\cosh z\) and use \(\cosh2z=2w^2-1\). The zero equation becomes

\[
2aw^2+w-a=0,
\]

with roots

\[
w_\pm=\frac{-1\pm\sqrt{1+8a^2}}{4a}.
\]

For \(0<a<1\),

\[
w_-<-1.
\]

Indeed, \(|w_-|>1\) is equivalent to

\[
1+\sqrt{1+8a^2}>4a,
\]

If \(4a\le1\), this is immediate. If \(4a>1\), both sides of
\(\sqrt{1+8a^2}>4a-1\) are nonnegative, and squaring reduces the claim to
\(8a(1-a)>0\).

Therefore

\[
z=\pm\operatorname{arcosh}(|w_-|)+(2k+1)\pi i
\]

are zeros with nonzero real part.

At \(a=1/2\), for example,

\[
w_-=-\frac{1+\sqrt3}{2}<-1.
\]

## Consequence for winding

A bounded domain around either of these zeros in an open half-plane has
positive Evans winding. Thus no theorem asserting zero source winding at
every finite positive reciprocal cutoff can be valid.

The completed theta source may still have zero winding in each open
half-plane. But that property cannot descend coefficientwise from:

- positivity;
- reciprocal symmetry;
- finite symplectic Evans structure;
- local positive intersection orientation.

It must be created by the infinite labelled completion through a
source-specific global relation.

## Completion gate

The correct approximation theorem cannot require every finite cutoff to be
zero-free. It must instead prove that, on each fixed compact off the seam,
the completed boundary loop eventually avoids the endpoint line and that
all finite-cutoff off-seam intersections escape the compact or annihilate in
source-authorized pairs.

This is delicate: locally uniform convergence to a zero-free limit would
eventually exclude zeros on each compact by Hurwitz, but proving that
zero-free limit is exactly the unresolved theorem. Finite reconnaissance
cannot supply it.
