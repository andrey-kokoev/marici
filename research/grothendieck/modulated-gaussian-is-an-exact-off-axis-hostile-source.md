# Modulated Gaussian is an exact off-axis hostile source

## Bounded question

Can positivity, evenness, uniform strict log-concavity, Schwartz decay, and
boundaryless algebraic cancellation coexist with off-axis transform zeros?

## Exact carrier

For \(0<\varepsilon<1\) and \(k>0\), define

\[
g_{\varepsilon,k}(x)
=
e^{-x^2}\left[1+\varepsilon\cos(kx)\right].
\]

It is positive, even, smooth, and Schwartz.

## Uniform strict log-concavity

Direct differentiation gives

\[
(\log g_{\varepsilon,k})''(x)
=
-2
-
\frac{
\varepsilon k^2[\cos(kx)+\varepsilon]
}{
[1+\varepsilon\cos(kx)]^2
}.
\]

The perturbation obeys the uniform bound

\[
\left|
\frac{
\varepsilon k^2[\cos(kx)+\varepsilon]
}{
[1+\varepsilon\cos(kx)]^2
}
\right|
\le
\frac{\varepsilon k^2(1+\varepsilon)}{(1-\varepsilon)^2}.
\]

Hence the source is uniformly strictly log-concave whenever

\[
\frac{\varepsilon k^2(1+\varepsilon)}{(1-\varepsilon)^2}<2.
\]

For example, \(\varepsilon=1/10\) and \(k=1\) satisfy this condition.

## Exact transform and zeros

With the Fourier convention

\[
F_{\varepsilon,k}(z)
=
\int_{\mathbb R}g_{\varepsilon,k}(x)e^{izx}\,dx,
\]

Gaussian translation gives the exact factorization

\[
F_{\varepsilon,k}(z)
=
\sqrt\pi e^{-z^2/4}
\left[
1+\varepsilon e^{-k^2/4}\cosh(kz/2)
\right].
\]

Put

\[
A=\frac{e^{k^2/4}}{\varepsilon}>1.
\]

The zeros are exactly

\[
z_{n,\pm}
=
\pm\frac{2}{k}\operatorname{arcosh}(A)
+
i\frac{2\pi(2n+1)}{k},
\qquad n\in\mathbb Z.
\]

Every zero has nonzero real part. They occur in the required reflection and
conjugation packets.

## Shared boundaryless properties

The carrier and all its autocorrelations are Schwartz. Its even/odd full-line
extensions therefore have every algebraic integration-by-parts boundary jet
cancelled, just as in the theta boundaryless theorem. Strict log-concavity
also makes every finite terminal current negative.

Thus this carrier shares all of the local and boundaryless properties used so
far while exhibiting explicit off-axis transform zeros.

## Result

The following properties are jointly insufficient for RH-style zero
confinement:

1. positivity;
2. evenness;
3. uniform strict log-concavity;
4. Schwartz decay;
5. disappearance of every algebraic terminal contribution in the full
   transform;
6. negative finite terminal currents;
7. reflection and conjugation symmetry of the zero packet.

The exact missing information must reject the cosine modulation before scalar
compression.

## Source discriminator

The hostile modulation introduces two shifted Gaussian frequency labels but
has no authorized modular-scale recursion tying those labels to a primal--dual
arithmetic boundary. This sharpens the next theorem:

> Derive a labelled modular correspondence that the completed theta source
> satisfies and the modulated Gaussian fails, then prove that the
> correspondence excludes off-axis transform zeros.

The last implication remains the hard RH-strength gate. But the hostile test
is now exact and correctly typed.
