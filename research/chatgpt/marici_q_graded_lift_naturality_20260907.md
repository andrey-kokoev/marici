# Graded Q lifts: the coefficient-linearity obstruction

Date: 2026-09-07  
Lane: the 215-state filtered target and its generic-Q lifting problem  
Repository input: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result

The seven minimal homogeneous generic multiples have unique lifts in their own fine degrees. Those lifts extend to an explicit graded, dihedrally compatible family **linear over the spectator ring**. They cannot extend to a family linear over the full alternating-sheet coefficient ring, even if grading and symmetry requirements are dropped.

The precise obstruction is the non-split extension

\[
0\longrightarrow M\longrightarrow H_3(E)\xrightarrow{\rho}\mathfrak a\longrightarrow0,
\qquad
\mathfrak e\in\operatorname{Ext}^1_{\mathcal B}(\mathfrak a,M).
\]

In words: the ambiguity module is part of the lifting module's extension structure, not merely a collection of freely removable choices. The projection records the coefficient of the generic class. The class of this exact sequence measures whether the individual lifts can be selected coefficient-linearly.

The new exact annihilator is

\[
\operatorname{Ann}_{\mathcal B}(\mathfrak e)
=I_++I_-+(\tau_+\tau_-),
\qquad
\mathcal B\mathfrak e\cong\mathcal C/(\tau_+\tau_-).
\]

In words: this **second**, coefficient-naturality obstruction is supported at the conductor and retains the product of the six Rees parameters. It has infinite additive order over the integers. It is not the earlier connecting class and is not an order-two or order-three torsion class.

Six explicit nonzero relation defects, each a 24-term top boundary cycle, represent this obstruction. A complete presentation of the lifting module has 43 generators and 174 relations. This is a presentation of the existing target's homology, not 43 new physical states or newly adjoined carrier cells.

All assertions here are about the fixed target. No identification with Branch A's native normalization/Morse source, the Entry-436 endpoint unit, or a complete mixed-variance physical functor is made.

## 1. Fixed coefficients, support, and grading

Use the labelled short and long sets

\[
S_+=\{13,35,15\},\qquad S_-=\{02,24,04\},\qquad
S=S_+\sqcup S_-,\qquad L=\{03,14,25\}.
\]

In words: the two short sets are the alternating endpoint triangulations; the long labels are the three physical long diagonals. They are not identified by a scalar symmetry quotient.

Keep the spectator ring and alternating normalization algebra

\[
\mathcal C=\mathbb Z[t_s\ (s\in S),X_l,u_l\ (l\in L)],
\qquad
\mathcal B=\mathcal C[X_s\mid s\in S]/(X_pX_m\mid p\in S_+,m\in S_-).
\]

In words: all six short Rees parameters and all long occurrence/normal parameters stay independent. A monomial with occurrences from both sheets is zero. Coefficients have the unique common-conductor, positive-branch, and negative-branch decomposition supplied by the normalization fibre product.

Set

\[
I_+=(X_p\mid p\in S_+),\qquad I_-=(X_m\mid m\in S_-),\qquad I=I_+\oplus I_-,
\qquad \tau_+=\prod_{p\in S_+}t_p,\qquad \tau_-=\prod_{m\in S_-}t_m.
\]

In words: these are the branch ideals and their three-factor Rees products. The normal coefficients of short labels are the actual products of the corresponding occurrence and Rees parameters.

The full loaded target consists of all noncrossing faces and their marked subsets. A generator and its differential have the conventions

\[
|[F,H]|=3-|F|+|H|,
\]

