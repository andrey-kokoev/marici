# 1686 — The Infinite Cubic Dyson-Schmidt Tower Has a Finite Shift Presentation

## Finite-presentation falsifier

Entry 1685 proves unbounded Schmidt rank. Test whether this infinite coefficient
object is nevertheless finitely presented and compatible with filtered Cut
composition.

Let

\[
A=q_1q_2q_3,
\qquad
U(z)=e^{zA}
=\sum_{n\ge0}c_nA^n,
\qquad
c_n=\frac{z^n}{n!}.
\]

The complete coefficient sequence obeys one first-order shift recurrence:

\[
\boxed{
(n+1)c_{n+1}=zc_n.
}
\]

Equivalently, the operator family has the finite differential presentation

\[
(\partial_z-A)U=0,
\qquad
U(0)=1.
\]

## Filtered composition

Composition of two copies uses binomial convolution:

\[
\sum_{i+j=n}\frac1{i!j!}
=\frac{2^n}{n!}.
\]

For three copies, both parenthesizations give

\[
\sum_{i+j+k=n}\frac1{i!j!k!}
=\frac{3^n}{n!}.
\]

Thus Dyson order is a canonical additive bond filtration and its convolution is
associative.

For every finite truncation

\[
U_{\le K}=\sum_{n=0}^Kc_nA^n,
\]

the map

\[
\rho\longmapsto U_{\le K}\rho U_{\le K}^{\dagger}
\]

is one-Kraus and completely positive. Partial trace/Cut contraction preserves
positivity. It is not generally trace-preserving because (U_{\le K}) is not
exactly unitary.

The exact checker verifies 34 factorial recurrences, 61 binary convolutions, 61
ternary parenthesization identities, and 100 exact CP Gram factorizations.

## Narrow result

\[
\boxed{
\text{the infinite cubic Dyson--Schmidt tower is unbounded in rank but finitely presented by one shift generator.}
}
\]

This parallels Entry 1649's finite differential presentation of the infinite
moment module. The two infinite coefficient realizations are structured, not
arbitrary, and require no infinite family of carrier incidences.

Finite-order positivity is retained, but trace preservation requires the full
unitary or a source-derived normalization/virtual comparison.

## Durable artifacts

- `research/benincasa/checkers/cubic_dyson_finite_presentation.rs`
- `research/benincasa/results/cubic-dyson-finite-presentation.json`
- `research/benincasa/cubic-dyson-finite-presentation.md`

## Next falsifier

Compare the moment-module presentation of Entry 1649 with the Dyson-Schmidt
shift presentation. Construct the source-derived transform from bond order
(n) to moment-degree growth and test whether it is a filtered chain map. Do
not infer equivalence merely from both presentations being finite.