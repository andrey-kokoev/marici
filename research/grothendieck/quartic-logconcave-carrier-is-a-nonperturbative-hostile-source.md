# Quartic log-concave carrier is a nonperturbative hostile source

## Scope correction

The asymptotic calculation below establishes real-axis sign changes. That is
not a hostile witness against RH-style zero confinement: zeros on the real
Fourier axis are precisely the permitted analogue. The claim that this packet
proves insufficiency for confinement is therefore retracted.

Classical Pólya and de Bruijn theory also places quartic-exponential kernels
inside a major real-zero family, so no off-axis conclusion may be inferred
from the saddle cosine. The exact replacement witness is
[Modulated Gaussian is an exact off-axis hostile source](modulated-gaussian-is-an-exact-off-axis-hostile-source.md).

## Bounded question

Do positivity, evenness, uniform strict log-concavity, rapid decay, and the
absence of a terminal boundary determine the nonperturbative orientation of
the full transform?

## Hostile carrier

For \(c>0\), define

\[
g_c(x)=\exp(-x^4-cx^2).
\]

This carrier is positive, even, smooth, and rapidly decreasing. Moreover,

\[
(\log g_c)''(x)=-12x^2-2c\le-2c<0.
\]

Thus it has a uniform strict log-concavity reserve. Its autocorrelation and
tilted first-moment current satisfy every finite-boundary theorem used in the
theta band analysis. Their complete cosine and sine transforms are beyond all
algebraic orders by exactly the same parity and decay argument.

## Nonperturbative saddle pair

Consider its Fourier transform

\[
F_c(b)=\int_{\mathbb R}e^{-x^4-cx^2+ibx}\,dx.
\]

The saddle equation is

\[
4x^3+2cx=ib.
\]

As \(b\to+\infty\), the two contributing saddles are conjugate deformations
of

\[
x_\pm
=
\left(\frac b4\right)^{1/3}
e^{i\pi/6},
\qquad
\left(\frac b4\right)^{1/3}
e^{5i\pi/6}.
\]

For the quartic leading phase, the saddle action has real and imaginary parts

\[
-\kappa b^{4/3},
\qquad
\lambda b^{4/3},
\]

where

\[
\kappa=\frac{3}{2\,4^{4/3}},
\qquad
\lambda=\frac{3\sqrt3}{2\,4^{4/3}}.
\]

The quadratic term changes lower-order amplitude and phase terms but does not
remove the conjugate saddle pair. Standard steepest descent therefore gives

\[
F_c(b)
=
A_c(b)e^{-\kappa b^{4/3}}
\left[
\cos\!\left(
\lambda b^{4/3}+O(b^{2/3})+\theta_c
\right)
+o(1)
\right],
\]

with positive amplitude \(A_c(b)\) of order \(b^{-1/3}\) and a fixed phase
offset \(\theta_c\).

The phase is unbounded and eventually increasing. Hence \(F_c\) changes sign
infinitely often and has infinitely many positive real zeros.

## Retracted interpretation

The calculation shows that the following source properties do not prevent
real-axis transform oscillation:

1. positivity;
2. evenness;
3. uniform strict log-concavity;
4. Schwartz decay;
5. disappearance of every algebraic boundary jet;
6. global negativity of every finite terminal current.

The carrier satisfies all six and still has real-axis transform zeros. This is
compatible with zero confinement and supplies no RH-strength falsifier.

## Former discriminator proposal

The carrier is not Fourier--modular self-reciprocal and carries no
prime-labelled scale recursion. Those differences remain suggestive, but this
packet does not prove that either is required for zero confinement.

1. metaplectic self-reciprocity of the completed source-boundary pair;
2. labelled arithmetic scale coherence;
3. their joint constraint on the complex saddle contributions.

Neither attribute may be replaced by scalar functional symmetry after the
transform is formed.

## Corrected Deutschian conclusion

Real-axis oscillation is not the counterfactual task. The proper hostile task
must construct off-axis transform zeros while preserving the declared local
source properties. The replacement modulated-Gaussian packet does this
exactly.

## Sharp next theorem

Write the completed theta transform as a sum of its source-derived complex
saddle or thimble contributions while retaining the modular correspondence
between them. Derive a constraint on their relative phase that fails for
\(g_c\) before examining either transform's zeros.

If modular sewing supplies no such constraint beyond even scalar symmetry,
then this entire nonperturbative-orientation route closes.
