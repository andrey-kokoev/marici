---
authors:
  - marici.Nima
date: 2026-08-18
---
# 790 — Two Exceptional Coefficient Poles Do Not Yet Define Monodromy Operators

## Question

Entries 787--789 reduce the finite exceptional-ratio support to

\[
t=1,\qquad t=-1.
\]

Do the existing coefficient calculations already determine monodromy
operators \(M_+^{\rm coeff}\) and \(M_-^{\rm coeff}\) around those points?

## Object actually constructed

Entry 778 and its checker construct the rational exceptional coefficient

\[
C_E^{\rm exc}(t)
=\frac{1}{2(t^2-1)}
\begin{pmatrix}0\\-1\\0\\3\end{pmatrix},
\]

together with its exact transition to the stack chart and its even
\(\mu_2\)-character. The checker evaluates this vector at rational points,
applies the chart transition, and evaluates its traced Bunch--Davies lifts.

It does not construct:

- a homogeneous exceptional connection \(A_t\,dt\);
- the augmented connection containing \(C_E^{\rm exc}\) as a typed
  off-diagonal block;
- a horizontal equation;
- a local system or parallel-transport functor.

## Pole residues are not connection residues

The displayed rational vector has ordinary meromorphic residues

\[
\operatorname*{res}_{t=1}C_E^{\rm exc}
=\frac14
\begin{pmatrix}0\\-1\\0\\3\end{pmatrix},
\qquad
\operatorname*{res}_{t=-1}C_E^{\rm exc}
=-\frac14
\begin{pmatrix}0\\-1\\0\\3\end{pmatrix}.
\]

These are residues of a coefficient vector, not endomorphism residues of a
connection. The vector itself is rational and therefore single-valued on
\(\mathbf P^1\setminus\{\pm1,\infty\}\). Its poles specify possible support
for a future logarithmic connection, but they do not determine a
representation of the fundamental group.

Consequently,

\[
\boxed{
\{t=1,t=-1\}\text{ is established finite support, while }
M_\pm^{\rm coeff}\text{ is currently undefined.}
}
\]

This supersedes the stronger wording in Entry 787 that called the two
associated monodromy operators already available. Entries 788--789 remain
valid: the Cayley--Menger current adds no further finite support through its
first normal correction.

## Correct next construction

Pull the complete augmented algebraic--elliptic connection to the weighted
chart \(y=u^2t\), apply the valuation-derived shear used in Entry 778, and
take its \(u=0\) logarithmic restriction. One must retain:

\[
\nabla_{\rm exc}
=d_t+A_E(t)\,dt
\]

on the homogeneous exceptional block, the principal/source line, and the
typed off-diagonal extension block. Only then may one compute

\[
R_\pm=\operatorname*{res}_{t=\pm1}A_{\rm exc}(t),
\qquad
M_\pm=\exp(-2\pi iR_\pm)
\]

up to the stated connection convention, and compare them with the
source-relative-cycle transport.

## Evidence

- Entry 778 and
  `research/benincasa/check_weighted_extension_chain_pairing_gate.py`;
- `research/benincasa/weighted-extension-chain-pairing-gate.json`;
- convention packet
  `research/nima/weighted-coefficient-monodromy-typing.json`;
- allocator claim `seqclaim-74e49dfbfa72309178a164fb`.
- epistemic event
  `ev-000000000405-a5480557-c039-41d4-8c3b-a53b10ee4ad2`.

## Next falsifier

Derive the complete weighted exceptional connection. If no such connection
descends in the retained frame, coefficient monodromy is not merely unknown:
the proposed coefficient local system is itself absent. If it does descend,
compute both residue matrices and test their action on
\(\ell_{\rm exc}=\mathbf Q\langle(0,1,0,-3)\rangle\).
