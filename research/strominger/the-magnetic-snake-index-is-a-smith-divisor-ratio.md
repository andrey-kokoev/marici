# The magnetic snake index is a Smith-divisor ratio

## Theorem

Let

\[
A:\mathbb Z^3\longrightarrow\mathbb Z^4
\]

be an integral map of rank three. Let

\[
\pi:\mathbb Z^4\longrightarrow\mathbb Z^3
\]

be the diagonal quotient,

\[
\pi(y_1,y_2,y_3,y_4)
=
(y_1-y_4,y_2-y_4,y_3-y_4),
\]

and write

\[
R=\pi A.
\]

Assume \(R\) has rank two. Let:

- \(d_1(A)\) be the gcd of the entries of \(A\);
- \(d_2(R)\) be the gcd of the \(2\times2\) minors of \(R\);
- \(d_3(A)\) be the gcd of the \(3\times3\) minors of \(A\).

Then the normalized diagonal snake index is

\[
I(A)=\frac{d_3(A)}{d_2(R)d_1(A)}.
\]

## Proof

Choose the unimodular target coordinates consisting of the three differences and the fourth coordinate. In these coordinates,

\[
A
\sim
\begin{pmatrix}
R\\
v
\end{pmatrix}
\]

for some integral row \(v\).

Since \(R\) has rank two, its row-pair cross products are all integer multiples of the primitive generator \(k\) of \(\ker R\). The gcd of those multipliers is exactly \(d_2(R)\).

Every nonzero maximal minor of the transformed matrix is therefore

\[
c_{ij}(v\cdot k),
\]

where the gcd of the \(c_{ij}\) is \(d_2(R)\). Hence

\[
d_3(A)=d_2(R)|v\cdot k|.
\]

The scalar \(|v\cdot k|\) is the coefficient of the diagonal lift \(Ak\). Dividing by the common matrix content \(d_1(A)\) gives the normalized cyclic target index.

This proof is purely integral and does not require constructing the enormous primitive kernel vector.

## Consequence

The Fox discriminant is already visible through finite determinantal data:

\[
[\delta(A)]
=
\left[
\frac{d_3(A)}{d_2(R)d_1(A)}
\right]
quad
\text{in }
\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2.
\]

This does not yet express the discriminant directly in the group ring, but it supplies the exact finite interface between source response and snake arithmetic.

The three layers are now:

1. \(\operatorname{rank}R=2\): existence of the diagonal snake;
2. \(d_3(A)/(d_2(R)d_1(A))\): its normalized torsion index;
3. the square class of that ratio: its Fox discriminant.

## Why this matters

The huge decorated kernel coordinates were a poor presentation of a small invariant construction. Smith divisors compute the answer without choosing the kernel generator or a preferred maximal minor.

This is presentation-invariant under unimodular source and target changes that preserve the typed diagonal quotient.

It also clarifies the atomic twice-square theorem. On the atomic Fox stratum, the Smith ratio reduces to

\[
2\kappa^2.
\]

Off that stratum, the same ratio remains valid while its square class varies.

## Verification

The augmented magnetic checker evaluates the baseline and three charge-neutral decorations under both primitive response signs. In every case,

\[
I(A)
=
\frac{d_3(A)}{d_2(R)d_1(A)}
\]

exactly reproduces the cyclic target index.

All seven aggregate gates pass.
