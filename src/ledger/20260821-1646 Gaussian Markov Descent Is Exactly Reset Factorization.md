# 1646 — Gaussian Markov Descent Is Exactly Reset Factorization

## Question

Entry 1645 shows that early internal pushforward can destroy temporal memory.  Identify the exact Gaussian stratum on which early pushforward is nevertheless universally safe.

## Two-step covariance comparison

After the first global Gaussian step, write

\[
V'=
\begin{pmatrix}
A'&C'\\
C'^T&B'
\end{pmatrix}.
\]

Early pushforward followed by reset to the fixed internal covariance (B_0) replaces it by

\[
V'_{\rm reset}=A'\oplus B_0.
\]

For any second Gaussian interaction whose observed output row has blocks ((X,Y)), the observed covariance discrepancy is

\[
\Delta A_2
=
Y(B'-B_0)Y^T
+XC'Y^T
+YC'^TX^T.
\]

## Exact criterion

If (B'=B_0) and (C'=0), then (Delta A_2=0) for every second step.

Conversely, requiring (Delta A_2=0) for every (X,Y) first forces (B'=B_0) by taking (X=0), then forces (C'=0) by polarization.  Hence

\[
\boxed{
\Delta A_2=0\ \forall(X,Y)
\quad\Longleftrightarrow\quad
B'=B_0, C'=0.
}
\]

For Gaussian states, (C'=0) means exact factorization of the observed and internal characteristic functions.  The equality (B'=B_0) further requires the internal factor to equal the reset state assumed by the reduced channel.

The checker verifies all 289 scalar assignments in a bounded lattice; only the unique reset-factorized assignment is invisible to every probe.

## Narrow result

\[
\boxed{
\text{The Gaussian Markov/product stratum is exactly reset factorization.}
}
\]

Outside this stratum, some later Gaussian interaction detects the discarded internal marginal or cross-correlation.  The process tensor is then mandatory.  Inside it, the process object descends canonically to ordinary channel composition.

This criterion belongs to sector coefficient data over existing labelled supports.  It introduces no new carrier incidence.

## Durable artifacts

- `research/benincasa/checkers/gaussian_markov_factorization_criterion.rs`
- `research/benincasa/results/gaussian-markov-factorization-criterion.json`
- `research/benincasa/gaussian-markov-factorization-criterion.md`

## Next falsifier

Apply the criterion to the frozen cubic cosmological interaction.  Compute the first generated internal deviation (B'-B_0) and cross block (C') in the Dyson/Rees filtration.  Determine the lowest normal order at which Markov descent fails on generic and opposite-momentum support.
