# Branch A: full conductor dualizing complex and reciprocal-excess residue evaluation

## Result and scope

The two reciprocal excess traces lift from the pair support `V(X02,X35)` to the full six-coordinate conductor support. They remain independent. The full supported Hom calculation has dimensions `(0,9,96,306)` in homological map degrees `(2,1,0,-1)`, differential ranks `(9,85)` at degrees one and zero, and a rank-two integral map-class lattice. Its cycle basis is unimodular.

The actual relative dualizing complex of the two-sheet coefficient ring has two nonzero cohomology modules: the two sheet canonical modules in cohomological degree `-3`, and a conductor module in degree `-1`. A primitive connecting morphism joins these modules. Thus this dualizing complex is neither a single orientation line nor the direct sum of its cohomology modules.

The relative coefficient residue is explicit in an ambient six-normal local-cohomology module. It is not a fraction in the already-glued ring. Five explicit source/target coefficient readings distinguish the two trace classes and their relation-only difference. They use the retained `W25` endpoint-normal state.

Dualizing the two original coherent maps gives two distinct morphisms from the dual of the ten-state interval target to `A[-2]`. This is a relative coefficient-duality construction. It does not identify an independently supplied physical tangential source with that dual target, and it does not assign the physical conductor–Morse class.

## 1. Coefficients, degrees, and retained lines

Set

\[
A=\mathbb Z[\beta,X_{03},X_{14},X_{25}],
\]

\[
\mathbf a=(X_{02},X_{04},X_{24}),\qquad
\mathbf b=(X_{13},X_{15},X_{35}),
\]

\[
S=A[\mathbf a,\mathbf b],\qquad
R=S/(a_i b_j:1\leq i,j\leq3).
\]

In words: `S` is the independent ambient polynomial ring, and `R` is the actual two-sheet normalization ring. The long occurrence coordinates and the regulator are base parameters, not residue variables.

Write

\[
I_-=(\mathbf a),\quad I_+=(\mathbf b),\quad I=I_-+I_+,
\]

\[
R_-=A[\mathbf a],\qquad R_+=A[\mathbf b],\qquad R/I=A.
\]

The source normalization sequence, with sheet order minus then plus, is

\[
0\longrightarrow R\longrightarrow R_-\oplus R_+
\xrightarrow{\epsilon_+-\epsilon_-}A\longrightarrow0.
\]

The six coefficients and their sheet assignment are inherited from ledger Entry 93. No new coefficient relation is imposed. In particular, the relation `X02*X35=0` holds in `R`, but not in `S`.

The input trace target is the complete ten-state complex

\[
T=(P_E\otimes K_R(z))\otimes\mathfrak o_{02,35}[2],
\qquad z=X_{35},
\]

where

\[
dg=X_{03}p_{03}+X_{25}p_{25},\quad
dh_{03}=\beta X_{03}p_{03},\quad
dh_{25}=\beta X_{25}p_{25},\quad dk=z.
\]

The two-native-normal orientation line `o02,35` is retained. Its degree shift is already included in `T`. It is not identified with a six-coordinate coefficient volume form. The independent physical `dX03` convention is not evaluated in this calculation.

The conductor resolution `P_A[2]` has relevant ranks `1,6,24,92`: a unit `p_A`, generators `e_i` with `de_i=X_i p_A`, the six same-sheet Koszul and eighteen mixed-sheet relations, and all ninety-two next equations. These source relations remain part of every map.

## 2. Refine coefficient support to the full conductor

For each nonempty pure-sheet subset `J` of the six short coordinates, retain the actual target localization `R_J`. Any mixed-sheet localization is zero, because its multiplicative set contains a zero product. Its nonzero term counts are `1,6,6,2`.

Let

\[
\mathcal J=\{\varnothing\}\cup
\{J:\varnothing\ne J\subseteq\{02,04,24\}\}\cup
\{J:\varnothing\ne J\subseteq\{13,15,35\}\}.
\]

Then

\[
\mathscr C_I(T)_n=
\bigoplus_{J\in\mathcal J}(T_J)_{n+|J|}.
\]

