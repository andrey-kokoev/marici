# Alternating Torsor and Descent Geometry

## Record

Date: 2026-08-12

Status: the polarity-choice obstruction is a nontrivial torsor class and does not obstruct an
equivariant all-fibers object. Entry 19 constructs the pointed cohomology-level factorization lift
and its first local presentation homotopy. An actual half-chain augmentation remains open.

## The correct base groupoid

Fix an even label set \(L\), with \(|L|=n\). Let

\[
\operatorname{Cyc}(L)
\]

be the set of oriented cyclic orders modulo rotation, and let

\[
\widetilde{\operatorname{Cyc}}(L)
=
\{(\alpha,\varepsilon):
\varepsilon(\alpha_{i+1})=-\varepsilon(\alpha_i)\}.
\]

The forgetful map

\[
p:\widetilde{\operatorname{Cyc}}(L)
\longrightarrow
\operatorname{Cyc}(L)
\]

is a principal \(\mathbb Z_2\)-bundle. Its deck transformation \(\tau\) globally flips polarity.

Permutation naturality is encoded by the action groupoids

\[
\mathcal B_L=[\operatorname{Cyc}(L)/S_L]
\simeq BC_n,
\]

\[
\widetilde{\mathcal B}_L
=[\widetilde{\operatorname{Cyc}}(L)/S_L]
\simeq BC_{n/2}.
\]

The cover is induced by the index-two inclusion \(C_{n/2}\subset C_n\). Its class is the parity
character

\[
\eta_L\in H^1(BC_n,\mathbb Z_2),
\qquad
\eta_L(r)=1
\]

for a one-step rotation \(r\). This is the precise obstruction to a permutation-natural choice of
one alternating polarity.

## What the obstruction does and does not say

The nonzero torsor class proves that there is no natural section of \(p\). It does not prove that
the two fibers cannot descend together.

For a presentation family \(Q\) over \(\widetilde{\mathcal B}_L\), the direct image

\[
p_*Q\simeq Q_+\oplus Q_-
\]

is already an all-fibers object over \(\mathcal B_L\). A descended object exists if the family has
coherent deck equivariance. Thus the corrected logical alternatives are:

\[
\boxed{\text{one canonically selected QTDS fiber: impossible}}
\]

and

\[
\boxed{\text{one equivariant object containing both fibers: possible, not yet proved}}.
\]

The same distinction applies to cyclic order itself: bare labels select no order, while a natural
family over all orders can exist.

## Factorization is operadic, not ordinary open-set descent

An ordinary topology on the finite order set has no useful overlaps. Physical composition instead
comes from gluing cyclic flags. The relevant base is therefore the two-colored cyclic Feynman
category

\[
\widetilde{\mathcal F}^{\rm alt}_0,
\]

whose objects are alternating even corollas and whose morphisms are relabelings and gluings of
oppositely colored flags. Planar quartic trees are composites of its quartic generator.

Accordingly, the desired QTDS object is a homotopy-coherent cyclic-operadic module, or dually a
factorization coalgebra, over the polarity torsor. Calling it a sheaf is too weak. Calling it a
gerbe is unsupported unless local objects and pairwise equivalences exist but a genuine triple
coherence obstruction is exhibited.

## Descent datum

Let \(\mathcal C^R_{J,P}\) be an actual chain model for the provenance-enhanced half-object, and
let

\[
Q_P\in\operatorname{Fun}(\widetilde{\mathcal B}_L,\operatorname{Ch}).
\]

A candidate augmentation is

\[
a_P:Q_P\longrightarrow p^*\mathcal C^R_{J,P}.
\]

Deck descent requires a chain equivalence

\[
T_\tau:\tau^*Q_P\xrightarrow{\sim}Q_P
\]

with

\[
T_\tau\,\tau^*T_\tau=\operatorname{id},
\qquad
a_PT_\tau=\tau^*a_P.
\]

For relabelings \(g,h\), a chosen transport can have defect

\[
c(g,h)=T_g\,g^*T_h\,T_{gh}^{-1}.
\]

If the augmentation kills this defect, it takes values in the automorphisms of the presentation
over its target. The primary strict-descent obstruction is then represented schematically by

\[
[c]\in
H^2(\mathcal B_L,
\operatorname{Aut}_{\mathcal C_J}Q_P).
\]

