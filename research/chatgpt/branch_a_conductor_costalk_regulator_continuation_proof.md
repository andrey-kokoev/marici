# Branch A — conductor costalk across the regulator family

Date: 2026-09-07.

## Result and scope

The entire occurrence-map-degree-zero conductor-costalk module is free over
\(\Lambda=\mathbb Z[\beta]\). In particular, all thirty-four classes in the
preceding regulator-grade-three calculation survive after inverting \(\beta\).
Their rank-thirty-one counit kernel survives as well. With the previously
specified reflection and three-label transport, the corresponding ranks are
\(11,10,1\) for the costalk, counit kernel, and counit image.

The counit nevertheless has three regulator-torsion directions in its
**lower-grade image**. A nonzero supported map in any of these directions
has a primary image killed by \(\beta\), while its own class is not killed.
The checker constructs three explicit transfers into the zero-unit kernel:
\(\mathcal B=\beta\mathcal F-\delta V\), with
\(\mathcal B(p)=0\) and \([\mathcal B]\ne0\).

These are calculations in the existing coefficient complex and frame. No
new physical source comparison, geometric purity theorem at \(\beta=0\),
or value of the physical conductor–Morse class \(\Delta_J\) is asserted.
The source's existing nonzero-regulator formal normal comparison can be
applied to these explicit coefficient maps, but does not select one of them.

## 1. Retained ring, source, and frame

Use

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]
/(X_aX_b:a\in\{02,04,24\},\ b\in\{13,15,35\}).
\]

Let

\[
I_-=(X_{02},X_{04},X_{24}),\qquad
I_+=(X_{13},X_{15},X_{35}),\qquad I=I_-\oplus I_+,\qquad A=R/I.
\]

The target \(C_\beta\) retains all 430 states \([F,H,e]\), where \(F\) is
noncrossing, \(H\subseteq F\), and \(e\in\{0,1\}\) records the independent
occurrence-\(35\) partner. Its degree is

\[
|[F,H,e]|=3-|F|+|H|+e.
\]

The radial coefficients are \(X_a\), native circle coefficients are
\(\beta X_a\), and the separate occurrence differential is \(X_{35}\).
The checker reconstructs the full signed differential and verifies its
square on every state. The endpoint packet contains 32 states, the short
boundary 416, and the actual \(Q\)-quotient fourteen.

Write \(q\) for the actual quotient and \(v\) for graded projection onto all
endpoint states. The receiving complex is unchanged:

\[
K_n=\{c\in C_{\beta,n}:q(c)=0,\ v(c)=0,\ v(dc)=0\}.
\]

This is an \(R\)-linear subcomplex. Including \(v(dc)\) is essential:
projection onto all endpoint states is not by itself a chain map. Each new
cochain and homotopy is checked against all three conditions.

The source is the same free resolution \(P_A[2]\) of the conductor module.
Its relevant ranks are \(1,6,24,92\). In the chosen even homological shift,

\[
d e_a=X_a p.
\]

The next differential contains six same-sheet Koszul relations and eighteen
ordered mixed-sheet annihilation relations; the following ninety-two
columns contain their compatibility equations. The alternating exterior-block
resolution is exact by the branchwise proof in the preceding calculation.
All these columns are reconstructed, rather than imported from a certificate.
Since the target ends in homological degree four, the displayed terms suffice
for degree-zero maps, their boundaries, and all equations they must satisfy.

For a cochain of homological degree \(n\), use

\[
\delta F=d_KF-(-1)^nFd_{P_A[2]}.
\]

Regulator degree is distinct from homological degree. A native mark has
regulator degree one; \(\beta\) has degree one; the separate occurrence
partner and source generators have regulator degree zero.

Define

\[
\mathscr M_g=
H_0\operatorname{Hom}_R(P_A[2],K)_{(0;g)},\qquad
\mathscr H_g=H_2(K)_{(0;g)}.
\]

The first index is occurrence-map degree zero and the second is regulator
normal grade. Set \(\mathscr M=\bigoplus_g\mathscr M_g\), and similarly for
\(\mathscr H\). These are graded \(\Lambda\)-modules, not assertions about
all occurrence degrees of the original \(R\)-modules.

The counit is the actual unit-column evaluation

