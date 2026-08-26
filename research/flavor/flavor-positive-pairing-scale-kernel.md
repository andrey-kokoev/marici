# Positive-pairing scale kernel (WP364)

## Bounded hostile test

WP363 showed that the Euclidean two-port metric fixes the scaled exchange to
\(s=1\). Does existence of a positive source-defined pairing suffice, or was
equal port norm doing the work?

Let the general symmetric Gram matrix be

\[
G=
\begin{pmatrix}
A&B\\
B&D
\end{pmatrix},
\qquad A>0,quad AD-B^2>0.
\]

For

\[
P_s=
\begin{pmatrix}
0&s\\
s^{-1}&0
\end{pmatrix},
\]

the isometry condition is

\[
P_s^TGP_s=G
\quad\Longleftrightarrow\quad
D=A s^2.
\]

The off-diagonal pairing \(B\) remains free subject to
\(|B|<As\). Hence every \(s>0\) admits a positive invariant Gram metric.
Positivity alone does not select unit normalization.

## Exact hostile metrics

At \(s=2\),

\[
G=\operatorname{diag}(1,4)
\]

is positive definite and exactly invariant. Even determinant normalization
does not help: for arbitrary \(s>0\),

\[
G_s=\operatorname{diag}(s^{-1},s)
\]

has determinant one and is invariant under \(P_s\).

Unit scale follows only after adding equal port norms, \(A=D\). Combined with
invariance, this gives \(s=1\). Equal norm is therefore the missing datum, not
positivity or volume normalization.

## Disposition

WP364 sharpens WP363: an arbitrary source-defined positive pairing does not
remove the scale kernel. It converts the scale into the norm ratio

\[
s=\sqrt{D/A}.
\]

This may be measured or derived, but it is not predicted by positivity. A
common multiplet with an independently derived equal-norm theorem would close
the normalization gate; choosing orthonormal coordinates after observing the
metric would only rigidify presentation.

The smallest exact falsifier is the invariant positive pair
\((P_2,\operatorname{diag}(1,4))\). The remaining physical gate is a
source-side constructor proving equal norms of the flavor and source ports in
one common representation, with a calibrated instrument realizing that
pairing.

Run `uv run --with sympy python
research/flavor/checkers/wp364_positive_pairing_scale_kernel.py` to regenerate
the exact result.
