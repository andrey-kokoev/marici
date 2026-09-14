# One-sided Suzuki semigroup sewing requires an unbounded inverse boundary map

## Remaining proposal

For an off-axis pair

\[
\rho=\alpha+i\beta,
\qquad
\bar\rho=\alpha-i\beta,
\qquad \beta>0,
\]

bilateral translations act by

\[
V_a=
\operatorname{diag}(e^{-ia\rho},e^{-ia\bar\rho}),

a\in\mathbb R.
\]

This cannot be a bounded positive-Hilbert representation because its singular values are `e^{a beta}` and `e^{-a beta}`. The remaining idea is to keep only the decaying branch for `a>=0` and reconstruct its conjugate partner by boundary sewing.

## Positive stable branch

After removing the harmless unitary phase `e^{-ia alpha}`, the decaying branch is the scalar contraction semigroup

\[
T_a=e^{-a\beta},
\qquad a\ge0.
\]

This is a legitimate positive Hilbert-space evolution with generator `beta>=0`. Its adjoint is

\[
T_a^*=T_a=e^{-a\beta}.
\]

The conjugate off-axis character required by the arithmetic pair has modulus

\[
e^{a\beta}.
\]

It is therefore not the adjoint semigroup. It is the inverse:

\[
T_a^{-1}=e^{a\beta}.
\]

Thus reflection of the spectral point is not Hilbert adjunction of the stable evolution; it is time reversal.

## Bounded sewing is impossible

Suppose bounded boundary maps `J_in` and `J_out` sew the stable carrier into the growing character:

\[
J_{out}T_aJ_{in}=e^{a\beta}R
\qquad(a\ge0)
\]

for some nonzero finite-rank arithmetic channel `R`. Then

\[
e^{a\beta}\|R\|
\le
\|J_{out}\|\,\|T_a\|\,\|J_{in}\|
\le
\|J_{out}\|\,\|J_{in}\|.
\]

Letting `a` tend to infinity gives a contradiction. Hence

\[
\boxed{
\text{no bounded input/output sewing of a contraction semigroup can recover the growing conjugate branch.}
}
\]

This remains true for arbitrary contraction semigroups, not only the scalar model, because their matrix coefficients are uniformly bounded by the norms of the boundary vectors.

## The inverse-semigroup domain is the hidden indefinite boundary

The only formal reconstruction is

\[
\text{growing branch}=T_a^{-1}(\text{boundary datum}).
\]

For a general positive generator `A>=0`, `T_a=e^{-aA}` is bounded while

\[
T_a^{-1}=e^{aA}
\]

is unbounded whenever `A` is unbounded, and its norm grows exponentially even on a positive eigenvalue. A boundary map taking stable data into the domain of every `e^{aA}` must impose an analytic-vector topology much stronger than the carrier Hilbert norm.

Consequently the cross-pairing

\[
\langle T_av,T_a^{-1}w\rangle
\]

may remain algebraically constant, but it is not controlled by the positive Hilbert energy. It is exactly the original hyperbolic/Krein pairing in disguised coordinates.

## Unitary dilation does not help

Every contraction semigroup admits, under standard hypotheses, a unitary dilation or unitary model. Compressing the dilation gives bounded matrix coefficients:

\[
\langle T_av,w\rangle
=
\langle U_a\tilde v,\tilde w\rangle,
\qquad
|\langle U_a\tilde v,\tilde w\rangle|
\le\|\tilde v\|\,\|\tilde w\|.
\]

Therefore a unitary dilation cannot produce `e^{a beta}` through bounded boundary vectors either. The growing mode can only appear through a distributional or unbounded boundary functional. Positivity of the bulk dilation then supplies no bound on that readout.

## Relation to relative-trace transfer

A relative-trace or co-Poisson sewing could still use unbounded distributional boundary maps; trace formulas routinely do. But then its positive `L^2` isometry is insufficient. To prove the Weil inequality it must additionally establish a graph-norm estimate of the form

\[
\|e^{aA}Jf\|
\le C_a\|f\|_{src}
\]

with constants compatible with the full bilateral polarization. For an off-axis eigenvalue the constants necessarily grow as `e^{a beta}`. Uniform translation covariance is impossible unless the corresponding component vanishes.

Thus the precise missing theorem in any relative-trace specialization is not merely Poisson sewing or `L^2` isometry. It is boundedness of the inverse-time boundary readout in the source norm.

## Finite-window loophole

On a bounded interval `0<=a<=L`, the inverse branch has norm at most `e^{L beta}`. A bounded sewing can therefore exist with a constant depending exponentially on `L`. This supports local finite-window estimates but cannot pass to the global Weil criterion unless one proves uniform control as `L -> infinity`. Such uniformity again forces `beta=0` or annihilation of the component.

This explains why compact-window and finite-width positivity can coexist with the global obstruction.

## Disposition

The one-sided-semigroup aperture does not provide a bounded global Hilbert factorization:

\[
\boxed{
\text{conjugate sewing requires }T_a^{-1},
\text{ and }T_a^{-1}\text{ is exponentially unbounded off axis.}
}
\]

A successful source construction must therefore do more than sew stable branches: it must prove a uniform graph-norm estimate that eliminates every exponentially growing divisor mode. That estimate is again spectral confinement, not a formal consequence of semigroup positivity.
