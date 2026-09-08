# Filtered Q after the alternating-sheet/Rees base change

Date: 2026-09-07  
Lane: the full support filtration and its generic-Q connecting class  
Source repository: `andrey-kokoev/marici`  
Pinned input: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result

The previously computed six-normal annihilator cannot be specialized as a homology formula to the alternating-sheet source. Its coefficient product, and the old global top-cycle representative, both become zero. Recomputing the actual bounded free target complexes gives a different, nonprincipal annihilator:

\[
\operatorname{Ann}_{\mathcal B}[\beta]
=\mathfrak a
=(\tau_+\tau_-,\ \tau_+ I_+,\ \tau_- I_-).
\]

In words: the generic-Q connecting class remains nonzero. Its common-conductor mode is killed by all six short Rees factors, while each positive-degree branch mode is killed by that branch's three Rees factors. This statement is about the specified target connecting class, not an already identified physical source class.

The computation also determines the complete top boundary homology:

\[
H_3(A_\partial)\cong I_+^{\oplus6}\oplus I_-^{\oplus6}.
\]

In words: twelve labelled families of boundary-supported top cycles are invisible to the generic-Q projection. The displayed isomorphism forgets their different internal normal multidegrees, which are retained explicitly below and in the checker.

Thus a generic multiple lifts exactly when its coefficient belongs to the displayed ideal. Nonempty *ungraded* lifting spaces are discrete torsors under this boundary module, not automatically contractible. The homogeneous zero-short-occurrence-degree sector has no such ambiguity. No unrestricted conclusion about the fully framed physical mapping space follows.

## 1. What the branch updates change

The latest retrieved source-admissibility proof (saved 2026-09-07, 15:21 UTC; internal title *Source admissibility of the proposed conductor–Morse primitive*) distinguishes the Entry-436 source unit from the corrected historical Morse roof. The unit is not a boundary and its conductor comparison sends it to one. The corrected Morse roof is a boundary. Consequently a degree-preserving chain comparison cannot identify them. Nor may a nonclosed conductor cochain be postcomposed with a derived roof while omitting its homotopy-transport correction.

The saved Branch A supported `(t04,t35)` Gysin calculation constructs purity for the **dual comparison resolution**, retaining the endpoint line, ordered normal determinant, and independent `u03` normal. It explicitly does not provide an ordinary inclusion realizing the native class or a scalar trace sending that class to one. Its compatible tensor maps do not manufacture a nonzero normalization-to-Q source map.

The latest Branch C normal-comparison artifact, `gysin_normal_comparison.md`, distinguishes a conormal-symbol evaluation from scalar division by a Rees coefficient. The factor-retaining overlap correction is not itself the physical residue map: its raw scalar version becomes null under the stated Cartier test. Different occurrence, Rees, branch, and physical-channel coordinates remain distinct.

Those results rule out another primitive-signature identification as the next move. The independent test here is instead to compute what happens to our actual target obstruction over their source coefficient ring. No new source primitive or geometric correspondence is postulated.

## 2. Fix the coefficient ring and the source map

The positive and negative short-diagonal sets in the loaded hexagon convention are

\[
S_+=\{13,35,15\},\qquad S_-=\{02,24,04\},\qquad
L=\{03,14,25\}.
\]

In words: the two short sets are the two alternating endpoint triangulations; the long set contains the three pairwise-crossing long diagonals. These labels are retained, rather than merged by a symmetry quotient.

Use the spectator ring

\[
\mathcal C=\mathbb Z[t_s\ (s\in S_+\cup S_-),\ X_l,u_l\ (l\in L)].
\]

In words: all six short Rees parameters and all three long occurrence/normal pairs are independent. Additional passive polynomial or Laurent spectator coordinates can be tensored in. No long normal is identified with an occurrence coordinate, and no long resonance is imposed in the main theorem.

The alternating source ring is

