# The joint normalization dual, its conductor class, and the endpoint Gysin test

Date: 2026-09-07  
Project: Marici  
Source repository: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result and scope

The actual normalization source supplies a joint derived-dual object with two branch classes in degree three and a conductor class in degree five. The conductor class is not an independently appended regular codimension-five Gysin class: it is the transgression of the codimension-six conductor, with all six occurrence determinant factors retained.

Both source-sheet maps and the homotopy coupling them are constructed on complete polynomial resolutions. This supplies a concrete source-side comparison datum, rather than another scalar signature. The corresponding normalization gluing class has a literal open-cover Cech representative. Its derived evaluation against the degree-five dual class is the primitive sixfold residue. The reflection comparison is fixed by the conductor unit.

The previous fivefold occurrence-Gysin construction passes a different test on its ambient Koszul source. Pulling that complete construction back along the natural map from the normalization node to its single-sheet coordinate axis gives a nonzero supported morphism, but **zero support counit and zero derived conductor specialization**. This holds in all six transported charts. Its ambient endpoint unit is not inherited by the actual node source along that map.

This is an exact calculation of the normalization source and its ambient polynomial derived dual. It does not identify these source-side comparison cells with the already constructed spatial endpoint collar operators in the support-PC target. It neither selects physical reflection parity nor claims the full supported-Verdier/logarithmic correspondence.

## 2. The source is the supplied normalization node

Let the spectator base be a polynomial ring over the integers; its variables, including the long occurrences, are suppressed below. Write

\[
A=R[X_0,X_1,X_2,X_3,X_4,X_5],\qquad
E=\{0,2,4\},\qquad O=\{1,3,5\}.
\]

In words: the six short occurrences remain independent polynomial coordinates. Neither the normal parameters nor the external Rees parameters are renamed as these coordinates.

Put

\[
I_E=(X_0,X_2,X_4),\quad I_O=(X_1,X_3,X_5),\quad
\mathfrak m=I_E+I_O,
\]

\[
B=A/(I_EI_O),\qquad B_+=A/I_E,\qquad B_-=A/I_O,\qquad C=A/\mathfrak m.
\]

In words: the plus normalization sheet carries the odd coordinates, the minus sheet carries the even coordinates, and the conductor is their common zero section. In particular, the ideal defining the plus sheet in the ambient space is the even ideal; its own conductor ideal is the odd ideal. These must not be interchanged.

The source [S1] supplies the exact sequence

\[
0\longrightarrow B\longrightarrow B_+\oplus B_-
\xrightarrow{\varepsilon_+-\varepsilon_-}C\longrightarrow0.
\]

In words: two branch functions come from the node exactly when their constant conductor values agree. There is no chosen splitting and no division by two.

All constructions below are over this sequence. Inverses appear only in explicitly named output Cech modules. The supplied spatial target's coefficient domains are unchanged.

## 3. An explicit finite free resolution of the node

Order the even and odd triples increasingly, with combined wedge order

\[
(0,2,4,1,3,5).
\]

In words: this fixes every determinant and residue sign in the calculation.

The node resolution has one degree-zero generator and, in positive degree, generators indexed by two nonempty subsets:

\[
P_0=A,\qquad
P_n=\bigoplus_{\substack{\varnothing\ne U\subseteq E,\ \varnothing\ne V\subseteq O\\
|U|+|V|=n+1}}A\,p_{U,V}.
\]

In words: it resolves the mixed-product ideal using the tensor product of the two positive Koszul resolutions, followed by its inclusion in the ambient ring.

The ranks in degrees zero through five are

\[
(1,9,18,15,6,1).
\]

In words: the complete resolution has fifty generators. It is not a one-line replacement of the source.

For singleton subsets the differential is

\[
dp_{\{e\},\{o\}}=X_eX_o.
\]

In words: the first differential is the actual mixed-product ideal defining the node.

In all higher degrees,