On a summand indexed by `J`, the internal differential is `(-1)^|J| d_T`. Its Čech component from `J` to `J union {a}` has sign `(-1)^pos(a,J union {a})`. The resulting complex has 150 module summands. It is not finite free over `R`.

Projection onto the three subsets `empty`, `{02}`, `{35}` gives the actual chain map

\[
\mathscr C_I(T)\longrightarrow\mathscr C_{(X_{02},X_{35})}(T).
\]

It returns the preceding thirty-summand pair-support construction exactly. It does not set the other four coordinates to zero.

### Explicit lifts

Retain

\[
\xi=h_{03}+h_{25}-\beta g.
\]

The original maps have

\[
\nu_E(e_i)=X_i\xi\quad(i=13,15,35),\qquad \nu_E(p_A)=0,
\]

and

\[
\nu_R(e_i)=X_i\xi\quad(i=13,15),\qquad
\nu_R(e_{35})=\nu_R(p_A)=0,
\]

\[
\nu_R(c_{i,35})=X_i\xi k\quad(i=13,15).
\]

All other columns are zero. Define the same comparison homotopy on each of the three positive single-coordinate opens:

\[
H_E^+(p_A)=\xi,
\]

\[
H_R^+(p_A)=\xi,\qquad H_R^+(e_{35})=\xi k.
\]

On all negative opens use zero. These formulas agree on every same-sheet double and triple overlap, so higher Čech homotopy components may be set to zero. All source-relation equations are checked, not merely the unit column.

The resulting full-support lifts have respectively eighteen and thirty polynomial terms. Projecting to pair support recovers exactly the two previously recorded lifts. Their difference retains the mixed-source-relation cocycle and its negative-sheet homotopies.

In reduced regulator grade one and occurrence-map degree zero, the complete Hom dimensions are `(0,9,96,306)`, with differential ranks `(9,85)`. The nine boundary columns and the two trace lifts form an integral cycle basis. Grade two has identical matrices after multiplication by beta. The exponents required by each state explain this stabilization for all higher grades, without a regulator-power cutoff.

There is also a categorical reason for preservation: `A[2]` is supported on the full conductor. Both local-cohomology counits induce equivalences on mapping complexes from this source. The code checks the support refinement and both concrete representatives.

## 3. The full relative dualizing complex

Fix the ambient ordered volume line

\[
\Omega_6= dX_{02}\wedge dX_{04}\wedge dX_{24}
\wedge dX_{13}\wedge dX_{15}\wedge dX_{35}.
\]

The relative dualizing object is

\[
\omega_{R/A}^{\bullet}
=R\operatorname{Hom}_S(R,S\Omega_6)[6].
\]

This convention keeps the regulator and long coordinates in the base. Since `A` is regular, this also gives a dualizing complex for `R`, with the chosen relative normalization.

### Finite ambient resolution

Let `E_-` and `E_+` be free rank-three modules with bases carrying the corresponding coordinate weights. A free `S`-resolution of `R` is

\[
P_0=S,
\qquad
P_n=\bigoplus_{i+j=n+1\atop i,j\geq1}
S\otimes\bigwedge^iE_-\otimes\bigwedge^jE_+
\quad(n\geq1).
\]

Its ranks are

\[
(1,9,18,15,6,1).
\]

The first differential sends `e_i tensor f_j` to `a_i b_j`. On a higher term, apply the ordinary Koszul differential to the first exterior factor when its size exceeds one, and `(-1)^(i-1)` times the Koszul differential to the second factor when its size exceeds one.

Exactness is not an empirical rank extrapolation. The two truncated Koszul resolutions resolve the ideals of the two disjoint polynomial triples. Tensoring them over `A` is exact because the ideals have explicit free `A`-module monomial bases. Their tensor identifies with their product ideal in `S`. Augment that ideal into `S` to obtain the displayed resolution.

Dualizing this entire resolution gives a fifty-summand finite free **ambient-S** model for the underlying dualizing object. It is not fifty free `R`-modules; the `R`-structure is the derived one inherited from `RHom_S(R,-)`.