\[
\mathcal B_+=\mathcal C[X_p\mid p\in S_+],\qquad
\mathcal B_-=\mathcal C[X_m\mid m\in S_-],
\]
\[
\mathcal B=\mathcal B_+\times_{\mathcal C}\mathcal B_-
=\mathcal C[X_s\mid s\in S_+\cup S_-]/(X_pX_m\mid p\in S_+,m\in S_-).
\]

In words: a coefficient is a pair of branch polynomials with the same conductor value. A product involving positive-degree variables from both sheets is zero. This is the source normalization/conductor construction of Entry 93, extended by the retained spectator ring.

Put

\[
I_+=(X_p\mid p\in S_+),\quad I_-=(X_m\mid m\in S_-),\quad
I=I_+\oplus I_-,
\]
\[
\tau_+=\prod_{p\in S_+}t_p,\qquad
\tau_-=\prod_{m\in S_-}t_m.
\]

In words: these are the two branch ideals and the two labelled products of three short Rees parameters. They are not integral primes.

From the previous independent coefficient ring

\[
R=\mathbb Z[X_a,u_a\mid a\in S_+\cup S_-\cup L]
\]

take the source-prescribed graph map

\[
R\longrightarrow\mathcal B,\qquad u_s\longmapsto t_sX_s\ (s\in S_+\cup S_-).
\]

In words: only the short normal coefficients acquire their actual Rees factorizations. Long coefficients remain independent. Entry 115 supplies the one-normal differential with coefficient `t_i x_i`; the later branch calculations use these factorizations on the alternating conductor ring.

The source's units `1+t_s X_s` may subsequently be localized. This is a flat change of the ring just defined and preserves the displayed exact sequences and ideals after localization. It does not invert any `t_s` or `X_s` at the conductor.

### Why the old formula cannot simply be substituted

Previously, with independent normal variables,

\[
\Delta=\prod_{s\in S_+\cup S_-}u_s,\qquad
\operatorname{Ann}_R[\beta_R]=(\Delta).
\]

In words: the old obstruction required all six independent short normal factors.

Under the graph map,

\[
\Delta\longmapsto\tau_+\tau_-\prod_sX_s=0.
\]

In words: the product contains occurrences from both alternating sheets. Every coefficient of the old global top cycle also contains this mixed occurrence product, so that entire representative becomes zero.

The map is not flat. It is therefore invalid to infer the new homology or annihilator by substituting into the old homology module. We apply the coefficient map to the **actual bounded free complexes**. These compute derived tensor product without an additional replacement. See Stacks Project, Section 15.60, especially Lemma 15.60.7. The previous source-admissibility correction is respected: no contraction of a nonzero unit is introduced.

## 3. Retain the full support triangle

The loaded generator is `[F,H]`, with `F` a noncrossing face and `H` a subset of `F`. Its homological degree is

\[
|[F,H]|=3-|F|+|H|.
\]

In words: marks add normal degree to the underlying face degree. The source differential is