\[
\varepsilon_*[F]=[F(p)]\in\mathscr H.
\]

It is the affine closed-immersion counit, without a regular-immersion purity
identification for the singular conductor.

## 2. Exhaust all regulator grades

For a source state of occurrence weight \(w\), a coefficient entering
\([F,H,e]\) has the forced exponent vector

\[
p_X=w+\sum_{a\in F}\epsilon_a-\sum_{a\in H}\epsilon_a-e\epsilon_{35},
\qquad p_\beta=g-|H|.
\]

Negative exponents and mixed-sheet monomials are excluded. The endpoint
conditions then give the complete cochain basis by integral unit-pivot kernel
reduction. This is an exact homogeneous component calculation, not a bound
on coefficient degree.

The complete results are:

| Regulator grade | Cochain coefficients | Closed cochains | Map boundaries | Costalk classes | Target primary rank | Counit rank |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 21 | 1 | 1 | 0 | 0 | 0 |
| 1 | 206 | 17 | 16 | 1 | 3 | 1 |
| 2 | 550 | 66 | 50 | 16 | 17 | 6 |
| 3 | 718 | 108 | 74 | 34 | 5 | 3 |
| 4 | 718 | 108 | 74 | 34 | 5 | 3 |

Every map boundary lattice has only unit invariant factors. No higher map
homotopies exist in these grades, and the map-homotopy differential is
injective. The rows therefore specify the complete derived-map quotient.

The finite table covers every regulator grade. Every target state satisfies
\(|H|\le3\). Thus once \(g\ge3\), multiplication by \(\beta\) identifies
all target-frame cochain bases and their equations at grades \(g\) and
\(g+1\). The checker verifies this identity on the entire Hom complex in
homological degrees \(-1,0,1,2\) at grades three and four. The formula for
\(p_\beta\) proves it for every later grade. Negative grades have no legal
polynomial cochains.

On costalk homology the multiplication matrices have ranks

\[
0,\ 1,\ 16,\ 34
\]

for transitions \(0\to1,1\to2,2\to3,3\to4\). Every nonzero invariant factor
is one. Thus every transition is injective, and the stable one is an integral
isomorphism.

The checker constructs homogeneous generators in degrees one, two, and
three, and verifies that their translates to grade three form a unimodular
basis. If \(\Lambda(-r)\) denotes a free regulator-graded module generated in
degree \(r\), then

\[
\mathscr M\cong
\Lambda(-1)\oplus\Lambda(-2)^{15}\oplus\Lambda(-3)^{18}.
\]

This is a module isomorphism with exported representatives, not merely a
Hilbert-series identity. In particular, \(\mathscr M\) has neither regulator
torsion nor integer torsion.

## 3. Track the entire counit under regulator multiplication

The target primary multiplication matrices have ranks \(0,3,5,5\), and the
two-step map from grade one to grade three has rank three. All nonzero
invariant factors are one. Compatible integral splittings give

\[
\mathscr H\cong
\Lambda(-1)^3\oplus\Lambda(-2)^2
\oplus\bigl(\Lambda/(\beta)\bigr)(-2)^{12}.
\]

The checker also constructs the kernel, image, and cokernel transition
matrices of the counit. They give

\[
\ker\varepsilon_*\cong
\Lambda(-2)^{10}\oplus\Lambda(-3)^{21},
\]

\[
\operatorname{im}\varepsilon_*\cong
\Lambda(-1)\oplus\Lambda(-2)^2
\oplus\bigl(\Lambda/(\beta)\bigr)(-2)^3,
\]

\[
\operatorname{coker}\varepsilon_*\cong
\Lambda(-1)^2\oplus\bigl(\Lambda/(\beta)\bigr)(-2)^9.
\]

These decompositions follow from the actual multiplication matrices, not
from ranks at independent parameter values. For the image, dimensions are
\(1,6,3\) in grades one, two, and three; transition ranks are \(1,3\), with
one surviving degree-one direction. For the cokernel they are \(2,11,2\),
with both degree-one directions surviving. The matrices and their two-step
composites have saturated images, so the indicated free and length-one
regulator-torsion summands have integral bases.

The resulting short exact sequence

\[
0\longrightarrow\ker\varepsilon_*
\longrightarrow\mathscr M
\longrightarrow\operatorname{im}\varepsilon_*
\longrightarrow0
\]