\[
d[F,H]=\sum_{a}(-1)^{\#\{b\in F:b<a\}}X_a[F\cup\{a\},H]
 +\sum_{h\in H}(-1)^{3-|F|+\operatorname{pos}_H(h)}u_h[F,H\setminus\{h\}],
\qquad u_s=t_sX_s\quad(s\in S).
\]

In words: add an allowed diagonal with its occurrence coefficient, or remove a mark with its normal coefficient. The first sum runs only over compatible additions. Positions start at zero. No occurrence variable or Rees parameter is inverted in this absolute calculation.

The actual support filtration gives

\[
0\longrightarrow A_\partial=F_B/F_V\longrightarrow E=F_K/F_V
\longrightarrow Q=F_K/F_B\longrightarrow0.
\]

In words: retain the full target, short boundary, and both endpoint cubes before taking the indicated quotients. There are 215 source states before quotienting. The degree-zero through degree-three ranks of the last three complexes are respectively

\[
(12,57,84,39),\qquad (12,57,87,43),\qquad (0,0,3,4).
\]

In words: this is the previously constructed honest support triangle, not the invalid erasure of mixed barycentric flags. There are no chain groups above homological degree three.

For the fine grading, give a coefficient monomial its usual exponent vector and give a cell the weight

\[
w(F,H)=-\sum_{a\in F}\mathbf e_{X_a}
 +\sum_{s\in H\cap S}(\mathbf e_{t_s}+\mathbf e_{X_s})
 +\sum_{l\in H\cap L}\mathbf e_{u_l}.
\]

In words: every term in the actual differential has the same total internal degree as its source. In top degree every face is fully marked; its short-occurrence weight is zero. Consequently positive short-occurrence order of a top coefficient is a genuine, unambiguous filtration here.

## 2. Prior lifting theorem, retained without changing source type

Put

\[
U_L=\prod_{l\in L}u_l,
\qquad
\theta=U_L[\varnothing,\varnothing]
 -\sum_{l\in L}X_l\prod_{j\in L\setminus\{l\}}u_j[\{l\},\{l\}].
\]

In words: this is the nonzero degree-three generic cycle in the seven-state quotient. It is not the corrected degree-one Morse roof, which is exact in its own honest quotient.

The preceding proof gives

\[
H_3(Q)=\mathcal B\theta,
\qquad
\operatorname{im}\!\left(H_3(E)\longrightarrow H_3(Q)\right)=\mathfrak a\theta,
\qquad
\mathfrak a=(g_0,g_{+,p},g_{-,m}),
\]

\[
g_0=\tau_+\tau_-,\qquad g_{+,p}=\tau_+X_p,\qquad g_{-,m}=\tau_-X_m.
\]

In words: there are seven minimal homogeneous generators of the lifting ideal. A generic multiple lifts precisely when its coefficient is in that ideal.

For reference, the proof reduces a top cycle to coefficients on fully marked faces. After the orientation gauge, the equations are

\[
u_a b_F=X_a b_{F\setminus\{a\}}.
\]

In words: the normal factor on a face matches the occurrence factor on its predecessor. On each polynomial sheet, the singleton equations force divisibility by that sheet's three independent Rees parameters. The common conductor value must be divisible by both products. These conditions are equivalent to membership in the displayed ideal; the following full cycles prove sufficiency.

The common lift is

\[
\Lambda_0=\sum_F(-1)^{|F|(|F|+1)/2}
\left(\prod_{s\in S\setminus F}t_s\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L\setminus F}u_l\right)[F,F].
\]

In words: sum the actual noncrossing faces with their original coefficient factors. Its full version includes both endpoints; its class in this note is taken in the endpoint quotient.

For one sheet define, for an element of its branch ideal,

\[
\Lambda_+(f)=f\sum_{F\subseteq S_+\cup L}(-1)^{|F|(|F|+1)/2}
\left(\prod_{p\in S_+\setminus F}t_p\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L\setminus F}u_l\right)[F,F],\qquad f\in I_+,
\]

and define the negative version with the opposite sheet. In words: only actual noncrossing faces are included. The branch-ideal coefficient kills outgoing opposite-sheet terms by the source ring relation. The bare sum without that coefficient is not asserted to be a cycle over the glued ring.

Write the six minimal lifts as the values at their branch occurrences. Direct calculation gives

\[
\rho(\Lambda_0)=g_0,\qquad \rho(\Lambda_+(X_p))=g_{+,p},\qquad
\rho(\Lambda_-(X_m))=g_{-,m}.
\]

In words: these are lifts inside the original target, not chosen formal symbols with stipulated boundaries.

The ambiguity module is

\[
M=H_3(A_\partial)=
\bigoplus_{\varnothing\ne N\subsetneq S_-} I_+\Gamma_{+,N}
\oplus
\bigoplus_{\varnothing\ne N\subsetneq S_+} I_-\Gamma_{-,N}.
\]

In words: each inactive nonempty proper subset labels a different family. There are six on each sheet. The summands are ideals, not free copies of the entire alternating ring.

For completeness, write \(a\sim n\) when two diagonals do not cross. If the active sheet is positive, define the compatible short and long extensions of an inactive subset by

