# The fifteenth theta quarter-turn rotates the flagged pencil into a Krein port metric

## Status

Exact finite symmetrizer classification. Fix the ordered theta transmission
flag and its bordered pencil from the fourteenth turn. A constant Hermitian
metric can make that pencil selfadjoint in an indefinite geometry only under a
sharp carrier-commutant condition: the metric must map the endpoint actuator
to the theta-source sensor while commuting with the internal carrier.

The condition is source-local and can be falsified without inspecting
transmission zeros. Even when it holds, indefinite selfadjointness permits
nonreal conjugate pairs, so a further Krein-sign or definitizability law is
required.

## Fixed framed pencil

Let

\[
L(z)
=
\begin{pmatrix}
0&c^*\\
b&A-zI
\end{pmatrix},
\]

where \(A=A^*\), \(b=b_0\) is the ordered endpoint actuator, and \(c=b_f\)
is the ordered theta-source sensor vector.

Seek a constant invertible Hermitian metric \(J\) satisfying

\[
L(\lambda)^*J
=
JL(\lambda)
\]

for every real \(\lambda\).

## Spectral coefficient forces block diagonality

Write

\[
L(\lambda)=L_0-\lambda P,
\qquad
P=
\begin{pmatrix}
0&0\\
0&I
\end{pmatrix}.
\]

Comparing coefficients of \(\lambda\) gives

\[
PJ=JP.
\]

Therefore every admissible constant metric has the block form

\[
J
=
\begin{pmatrix}
\alpha&0\\
0&K
\end{pmatrix},
\]

where \(\alpha\in\mathbb R\setminus\{0\}\) and \(K=K^*\) is invertible.

No off-diagonal metric block can repair the port mismatch while preserving the
fixed spectral coefficient.

## Exact symmetrizer criterion

Comparing the constant blocks yields

\[
AK=KA
\]

and

\[
Kb=\alpha c.
\]

The adjoint equation

\[
b^*K=\alpha c^*
\]

then follows automatically.

Thus a constant Hermitian symmetrizer exists exactly when the commutant of the
carrier contains an invertible Hermitian operator that maps the endpoint port
to the source port, up to the real boundary scale \(\alpha\).

This is the precise control-theoretic version of source-derived port
collocation in an indefinite metric.

## Simple-spectrum finite test

Suppose \(A\) has simple eigenvalues and choose its orthonormal eigenbasis. Any
Hermitian \(K\) commuting with \(A\) is diagonal:

\[
K
=
\operatorname{diag}(k_1,\ldots,k_n),
\qquad
k_j\in\mathbb R\setminus\{0\}.
\]

Writing the port coordinates as \(b_j\) and \(c_j\), the symmetrizer equation
becomes

\[
k_jb_j=\alpha c_j
\]

for every \(j\).

Hence:

1. \(b_j=0\) exactly when \(c_j=0\);
2. every nonzero ratio \(c_j/b_j\) must be real;
3. the signs and magnitudes of those ratios determine the signature weights
   \(k_j\) up to the common real scale \(\alpha\).

A single spectral coordinate with a nonreal ratio, or a support mismatch,
falsifies every constant Hermitian port metric.

## Degenerate carrier eigenspaces

If \(A\) has degenerate eigenspaces, \(K\) may be any invertible Hermitian
operator within each eigenspace. The criterion remains finite and blockwise:
within every spectral block, an invertible Hermitian map must send the
projection of \(b\) to the corresponding projection of \(\alpha c\).

The source must select these block metrics. Existence of an arbitrary fitted
map inside a degenerate eigenspace does not provide metric authority.

## The fifteenth quarter-turn

The ordered port mismatch has become geometry:

\[
\left(A,b,c\right)
\longrightarrow
\left(J,L,J L\right).
\]

When the criterion holds, \(JL(\lambda)\) is Hermitian on the real axis. The
bordered transmission problem is then a selfadjoint pencil in the Krein or
Pontryagin metric defined by \(J\).

This preserves the correct transmission divisor. It does not identify or
forget the ordered ports.

## Why indefinite symmetry is insufficient

A matrix can be selfadjoint in an indefinite metric and still have nonreal
eigenvalues. The minimal example is

\[
H
=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
J
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

It satisfies

\[
H^*J=JH,
\]

but

\[
\operatorname{spec}(H)=\{i,-i\}.
\]

Therefore a modular port metric would explain conjugate symmetry of
transmission zeros, not confinement to the seam.

The missing second law must control the Krein type of every characteristic
state or prove definitizability with no open-sector exceptional spectrum.

## Source-derived candidate

Modular reflection is the only current source operation with the correct
variance to exchange the endpoint and theta-source perspectives. The finite
test is now exact:

1. compute its induced state-space operator \(K_X\);
2. verify \(K_X=K_X^*\) and invertibility;
3. verify \(A_XK_X=K_XA_X\);
4. verify \(K_Xb_{0,X}=\alpha_Xb_{f,X}\) with real nonzero \(\alpha_X\);
5. transport \(K_X\) through prime and prime-power extensions;
6. test whether the completed metric remains nondegenerate on the rigged
   domain.

No metric inferred from solving these equations after observing the zero
divisor counts as source-derived.

## Finite falsifiers

The framed Krein route fails if:

- the endpoint and source ports have different carrier spectral support;
- one simple-spectrum ratio \(c_j/b_j\) is nonreal;
- the only solutions \(K\) are singular;
- a solution exists but is not the action induced by modular reflection;
- prime transport fails to intertwine the metrics;
- or a source-compatible \(J\)-selfadjoint hostile pencil has an open-sector
  conjugate zero pair.

The two-by-two matrix \(H\) above is the minimal falsifier to any claim that
indefinite selfadjointness alone forces seam confinement.

## Decisive conclusion

The fifteenth rotation turns the ordered-port problem into a finite carrier-
commutant equation. This is the first repair that preserves both the actual
theta transmission divisor and a selfadjoint-type geometry. Its existence is
not yet established for the theta source, and its existence would still leave
a separate Krein-sign problem. The next move should compute the modularly
induced \(K_X\), not rotate the unframed Weyl system again.
