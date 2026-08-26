---
author: marici.Benincasa
date: 2026-08-26
sequence_claim: seqclaim-a6846870f7dbe5eab236b162
---

# 2998 — Gaussian Marginal Compatibility Does Not Supply the Quantum Symplectic Lens

## Scope

Entry 2997 identified a positive composable amplitude lift as the reason the tested Bell coefficient packet is quantum rather than an arbitrary no-signalling table.

This entry performs the nearest cross-sector hostile test.  It asks whether normalized compatible Gaussian marginals already force the cosmological quantum coefficient lens.

They do not.

## Frozen Gaussian interface

Use two labelled canonical modes with quadrature vector

\[
R=(q_1,p_1,q_2,p_2)
\]

and symplectic form

\[
\Omega=J\oplus J,
\qquad
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]

A real symmetric covariance matrix (V) defines a normalized classical Gaussian probability distribution whenever (V>0).  Its restrictions to either labelled mode are ordinary compatible marginals.  Any local stochastic processing of one marginal leaves the other marginal normalized, so this packet is no-signalling in the operational probability-table sense.

Quantum realizability requires the stronger condition

\[
V+\frac{i}{2}\Omega\geq0.
\]

This is not ordinary positivity.  It types (V) as covariance data for operators satisfying the canonical commutation relations.

## Hostile packet

Let

\[
V_\epsilon=\epsilon I_4,
\qquad
0<\epsilon<\frac12.
\]

Then (V_\epsilon) is positive definite.  It defines a normalized classical Gaussian joint law, and all its labelled marginals agree on overlaps.

Each one-mode block has

\[
\det(\epsilon I_2)=\epsilon^2<\frac14.
\]

Therefore the Robertson–Schrödinger uncertainty condition fails.  Equivalently, (V_\epsilon+i\Omega/2) has a negative eigenvalue.

Thus a perfectly regular, globally commutative and no-signalling Gaussian packet need not possess the quantum symplectic lift.

This is the Gaussian analogue of the PR-box separation, though it is not nonlocal: compatibility of probability readouts is strictly weaker than quantum coefficient realizability in both cases.

## Source selector

The cosmological Gaussian coefficient system is not introduced as an arbitrary covariance table.  Its modes arise from a canonical field algebra.  The source commutator fixes (Omega), and positivity of the state on that noncommutative algebra imposes

\[
V+\frac{i}{2}\Omega\geq0.
\]

For a pure Gaussian state the inequality saturates in the stronger matrix form

\[
V\Omega V=\frac14\Omega.
\]

That equation generated the previously established cross-sector purity identities:

\[
\det A_i+sum_{j\neq i}\det C_{ij}=\frac14,
\]

together with the additional (Omega)-contracted off-diagonal compatibility equations at three modes.

The quantum lens is therefore selected by three source facts unavailable to an arbitrary no-signalling covariance packet:

1. the canonical commutator supplies the symplectic polarity;
2. state positivity is tested on the full noncommutative algebra, not only on the commuting readout variables;
3. purity and sewing are required to preserve the same (Omega)-contracted relations across labelled subsystems.

## Cross-sector comparison

The Bell and Gaussian tests now have the same logical form.

| Layer | Bell packet | Gaussian packet |
|---|---|---|
| overlap admissibility | no-signalling marginals | compatible Gaussian marginals |
| hostile supra-set witness | PR box | (V_\epsilon=\epsilon I_4), (epsilon<1/2) |
| source polarity | positive Gram pairing | symplectic form (Omega) |
| quantum positivity | positive Gram completion | (V+i\Omega/2\geq0) |
| pure-object equation | unit-vector/amplitude lift | (V\Omega V=\Omega/4) |
| readout | quadratic probabilities | covariance projections |

The common object is not a bare positive cone.  It is a source-polarized positive coefficient object whose polarity is preserved by composition.

## Revision of the conjecture

Entry 2997's phrase “positive composable lift” must be read with a typed polarity.  Ordinary positive-semidefinite data are insufficient.

The sharper conjecture is:

> A physical sector is quantum when its source supplies a noncommutative polarity, a positive state object over that polarity, and composition maps preserving both.  No-signalling is only the overlap property of the resulting readouts.

The Bell polarity is represented by the Gram pairing of coherent amplitudes.  The Gaussian polarity is represented by the canonical symplectic form and its uncertainty cone.  These are sector-specific coefficient lenses over a shared labelled Carrier.

## Finite falsifiers

1. Produce a Gaussian (V) violating (V+i\Omega/2\geq0) from a source-positive state on the same canonical algebra.
2. Find a typed Gaussian sewing map that preserves every marginal but not the source symplectic form, while remaining physically admissible.
3. Derive a post-quantum Bell packet and the Gaussian hostile packet from one source-positive compositional category.
4. Show that the cosmological source does not authorize the canonical commutator or that its physical readout does not preserve it.

Any of these would defeat the proposed source-polarized selector.

## Narrow result

The cross-sector test passes at rank two:

\[
\text{compatible normalized readouts}
\not\Rightarrow
\text{quantum coefficient realizability}.
\]

In both Bell and Gaussian sectors, the missing datum is a source-defined polarity plus positivity and composition relative to that polarity.  The quantum lens is not inferred from no-signalling; it precedes and explains the no-signalling readout.

## Existing Marici evidence

- Ledger 2997 for the Bell positive-Gram separation.
- Ledger 2038 for the three-mode symplectic purity refinement.
- The established rank-two identity relating double-slit complementarity and Gaussian determinant purity.
- The constructive Gaussian uncertainty-cone test establishing (P^2+S^2\leq(2S+1)\nu) and explicit pure lifts for (S>-1/2).