\[
\begin{aligned}
d[F,H]={}&\sum_{a\text{ addable}}(-1)^{\#\{b\in F:b<a\}}X_a[F\cup\{a\},H]\
&+(-1)^{3-|F|}\sum_{h\in H}(-1)^{\operatorname{pos}_H(h)}u_h[F,H\setminus\{h\}],
\end{aligned}
\]

with the short substitutions just specified. In words: add an allowed diagonal with its occurrence coefficient, or remove a mark with its normal coefficient. Positions begin at zero.

The actual source subcomplexes give

\[
0\longrightarrow A_\partial:=F_B/F_V
\longrightarrow E:=F_K/F_V
\xrightarrow{\pi}Q:=F_K/F_B\longrightarrow0.
\]

In words: remove the two complete endpoint cubes only in the indicated quotient; retain every mixed cell in the other terms. Before quotienting, there are 215 loaded states. Their free-module ranks in degrees zero through three are:

| Object | Ranks |
|---|---|
| Full target `F_K` | 14, 63, 93, 45 |
| Both endpoint cubes `F_V` | 2, 6, 6, 2 |
| Short boundary `F_B` | 14, 63, 90, 41 |
| Endpoint quotient `E` | 12, 57, 87, 43 |
| Boundary quotient `A_partial` | 12, 57, 84, 39 |
| Generic quotient `Q` | 0, 0, 3, 4 |

The exact sequence is degreewise split over the coefficient ring because its summands are labelled source states. No claim that its homology sequence splits is made. The preceding correct barycentric subdivision comparison also base-changes; no mixed-flag erasure is reintroduced.

## 4. The genuine generic class survives

Write `q0` for the empty-face top generator, `h_l` for a marked long facet, and `e_l` for an unmarked long facet. Then

\[
dq_0=\sum_{l\in L}X_l e_l,\qquad dh_l=u_l e_l.
\]

In words: these are the entire seven-state quotient differential. Its coefficients do not involve short variables.

Set

\[
U_L=\prod_{l\in L}u_l,\qquad
\theta=U_Lq_0-\sum_{l\in L}X_l\prod_{j\in L\setminus\{l\}}u_j\,h_l.
\]

In words: this is the actual degree-three polynomial cycle, not the earlier degree-one Morse roof.

The long variables remain regular polynomial variables over the alternating ring. Reducing `X_l a+u_l b_l=0` modulo `u_l` forces `u_l` to divide `a`; imposing all three rows forces `U_L` to divide `a`. The remaining coordinates are then uniquely determined. There are no degree-four terms. Hence

\[
H_3(Q)=\mathcal B\theta.
\]

In words: the generic top homology is still one free line over the full alternating coefficient ring.

Use the same four-term vector as a lift `theta_tilde` into the full target and set

\[
\beta=d\widetilde\theta\in(A_\partial)_2.
\]

In words: its eighteen-term boundary is the actual connecting cycle. It has six single-short-facet terms and twelve mixed short/long terms. Every coefficient contains exactly one short occurrence variable. The executable certificate exports all terms, not just their leading coordinates.

## 5. Exact lifting ideal

### Necessity

A degree-three chain has only fully marked generators. Write its coefficient at `[F,F]` as

\[
c_F=(-1)^{|F|(|F|+1)/2}b_F.
\]

In words: this orientation gauge puts every top-cycle equation into the same form:

\[
u_a b_F=X_a b_{F\setminus\{a\}}.
\]

In words: the normal coefficient on a face matches the occurrence coefficient on its predecessor. These equations are imposed only where the corresponding target state is retained in `E`.

For a lift of `k theta`, the empty-face coefficient is `U_L k`. Restrict to the positive polynomial sheet. At each positive short singleton, cancellation of the nonzero polynomial `X_p` gives

\[
t_p b_{\{p\},+}=U_L k_+.
\]

In words: this is cancellation in the polynomial sheet for a proof, not inversion in the original ring or a proposed trace. Coprimality of the independent Rees and long-normal variables implies that each `t_p` divides `k_+`. The three parameters are independent, so their product divides it. The negative sheet gives the other condition:

\[
k_+\in\tau_+\mathcal B_+,\qquad
k_-\in\tau_-\mathcal B_-.
\]

In words: both branchwise divisibility conditions are necessary.

Their common conductor value belongs to the intersection of the two principal ideals in `C`, which is their product. Using the unique branch normal form gives the equivalent single ideal condition

\[
k\in(\tau_+\tau_-,\ \tau_+I_+,\ \tau_-I_-)=\mathfrak a.
\]

In words: a common conductor term needs all six Rees factors; a positive-degree term on one sheet needs its own three factors.

### Sufficiency, with all endpoint coefficients retained

Let `D` denote all nine diagonals, and put

\[
\Lambda_0=
\sum_{F}(-1)^{|F|(|F|+1)/2}
\left(\prod_{s\in S\setminus F}t_s\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L\setminus F}u_l\right)[F,F].
\]

In words: sum all 45 faces, including both endpoints. The short factors are the retained Rees parameters, not inverses. Every top-cycle equation holds directly, so

