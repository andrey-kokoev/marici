# Branch A: full normalization duality and a two-grade conductor trace

## Results and scope

This calculation uses the full six-short-variable normalization ring, not the nodal two-variable slice. It constructs:

1. a polynomial factorization of both recorded reciprocal trace maps through the normalization fibre, followed by the actual relative-interval quotient;
2. a two-grade conductor readout whose matrix is `-beta * [[1,1],[0,1]]`;
3. a 50-state ambient free model of the relative dualizing complex, its two nonzero cohomology modules and their nonzero connecting morphism;
4. an explicit conductor-supported coefficient residue on that dualizing complex.

The second trace coordinate is the retained occurrence-normal line paired with the `X35` conductor conormal-dual class. It is not division by `X35`. Projecting onto the scalar conductor-unit coordinate loses this class.

The coefficient residue is defined on the relative dualizing complex. It is not, without an additional map, a tangential trace on the interval/native/occurrence target. No physical conductor–Morse class or complete spatial Gysin correspondence is assigned.

## 1. Coefficients, source and retained target

Put

\[
A=\mathbb Z[\beta,X_{03},X_{14},X_{25}],
\]

\[
S=A[X_{02},X_{04},X_{24},X_{13},X_{15},X_{35}],
\]

\[
R=S/(I_-I_+),\quad
I_-=(X_{02},X_{04},X_{24}),\quad
I_+=(X_{13},X_{15},X_{35}),\quad I=I_-+I_+.
\]

Here `A` is the full conductor coefficient ring. The normalization modules are

\[
R_-=A[X_{02},X_{04},X_{24}],\qquad
R_+=A[X_{13},X_{15},X_{35}].
\]

The normalization sequence, in the ordered pair `(negative, positive)`, is

\[
0\longrightarrow R\longrightarrow R_-\oplus R_+
\xrightarrow{\epsilon_+-\epsilon_-}A\longrightarrow0.
\]

The quotient has the polarity sign under sheet exchange. A fixed ordered trivialization is used in the matrices; invariant statements retain this line.

The conductor source is the existing free resolution `P_A[2]` with ranks `1,6,24,92` in homological degrees `2,3,4,5`. Its first equations are `d e_i = X_i p_A`. Six same-sheet and eighteen mixed-sheet relations and all ninety-two next equations are retained.

Write `x=X03`, `v=X25`, `z=X35`. The interval factor is

\[
dg=xp_{03}+vp_{25},\qquad
dh_{03}=\beta xp_{03},\qquad
dh_{25}=\beta vp_{25},
\]

\[
\xi=h_{03}+h_{25}-\beta g,\qquad d\xi=0.
\]

After the prescribed reciprocal pairing of the two native normals, retain

\[
T=(P_E\otimes K_R(z))\otimes\mathfrak o_{02,35}[2],
\qquad dk=z.
\]

The target has ten states. The ordered native-normal line and the radial interval orientation are retained throughout. The factor `k` is the independent occurrence normal, not the native `35` circle. The full 430-state complex and the forty-state edge inclusion are reconstructed before the new operations.

The recorded traces have the exact columns

\[
\nu_E(p_A)=0,\qquad
\nu_E(e_i)=X_i\xi\quad(i=13,15,35),
\]

and

\[
\nu_R(p_A)=0,\qquad
\nu_R(e_i)=X_i\xi\quad(i=13,15),\qquad \nu_R(e_{35})=0,
\]

\[
\nu_R(c_{i,35})=X_i\xi k\quad(i=13,15).
\]

Every other column is zero. They are checked against the complete resolved source.

## 2. A finite normalization factorization of the supported maps

For any bounded free target `T`, define

\[
\mathcal N(T)=\operatorname{fib}
\left(T\longrightarrow T\otimes_R(R_-\oplus R_+)\right).
\]

Its homological degree `n` is

\[
\mathcal N(T)_n=T_n\oplus(T_-)_{n+1}\oplus(T_+)_{n+1},
\]

with differential

\[
D(t,h_-,h_+)=(dt,\ell_-t-dh_-,\ell_+t-dh_+).
\]

Unlike the preceding local-cohomology terms, these two branch modules are not localized. All coefficients in the displayed lifts below are polynomial.

Tensoring the actual normalization sequence with the free terms of `T` gives the chain map and quasi-isomorphism

\[
q_\nu:\mathcal N(T)\longrightarrow(A\otimes_R T)[-1],
\]

\[
q_\nu(t,h_-,h_+)=\overline{h_+}-\overline{h_-}.
\]

The target differential is `-d` on the shifted complex. Thus

\[
q_\nu D=-d\,q_\nu.
\]

