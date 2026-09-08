# Branch A: completed fixed-road q2 test

Date: 2026-09-06.
Repository input: `andrey-kokoev/marici`.
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Result and qualification

The direct continuation of the previously certified q0 carrier to q2 exists as a sequence of actual face incidences. Keeping its F03 road, its x3-marked road flag, its road-prefix coefficient readout, and generic normalization g=1 does **not** give a diagonal polynomial coefficient comparison. Its obstruction is the nonzero class of x1 in R/(x5).

This completes a finite test of the proposed construction. It does not compute the full physical support-relative Beck–Chevalley obstruction. The earlier conversation asserted that this full obstruction reduced to the remaining scalar endpoint equation. That assertion was not justified: the q0 source audit explicitly leaves the spatial reciprocal-standard to original-Borel–Moore Tor comparison unconstructed. A carrier interval and its coefficient identity are not that comparison.

A separate computation of the displayed ordinary local Q collar gives an explicit nullhomotopy of the map e3 -> p03. Thus a nonzero coefficient on the unmarked target generator is not, by itself, a nonzero derived generic attachment.

## 1. Geometry and fixed inputs

Use hexagon vertices 0 through 5, with short diagonals

\[
x_i=\{i,i+2\}\quad(\bmod 6),\qquad D03=\{0,3\}.
\]

In words: xi denotes a labelled short diagonal in the face geometry. The corresponding independent occurrence variable has the same name when it occurs as a coefficient. D03 denotes the long diagonal; its occurrence coefficient is X03.

The relevant faces are

\[
\begin{aligned}
v_+&=\{x_1,x_3,x_5\},&
e_3&=\{x_1,x_5\},\\
q_0&=\{x_5\},&q_2&=\{x_1\},\\
Z_3&=\{D03,x_3\},&v_{10}&=\{D03,x_1,x_3\},\\
e_c&=\{x_1,x_3\}.&&
\end{aligned}
\]

In words: the q0 and q2 endpoints are Boolean facets, not vertices of the road square.

The independent enumeration gives 45 noncrossing faces, with counts (1,9,21,14), and 215 loaded face/mark generators. The F03 square has four vertices, four edges, and eight saturated vertex–edge–facet flags.

F03 does not meet q0: D03 crosses x5. F03 meets q2 in the edge labelled {D03,x1}, with two vertices. At v+ there are two q2-containing edges, {x1,x3} and {x1,x5}. The prescribed terminal x5 mark selects e3. The prescribed central flip and the x3 road mark select Z3 and v10.

Consequently the proposed q2 continuation is

\[
F_{03}\supset Z_3\supset v_{10}
\subset e_c\supset v_+\subset e_3\subset q_2.
\]

In words: start on the F03 road, follow its x3-marked flag, cross the existing central flip to v+, and end through e3 at q2. The containment symbols refer to geometric faces; their sets of diagonal labels have reverse inclusion. This is a zigzag, not a composite of ordinary exit arrows in one direction.

It differs from the earlier q0 route only in its terminal facet.

## 2. Coefficients derived from the road flag

Work over

\[
R=\mathbb Z[X_{03},x_0,x_1,x_3,x_4,x_5],
\]

with additional independent spectator coefficients allowed.

Give a face the product of its occurrence labels. For a saturated face-label inclusion, the occurrence multiplier is the target product divided by the source product; this is exact monomial divisibility, not localization of the ring.

On the selected flag, after omitting the common X03 factor, the labels are

\[
1,\quad x_3,\quad x_1x_3.
\]

In words: the two consecutive multipliers are x3 and x1. Their signed composite is positive in the inherited q0 orientation.

The prescribed first-normal evaluation therefore yields

\[
b_0^{\mathrm{flag}}=x_1,\qquad
b_2^{\mathrm{flag}}=x_1.
\]

In words: under the *same road-prefix readout* used by the q0 audit, the common prefix gives x1 for either terminal continuation. The superscript is essential: these are flag-model coefficients, not independently constructed physical costalk generizations.

The source endpoint differential is

\[
d e_3=-x_1q_0+x_5q_2.
\]

In words: the two deletions have different occurrence factors. Principal-line evaluation gives the candidate endpoint coefficients minus one and plus one. The latter does not change the fixed road prefix into an x5-labelled flag.

## 3. Complete diagonal coefficient test

The necessary equations for a diagonal comparison are

\[
gb_0=-x_1a_0,\qquad gb_2=x_5a_2.
\]

