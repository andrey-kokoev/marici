---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2139 — The Same Normal Wall Carries Inequivalent Logarithmic and Kummer Coefficients

> **Scope correction from Entry 2143.** The one-wall monodromy comparison in
> this entry remains valid. Its inference that the full deletion adapter
> cannot supply mixed structure does not: the all-deleted source term is a
> tensor product of contact factors.

## Hard-to-vary claim

The deletion-contact sector and the generic lower algebraic-letter sector are
supported on the same labelled normal wall

\[
\nu_i=P_i^2-X_i^2=0,
\]

but carry inequivalent local coefficient systems.

## Deletion-contact monodromy

Entry 2137 derives the Morse--Bott singular part

\[
c_i\log(\nu_i-i0).
\]

In the normalized basis

\[
(1,\tau_i),
\qquad
\tau_i=(2\pi i)^{-1}\log\nu_i,
\]

a positive loop around the wall gives

\[
T_{\log}=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
\qquad
N=T_{\log}-I,
\qquad
\operatorname{rank}N=1,
\qquad N^2=0.
\]

The deletion contact therefore carries a nontrivial unipotent extension of
the trivial line by the trivial line.

## Lower-sector monodromy

Entry 698 gives

\[
\Delta_{ij}=-4\nu_i\nu_j\Lambda_PF_{ij}.
\]

Keeping \(\nu_j\ne0\) generic, its radical is locally a unit times
\(\sqrt{\nu_i}\). Hence its rank-one Kummer monodromy is

\[
T_{\rm Kum}=-1.
\]

These representations cannot be identified. A horizontal map from the
Kummer line into the logarithmic block would require

\[
(T_{\log}+I)f=0,
\]

but

\[
\det(T_{\log}+I)=4.
\]

Thus the only such map is zero.

## Classification

- common carrier support: the labelled wall \(\nu_i=0\);
- correlator-deletion coefficient: rank-two unipotent logarithmic system;
- generic-lower coefficient: rank-one semisimple Kummer character;
- canonical horizontal identification: none;
- new carrier datum: none.

## Narrow conclusion

\[
\boxed{
\text{equality of support does not imply equality of coefficient object.}
}
\]

This is a finite cosmological realization of H2:

\[
\text{shared labelled carrier and nearby-cycle calculus}
+
\text{readout-specific coefficient systems}.
\]

It also explains why the deletion adapter cannot simply be used as the
missing bridge to the lower square-free module: even its one-wall local
system has the wrong monodromy character.

## Evidence

- Entries 698, 2136--2138;
- `research/benincasa/checkers/contact_log_kummer_character.rs`;
- allocator claim `seqclaim-aa5aa351471768145bf45352`.

## Next falsifier

Test whether an independently source-derived comparison functor supplies a
Kummer twist that converts one monodromy type into the other. Without such a
twist and a typed source map, the two objects must remain distinct despite
their common support.
