# Relative admissibility of the coherent endpoint lift

Date: 2026-09-06  
Pinned repository: `andrey-kokoev/marici`  
Commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and evidence boundary

Two computations are completed here, and their comparison is **not** assumed.

First, a canonical node/norm detector in the supplied endpoint coefficient model turns the previous unframed coherent-lifting result into a genuinely relative problem. The coherent unit has a nonzero order-two node component and a nonzero order-three norm component. Prescribing an incompatible component makes the relative lifting space empty. Prescribing a compatible complete detector object gives two contractible components, forming a torsor for the group of order two. The extra choice is a compatibility homotopy, not a second underlying arithmetic unit.

Second, the actual seven-generator generic quotient in the source's target-side extended-Cech complex has a calculable support-sensitive top obstruction. Every legal filler of the negative top boundary is classified. No such filler has zero top coefficient over the independent polynomial coefficient ring. The obstruction is a nonzero principal-part class annihilated by the product of the three normal parameters, and not by any nonzero integer. A globally localized repair would work algebraically but is outside the prescribed stalks.

The one-road first-Rees/closed coefficient equation also checks exactly. However, these results do not construct the support-typed normalization-sheet arrow and both endpoint connector cells. They therefore do not decide the actual physical parity or identify the detector's two-element torsor with the source's physical endpoint torsor. Matching their abstract group structures would not suffice.

## 1. The existing coefficient complex and orientation

All chain degrees in this note are homological. In the polynomial endpoint model, put

\[
A=\mathbb Z[x,y]/(xy),\qquad N=\mathbb Z[x]\oplus\mathbb Z[y].
\]

In words: use node functions and independent functions on their two normalization branches. The complex is

\[
P_3=\mathbb Z,\quad P_2=A\oplus\mathbb Z^3,\quad
P_1=N\oplus\mathbb Z^3,\quad P_0=\mathbb Z_\chi,
\]
\[
d_3(c)=(0,(c,c,c)),\quad
 d_2(a,t)=(\nu(a),(1-r)t),\quad
 d_1(f,g,q)=f(0)-g(0)-\sum_iq_i.
\]

In words: retain the source norm, node, tag, sheet, road, and endpoint terms. The symmetry group is

\[
G=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle,
\qquad\chi(r)=1,\quad\chi(s)=-1.
\]

In words: use the triangle dihedral group, of order six, and its reflection character. This is not the octagon group of order sixteen.

Use the source's once-relative polarity compensation on the entire complex. The compensated action is the original action multiplied by the character. Under it, the node constant and top norm generator are both reflection-odd. The physical readout is invariant.

Let

\[
K_0=\ker d_1,\qquad K_1=P_2,\qquad K_2=P_3,
\qquad \varphi(v)=\sum_iq_i.
\]

In words: cycles become marking objects, node/tag terms become paths, and the norm term becomes a comparison between paths. The normalized marking space is the fibre at one of the Dold-Kan readout. The prior exact contraction proves that the full equivariant readout is a quasi-isomorphism, and consequently

\[
X^{hG}\simeq *.
\]

In words: before fixing further coherent data, the space of coherent physical-unit markings is contractible. This statement was rechecked by rerunning the existing 6,643-assertion checker.

The degreewise branch-polynomial comparison to the finite endpoint model is an equivariant quasi-isomorphism. Its kernel is an identity complex on the positive branch ideals. Nothing below discards positive polynomial modes without those actual relations.

## 2. A specified relative detector

Define a chain complex and a map by

\[
D_1=D_2=\mathbb Z_\chi,\qquad D_n=0\ (n\ne1,2),\qquad d_D=0,
\]
\[
p_0=0,\qquad p_1(a,t)=a(0,0),\qquad p_2(c)=c.
\]

In words: record the node's conductor constant in path degree and the norm coefficient in the next degree. The differential has no node component on the norm, so this is a chain map. Both retained coefficients have the same compensated sign action, so it is equivariant.

This detector uses distinguished summands already present in the supplied complex. It is **not** declared to be the physical generic-Q/endpoint restriction. In particular, the norm generator in this coefficient complex is not identified with the geometric generic top merely because both are called a top cell.

The positive branch-ideal contraction has detector value zero, and the polynomial-to-finite comparison commutes with p. Therefore this relative detector computation is unchanged by retaining the full polynomial branches.

Write

\[
Y=(\operatorname{DK}D)^{hG},\qquad
\mathcal R_b=\operatorname{hofib}_b\bigl(X^{hG}\longrightarrow Y\bigr).
\]

