# The minimal even border recovers Xi but is completely eliminable

## Canonical linearization

Let

\[
G=
\begin{pmatrix}
a&b\\
b&a
\end{pmatrix}
\]

be the reciprocal wall--jump return, and let

\[
w=
\begin{pmatrix}1\\0\end{pmatrix}
\]

be the normalized even wall covector in this frame. Then

\[
w^*Gw=a.
\]

The minimal bordered matrix is

\[
D_{\mathrm{even}}
=
\begin{pmatrix}
I_2&Gw\\
w^*&0
\end{pmatrix}.
\]

Its determinant is

\[
\det D_{\mathrm{even}}
=
-w^*Gw
=
-a.
\]

Thus, in the conventional normalization,

\[
det D_{\mathrm{even}}
=
-\frac12\Xi.
\]

This is the smallest exact determinant that linearizes the even reciprocal matrix coefficient without introducing a fitted scalar entry.

## Canonical kernel vector

At \(a=0\),

\[
D_{\mathrm{even}}
\begin{pmatrix}
-Gw\\
1
\end{pmatrix}
=
0.
\]

So every scalar completed zero produces a finite bordered kernel state.

The construction is source-forward in the limited sense that \(G\) and the even wall covector are already derived before the determinant is taken.

## Exact elimination

Define

\[
L=
\begin{pmatrix}
I_2&0\\
-w^*&1
\end{pmatrix},
\qquad
R=
\begin{pmatrix}
I_2&-Gw\\
0&1
\end{pmatrix}.
\]

Both are invertible, with inverses obtained by reversing their off-diagonal signs. Direct multiplication gives

\[
LD_{\mathrm{even}}R
=
\begin{pmatrix}
I_2&0\\
0&-a
\end{pmatrix}.
\]

No inverse of \(a\) is used.

Therefore

\[
D_{\mathrm{even}}
\simeq
I_2\oplus(-a)
\]

by bounded finite-dimensional triangular equivalences.

## No typed obstruction at this level

All blocks act on the fixed finite wall--jump boundary carrier:

- \(G\) is a bounded \(2\times2\) analytic return;
- \(w^*\) is the bounded even coordinate projection;
- \(Gw\) is a bounded column on compact parameter sets;
- the triangular maps preserve the finite boundary space.

Hence the completion and unbounded-trace failures that can obstruct Gaussian elimination in an infinite rigged system do not occur here.

The minimal even border is therefore stably just the scalar section. Its kernel vector is a presentation of \(a=0\), not an independently constrained Green state.

## Consequence

The bordered repair resolves the algebraic determinant mismatch found for rigid sewing, but it does not provide an RH explanation.

It establishes only

\[
\Xi(z)=0
\quad\Longleftrightarrow\quad
\ker D_{\mathrm{even}}(z)\ne0.
\]

This equivalence is tautological under admitted finite elimination. It does not imply:

- that the kernel state lies in the completed history domain;
- that it satisfies a maximal isotropic boundary condition;
- that its Green flux vanishes;
- that off-seam positivity excludes it;
- or that the determinant is the top exterior readout of a common source operator.

## Why the top-exterior route is different

For a source-derived operator \(T_X\),

\[
\det T_X=0
\]

means \(T_X\) itself is singular before scalar bordering. Its top exterior state vanishes because a genuine source direction is lost.

For \(D_{\mathrm{even}}\), singularity is installed by adjoining the scalar matrix coefficient as a Schur complement. The identity block remains contractible and the only cohomology is multiplication by \(a\).

Thus:

- even border: scalar zero represented as a kernel;
- top exterior determinant: operator singularity observed as a scalar zero.

Only the second direction can support the desired spectral-identification theorem without additional typed obstruction.

## Remaining legitimate routes

After the rigid-sewing no-go and the border elimination, two serious architectures remain.

### Complete common operator

Construct the full finite-cutoff theta/Tate operator \(T_X(z)\), retaining prime, seam, endpoint, Gaussian, and archimedean ports, and prove

\[
\det T_X(z)
\to
v(z)\Xi(z)
\]

in the relative determinant line.

### Nontrivial arithmetic boundary pencil

Construct a source-derived boundary relation \(\Theta(z)-G(z)\) distinct from the rigid reciprocal identification, with domain typing that prevents reduction to the scalar even coefficient. Its determinant must be derived from arithmetic assembly rather than selected to equal \(\Xi\).

A larger bordered complex is useful only if its triangular elimination fails for a specific source-domain reason. Merely adding more finite auxiliary coordinates cannot help.

## Immediate audit target

The next source extraction should inspect the adelic and archimedean attachments for an operator acting before scalar Mellin evaluation.

The decisive questions are:

1. What is the common finite-cutoff carrier \(V_X\)?
2. Which source operation defines \(T_X\)?
3. Does the even wall coefficient arise as \(\det T_X\), or only as a matrix coefficient?
4. Which anomaly lines convert finite determinants into the completed relative determinant?
5. Is any proposed auxiliary border noneliminable in the declared topology?

Until these are answered, the exact statement remains:

> Xi is the even matrix coefficient of the reciprocal outer return, but not yet the spectral determinant of a source-derived operator.

## Minimal hostile

For any analytic scalar \(f(z)\), the same construction

\[
\begin{pmatrix}
I&u(z)\\
y&0
\end{pmatrix},
\qquad
yu=f,
\]

manufactures a kernel exactly at the zeros of \(f\). Finite triangular elimination always reduces it to \(I\oplus(-f)\).

Therefore the existence of the even border alone cannot distinguish the Riemann section from an arbitrary analytic target.
