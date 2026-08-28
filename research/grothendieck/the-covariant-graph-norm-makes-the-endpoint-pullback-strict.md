# The covariant graph norm makes the endpoint pullback strict

## Weighted half-line fibers

For real `a`, let

\[
\mathcal H_a^+
=
L^2(\mathbb R_+,e^{2aq}\,dq).
\]

The unitary trivialization to ordinary `L^2` is

\[
T_af=e^{aq}f.
\]

The derivative transported through this trivialization is

\[
\nabla_af
=T_a^{-1}\partial_qT_af
=f'+af.
\]

Equip the domain of `nabla_a` with the covariant graph norm

\[
\|f\|_{a,1}^2
=
\|f\|_{\mathcal H_a^+}^2
+
\|\nabla_af\|_{\mathcal H_a^+}^2.
\]

Under `T_a`, this is exactly the ordinary `H^1(R_+)` norm.

## Uniform endpoint theorem

For `g` in `H^1(R_+)`, the standard trace estimate gives

\[
|g(0)|^2
\le
2\|g\|_2\|g'\|_2
\le
\|g\|_2^2+\|g'\|_2^2.
\]

Since `T_af(0)=f(0)`, it follows that

\[
|f(0)|^2\le\|f\|_{a,1}^2.
\]

The endpoint map

\[
\operatorname{ev}_0:\operatorname{Dom}\nabla_a\longrightarrow\mathbb C
\]

is therefore continuous with a constant independent of `a`.

## Mellin covariance

For the moving-fiber transport

\[
U_{a\to b}f=e^{(a-b)q}f,
\]

one has

\[
\nabla_bU_{a\to b}=U_{a\to b}\nabla_a
\]

and

\[
(U_{a\to b}f)(0)=f(0).
\]

Thus Mellin transport is unitary for the graph norms and preserves endpoint
evaluation exactly. No endpoint anomaly is created by moving between
spectral-weight fibers.

## Strict plus/minus pullback

Apply the same construction to the reciprocal half-line fiber. Let `E_+` and
`E_-` denote the two graph domains and define the completed augmentation

\[
\epsilon:E_+\oplus E_-\longrightarrow\mathbb C,
\qquad
\epsilon(f_+,f_-)=f_+(0)+f_-(0).
\]

The map is continuous and surjective. A bounded right inverse is obtained by
choosing one fixed `H^1` bump with endpoint value one and transporting it
unitarily into the required weighted fiber. Hence

\[
\ker\epsilon
\]

is closed and complemented. The anti-diagonal endpoint domain is a strict
pullback, not a dense nonclosed relation.

Equivalently, with the orientation sign absorbed on the negative chart, the
pullback is the ordinary `H^1` gluing of two half-lines across a common trace.

## Consequence

The following layers are now flat or strict under their natural typing:

1. local Fourier–Tate transport;
2. injective trace sewing;
3. Mellin spectral-flow filling;
4. weighted graph completion;
5. scalar endpoint augmentation and plus/minus pullback.

None can create the missing RH class by itself.

The remaining candidate must use data not present in this scalar first-order
endpoint problem:

- simultaneous restricted-product control across primes;
- primitive and prime-square boundary seminorms not equivalent to the
  covariant `H^1` norm;
- an operator-valued Green/response incidence;
- determinant compression that detects a relative class;
- or a global multiplicative-to-additive distributive defect.

## Sharp warning

If a proposed completion class disappears when the covariant derivative
`nabla_a=f'+af` is used instead of the ordinary derivative in every fiber,
then it was caused by comparing moving spectral frames with a fixed
connection. Such a class is a coordinate artifact.

## Next test

Adjoin the first genuinely arithmetic boundary coordinate to the covariant
graph norm. The primitive current is the minimal candidate. Determine whether
its evaluation is continuous under `U_(a->b)` and whether the augmented
endpoint map remains split uniformly over prime cutoff. If it does, repeat
with the prime-square coordinate. If it fails, the first escaping sequence is
the sought completion witness.

## Scope

This proves uniform endpoint continuity and strict anti-diagonal pullback for
the covariant weighted first-order graph domains. It does not include the
arithmetic boundary currents, operator-valued Green response, determinant
bridge, or RH.
