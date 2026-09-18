# Injective semidefinite energy is enough for pointwise Xi confinement

Let `R` be a bounded nonnegative operator. Then

$$
\langle Rv,v\rangle=\|R^{1/2}v\|^2.
$$

Hence

$$
\langle Rv,v\rangle=0
\quad\Longleftrightarrow\quad
v\in\ker R.
$$

If `R` is injective, every nonzero vector has strictly positive energy even when

$$
\inf_{\|v\|=1}\langle Rv,v\rangle=0.
$$

Therefore a uniform Green margin is not necessary for pointwise confinement of an already constructed Xi kernel state. It is enough that:

1. the completed residual form is nonnegative;
2. its kernel is zero on the source-generated Xi lift;
3. the arithmetic balance identity holds for that same state.

For a nonzero lifted state `x_z`, if

$$
2\operatorname{Re}z\,E_{\rm total}(x_z)=0
$$

and

$$
E_{\rm total}(x_z)>0,
$$

then

$$
\operatorname{Re}z=0.
$$

The completed odd endpoint residual is nonnegative and injective despite lacking coercivity, so it passes this pointwise positivity test. Uniform margins remain necessary for stable inversion, cutoff-uniform resolvents, and Riesz-bundle control, but not for the scalar confinement implication itself.

Status: coercivity requirement weakened to source-range injectivity for pointwise Xi confinement; arithmetic balance and nonnegativity of the full assembled residual remain open.
