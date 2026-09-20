# Higher-coherence topology iteration 01: energy-bounded pro-Hilbert totalization is conservative on the Haar residual

## Candidate topology

Model repeated simplex--prism--cone completion by an inverse system of finite
coherence packets

\[
\cdots\longrightarrow C_{N+1}\xrightarrow{\pi_{N+1,N}}C_N
\longrightarrow\cdots\longrightarrow C_1,
\]

where each `C_N` carries a positive graph energy `E_N` and every bonding map is
energy-contracting. Use the energy-bounded projective limit

\[
C_{\rm pro}^{E}
=
\left\{(x_N):\pi_{N+1,N}x_{N+1}=x_N,
\ \sup_NE_N(x_N)<\infty\right\}.
\]

This excludes phantom compatible families. In the diagonal sequence model it
is exactly a weighted `ell^2` space rather than the unrestricted product.

## Higher fillers

Let `omega_N` be the finite residual and suppose a higher cone provides
`H_(N+1)` with

\[
dH_{N+1}=\omega_N.
\]

Compatibility requires

\[
\pi_{N+1,N}\omega_{N+1}=\omega_N.
\]

A pro-residual is zero only when every finite projection is zero:

\[
(\omega_N)_N=0
\quad\Longleftrightarrow\quad
\omega_N=0\text{ for every }N.
\]

Thus this topology can retain an infinite coherent primitive, but it cannot
turn a nonzero finite residual into zero merely by moving it to higher degree.

## Relative-Haar readout

At any finite packet containing prime `p`, the terminal Hermitian observation
is

\[
r_{p,N}(z)
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)E_{p,N}(b_{z,N}).
\]

Assume the readouts commute with restriction. They define a continuous
pro-observer

\[
r_p:C_{\rm pro}^{E}\to\mathbb R
\]

because it is already detected at the first packet containing `p`. If
`E_(p,N)(b_(z,N))>0`, then

\[
r_{p,N}(z)=0
\quad\Longleftrightarrow\quad
\operatorname{Re}z=0.
\]

No later cone coordinate can change this value without violating projection
compatibility or changing the finite readout itself.

## Exactness versus observation

A higher filler may make `omega_N` exact in the total complex. But the positive
Haar observer is not a cohomology functional unless one independently proves

\[
r_p(dH)=0.
\]

If this is imposed, exactness forces the already existing finite scalar to
vanish and is therefore RH-strength. If it is not imposed, higher exactness has
no confinement consequence.

## Verdict for topology 1

The energy-bounded pro-Hilbert topology is analytically sound and useful for:

- excluding phantom inverse-limit states;
- retaining all finite simplex/prism/cone packets;
- supporting regulator-relative positive completion;
- avoiding an unjustified ordinary Hilbert limit.

It does **not** absorb the relative-Haar incoherence. Finite projections are
jointly faithful, so the primewise residual survives unchanged. Any tower that
kills it must either:

1. alter a finite bonding/readout map;
2. quotient by a subspace visible to the Haar observer;
3. introduce a new sourced homotopy on which the Haar observer vanishes.

Each option is additional mathematical input, not a consequence of the
pro-Hilbert topology.

## Iteration disposition

Topology 1 is retained as the safe completion topology but rejected as an
automatic RH unlock. The next nonredundant topology to test is an inductive or
bornological cone completion, where a finite residual might escape to infinity
rather than remain visible under every projection.