# 1642 — Second-Order Cut Positivity Is a Filtered Statement

## Falsifier

Entry 1641 proves positivity of the exact intervention superchannel.  Test whether replacing its global evolution by the real-plus-virtual second-order Dyson polynomial preserves positivity at finite coupling.

## Exact two-level test

Take

\[
H=\sigma_x,
\qquad
\rho=|0\rangle\langle0|.
\]

The second-order packet is

\[
\Phi_g^{[2]}(\rho)
=
\rho-ig[H,\rho]
+g^2\left(H\rho H-\frac12\{H^2,\rho\}\right).
\]

The (H\rho H) term is the real/Cut contribution and the anticommutator is its virtual companion.  Explicitly,

\[
\Phi_g^{[2]}(\rho)
=
\begin{pmatrix}
1-g^2&ig\\
-ig&g^2
\end{pmatrix}.
\]

Its trace is exactly one, while

\[
\boxed{\det\Phi_g^{[2]}(\rho)=-g^4.}
\]

Thus the polynomial truncation is not positive for any finite (g\ne0).  The first negative term occurs at order four, beyond the declared second-order grade.

## Narrow result

\[
\boxed{
\text{Real-plus-virtual Cut balance gives conditional positivity through }g^2,
\text{ not an exact CP polynomial at finite }g.
}
\]

The second-order packet must be typed as a filtered/Rees grade of the exact positive superchannel, or be accompanied by an independently derived positivity-preserving completion.  Its success at the retained order cannot be promoted to global positivity.

This is the dynamical analogue of the established cosmological warning

\[
\text{associated grade}\not\Rightarrow\text{global chain-level theorem}.
\]

It does not invalidate Entries 1632–1634: their real–virtual cancellation is exactly what is needed at order (g^2).  It narrows the meaning of that cancellation.

## Durable artifacts

- `research/benincasa/checkers/second_order_dyson_positivity.rs`
- `research/benincasa/results/second-order-dyson-positivity.json`
- `research/benincasa/second-order-dyson-positivity.md`

## Next falsifier

Construct the minimal source-derived CP completion whose Taylor grade agrees with the real-plus-virtual packet through (g^2).  Compare the exponential/unitary completion with a Kraus completion and test whether the completion is unique under labelled Cut sewing, trace preservation, and the (c\to0) restriction.  Nonuniqueness would show that finite-order Cut data determines only the filtered jet, not the global dynamics.
