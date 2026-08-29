# Coherent cross-prime rows are the sharp seam hostile after local contraction

## Factorized audit

Write the typed mixed block as

[
B_{p,q}=L_{Q,q}D_{p,q}L_{P,p}^{*},
qquad
D_{p,p}=M_{W_{2log p}-W_{log p}}.
]

The diagonal propagator obeys (|D_{p,p}|le1).  Thus a finite audit
should record

[
a_p=|L_{P,p}|,
qquad
b_p=|L_{Q,p}|,
qquad
d_{p,q}=|D_{p,q}|.
]

For the diagonal channel,

[
|K_{p,p}(sigma)|
le
rac12p^{-3/2-sigma}a_pb_p.
]

If

[
a_pb_ple Cp^	heta(log p)^m,
]

then absolute convergence through the seam follows for every fixed
(m) whenever (	heta<1/2).

## The sharp coherent-row hostile

Entrywise bounded cross-prime propagation is not enough.  Take
one-dimensional prime fibers, identity endpoint lifts, and

[
D_{p,q}=1
]

for every (p,q).  At the seam the weighted matrix is

[
K_{p,q}
=
rac12p^{-1/2}q^{-1}.
]

This is the rank-one formal operator

[
K=rac12,uotimes v,
qquad
u_p=p^{-1/2},
quad
v_q=q^{-1}.
]

Here (vinell^2(mathbb P)), but (u
otinell^2(mathbb P)), since

[
sum_prac1p=infty.
]

For any (x) with (langle v,xangle
e0), the output is a nonzero
multiple of (u) and therefore does not lie in the primitive Hilbert
space.  Every local block has norm one and every diagonal series
converges, yet the assembled seam operator is not Hilbert bounded.

This hostile isolates coherent cross-prime accumulation without local
growth.

## Three sufficient exits

### Prime-fiber intertwining

Let (P_p) and (Q_q) be the source prime-fiber projectors.  The
strongest exit is the typed law

[
Q_qBP_p=0
qquad(p
e q).
]

This must follow from an intertwining square between the Fourier--Bohr
valuation decomposition and the Green/Stokes endpoint lifts.  Scalar
orthogonality is not enough.

### Hilbert--Schmidt control

A sufficient off-diagonal criterion is

[
sum_{p,q}
p^{-1-2sigma}q^{-2}
a_p^2b_q^2d_{p,q}^2
<infty.
]

At the seam this directly prevents the coherent-row hostile.

### Weighted Schur control

More generally, find positive weights (r_p,s_q) and a constant (C)
such that

[
sup_prac1{r_p}
sum_q
rac12p^{-1/2-sigma}q^{-1}
a_pb_qd_{p,q}s_q
le C
]

and the transposed companion bound also holds.  This permits
non-diagonal propagation without requiring Hilbert--Schmidt decay.

## Next source theorem

Construct the endpoint lifts and prove whether they intertwine the
valuation projectors:

[
L_P^{*}P_p
quad	ext{and}quad
L_Q^{*}Q_q.
]

Then calculate the ordered mixed matrix, not merely its scalar Euler
shadow.  The first decision is binary:

1. the Green/Stokes constructor is prime-fiber diagonal; or
2. its off-diagonal kernel must carry a declared Schur,
   Hilbert--Schmidt, or rigged-form estimate.

The local propagator is solved.  The coherent rank-one hostile shows
that cross-prime assembly is now the first genuinely global analytic
gate.