This uses the exact sequence and its fixed branch difference. It does not choose an `R`-linear section of `R_- + R_+ -> A`.

The original polynomial comparison homotopies already work over the whole normalization branches:

\[
H_E^+(p_A)=\xi,
\]

\[
H_R^+(p_A)=\xi,\qquad H_R^+(e_{35})=\xi k.
\]

The negative-branch homotopies are zero. The equations are

\[
\delta H_i^+=\nu_i|_{R_+},\qquad \nu_i|_{R_-}=0.
\]

Hence

\[
\widehat\nu_i^{\nu}=(\nu_i,0,H_i^+)
\]

are actual maps into `N(T)`.

Their conductor images are

\[
q_\nu\widehat\nu_E^\nu(p_A)=\xi,\qquad
q_\nu\widehat\nu_E^\nu(e_i)=0,
\]

\[
q_\nu\widehat\nu_R^\nu(p_A)=\xi,\qquad
q_\nu\widehat\nu_R^\nu(e_{35})=\xi k.
\]

All other columns of the second map vanish. The conductor unit and the resolved first-normal column are both retained.

### Complete homogeneous check

At the preceding reduced regulator grade one and occurrence-map degree zero, the Hom complex into `(A tensor T)[-1]` has dimensions

\[
(0,6,4)
\]

in homotopy, map and equation degrees. Its outgoing differential has rank four, giving a rank-two integral class lattice. The two independent generators can be taken as `p_A -> xi` and `e35 -> xi k`. Their coordinate determinant is one. The next regulator grade gives identical matrices after multiplication by `beta`, and the basis has at most one native mark, proving stabilization for every higher grade.

The independent unlocalized trace Hom calculation was also replayed: dimensions `(6,46,94)`, differential ranks `(6,38)`, and rank-two cohomology generated by the original traces. The normalization counit maps the two displayed lifts to those generators. Thus no additional normalized-lift ambiguity occurs in this specified homogeneous component.

This does not assert a canonical retraction from arbitrary local-cohomology representatives onto the finite normalization fibre.

## 3. Extend to full conductor support without mixed Laurent inverses

The full conductor Čech complex has module summands

\[
R;\quad
\bigoplus_{i\in I_-\cup I_+}R_{X_i};\quad
\bigoplus_{\{i,j\}\subset I_-\text{ or }I_+}R_{X_iX_j};\quad
R_{X_{02}X_{04}X_{24}}\oplus R_{X_{13}X_{15}X_{35}}.
\]

There are `1+6+6+2=15` nonzero coefficient summands. Every mixed-sheet localization is the zero module. The displayed index sets refer to the six labelled variables, not to arbitrary elements of the ideals.

Tensoring with `T` gives 150 module summands. Before reciprocal pairing, the full edge has 600 summands. These are not asserted to be finite free modules over `R`.

There is a chain map from the finite normalization fibre: its global component is the identity, and each polynomial branch homotopy is repeated on the three basic opens of that branch. The pair-overlap terms cancel because the repeated restrictions agree. There are no fitted higher Čech terms.

The two trace lifts therefore extend to `R Gamma_I T`. The complete differential and all six-open source equations were verified. The reciprocal pairing commutes with this construction on all 600 input summands.

Because the source is supported on `I`, local-cohomology adjunction identifies the derived mapping space into `R Gamma_I T` with the one into `T`. The present matrices give explicit representatives of that identification for the two traces.

## 4. The relative interval produces a two-grade readout

Quotient both complete edge-endpoint packets in `T`. The quotient is

\[
\mathcal O=K_R(z)[3],\qquad
q(g)=e_0,\quad q(gk)=e_1,\quad de_1=-z e_0.
\]

Both endpoint connecting maps remain part of the support triangle. In particular the `W25` endpoint is not deleted from the full construction before the quotient is formed.

After normalization descent,

\[
(A\otimes_R\mathcal O)[-1]
=Ae_0[2]\oplus(A\otimes\mathcal L_{35})e_1[3],
\]

with zero differential. The upper occurrence line `L35` has the weight of `X35`. Both summands retain the common native-pair and interval orientation lines.

The complete readout is

\[
\begin{array}{c|cc}
 &p_A&e_{35}\\ \hline
\mathcal R(\nu_E)&-\beta e_0&0\\
\mathcal R(\nu_R)&-\beta e_0&-\beta e_1.
\end{array}
\]

All other source columns have zero image. The raw coefficient matrix is