In words: prescribe an actual coherent detector object b and keep a specified comparison to it as part of the lift. Merely selecting a connected component of Y would be a weaker framing and would omit the ambiguity computed below.

## 3. The coherent boundary data are not zero

Write group elements as \(g=r^i s^e\), with rotation index in zero through two and reflection index in zero through one. The previous integral coherent unit uses

\[
h_g=-e\,a-\sum_{j=0}^{i-1}t_j,
\qquad
k_{g,h}=-\left\lfloor\frac{i+(-1)^e j}{3}\right\rfloor u.
\]

In words: the node relation compares reflected sheets, road tags compare rotations, and the norm cell records wrapping around the three-road cycle.

Their detector images are

\[
\alpha(r^i s^e)=-e,
\qquad
\beta(r^i s^e,r^j s^f)
=-\left\lfloor\frac{i+(-1)^e j}{3}\right\rfloor.
\]

In words: alpha is the recorded node homotopy and beta the recorded norm comparison. With the sign action, these are respectively a group one-cocycle and two-cocycle. The checker verifies every group pair and every one of the 216 triples.

For the usual group-cochain differential,

\[
2\alpha=\delta(1),\qquad
3\beta=\delta b,\qquad b(r^i s^e)=-i.
\]

In words: twice the node record and three times the norm record are coboundaries. Neither original record is a coboundary. On the reflection subgroup, alpha has odd value; on the rotation subgroup,

\[
\sum_{i=0}^{2}\beta(r^i,r)=-1.
\]

In words: a cyclic coboundary has a sum divisible by three, whereas this sum is minus one. This proves the exact orders without assuming that a failure of one chosen filler excludes all replacements.

### Complete low-degree group cohomology

A sign-module one-cocycle vanishes on r because three times its value is zero in the integers. Its value on s is arbitrary; coboundaries change it by an even integer. The invariant subgroup of the sign module is zero. Thus

\[
H^0(G,\mathbb Z_\chi)=0,\qquad
H^1(G,\mathbb Z_\chi)=\mathbb Z/2.
\]

In words: there is no invariant integer in the sign line, and the one-cocycle obstruction is exactly parity.

For completeness, classify the extensions describing the second cohomology. Write A for the infinite cyclic kernel and choose lifts R and S of r and s. Rotation centralizes A and reflection inverts it. If the square of S is a power of A, conjugating that square by S forces the exponent to be zero. Write the mixed relation as S R S-inverse equal to A to the t times R-inverse. Applying the conjugation twice forces twice t to vanish, so t is zero. The only remaining parameter is the integer p in R-cubed equal to A to the p. Replacing R by A to the m times R changes p by three m. Every p is realizable. Hence

\[
H^2(G,\mathbb Z_\chi)=\mathbb Z/3.
\]

In words: the norm record generates the entire second cohomology group, not just an exhibited subgroup. The extension classification is an all-integer proof; the finite checker validates the explicit cocycles and their exact-order tests.

## 4. The relative lifting space has two components

Mapping-space homotopy for the two detector degrees gives

\[
\pi_0Y\cong\mathbb Z/2\oplus\mathbb Z/3,
\qquad\pi_1(Y,b)\cong\mathbb Z/2,
\qquad\pi_n(Y,b)=0\quad(n\ge2).
\]

In words: Y has six components. Each component is a classifying space for the group of order two. The first homotopy group comes from the sign-module first cohomology of the detector's degree-two term; it is not the same role as the degree-one record in the component group.

The unique unframed coherent unit maps to the component

\[
e_D=([\alpha],[\beta]).
\]

In words: both components of its coherent record are nonzero. All alternative coherent unit representatives have the same component, since the unframed source space is contractible.

Therefore an incompatible prescribed record, including the zero record, gives an empty relative lifting space. For a prescribed object in the matching component,

\[
\#\pi_0\mathcal R_b=2,
\qquad\pi_n(\mathcal R_b)=0\quad(n\ge1).
\]

In words: there are two relative classes and each is contractible. More intrinsically, the component set is a torsor for the group of order two. There is no preferred component until a compatibility path has been supplied.

Proof: replace the contractible domain by a point. The homotopy fibre over b is the space of paths between that point's image and b. It is empty outside the image component and otherwise equivalent, after choosing one such path, to the loop space of that component. This uses a genuine homotopy fibre and retains the compatibility homotopies. It is not an argument from strict fixed points or from deleting generators.

An explicit generator of the difference between the two relative classes is the one-cocycle alpha, now placed in the detector's degree-two term. It is a loop of coherent norm data. Twice that loop is a boundary. It changes the compatibility identification, not the state z or its endpoint readout.

