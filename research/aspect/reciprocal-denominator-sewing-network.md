# Reciprocal denominator-sewing network

Owner: `marici.Aspect`

## Bounded question

Can one passive reciprocal finite optical network exhibit all of the following
without conflation: a zero-free driving-point denominator, a dark Cayley
numerator, exact boundary-mode elimination, mixed Schur first-jet increments,
and order-independent telescoping under two mode additions?

This packet supplies that finite coherence witness.  It implements the optical
test requested in
`research/nima/theta-sector-denominator-sewing-would-confine-completion-zeros-by-hurwitz.md`
and
`research/nima/theta-determinant-frame-increment-is-the-schur-complement-first-jet.md`.
It supplies no theta/Tate source authority.

## Source authority and typed ports

The retained modes are three calibrated reciprocal resonator or waveguide
ports in one energy-normalized frame.  Let

`M_+(z)=M_0+z I`, `A_+(z)=I+M_+(z)`.

The static matrix is source-constructed as

`M_0=Q diag(1/2,1/4,1/5) Q^T`,

where

`Q=[[3/5,-4/13,48/65],[4/5,3/13,-36/65],[0,12/13,5/13]]`.

The checker verifies `Q^T Q=I` exactly.  Hence `M_0` is positive definite and
symmetric.  For `Re z>0`, the Hermitian part of `M_+(z)` is positive definite,
so `A_+(z)` is invertible and

`D_+(z)=det A_+(z)`

is zero-free in the open right half-plane.

## Denominator versus selected Cayley numerator

The selected determinant readouts are

`D_+(z)=det(I+M_+(z))`,
`N_+(z)=det(M_+(z)-I)`.

Because `M_0` has eigenvalue `1/2`, `N_+(1/2)=0`.  At the same point every
eigenvalue of `I+M_+(1/2)` is positive, so `D_+(1/2)` is nonzero.  The dark
Cayley numerator therefore does not threaten the positive-real denominator.

These are global determinant channels, not individual matrix entries.  An
experimental realization needs coherent multiport tomography or determinant
reconstruction; one analyzer scalar is insufficient.

## Boundary-mode elimination

For a retained index set `X` and one added mode `b`, partition

`A_Y(z)=[[A_X(z),B(z)],[C(z),E(z)]]`.

The boundary-mode Schur complement is

`S_(Y/X)=E-C A_X^-1 B`.

At exact sample `z=1/3`, the checker verifies separately for both possible
mode-addition orders that

`det A_Y=det A_X det S_(Y/X)`.

This is algebraic boundary-mode elimination.  It is not a physical lossless
multiport dilation: the eliminated mode is integrated out, not retained as a
measured complementary output.

## First-jet bonding law and mixed terms

All jets are evaluated at the source-fixed basepoint `z=0`.  Since the
couplings are static but the retained block varies,

`S'=E' + C A_X^-1 A_X' A_X^-1 B`.

The second term is nonzero in this witness.  Dropping it gives a deliberate
failure.  With it retained, the checker proves

`(D_Y'/D_Y-D_X'/D_X)(0)=S'(0)/S(0)`

for each scalar boundary addition.

Starting from mode 0, add modes in orders `(1,2)` and `(2,1)`.  The individual
increments depend on the order, because the intermediate retained block is
different.  Their sums agree exactly with the full-minus-base logarithmic
jet.  Thus the determinant line telescopes while remembering constructor
order locally.

## Reciprocal sector double

Define the reflected sector by

`M_-(z)=M_0-zI`, `D_-(z)=D_+(-z)`.

It is accretive and zero-free in the open left half-plane.  The finite sewn
scalar `F(z)=D_+(z)D_-(z)` is even.  This determinant sewing is an analytic
sector product.  It is not a unitary scattering dilation and does not by
itself specify environmental power routing, quantum noise, or a laboratory
input-output matrix.

## Detector kernel and smallest hostile

The smallest hostile to denominator/numerator conflation is the eigenmode of
`M_0` with eigenvalue `1/2` at `z=1/2`: `M_+-I` kills it while `I+M_+` acts on
it by multiplication by `2`.  The smallest hostile to diagonal-only bonding
is any first addition in this network: the exact mixed Schur derivative is
nonzero, so using only `E'` gives the wrong increment.

## Conserved and dissipated quantities

Symmetry certifies reciprocity in the common port frame.  Accretivity supplies
the denominator invertibility certificate.  Neither condition asserts total
optical power conservation.  A physical passive realization may require
explicit bath ports; those must be measured or dilated before claiming
unitarity.

## Completion gate

The packet proves a three-mode finite bonding identity only.  It does not
establish locally uniform convergence as mode count grows, a cutoff-uniform
inverse bound, a nonvanishing limiting basepoint, equality to a completed
theta section, or identification of the Schur first jet with a primitive
arithmetic current.  Those are precisely the remaining continuum and source
gates.

Run `python research/aspect/checkers/reciprocal_denominator_sewing_network.py`.
The result is
`research/aspect/results/reciprocal_denominator_sewing_network.json`.
