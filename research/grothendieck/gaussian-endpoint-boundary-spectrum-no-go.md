# The Gaussian endpoint boundary has the wrong spectral growth

Epistemic-graph event: 1407.

## The direct self-adjoint realization

Let \`V\` be a finite-dimensional Hermitian space and let \`U\` be a unitary
operator on \`V\`. On \`H=L^2([0,L],V)\` consider

\`D=-i d/dy\`

with domain consisting of \`H^1\` sections satisfying \`f(L)=U f(0)\`.
The boundary form is

\`<Df,g>-<f,Dg>=-i(<f(L),g(L)>-<f(0),g(0)>)\`.

Unitarity of \`U\` makes it vanish, and the standard maximality argument for
first-order endpoint conditions makes this domain self-adjoint.

For the paired coefficient--Betti plane of Ledger 1374, take

\`U=K/sqrt(2)=(1+J)/sqrt(2)=exp(pi J/4)\`.

Thus the integral norm-two correspondence defines an explicit self-adjoint
boundary law after its archimedean normalization.

## Exact spectrum

Write the eigenvalues of \`U\` as \`exp(i theta_j)\`, with multiplicity, for
\`j=1,...,r\`. An eigensection is \`f(y)=exp(i lambda y)v_j\`, so

\`lambda_(j,n)=(2 pi n+theta_j)/L\`, for \`n in Z\`.

For one real symplectic mode, complexification gives phases \`+pi/4\` and
\`-pi/4\`. The Gaussian boundary therefore produces two shifted arithmetic
progressions. In general,

\`N_D(T)=r L T/(2 pi)+O(1)\`.

This remains true for every finite-rank, energy-independent endpoint unitary:
changing the unitary changes only finitely many offsets, not the Weyl order.

## Determinant obstruction

Up to a nowhere-zero exponential normalization, the characteristic
determinant is

\`Delta_U(z)=det(exp(i z L) I-U)\`.

Equivalently it is a finite product of shifted sine factors. It is an entire
function of finite exponential type, and its zeros have linear density.

By contrast, the nontrivial zeros of the completed Riemann function satisfy

\`N_xi(T)=T/(2 pi) log(T/(2 pi))-T/(2 pi)+O(log T)\`.

The leading \`T log T\` term is incompatible with every finite-dimensional
endpoint unitary. Therefore no determinant obtained from this direct Gaussian
endpoint realization can equal completed \`xi\`, even up to a nowhere-zero
exponential factor.

## What survives

The hostile test does not remove the Gaussian correspondence from the
program. Its phases \`+/- pi/4\` still supply the metaplectic eighth-phase
corner correction identified in Ledgers 1371--1374. What fails is the claim
that this finite boundary, by itself, supplies the full spectral system.

Any surviving construction must add an infinite-dimensional or
energy-dependent boundary component. The source-derived intrinsic-prime
operator is the only established candidate capable of carrying the missing
prime fluctuations, but coupling it to the Gaussian corner without importing
analytic continuation remains open.

## Scope

This is an exact spectral no-go theorem for the direct finite-rank,
energy-independent endpoint realization. It does not falsify \`K\` as an
integral corner factor, construct a physical relative-chain pushforward, or
exclude infinite-rank and energy-dependent boundary laws.
