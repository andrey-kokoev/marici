# Typed pole-atom provenance: WP1053

## Question

Can a typed pole spectrum and mass clock be derived from the same finite
source atoms as the integer coefficient \(C=23\)?

## Minimal pole-atom cell

Take twenty-three atoms. Each atom carries

- two source ports, giving \(k=2\);
- unit residue;
- pole mass square \(M_i^2=1\).

Atom derivation gives

\[
k=2,
\qquad
C=\sum_i r_i=23,
\qquad
R(0)=23.
\]

The capacity coefficient is therefore

\[
h=\frac{12C\pi^2}{1367k}
 =\frac{138\pi^2}{1367}.
\]

All masses agree, so the cell is degenerate with mass clock \(M^2=1\). At
\(q^2=1\),

\[
R(1)=\sum_i r_i\frac{M_i^2}{M_i^2+1}
    =23\cdot\frac12,
\]

and hence

\[
\frac{R(1)}{R(0)}=\frac12.
\]

This is a minimal common-atom realization of the WP1036 capacity point and
the WP1039/WP1040 repairs.

## Scalar-declaration hostiles

A scalar packet can declare

\[
k=2,
\qquad
C=23,
\qquad
\text{degenerate}=1,
\qquad
M^2=1,
\qquad
R(1)/R(0)=1/2.
\]

Two atom cells expose why that declaration is insufficient.

1. Twenty-two atoms with \(M_i^2=1\) and one atom with \(M_i^2=4\) derive

   \[
   \frac{R(1)}{R(0)}=\frac{59}{115},
   \]

   not \(1/2\), and are not degenerate.

2. Twenty-three degenerate atoms with \(M_i^2=2\) derive

   \[
   \frac{R(1)}{R(0)}=\frac23,
   \]

   not \(1/2\), and have the wrong mass clock.

Thus residue count, degeneracy, mass clock, and finite response must be atom
derived, not appended as scalar repairs.

## Classification

This is a conditional pole-atom provenance constructor. It shows what a
common-source repair must look like: one finite atom cell derives \(k=2\),
\(C=23\), unit residues, degeneracy, \(M^2=1\), \(h=138\pi^2/1367\), and the
normalized response \(1/2\).

## Disposition

Productive but still not source selection. The next gate is to derive the
twenty-three pole atoms, their two ports, unit residues, and common mass clock
from the actual source representation or dynamics.

Checker: `research/flavor/checkers/wp1053_typed_pole_atom_provenance.py`

Result: `results/wp1053_typed_pole_atom_provenance.json`