### Cohomology and nontrivial attachment

Dualizing the actual normalization sequence, or computing the ambient dual matrices, gives

\[
H^{-3}(\omega_{R/A}^{\bullet})
=\omega_{R_-/A}\oplus\omega_{R_+/A},
\]

\[
H^{-1}(\omega_{R/A}^{\bullet})=A,
\qquad H^j(\omega_{R/A}^{\bullet})=0\quad(j\ne-3,-1).
\]

The sheet modules retain their ordered three-form lines. They are not identified without signs with the ambient dual-normal generators.

The canonical triangle is

\[
(\omega_{R_-/A}\oplus\omega_{R_+/A})[3]
\longrightarrow\omega_{R/A}^{\bullet}
\longrightarrow A[1]
\longrightarrow
(\omega_{R_-/A}\oplus\omega_{R_+/A})[4].
\]

The final arrow is nonzero. Resolve each normalization sheet by the Koszul complex on its killed triple. The map to the six-coordinate conductor resolution is the actual normalization difference: minus the inclusion for the negative sheet, plus the inclusion for the positive sheet. Dualize that map, keeping all determinant lines.

The checker constructs the Hodge chain isomorphism between the full six-variable Koszul resolution and its dual shifted by six. Its composition with the two dual sheet quotient maps gives primitive degree-three extension cocycles. In the exported **ambient dual-normal frames**, their coefficients are `(-1,-1)`. These raw signs include the Hodge signs; they are not the naive `(-1,+1)` of the undualized sheet difference. Translating to sheet volume forms must also use the determinant-line permutation recorded in the certificate.

Each component remains a unit modulo the corresponding active triple ideal. Therefore each is nonzero already after forgetting to `S`-modules, and the triangle cannot split as `R`-modules.

The first-order nature of all basis weights reduces the complete nonnegative multigraded cohomology calculation to sixty-four zero/positive support patterns. The code verifies every pattern and additional higher-weight controls. The exactness proof and dualized normalization triangle supply the unbounded argument.

Thus neither replacing the dualizing object by a single shifted line nor splitting off its two cohomology layers is legitimate.

## 4. Relative coefficient residues without localizing the glued ring to zero

Let

\[
\mathcal E_S=H^6_{(\mathbf a,\mathbf b)}(S\Omega_6).
\]

Its basis consists of inverse monomials

\[
\delta_{\alpha,\gamma}
=
\left[
\frac{\Omega_6}
{\prod_{i=1}^3 a_i^{\alpha_i+1}
 \prod_{j=1}^3 b_j^{\gamma_j+1}}
\right],
\qquad\alpha_i,\gamma_j\geq0.
\]

These classes belong to ambient local cohomology over `S`. They are not fractions in `R`.

Local cohomology of the full relative dualizing object is concentrated in degree zero:

\[
R\Gamma_I(\omega_{R/A}^{\bullet})\simeq\mathcal E_R,
\qquad
\mathcal E_R=\operatorname{Ann}_{\mathcal E_S}(I_-I_+).
\]

Equivalently,

\[
\mathcal E_R=\{e\in\mathcal E_S:(a_i b_j)e=0\ \forall i,j\in\{1,2,3\}\}.
\]

Its explicit basis criterion is

\[
\delta_{\alpha,\gamma}\in\mathcal E_R
\quad\Longleftrightarrow\quad
\alpha=0\ \lor\ \gamma=0.
\]

Multiplication by a coordinate lowers its dual exponent, and gives zero once the exponent would become negative. This proves the criterion for arbitrary pole orders. The code checks every exponent tuple in `{0,1,2}^6` and every one-coordinate module action as implementation controls.

The concentration statement follows directly by applying ambient top local cohomology to the finite free dualizing model. The resulting complex is `Hom_S(P,E_S)`. It is the fine-graded `A`-linear dual of the displayed free resolution. That resolution is split exact in each fine degree over `A`; therefore only `Hom_S(R,E_S)=E_R` survives. This argument avoids any unsupported claim of absolute injectivity over a nonfield base.

