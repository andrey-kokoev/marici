---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2167 — The Exceptional Moment Insertions Span Rank Two in the Frozen Source Module

## Source chart

Use the canonical \(q_{\mathcal G_{12}}\)-residue chart of Entry 169:

\[
y_{12}=-E,\qquad
a=y_{23},\qquad
b=y_{31}.
\]

For the cyclic component in which vertex \(1\) is isolated, the retained
edge is \(23\), so

\[
\widehat y=\widehat y_{23}=a.
\]

Its connected complementary component has

\[
q_{23}=X_2+X_3+y_{12}+y_{31}=b-X_1.
\]

Hence the two numerator insertions of Entry 2166 are

\[
\widehat y\,\omega_{\rm exc}
=
\frac{a\,da\wedge db}{W},
\]

\[
\widehat q\,\omega_{\rm exc}
=
\frac{(b-X_1)\,da\wedge db}{W}.
\]

## Identification in the frozen basis

Entry 169 fixes the simple-pole source masters

\[
e_2=\frac{a\,da\wedge db}{W},
\qquad
e_3=\frac{b\,da\wedge db}{W},
\qquad
e_4=\frac{da\wedge db}{W}.
\]

Therefore

\[
\boxed{
\widehat y\,\omega_{\rm exc}=e_2,
\qquad
\widehat q\,\omega_{\rm exc}=e_3-X_1e_4.
}
\]

The \(e_2,e_3\) coordinate minor of these two vectors is identically one.
Thus

\[
\boxed{
\operatorname{rank}_{\mathcal M_q^{(9)}}
\langle
\widehat y\,\omega_{\rm exc},
\widehat q\,\omega_{\rm exc}
\rangle
=2
}
\]

for every \(X_1\).

## Consequence

The first outcome in Entry 2166's contract is falsified:

\[
\text{the exceptional moment insertions do not form a universal rank-one
coefficient subsystem.}
\]

They are two independent source classes before pairing with a physical
cycle. Consequently any scalar circuit

\[
(I_y,-2I_q)
\]

is genuinely a readout of a two-component period system. It cannot be
reconstructed from an algebraic proportionality of the coefficient forms.

This does not prove that the two numerical periods are functionally
independent after choosing one physical chain. It proves that any relation
between them must come from that chain, its boundary conditions, or its
transport—not from the frozen de Rham module.

## Strominger comparison

The cosmological mechanism now differs sharply:

- the supported fault packet exists canonically;
- its radial weight is finite;
- its two readout insertions are independent source masters;
- a primitive circuit, if present, is a period relation selected by the
  physical current.

Thus the remaining question is analytic/Betti, not algebraic/Carrier.

## Evidence

- Entries 169 and 2165--2166
- research/benincasa/checkers/exceptional_moment_master_rank.rs
- allocator claim seqclaim-0a3fc0448ef074afe7fc63db
