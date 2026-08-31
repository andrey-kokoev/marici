# Logarithmic denominator gate for the triple-incidence p-normal primitive

## Question

Does the cleared numerator primitive

\[
H_p=pq_1\,dq_2
\]

lift to a logarithmic one-form primitive for

\[
p\eta=p\frac{dq_1\wedge dq_2}{q_1q_2q_3},
\qquad q_3=q_1+q_2+p,
\]

without using \(1/p\)?

## Claim boundary

This packet tests the pure logarithmic denominator carrier and a bounded rational ansatz. It does not construct a Čech localization complex, resolved/Rees exceptional face, global contour, physical period, or full Cayley--Menger face census.

## Disposition

In the logarithmic denominator carrier

\[
R[q_1^{-1},q_2^{-1},q_3^{-1}],
\]

the degree-one logarithmic basis is

\[
d\log q_1,
\quad d\log q_2,
\quad d\log q_3,
\]

and the degree-two basis is

\[
\omega_{12},\quad \omega_{13},\quad \omega_{23}.
\]

The degree-one logarithmic generators are closed. Therefore the logarithmic subcomplex supplies no one-form primitive whose differential is

\[
p\eta=\omega_{12}-\omega_{13}+\omega_{23}.
\]

A bounded rational search was also negative. After setting \(p=1\), the checker searched forms

\[
A\,dq_1+B\,dq_2,
\qquad
A=P/D^m,\quad B=Q/D^m,
\quad D=q_1q_2q_3,
\]

with pole depths \(m=1,2\) and numerator degree at most \(2m\). Matching

\[
\partial_{q_1}B-
\partial_{q_2}A=1/D
\]

gave inconsistent linear systems over both \(\mathbb F_{101}\) and \(\mathbb F_{103}\): ranks \((9,10)\) for depth one and \((24,25)\) for depth two.

Thus the cleared numerator primitive does not pass the denominator gate. The first missing enlargement is a genuine Čech localization differential or resolved/Rees exceptional face generator that can supply a source-derived primitive. The test uses no ambient division by \(p\), no circuit quotient, no all-soft \(\mathbb Z/3\) import, no identity-monodromy inference, and no physical-period promotion.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_log_denominator_primitive_gate.py`

Result:

- `research/voevodsky/results/cosmology_log_denominator_primitive_gate.json`

Command:

- `uv run --with sympy python research/voevodsky/check_cosmology_log_denominator_primitive_gate.py`
