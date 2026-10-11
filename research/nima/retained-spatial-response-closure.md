# Spatial response under the existing six-port Hamiltonians

## Question and frozen scope

Can the current carrier, record and cross-term spatial first moments, together
with their pulse responses, serve as a closed mechanical reading of the same
retained interaction? SCC obligation: readout descent with inherited symplectic
structure. Pulse area is the declared parameter; no physical duration is inferred.

Conjecture to test: these spatial readings and their first derivatives form a
closed linear quadratic-observable packet under every bound port, with the
carrier readings usable as ordinary commuting configuration coordinates.

Rivals: omitted imaginary coherences already distinguish the first response;
higher derivatives require further retained observables; the endpoint intensity
chart is not a canonical configuration chart even though its coordinates look
spatial. The all-port natural-mechanics candidate is H_e=T(p)+V_e(x), with the
same kinetic law and fixed x,p for every port. Momentum-dependent interactions
or a revised spatial reader are outside that candidate, not declared impossible.

Tests: exact derivative and second-derivative operator identities; all 68 actual
branch midpoint responses; conjugation hostile on the declared complex state
domain; closure ranks of the quadratic-observable span; Poisson brackets of the
candidate positions; comparison of their first responses across ports.

## Exact response law

Write G for the existing 22-coordinate metric, E_e for a bound exchange and
P_e=(I-E_e)/2. The existing interpolation is U_e(alpha)=exp(-i alpha P_e).
For any retained Hermitian readout B, differentiating that SAME operation gives

    L_e(B)=i(P_e^dagger B-B P_e),
    d(z^dagger B z)/d alpha=z^dagger L_e(B) z.

The second derivative is L_e squared. Since P_e squared=P_e, L_e cubed=-L_e:
a fixed port has a closed oscillatory response. This is a statement about the
specified pulse parameter, not a frequency in physical seconds.

The conserved anchor a=y+F r stays on the complex line f_AB*c for this
preparation. Thus an exact invariant linear carrier uses eta=(c,r) in C^7,
with z=T eta=(f_AB*c-F r,r). T is injective; its pulled-back metric M=T^dagger G T
is positive. Every port intertwines through T, and the actual 68 midpoint
states span this seven-dimensional linear space. This does not make an
arbitrary linear combination another prepared native history.

With Omega(v,w)=2 Im(v^dagger M w), the existing generator has Hamiltonian
h_e=eta^dagger M P_e eta. The response above agrees with its Poisson bracket.
The common phase quantity has zero derivative at every port.

## Actual branch response and the cross term

For each of the same 68 complete labelled plans, differentiate its own final
pulse at alpha=pi/2. This does not insert arbitrary extra edges into a path.

| Quantity | Number of paths |
|---|---:|
| Nonzero carrier spatial-moment response |62|
| Nonzero cross-term response |60|
| Exact carrier+record+cross response balance |68|

The whole first moment has zero first and second response as an operator
identity. The separate sectors need not recoil oppositely: in the first
lexicographic nonzero example their first responses are EQUAL, while the
cross-term response is minus twice either. The retained relation supplies
an essential part of the balance.

On the declared complex state domain, eta and its complex conjugate have the
same carrier, record and cross-term first moments and the same phase quantity,
but opposite nonzero response to the SAME port. One member is an actual
forward midpoint. The conjugate is obtained from the same real prefix by
inverse half-pulse transport; it is not claimed to be a second member of the
68 forward midpoint census. Common rephasing, in contrast, changes neither
the readings nor their derivatives.

## All-port linear response closure

Starting with the spatial moment forms and the conserved phase quantity,
repeatedly adjoin every L_e image and compute the exact real linear span:

| Maximum response order | Independent Hermitian forms |
|---|---:|
|0|6|
|1|13|
|2|35|
|3|49|
|4|49|

The first-response packet is not linearly closed. Mixed port derivatives
reveal directions not present in the closed single-port oscillation.
Closure is the full Hermitian-form space on C^7. Equivalently, retain the
raw coherence matrix C=eta eta^dagger; it obeys the existing law

    dC/d alpha=-i(P_e C-C P_e^dagger).

Then every spatial response is a trace pairing with C. This packet is
common-phase neutral and preserves the original quadratic budget. It is not
a Born probability assignment. Its 49 linear observable directions are NOT
49 independent state degrees of freedom; pure C has rank one. This minimal
linear-span result does not exclude a smaller nonlinear parametrization.

## Why a mass matrix does not repair the current position reading

For B,C Hermitian, the inherited bracket is represented by

    {f_B,f_C}=i eta^dagger(C M^-1 B-B M^-1 C) eta.

The three carrier first-moment forms have nonzero pairwise brackets, of
matrix ranks 6,2,4. Their values are nonzero on respectively 59,60,54 of the
actual 68 midpoints. Fixing the prepared anchor c=1 and using the inherited
six-coordinate affine symplectic structure gives the same ranks and census,
so allowing an extra anchor variation is not responsible. These readings
therefore cannot simply be adopted as ordinary commuting configuration
coordinates in either tested description. An arbitrary constant mass choice
does not change that obstruction.

There is a second failure of the frozen natural-mechanics candidate:
H_e=T(p)+V_e(x) with common canonical x,p and common kinetic law would make
x-dot independent of e at a fixed state. These proposed x readings instead
have different response operators for different ports. Neither finding
excludes a different source-derived spatial reading, internal degrees of
freedom, or momentum-dependent interactions. The test does not classify all
possible mechanics.

A nonorthogonal state-coordinate rescaling transports the metric, response
forms and Poisson brackets exactly, so the reported failures are not repaired
by ignoring the kinetic metric in another chart.

## Disposition and verification

The frozen closed-first-response/canonical-position conjecture is falsified.
Retain the positive all-port response law and full coherence closure; do not
rename the conserved first moment momentum or fit separate inertial masses.
The physical momentum/inertia identification remains open for a different
justified readout. No new force or physical clock is installed.

Run:

    uv run --with sympy python research/nima/checkers/check_retained_spatial_response_closure.py
    uv run --with sympy python research/aspect/scc/scc.py check nima-retained-spatial-response-closure

455 exact checks pass in the fresh standalone run. SCC also executes the
checker successfully; its classification is exit-code orchestration, not
independent scientific certification. The receipt
is `results/retained-spatial-response-closure.json`.

The runner admitted the SymPy-only invocation but not the combined SymPy/NumPy
invocation. This checker therefore uses count-checked, source-hashed AST
extraction of the original rational exchange constructor, moment forms and
history evaluators. It freshly executes the actual branch construction and
checks all required algebra. It does NOT rerun the old NumPy comparison to
the full 137-port model, the preceding phase census, or any formal proof root.
