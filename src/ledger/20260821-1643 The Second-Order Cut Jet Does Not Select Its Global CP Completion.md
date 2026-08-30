# 1643 — The Second-Order Cut Jet Does Not Select Its Global CP Completion

## Question

Entry 1642 shows that the second-order Dyson polynomial is only a filtered positive object.  Test whether its source-fixed real-plus-virtual coefficients nevertheless determine a unique exact CP completion.

## Two completions

For (H^2=I), write the truncated amplitude as

\[
A_2(g)=\left(1-\frac{g^2}{2}\right)I-igH.
\]

The Hamiltonian exponential is

\[
U_{\exp}(g)=e^{-igH}.
\]

Independently, since

\[
A_2^\dagger A_2
=
\left(1+\frac{g^4}{4}\right)I,
\]

polar normalization gives another exact unitary,

\[
U_{\rm pol}(g)
=
\frac{A_2(g)}{\sqrt{1+g^4/4}}.
\]

Both induce exact CPTP channels and reproduce the same Dyson/Cut jet through (g^2).  They differ at (g^3):

\[
U_{\exp}(g)
=I-igH-\frac{g^2}{2}I+\frac{ig^3}{6}H+O(g^4),
\]

whereas (U_{\rm pol}) has no cubic term.

## Narrow result

\[
\boxed{
\text{The second-order Cut/Rees jet admits inequivalent exact CP completions.}
}
\]

Therefore finite-order Cut data determines the filtered dynamics but not its global completion.  The exponential is canonical only after adjoining an additional source law: (g) must parametrize a one-parameter group with fixed generator (H).  That group law is not encoded by the second-order jet itself.

This does not imply arbitrariness of the primary quantum theory, where the Hamiltonian and time-ordering prescription are frozen.  It prohibits reconstructing that global theory from the second-order cosmological Cut packet alone.

## Durable artifacts

- `research/benincasa/checkers/second_order_cp_completion_nonuniqueness.rs`
- `research/benincasa/results/second-order-cp-completion-nonuniqueness.json`
- `research/benincasa/second-order-cp-completion-nonuniqueness.md`

## Next falsifier

Adjoin the source one-parameter composition law and test whether it is compatible with labelled Cut sewing and the supported intervention superchannel.  If composition fixes the exponential uniquely and respects the (c\to0) restriction, the exact global dynamics is recovered from

\[
\text{filtered Cut jet}+\text{source composition law},
\]

not from the carrier or jet alone.
