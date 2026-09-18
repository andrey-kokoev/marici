# Reciprocal Wiener–Hopf sewing factors the two-height boundary through Xi-square

Let

$$
R(z)=\int_0^\infty e^{-zt}A_\Phi(t)\,dt
$$

in its initial half-plane, continued by the completed source prescription. Since `Phi` is real and even, its autocorrelation is even:

$$
A_\Phi(-t)=A_\Phi(t).
$$

The bilateral transform identity gives

$$
\Xi(z)^2
=\int_{\mathbb R}A_\Phi(t)e^{zt}\,dt
=R(z)+R(-z).
$$

Thus reciprocal causal orientations satisfy the exact Wiener–Hopf sewing law

$$
\boxed{R(z)+R(-z)=\Xi(z)^2.}
$$

For the positive orientation,

$$
\langle\Phi,G_z^+\rangle=-R(z).
$$

For the reciprocal orientation, with the reflected stable prescription,

$$
\langle\Phi,G_z^-\rangle=-R(-z).
$$

Hence their sewn forcing contribution is

$$
\langle\Phi,G_z^+\rangle+
\langle\Phi,G_z^-\rangle
=-\Xi(z)^2.
$$

After polarization in both spectral variables, the complete doubled forcing boundary is

$$
\boxed{
\mathcal F_{\rm dbl}(w,z)
=-\Xi(z)^2-\overline{\Xi(w)^2}
}
$$

in the Hermitian lane, up to the fixed global sign convention for the tail equation. In the analytic-transpose lane, replace conjugation by the declared transpose pairing.

Therefore

$$
\mathcal F_{\rm dbl}(w,z)=0
$$

whenever

$$
\Xi(z)=\Xi(w)=0.
$$

This is source-derived, two-height, and established before diagonal specialization. It is not an imposed equal-energy condition: it follows from completed theta autocorrelation, causal splitting, and reciprocal reflection.

To turn it into seam confinement, one must verify that the doubled endpoint-plus-difference Green boundary used by the Rosenbrock state is exactly this sewn forcing boundary, with the two orientation signs and endpoint traces unchanged. The one-sided Green identities already provide the local comparison; the remaining check is typed reciprocal port bookkeeping.

Status: scalar reciprocal two-height boundary factorization through Xi-square proved; typed six-port identification remains to be checked.
