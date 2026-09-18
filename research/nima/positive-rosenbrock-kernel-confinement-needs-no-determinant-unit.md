# Positive Rosenbrock kernel confinement needs no determinant unit

Let

$$
L(z)=L_0-zP
$$

and suppose a bounded strictly positive invertible `J` satisfies

$$
L_0^*J=JL_0,
\qquad
P^*J=JP,
$$

with the quadratic form `JP` nonnegative. Assume also the transversality condition

$$
\ker L(z)\cap\ker P=\{0\}
$$

for every `z`.

If `L(z)v=0` for nonzero `v`, then

$$
\langle JL_0v,v\rangle
-z\langle JPv,v\rangle=0.
$$

The numerator is real. Nonnegativity and transversality give

$$
\langle JPv,v\rangle>0.
$$

Therefore

$$
z=\frac{\langle JL_0v,v\rangle}
        {\langle JPv,v\rangle}
\in\mathbb R.
$$

For the bordered theta pencil, `P` vanishes only on the scalar reference coordinate. A vector in `ker P` has form `(c,0)`, and

$$
L(z)(c,0)=(0,c b_0).
$$

Since the source port `b_0` is nonzero, such a vector lies in the kernel only when `c=0`. Hence transversality is automatic.

The source-derived Xi Rosenbrock theorem already gives

$$
\ker\mathcal R_\Xi(z)\ne0
\quad\Longleftrightarrow\quad
\tau(z)=\Xi_{\rm centered}(z)=0,
$$

with matching root-chain multiplicity. Consequently a positive symmetrizer of this same pencil would confine Xi zeros directly. No separate determinant unit is required for zero-set confinement.

A relative determinant unit remains relevant only when replacing the exact Rosenbrock kernel characteristic by another determinant presentation.

Status: determinant-unit gate removed from direct Rosenbrock confinement; positive source-derived symmetrizer remains the sole RH-bearing gate.
