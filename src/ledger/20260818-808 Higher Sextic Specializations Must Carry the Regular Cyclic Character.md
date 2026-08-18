# Higher Sextic Specializations Must Carry the Regular Cyclic Character

## Input

Entry 807 reduces every higher finite-sextic degeneration to the invariant
divisors

\[
E=0
\qquad\text{and}\qquad
\Lambda(P_1,P_2,P_3)=0,
\]

plus their frozen coordinate-boundary strata.  Entries 803, 805, and 806
show that every labelled finite-sextic occurrence orbit is a free
\(C_3\)-orbit with transition unit \(+1\).

These facts impose an equivariant constraint before any local Milnor or Kato
rank is known.

## Regular representation

Let \(W\) be the local higher specialization object for one occurrence, of
rank \(r\).  Functorial cyclic transport forces the full orbit object to be

\[
\boxed{
\operatorname{Ind}_{\{1\}}^{C_3}W
=\mathbb Q[C_3]\otimes W.
}
\]

For the cyclic permutation matrix

\[
\sigma=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix},
\]

the character is

\[
\boxed{
\chi_W(1)=3r,
\qquad
\chi_W(\sigma)=\chi_W(\sigma^2)=0.
}
\]

Over \(\mathbb Q\),

\[
\mathbb Q[C_3]
\simeq
\mathbb Q_{\rm triv}\oplus\mathbb Q(\zeta_3),
\]

so each local rank contributes one rank-\(r\) trivial block and one
rank-\(2r\) cyclotomic block.

## Eight-orbit constraint

If the eight representatives have a common local rank \(r\), their aggregate
must have

\[
\boxed{
\dim=24r,
\qquad
\chi=(24r,0,0),
}
\]

with eight trivial rank-\(r\) blocks and eight cyclotomic rank-\(2r\) blocks.
If the local ranks differ, the same statement applies orbit by orbit.

## Scalar-invariant sextic

The sextic represented in the \(\mathcal G_{12}\) chart by
\((\mathcal G_{23},\mathcal G_{31})\) is invariant as an external polynomial.
Nevertheless its labelled occurrence orbit is free.  Its specialization must
still have rank \(3r\), not \(r\), unless a separately derived descent or
fixed-point map identifies the three labelled objects.

Thus this orbit supplies the strongest implementation check:

\[
\boxed{
\text{fixed scalar equation does not authorize quotienting occurrence labels.}
}
\]

## Falsifier for the local calculation

Benincasa's forthcoming \(E=0\) and \(\Lambda=0\) local ranks must satisfy:

- total rank divisible by three on every labelled orbit;
- trace zero for both nonidentity cyclic elements;
- transition unit \(+1\), unless a new source-derived fixed-point datum is
  exhibited;
- the rational decomposition into trivial and cyclotomic blocks above.

A smaller rank on the scalar-invariant orbit means the calculation forgot
labels or residue charts.  A nonzero nonidentity trace means that additional
fixed-point or transition data has entered and must be sourced geometrically.

## Scope

This determines the equivariant assembly, not the local ranks
\(r_E,r_\Lambda\) or the extension at \(E=\Lambda=0\).

## Verification

- checker: `research/nima/audit_higher_specialization_cyclic_constraint.py`;
- packet: `research/nima/higher-specialization-cyclic-constraint.json`;
- allocator claim: `seqclaim-899ead803eee49569b9856b7`.
