# Stopped Dirichlet label fibers assemble every prime sewing without false poles

Status: exact finite-fiber passivity architecture; Clark descent remains open

Put

\[
 s=\frac12+iz,
 \qquad
 \chi_z(n)=n^{-s}.                                    \tag{1}
\]

At the faithful quotient coordinate `v>=0`, define the finite label fiber

\[
 \mathcal F_v=\ell^2\{n\in\mathbb N:n\le e^v\}       \tag{2}
\]

and its arithmetic character vector

\[
 k_v(z)=\sum_{n\le e^v}\chi_z(n)e_n.                 \tag{3}
\]

The stopped Dirichlet packet is only its scalar all-label readout:

\[
 D_v(z)=\langle\mathbf1_v,k_v(z)\rangle.              \tag{4}
\]

Keeping (3) rather than only (4) preserves the label incidence that scalar
prime recursions obscure.

## Exact prime decomposition

For a prime `p`, split the fiber orthogonally into primitive and divisible
labels:

\[
 \mathcal F_v
 =\mathcal F_v^{p\nmid}\oplus
 U_p\mathcal F_{v-\log p},                            \tag{5}
\]

where the second summand is absent for `v<log p` and

\[
 U_pe_m=e_{pm}                                        \tag{6}
\]

is an isometry onto the divisible-label subspace.  Unique factorization gives

\[
 \boxed{
 k_v(z)=k_v^{p\nmid}(z)
 \oplus\chi_z(p)U_pk_{v-\log p}(z).
 }                                                     \tag{7}
\]

Taking the scalar readout recovers

\[
 D_v(z)=D_v^{p\nmid}(z)+\chi_z(p)D_{v-\log p}(z),     \tag{8}
\]

the local stopped-packet form of Nima's prime recursion.

## Positive fiber energy

Because (5) is orthogonal,

\[
 \boxed{
 \|k_v(z)\|^2
 =\|k_v^{p\nmid}(z)\|^2
 +|\chi_z(p)|^2\|k_{v-\log p}(z)\|^2.
 }                                                     \tag{9}
\]

For `z=x+iy`,

\[
 |\chi_z(p)|=p^{y-1/2}<1
 \quad\text{exactly when }y<1/2.                     \tag{10}
\]

Thus (7) is a passive state recursion throughout the unresolved half-strip:
the primitive labels are the innovation channel, `U_p` is lossless label
transport, and `chi_z(p)` supplies strict contraction.

This energy identity exists before any Fourier cancellation.  It is absent
after projection to (4), because different labels then interfere in one
scalar.

## Fold repair is the number-operator commutator

On each fiber let

\[
 \mathsf N e_n=(\log n)e_n.                           \tag{11}
\]

Then

\[
 \boxed{
 \mathsf N U_p-U_p\mathsf N=(\log p)U_p.
 }                                                     \tag{12}
\]

This is the finite-fiber version of the fold commutator.  Applying it to
`k_{v-log p}` produces exactly the positive prime-shift repair
`log(p) chi_z(p)` in the differentiated packet recursion.

Hence the contraction and repair are two faces of the same typed operator:

\[
 \partial_y\chi_z(p)=\log(p)\chi_z(p),
 \qquad
 [\mathsf N,U_p]=\log(p)U_p.                          \tag{13}
\]

## Why the false arithmetic singularities disappear

Solving the scalar recursion by division introduces

\[
 (1-\chi_z(p))^{-1},                                  \tag{14}
\]

whose apparent poles lie at

\[
 z=\frac{2\pi k}{\log p}+\frac i2.                   \tag{15}
\]

These are not source singularities.  In the finite fiber (7), no division
occurs: the primitive and divisible components coexist as orthogonal
coordinates.  The compact sewing current over `0<=u<log p` is exactly the
incidence correction for the absent shifted fiber when `v<log p`.

Thus entirety is structural at the label-fiber level and looks like a
delicate cancellation only after scalar projection.

## Compatibility over all primes

The partial isometries commute on their admitted domains,

\[
 U_pU_q=U_qU_p=U_{pq},                                \tag{16}
\]

and the number-operator cocycle satisfies

\[
 [\mathsf N,U_{pq}]=\log(pq)U_{pq}.                   \tag{17}
\]

Therefore the fibers (2) are the common refinement of every prime recursion.
No prime-by-prime choice of sewing current is needed; all compatibility is
already encoded by integer-label incidence.

## Remaining descent gate

The positive identity (9) is not yet RH.  The physical Clark quantity is a
particular scalar polarization involving the primitive theta weight
`phi_1(v)`, the fold operator, bilateral modular reflection, and the all-label
readout (4).  A finite-to-one label fiber is not a scalar fiber.

The exact remaining theorem is to construct a contractive observation map

\[
 \mathcal O_z:
 \int_0^\infty{}^\oplus
 \phi_1(v)\mathcal F_v\,dv
 \longrightarrow\mathbb C^2                         \tag{18}
\]

whose two outputs are `E(z)` and `E^*(z)` and whose defect identity descends
(9), together with (12), to

\[
 |E(z)|^2-|E^*(z)|^2>0.                               \tag{19}
\]

Proving contractivity of an invented scalar sum is insufficient.  The map
must reproduce the exact theta integral and its finite sewing cells.  The
sharp falsifier is a negative direction in the observation-map defect after
the full labelled fiber has been retained.