\[
d\Lambda_0=0,\qquad \pi\Lambda_0=\tau_+\tau_-\theta.
\]

In words: this is a new lift; it is not the vanished specialization of the old global cycle.

For a positive short label `p`, define

\[
\Lambda_{+,p}=X_p
\sum_{F\subseteq S_+\cup L}(-1)^{|F|(|F|+1)/2}
\left(\prod_{s\in S_+\setminus F}t_s\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L\setminus F}u_l\right)[F,F],
\]

where only noncrossing faces are included. In words: retain one branch's complete allowed faces and its actual positive endpoint. The prefactor `X_p` kills every outgoing opposite-sheet occurrence coefficient by the source relation, rather than by deleting those arrows.

The analogous negative cycles satisfy, together with the positive ones,

\[
d\Lambda_{\pm,s}=0,\qquad
\pi\Lambda_{\pm,s}=\tau_\pm X_s\theta.
\]

In words: six further full target cycles lift the other six ideal generators. These seven constructions prove sufficiency for every polynomial coefficient in the ideal.

For each generator `g` with its displayed lift, the source-supported annihilation homotopy is

\[
W_g=g\widetilde\theta-\Lambda_g,\qquad dW_g=g\beta.
\]

In words: the homotopy is an actual chain in the full short boundary, retaining its endpoint entries. All seven are exported in the certificate.

The long exact sequence of the support triangle now gives

\[
\operatorname{Ann}_{\mathcal B}[\beta]=\mathfrak a,\qquad
\mathcal B[\beta]\cong\mathcal B/\mathfrak a\subseteq H_2(A_\partial).
\]

In words: this computes the entire cyclic submodule generated by the obstruction, not all of the second boundary homology.

## 6. Lift ambiguity, not just lift existence

The same top equations determine the complete kernel of the generic projection.

A top cycle in `A_partial` has zero empty and long-only coefficients. Its conductor specialization is zero coefficientwise: applying the short recurrence on the appropriate sheet and then restricting to the conductor gives `t_a b_F=b_(F-a)`. Induction from the zero empty and long-only coefficients, using regularity of the retained parameters, forces every conductor coefficient to vanish.

It therefore decomposes uniquely into positive- and negative-ideal parts. On the positive sheet, the inactive negative short marks cannot be changed by any nonzero coefficient in a top-cycle equation. Fix their subset

\[
\varnothing\ne N\subsetneq S_-.
\]

In words: there are six possible proper nonempty inactive subsets. The full negative endpoint subset is absent from `E`.

Let

\[
P_N=\{p\in S_+:p\text{ is compatible with every }n\in N\},\quad
L_N=\{l\in L:l\text{ is compatible with every }n\in N\}.
\]

In words: these are the allowed active short and long extensions of the fixed inactive subset. The component generator has coefficients

\[
\Gamma_{+,N}=
\sum_{N\subseteq F\subseteq N\cup P_N\cup L_N}
(-1)^{|F|(|F|+1)/2}
\left(\prod_{p\in P_N\setminus F}t_p\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L_N\setminus F}u_l\right)[F,F].
\]

In words: sum only actual noncrossing faces. Multiplying this vector by any element of `I_plus` gives a genuine boundary-supported cycle. The coefficient factor is necessary; `Gamma` alone need not be a cycle over the glued ring.

The recurrence proves that every cycle in this component is uniquely of this form. Dividing a coefficient by the necessary product of independent `t` and long-`u` parameters preserves its zero conductor value, so the free parameter lies precisely in `I_plus`. The negative argument is identical. Consequently

\[
H_3(A_\partial)\cong
\bigoplus_{\varnothing\ne N\subsetneq S_-}I_+\Gamma_{+,N}
\ \oplus\!
\bigoplus_{\varnothing\ne N\subsetneq S_+}I_-\Gamma_{-,N}.
\]

In words: this is a labelled module decomposition into six copies of each branch ideal. It is not a free module of rank twelve over `B`. There is an exact sequence