\[
\begin{aligned}
dp_{U,V}={}&
\sum_{\substack{e\in U\\ |U|>1}}
(-1)^{\operatorname{pos}_U(e)}X_e\,p_{U\setminus\{e\},V}\\
&+\sum_{\substack{o\in V\\ |V|>1}}
(-1)^{|U|-1+\operatorname{pos}_V(o)}X_o\,p_{U,V\setminus\{o\}}.
\end{aligned}
\]

In words: the two ideal resolutions retain their ordered tensor differential. Positions begin at zero. The signs and polynomial coefficients give a square-zero differential.

There is a direct all-polynomial exactness proof. Fix any nonnegative occurrence multidegree. If its support lies entirely on one branch, only the degree-zero quotient class remains. If it has both even and odd support, the homogeneous resolution is the augmented product of two simplex chain complexes and contracts integrally. The checker independently reduces all sixty-four support patterns with signed-unit operations. Exponent magnitudes introduce no additional incidence types. Thus this proves a resolution of the entire polynomial node, not merely a bounded-degree approximation.

## 4. Both source endpoint maps and their joint homotopy

Let

\[
K_E=K_A(X_0,X_2,X_4),\qquad
K_O=K_A(X_1,X_3,X_5),\qquad
K_6=K_A(X_0,X_2,X_4,X_1,X_3,X_5).
\]

In words: these are the ordered homological Koszul resolutions of the plus sheet, minus sheet, and conductor [M1].

The two quotient maps from the node have explicit lifts. Both send the degree-zero unit to the unit. On positive generators,

\[
f_+(p_{U,V})=
\begin{cases}X_v e_U,&V=\{v\},\\0,&|V|>1,\end{cases}
\qquad
f_-(p_{U,V})=
\begin{cases}X_u e_V,&U=\{u\},\\0,&|U|>1.\end{cases}
\]

In words: each sheet map retains its actual opposite-parity coefficient. They are full chain maps, not endpoint values assigned after taking homology.

Let the exterior inclusions into the conductor resolution be denoted by \(\iota_E,\iota_O\), and set

\[
\delta=(\iota_E,-\iota_O):K_E\oplus K_O\longrightarrow K_6.
\]

In words: the same conductor difference used in the source sequence now appears on its free resolutions.

The following degree-one map couples the two sheet maps:

\[
H(1)=0,\qquad
H(p_{U,V})=(-1)^{|U|}e_U\wedge e_V,
\]

\[
dH+Hd=\iota_Ef_+-\iota_Of_-.
\]

In words: the two composites to the conductor agree through this specified polynomial homotopy. The formula uses the full source wedges, including their highest term. No occurrence factor is inverted.

The homological normalization fibre is

\[
F_n=(K_E\oplus K_O)_n\oplus(K_6)_{n+1},
\qquad d(n,c)=(dn,\delta n-dc).
\]

In words: this is the fibre of the resolution of the actual source normalization sequence, not a cone introduced to force a physical class to vanish.

The map

\[
P\longrightarrow F,\qquad p\longmapsto(f_+(p),f_-(p),H(p))
\]

is a chain map. In words: both endpoint maps and their comparison occupy one object. The checker constructs and verifies a polynomial contraction of its 130-generator comparison cone using sixty-five unit cancellations. Hence this map is an integral homotopy equivalence of resolutions. No source class is lost by moving between the fifty-generator resolution and the eighty-generator normalization fibre.

## 5. The derived dual has a genuinely coupled conductor class

Dualizing the complete normalization sequence over \(A\) gives

\[
R\operatorname{Hom}_A(C,A)
\longrightarrow R\operatorname{Hom}_A(B_+\oplus B_-,A)
\longrightarrow R\operatorname{Hom}_A(B,A)
\longrightarrow R\operatorname{Hom}_A(C,A)[1].
\]

In words: the source dual is a cone on the two jointly signed conductor-to-sheet maps. The reversal of arrows does not identify it with a collection of independent branch residue lines [M2, M3].

Let \(L_E,L_O\) be the ordered ambient conormal determinant lines for the two triples, and let \(L_6=L_E\otimes L_O\). Then

\[
\operatorname{Ext}^3_A(B,A)
\cong B_+\otimes L_E^\vee\ \oplus\ B_-\otimes L_O^\vee,
\]