The relative coefficient residue is

\[
\operatorname{Res}(\delta_{0,0})=1,
\qquad
\operatorname{Res}(\delta_{\alpha,\gamma})=0
\quad((\alpha,\gamma)\ne(0,0)).
\]

It is `A`-linear. It is not `R`-linear, and it is not an unrestricted scalar map on the original trace target.

For comparison, the two sheet residue modules satisfy

\[
0\longrightarrow A
\xrightarrow{(-\delta^-_0,\delta^+_0)}
\mathcal E_-\oplus\mathcal E_+
\longrightarrow\mathcal E_R\longrightarrow0.
\]

The two constant residues become one common residue. No averaging or division by two is used. The conductor comparison supplies the relation; treating the two sheet dualizing modules as an unrelated direct sum would omit it.

The scalar local cohomology of `R` itself is different:

\[
H_I^1(R)=A,
\qquad
H_I^3(R)=H^3_{I_-}(R_-)\oplus H^3_{I_+}(R_+),
\]

with every other group zero. The class equal to one on all positive single-coordinate opens and zero on all negative single-coordinate opens generates `H_I^1(R)`. The full Čech calculation checks all `3^6` sign patterns of the occurrence weights. A weight is relevant only through negative/zero/positive status; the all-weight conclusion also follows from the source normalization exact sequence and the two regular polynomial triples.

## 5. Five resolved coefficients distinguish the two traces

Write `m24,35` for the mixed relation with boundary `X24 e35`, and `c15,35` for the Koszul relation with boundary `X15 e35-X35 e15`. The target state `h25 k` retains the opposite endpoint normal and the separate occurrence partner.

For a full supported resolved map `F`, use its unlocalized component to define

\[
\ell_E(F)=
-[X_{24}]F(e_{24})_{h_{25}}
+[X_{35}]F(e_{35})_{h_{25}}
+[X_{24}]F(m_{24,35})_{h_{25}k},
\]

\[
\ell_R(F)=
[X_{15}]F(c_{15,35})_{h_{25}k}
-[X_{24}]F(m_{24,35})_{h_{25}k}.
\]

Coefficient extraction is over the retained base `A`; in the particular occurrence-map degree and regulator grade under test the outputs are integers. Each `[X_i]` extraction is the relative residue pairing with the explicit class `delta_(e_i)` in `E_R`:

\[
[X_i]f=\operatorname{Res}(f\,\delta_{e_i}).
\]

This does not cancel an `X_i` factor in a target chain. It is the pairing with a specified dual-normal residue class.

For a general polynomial map homotopy `H`, only

\[
u=H(p_A)_{h_{25}},\qquad
v_i=H(e_i)_{h_{25}k}
\]

can contribute to these rows. The full Hom differential gives

\[
(\delta H)(e_i)_{h_{25}}=-zv_i+X_i u,
\]

\[
(\delta H)(c_{15,35})_{h_{25}k}=X_{15}v_{35}-zv_{15},
\]

\[
(\delta H)(m_{24,35})_{h_{25}k}=X_{24}v_{35}.
\]

Their constant conductor coefficients cancel exactly in both functionals. Thus

\[
\ell_E(\delta H)=\ell_R(\delta H)=0.
\]

Localized homotopy components cannot alter these unlocalized equations. The complete 96-column homogeneous matrix verifies the same statement and reproduces these two sparse dual covectors exactly.

Their evaluation matrix is

\[
\begin{pmatrix}
\ell_E(\widehat\nu_E)&\ell_E(\widehat\nu_R)\\
\ell_R(\widehat\nu_E)&\ell_R(\widehat\nu_R)
\end{pmatrix}
=
\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]

The relation-only difference has coordinates `(1,-1)`. The five-row formula explicitly needs the mixed relation. Comparing only the conductor-unit column and the six generator columns would lose that information.

The code's integral transpose pairing is the pairing of the computed Hom complex with its integral dual. The coefficient residues above realize its five nonzero readings. This is a complete coefficient-level evaluation, not a claim that the missing physical tangential source has been identified with these dual covectors.

