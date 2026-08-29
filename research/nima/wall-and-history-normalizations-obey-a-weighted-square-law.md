# Wall and history normalizations obey a weighted square law

## General normalized auxiliary block

The source may not provide the unit-normalized graph block. Introduce explicit coefficients

\[
D_\pm(\lambda,\mu)
=
\frac12
\left(
\lambda I+H^{*}H
\right)
\pm
\frac{i\mu}{2}
\left(
H-H^{*}
\right),
\]

where:

- \(\lambda>0\) is the coefficient-wall energy;
- \(\mu\in\mathbb R\) is the causal odd coupling strength;
- the history-output coefficient is frozen to one in this presentation.

For any \(x\),

\[
2\langle x,D_\pm x\rangle
=
\lambda\|x\|^2+\|Hx\|^2
\mp
2\mu\,\operatorname{Im}\langle x,Hx\rangle.
\]

## Universal positivity condition

Cauchy–Schwarz gives

\[
2|\mu|
\left|
\operatorname{Im}\langle x,Hx\rangle
\right|
\le
2|\mu|\|x\|\|Hx\|.
\]

The weighted square identity is

\[
\lambda\|x\|^2+\|Hx\|^2
-
2|\mu|\|x\|\|Hx\|
=
\left(
\sqrt\lambda\|x\|-\frac{|\mu|}{\sqrt\lambda}\|Hx\|
\right)^2
+
\left(
1-\frac{\mu^2}{\lambda}
\right)\|Hx\|^2.
\]

Hence a source-independent sufficient condition is

\[
|\mu|\le\sqrt\lambda.
\]

At the matched value

\[
|\mu|=\sqrt\lambda,
\]

the block factors exactly:

\[
D_\pm
=
\frac12
\left(
\sqrt\lambda I\pm i\,\operatorname{sgn}(\mu)H
\right)^{*}
\left(
\sqrt\lambda I\pm i\,\operatorname{sgn}(\mu)H
\right),
\]

with the sheet sign adjusted consistently.

Thus the previous unit square is the special case \(\lambda=\mu=1\).

## Uniform cutoff bound from theta mass

If

\[
\|H_L\|\le M
\]

uniformly, then in the matched case

\[
D_{L,\pm}
\ge
\frac12
\left(
\sqrt\lambda-M
\right)^2I
\]

provided

\[
M<\sqrt\lambda.
\]

If \(H_L=\alpha_p H_L^{(0)}\) and the base theta mass is \(M_\Phi\), the condition is

\[
|\alpha_p|M_\Phi<\sqrt\lambda.
\]

This is the exact weighted normalization budget.

## Unmatched odd coupling

When \(|\mu|<\sqrt\lambda\), positivity has reserve even without a small history norm. But the block is no longer one shifted-history square; it is a square plus residual history energy.

When \(|\mu|>\sqrt\lambda\), universal positivity fails. A particular bounded history may still yield a positive block if its norm range avoids the dangerous scale, but that requires a source-specific numerical-range theorem.

Therefore matching \(\mu=\sqrt\lambda\) is structural, not cosmetic: it is the coefficient law that makes causal oddness and wall/history energy one Gram constructor.

## Conventional theta budget

Under the candidate conventional normalization

\[
M_\Phi=\xi(1/2)\approx0.497120778,
\]

a unit wall has amplitude budget

\[
|\alpha_p|<\frac1{M_\Phi}
\approx2.011584.
\]

Thus:

- one half-line copy passes with substantial margin;
- a factor-two bilateral convention still passes, but only narrowly:
  \[
  2M_\Phi\approx0.994241556<1;
  \]
- any additional factor beyond approximately \(2.011584\) breaks the Neumann certificate.

These numerical statements are conditional until the exact source normalization is frozen.

## Coefficient placement test

The following operations are not interchangeable:

1. scale the history operator \(H\mapsto\alpha H\);
2. scale the odd coupling \(\mu\);
3. scale the wall energy \(\lambda\);
4. scale the complete block after forming it.

Only the fourth preserves all dimensionless internal geometry automatically. Prime pushforward must therefore state where Euler half-density and bilateral factors enter.

## Hostile

Choose \(\lambda=1\), \(\mu=2\), and a history mode with \(Hx=ix\). Then

\[
\langle x,D_+x\rangle<0
\]

despite positive wall and history energies. Correct sign and causal typing do not repair a normalization mismatch.

## Next source theorem

Extract the exact triple

\[
(\lambda_p,\mu_p,\alpha_p)
\]

from coefficient-wall representation, causal-history incidence, and prime weighting. Then verify

\[
|\mu_p|\le\sqrt{\lambda_p},
\qquad
|\alpha_p|M_\Phi<\sqrt{\lambda_p}
\]

uniformly. This is the complete normalization audit for the auxiliary Adams cell.