\[
0\longrightarrow I_+^{\oplus6}\oplus I_-^{\oplus6}
\longrightarrow H_3(E)\longrightarrow\mathfrak a\longrightarrow0.
\]

In words: the middle group maps onto the lifting ideal; no splitting of this sequence is asserted.

There are no chains above degree three, so the unrestricted derived spaces of degree-three markings are discrete. For `k` in the lifting ideal, the fibre over `k theta` is a torsor for the displayed boundary module. It is empty for `k` outside the ideal. In particular the unit does not lift.

### The internal-grading qualification is essential

All ambiguity coefficients have positive short occurrence degree. In the fixed zero-short-occurrence-degree sector, the ambiguity module is zero. The minimal seven homogeneous ideal generators also have their unique lifts in their own minimal fine degrees; extra ambiguities appear in suitable larger multidegrees. A fully source-framed comparison may impose additional conditions. This computation does not license arbitrary boundary variations in that more restricted category.

## 7. The same main obstruction in the specified PC target

For a cell, retain exactly the source ring

\[
\mathcal B[u_a^{-1}\mid a\in F\setminus H].
\]

In words: inverse normal coordinates are allowed only in that cell's indicated summand. After the graph substitution, inverting one short normal also inverts its occurrence and Rees factors on that localization. It kills the other normalization sheet. A summand that inverts short normals from both sheets is the zero ring. The checker finds fifteen such source-labelled summands; their disappearance follows from their actual ring, not an imposed chain erasure.

The source PC differential has radial coefficient `X_a/u_a` and unit mark-removal coefficient. The diagonal comparison multiplies a state by the inverse product of its unmarked normals. All 215 comparison squares and all localized differential identities are checked with these actual zero-divisor rules.

Every top state is fully marked, so its coefficient ring is still `B`. A top boundary has exactly one unmarked normal. For a positive short label its PC equation is, on the positive localization, `b_(F-a)/t_a=b_F` after orientation gauge. This is equivalent to the polynomial positive-sheet equation because the positive branch is a domain and the retained Rees parameter is nonzero. The opposite sheet imposes no equation in either model. Long-normal localization is injective and gives the same long equation.

Thus the top kernels and their generic projection images agree in the absolute and PC models. Both the annihilator and the top ambiguity module computed above are unchanged. This argument does **not** claim that the whole finite-to-PC map is a quasi-isomorphism, and it does not rely on localization being injective on the entire glued ring.

## 8. Conductor symbols and a separate supported-pair control

At the ordinary conductor, every short occurrence is zero and the eighteen-term vector `beta` becomes zero. Before forgetting its first conductor grade, write

\[
\beta=\sum_{s\in S}X_s\beta_s,\qquad
\operatorname{gr}^1_I\beta=\sum_{s\in S}[X_s]\otimes\beta_s.
\]

In words: each coefficient direction has an explicit three-term first symbol in the **absolute** conductor target. This tensor defines a map from the dual conormal module; it is not an identification of a coordinate with its normal dual.

All six `beta_s` are closed. The coefficient of the singleton state `[s,empty]` in `beta_s` is `U_L`. No boundary into that state exists in the conductor-specialized boundary complex: its only possible top predecessor has coefficient `u_s`, which is zero there. These six separate detectors prove that the six symbol classes are nonzero and independent over the retained spectator ring.

If the independent normal `u03` is next set to zero, four of these specified symbols remain nonzero and two become zero. The surviving ones are exactly those for short labels compatible with `03`; each has an explicit one-term detector. This does not evaluate the `u03` normal line or identify it with `dX03`.

Ordinary conductor restriction of a PC summand already inverting a short normal is zero. The preceding symbol calculation is therefore not a claim that ordinary restriction and PC support-duality have interchangeable outputs. It is a calculation before that change of variance, consistent with Branch C's distinction between scalar specialization and conormal-symbol evaluation.

