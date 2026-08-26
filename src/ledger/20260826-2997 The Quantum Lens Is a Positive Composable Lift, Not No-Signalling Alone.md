---
author: marici.Benincasa
date: 2026-08-26
sequence_claim: seqclaim-9d0c2b627b3df57594c5ff01
---

# 2997 — The Quantum Lens Is a Positive Composable Lift, Not No-Signalling Alone

## Question

Why is the tested sector coefficient lens quantum rather than an arbitrary no-signalling lens?

This entry separates a finite answer in the two-setting Bell sector from the stronger, currently unproved claim that Carrier alone reconstructs quantum theory.

## Frozen distinction

No-signalling is an overlap condition on readouts.  For a bipartite packet (p(a,b\mid x,y)), it requires the (A)-marginal to be independent of (y) and the (B)-marginal to be independent of (x).

It does not provide:

- an amplitude object before readout;
- a positive pairing on that object;
- coherent addition of alternatives;
- tensor sewing of independently prepared systems;
- reversible transport of pure coefficient data;
- purification of mixed readouts.

The Popescu–Rohrlich packet is the finite hostile witness.  Let (a,b,x,y\in\{0,1\}) and assign probability (1/2) to the two outcomes satisfying

\[
a\mathbin{\mathsf{xor}}b=xy.
\]

Its marginals are uniform, so it is normalized and no-signalling.  Its correlators obey

\[
E_{00}=E_{01}=E_{10}=1,
\qquad
E_{11}=-1,
\]

and hence its CHSH value is (4).  No-signalling therefore admits more than the quantum lens.

## The finite quantum selector

In the correlator-only two-setting sector, a quantum realization supplies real unit vectors (u_0,u_1,v_0,v_1) such that

\[
E_{xy}=u_x\cdot v_y.
\]

Equivalently, the partially specified correlator table admits a positive-semidefinite Gram completion with unit diagonal.  Then

\[
S
=u_0\cdot(v_0+v_1)+u_1\cdot(v_0-v_1),
\]

so

\[
|S|
\leq
\|v_0+v_1\|+\|v_0-v_1\|
\leq2\sqrt2.
\]

The PR packet cannot possess such a completion because it would imply both (S=4) and (|S|\leq2\sqrt2).

The source photon packet of Entry 1571 does possess the quantum lift.  Its Bell expression is

\[
I=4\sqrt2\frac{rs}{r^2+s^2},
\]

and its distance from the quantum boundary factors as

\[
2\sqrt2-I
=
2\sqrt2\frac{(r-s)^2}{r^2+s^2}.
\]

Thus the quantum bound is not inserted as an inequality after readout.  It follows from a source amplitude packet with a positive quadratic normalization.

## Deutschian explanation

The sector lens is quantum because the frozen source does not emit an arbitrary table of compatible probabilities.  It emits coherent amplitudes.  Those amplitudes:

1. add before readout;
2. sew linearly across labelled ports;
3. carry a positive pairing used for normalization;
4. produce probabilities only after the quadratic readout;
5. compose with other coefficient objects before any setting-dependent projection.

The resulting readout necessarily factors through a positive amplitude or Gram object.  No-signalling is then a consequence of typed local restriction and normalization, not the constructor of the coefficient system.

A PR box reverses this explanatory order.  It postulates the readout table directly.  The table has compatible marginals, but there is no positive coherent lift supporting the same compositional operations.  It is an admissible overlap packet without the source object needed to generate and sew it.

Each clause is load-bearing:

- remove coherent addition and interference is unexplained;
- remove positivity and readout need not be probabilistic;
- remove quadratic normalization and the Born-type relation is lost;
- remove compositional sewing and the single experiment does not define a sector coefficient theory;
- retain only no-signalling and PR behavior returns.

## What is established

For the frozen two-setting correlator packet:

\[
\text{quantum coefficient realizability}
\Longrightarrow
\text{positive Gram completion}
\Longrightarrow
|S|\leq2\sqrt2.
\]

The source photon packet realizes this architecture and reaches the boundary when (r=s).  Arbitrary no-signalling packets do not.

This answers why the tested coefficient lens is quantum at the source-packet level: its primitive data and admitted composition are amplitude-theoretic, not probability-table-theoretic.

## What is not established

Positive Gram completion is an exact selector for the declared correlator problem, not a universal reconstruction of quantum theory.

No-signalling plus familiar device-independent constraints is known to leave post-quantum candidates.  In particular, the almost-quantum set is closed under standard classical operations and satisfies several proposed principles while remaining larger than the quantum set.

Operational reconstructions of finite-dimensional quantum theory require a stronger package.  One established route combines causality, distinguishability, compression, local distinguishability, and pure conditioning, with purification as the postulate that singles out quantum theory within that framework.

Marici has not yet derived that entire package from Carrier.  Therefore the universal claim

\[
\text{Carrier alone forces the quantum coefficient lens}
\]

remains open.

## Hard-to-vary conjecture

For every physical sector whose source objects admit coherent linear sewing, positive normalized readout, local composition, and source-authorized purification, the coefficient functor factors through a quantum positive category.  A merely no-signalling coefficient theory fails at least one of those source operations.

This conjecture predicts more than Tsirelson's bound.  It predicts that every admitted mixed coefficient packet has a source-compatible purification and that different sew-then-read and read-then-sew routes agree wherever both are typed.

## Finite falsifiers

1. Derive a source-authorized sector packet with PR correlations and all the same positive sewing and purification operations.  This falsifies the conjecture.
2. Find a frozen quantum sector whose mixed coefficient packet has no source-compatible purification.  This falsifies the proposed selector.
3. Construct two typed sewing orders whose positive readouts disagree.  This falsifies compositional sufficiency.
4. Show that the photon Bell packet's positive Gram lift depends on a fitted basis rather than the source amplitudes (r,s).  This retracts the present source-level explanation.
5. Independently recover the positive composable lift in cosmology, flavor, strings, or radiative gravity.  This supports a cross-sector promotion.

## Narrow conclusion

The tested lens is quantum not because no-signalling secretly implies quantum mechanics, but because the source supplies coherent, positively paired, composable amplitude data before readout.  No-signalling describes compatibility of the resulting local views.  It does not determine the coefficient ontology that generated them.

## Primary and local sources

- B. S. Cirel'son, *Quantum generalizations of Bell's inequality* (1980), for the quantum correlator bound and vector representation.
- S. Popescu and D. Rohrlich, *Nonlocality as an axiom for quantum theory*, arXiv:quant-ph/9508009, for superquantum no-signalling correlations.
- G. Chiribella, G. M. D'Ariano, and P. Perinotti, *Informational derivation of Quantum Theory*, arXiv:1011.6451, for the operational reconstruction and purification postulate.
- M. Navascués, Y. Guryanova, M. J. Hoban, and A. Acín, *Almost quantum correlations*, arXiv:1403.4621, for the insufficiency of several device-independent principles.
- Ledger 1571 and its exact photon Bell source-formula audit.
- Ledger 2996 and Nima's exact Bell Carrier-typing checker.
