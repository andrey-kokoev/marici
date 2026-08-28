# Determinant mediator chain

## Objective

WP977 asks whether the degree-twelve CP-magnitude operator isolated by WP976
can arise from a renormalizable source grammar rather than being inserted as a
fundamental high-degree interaction.

Let \(X,Y\) be the Hermitian coefficient fields and
\(H=i[X,Y]\). Add a Hermitian adjoint mediator \(A\) and a real CP-odd scalar
\(s\). The source interactions are

\[
V_{\rm aux}=
\frac{m_A^2}{2}\operatorname{tr}A^2
-\mu\operatorname{tr}(AH)
+\frac{m_s^2}{2}s^2
-\gamma s\det A
+\lambda\left(s^2+\operatorname{tr}A^2\right)^2.
\]

The \(A[X,Y]\) vertex has field degree three and \(s\det A\) has degree four.
Every displayed fundamental interaction is therefore renormalizable.

## Low-field elimination

At leading order around the massive auxiliary origin,

\[
A=\frac{\mu}{m_A^2}H+O(H^3),\qquad
s=\frac{\gamma}{m_s^2}\det A+O(A^5).
\]

Substitution generates

\[
V_{\rm eff}\supset
-\frac{\gamma^2\mu^6}
{2m_s^2(m_A^2)^6}
\left(\det H\right)^2.
\]

Since \(H=i[X,Y]\), this is the negative full-rank CP-magnitude operator of
WP976. The same chain also generates the lower-degree negative commutator
square through elimination of \(A\).

## Auxiliary-sector stability

For Hermitian three-by-three \(A\), let
\(R=s^2+\operatorname{tr}A^2\). The determinant and arithmetic-geometric mean
bounds give

\[
|s\det A|\le\frac{R^2}{16}.
\]

Hence the quartic auxiliary sector obeys

\[
\lambda R^2-\gamma s\det A
\ge\left(\lambda-\frac{|\gamma|}{16}\right)R^2.
\]

It is strictly coercive when \(\lambda>|\gamma|/16\). The exact benchmark
\((\lambda,\gamma,\mu,m_A^2,m_s^2)=(1,8,1,1,1)\) has stability margin
\(1/2\) and leading determinant coefficient \(32\).

## Authority and remaining gates

This is a genuine renormalizable source-constructor architecture for the
WP976 operator. It does not yet prove a full stable coupled \(X,Y,A,s\) vacuum,
select the remaining coefficient ratios, map the vacuum across the complete
physical16 ensemble, or provide an instrument. The pseudoscalar remains
dynamical, so the reference-free theory retains the CP-conjugate sign pair
identified by WP975.

## Reproduction

Run:

    python research/flavor/checkers/wp977_determinant_mediator_chain.py

The generated result is
research/flavor/results/wp977_determinant_mediator_chain.json.
