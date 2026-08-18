# 20260818-857 The Canonically Fixed Final-Block Extension Projection Is Dense

## Question

Before choosing a common primitive normalization for the five ambiguous absolute rows, does the exact reduction already force a smaller decoupled extension involving the final four masters?

## Fixed projection

Entry 374's invariant coordinate mask includes

\[
(e_6,e_7,e_8,e_9).
\]

Therefore the projection

\[
B_\mu^{\rm final}:
W_3\longrightarrow
\langle e_6,e_7,e_8,e_9\rangle
\]

is independent of the primitive exact-lift nullspace at every generic sample.  The reduction engine now exports this \(4\times3\) block alongside \(A_3\).

## Census

At

\[
(u,v)=(7,11),(13,19),(23,29)
\]

over

\[
\mathbb F_{2305843009213693951},
\]

for both \(\partial_u\) and \(\partial_v\), all

\[
3\cdot2\cdot4\cdot3=72
\]

entries are nonzero.

Thus every quotient generator

\[
q_0,q_1,q_2
\]

couples to every final-block class

\[
e_6,e_7,e_8,e_9
\]

at the tested generic points.

## Narrow conclusion

No top-line-only, wall-line-only, elliptic-quotient-only, or algebraic-kernel-only shortcut is supported by the source reduction.  Even the primitive-lift-invariant projection of the extension is generically dense.

This does not determine its characteristic-zero entries or its class modulo triangular connection gauge.  Density is basis-dependent and is not intrinsic support.  Its role is only to prohibit splitting the source derivation into independently fitted line extensions.

The next calculation must derive the common four-stratum extension representative as one coupled object, then apply Entry 850's gauge-invariant acceptance contract.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`
- `research/benincasa/marked-extension-fixed-final-block-census.json`
- Epistemic event `ev-000000000471-84915db7-8a4b-4cf2-8dd3-90f2926b30bf`
