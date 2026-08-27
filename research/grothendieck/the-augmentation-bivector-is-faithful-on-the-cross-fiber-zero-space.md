# The augmentation bivector is faithful on the cross-fiber zero space

## Source-labelled augmentation geometry

At a finite cutoff, let `V_X` be the discrete label port for the retained
`p`-free valuation fibers. Give its source basis the declared Fock inner
product and let `Omega_X` be the Riesz vector of scalar augmentation:

\[
\epsilon_X(v)=\langle\Omega_X,v\rangle.
\]

For the standard orthonormal label basis,

\[
\Omega_X=(1,\ldots,1),
\qquad
\lVert\Omega_X\rVert^2=d_X,
\]

where `d_X` is the number of retained fibers.

Define the representation-valued exterior observer

\[
\mathcal E_X(v)=\Omega_X\wedge v.
\]

The Gram identity gives

\[
\lVert\mathcal E_X(v)\rVert^2
=\lVert\Omega_X\rVert^2\lVert v\rVert^2
-|\langle\Omega_X,v\rangle|^2.
\]

On the scalar-null pullback `epsilon_X(v)=0`,

\[
\lVert\Omega_X\wedge v\rVert^2
=d_X\lVert v\rVert^2.
\]

Thus the bivector observer is faithful on the entire cross-fiber
augmentation kernel.

## Apply it to the backward equalizer

Let the labelwise defect vector be

\[
\mathcal D_X
=(1+q)R_X-qA_X-q^2B_{2,X}.
\]

The labelwise source identity is

\[
\mathcal D_X=(1-q^2)F_X.
\]

Wedge with the augmentation vector:

\[
\Omega_X\wedge\mathcal D_X
=(1-q^2)\Omega_X\wedge F_X.
\]

If the completed scalar output vanishes, then

\[
\lVert\Omega_X\wedge\mathcal D_X\rVert^2
=|1-q^2|^2d_X\lVert F_X\rVert^2.
\]

This is the first faithful positive quadratic readout of the cross-fiber
cancellation space derived from the backward mate. It uses one
representation-valued bivector port rather than an impossible fixed family of
scalar observers.

## Geometric-algebra meaning

The scalar zero is the vanishing dot channel

\[
\Omega_X\mathbin{\cdot}F_X=0.
\]

The same state generally has a nonzero exterior channel

\[
\Omega_X\wedge F_X\ne0.
\]

The zero therefore does not mean that the relationship disappears. It means
the relationship has moved entirely from grade zero into grade two. The
bivector records the oriented cancellation that the scalar readout erased.

## Source-authority condition

The construction requires the discrete label metric and augmentation vector
to be independently source-authorized. They cannot be imported from the
analytic Gram quotient, where adjacent logarithmic labels become
asymptotically indistinguishable. Positive Fock/valuation typing supplies the
candidate discrete port; its compatibility with cutoff and Mellin transport
must be retained.

## Remaining RH gate

The exterior observer solves the finite cross-fiber faithfulness problem. It
does not yet orient the spectral parameter. The next theorem must derive a
Green or conservation identity in which the positive bivector energy appears
with coefficient proportional to the centered real part and the complete
typed boundary flux vanishes on an admissible zero-state.

That identity must hold before scalar compression and remain natural as
`X` grows. Without it, the bivector explains what survives a zero but not why
the zero must occur on the seam.

## Durable verification

- Checker: `checkers/check_augmentation_bivector_faithfulness.py`
- The checker verifies the exact Gram identity and faithful recovery on a
  three-fiber scalar-null witness.
