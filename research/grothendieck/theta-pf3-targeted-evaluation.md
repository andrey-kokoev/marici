# Theta PF3 targeted evaluation

Author: `marici.Grothendieck`
Status: high-precision numerical pass; not interval-certified
Predecessor: `theta-bilateral-kernel-normalization.md`

## Question

Does the smallest noncoalescent PF3 determinant found by the exploratory search remain positive when recomputed at substantially higher precision?

## Claim boundary

For

\[
x=(0.9997095170255212,1.7063623764293738,2.1514574926576113)
\]

and

\[
y=(0,0.0033579818240539383,0.11372711033944112),
\]

evaluate

\[
D_3(x,y)=\det[\Phi(x_i-y_j)]_{i,j=1}^{3}.
\]

A dependency-bearing high-precision preflight through `uv` was refused by structured-command policy, so no shell fallback or package installation was used. The calculation was instead repeated with Python's dependency-free `decimal` arithmetic at 100 digits, a 100-digit decimal value of \(\pi\), and 19 theta terms.

The result was

\[
D_3=1.153130727591647179647607281222035964405659782898441470739252090423720065319185744400181380501071302
\times10^{-118},
\]

and, after scaling every matrix entry by the largest entry,

\[
D_{3,\mathrm{scaled}}=
1.845100749192567198212616135323623692075718158955026483872535921358015428286313521134375537640151834
\times10^{-104}>0.
\]

Execution reference: `structured_command_execution:e_19044_1788225399555669100_6`.

## Divided-difference and positive scaling diagnosis

The Vandermonde factors are

\[
V(x)=0.3622566838969549474\ldots,
\qquad
V(y)=0.00004214926044273886\ldots.
\]

Dividing by \(V(x)V(y)\) leaves a small positive number because the matrix entries themselves lie deep in the theta tail. To remove that harmless positive scaling, set

\[
N_{ij}=\frac{M_{ij}M_{00}}{M_{i0}M_{0j}},
\qquad M_{ij}=\Phi(x_i-y_j).
\]

This multiplies rows and columns only by positive factors and therefore preserves the determinant sign. At 100-digit precision,

\[
\det N=1.849748667076097770\ldots\times10^{18}>0.
\]

Execution references: `structured_command_execution:e_19044_1788225523369860300_7` and `structured_command_execution:e_19044_1788225554852753800_8`.

The tiny raw determinant is therefore caused by tail amplitude and the small Vandermonde factor, not proximity to a PF3 sign boundary after natural positive normalization.

## Cross-ratio divided-minor search

A second seeded search used the positive row--column normalization \(N\) and minimized

\[
Q_3(x,y)=\frac{\det N}{V(x)V(y)}
\]

rather than the raw determinant. Across 200,000 ordered configurations with spacings bounded below by \(0.02\), no negative value occurred. The minimum was

\[
Q_3=153768.35481177064,
\qquad
\det N=13.1924296482061,
\]

at

\[
x=(-0.0221579756,0.0099318862,0.5129524319),
\]

\[
y=(0,0.0358310093,0.5447232908).
\]

Execution reference: `structured_command_execution:e_19044_1788225673601803400_9`.

The normalized search has a large positive margin and removes both tail amplitude and coalescence as sources of false minima. It remains exploratory and covers only the sampled bounded domain.

## Disposition

The apparent minimum was not a floating-point sign error: its positive sign persists at 100-digit precision and agrees with the original normalized value. This remains non-certifying because the decimal \(\pi\), exponentials, coordinate values, and theta tail were not enclosed with directed intervals. The next discriminating test is to remove the near-coalescent Vandermonde factors and evaluate the resulting divided-difference minor; that distinguishes genuine proximity to a PF3 boundary from coordinate coalescence.