\[
P_N=\{p\in S_+:\forall n\in N,\ p\sim n\},\qquad
L_N=\{l\in L:\forall n\in N,\ l\sim n\}.
\]

In words: retain the labels compatible with all of the fixed inactive marks. The symbolic generator is

\[
\Gamma_{+,N}=\sum_{N\subseteq F\subseteq N\cup P_N\cup L_N}
(-1)^{|F|(|F|+1)/2}
\left(\prod_{p\in P_N\setminus F}t_p\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L_N\setminus F}u_l\right)[F,F].
\]

In words: the formula is used after multiplication by a coefficient from the positive branch ideal. The reflected formula gives the other sheet. Top recurrences preserve the inactive subset, and their active equations force precisely these coefficients, up to the branch-ideal parameter. This also proves independence of the twelve summands.

## 3. What the grading actually accomplishes

The new computation independently solves the complete integral top equations in the minimum degree of each of the seven lifting generators. Each kernel has rank one and the generic coefficient fixes it. Thus each minimum-degree lift is unique.

A coefficient in the lifting ideal has a unique normal form

\[
k=g_0c+\tau_+f_++\tau_-f_-,\qquad c\in\mathcal C,\quad f_+\in I_+,\quad f_-\in I_-.
\]

In words: first separate the common conductor coefficient, then the two zero-constant branch parts. The factors shown exist because membership in the lifting ideal has already been proved. This is a decomposition of a module, not localization of the ambient coefficient ring.

It supplies an explicit section

\[
s_{\mathcal C}(k)=c\Lambda_0+\Lambda_+(f_+)+\Lambda_-(f_-),
\qquad \rho s_{\mathcal C}=1_{\mathfrak a}.
\]

In words: the spectator-linear family exists. It preserves every internal degree and commutes with the source's six semilinear dihedral actions. It uses the named branch labels and no averaging.

However, multiplication by a short occurrence leaves the common-conductor sector and exposes a different requirement. For a positive label,

\[
X_p s_{\mathcal C}(k)-s_{\mathcal C}(X_p k)=c\,\mathscr D_{+,p},
\qquad
\mathscr D_{+,p}=X_p\Lambda_0-\tau_-\Lambda_+(X_p).
\]

In words: the failure to commute with a coefficient multiplication is exactly the common coefficient times an explicit boundary-supported top cycle. The analogous negative defect has the opposite Rees product.

This is not a failure of group equivariance. Multiplication is a noninvertible coefficient operation inside a ringed diagram; it is not being reclassified as an invertible transport. The problem is full coefficient linearity.

## 4. Compute all six relation defects

The generic coefficients obey

\[
X_p g_0=\tau_-g_{+,p},\qquad X_mg_0=\tau_+g_{-,m}.
\]

In words: two orders of coefficient multiplication reach the same generic multiple. A coefficient-linear family must make their lifts equal, or homotopic in the required target.

The defects of the chosen lifts are genuine cycles, have zero generic projection, and have no endpoint coordinates in the quotient. For the positive side they decompose as

\[
\mathscr D_{+,p}=\sum_{\varnothing\ne N\subsetneq S_-}
 c_{+,N}\,X_p\Gamma_{+,N},
\]

\[
c_{+,N}=
\left(\prod_{m\in S_-\setminus N}t_m\right)
\left(\prod_{q\in S_+\setminus P_N}t_q\right)
\left(\prod_{l\in L\setminus L_N}u_l\right).
\]

In words: each of the six inactive-subset families appears. There are 24 actual fully marked face terms, not just a formal nonzero label. The reflected formulas supply the negative defects.

A concrete coefficient is

\[
\operatorname{coeff}_{[\{02\},\{02\}]}(\mathscr D_{+,13})
=-X_{13}\tau_+t_{24}t_{04}U_L.
\]

In words: its opposite-sheet Rees factor lacks the parameter for label 02. It cannot be a multiple of the full negative Rees product. The coefficient is already of first positive occurrence order.

In the common-to-branch relation degree, the exact top kernel has rank seven: one generic direction and six boundary directions. These are the ambiguities excluded in the smaller generator degrees but restored by coefficient multiplication. This explains why seven separate rigidity checks do not prove naturality.

## 5. The defect cannot be removed by different lifts

