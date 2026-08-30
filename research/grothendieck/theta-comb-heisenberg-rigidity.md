# The integer comb is the unique joint-fixed Heisenberg boundary distribution

Author: `marici.Grothendieck`

## 1. Translation and modulation

On \(\mathcal S'(\mathbb R)\), let

\[
 (\tau_1h)(x)=h(x-1),
 \qquad
 (M_1h)(x)=e^{2\pi ix}h(x).
\]

The integer comb

\[
 \Delta_{\mathbb Z}
 =\sum_{n\in\mathbb Z}\delta_n
\]

satisfies

\[
\boxed{
 \tau_1\Delta_{\mathbb Z}=\Delta_{\mathbb Z},
 \qquad
 M_1\Delta_{\mathbb Z}=\Delta_{\mathbb Z}.}
\]

Translation permutes its support, while modulation evaluates to
\(e^{2\pi in}=1\) at every integral point.

## 2. Exact uniqueness theorem

**Theorem.** If \(\Lambda\in\mathcal S'(\mathbb R)\) satisfies

\[
 \tau_1\Lambda=\Lambda,
 \qquad
 M_1\Lambda=\Lambda,
\]

then

\[
 \Lambda=c\,\Delta_{\mathbb Z}
\]

for some scalar \(c\).

**Proof.** Translation invariance makes \(\Lambda\) a one-periodic tempered
distribution, hence it has a distributional Fourier series

\[
 \Lambda=\sum_{n\in\mathbb Z}c_ne^{2\pi inx}
\]

with polynomially bounded coefficients. Multiplication by \(e^{2\pi ix}\)
shifts the sequence:

\[
 M_1\Lambda
 =\sum_nc_{n-1}e^{2\pi inx}.
\]

The equality \(M_1\Lambda=\Lambda\) implies

\[
 c_{n-1}=c_n
\]

for every \(n\). Thus all coefficients equal one constant \(c\), and

\[
 \Lambda
 =c\sum_{n\in\mathbb Z}e^{2\pi inx}
 =c\,\Delta_{\mathbb Z}
\]

by Poisson summation in \(\mathcal S'\). \(\square\)

## 3. Distributional typing is forced

There is no nonzero vector in \(L^2(\mathbb R)\) invariant under unit
translation. A nonzero one-periodic function has infinite \(L^2(\mathbb R)\)
norm. Therefore the joint-fixed arithmetic boundary cannot be an ordinary
Hilbert vector.

The Gelfand triple

\[
 \mathcal S(\mathbb R)
 \subset L^2(\mathbb R)
 \subset\mathcal S'(\mathbb R)
\]

is not a technical indulgence introduced to accommodate the desired answer.
It is the minimal natural type in which the unique Heisenberg-fixed boundary
exists.

## 4. Fourier quarter-turn exchanges the two constraints

Fourier transformation conjugates translation and modulation:

\[
 \mathcal F\tau_1\mathcal F^{-1}=M_{-1},
 \qquad
 \mathcal FM_1\mathcal F^{-1}=\tau_1.
\]

Hence the joint-fixed line is preserved by the metaplectic quarter-turn.
Uniqueness then implies

\[
 \mathcal F\Delta_{\mathbb Z}
 =c\Delta_{\mathbb Z}.
\]

The standard Fourier convention and Poisson normalization give \(c=1\).

Thus self-duality of the comb follows from the more primitive relational
statement that it is fixed by the critical integral time--frequency lattice.

## 5. Dilation moves the polarization lattice

Conjugating the Heisenberg generators by dilation gives

\[
 R_u\tau_1R_u^{-1}=\tau_{e^{-u}},
 \qquad
 R_uM_1R_u^{-1}=M_{e^u},
\]

up to the chosen active/passive convention. Their phase-space cell retains
area one:

\[
 e^{-u}e^u=1.
\]

Therefore \(R_u\Delta_{\mathbb Z}\) is the unique distribution fixed by the
dilated critical lattice. The continuous arithmetic boundary carrier is the
orbit of one rigid joint-fixed line through the moduli of critical
polarizations.

This makes the moving-lattice interpretation exact.

## 6. Hostile combs are retyped

Shifted and twisted combs are not additional fixed boundaries. They satisfy
character-valued covariance:

\[
 \tau_1\Lambda=\chi_\tau\Lambda,
 \qquad
 M_1\Lambda=\chi_M\Lambda,
\]

with at least one nontrivial character. They belong to different boundary
sectors.

Weighted periodic combs similarly fail one of the two fixed equations unless
all weights coincide.

Thus the hostile boundary census is sharply reduced:

\[
\boxed{
\text{the untwisted critical Heisenberg-fixed boundary is unique up to scale}.}
\]

## 7. The rigid relational pair

The two ends of the theta matrix coefficient now have independent uniqueness
properties:

\[
\begin{array}{c|c}
f&
\text{unique normalized minimal }D(D+1)\text{ Gaussian descendant}\\
\Delta_{\mathbb Z}&
\text{unique joint-fixed integral Heisenberg boundary distribution}.
\end{array}
\]

Their interaction under dilation is

\[
 \mathcal A(u)
 =\langle\Delta_{\mathbb Z},R_uf\rangle.
\]

The pair is therefore much more rigid than “two Fourier-fixed objects.”
Higher-Hermite states violate minimality; shifted or weighted combs violate
the joint-fixed boundary law.

## 8. Remaining question

This rigidity derives the completed theta source uniquely within the stated
relational class. It still does not prove that the analytic continuation of
its dilation cross-spectrum has no complex zeros.

The next positivity problem should retain the full Heisenberg orbit, not only
the scalar comb matrix coefficient. A natural target is the operator-valued
spectral kernel of the two conjugate Heisenberg generators along dilation,
whose vacuum compression is xi.

## 9. Scope

The joint-fixed uniqueness theorem, forced distributional typing, Fourier
covariance, and dilation of the critical Heisenberg lattice are exact. The
claimed uniqueness of the state refers only to the normalized minimal
Euler-invariant differential class already specified. No positive
operator-valued spectral lift, off-axis nonvanishing, or RH theorem is
claimed.
