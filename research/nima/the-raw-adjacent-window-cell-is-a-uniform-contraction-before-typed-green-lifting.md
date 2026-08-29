# The raw adjacent-window cell is a uniform contraction before typed Green lifting

## Claim

Let

[
W_t(q)=H(q+t)-H(q-t),
qquad 0le Hle 1,
]

with (H) monotone decreasing.  For (L=log p), the raw adjacent
primitive-to-square cell is

[
alpha_{p,1}(q)=W_{2L}(q)-W_L(q).
]

It obeys the prime-independent pointwise estimate

[
|alpha_{p,1}(q)|le 1.
]

Consequently its multiplication representation satisfies

[
|M_{alpha_{p,1}}|_{L^2	o L^2}le 1
]

for every prime (p).

## Proof

Because (H) is decreasing,

[
W_t(q)=H(q+t)-H(q-t)in[-1,0].
]

More specifically, (-W_t(q)) is the mass of the positive density
(-H') on the interval ([q-t,q+t]).  The interval for (t=L) is
contained in the interval for (t=2L).  Hence

[
-1le W_{2L}(q)le W_L(q)le0,
]

and therefore

[
-1le W_{2L}(q)-W_L(q)le0.
]

Taking the essential supremum proves the operator bound.

## Prime-diagonal consequence

With the frozen primitive and square coefficients

[
p^{-1/2-sigma-it},
qquad
rac12p^{-1-2it},
]

the raw prime-diagonal mixed term is bounded by

[
rac12sum_p p^{-3/2-sigma}.
]

This converges uniformly for (sigmage0).  Thus the raw adjacent
window creates no seam divergence and needs no Laplace displacement for
prime-diagonal summability.

This is stronger than the history-graph estimate.  The history norm can
grow like (O(sqrt{log p})) because it controls the entire path and
its derivative, while the endpoint difference is a uniformly bounded
annular mass.

## What remains unresolved

This does not yet construct the typed Green/Stokes arrow.  The required
mixed operator has the form

[
eta_p
=
L_{Q,p},M_{alpha_{p,1}},L_{P,p}^{*},
]

where the primitive and square endpoint lifts must be independently
derived from the source riggings.  Their norms, radicals, domains, and
orientation can change the estimate.

The next theorem should therefore prove source-authorized bounds for
the lifts, for example

[
|L_{Q,p}|,|L_{P,p}^{*}|le C_arepsilon p^	heta
]

on each compact off-seam region, with an exponent (	heta<1/2) being
already sufficient for prime-diagonal absolute convergence.  Better,
one should calculate the exact endpoint trace constants from the
relative Green identity.

The separation is now exact:

1. raw geometric cell: uniformly contractive;
2. history graph: path norm may grow with (log p);
3. typed Green lift: still to be constructed and bounded;
4. cross-prime assembly: still requires compositional control.

Any remaining local-to-global failure cannot be blamed on the raw
adjacent-window multiplier.  It must enter through typed endpoint
lifting, cross-prime interactions, radical descent, or domain closure.
