# Incidence Projection No-Go and Pre-Quotient Correspondence Gate

## Result

Entry 352 makes the target of (q^!) type-correct, but the tempting
incidence-graph projection from the two-route (D03) diamond does not define
the required central-flip correspondence.

The source contains the pre-quotient generic and lower generators

[
dq_J=x_3r_J,
]

while the ringed target contains the radial pair

[
dn_D=(X_D/u_D)p_D.
]

For an incidence-only degree-zero pairing, put

[
k=langle q_J,p_Dangle,qquad
a=langle r_J,n_Dangle.
]

The ringed chain-map condition is

[
x_3a mathbin{pm} (X_D/u_D)k=0.
]

Reducing modulo the conductor (x_3=0) proves that (k=pm1) is
impossible. More generally, (x_3mid k), and the least monomial solution
is

[
k=x_3,qquad a=mp X_D/u_D.
]

Thus the incidence relation supplies only an orientation shadow. It cannot
be promoted to the primitive generic projection needed by the
central-flip span. Inverting (x_3) is not a repair: it removes the
conductor support on which the extraordinary map must be nonzero.

## Consequence for a category-of-elements span

Let (Z_{m inc}) be the category of elements of the visible relation
between the source diamond and the target state poset. Its two forgetful
order maps exist as maps of finite spaces. Equipping a point with the target
localization ring also makes the target projection ringed.

This still does not construct the required span. A ringed source projection
must intertwine the source differential (x_3) with the target radial
coefficient (X_D/u_D). The equation above shows that the unit incidence
map fails that condition. Pulling back the target module along the
forgetful relation merely repackages the target coefficient diagram; it
does not supply the missing mixed-variance source map.

## Exact replacement for the projection block

A viable correspondence must be constructed before taking endpoint or
generic quotients. It must retain, in one ringed object:

1. the Morse top (H), the generic term (q_J), and lower term (r_J);
2. the principal ideal line ((x_3)) without inverting (x_3);
3. both occurrence and repeated-normal Tor grades;
4. every target Cech lower and overlap term;
5. the shifted Cartier/Gysin arrow on the conductor; and
6. a Beck--Chevalley homotopy whose generic and special restrictions are
   induced by the same correspondence.

Accordingly the former single obligation `d_central_flip_projections`
splits into:

- `d_central_flip_prequotient_correspondence`: construct the full
  ideal-valued ringed/log object (Z);
- `d_central_flip_projection_beck_chevalley`: prove compatibility of its
  generic localization and special extraordinary restrictions; and
- `d_central_flip_projections_assembled`: only then record the actual
  morphisms (p,q) with the hypotheses needed for (q^!) and pushforward.

The labelled double-Rees relative cap of entry 176 remains necessary local
input, but its universal closure has extra special-fibre components and
does not itself choose this pre-quotient correspondence.

## Scope

This is a sharp no-go for the naive incidence projection, not a global
nonexistence theorem. It leaves open an ideal-valued DNC/nearby-cycle
correspondence with all lower terms and its shifted extraordinary
Beck--Chevalley cell.

Evidence is the exact coefficient theorem and checker of entry 177,
`research/voevodsky/check_d03_generic_incidence_pairing_obstruction.rs`,
together with entries 120, 160, 174, 176, 348, and 352. Delegated runs
run-3557dcd4cb374e1186c3ae43038c06e5,
run-365bae6be8c84b38817e53dad63c35a6, and
run-5b6a82a7b0e14bc08f878a4ac28ca783 all failed without results and are
not used as evidence.
