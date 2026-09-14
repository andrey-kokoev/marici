# The grade-8085 four-cube raises probe depth

## Question

Does the canonical four-shell Boolean cube complete at grade 8085 and force a third modulated character evaluation?

## Claim boundary

Yes for the exact finite incidence model over two tested prime fields. At cutoff 8084, two modulated settings together with the coarse readout have full edge rank. At cutoff 8085, the same family has deficiency one, while three modulated settings restore full rank. This identifies a finite cubical probe-depth transition. Characteristic-zero proof and a general all-dimensional theorem remain separate obligations.

## Canonical four-cube

Use the first four shell ratios

\[
\frac32,\qquad\frac53,\qquad\frac75,\qquad\frac{11}{7}
\]

and base vertex

\[
210=2\cdot3\cdot5\cdot7.
\]

Applying every subset produces sixteen vertices and thirty-two edges, hence a functor

\[
\{0<1\}^4\longrightarrow\mathcal C.
\]

The top vertex is

\[
210\cdot\frac32\cdot\frac53\cdot\frac75\cdot\frac{11}{7}=1155.
\]

The final edge is

\[
735\longrightarrow1155
\]

in shell \((7,11)\). Its admission grade is

\[
105\cdot7\cdot11=8085
=3\cdot5\cdot7^2\cdot11.
\]

## Exact rank transition

At cutoff 8084:

- 2407 edges;
- boundary rank 1955;
- cycle dimension 452;
- one-setting deficiency 43;
- two-setting deficiency 0.

At cutoff 8085 three edges enter:

\[
1617\to2695,
\qquad
1155\to1617,
\qquad
735\to1155,
\]

in shells 2, 3, and 4 respectively. The graph then has:

- 2410 edges;
- boundary rank 1956;
- cycle dimension 454;
- one-setting deficiency 44;
- two-setting deficiency 1;
- three-setting deficiency 0.

Both moduli \(1000000007\) and \(1000000009\) give the same ranks.

## Emerging law

The first adjacent-shell square completes at

\[
45=3^2\cdot5.
\]

The three-shell cube completes at

\[
525=3\cdot5^2\cdot7.
\]

The four-shell cube completes at

\[
8085=3\cdot5\cdot7^2\cdot11.
\]

At cubical dimension \(n\), the coarse readout plus \(n-1\) distinct modulated evaluations supplies \(n\) character values. The observed transitions agree with the interpolation rule:

- square: one modulated setting;
- cube: two modulated settings;
- four-cube: three modulated settings.

For consecutive primes \(p_1=2,p_2=3,\ldots\), the canonical adjacent-shell \(n\)-cube based at \(p_1\cdots p_n\) has final-edge grade

\[
L_n=p_2p_3\cdots p_{n-1}p_n^2p_{n+1}
\]

for \(n\geq2\). The formula constructs the cube and its final edge. A theorem that this grade always gives the first global probe-depth transition requires further proof.

## Strongest falsification attempt

The hostile compares the complete graph immediately below and at the predicted grade. This prevents a large-cutoff observation from being attributed to an unspecified accumulation of edges. The predicted change is specific: two settings go from full rank to deficiency one exactly when the four-cube's final edge enters, and a third setting restores rank.

The hostile passes. Deletion tests localize the cause among the three edges entering at grade 8085. Removing either \(1617\to2695\) or \(1155\to1617\) leaves the two-setting deficiency at one. Removing the cube-final edge \(735\to1155\) restores full two-setting rank. Thus the simultaneous-edge rival fails: the predicted four-cube completion uniquely carries the new blind direction.

## Disposition

The cubical-dimension law survives its first out-of-sample prediction. The grade 8085 was derived from the cube before the rank computation, the exact rank change matches the predicted setting count, and edge deletion localizes the transition to the cube-final edge. The result is finite modular evidence; characteristic-zero proof and the general dimension law remain open.
