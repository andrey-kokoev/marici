# The paired half-rotation is an integral Gaussian norm-two correspondence

Epistemic-graph event: 1404.

## Gaussian structure from paired polarization

On the integral symplectic double of a regular coefficient--Betti fiber,
Ledger 1372 constructs the canonical polarization exchange `J` with

`J^2=-1`.

Thus the lattice is canonically a module over `Z[i]`, with `i` acting as `J`.
Define the integral endomorphism

`K=1+J`.

It satisfies

`K^2=2J`.

For the positive metric `g(v,w)=omega(v,Jw)`, one has `J_dagger=-J` and

`K_dagger K=(1-J)(1+J)=2`.

Hence `K` is a norm-two isogeny.  In each symplectic mode its matrix is

`[[1,-1],[1,1]]`,

with determinant `2`, Smith form `(1,2)`, and cokernel `Z/2`.

## Half-rotation without an inserted square root

After real extension,

`K/sqrt(2)=(1+J)/sqrt(2)=exp(pi J/4)`.

Therefore the conditional metaplectic half-rotation of Ledger 1372 is the
unitary normalization of a primitive integral correspondence already defined
by paired addition and polarization exchange.  The square root appears only
when converting the norm-two isogeny into a unitary operator.

Equivalently, `1+J` is multiplication by the Gaussian prime `1+i`, and

`(1+i)^2=2i`.

The intrinsic bad prime `2` is exactly the ramified norm of the half-rotation
correspondence.  Up to Gaussian units and conjugation, this is the primitive
norm-two factorization.  The positive coefficient-to-Betti orientation
selects `1+J` rather than `1-J`.

## Consequence for the boundary gate

The half-rotation endpoint is no longer an arbitrary analytic interpolation:
it is an integral degree-two correspondence derived from the perfect paired
fiber.  This supplies a noncircular algebraic candidate for the dual-cutoff
corner and explains why its normalization carries an eighth phase.

What remains unproved is decisive:

- no physical relative-chain map realizes `K`;
- the source calculus has not proved that its cutoff boundary is the graph of
  this correspondence;
- normalization by `sqrt(2)` is archimedean;
- no self-adjoint operator domain or determinant has been constructed; and
- no fluctuating prime trace follows from `K` alone.

## Scope

This is an exact integral correspondence theorem.  It is not yet the desired
Hilbert--Polya boundary operator.
