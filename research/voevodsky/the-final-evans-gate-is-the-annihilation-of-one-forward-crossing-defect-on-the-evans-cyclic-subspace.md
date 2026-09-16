# The final Evans gate is annihilation of one forward-crossing defect on the Evans cyclic subspace

## Question

Once the constructed pair-to-bordered crossing is fixed and contragredient return is unique, what is the weakest exact operator statement needed for Evans membership? Is full equality of forward G4 maps necessary?

## Claim boundary

Full forward-map equality is sufficient but stronger than necessary. If the authoritative G4 forward map is exposed, the Evans residual is the transpose of its defect from the constructed crossing, evaluated on the Evans jet subspace. The exact gate is annihilation of that subspace. If the Evans subspace is total in the bordered dual, this reduces to full map equality; otherwise it is a genuine restricted comparison.

## Two forward maps

Let

$$
T_{\rm PB}:P\to B
$$

be the constructed pair-to-bordered crossing, and let

$$
U_{\rm G4}:P\to B
$$

be the authoritative forward arithmetic/radial incidence once exposed on the same source and target pairings.

Define the forward crossing defect

$$
\boxed{\Delta=U_{\rm G4}-T_{\rm PB}.}
$$

Its contragredient defect is uniquely

$$
\Delta^\top
=U_{\rm G4}^\top-T_{\rm PB}^\top.
$$

## Evans cyclic subspace

Let \(\mathcal E_{\rm Ev}\subset B^\vee\) be the closed span, in the declared dual/graph topology, of all unchanged Evans shell traces and their parameter jets:

$$
\mathcal E_{\rm Ev}
=
\overline{\operatorname{span}}
\left\{
\operatorname{Tr}_{p,q}
\partial_z^ju(\cdot;z_0):
\begin{array}{l}
p<q\text{ consecutive},\\
\tau(z_0)=0,\\
0\le j<m(z_0)
\end{array}
\right\}.
$$

Include the limiting common mode when required by the arithmetic source topology.

## Residual as defect pairing

The radial Stokes identity proves that the constructed return \(T_{\rm PB}^\top\) cancels the ordinary-plus-endpoint shell section. Therefore the residual left by the authoritative G4 return is exactly

$$
r_U
=\Delta^\top e
$$

for the corresponding Evans trace \(e\).

Consequently the complete shell-jet family vanishes exactly when

$$
\boxed{
\Delta^\top|_{\mathcal E_{\rm Ev}}=0.
}
$$

Equivalently,

$$
\langle e,\Delta x\rangle_B=0
$$

for every \(e\in\mathcal E_{\rm Ev}\) and every pair source \(x\in P\).

## Full equality versus restricted equality

Full source identification

$$
U_{\rm G4}=T_{\rm PB}
$$

sets \(\Delta=0\) and is sufficient.

It is necessary only if \(\mathcal E_{\rm Ev}\) is total for the relevant target range. If

$$
\mathcal E_{\rm Ev}^\perp=\{0\},
$$

then \(\Delta^\top\mathcal E_{\rm Ev}=0\) implies \(\Delta=0\). If the annihilator is nonzero, G4 may differ from the constructed crossing in directions invisible to all Evans jets without affecting chain promotion.

## Exact owner choices

The owner can close the gate by either:

1. **global identification:** expose \(U_{\rm G4}\) and prove \(\Delta=0\);
2. **Evans-restricted identification:** prove \(\operatorname{ran}\Delta\subseteq\mathcal E_{\rm Ev}^\perp\);
3. **totality plus restricted test:** prove \(\mathcal E_{\rm Ev}\) total and verify defect annihilation on its generating shell jets.

The second route is the weakest theorem actually needed by the unchanged Evans complex.

## Why the current contract cannot decide it

Version 5 declares no authoritative \(U_{\rm G4}\). Thus \(\Delta\) is not yet a defined operator in the materialized contract. Neither its full vanishing nor its restriction to \(\mathcal E_{\rm Ev}\) can be evaluated.

## Disposition

The final RH-bearing placement problem has an exact defect formulation. Once the G4 forward map is exposed, no further architecture is needed: compute \(\Delta=U_{\rm G4}-T_{\rm PB}\) and test whether \(\Delta^\top\) annihilates the Evans cyclic jet subspace. Full forward equality is a sufficient optional strengthening.