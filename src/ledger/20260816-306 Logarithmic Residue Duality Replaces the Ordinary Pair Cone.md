---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Logarithmic Residue Duality Replaces the Ordinary Pair Cone

## Result

Entry 302 correctly falsified naive contraction of equation-(58) master
coordinates, but proposed the wrong replacement complex.  The frozen
three-site marked system is defined by forms on

\[
U_E=S_E\setminus W_E,
\]

not by the ordinary relative pair \((S_E,W_E)\).  Consequently its boundary
map is logarithmic residue, not pullback.

For a smooth wall component the canonical sequence is

\[
\boxed{
0\longrightarrow\Omega^\bullet_{S_E}
\longrightarrow\Omega^\bullet_{S_E}(\log W_E)
\xrightarrow{\operatorname{Res}_{W_E}}
\Omega^{\bullet-1}_{W_E}
\longrightarrow0.
}
\]

For the reducible source wall, this is replaced by the
normalization/conductor totalization already frozen in Entries 265--280.

## Finite type falsifier

The forms \(\eta_{101},\eta_{110},\eta_{111}^{\rm rat}\) of Entries 296--297
are meromorphic one-forms on the surface complement.  They have poles along
the wall.  Therefore \(i^*\eta\) is not a regular form on \(W_E\), and these
objects cannot be the boundary component of

\[
\operatorname{Cone}\bigl(
\Omega^\bullet(S_E)\to\Omega^\bullet(W_E)
\bigr)[-1].
\]

Thus the hard-to-vary claim

\[
\text{the central meromorphic primitives are boundary cochains in the
ordinary pair cone}
\]

is falsified by type alone.

Their valid role survives: they certify complement exactness and exact-lift
gauge.  The actual wall objects are the residues

\[
\rho_i=\operatorname{Res}_{W_i}\Omega.
\]

Entry 304 computes their source-normalized exceptional limits:

\[
\rho_1\longrightarrow-\frac{dr}{2xy(r-1)},
\qquad
\rho_2\longrightarrow-\frac{dr}{2xy(r+1)}.
\]

## Correct duality

If \(\gamma\subset W_i\) is a wall cycle and \(T(\gamma)\subset U_E\) its
source-oriented Leray tube, then locally

\[
\boxed{
\int_{T(\gamma)}\Omega
=
2\pi i\int_\gamma\operatorname{Res}_{W_i}\Omega,
}
\]

up to the fixed orientation convention.  Exact-gauge cancellation therefore
survives, but through residue/tube duality rather than through evaluation of
a surface primitive on the wall.

The orientation character is not optional.  Entry 305 proves that twisting
the conductor quotient by the source line
\(\mathfrak o_{ab}=\chi_{\epsilon\delta}\) gives the enhanced Rees character
and integral lattice exactly:

\[
J=
\begin{pmatrix}
2&0&1\\
0&2&1\\
0&0&1
\end{pmatrix},
\qquad
\operatorname{im}J
=
\{(u,v,w):u\equiv v\equiv w\pmod2\}.
\]

Hence the corrected duality uses no fitted pairing kernel and no new cell.

## Classification

| Datum | Classification |
|---|---|
| \(S_E\setminus W_E\) | frozen marked coefficient geometry |
| logarithmic residue triangle | shared derived/six-functor calculus |
| normalized wall and conductor | existing energy/Cut carrier |
| Entry 304 endpoint logarithms | sector-specific coefficient data |
| Leray tube orientation | existing occurrence/orientation datum |
| central meromorphic primitives | complement exact gauges |
| new carrier datum | none |

## Deutsch--Popperian update M2.49

The stronger ordinary-pair interpretation fails.  The smaller surviving
claim is

\[
\boxed{
\text{the enhanced/logarithmic comparison is residue-compatible
Gauss--Manin transport followed by source-oriented Leray duality.}
}
\]

This correction changes the derived calculus used at the marked boundary;
it does not change the frozen carrier.

## Next hostile test

Compute the Gauss--Manin connection on the normalized residue triangle in
the orientation-twisted frame and test

\[
\operatorname{Res}\circ\nabla
=
\nabla_W\circ\operatorname{Res}.
\]

Then pair the resulting wall classes with the enhanced exceptional classes
through Leray tubes.  The calculation must:

1. reproduce the Kummer characters and half-sum extension of Entries
   280 and 305;
2. reproduce the endpoint logarithms of Entry 304;
3. introduce no singular support outside the frozen energy, conductor,
   Cayley--Menger, soft, and \(\mathcal Q\) coefficient divisors.

A required new incidence divisor is the next finite falsifier of the
shared-carrier hypothesis.