has no \(\Lambda\)-linear section on its full image. Indeed the image has
nonzero \(\beta\)-torsion whereas \(\mathscr M\) is torsion-free. A section
would carry such a torsion element into zero and could not be a right inverse.
This does not exclude a section on a chosen free primary summand, nor imply
that a generic section is physically canonical.

## 4. Three explicit primary-to-comparison transfers

The rank-three regulator-torsion part of the counit image is represented by
three grade-two supported maps. The checker exports each full source map,
its primary image, a polynomial primitive after multiplication by \(\beta\),
and the resulting zero-unit supported map.

For the first example, call the supported map \(\mathcal F_*\) and its
nonzero ten-term unit image \(U_*\). The complete map has 48 terms.
A four-term primitive is

\[
\begin{aligned}
P_*={}&-\beta^2[\{13\},\{13\},0]
-\beta[\{04,13\},\{04,13\},0]\\
&+[\{03,04,13\},\{03,04,13\},0]
+[\{04,13,14\},\{04,13,14\},0].
\end{aligned}
\]

Its full differential satisfies

\[
dP_*=\beta U_*.
\]

No parameter is inverted to obtain \(P_*\). Its endpoint and \(Q\)
components vanish, as do all incoming endpoint terms.

Let \(V_*\) be the degree-one source cochain with \(V_*(p)=P_*\) and zero
values on all other source states. Define

\[
\mathcal B_*=\beta\mathcal F_*-\delta V_*.
\]

The complete equations give

\[
\delta\mathcal B_*=0,\qquad
\mathcal B_*(p)=0,\qquad
[\mathcal B_*]=\beta[\mathcal F_*]\ne0.
\]

On source generators and relations the formulas are

\[
\mathcal B_*(e_a)=\beta\mathcal F_*(e_a)-X_aP_*,
\qquad
\mathcal B_*(r)=\beta\mathcal F_*(r).
\]

Thus setting the primary image to zero requires carrying along the actual
source-relation homotopies. The resulting map has 58 polynomial terms.
Its grade-three quotient coordinates are \(+1\) in coordinates 20 and 31
(zero-indexed, in the exported basis), and zero otherwise. These coordinates
are an integral nonvanishing detector and certify primitiveness.

The other two examples have complete term counts

| Example | Supported map | Unit image | Primary primitive | Zero-unit map |
|---:|---:|---:|---:|---:|
| 0 | 48 | 10 | 4 | 58 |
| 1 | 48 | 10 | 4 | 58 |
| 2 | 34 | 10 | 4 | 42 |

Their zero-unit classes have an integral rank-three minor with unit invariant
factors. They remain nonzero after inverting \(\beta\), since the entire
costalk module is free. Only their unit images are regulator-torsion.

The first example and its reflection sum give a strictly invariant supported
map and a strictly invariant zero-unit comparison with primitive class.
Their three labelled rotations are all checked against the corresponding
complete occurrence-corrected targets.

This transfer is not an identification with \(\Delta_J\). It identifies
an explicit mechanism by which a nonzero supported comparison can persist
although its counit/primary class vanishes after specialization.

## 5. Continue to the nonzero-regulator domain

Let \(C_1\) denote the same labelled target with native normal coefficients
\(X_d\) and the unchanged occurrence differential \(X_{35}\). Over
\(R[\beta^{-1}]\), define

\[
\Phi_\beta[F,H,e]=\beta^{|H|}[F,H,e]_1.
\]

The full 430-state calculation verifies

\[
d_1\Phi_\beta=\Phi_\beta d_\beta,
\qquad
\Phi_\beta^{-1}\Phi_\beta=1.
\]

This changes only the native normal basis. Every endpoint and short-support
label is fixed; the separate occurrence partner is not rescaled. A
homogeneous map of regulator grade \(g\) is transported to
\(\beta^g\) times its \(\beta=1\) coefficient map.

Localization is exact. Every cochain term affecting the present mapping
cohomology uses finitely many free source generators, so localization also
commutes with this Hom calculation. Therefore

\[
\mathscr M[\beta^{-1}]\cong\mathbb Z[\beta,\beta^{-1}]^{34},
\]

