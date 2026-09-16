# C31 is unitary reconstruction from the compatible canonical-dual pair

## Question

Does the reverse presentation map from the canonical-dual spectral pair to the source observer have an analytic realization?

## Claim boundary

Yes on the compatible image of the paired transform. This does not reconstruct an observer from the structural connection or scattering phase without its transformed observer vector.

Let \(H_S^{\mathrm{src}}\) be the declared semilocal source Hilbert carrier. The canonical and dual transforms are unitary maps

$$
\Omega_S^+:H_S^{\mathrm{src}}\longrightarrow H_S^+,
\qquad
\Omega_S^-:H_S^{\mathrm{src}}\longrightarrow H_S^-.
$$

Define the compatible spectral image

$$
\mathsf{Spec}_S^{\mathrm{obs}}
=
\left\{
(\xi^+,\xi^-):
(\Omega_S^+)^{-1}\xi^+
=
(\Omega_S^-)^{-1}\xi^-
\right\}.
$$

The forward constructor is

$$
C_{13}(g)=(\Omega_S^+g,\Omega_S^-g).
$$

The reverse constructor is

$$
C_{31}(\xi^+,\xi^-)
=(\Omega_S^+)^{-1}\xi^+
=(\Omega_S^-)^{-1}\xi^-.
$$

Therefore

$$
C_{31}C_{13}(g)=g,
$$

and for every compatible pair,

$$
C_{13}C_{31}(\xi^+,\xi^-)=(\xi^+,\xi^-).
$$

The equality of the two inverse formulas is the compatibility condition defining the paired image. Unitarity makes both inverses continuous.

## Disposition

Both \(C_{13}\) and \(C_{31}\) are analytic inverse constructors between the source Hilbert carrier and the compatible canonical-dual observer image. The reduced datum \((B_S,J_S,V_{\mathrm{loc},S})\) is not a substitute for the spectral observer pair and does not support this inverse.