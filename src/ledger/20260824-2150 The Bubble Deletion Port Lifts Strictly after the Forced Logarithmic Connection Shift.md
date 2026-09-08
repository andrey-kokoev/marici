---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2150 — The Bubble Deletion Port Lifts Strictly after the Forced Logarithmic Connection Shift

> **RETRACTED as a deletion-map theorem by Entry 2153.** Conjugating a
> rank-one connection by the ratio of two forms is a tautological gauge
> construction. It does not prove a map between the source coefficient
> complexes or their derived pushforwards.

## Hard-to-vary claim

Entry 2149's rational last-edge deletion adapter lifts canonically to a
strict morphism of logarithmic de Rham complexes on the complement of its two
declared exceptional divisors.

## Forced connection shift

Write

\[
q=x_1+x_2+2y_a,
\qquad
f=\frac q{y_b}.
\]

Let \(\nabla_a=d+A_a\) be the connection on the one-edge-deleted integrand
line. Multiplication by \(f\) is horizontal precisely when the all-deleted
line carries

\[
\boxed{
A_{ab}=A_a-d\log f
=A_a-d\log q+d\log y_b.
}
\]

Indeed,

\[
\nabla_{ab}(f\omega)=f\nabla_a\omega.
\]

This shift is not fitted: its residues are forced by the source ratio in
Entry 2149,

\[
\operatorname{res}_{q=0}(A_{ab}-A_a)=-1,
\qquad
\operatorname{res}_{y_b=0}(A_{ab}-A_a)=+1.
\]

## Pushforward consequence

On

\[
U=\{q\ne0, y_b\ne0\},
\]

multiplication by \(f\) is an isomorphism of coefficient complexes. Derived
pushforward along the loop projection therefore carries it to a horizontal
Gauss--Manin morphism on the corresponding open base locus.

This does not turn \(f\) into a scalar after integration. It remains a
rational insertion in the fiber complex. Functorial pushforward, rather than
pulling \(f\) outside the integral, is the typed lift.

## Supported cone

The map ceases to be invertible only on

\[
\operatorname{div}(f)=\{q=0\}-\{y_b=0\}.
\]

Thus its extension cone can be supported only on the removed connected
total-energy wall and the erased-edge soft pole. No additional support is
available in this pilot.

## Narrow conclusion

\[
\boxed{
\text{the first adjacent deletion map is coefficient-horizontal after a
source-forced logarithmic gauge shift.}
}
\]

Physical-chain compatibility remains separate: a period comparison requires
the source contour to define the corresponding relative-chain morphism or
boundary term.

## Evidence

- Entries 2113--2115 and 2149;
- `research/benincasa/marici-gm/src/bin/bubble_deletion_derham_lift.rs`;
- allocator claim `seqclaim-1799630791dbf07978991467`.

## Next falsifier

Compute the relative-chain boundary induced at \(q=0\) and \(y_b=0\). Test
whether the physical bubble contour intertwines the coefficient map strictly
or produces a supported Gysin correction. Only after that test should the
map be transported to the triangle deletion cube.