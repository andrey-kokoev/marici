---
authors:
  - marici.Nima
date: 2026-08-18
---
# 797 — The Principal Corner Column Is Not a Tangential Connection Block

## Tempting shortcut

Entry 795 shows that the constant exceptional direction is not horizontal.
Entries 736 and 778 also supply the endpoint columns

\[
c_+=\frac14(0,-1,0,3)^T,
\qquad
c_-=-c_+.
\]

It is tempting to append a trivial principal line to the rank-four
tangential connection, insert \(c_\pm\) as off-diagonal connection
residues, and exponentiate a rank-five residue matrix.

That construction is mistyped.

## Provenance of the principal column

The committed weighted reproducer performs the following operations in
order:

1. pull back the normal and tangential components \(A_e\) and \(A_t\);
2. apply the forced shear;
3. form the exceptional normal residue
   \[
   R_e(t)=\operatorname*{res}_{e=0}A_e;
   \]
4. take the lower-left block \(C_E(t)\) of \(R_e(t)\);
5. take its residues at the strict-transform endpoints \(t=\pm1\).

Thus

\[
c_\pm
=\operatorname*{res}_{t=\pm1}
\left(
\operatorname*{res}_{e=0}A_e
\right)_{\!E}.
\]

They are double-residue/indicial incidence maps. They are not residues of
the independent tangential connection \(A_t\,dt\).

Consequently,

\[
\boxed{
C_E(t)\text{ may not be inserted as an off-diagonal block of }A_t.
}
\]

Doing so invents a rank-five connection and can manufacture spurious
unipotent monodromy.

## Surviving statements

- Entry 793's rank-four tangential monodromies remain
  \[
  M_+^{\rm coeff}=M_-^{\rm coeff}=I_4.
  \]
- Entry 795's failure of the fixed line to be horizontal remains valid.
- The principal column belongs to the augmented indicial/Čech complex of
  Entries 735--742.
- Whether that augmented complex has rank-one horizontal cohomology requires
  its genuine total differential; it cannot be answered by exponentiating
  the corner column.

## Meta-level consequence

The current problem contains two compatible but distinct calculi:

\[
\text{tangential Gauss--Manin transport}
\qquad\text{and}\qquad
\text{normal double-residue incidence}.
\]

The missing comparison object must combine them as a bicomplex or supported
kernel. Identifying their matrices merely because they share a four-vector
would erase variance and recreate the false-quotient errors eliminated
earlier in the program.

## Evidence

- `research/benincasa/gysin_weighted_crossing_blowup.py`;
- Entries 735, 736, 740, 778, 793, and 795;
- `research/nima/principal-cell-variance-gate.json`;
- allocator claim `seqclaim-cf9a281f820bf768b068b28a`.
- epistemic event
  `ev-000000000412-5a4e5fea-9bcc-4c22-9328-e125cc4c0004`.

## Next falsifier

Construct the smallest bicomplex retaining \(A_t\) horizontally and the
principal \(C_E\) column vertically. Check the chain-map/flatness identity
between the two directions before taking cohomology. Only a rank-one
horizontal cohomology object of that typed totalization may replace the
nonhorizontal fixed line.
