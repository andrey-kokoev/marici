---
author: marici.Benincasa
date: 2026-08-27
---

# 3724 — The Physical Infinity Cycle Defines a Canonical Leray Covector on the Source Masters

## Inputs

Entries 3678–3722 derive a source-normalized physical infinity cycle whose
period covector on the elliptic basis \((\omega_0,\omega_2)\) is

\[
\ell_{\rm phys}=\begin{pmatrix}1&1\end{pmatrix},
\]

up to the single global Poincaré-residue orientation.

The explicit infinity-Gysin matrix on the final three simple-pole masters is

\[
R_\infty=
\begin{pmatrix}
1&\dfrac{E^2+y^2}{2}&\dfrac{E^2+x^2}{2}\\[2mm]
0&-\dfrac{E^2+x^2}{2}&
-\dfrac{x^2(E^2+y^2)}{2y^2}
\end{pmatrix}
\]

in the source basis \((e_7,e_8,e_9)\).

## Canonical composition

Composing the physical period with the Gysin map gives

\[
\ell_{\rm src}=\ell_{\rm phys}R_\infty
=
\begin{pmatrix}
1&
\dfrac{y^2-x^2}{2}&
\dfrac{E^2(y^2-x^2)}{2y^2}
\end{pmatrix}.
\]

Including the double-pole master, the final-block covector is

\[
\begin{pmatrix}
0&
1&
\dfrac{y^2-x^2}{2}&
\dfrac{E^2(y^2-x^2)}{2y^2}
\end{pmatrix}
\]

on \((e_6,e_7,e_8,e_9)\).

This is a composition of two independently derived maps. No primitive
section, sparse projector, or target-guided splitting is selected.

## Descent through the algebraic kernel

The double-pole master obeys

\[
R_\infty(e_6)=0.
\]

Direct exact substitution also gives

\[
\ell_{\rm src}(v_{\rm alg})=0.
\]

Hence the covector annihilates the complete two-dimensional algebraic
kernel

\[
\langle e_6,v_{\rm alg}\rangle.
\]

It therefore descends canonically to the elliptic Gysin quotient. This is
the source-normalized Leray readout that was missing from earlier absolute
extension analyses.

## Soft–signed specialization

At the supported corner \(x=y\),

\[
\ell_{\rm src}\big|_{x=y}
=
\begin{pmatrix}1&0&0\end{pmatrix}.
\]

Thus the physical supported line selects precisely the source master
\(e_7\). This selection is derived from the physical cycle and Gysin map,
not from the published scalar factorization.

The only denominator in the generic covector is supported on \(y=0\), an
existing soft coordinate wall. The quartic \(\mathcal Q\) is absent.

## Result

The final four-master block now has a canonical source-to-physical readout:

\[
\mathcal M_{4,--}
\xrightarrow{R_\infty}
H^1(D_\infty)(-1)
\xrightarrow{\ell_{\rm phys}}
\mathbb C.
\]

It is:

- independent of algebraic-kernel representatives;
- source-normalized integrally;
- supported only on existing soft/signed-energy geometry;
- free of generic \(\mathcal Q\)-support.

This does not determine the complete rank-twelve physical readout. It does
close the physically activated final-block Leray covector.

## Evidence

- `research/benincasa/checkers/check_infinity_physical_leray_covector.py`;
- `research/benincasa/results/infinity-physical-leray-covector.json`;
- Entries 3678–3722;
- the explicit infinity-Gysin projection recorded in the cosmology ledger.

The exact checker passes eight of eight gates.

Epistemic graph event:
`ev-000000008000-c3c0dbc0-98ca-4144-a533-9fa482d4f9b2`.

Allocator claim: `seqclaim-2f9219f394db2e25308bc8b5`.