## 5. The actual target-side Q quotient

Independently of the detector, the pinned target-side Cech source specifies a concrete support triple

\[
F_V\subset F_B\subset F_K,
\qquad Q=F_K/F_B.
\]

In words: retain both distinguished endpoint vertices, the short-boundary support, and the full six-point associahedral support. The checker reconstructs all 215 loaded generators and the two subcomplexes, of ranks 16 and 208. It verifies the full absolute and Cech differential identities and their coefficient comparison on every generator.

For the target differential, a loaded cell labelled (S,H) has coefficient ring with precisely the normals indexed by S minus H inverted. Radial arrows have coefficient X-a divided by u-a; normal-removal arrows have coefficient one. No global normal localization is performed.

The resulting Q has one top T and three marked normal generators M-i in degree three, and three unmarked facet generators F-i in degree two. Let R be the independent polynomial ring in the three long occurrences and their normals, with polynomial spectators adjoined. Then

\[
Q_3=RT\oplus\bigoplus_{i=0}^{2}RM_i,
\qquad Q_2=\bigoplus_{i=0}^{2}R[u_i^{-1}]F_i,
\]
\[
dT=\sum_i\frac{X_i}{u_i}F_i,\qquad dM_i=F_i.
\]

In words: the normal generator itself is unlocalized, even though its target facet allows that normal inverse. An identity coefficient on an arrow between these modules is a localization inclusion, not an isomorphism of their coefficient modules.

These are the literal seven quotient generators and the literal source differential. They are not the earlier finite three-tag complex with every coefficient replaced by one.

## 6. All legal replacements of the top filler

Put

\[
U=u_0u_1u_2,\qquad
\omega=UT-\sum_iX_i\!\prod_{j\ne i}u_j\,M_i.
\]

In words: the product of all normal parameters clears the three different stalk denominators. The displayed element is a cycle.

More strongly,

\[
\ker(d:Q_3\to Q_2)=R\omega.
\]

In words: every cycle is an R-multiple of this one. To prove completeness, write a cycle as a T plus the sum of b-i M-i. Its equations force b-i equal to minus a X-i divided by u-i. Since X-i and u-i are independent and the b-i are unlocalized, every u-i divides a. Their product therefore divides a. Conversely that divisibility makes every b-i legal. No averaging, generic-rank calculation, or polynomial degree bound is involved.

It follows, for any prescribed polynomial k, that

\[
dv=-k\,dT
\quad\Longleftrightarrow\quad
v=-kT+b\omega\quad(b\in R).
\]

In words: this lists **every** legal replacement filler. Its top coefficient is minus k plus b U. Thus a zero-top replacement exists exactly when k is divisible by U. In particular, neither k equal to one nor the independent first-Rees coefficient k equal to x3 admits such a replacement.

The tempting expression with coefficients minus k X-i divided by u-i on the marked normal generators has the correct formal boundary but lies outside their rings. It becomes valid after globally inverting normals, which changes the problem. This negative control is checked explicitly.

### Relative-complex form of the same obstruction

Project Q onto the labelled top coefficient R in homological degree three, and take its homotopy fibre. The projection is degreewise surjective, so its ordinary kernel is a correct fibre model:

\[
F_T=\bigoplus_i[RM_i\longrightarrow R[u_i^{-1}]F_i].
\]

In words: hold the labelled top coefficient fixed and retain all normal/facet comparison data. This is a direct sum of localization maps in degrees three and two.

Its only homology is

\[
H_2(F_T)=\bigoplus_i R[u_i^{-1}]/R.
\]

In words: principal parts at the three normal divisors are the relative obstruction module. The connecting class of the top unit is

\[
\theta=\left[\left(\frac{X_0}{u_0},\frac{X_1}{u_1},\frac{X_2}{u_2}\right)\right],
\qquad \operatorname{Ann}_R(\theta)=(U).
\]

In words: precisely multiples of the product of the normal parameters annihilate the class. It has infinite additive order; multiplying by two, three, or six does not remove it. This is normal-support torsion as an R-module, **not integer-prime torsion**.

This is a labelled-top relative calculation on the source's actual target coefficient complex. It does not identify that top projection with the full physical based-Q restriction. A physical framing may prescribe a nonzero connecting class rather than demand this class vanish. Extra geometric base-change relations can also change the divisibility calculation; they must be supplied and computed, not assumed.

## 7. One actual D03 coefficient chart

The source's first-Rees/closed bridge fixes the independent coefficients

