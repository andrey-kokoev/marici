# Convolution powers reduce Weil localization to a strict-peak interpolant

Finite interpolation alone does not control the completed divisor tail. A
clean amplification mechanism is available if one strict-peak condition can
be established.

Let \(f\in C_c^\infty(\mathbb R)\) have Mellin transform \(\Phi\), and suppose
for a hypothetical off-seam pair \(\rho,\rho^\vee\) that

\[
\Phi(\rho)=1,
\qquad
\Phi(\rho^\vee)=-1.
\]

Assume additionally that every other divisor evaluation satisfies

\[
|\Phi(z)|\le q<1.
\]

For an odd integer \(n\), take the \(n\)-fold additive convolution

\[
f_n=f^{*n}.
\]

Then

\[
\widehat f_n(s)=\Phi(s)^n.
\]

The target reciprocal pair continues to contribute

\[
1^n\overline{(-1)^n}
+
(-1)^n\overline{1^n}
=
-2.
\]

Every other reciprocal contribution is bounded in magnitude by
\(2q^{2n}\). Since \(\Phi\) decays faster than every power on vertical lines
and the zero count grows polynomially, dominated convergence gives

\[
\sum_{z\ne\rho,\rho^\vee}
\Phi(z)^n\overline{\Phi(z^\vee)^n}
\longrightarrow0
\]

along odd \(n\to\infty\).

Hence

\[
Q_\Xi(f_n,f_n)\longrightarrow-2m_\rho
\]

up to the quartet and multiplicity convention. Positivity fails.

## What this closes

The support of \(f_n\) grows linearly with \(n\), but remains compact for
each finite \(n\). Thus convolution amplification stays inside the standard
explicit-formula test class. No uniform interpolation norm over all divisor
cutoffs is required.

The terminal localization problem reduces to:

> Can the authorized Mellin class construct one function whose transform has
> the disagreement values \(1,-1\) at a chosen reciprocal pair and has
> strictly smaller modulus at every other divisor point?

This is a strict-peak interpolation theorem.

## Remaining circularity in naive finite interpolation

Event 10290 does not by itself prove the strict peak. If one interpolates all
zeros below a chosen height \(T\), the resulting function has rapid decay,
but the height beyond which its transform is \(<1\) may exceed \(T\).
Rebuilding the interpolant at the larger cutoff changes that decay threshold.

Therefore the argument

\[
\text{finite interpolation}
+
\text{rapid decay}
\Rightarrow
\text{global peak}
\]

is not automatic. It needs either:

1. a quantitative interpolation bound closing this cutoff loop;
2. a source reproducing-kernel peak theorem;
3. or a classical Weil localization lemma already proved for the frozen test
   class.

## Categorical interpretation

Convolution power is the authorized Adams-like amplification of an
evaluation character:

\[
\Phi(z)\mapsto\Phi(z)^n.
\]

A strict spectral peak turns the local negative swap mode into a dominant
global mode, while all other evaluations contract.

This is exactly a power-method/Birman–Schwinger mechanism:

\[
\text{point separation}
\to
\text{strict peak}
\to
\text{convolution amplification}
\to
\text{global negative Weil vector}.
\]

The unresolved analytic gate is now narrower than arbitrary
completion-stable interpolation: prove one global strict peak for each
hypothetical off-seam reciprocal pair.
