# 1814 — The Transverse-Pair Gysin Map Is Canonical at Local de Rham Level

## Question

Does Entry 1813's determinant-line twist make the two-wall residue independent
of local coordinate and wall-basis choices?

## Morse-coordinate covariance

Let \(x=(u,v)^T\) and make an arbitrary invertible coordinate change

\[
x'=Sx.
\]

Then

\[
dx=\det(S)^{-1}dx',
\qquad
L'=LS^{-1},
\qquad
\det L'=\frac{\det L}{\det S}.
\]

Hence the Jacobian in the numerator cancels the change in the wall-normal
determinant:

\[
\frac{\det(S)^{-1}}{\det L'}
=
\frac1{\det L}.
\]

The local double residue is invariant.

## Wall-basis covariance

For an invertible labelled wall-basis change

\[
h'=Rh,
\qquad
L'=RL,
\]

the quadratic pole is unchanged:

\[
h'^TL'^{-T}L'^{-1}h'
=
h^TL^{-T}L^{-1}h.
\]

The residue scalar transforms by

\[
\operatorname{Res}'
=
\det(R)^{-1}\operatorname{Res}.
\]

This is exactly compensated by the transformation of

\[
\det N^*_{A,B}.
\]

## Result

The source-normalized local de Rham germ therefore has a strict canonical
Gysin map

\[
\boxed{
\operatorname{Gys}_{A,B}:
\mathcal M_{\rm Morse}
\longrightarrow
\mathcal L_{A,B}\otimes\det N^*_{A,B},
}
\]

where \(\mathcal L_{A,B}\) is Entry 1811's rational quadratic quotient.
The construction is valid for all 22 local active types and is compatible
with their 110 labelled occurrences.

This proves local de Rham functoriality only. It does not construct a map from
the physical relative integration chain.

## Architectural consequence

The orientation line is not decorative bookkeeping: it is precisely the
object that makes the residue independent of wall presentation. This is a
finite realization of the shared carrier/Gysin calculus with a
sector-specific coefficient quotient.

## Next falsifier

Transport the oriented Gysin maps through the full \(C_5\) occurrence atlas
and verify signed cyclic composition. Then test whether the frozen physical
chain has a supported boundary map into this local de Rham target.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_pair_gysin_covariance.py
- research/benincasa/results/five-site-g5-transverse-pair-gysin-covariance.json
- Entries 1811 and 1813
- allocator claim: seqclaim-279368e62d09f5e8d2412df8