\[
-\beta\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

At fixed nonzero `beta`, normalization by the interval factor `-beta` gives the unimodular matrix

\[
\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

No assertion divides by `beta` at regulator zero. No occurrence variable is inverted.

The second coordinate is identified on the actual source resolution. Since its differential has conductor coefficients, applying `Hom_R(-,A)` makes the first differential zero. Hence

\[
\operatorname{Ext}_R^1(A,A)=\operatorname{Hom}_A(I/I^2,A).
\]

The map `e35 -> e1` is the primitive class

\[
[X_{35}]^\vee\otimes\mathcal L_{35}.
\]

This is a resolved conormal-dual class. It is not a derivative defined by cancelling `X35`.

Projecting the output onto its degree-two scalar line makes the two traces equal. Retaining the adjacent occurrence grade distinguishes them. Their difference has zero unit coordinate and a unit first-normal coordinate after fixed-nonzero-regulator normalization.

### Relation-only comparison is retained

The earlier homotopy `U(e35)=-xi k` has residual map

\[
\kappa(m_{n,35})=X_n\xi k\quad(n=02,04,24).
\]

Its finite normalization lift uses the negative-branch comparison

\[
H_\kappa^-(e_{35})=\xi k.
\]

The full identity is

\[
\widehat\nu_E^\nu-\widehat\nu_R^\nu-\delta(U,0,0)
=(\kappa,H_\kappa^-,0).
\]

Normalization descent and relative-interval projection send the right side to the single column `e35 -> +beta e1`, exactly the difference of the two readouts. Thus the source-relation class has not been erased; it has a lower-degree representative after the normalization connecting operation.

## 5. The full relative dualizing complex is not one shifted line

The following degrees are cohomological. Let

\[
\mathcal D_{R/A}=R\operatorname{Hom}_S(R,\Omega^6_{S/A}[6]).
\]

This is the relative dualizing complex for the full normalization ring. The ordinary polynomial ring `S` is used here: mixed monomials must not be killed in its free resolution.

### An explicit ambient free resolution

The product ideal `I_- I_+` has the tensor resolution of the two three-generator polynomial ideals. Prepending `S` gives a free resolution of `R` with ranks

\[
1,9,18,15,6,1.
\]

For homological degree `n>=1`, its generators are

\[
\bigoplus_{p+q=n+1,\ p,q\ge1}
\Lambda^p S^3_-\otimes\Lambda^q S^3_+.
\]

The first map sends the pair `(i,j)` to `X_i X_j`. Higher maps use the Koszul differential on each block with the tensor sign `(-1)^{p-1}` on the second block. Both full 50-state differentials, before and after dualization, are exported.

Exactness is not inferred from finitely many monomials. Each single-sheet ideal has its truncated regular-sequence Koszul resolution. Disjoint polynomial variables make their tensor resolution exact: the variables of one sheet remain a regular sequence on the other sheet's polynomial ideal module. Multiplication identifies the tensor of the two ideals with their product, since both are free over the coefficient base on their respective monomial bases.

### Compute the cohomology and the extension

Dualize the actual normalization sequence. The three independent variables on each normalization sheet give

\[
A\otimes L_{\rm pol}^\vee
\xrightarrow{(-\gamma_-,\gamma_+)}
\Omega^3_{R_-/A}[3]\oplus\Omega^3_{R_+/A}[3]
\longrightarrow\mathcal D_{R/A}
\longrightarrow(A\otimes L_{\rm pol}^\vee)[1].
\]

In the fixed ordered frame, `gamma_-` sends the ordered negative triple of the ambient Koszul resolution of `A` to its volume generator; `gamma_+` does the same on the positive triple. Their source signs are `(-1,+1)`, dual to the specified normalization difference.

Therefore

\[
H^{-3}(\mathcal D_{R/A})
=\Omega^3_{R_-/A}\oplus\Omega^3_{R_+/A},
\]

\[
H^{-1}(\mathcal D_{R/A})=A\otimes L_{\rm pol}^\vee,
\]

and all other cohomology vanishes.

The second statement is also visible in the exported minimal dual: its last free generator is hit by precisely the six short variables with unit signs. Its cokernel is `A`.

The displayed connecting map is nonzero. Its two ordered-triple values are units. Every possible Hom boundary evaluated on those triples has coefficients in the relevant branch augmentation ideal, so cannot produce either unit. Hence the canonical truncation triangle does not split. The two cohomology modules cannot be replaced by an unrelated direct sum, and the whole dualizing object cannot be replaced by a single orientation line with a shift.

These are coefficient-space statements. They do not identify the physical face `W03` with the conductor immersion.

## 6. A full-conductor coefficient residue on the correct dualizing object

Put

\[
E_-=H^3_{I_-}(\Omega^3_{R_-/A}),\qquad
E_+=H^3_{I_+}(\Omega^3_{R_+/A}).
\]

Use the ordered residue classes

\[
\rho_-=\left[\frac{dX_{02}\wedge dX_{04}\wedge dX_{24}}
{X_{02}X_{04}X_{24}}\right],
\]

\[
\rho_+=\left[\frac{dX_{13}\wedge dX_{15}\wedge dX_{35}}
{X_{13}X_{15}X_{35}}\right].
\]

These are local-cohomology classes on separate polynomial branches. They are not fractions in `R` and never invert a mixed-sheet product.

Applying full conductor support to the dualizing triangle gives the two-term model

\[
R\Gamma_I\mathcal D_{R/A}
\simeq[\,A\xrightarrow{1\mapsto(-\rho_-,\rho_+)}E_-\oplus E_+\,]
\]

in cohomological degrees `-1,0`. The first map is injective. Thus the result has cohomology only in degree zero, equal to the displayed cokernel.

The scalar coefficient residue is

\[
\operatorname{Tr}_I[(a_-,a_+)]
=\operatorname{Res}_-(a_-)+\operatorname{Res}_+(a_+).
\]

It is well defined because the image of `1` has residue `-1+1=0`.

Both single-branch simple residues represent the same conductor evaluation and have value `+1`. The sum of the two has value `2`. No half-sum is used.

The arbitrary-pole proof is explicit. A branch pole with exponent vector `n`, with all entries at least one, is dual under residue to the branch monomial with exponent vector `n-1`. The only monomial duplicated between the two branches is the common constant. The relation `(-rho_-,rho_+)` removes that duplication. This identifies the cokernel with the finite-order, conductor-adically continuous `A`-dual of `R`. The trace is evaluation at `1_R`.

This trace is `A`-linear, not `R`-linear. For example the negative-branch pole of orders `(2,1,1)` has residue zero, but multiplication by `X02` changes its residue to one. The image of `X02` in `A` is zero.

The six ambient form factors, the two branch determinant lines, and the polarity dual line remain in this calculation. The physical `X03`-normal belongs to the coefficient base `A` and has not been integrated or identified with any short normal.

## 7. What the residue can and cannot evaluate

The finite normalization readout of Sections 2–4 is defined on the recorded normalization lifts. It is not a map on arbitrary localized representatives. In particular, the earlier positive-open `1/X35` homotopy restoring a zero unit column is not a homotopy in the polynomial normalization fibre.

The coefficient residue of Section 6 is defined on `R Gamma_I D_{R/A}`, not on `R Gamma_I T`. These are different target objects. A tangential/dualizing comparison between them must be constructed before assigning a scalar value to either reciprocal trace.

The actual duality normalization is

\[
R\operatorname{Hom}_R(A,\mathcal D_{R/A})\simeq A.
\]

It follows by finite adjunction from

\[
R\operatorname{Hom}_S(A,\Omega^6_{S/A}[6])\simeq A,
\]

whose map is the ordered six-variable Koszul evaluation. Thus, for the currently fixed source `A[2]`, a scalar comparison would require the appropriately orientation-framed map to `D_{R/A}[2]`, not an arbitrary scalar augmentation of the interval target. No such physical comparison is asserted here.

Both trace coordinates and their relation data are now explicit in a finite conductor target. A single projection onto its scalar degree erases the `X35` conormal-dual coordinate. The new coefficient residue does not identify the physical Delta_J, select a source homotopy, or create the missing generic-Q spatial component.

## Verification and provenance

Run:

```sh
python branch_a_full_normalization_duality_and_two_grade_trace_checker.py \
  --output branch_a_full_normalization_duality_and_two_grade_trace_certificate.json
```

The checker is standalone and uses only the Python standard library. It embeds the required old definitions, reconstructs the 430-state differential and the source resolution, recomputes the original trace Hom group, verifies the normalization and full-conductor maps, constructs both ambient free differentials and the connecting Koszul map, and tests the residue formulas.

The all-polynomial exactness and cohomology assertions use the proofs above. The 729 residue monomial controls test the implementation; they are not the proof for arbitrary pole order.

Repository input: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

- Entry 93: actual normalization ring, modules, conductor difference, and polarity.
- Entry 97: prescribed reciprocal pairing and the separate occurrence-Laurent scope of its tangential trace.
- `check_absolute_unlocalized_support_pc.rs`: signed loaded differential.
- Previous standalone `branch_a_w03_cech_support_and_trace_descent_checker.py`: source and trace formula provenance; not a runtime dependency.

Mathematical references: Stacks Project 0952 (local cohomology), 0117 (connecting maps), 0621 (Koszul complexes), 0A8H (Hom signs), 0A7A (finite duality and biduality), 0ATZ (upper shriek and polynomial presentations), and 0A81 (local duality; the relative residue here is additionally proved directly by coefficient pairing).
