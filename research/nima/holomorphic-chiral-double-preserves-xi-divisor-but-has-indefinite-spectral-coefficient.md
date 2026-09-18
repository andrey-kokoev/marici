# Holomorphic chiral double preserves the Xi divisor but has indefinite spectral coefficient

For a holomorphic pencil

$$
L(z)=L_0-zP,
$$

define its coefficient-adjoint reflection

$$
L^\sharp(z)=L_0^*-zP^*.
$$

This is holomorphic in `z` and satisfies

$$
L^\sharp(x)=L(x)^*
$$

for real `x`. Define the chiral double

$$
\mathcal Q(z)=
\begin{pmatrix}
0&L^\sharp(z)\\
L(z)&0
\end{pmatrix}.
$$

Then `Q(x)` is self-adjoint for every real `x`. Moreover,

$$
\ker L(z)\ne0
\Longrightarrow
\ker\mathcal Q(z)\ne0,
$$

and the second chiral sector records the reflected-adjoint divisor. At finite cutoff,

$$
\det\mathcal Q(z)
=(-1)^N\det L(z)\det L^\sharp(z).
$$

Thus the Xi divisor is retained, together with its reciprocal/conjugate partner, rather than replaced by a full Weyl determinant.

The spectral coefficient is

$$
\mathcal P=
\begin{pmatrix}0&P^*\\P&0\end{pmatrix}.
$$

On every nonzero singular-value channel of `P`, `Pcal` has one positive and one negative eigenvalue. Hence it is indefinite. Pairing a kernel equation with a vector gives a real numerator but an indefinite denominator, so no real-axis confinement follows.

This construction supplies an exact holomorphic, real-axis-self-adjoint, divisor-preserving dilation. It also isolates the remaining obstruction: replace or compress the chiral spectral coefficient by a source-derived positive active coefficient without changing the Xi kernel divisor.

Status: holomorphic divisor-preserving conservative double constructed; spectral coefficient positivity remains open and RH-bearing.
