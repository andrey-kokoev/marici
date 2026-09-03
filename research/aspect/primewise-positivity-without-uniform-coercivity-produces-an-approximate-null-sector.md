# Primewise positivity without uniform coercivity produces an approximate-null sector

## Question

Do zero-trace elimination and strict positivity in every prime sector suffice for scalar-null confinement on the completed direct sum?

## Hostile family

Let

\[
H=\bigoplus_{n\ge1}\mathbb R^2
\]

with endpoint recovery in sector \(n\)

\[
T_n(x_n,y_n)=x_n.
\]

The vertical auxiliary line is \(N_n=\{(0,y_n)\}\subseteq\ker T_n\), so elimination is exactly zero-trace and does not modify endpoint data.

Define the positive sector energy

\[
Q_n(x_n,y_n)=x_n^2+\frac1n y_n^2.
\]

Every sector is strictly positive and has trivial kernel. On the Hilbert direct sum,

\[
Q(x,y)=\sum_{n\ge1}\left(x_n^2+\frac1n y_n^2\right)
\]

also has trivial algebraic kernel.

## Approximate-null sequence

Let \(v_n\) be the unit vector supported on the vertical coordinate of sector \(n\). Then

\[
\|v_n\|=1,
\qquad
Q(v_n)=\frac1n\longrightarrow0.
\]

Hence there is no constant \(c>0\) with

\[
Q(v)\ge c\|v\|^2
\]

on the completed vertical sector. Zero belongs to the spectrum as an accumulation point even though zero is not an eigenvalue.

## What the hostile refutes

Primewise positivity plus zero-trace elimination does not imply a uniform spectral gap, stable inverse, or quantitative confinement on the completed prime sum. It does not refute the weaker algebraic statement that the kernel is trivial. Therefore any use of “scalar-null confinement” must choose between:

- algebraic null exclusion: \(\ker Q=0\);
- uniform confinement: \(Q\ge cI\) for one \(c>0\).

The first follows in this diagonal hostile; the second fails.

## Source consequence

A source-derived Fourier–Tate argument seeking uniform confinement must supply a prime-uniform lower bound after normalization and transport. Sectorwise positivity, equal formal expressions, and finite-cutoff minima do not provide it. If only algebraic null exclusion is intended, a spectral-gap claim must be withdrawn.

## Verification

`research/aspect/checkers/check_primewise_nonuniform_coercivity.py` verifies with exact rational arithmetic that every finite sector is positive while the cutoff coercivity minimum equals \(1/N\) and tends downward along the tested cutoffs.

## Disposition

The hostile survives and distinguishes two rival meanings of confinement. Existing local conditions are insufficient for uniform scalar-null confinement. The next decisive audit is whether the actual source normalization produces a prime-uniform lower bound or only sectorwise positivity.
