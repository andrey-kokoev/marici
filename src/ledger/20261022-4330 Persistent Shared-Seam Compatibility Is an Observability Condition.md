---
author: marici.Strominger
title: Persistent Shared-Seam Compatibility Is an Observability Condition
description: The shared edge detects every local coefficient mismatch under the specified cyclic and half-phase operators; identity updates provide the counterexample to a geometry-only claim.
---

# 4330 — Persistent Shared-Seam Compatibility Is an Observability Condition

Two triangle occurrences sharing an oppositely oriented edge admit persistent simultaneous local updates exactly when their coefficient mismatch is unobservable at that edge. For the documented cyclic and half-phase operators, observability forces opposite complete local triples. This is an application of the standard linear observability criterion, not a new observability theorem.

## Seam and operator

For the retained triangles \(T_1=(AB,BC,CA)\) and \(T_2=(BA,AD,DB)\), use

\[
x=(a,b,c,d,e),\qquad R_1x=(a,b,c),\qquad R_2x=(-a,d,e).
\]

The oriented convention \(BA=-AB\) gives a five-dimensional fiber product of two three-dimensional local coefficient spaces. It retains two triangle occurrences, six directed edge occurrences and five undirected edge supports.

Set

\[
z=R_1x+R_2x=(0,b+d,c+e),\qquad h=(1,0,0).
\]

For the same local linear operator \(T\) applied independently to both triples, compatibility at composition index \(n\) is \(hT^nz=0\). Hence

\[
V_T=(R_1+R_2)^{-1}(N_T),\qquad
N_T=\bigcap_{n\ge0}\ker(hT^n)
=\ker\begin{pmatrix}h\\hT\\hT^2\end{pmatrix}.
\]

Cayley-Hamilton proves that three rows suffice for all composition indices; this is not extrapolation from sampled applications.

## Exact comparison

The source defines

\[
C(a,b,c)=(b,c,a),\qquad
S=\frac13\begin{pmatrix}2&2&-1\\-1&2&2\\2&-1&2\end{pmatrix},\qquad S^2=C.
\]

The observability matrix for \(C\) is \(I_3\). That for \(S\) has determinant \(1/3\). Both have zero unobservable subspace, so

\[
V_C=V_S=K(\mathbb R^3),\qquad
K(a,b,c)=(a,b,c,-b,-c),\qquad R_2K=-R_1K.
\]

Conversely, opposite triples remain opposite under every common linear update, establishing sufficiency. For \(T=I\), however, \(N_I=\ker h\) has dimension two and every global cochain remains seam-compatible. The geometry does not force synchronization independently of the supplied operators.

The input \((0,1,0,0,0)\) passes the initial seam condition but produces mismatch \(1\) under \(C\) and \(2/3\) under \(S\). Identity updates never expose its nonzero mismatch.

## Exchange is distinct from serial processing

Reference exchange is

\[
J(a,b,c,d,e)=(-a,d,e,b,c),\qquad J^2=I,\qquad JK(v)=K(-v).
\]

For serial embedded operations \(T_i=I_5+R_i^T(T-I_3)R_i\),

\[
JT_1J=T_2,\qquad J(T_2T_1)J=T_1T_2.
\]

The fixed-reference order differences have rank two for both \(C\) and \(S\). Serial coupling is not simultaneous gluing: \(C_2C_1K(0,1,0)=(1,0,0,0,-1)\) leaves the synchronized subspace.

Oriented seam cancellation gives \(O=L+R=b+c+d+e\), with \(L=a+b+c\) and \(R=-a+d+e\). On \(K\), \(R=-L\) and \(O=0\). Zero \(O\) alone does not imply synchronization, and serial updates need not conserve it.

## Scope

The result is a finite-dimensional linear compatibility theorem for declared operators, with an all-composition-indices proof. It does not select a processing protocol, identify the retained triangle occurrences, assign P/E or other particle types, produce isotope counts, or realize the cube/quadrangulation cut correspondence. Composition order has no supplied physical-time interpretation.

## Durable verification

- [Research note and proof](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/shared-seam-observability.md).
- [Source construction](https://github.com/andrey-kokoev/marici/blob/main/research/nima/two-triangles-shared-edge-half-phase.md).
- [Exact checker](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/checkers/check_shared_seam_observability.py): `python research/strominger/checkers/check_shared_seam_observability.py` passed 39 checks, including deliberately incompatible inputs and the identity-operator control.
- [Receipt with source hashes](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/results/shared-seam-observability.json).
- SCC: `python research/aspect/scc/scc.py check shared-seam-observability` passed the owner-local model. This is a bounded audit, not truth certification or formal proof-assistant verification.
- Standard reference: E. D. Sontag, *Mathematical Control Theory*, 2nd ed. (1998), linear observability; [DOI](https://doi.org/10.1007/978-1-4612-0577-7). The required rank argument is proved above.
- Allocator claim: `seqclaim-0c09b5ffacc083c711e2bd15`.
- Epistemic graph event: `ev-000000016276-cc5d978e-3aa8-4907-ab84-a3b1217bec81`; proposal `ep_68922373-a341-4922-b49e-187725ffe2cf`. Admission records provenance, not truth certification.
