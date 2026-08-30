# Source scale and the dimensionless coefficient fiber

## Question

WP981 tests the strongest transfer proposed after WP980: can one independently
declared source normalization scale \(N>0\) select the determinant-mediator
coefficient ray?

The WP977 elimination formula is

\[
\rho=\frac{k}{q}
=\frac{\gamma^2\mu^4}{m_s^2(m_A^2)^5}.
\]

Its mass weight is \(-8\). Define source-normalized coordinates

\[
a=\frac{\mu}{N},\qquad
b=\frac{m_s^2}{N^2},\qquad
c=\frac{m_A^2}{N^2},
\]

and the dimensionless competition coefficient

\[
\widehat\rho=N^8\rho
=\frac{\gamma^2a^4}{bc^5}.
\]

The normalization scale cancels exactly.

## Hostile normalized pair

Fix the same source scale, coercive coupling, and normalized squared masses:

\[
N=1,qquad \gamma=8,qquad b=c=1.
\]

Only the dimensionless cubic ratio \(a\) differs:

\[
\begin{array}{c|c}
a & \widehat\rho\\
\hline
4 & 16384\\
5 & 40000
\end{array}
\]

These values lie on opposite sides of the WP978 crossing \(24696\).

## Consequence

A source-bearing scale repairs dimensional typing but does not select the
dimensionless coefficient ray. Even the two additional relations
\(m_s^2=N^2\) and \(m_A^2=N^2\) leave the free ratio \(\mu/N\), which
crosses the hostile vacuum boundary.

The required source structure is therefore not merely a scale. It must derive
enough dimensionless relations to constrain
\(\gamma^2a^4/(bc^5)\) to a proper range before the desired flavor readout is
used. It need not fix every coupling separately, but it must cut this
combination.

This result does not reject dimensional transmutation or a dynamical source
scale. It rejects granting selector authority to the scale alone.

The smallest falsifier is an independently derived dimensionless relation
whose solution set forces \(\widehat\rho\) to one side of the exact crossing
and survives the complete coupled-vacuum and instrument gates.

## Reproduction

Run:

    python research/flavor/checkers/wp981_source_scale_dimensionless_fiber.py

The generated result is
research/flavor/results/wp981_source_scale_dimensionless_fiber.json.
