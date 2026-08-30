# The odd Wronskian quarter-column exactly normalizes the ordered curvature return

## Source endpoint columns

The completed theta boundary supplies

\[
w_\theta
=
\begin{pmatrix}
\frac12\\[2pt]
\frac12
\end{pmatrix},
\qquad
j_\theta
=
\begin{pmatrix}
\frac14\\[2pt]
-\frac14
\end{pmatrix}.
\]

The endpoint metric compatible with a unit coefficient wall is \(2I\). In
this metric,

\[
\|w_\theta\|_{2I}^2=1,
\qquad
\|j_\theta\|_{2I}^2=\frac14.
\]

Thus the normalized odd endpoint vector is

\[
\widehat j_\theta
=
2j_\theta
=
\begin{pmatrix}
\frac12\\[2pt]
-\frac12
\end{pmatrix}.
\]

## Comparison with bilateral history

For unit source mass, the odd bilateral Volterra history has endpoint vector

\[
H_{\mathrm{jump}}
\leadsto
\begin{pmatrix}
-\frac12\\[2pt]
\frac12
\end{pmatrix}.
\]

Therefore

\[
\widehat j_\theta
=
-H_{\mathrm{jump}}
\]

at the endpoint port.

Since

\[
S_{\mathrm{ord}}
=
-2H_{\mathrm{jump}},
\]

one obtains

\[
\widehat j_\theta
=
\frac12S_{\mathrm{ord}},
\]

and hence the unnormalized source Wronskian column is

\[
j_\theta
=
\frac14S_{\mathrm{ord}}.
\]

This fixes both magnitude and sign from source traces.

## Curvature return

The ordered port resolves the connection curvature by

\[
S_{\mathrm{ord}}\Omega=4A.
\]

Consequently the actual quarter-column satisfies the exact identity

\[
j_\theta\Omega
=
\frac14S_{\mathrm{ord}}\Omega
=
A.
\]

The source Wronskian normalization cancels the factor four in the ordered
curvature return exactly.

For the Gaussian seed,

\[
j_\theta\Omega f_0
=
Af_0
=
-2\pi f_2.
\]

Thus the odd window-to-theta comparison lands on the first even dilation
current with no residual fitted scalar.

## Reciprocal orientation

The sign is not optional. Replacing \(j_\theta\) by \(-j_\theta\) gives

\[
j_\theta\Omega=-A
\]

and reverses the reciprocal sheet character while preserving all even wall
energies.

The ordered endpoint column therefore supplies the orientation bit that the
real endpoint Gram could not determine.

## Tail propagation

For the completed theta derivative-tail operator \(B=H_KD\),

\[
BS_{\mathrm{ord}}=-2H_K.
\]

Using \(S_{\mathrm{ord}}=4j_\theta\),

\[
Bj_\theta
=
-\frac12H_K.
\]

Hence the source quarter-column also fixes the magnitude of its bounded tail
propagation.

Together, the two exact identities are

\[
j_\theta\Omega=A,
\qquad
Bj_\theta=-\frac12H_K.
\]

They connect curvature, ordered orientation, dilation, and theta-tail history
in one normalization frame.

## Typing qualification

The equations use \(j_\theta\) as the operator represented by the
Wronskian odd endpoint column, not merely as a numerical two-vector. The
representation theorem must show that endpoint-column composition agrees
with the ordered-port operator on the common rapid zero-mode-reduced core.

The endpoint values and bilateral history prove the only possible
normalization; quadratic Green functoriality must still authorize the operator
identification.

## What is now closed

At the linear and endpoint level, both wall and odd scales are fixed:

\[
e_{\mathrm{wall}}
\mapsto
w_\theta,
\]

\[
e_{\mathrm{odd}}
\mapsto
j_\theta
=
\frac14S_{\mathrm{ord}}.
\]

No free \(\lambda\), \(\mu\), or phase remains in the two-column
Wronskian frame.

## Remaining local theorem

The earliest remaining gate is now purely quadratic:

> Prove that the source endpoint-column representation intertwines the
> Stieltjes window Green form with the theta-history graph form after wall
> and odd incidence are inserted.

If it does, the local Adams comparison cell acquires an authorized mixed form.
If it fails, the exact linear normalization still does not define the edge.
