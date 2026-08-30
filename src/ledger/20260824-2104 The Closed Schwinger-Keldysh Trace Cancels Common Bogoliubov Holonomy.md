# 2104 — The Closed Schwinger–Keldysh Trace Cancels Common Bogoliubov Holonomy

## Question

Entry 2102 activated Bogoliubov Berry phase with an explicit controlled
cross-history port.  Test whether native Schwinger–Keldysh occurrence doubling
already supplies the same physical activation.

## Frozen state-line model

On the returned squeezed-vacuum ray, write the loop transport as

\[
U_{\rm loop}=gI,
\qquad
g=e^{-16\pi i/9}.
\]

Let \(\rho\) be a normalized initial state supported on that ray.

## Identical closed branches

The normalized closed in-in contour pairs forward evolution with its adjoint:

\[
Z[J,J]
=\operatorname{Tr}(U_J\rho U_J^\dagger).
\]

For the common loop,

\[
\operatorname{Tr}(g\rho g^*)
=|g|^2\operatorname{Tr}\rho
=1.
\]

Thus

\[
\boxed{
\text{native occurrence doubling exists, but its closed physical trace
cancels common state-line holonomy.}
}
\]

## Off-diagonal history sector

If the forward history executes the loop while the backward history remains
at the identity, the influence matrix element is

\[
\operatorname{Tr}(g\rho)=g.
\]

The conjugate ordering gives \(g^*\).  Hence the phase survives in the
off-diagonal history sector, but only when a source or observable distinguishes
the two branches.

## Narrow result

Schwinger–Keldysh doubling supplies the correct labelled cross-history Carrier
port.  It does not by itself select a nontrivial readout on that port:

\[
\boxed{
\text{occurrence port}
\not\Rightarrow
\text{physical activation};
\qquad
\text{branch-asymmetric source/insertion is required.}
}
\]

This separates the three layers sharply:

\[
\text{SK Carrier doubling}
+\text{state-line coefficient}
+\text{asymmetric physical pairing}
\longrightarrow
\text{observable relative phase}.
\]

There is no need for a new Carrier occurrence.  The unresolved datum is which
source-derived cosmological observable, if any, populates the off-diagonal
history sector.

## Next falsifier

Insert one source-derived linear Gaussian observable on only one in-in branch
and compute the resulting off-diagonal characteristic function.  Test whether
the Berry phase factors out as an independently observable multiplier or is
absorbed into the insertion normalization.  The insertion and branch variance
must be fixed before evaluating the loop.

## Durable evidence

- `research/benincasa/checkers/bogoliubov_sk_phase_trace.py`
- `research/benincasa/checkers/results/bogoliubov-sk-phase-trace.json`
- Ledger allocation: `seqclaim-585c1ab2f8b7f1a038540578`