Let arbitrary lifts differ from the displayed ones by elements of the full ambiguity module. A positive relation defect changes by

\[
\mathscr D'_{+,p}-\mathscr D_{+,p}=X_p m_0-\tau_-m_p,
\qquad m_0,m_p\in M.
\]

In words: this describes every possible change, including nonhomogeneous and nonequivariant ones. It is not a bounded ansatz for corrections.

Pass to the explicitly defined quotient

\[
\overline M_+=M/(IM+\tau_-M).
\]

In words: keep first branch-conductor order and reduce by the opposite sheet's Rees product. The first correction has an extra occurrence factor and the second has the entire opposite Rees product. Both vanish in this quotient.

The defect class remains nonzero. In the labelled summands, the annihilator of its individual coefficient is the ideal generated by the product of the missing inactive parameters:

\[
((\tau_-):c_{+,N})=\left(\prod_{n\in N}t_n\right),
\qquad
\bigcap_{\varnothing\ne N\subsetneq S_-}
\left(\prod_{n\in N}t_n\right)=(\tau_-).
\]

In words: the independent spectator ring is a polynomial domain, so these are ordinary monomial divisibility identities. In particular the complete positive defect symbol has exact annihilator the negative Rees product. The reflected defect has exact annihilator the positive product.

Consequently no alteration of the lifts can make all coefficient relations commute. The exact sequence defining the lifting module does not split as a sequence of modules over the alternating ring. Forgetting the grading or forgetting the dihedral action cannot help, because neither was assumed in this proof.

This is an argument with the first conormal symbol, not ordinary conductor evaluation: setting all short occurrences to zero makes the displayed vector zero but loses the symbol that detects the defect. It does not replace a Rees coordinate or a conormal line by one.

## 6. Exact module presentation and extension class

Let a free module have one basis vector for the common generator and one for each of the six branch generators. A complete set of relations for its surjection onto the lifting ideal consists of the following types:

\[
X_p e_0-\tau_-e_{+,p},\qquad X_m e_0-\tau_+e_{-,m},
\]

\[
X_q e_{+,p}-X_p e_{+,q},\qquad X_n e_{-,m}-X_m e_{-,n},
\]

\[
X_m e_{+,p},\qquad X_p e_{-,m}.
\]

In words: six common-to-branch relations, six same-sheet Koszul relations, and eighteen opposite-sheet annihilator relations give thirty generators of the relation module.

To prove completeness, take any relation. Its coefficient on the common generator has zero conductor value, since the common Rees product is a non-zero-divisor on the spectator ring. Express that coefficient in the two branch ideals, and use the first six relations to eliminate it. Opposite-sheet coefficient parts of each remaining branch generator are covered by the annihilator relations. On a single polynomial sheet, the remaining relation is a syzygy of its three independent occurrence variables and is generated by their Koszul relations. This handles every polynomial degree.

Mapping the free generators to their actual lifts sends the last twenty-four relations to zero and the first six to the defects computed above. This represents the extension class by the standard free-presentation construction of Ext. Changing the lifts adds the restriction of a homomorphism from the free generator module into the ambiguity module. The preceding quotient detects the class modulo every such change. References [M1] and [M2] give the extension and splitting conventions.

Each of the twelve ambiguity summands has three branch-ideal generators, three Koszul relations, and nine opposite-sheet annihilator relations. Combining their 36 generators and 144 relations with the seven lifts gives 43 generators. Add the 24 zero ideal relations and the six common-to-branch relations **with their computed ambiguity terms subtracted**. The result is a 174-relation presentation of the full lifting module.

Completeness follows also directly from the extension: every top cycle is a sum of a lift of its generic ideal coefficient and an ambiguity element. Any relation among those generators projects to one of the thirty ideal relations; subtract its displayed lifted relation and the remainder is precisely a relation internal to the ambiguity module.

The certificate exports all 43 actual target vectors and all 174 relations. Every relation is checked as an exact zero in the original target, not only in an abstract quotient presentation.

## 7. Exact annihilator of the second obstruction

The first-symbol argument determines a necessary condition for any coefficient to kill the extension class. If that coefficient is denoted by the letter below, its conductor value must kill every positive and negative defect symbol:

\[
b\mathfrak e=0\quad\Longrightarrow\quad
\epsilon(b)\in(\tau_-)\cap(\tau_+)=(\tau_+\tau_-),
\]