In words: the generic coefficient and the endpoint coefficients must commute with both boundary components.

For g=1, b0=b2=x1, and the principal endpoint candidates a0=-1, a2=1, their defects are

\[
(0,x_1-x_5).
\]

In words: the first component passes; the second does not.

Allowing an arbitrary polynomial a2 cannot repair the second equation:

\[
x_1=x_5a_2
\]

has no solution in R, since reduction modulo x5 gives the nonzero polynomial x1. The coefficient obstruction is

\[
[x_1]\in R/(x_5),\qquad [x_1]\ne0.
\]

In words: changing a2 changes the discrepancy by a multiple of x5, while its residue modulo x5 remains nonzero. Reversing a frame can change signs, but not this divisibility failure.

Without fixing g, the complete solution family is

\[
(g,a_0,a_2)=(x_5h,-x_5h,x_1h),\qquad h\in R.
\]

In words: every diagonal polynomial solution loses the prescribed unit generic coefficient.

Proof: the first equation and cancellation of the non-zero-divisor x1 give a0=-g. The second gives gx1=x5a2. Since x1 and x5 are independent prime variables, x5 divides g; write g=x5h. Cancellation of x5 gives a2=x1h. Conversely, substitution verifies both equations. This proves the all-polynomial claim without extrapolating a bounded calculation.

Prematurely setting x1=x5=0 makes the equations zero, but destroys the divisibility information. Inverting x5 allows a2=x1/x5, but is excluded in this polynomial source and removes the corresponding Cartier locus.

### Why a reflection does not complete the fixed-road construction

The hexagon reflection

\[
s(i)=2-i\pmod6
\]

fixes v+, x3, and e3, and exchanges x1 with x5. It also sends

\[
s(D03)=D25.
\]

In words: the endpoint-exchanging symmetry transports the road to F25. The reflected q0 flag has road coefficient x5, as expected, but it is a flag on F25, not F03.

The checker enumerates all twelve hexagon dihedral relabellings. None preserves F03 while exchanging q0 and q2. This also follows without enumeration: one endpoint facet is disjoint from F03 and the other intersects it, and relabellings preserve incidence.

The result does not contradict a cone-roof or exact-couple transgression. Such a comparison can use more than the fixed road flag. It establishes that the missing physical q2 map cannot be supplied by this literal continuation or by invoking fixed-road symmetry.

## 4. Keep the full endpoint Koszul hull

The unaugmented free complex is

\[
P_2=Re_3\xrightarrow{(-x_1,x_5)^T}
P_1=Rq_0\oplus Rq_2\xrightarrow{(x_5,x_1)}P_0=Ra.
\]

In words: it retains both endpoint branches and the augmentation cell. Its degree-zero homology is R/(x1,x5); its positive homology vanishes. Adding the final quotient gives its exact augmented resolution.

The equality d squared equals zero follows from commutativity. Exactness in degree one is the regular-pair syzygy: the kernel of (x5,x1) is generated by (-x1,x5). The q0 term alone has nonzero second boundary -x1*x5*a.

This packet repairs Boolean closure. It does not by itself identify either Boolean endpoint with a spatial Tor costalk, nor does it force a global generic generator to factor through this packet.

## 5. Ordinary local-collar mapping calculation

Use the one-road collar row actually stated in source entry 174, retaining the target-only localization rule. Enlarge R by an independent variable U03, writing X=X03 and U=U03. Define

\[
C_3=Rk\oplus Rn,
\qquad C_2=R[U^{-1}]p,
\qquad d_C(k)=\frac XU p,\quad d_C(n)=p.
\]

In words: neither upper generator has arbitrary inverse-U coefficients. Only the lower target summand is localized. The calculation is in ordinary complexes with these exact terms and degrees, not an asserted model of the full filtered support-relative category.

The map

\[
f(e_3)=p,\qquad f(q_0)=f(q_2)=f(a)=0
\]

is closed. But define a degree-plus-one homotopy by

\[
H(e_3)=n,\qquad H(q_0)=H(q_2)=H(a)=0.
\]

Then

\[
d_CH+Hd_P=f.
\]

In words: the purported unit attachment is null-homotopic in the ordinary mapping complex. The homotopy uses a retained generator and no prohibited inverse. The same conclusion holds for the map e3 -> (X/U)p, using k instead of n.

This is not a claim that the entire localized collar is acyclic. Its upper kernel is generated primitively by Uk-Xn. Its lower cokernel is

