# Cayley admission: fixed algebra versus transported presentation

Fresh source reference: `research/voevodsky/source-algebra-selection-boundary.md`.
Its eight-fiber pointwise closure has counting weights (1,1,1,1,1,2,2,7).
The sixteen underlying points are not deleted. This note tests the documented
coefficient algebra; it does not implement a native admission constructor.

## A concrete extension to the full pointwise closure

Let e_0,...,e_7 denote its eight primitive idempotents, in the owner's listed
order. Then B1=e_1-e_2 and B2=e_3-e_4. Extend the audited Cayley map by fixing
all other directions, including e_1+e_2 and e_3+e_4. With c=-7/25 and s=24/25,

\[
T(B_1)=cB_1-sB_2,\qquad T(B_2)=sB_1+cB_2.
\]

This invertible map fixes the global unit and B0 and preserves the full counting
norm. Nevertheless B1*B2=0 while T(B1)*T(B2) is nonzero. Thus even on the
complete eight-dimensional pointwise closure, unit and norm preservation do
not authorize the map as an automorphism of that unchanged algebra.

There is a general strengthening: any unital algebra automorphism of Q^8
permutes its primitive idempotents. A continuous real-parameter family of
such automorphisms, after the analogous real scalar extension, is constant.
With the given counting weights, permitted permutations must also preserve
weights. This statement concerns this fixed finite pointwise algebra, NOT
all possible native source objects or noncommutative enlargements.

## Transporting the product does work, but changes the question

Define a new product and a transported readout by

\[
x\star_T y=T\bigl(T^{-1}x*T^{-1}y\bigr),
\qquad r_T(x)=T^{-1}x.
\]

Then T is a unital algebra isomorphism from the original pointwise algebra to
the transported one. The new product is associative and commutative, and
r_T restores the old product and readings exactly. The checker verifies all
64 basis sewing equations and all 512 basis associativity equations; bilinearity
extends them to all vectors. Norm transport retains the documented weights.

This construction is a legitimate mathematical presentation change. It is not
an owner admission response, does not establish a native policy allowing that
change, and does not produce the four-dimensional noncommutative Clifford
algebra. Conjugating a commutative multiplication leaves it commutative.

## Infinitesimal distinction

For the completed angular family let K(B1)=-2B2, K(B2)=2B1 and let K vanish
on the fixed complementary directions. It is not a derivation of the original
pointwise product. Indeed a derivation D must satisfy

\[
D(e)=2eD(e)
\]

for each primitive idempotent e. Since 1-2e is invertible, D(e)=0, and these
idempotents span the algebra. The checker exhibits K(e_1) nonzero.

If products and readouts are transported with T(theta), their variation obeys

\[
\partial_\theta\mu_\theta(x,y)
=K\mu_\theta(x,y)-\mu_\theta(Kx,y)-\mu_\theta(x,Ky).
\]

The coordinate connection D_theta=partial_theta-K makes transported states
parallel: D_theta(T(theta)v)=0. Thus precisely the same coordinate motion can
be a pure presentation change when the measuring structure moves with it.
A generator alone does not distinguish that case from active evolution
relative to a fixed measuring structure.

## Result and next step

The existing handoff is narrowed to three explicit choices: preserve the
pointwise product (this map fails), transport product and readout (a mathematical
presentation exists), or supply a different admitted observable/implementer
structure. None has been chosen by a received owner authorization here.

Continue locally by testing the earlier Hamiltonian/action and phase lift
under a time-dependent moving frame. Check whether apparent dynamics can be
removed only at the cost of transporting the measuring structure, and retain
endpoint phase/clutching witnesses so a frame change does not erase a loop.
The owner-admission request remains pending independently.

Verification:

```text
python research/nima/checkers/check_cayley_product_transport.py
```

Receipt: `results/cayley-product-transport.json`. All claims of exact checking
are finite rational algebra checks; the general automorphism/derivation
arguments are given above and are not claimed as new Agda formalizations.