\[
\operatorname{Ext}^5_A(B,A)\cong C\otimes L_6^\vee
\]

as nonequivariant modules; all other degrees vanish. In words: two branch dualizing channels and one conductor channel survive. The conductor-difference character must also be restored in the equivariant version below.

This follows from the exact triangle and the regular Koszul resolutions. The checker additionally computes every dual homogeneous complex in all 729 negative/zero/positive threshold frames, retaining all maps over the integers. The results agree with these complete module formulas.

The degree-five conductor class is a transgression:

\[
\operatorname{Ext}^5_A(B,A)
\xrightarrow{\ \sim\ }
\operatorname{Ext}^6_A(C,A).
\]

In words: the connecting map is an isomorphism. Its determinant has **six** factors although its source cohomological degree is five.

An actual representative is

\[
\kappa=H^*(e_{E\cup O}^{\vee})=-p_{E,O}^{\vee}.
\]

In words: the top comparison wedge gives the conductor class with the source's fixed sign. Its boundaries in degree five generate exactly \(\mathfrak m\), so it is primitive and

\[
\operatorname{Ann}_A[\kappa]=\mathfrak m.
\]

In words: it is supported on the conductor as a cohomology class. This statement alone must not be confused with a separately constructed morphism into an arbitrary support functor.

### Why the dual cannot be split before comparison

Write \(\alpha\) for the first arrow of the dual triangle. On the explicit dual resolutions, it is the signed projection onto the even and odd exterior summands. After derived base change to the conductor, all Koszul differentials become zero, but the two projections remain nonzero unit matrices; in degree zero their row is

\[
\alpha^0=(1,-1).
\]

In words: the coupling is not nullhomotopic. Its two components are regular codimension-three Gysin maps, with their determinant lines intact. Equivalently, the degree-three and degree-five cohomology modules of the source dual are joined by a nonzero degree-three extension. Replacing the dual by their direct sum discards precisely this coupling.

## 6. A literal source gluing cocycle and its nonzero residue pairing

The class above has a geometric source counterpart. Cover the complement of the conductor by the six principal opens

\[
D(X_0),\ D(X_2),\ D(X_4),\ D(X_1),\ D(X_3),\ D(X_5).
\]

In words: mixed even/odd intersections are empty on the node, because every mixed product is zero. Each nonempty intersection lies on one specified normalization sheet.

In the extended Cech complex of this cover, take the degree-one cochain whose entries are one on odd opens and zero on even opens. Call it \(\lambda\). It is closed because values agree on every nonempty intersection. It is not the restriction of a node function: such a function cannot have unequal conductor constants. The normalization sequence and local cohomology give

\[
H^1_{\mathfrak m}(B)\cong C,
\qquad [\lambda]\longleftrightarrow1.
\]

In words: the source itself supplies an oriented gluing class. It is not an additional pole introduced in the original spatial target.

The other nonzero source supported cohomology is

\[
H^3_{\mathfrak m}(B)
\cong H^3_{I_O}(B_+)\oplus H^3_{I_E}(B_-).
\]

In words: both branch residue channels are retained alongside the gluing class. The complete Cech object is not replaced by these groups.

To compute the derived pairing without choosing a scalar identification, the checker lifts \(\lambda\) to the total complex of the fifty-generator resolution with the ambient six-variable Cech complex. In its unit occurrence frame this total complex has 425 generators. Its explicit cocycle \(\Lambda\) has fifty-two terms: three odd-open unit terms and one term for every mixed resolution generator.

For \(a=|U|\), \(b=|V|\), its mixed coefficient is

\[
(-1)^{1+a(a-1)/2+a-1+(b-1)(a+1)+b(b-1)/2}
\frac{p_{U,V}}{\prod_{i\in U\cup V}X_i}
\]

in the output localization indexed by \(U\cup V\). In words: every denominator belongs to its declared output Cech summand. The complete differential, including all source-resolution terms, kills this cocycle.

In particular its top-resolution coefficient is

