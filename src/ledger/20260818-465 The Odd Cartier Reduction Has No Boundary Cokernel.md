---
id: 465
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Odd Cartier Reduction Has No Boundary Cokernel

## Record

Status: global boundary extension of Entry 464's normalized odd first-Cartier
map; not yet a construction of the complete specialization morphism.

Entry 464 identifies the odd Rees lattice generator as

\[
\eta_-=a\,t^3(b+1),
\qquad
t=\frac{b^2-1}{2}.
\]

Its scalar transition is

\[
t^3(b+1)
=
\frac{(b-1)^3(b+1)^4}{8},
\]

so its divisor is exactly

\[
3[b=1]+4[b=-1].
\]

The normalized \(q\)-symbol in each of the two contributing \(s_a=1\)
sectors is

\[
\bar\sigma_z(q)=-6\eta_-.
\]

Thus the seven boundary zeros belong to the target lattice generator, not to
the coefficient of the morphism. Relative to the source-derived source and
target lattices, the coefficient is the unit \(-6\). Consequently the odd
first-Cartier map remains surjective at both \(b=1\) and \(b=-1\), and it has
no boundary-supported cokernel.

Combining this with Entry 464, the resonant exceptional object extends over
the full \(b\)-axis as

\[
\mathcal R_+\oplus\mathcal L_-,
\]

where \(\mathcal R_+\) is the length-two invariant Cartier block and
\(\mathcal L_-\) is the reduced anti-invariant line with transition divisor
\(3[1]+4[-1]\).

This closes the boundary-extension gate for the normalized resonant associated
object. It does not yet prove that the full exact-form cokernel specializes
isomorphically to it.

## Classification

- carrier: unchanged translated double section;
- coefficient data: one thick invariant block and one reduced twisted odd
  line;
- boundary support: absorbed by the source-derived odd lattice;
- new carrier datum: none.

## Next falsifier

Construct the specialization morphism from the complete weighted-Rees
exact-form cokernel to the extended resonant object and compute its kernel and
cokernel. A nonzero residual must be classified by Rees degree and support;
only a residual outside the existing Cartier, boundary, or quartic-tail
coefficient sectors can motivate new carrier structure.

## Evidence

- research/benincasa/marici-gm/src/bin/soft_axis_cartier_boundary.rs;
- Entries 455--456 and 462--464.