\[
\operatorname{Ann}_{\mathcal B}(\mathfrak e)\subseteq I+(\tau_+\tau_-).
\]

In words: the branch ideal acts trivially on the first-symbol quotient. The two independent Rees products must both divide the conductor value. This is necessity for the full extension class, not only for its selected representative.

There are explicit corrections proving the reverse inclusion. Let the relation-image map from the free presentation be denoted by the letter below. For a positive or negative short occurrence, define a map from the seven free generators into the ambiguity module by sending the common generator to its corresponding defect and the other six to zero:

\[
f_s(e_0)=\mathscr D_s,\qquad f_s(e_j)=0\ (j\ne0),
\qquad f_s|_{\ker(F\to\mathfrak a)}=X_s\kappa.
\]

In words: the identity follows from same-sheet proportionality of the defects and the vanishing of opposite-sheet products. All thirty source relations are verified. Thus every short occurrence annihilates the extension class.

For the common Rees product use

\[
f_0(e_0)=0,\qquad
f_0(e_{+,p})=-\tau_+\mathscr D_{+,p},\qquad
f_0(e_{-,m})=-\tau_-\mathscr D_{-,m},
\qquad f_0|_{\ker(F\to\mathfrak a)}=(\tau_+\tau_-)\kappa.
\]

In words: this supplies the other annihilator generator. Equivalently, multiplication by the common product has the coefficient-linear lift obtained by multiplying an arbitrary ideal element by the full common cycle. No inverse coefficient is used.

Therefore

\[
\operatorname{Ann}_{\mathcal B}(\mathfrak e)=I+(\tau_+\tau_-),
\qquad
\mathcal B\mathfrak e\cong\mathcal B/(I,\tau_+\tau_-)
\cong\mathcal C/(\tau_+\tau_-).
\]

In words: the precise cyclic obstruction module is supported on the conductor and on the six-factor Rees divisor. This computes the cyclic submodule generated by the class, not the whole Ext group.

The quotient has no nonzero integer torsion. Hence the extension class has infinite additive order over the integers and remains nonzero over the rationals. Repeating the same polynomial argument over any field gives a nonzero extension class there as well. Dividing by two, by three, or by a group order cannot repair this coefficient-linearity failure. Inverting the six Rees factors would change the problem and remove this particular obstruction, but that localization is not admitted by the absolute source under study.

The primary and secondary results must be kept distinct:

\[
\operatorname{Ann}[\beta]=
(\tau_+\tau_-,\tau_+I_+,\tau_-I_-),
\qquad
\operatorname{Ann}(\mathfrak e)=
(I_+,I_-,\tau_+\tau_-).
\]

In words: the first tests existence of a lift of an individual generic multiple. The second tests selection of all already liftable multiples by one coefficient-linear family. A coefficient killing the second class need not kill the first.

## 8. The precisely specified infinity-groupoid

The top cycle defines a coefficient-linear map from the lifting ideal, placed in homological degree three, into the generic quotient. Denote that map by the symbol below and define its derived lifting space:

\[
\iota:\mathfrak a[3]\longrightarrow Q,\qquad \iota(k)=k\theta,
\]

\[
\mathscr L_{\mathfrak a}
=\operatorname{hofib}_{\iota}
\left(
\operatorname{Map}_{D_\infty(\mathcal B)}(\mathfrak a[3],E)
\longrightarrow
\operatorname{Map}_{D_\infty(\mathcal B)}(\mathfrak a[3],Q)
\right).
\]

In words: this is the infinity-groupoid of coefficient-linear lifts of the entire admissible generic ideal, together with the required comparison homotopy. It is not the space of one fixed coefficient marking.

Any object would induce on third homology a section of the non-split lifting-module sequence. Therefore

\[
\mathscr L_{\mathfrak a}=\varnothing.
\]

In words: higher comparison paths cannot remove this obstruction. For the six displayed top-cycle defects the elementary reason is already visible: their classes are nonzero, and the target has no degree-four boundaries. Changing to a derived presentation of the source cannot evade the induced map on homology.

This conclusion does **not** assert that Marici's full physical moduli problem is empty. The tested source is the module of generic coefficients alone, placed in one degree. A physical source may retain boundary data and a different filtered differential, or use a separately constructed support-changing comparison. Such data cannot be inferred from seven separately normalized lifts.