In a dg or infinity-categorical model, one instead chooses null-homotopies and tests the ensuing
higher coherence classes

\[
H^{k+1}(\mathcal B_L,\pi_k\operatorname{Aut}Q_P).
\]

No nonzero \(H^2\) obstruction has yet been found. The existing calculation establishes only
equality of the two evaluated total tree sums.

## Boundary datum

For a consecutive odd block \(S\subset L\), cutting adds two internal flags of opposite polarity
and produces even cyclic label sets \(S_*\) and \(S^c_*\). Required maps are

\[
\Delta_D^Q:Q_L\longrightarrow Q_{S_*}\otimes Q_{S^c_*}
\]

and

\[
\rho_D^J:\mathcal C^R_{J,L}
\longrightarrow
\mathcal C^R_{J,S_*}\otimes\mathcal C^R_{J,S^c_*}.
\]

They must obey, strictly or coherently,

\[
(a_{P,S_*}\otimes a_{P,S^c_*})\Delta_D^Q
\simeq
\rho_D^J a_{P,L},
\]

\[
\Delta_D^QT_\tau
\simeq
(T_\tau\otimes T_\tau)\tau^*\Delta_D^Q.
\]

If \(K=\operatorname{hofib}(a_P)\), the minimum composition-stability condition is

\[
\Delta_D^Q(K_L)
\subset
K_{S_*}\otimes Q_{S^c_*}
+
Q_{S_*}\otimes K_{S^c_*}.
\]

Nested cuts add cyclic Segal or coassociativity coherences. Modular completion further requires
this kernel to remain a congruence under nonseparating contractions.

## Jordan data are moduli, not a polarity gerbe

The coefficient datum is a metric Jordan pair

\[
P=(V^+,V^-,b,Q^+,Q^-),
\]

with morphisms preserving the pairing and both quadratic maps. It therefore belongs to a moduli
groupoid \(\mathcal{JP}^{\rm met}\), and the honest parameter space is

\[
\widetilde{\mathcal B}_L\times\mathcal{JP}^{\rm met},
\]

or a rank-stratum fibration of such pairs if the scalar normal geometry supplies \(P\).

Different Jordan pairs that strip to the same kinematic vertex need not be locally isomorphic.
They are genuine moduli, not different trivializations of one gerbe. The construction is intrinsic
relative to scalar provenance only when that provenance canonically retains the relevant point or
family in \(\mathcal{JP}^{\rm met}\).

## First decisive tests

At six points, build a half-chain candidate from the three quartic trees and test all six elements
of a PT basis:

\[
I_6(\operatorname{PT}_{\beta_i},[\widehat q_6])
=
I_6(\operatorname{PT}_{\beta_i},\mathsf J_6),
\qquad i=1,\ldots,6.
\]

Then construct the deck comparison and verify each of the three one-edge boundary squares.

At eight points, test all \(120=(8-3)!\) basis periods, all consecutive \(3|5\) channels, both
orders of iterated residue at codimension-two corners, and the relations among adjacent-order
transports. The difference between the two nested target contractions is predicted to be the
polarized Jordan defect

\[
\mathfrak d^\sigma(x,y)
=
Q^\sigma_{Q^sigma_x y}
-
Q_x^\sigma Q_y^{-\sigma}Q_x^\sigma.
\]

Exact samples can falsify these identities. A proof requires symbolic identities, or rational
reconstruction with declared pole and degree bounds.

## Terminology decision

Until explicit chain models and differentials exist:

- use **QTDS cyclic presentation** or **quartic lift candidate**;
- reserve **quasi-isomorphism** for a map of chain objects inducing an isomorphism on full
  homology;
- use **intrinsic modulo polarity** only after deck descent;
- use **intrinsic before pairing** only after complete-period reconstruction and factorization
  compatibility;
- reserve **strictification** for an equivalence in a declared presentation or homotopy category.

## Decision

The choice obstruction is complete and does not kill the primary frontier. Entry 19 establishes
the all-orders pointed lift after complete-period reconstruction and verifies presentation-level
factorization. The first unresolved obstruction is now chain-local: realization of the
six-point flip flow inside scalar specialization, followed by square, octagonal, and
\(\mathbb Z_2\) coherence at eight points.