\[
-\frac{p_{E,O}}{X_0X_2X_4X_1X_3X_5}.
\]

In words: this term cannot be omitted while keeping the cocycle closed.

Evaluation now gives the exact derived pairing

\[
\bigl\langle[\kappa],[\lambda]\bigr\rangle
=\left[\frac1{X_0X_2X_4X_1X_3X_5}\right]
\in H^6_{\mathfrak m}(A).
\]

In words: the paired value is the primitive sixfold residue in the declared order. This is nonzero and has conductor annihilator \(\mathfrak m\); it is not an ordinary scalar unit in \(A\). The checker verifies the pairing on the full resolution-Cech total complex, rather than inferring it from two rank-one groups.

### Reflection and the source comparison

Use the physical relabellings on short indices: rotation by two and reflection \(i\mapsto1-i\). Reflection exchanges the two sheets. On the source-supported cocycle,

\[
r\Lambda=\Lambda,\qquad s\Lambda+\Lambda=d(1).
\]

In words: rotation fixes it; reflection changes its sign up to the actual conductor-unit coboundary. The formula holds on all fifty-two terms, not only in cohomology.

After compensation by the sheet-orientation character, the comparisons can be written

\[
h_r=0,\qquad h_s=-1,
\qquad h_g+\chi(g)h_h-h_{gh}=0.
\]

In words: the source supplies its reflection homotopy, and all group composition equations close without a further choice. This does not assign the reflection parity of the as-yet-unidentified target connector.

For the ambient \(A\)-valued dual, the top conductor comparison has even reflection character: the six-variable determinant sign and the conductor-difference sign cancel. If one instead uses the relative dualizing object

\[
\omega_B^\bullet=R\operatorname{Hom}_A(B,\Omega^6_{A/R}[6]),
\]

its conductor cohomology is in degree minus one with the sheet-orientation character. In words: the ambient volume twist changes the character bookkeeping. These two duality conventions must not be mixed when comparing with a physical polarity line.

## 7. The fivefold Gysin candidate fails the actual source endpoint test

For any omitted short coordinate \(r\), put

\[
J_r=(X_i:i\ne r),\qquad A_r=A/J_r.
\]

In words: this is the coordinate-axis source of the previous fivefold Gysin map. The reference plus/03 calculation omitted \(X_0\).

The natural node-to-axis quotient factors through a single normalization sheet. For even \(r\) it factors through \(B_-\); for odd \(r\) through \(B_+\). On resolutions the map is exactly the appropriate \(f_-\) or \(f_+\), followed by the exterior inclusion into \(K_A(J_r)\).

Therefore this resolution map is zero above degree three. Pulling a degree-five \(A\)-valued Gysin cocycle back along it gives

\[
\operatorname{Ext}^5_A(A_r,A)
\longrightarrow\operatorname{Ext}^5_A(B,A),
\qquad [\varepsilon_{J_r}]\longmapsto0.
\]

In words: equality of the displayed cohomological degree does not identify the old fivefold class with the nonzero node conductor class. Every representative and replacement homotopy is covered by this factorization; the chosen chain representative already pulls back to zero after the support counit.

The complete supported map deserves a separate statement. The ordered Koszul-to-Cech Gysin cochain has a component on every source wedge. Composing it with the actual node-to-axis resolution map gives a nonzero degree-five cochain \(\mu_r\) into the output \(\mathcal C_{J_r}\). Its top supported value on the node unit is a primitive fivefold pole, so this supported morphism is not null.

But all its nonzero output components have Cech degree at least two. It has **no empty-localization component**. Consequently,

\[
\mathcal C_{J_r}\longrightarrow A
\quad\Longrightarrow\quad \mu_r\longmapsto0,
\qquad
\mu_r\otimes_A^LC=0.
\]

In words: its support counit is strictly zero, and after derived conductor base change every remaining localized output disappears. This is checked on all unreduced source columns in all six charts.

This is compatible with the previous result: the ambient five-normal Koszul source has a top input whose Gysin image is the bottom coefficient one. The actual node-to-axis map has no such degree-five input component. The old ambient primitive endpoint value therefore does not transfer through this natural source map.