\[
0\longrightarrow\mathbb Z[\beta,\beta^{-1}]^{31}
\longrightarrow\mathscr M[\beta^{-1}]
\xrightarrow{\varepsilon_*}
\mathbb Z[\beta,\beta^{-1}]^3
\longrightarrow0.
\]

The image on the right is the counit image, not the full rank-five target
primary module. All thirty-four previous grade-three classes remain
independent under this continuation.

For the prescribed formal physical graph, first apply the unit change

\[
u_d=e^{\beta X_d}-1=\beta X_dv_d(X_d),\qquad v_d(0)=1.
\]

Scaling the native marks by the products of \(v_d\) gives the family already
used here. For fixed \(\beta\ne0\), the remaining scale
\(\beta^{|H|}\) is also invertible. The source requires characteristic-zero
formal coefficients for the exponential, and that scope is retained. No
occurrence coordinate is inverted, and no new claim of purity at regulator
zero is made. The normal and occurrence factors are not identified with one
another.

The integer ranks above continue to the characteristic-zero coefficient
field. This is an explicit continuation of the coefficient model; identifying
its supported map with a marked physical spatial Gysin operation remains
separate.

## 6. Symmetry and the remaining choice

Use the inherited cellular/source reflection and the three occurrence
corrections \(35,15,13\). The costalk invariant ranks are

| Regulator grade | Invariant costalk classes | Invariant counit image |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 5 | 2 |
| 3 and above | 11 | 1 |

The invariant multiplication maps are injective with unit invariant factors.
Thus

\[
\mathscr M^{\langle s\rangle}
\cong\Lambda(-2)^5\oplus\Lambda(-3)^6.
\]

After localizing,

\[
0\longrightarrow\Lambda[\beta^{-1}]^{10}
\longrightarrow\mathscr M^{\langle s\rangle}[\beta^{-1}]
\longrightarrow\Lambda[\beta^{-1}]
\longrightarrow0.
\]

The action is the specified one, including the source-unit convention. A
new physical orientation-line twist would require re-evaluating its invariant
condition; it is not silently inserted here. Full dihedral families are
obtained by transporting the reflection-fixed maps through all three occurrence
labels, not by pretending rotation fixes one corrected complex.

Consequently nonzero-regulator continuation does not make the supported lift
unique. Fixing its invariant primary still leaves ten invariant zero-primary
directions. The two relation-only invariant directions from the preceding
calculation survive, since the complete grade-three costalk injects into its
localization. Regulator regularity cannot replace their missing geometric
selector.

## 7. Verification and reproducibility

The checker is standalone and uses only the Python standard library. Its
embedded algebra routines reconstruct the coefficient ring, full differential,
source resolution, frame kernels, Hom equations, homotopy quotient, all
regulator transition matrices, the counit, and the example transfers. It does
not read old certificates, companion modules, or network resources.

It performs 554,284 counted exact checks in addition to the native Python
assertions in the generalized grade solver. Grades zero through four are
computed; all later grades follow from the explicit basis/differential
stabilization identity and the global bound \(|H|\le3\).

A fresh execution with only the checker in a temporary directory and a
different Python hash seed reproduced the certificate byte-for-byte.
Mathematical content hash:

```text
2a3d3869d77ec2ecbcdb8a6057f324c288db482090282ab79a5094dc178db9ed
```

Run:

```bash
python branch_a_conductor_costalk_regulator_continuation_checker.py \
  --output branch_a_conductor_costalk_regulator_continuation_certificate.json
```

## Sources

The repository inputs are pinned to commit
`d1947b67a60d3e88ba77f4ca60ea02c2a306ee61` of `andrey-kokoev/marici`:

- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`:
  the normalization ring, two conductor ideals, and exact sequences.
- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`:
  the signed radial/native differential, support subcomplexes, and label action.
- `research/voevodsky/check_d03_formal_support_purity.rs`:
  the fixed-nonzero-regulator normal comparison and its formal characteristic-zero
  scope.

Standard facts used: Stacks Project tags `0A74` for the closed-immersion
costalk and counit, `0A8H` for the Hom differential, `064B` for computation
with projective resolutions, `0621` for changes of Koszul generators, and
`00H9` for exact localization/flatness. The rank computations and displayed
chain witnesses are established by the accompanying matrices, not by these
general references.