For an additional check **in the finite absolute target only**, impose `t04=t35=0` before conductor restriction and before long resonance. Each polynomial sheet then has one short singleton whose normal coefficient is zero but whose occurrence is nonzero. The positive and negative singleton equations force `k_plus=k_minus=0`. Therefore the image of the top generic projection is zero, and the specialized connecting map is injective on the entire generic line. Its cyclic class has zero annihilator.

This last statement is not asserted for the PC complex after the same specialization: localizations at those zero normal coefficients are then zero modules and must be recomputed. Nor is it a statement about the value of Branch A's dual Gysin on the native class. It is a controlled test showing that the supported pair alone cannot be treated as an ordinary finite-target annihilation of our generic obstruction.

## 9. Verification and provenance

Run:

```sh
python check_marici_q_alternating_rees_base_change.py \
  --output marici_q_alternating_rees_base_change_certificate.json
```

The standalone standard-library checker passes **114,594 exact assertions**. It reconstructs all 215 source states and their quotients; checks polynomial and PC differentials, actual localization zero rings, and all finite-to-PC squares; constructs the seven full lifts and supported annihilation homotopies; verifies the twelve labelled boundary-ideal families and their branch-module syzygies; and checks all six dihedral actions.

The independent fine-degree control covers all fifteen legal short-occurrence support types and all sixty-four short Rees support types: **960 cases**. In each case it solves the complete integral top kernel by signed unit-incidence constraints, not by numerical rank sampling. The answer agrees with both the lifting ideal and the twelve-family ambiguity formula. It also verifies the six first-symbol detectors and the explicitly scoped pair/resonance controls.

The arbitrary-degree theorem is proved by the polynomial sheet divisibility and gluing argument above. No exponent truncation is used as a quotient ring. The finite support tests are independent checks of those formulas, not a substitute for their proof. There is no proof-assistant claim.

The preceding independent-base checker was rerun and passed **11,083** exact assertions. Its theorem remains valid over its original ring; it must not be used unchanged after the nonflat source substitution.

### Primary repository inputs

- Entry 93, `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: actual alternating fibre product and branch/conductor ideals.
- Entry 115, `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`, blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`: the independent labelled Rees normal coefficient and connecting-degree distinction.
- `research/voevodsky/check_ringed_alexandrov_pc_target.py`, blob `7c993d05837fbe2ba29ba30e5b665b5429ab940b`: full loaded target, incidence signs, and specified PC rings/differentials.
- Entry 143, `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md`: complete endpoint support, seven-state Q quotient, and separate target-side PC realization.
- Previous artifact `filtered_q_comparison.md` and its checker: the honest support triangle and correct subdivision map, including mixed flags.

### Branch artifacts used

- `supported_gysin_proof.md`, saved 2026-09-07 01:16 UTC: Branch A's ordered pair Gysin and native non-lift distinctions.
- `proof.md`, saved 2026-09-07 15:21 UTC, internal heading *Source admissibility of the proposed conductor–Morse primitive*: the latest source-unit/Morse-boundary correction and the normalization ring.
- `source_admissible_overlap.md` and `gysin_normal_comparison.md`: Branch C's source-locality, retained-factor, and conormal-symbol scope.
- `equivariant_physical_lift.md`: strict versus coherent endpoint lifting; no order-two/order-three splitting obstruction is mistaken here for failure of a full coherent state.

### Mathematical framework

- Stacks Project, Section 15.60, tag `06XY`, especially Lemma 15.60.7: bounded free complexes compute derived coefficient change.
- Stacks Project, Section 13.9, tag `014D`: cones and degreewise split short exact sequences of complexes.

### What is still not identified

The new objects are a derived coefficient change of the fixed **215-state target**. They are not a reconstruction of Branch A's native 245-state normalization source. The top generic class is not renamed as the Entry-436 endpoint unit or the exact Morse roof. The actual physical source must supply a compatible connecting class and map it to this target obstruction with its endpoint, normal-line, and filtration data retained. This computation provides a sharper target for that comparison; it does not declare the comparison proved.