\[
R[U^{-1}]\big/\bigl(R+(X/U)R\bigr).
\]

In words: higher target Laurent terms can survive; one must not replace all terms by a common localized ring and contract them.

Because P is bounded and free, its ordinary derived maps into this collar are computed by the actual Hom complex. Every degree-zero chain map is specified by the coefficient f of p in the image of e3. Degree-plus-one homotopies can change f by a regular n term, an (X/U)k term, and arbitrary localized x1 or x5 multiples from the two endpoint generators. Therefore

\[
\operatorname{Hom}_{D(R)}(P,C)
\cong
\frac{R[U^{-1}]}{R+(X/U)R+(x_1,x_5)R[U^{-1}]}.
\]

In words: this is the complete ordinary mapping-class group for the displayed endpoint packet and local collar.

For example,

\[
[U^{-1}]\ne0,
\qquad U[U^{-1}]=X[U^{-1}]=x_1[U^{-1}]=x_5[U^{-1}]=0.
\]

In words: a genuine nonzero ordinary class exists, but this particular class is supported on all four zero loci. To certify nonvanishing, set X=x1=x5=0 and retain the negative Laurent part in U. This annihilates the whole denominator submodule but not U inverse. This class is not declared to be the physical generic Q attachment.

## 6. What has and has not been decided

The completed calculation rules out the direct fixed-F03 marked-flag completion with a diagonal polynomial map and generic coefficient one. It also rules out using the coefficient of the ordinary collar generator p03 as evidence for a nonzero derived attachment.

It does not rule out a source-derived support-relative correspondence with different spatial comparison maps. That correspondence must construct the endpoint Tor maps and their common generic-Q comparison. Neither a declared target boundary nor exclusion of the explicit homotopy H merely to obtain a nonzero answer constitutes such a construction.

In particular, this note does not promote the scalar discrepancy to the universal physical obstruction from source entry 160. That obstruction requires independently defined boundary pairings and localization comparison maps in a common category. The missing q0 Tor map is already explicitly identified in the source audit, so physical vanishing was not established before this q2 calculation.

## Verification

Run:

```sh
python check_branch_a_q2_completion.py --output branch_a_q2_completion_certificate.json
```

The standalone Python checker passed **954 exact assertions**. It enumerates all hexagon faces, checks actual weighted incidence squares, constructs both marked routes, verifies their flag products and endpoint equations, enumerates all dihedral relabellings, checks the complete solution-family identities, and verifies the ordinary-collar nullhomotopy on every source basis generator. The ideal and mapping-class conclusions are proved above for all polynomial degrees; finite checks are not used as substitutes for those proofs.

No proof-assistant verification is claimed. No repository files were changed.

## Sources

All repository sources are pinned to the commit above.

1. `research/voevodsky/check_d03_q0_endpoint_exit_flags.rs`, blob `528fca153efcf4720f24016ee285cabaabe75d4e`: inherited q0 marks, actual incidence coefficients, and qualification of the carrier calculation.
2. `research/voevodsky/check_d03_q0_endpoint_relative_tor_lift.rs`, blob `f5b13df4421187c70e97b8625a2f1a76d2e12502`: the remaining spatial Tor-map gap and the distinction between the flag and a full extraordinary kernel.
3. `src/ledger/20260814-116 Saturated D03 Exit Carrier and the Missing Thom-Decorated Road Lift.md`, blob `ff5c6bc04a1c4507a18e1326e42d30691ab70b13`: cone-roof carrier transgression, occurrence boundary, and external normal-line requirement.
4. `src/ledger/20260814-117 D03 Thom Endpoint Koszul Hull and the Missing Road Generizations.md`: full endpoint hull and the necessary two scalar comparison equations.
5. `src/ledger/20260815-174 Two-Edge Bivariant Trace and the Unlocalized Two-Flip Alignment Gate.md`, blob `ae5d4fc93fa135e7dc0ee6088928f9b8f8cad405`: the symbolic one-road collar and its explicitly stated physical limitation.
6. `src/ledger/20260815-160 Primal Localization-Triangle Obstruction and the One-Road Beck-Chevalley Cell.md`: additional inputs required to define the full physical obstruction.
7. Stacks Project, tag `0A8H`, Hom complexes: the mapping differential and homotopy-class interpretation.
8. Stacks Project, tag `0621`, The Koszul complex: exterior construction and its differential.