The new presentation provides a precise test for that source: after the required typing and shifts have been established, its common-to-branch coefficient relation must account for the displayed boundary defect, rather than silently treating it as zero.

## 9. Transport, PC scope, and other branches

The six source dihedral transformations permute the seven lifts, twelve ambiguity summands, and six defects with their actual labels. The common lift is fixed. The spectator-linear section is semilinearly equivariant. Every identity was tested on the actual target and its polynomial coefficient action, without a group-order denominator. A polarity convention consistently twisting all terms does not eliminate an underlying non-split coefficient sequence.

All top generators are fully marked, so their coefficient rings in the specified target-side PC realization are still the alternating ring. The previous top-kernel comparison and the new direct PC cycle checks preserve these same top modules and their extension. This does not assert a quasi-isomorphism of the entire finite and PC complexes in lower degrees.

The native source corrections from the other branches remain in force. The exact Morse cycle is not identified with the nonzero endpoint unit. A conormal-symbol calculation is not ordinary specialization or division of a scalar multiplier by a Rees parameter. This note neither contracts a nonzero source unit nor manufactures an unprovided source-to-target map.

The diagonal coefficient relation is meaningful only within the chosen coefficient model. Extra source restrictions may narrow the domain to a spectator-linear sector, where the constructed section is valid. That is a smaller problem, not a full coefficient-linear splitting. Conversely, a source operation mixing occurrence, Rees, and support data must be constructed before conclusions can be transported to it.

## 10. Exact verification

Run the standalone checker with

```sh
python check_marici_q_lift_naturality_20260907.py \
  --output marici_q_lift_naturality_certificate_20260907.json
```

The new run passes **138,416 exact assertions**. It verifies the 215-state differential and target PC squares, seven actual lifts, all six 24-term defects and their twelve-family decomposition, their first-symbol monomial annihilators, explicit coefficients annihilating the extension class, the spectator-linear section, all 174 presentation relations, and the six source dihedral actions.

Two independent integral presentation checks are included. The 30-relation ideal presentation is checked in **6,091 fine degrees**, including mixed degrees whose coefficient-ring monomial is zero and repeated-exponent cases. The 43-generator lifting-module presentation is compared with the complete original top kernel in **996 fine degrees**. Both use integer unit pivots and saturated lattices, not finite-field rank guesses. Minimum generator degrees and common-to-branch relation degrees are checked independently.

The previous standalone alternating/Rees checker was rerun separately and again passed **114,594 exact assertions**. It verifies the input lifting ideal and ambiguity classification. Its output was not substituted for the new non-splitting proof.

The arbitrary-polynomial theorems follow from the complete module presentation, top recurrence, and first-symbol argument. Finite tests are independent controls, not extrapolation or proof-assistant verification. No repository file was modified.

## Sources and provenance

Repository sources at the pinned commit:

- `research/voevodsky/check_ringed_alexandrov_pc_target.py`, blob `7c993d05837fbe2ba29ba30e5b665b5429ab940b`: loaded cells, signs, and actual localization domains; read again during this computation.
- Entry 93, `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: alternating fibre-product algebra and conductor ideals.
- Entry 115, `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`, blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`: independent occurrence/Rees factors and their normal differential.
- Entry 143: the complete endpoint support triangle and its distinct target-side PC realization.

Previous computation, retained with its scope: `marici_filtered_q_alternating_rees_update_20260907.md` and `check_marici_q_alternating_rees_base_change.py`.

Relevant branch constraints: `proof.md`, internal title *Source admissibility of the proposed conductor–Morse primitive* (2026-09-07), and `gysin_normal_comparison.md` (2026-09-06). The former separates the endpoint unit from the exact Morse boundary; the latter separates conormal symbols from raw scalar multipliers. Neither is used as proof of a source identification absent from this note.

Mathematical references:

- [M1] Stacks Project, Section 12.6, tag `010I`, *Extensions*: extension classes and equivalence of exact sequences.
- [M2] Stacks Project, Section 10.74, tag `02HN`, proof of Lemma 10.74.1: representing an extension by a free-presentation relation map, and its splitting criterion.
- [M3] Stacks Project, Section 15.73, tag `0A8H`, *Hom complexes*: chain maps, homotopies, and their induced homology maps.

No result about RH, numerical amplitudes, or a complete global physical comparison is asserted.