There is also an internal-degree obstruction to identifying the two classes:

\[
\deg\varepsilon_{J_r}=-\sum_{i\ne r}e_i,
\qquad
\deg\kappa=-\sum_{i=0}^5e_i.
\]

In words: the conductor class retains the missing sixth occurrence line. Its five cohomological degrees come from a normalization transgression, not a regular five-coordinate immersion. A polynomial scalar cannot supply the missing negative occurrence degree.

## 8. Relation to the two spatial endpoint collars

The source endpoint comparison data are now explicit: the two complete sheet resolution maps, their joint homotopy \(H\), the two nonzero Gysin components in the dual triangle, and the conductor-unit reflection comparison. The source-defined labels remain those of the odd and even physical endpoints [S2].

This is more information than the earlier two endpoint scalar values, but it is still not a proof that the spatial collar operators realize these maps. In particular, the weighted spatial collars carry the coefficients

\[
w_+=X_1X_3X_5,\qquad w_-=X_0X_2X_4.
\]

In words: their primitive occurrence frames are not units in the source coefficient ring. Both products annihilate the conductor dual class. The checker constructs their polynomial nullhomotopies using the existing degree-four source rows. A direct multiplication/evaluation using these products cannot be called a primitive transport of \(\kappa\); a determinant-line and degree comparison is required.

The independent excess \(\eta\) may be retained by tensoring all the constructed maps and homotopies with its exterior factor. The checker verifies both tensor channels. This neither replaces it by an internal normal multiplier nor proves that its physical image is the conductor class. Similarly, changes of Rees coefficients cannot turn the strictly zero support-counit pullback above into a nonzero map; the full Rees/source comparison would have to use a different specified morphism.

The concrete next comparison is now between two complete diagrams: this non-split source normalization-dual triangle and the complementary-support cubical target diagram, with the two framed endpoint maps and the actual generic pairing. It must carry the source gluing homotopy, not factor through one normalized branch, and it must account for the six-factor determinant. No target physical parity is selected by identifying the signs in one isolated coefficient channel.

## 9. Reproduction and provenance

Run:

```sh
python check_marici_joint_conductor_dual_endpoints.py \
  --output marici_joint_conductor_dual_endpoints_certificate.json
```

The new self-contained checker passes **13,203 exact checks**. It constructs all fifty node-resolution generators, the eighty-generator normalization fibre, both endpoint maps, their full homotopy, an explicit contraction of the comparison cone, all sixty-four polynomial support patterns, all 729 dual threshold frames, all six group actions, all six complete supported fivefold Gysin pullbacks, the 425-column supported total complex, its fifty-two-term gluing cocycle, and the primitive sixfold pairing. No cancellation pivots other than integer units are used. Polynomial exponents outside the finite threshold audit are covered by the support and regular-sequence proofs.

The preceding `check_marici_occurrence_support_conductor_trace.py` was also rerun in the active environment and passed its 35,051 assertions. This continuation distinguishes a new node-source pullback from that earlier ambient/source-square calculation; it does not revoke the latter's scoped chain identities.

This is executable exact arithmetic with accompanying algebraic proofs, not proof-assistant verification. No repository files were modified.

### Source records

[S1] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: the actual two-sheet node, branch maps, conductor and difference sign.

[S2] `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: the labelled closed-conductor endpoints and the distinction between their carrier identification and a full ringed endpoint correspondence.

Prior local inputs: `marici_occurrence_support_conductor_trace.md`, `marici_cubical_supported_dual_kernel.md`, and `log_endpoint_completion.md`. Their target coefficient-domain and physical-scope qualifications remain in force.

[M1] Stacks Project, *The Koszul complex*, tag `0621`, especially functoriality, tensor products and the multiplication nullhomotopy.

[M2] Stacks Project, *Cones and termwise split sequences*, tag `014D`.

[M3] Stacks Project, *Hom complexes*, tag `0A8H`.

[M4] Stacks Project, *Local cohomology*, tag `0952`: the flat extended Cech model and derived support operations.
