---
title: "The Integral Cusp Ambiguity Is a Two-Bit Extension Class"
date: 2026-08-20
entry: 1152
status: established-finite-extension-frontier
sector: cosmology
---

# 1152 — The Integral Cusp Ambiguity Is a Two-Bit Extension Class

Sequence claim: `seqclaim-e8ae119501faedd8b4b0ffc3`.

## Question

Entry 1151 proves that the generic integral infinity-Gysin sequence has a
primitive free algebraic kernel and free elliptic quotient. At the
total-energy cusp, does Entry 1147's elliptic (mathbb Z/2) coinvariant
survive as a direct summand of the full rank-nine coinvariants, or is it
absorbed by an integral extension with the algebraic lattice?

## Rational monodromy input

Entry 289 computes the exact total-energy residue and proves:

\[
T|_{\mathcal T_7}=1,
\qquad
N_E=N_{\rm ell},
\qquad
\operatorname{rank}N_E=1,
\qquad N_E^2=0.
\]

Thus the variation splits into algebraic and elliptic monodromy sectors over
(\mathbb Q). In the snake sequence for (T-I), the connecting map from
elliptic invariants to the free algebraic coinvariants vanishes rationally.
Because the target (mathcal T_7) is torsion-free by Entry 1151, it
vanishes integrally as well.

This does not force the resulting coinvariant extension to split.

## Character reduction

Entry 150 shows that the elliptic boundary cohomology occupies the character
of the final four-master block. The other algebraic character blocks cannot
mix with it. The only allowed algebraic target is therefore

\[
\mathcal A_{--}
=\mathbb Z\langle e_6,v_{\rm alg}\rangle.
\]

Hence the complete unresolved integral datum lies in

\[
\boxed{
\operatorname{Ext}^1_{\mathbb Z}
(\mathbb Z/2,\mathcal A_{--})
\simeq
\mathcal A_{--}/2\mathcal A_{--}
\simeq(\mathbb Z/2)^2.}
\]

It is two parity bits, not an unbounded off-diagonal matrix.

## Four possible lattices

Choose an elliptic coinvariant lift (m). The four classes have
presentations

\[
2m=a e_6+b v_{\rm alg},
\qquad (a,b)\in(\mathbb Z/2)^2.
\]

- For ((a,b)=(0,0)), the coinvariant group is
  (mathcal A_{--}\oplus\mathbb Z/2); the width-two torsion remains
  visible.
- For each nonzero parity vector, the relation is primitive and the total
  group is free of rank two; the apparent elliptic (mathbb Z/2) is
  absorbed into the algebraic lattice extension.

The rational connection cannot distinguish these four cases.

## Verdict

\[
\boxed{
\text{the unresolved integral total-energy problem is exactly one class in
}(\mathbb Z/2)^2.}
\]

This corrects an overstrong possible inference from Entry 1147: the
elliptic quotient has a width-two coinvariant, but a visible
(mathbb Z/2) summand in the full rank-nine coinvariants is not established.

No carrier modification is implicated. The missing datum is an integral
Betti/Gysin comparison or polarization fixing the extension class.

## Next falsifier

Construct the integral Picard--Lefschetz action on

\[
H^2(S\setminus D_\infty;\mathbb Z)
\]

in a basis compatible with the primitive Gysin sequence. It is sufficient
to compute the parity of twice one elliptic coinvariant lift along
((e_6,v_{\rm alg})). The result must be one of the four classes above;
no rational reconstruction of the full connection is required.

Evidence:

- `research/benincasa/checkers/total_energy_coinvariant_extension_classes.py`;
- `research/benincasa/results/total-energy-coinvariant-extension-classes.json`;
- Entries 150, 289, 1147, and 1151.
