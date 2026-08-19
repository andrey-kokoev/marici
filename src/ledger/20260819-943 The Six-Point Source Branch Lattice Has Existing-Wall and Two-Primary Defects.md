# 943 — The Six-Point Source Branch Lattice Has Existing-Wall and Two-Primary Defects

## Frozen source matrix

The pair-shift action splits the rational source module into labelled
character blocks of dimensions

\[
(2,1,1,2).
\]

Using the (X=+1) and (X=-1) source rows in the two-dimensional blocks and
the (X=+1) row in the singleton blocks gives a source-derived maximal minor.
No kinematic factor is inverted when forming it.

## Factorization

Up to the declared Laurent monomial units, the maximal minor is proportional
to

\[
\begin{aligned}
&(A_2^2-1)^2(A_3^2-1)^2
((A_2B_{24})^2-1)((A_3B_{34})^2-1)\\
&\quad\times((ZA_2)^2-1)
((ZA_2B_{24})^2-1)^2\\
&\quad\times(A_3^2-Z^2)
((A_3B_{34})^2-Z^2)^2,
\end{aligned}
\]

with the exact rational expression retained in the machine packet.

This is not a unit.  Hence the six rational branch directions do not define a
globally saturated source lattice over the frozen Laurent ring.

## Classification

Every displayed kinematic factor is an existing sine/incidence hyperplane.
The defect therefore has the form

\[
\boxed{
\text{generic source saturation}
+
\text{supported lattice defect on existing carrier walls}.
}
\]

It does not require a new carrier divisor.

There is a second, logically separate integral issue.  Extracting the four
pair-shift characters from their orbit uses the order-four Fourier projector,
so its denominator is (4).  Over characteristic zero this is harmless; over
\(\mathbb Z\) the possible two-primary index remains unresolved.  The wall
defect and the two-primary defect must not be conflated.

## Consequence

Entry 941's target lattice remains unimodular.  The full rank-twelve object is
therefore generically lattice-valued after localization away from existing
walls, but no global integral Betti lattice has yet been derived.

## Next falsifier

Compute the orbit-basis Smith normal form without character projectors.  This
will determine the exact two-primary index.  Separately, take valuations of
the maximal minor along each existing wall and test whether the frozen
Cartier/Gysin lattice supplies the corresponding saturation automatically.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_cartier_sheet_transition.rs`;
- packet:
  `research/benincasa/string-six-point-cartier-sheet-transition.json`;
- allocator claim:
  `seqclaim-07e84d29020d16c5910497c2`.
- epistemic event:
  `ev-000000000560-34a69185-200f-4368-98cc-b3a09c86dc72`.