\[
k=x_3,\qquad a=-\frac{X_{D03}}{u_{D03}},
\qquad x_3a+\frac{X_{D03}}{u_{D03}}k=0.
\]

In words: the generic component is nonzero and first order in x3, while the lower component uses a normal inverse only in its already-localized target summand. The displayed chain equation closes exactly.

The source identifies the first conormal symbol of x3, with its positive orientation, with the closed unit. It does not evaluate the ordinary polynomial value of x3 at zero and call that a unit. The checker reproduces the coefficient identity and its first-order leading coefficient. It does not build the missing geometric support attachment by tensoring formal coefficient symbols.

For the independent polynomial model the complete one-road syzygy is generated by the displayed pair: all solutions are its multiples, with allowed coefficients determined by the source/target rings. The generic normalization and fine grading fix the primitive multiple. The source's own audit distinguishes this strict coefficient compatibility from attachment of the relative logarithmic path to the absolute generic-Q generator.

The earlier node and norm fillers cannot simply be carried through this chart by identifying names. The actual support quotient and stalk rings described in Sections 5–6 must be respected, and a map into those rings has not been supplied by the coefficient detector.

## 8. What remains undecided

The physical relative lift would be a homotopy fibre for the actual restriction of admissible, mixed-variance maps to the prescribed generic leg and both endpoint connectors. Its differential is a relative Hom differential, not a scalar normalization equation.

The missing comparison must establish which coherent target object is induced by the normalization-sheet geometry, including both endpoint comparison cells. Only then can one compare its induced class with the coefficient record in Section 3, or identify its residual parity with the two-component fibre in Section 4.

The inspected `check_dp6_endpoint_q_mapping_fiber.rs` explicitly reports its spatial restriction as unconstructed and its mapping fibre as uninstantiated. Its zero-parity calculation is conditional on these maps. The later one-road coefficient gate proves a strict coefficient identity but explicitly does not construct the required support attachment. Those facts prevent assigning physical parity here.

Accordingly, the conclusions are:

- fixing only endpoint scalar values leaves the known contractible coherent-unit space;
- fixing the explicit node/norm detector produces the exact empty-or-two-component relative answer;
- in the actual labelled Q coefficient complex, a top filler cannot in general be made relative-zero without changing the allowed stalks;
- the full physical restriction and its preferred compatibility class have not been constructed by this calculation.

## 9. Reproduction and sources

Run:

```sh
python check_relative_physical_admissibility.py --output relative_physical_admissibility_certificate.json
```

The run passes 3,541 exact assertions. It checks the source detector and D3 covariance, every pair and triple of the coherent lift, the exact-order cocycle identities, polynomial contraction compatibility, all 215 target generators, the support inclusions, the absolute-to-Cech comparison, the seven-generator Q equations, the all-filler formulas on explicit inputs, and the one-road coefficient identities. The algebraic proofs establish completeness over all polynomial degrees and the full homotopy-type claims. This is not proof-assistant certification.

No repository files were modified. The checker is self-contained and uses only Python's standard library. It copies the prior explicitly verified coefficient-model helpers and adds the new relative and target calculations.

Pinned source records:

| Source | Blob or role |
|---|---|
| `research/voevodsky/check_conductor_road_endpoint_pullback.rs` | `cfe13e928e911f8914de6670f34cc4c8859b3402`; source D3 action and endpoint complex |
| `research/voevodsky/check_global_k6_koszul_cech_promotion.rs` | `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`; target stalks and signed differentials |
| `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md` | `02cedbb15dd385a75bab759dfcdb4daa28bd3b3c`; fixed target, exact support triple, paired-packet and endpoint restrictions |
| `src/ledger/20260817-378 The Generic x3 Coefficient Is the Rees Lift of the Cartier Unit.md` | `8f090ff19cda4f6bc6283a1e6c40057f12503490`; first-Rees coefficient and closed conormal placement |
| `src/ledger/20260817-393 The Beck-Chevalley Coefficient Square Closes Strictly.md` | `f172422e7be3b9a4080f2afc9d977c50903b0f27`; coefficient closure versus support attachment |
| `research/voevodsky/check_dp6_endpoint_q_mapping_fiber.rs` | `592811b138855554c921dcf4269581632e8f0050`; explicitly conditional parity calculation |

Mathematical conventions: Stacks Project, *Hom complexes*, tag `0A8H`, and *Group cohomology*, tag `0A2H`; Kedlaya's *Notes on Class Field Theory*, section *Cohomology of cyclic groups*. All new relative conclusions are proved above rather than attributed to these references.
