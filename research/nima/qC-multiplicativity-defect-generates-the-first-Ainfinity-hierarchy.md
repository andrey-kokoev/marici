# The q-C multiplicativity defect generates an A-infinity hierarchy

Let

$$
f_1=W
$$

be the historical radial chart map. Its multiplicativity defect is

$$
\mu_2(a,b)
=
f_1(ab)-f_1(a)f_1(b).
$$

Adjoin a degree-one mapping-cylinder component

$$
h_2(a,b)
$$

with differential

$$
dh_2=\mu_2.
$$

This is the first A-infinity correction to the q-C comparison.

Associativity gives the identity

$$
f_1(a)\mu_2(b,c)
-
\mu_2(ab,c)
+
\mu_2(a,bc)
-
\mu_2(a,b)f_1(c)
=0.
$$

Expanding the four terms cancels every monomial. Hence the boundary prescribed for the next component is closed.

For each adjacent axis

$$
a\in\{H,V,D,L,O,R\},
$$

the transported cylinder component has comparison boundary

$$
dK_{qCa}
=
a(h_2)-h_2(a\text{-transported inputs}).
$$

Applying the differential again gives zero. These six components occupy the q-C-a cubes:

$$
K_{qCH},
\quad
K_{qCV},
\quad
K_{qCD},
\quad
K_{qCL},
\quad
K_{qCO},
\quad
K_{qCR}.
$$

The free dg correspondence therefore carries the q-C square and all six secondary fillers.

A native analytical realization requires continuous or closable representatives of

$$
h_2
$$

and

$$
K_{qCa}
$$

on the retained historical graph. Their graph estimates determine whether the universal A-infinity comparison descends from the free mapping-cylinder carrier.

The checker `check_qC_Ainfinity_defect_hierarchy.py` verifies the expanded associator cancellation and closure of all six secondary boundaries.
