# Rational outward bounds certify the first-prime tail dimension

## Question

Can the corrected first-prime resonance reduction be converted from a floating diagnostic into a fully outward-rounded dimension bound?

## Claim boundary

Yes. Coarse rational bounds for \(\pi\), \(\log2\), \(\log24\), the negative multiplier floor, and every term in the transition estimate give the certified sufficient integer \(M=17537\). This certifies only strict positivity of the tail compression; the finite Schur form remains unchecked.

## Rational constants

Use

\[
L=\frac7{20},
\qquad
N=24,
\qquad
W=200.
\]

The elementary bounds

\[
\pi<\frac{22}{7},
\qquad
\log2>\frac{69}{100}
\]

give

\[
p=rac{2\pi}{\log2}
<
\frac{4400}{483}.
\]

Also,

\[
\pi>3,
\qquad
\log24<\frac{16}{5}.
\]

The resonance cutoff has \(K\leq4\), and

\[
\sum_{k=1}^{4}\frac1{k-1/2}
=
\frac{352}{105}.
\]

## Transition bound

The zero cell obeys

\[
D_0
<
1+2\frac{16}{5}
=
\frac{37}{5}.
\]

The middle cells obey

\[
D_{\rm middle}
<
\frac{991232}{4347}.
\]

The exterior tail obeys

\[
D_{\rm tail}
<
\frac{7040}{207}.
\]

Hence

\[
\operatorname{Tr}(T-T^2)
<
\frac{5856199}{21735}.
\]

The trace bound is

\[
\operatorname{Tr}(T)
<
\frac{70}{3}.
\]

## Tail margin

For the corrected unitary multiplier, coarse bounds

\[
\gamma<0.58,
\quad
\frac\pi2<\frac{11}{7},
\quad
3\log2<2.1,
\quad
\log\pi<1.15,
\quad
\frac{\log2}{\sqrt2}<0.497
\]

give

\[
C_-<\frac{16}{5}.
\]

Therefore

\[
\eta
=
\frac{1/20}{1/20+C_-}
>
\frac1{65}.
\]

Combining all bounds,

\[
\operatorname{Tr}(T)
+
\frac1\eta
\operatorname{Tr}(T-T^2)
<
\frac{76232017}{4347}
<17537.
\]

Thus

\[
M=17537
\]

is sufficient for the corrected first-prime tail compression to have the prescribed strict positive margin.

## Remaining gate

Let \(P_M\) project onto the first \(M\) concentration modes and let the positive tail be factored as

\[
B_M=D_MC_M^{1/2}.
\]

The unresolved RH-bearing condition is now exactly

\[
S_M
=
F_M-D_MD_M^*
\geq0
\]

for this finite block, followed by the corresponding construction for every support window. No tail estimate proves this matrix inequality.

## Disposition

The first-prime tail is now analytically and arithmetically certified. Root isolation, floating interval measures, and floating transition constants are no longer prerequisites. The finite Schur positivity gate remains open.

## Verification

- `research/voevodsky/checkers/check_rational_first_prime_dimension.py`
- `research/voevodsky/results/rational_first_prime_dimension.json`