## 6. Actual dualized trace maps and their type

Define

\[
\mathbb D_R(-)=R\operatorname{Hom}_R(-,\omega_{R/A}^{\bullet}).
\]

The closed conductor section and the chosen relative normalization give

\[
\mathbb D_R(A[2])\simeq A[-2].
\]

Therefore the two original trace maps have well-defined duals

\[
\nu_E^\dagger,\nu_R^\dagger:
\mathbb D_R(T)\longrightarrow A[-2].
\]

They are defined by precomposition with the entire resolved maps. In an injective representative of the coefficient dualizing object this is literally precomposition on the Hom complex. All generator and relation columns are part of that operation.

The dualizing functor is an anti-equivalence on bounded coherent complexes. The independence already proved for `nu_E` and `nu_R` therefore implies the independence of these two dualized morphisms in the transported homogeneous component. The localized support complexes need not themselves be coherent: the dualization is applied to the original coherent maps after the support counit, whose mapping equivalence has been checked.

The finite matrices exported here are the fifty-state ambient dualizing model, the full 150-summand support model, the original resolved maps, the ten-state dual evaluation, and the coefficient pairings. They are not mislabelled as a finite strict `R`-free model of an injective dualizing complex or a newly constructed spatial correspondence.

The source has changed from `A[2]` to `D_R(T)`. These arrows cannot be relabelled as two scalar evaluations of `T` itself. An independently prescribed reciprocal/tangential spatial source would need its own map into `D_R(T)` before composition is justified.

## 7. Endpoint and normal-frame compatibility

The full edge endpoint sequence has

\[
\kappa(g)=X_{03}p_{03}+X_{25}p_{25},
\]

\[
\kappa(gk)=(X_{03}p_{03}+X_{25}p_{25})k.
\]

Both terms are retained in every Čech summand. Tensor-Hom dualization transposes their complete differential blocks with the graded signs. The ten-state dual evaluation was checked on every pair of basis states, not just on a normal top term.

The coefficient covectors use `h25`, so they cannot be transported through a deletion of the opposite edge endpoint without an additional comparison. Nothing in the coefficient residue construction supplies that deletion.

The six coefficient normal directions used to construct `omega_R/A` are separate from the two native-normal factors already paired in `T`. Their determinant lines are not consumed twice. The long coordinate `X03` remains a base parameter; this calculation does not perform another Cartier restriction or evaluate its physical coorientation.

## 8. Verification and remaining input

The standalone checker has no external package or companion-file dependency. It reconstructs the full 430-state differential, the local edge map and both trace classes, the `1,6,24,92` source relations, all fifteen conductor Čech subsets, and the fifty-state ambient resolution.

It verifies 11,420 counted identities. The unbounded arguments are supplied above: exact tensor resolutions, first-order multigrading thresholds, the normalization exact sequence, and explicit coefficient-lowering in ambient local cohomology. Finite monomial tests are implementation controls rather than substitutes for those arguments.

The remaining physical datum is a source-defined tangential/relative-dualizing correspondence into `D_R(T)`, with the conductor attachment and both edge-endpoint comparison cells. The calculation has produced the coefficient-duality target and two distinguishable evaluations. It has not selected their physical combination or identified either one with `Delta_J`.

## References

Repository input, pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`.
- `src/ledger/20260814-97 Reciprocal-Twist D03 Bivariant Road Trace.md`.
- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`.
- Previous explicit trace source: `branch_a_w03_cech_support_and_trace_descent_checker.py`.

Framework references:

- Stacks Project, Tag `0952`, local cohomology and augmented Čech complexes.
- Stacks Project, Tag `0E9M`, relative dualizing complexes and polynomial/finite factorizations.
- Stacks Project, Tag `0A7A`, finite-map dualizing complexes and biduality.
- Stacks Project, Tag `0A74`, the right adjoint for a closed immersion.
- Stacks Project, Tag `0A8H`, the Hom-complex differential.

These references justify the stated general constructions. The matrices, residue covectors, cohomology, and class evaluations in this document are the present calculation.
