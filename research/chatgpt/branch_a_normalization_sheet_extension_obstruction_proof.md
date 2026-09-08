# Branch A — extension of conductor-ideal comparisons across the normalization sheets

Date: 2026-09-07.

## Result and scope

The preceding calculation produced a rank-40 lattice of source-resolved maps from the conductor ideal in homological degree three. This calculation tests whether these maps are restrictions of maps defined on the complete normalization modules, including their units.

The test has two distinct answers, depending on the coefficient condition imposed on comparison homotopies.

* With conductor-valued homotopies retained, every nonzero member of the rank-40 lattice is obstructed.
* Allowing zeroth-conductor-order coefficients in homotopies, while retaining the complete endpoint and Q conditions, kills a saturated rank-nine sublattice. The rank-31 quotient is a lattice of nonzero normalization-extension obstructions. With the previously checked dihedral transport the ranks are 13, 3, and 10.

No nonzero map from either normalization module in degree three exists in the tested homogeneous component, even into the full unframed 430-state target. An extendable ideal map must therefore already be nullhomotopic in the selected target category. The nine extendable classes in the second test extend by the zero sheet map together with their explicit comparison homotopies; they are not nonzero maps on sheet units.

The calculation constructs the connecting cocycles on the doubled upper conductor. It does not identify the declared shift of the ideal with a physical Gysin shift, select a physical conductor homotopy, or compute the physical Delta_J. The regulator-zero extension remains a coefficient calculation, not an extension of the fixed-nonzero-beta geometric purity theorem.

## 1. Coefficients, supports, and the actual normalization extension

Use the same ring and diagonal order as the preceding calculation:

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]
/(X_aX_b:a\in\{02,04,24\},\ b\in\{13,15,35\}).
\]

Let

\[
I_+=(X_{13},X_{15},X_{35}),\qquad
I_-=(X_{02},X_{04},X_{24}),\qquad I=I_+\oplus I_-,\qquad A=R/I.
\]

The full normalization modules are

\[
R_+=R/I_-,\qquad R_-=R/I_+,\qquad \widetilde R=R_+\oplus R_-.
\]

The relevant exact sequence is

\[
0\longrightarrow I\longrightarrow\widetilde R
\longrightarrow A\oplus A\longrightarrow0.
\]

The two quotient coordinates retain the two upper conductor components. This is different from the normalization sequence

\[
0\longrightarrow R\longrightarrow\widetilde R
\xrightarrow{\varepsilon_+-\varepsilon_-}A\longrightarrow0.
\]

Both follow from the actual normalization square. No map of the geometric normalizations into the coefficient target is assumed merely from these module sequences.

The target C_beta has all 430 states [F,H,epsilon] and the same radial, native-circle, and occurrence-circle differentials. Native normals are beta X_d, whereas the separate occurrence partner has differential X35 without beta. Let v be graded projection onto both complete endpoint packets, and let q be the actual fourteen-state Q-quotient map.

Define

\[
N=\{c\in IC_\beta:q(c)=v(c)=v(dc)=0\},
\]

\[
N^{\mathrm{ext}}=\{c\in C_\beta:q(c)=v(c)=v(dc)=0\}.
\]

Both are genuine subcomplexes. The incoming-endpoint condition is necessary because v is not itself a chain map. Passing from N to N^ext changes only the conductor-order requirement; it does not remove the endpoint or Q conditions.

All map computations have occurrence-map multidegree zero and output regulator-normal grade three. The coefficient monomial on each possible source-to-target entry is fixed by those multidegrees. No occurrence-degree or regulator-power search cutoff is imposed. The integral lattice records this homogeneous component; no claim about all shifts and all multidegrees is made.

## 2. Resolve the normalization modules and test their units

The already constructed resolution of I begins with ranks

\[
6,24,92.
\]

Its positive and negative summands each have ranks 3,12,46. Consequently a free resolution of R_+ starts with R followed by the negative-ideal resolution, and a free resolution of R_- starts with R followed by the positive-ideal resolution:

\[
\cdots\longrightarrow R^{46}\longrightarrow R^{12}
\longrightarrow R^3\longrightarrow R\longrightarrow R_\pm\longrightarrow0.
\]

For a degree-zero map from R_+[3], the unit image is a degree-three cycle U_+ of occurrence weight zero. The three annihilating coordinates X02, X04, X24 must annihilate U_+ through possible degree-four relation images. There are no possible degree-four images in these three weights.

For R_-[3], the relations are X13, X15, X35. Only the X35 relation has possible degree-four images: all 45 fully native-marked face states with their occurrence partners, and the regulator powers forced by the grading.

The complete systems are:

| Normalization source | Unit-image unknowns | Relation-image unknowns | Integer rank of equations | Closed maps |
| --- | ---: | ---: | ---: | ---: |
| R_+[3] | 56 | 0 | 56 | 0 |
| R_-[3] | 56 | 45 | 101 | 0 |

Every elimination pivot is a signed unit. The systems include closure, all first source equations, and their next relations. Higher source terms have homological degree at least five and cannot map into this target. There are also no degree-plus-one map homotopies starting on the sheet unit, since a degree-four target at occurrence weight zero does not exist.

Thus in the stated homogeneous component,

\[
\operatorname{Hom}_{D(R)}(R_\pm[3],C_\beta)=0.
\]

This statement includes an unframed target. Its endpoint/Q-framed and conductor-valued versions vanish as well. It is not a statement that all maps from normalization sheets vanish in every degree, nor that a shifted extraordinary correspondence cannot exist.

## 3. Which ideal maps become null when zeroth-order homotopies are admitted?

Let H denote the previous rank-40 group of maps from I[3] to N. The checker reconstructs its full free-source resolution, equations, integral basis, and symmetry before carrying out the new test.

A degree-plus-one homotopy from the resolved I[3] into the full C_beta can have a value only on the generator a35. The degree-four images on all other generators have negative occurrence exponents. There are 45 possible images on a35. Each has conductor order zero.

For a homotopy H_U with

\[
H_U(a_{35})=U,\qquad H_U(a_i)=0\quad(i\ne35),
\]

the complete differential is

\[
(\delta H_U)(a_{35})=dU,
\qquad
(\delta H_U)(r)=H_U(d_1r).
\]

Its relation images cannot be omitted. The map from these 45 homotopy coefficients to map boundaries is injective; a closed homotopy would require a degree-four cycle in this component, and the complete equation matrix has rank 45.

Solving

\[
F=\delta H_U,
\qquad F\in H,
\]

uses 85 unknowns: 40 map coordinates and 45 homotopy coordinates. The equation rank is 76, giving nine solutions. Their projection to H has nine unit invariant factors, so

\[
0\longrightarrow\mathbb Z^9\longrightarrow\mathbb Z^{40}
\longrightarrow\mathbb Z^{31}\longrightarrow0
\]

is an exact sequence of integral lattices.

Every one of the nine resulting homotopies is verified to satisfy

\[
q(U)=v(U)=v(dU)=0.
\]

Thus N^ext already admits all the homotopies found by testing the full target. No additional ideal-map classes are lost by then forgetting endpoint and Q conditions. Each U has conductor order zero, whereas every entry of delta H_U has positive conductor order. These homotopies are unavailable in N for exactly that coefficient reason.

### A three-term homotopy

One of the nine primitives is

\[
\begin{aligned}
U_{02}={}&\beta^2[\{02\},\{02\},1]\\
&+\beta[\{02,03\},\{02,03\},1]\\
&+\beta[\{02,25\},\{02,25\},1].
\end{aligned}
\]

Its complete derivative has thirteen terms, all in I and with zero endpoint/Q components. The corresponding source map is

\[
F_U(a_{35})=dU_{02},\qquad F_U(a_i)=0\quad(i\ne35),
\]

\[
F_U(k_{13,35})=X_{13}U_{02},\qquad
F_U(k_{15,35})=X_{15}U_{02},
\]

\[
F_U(m_{n,35})=X_nU_{02}
\quad(n\in\{02,04,24\}),
\]

with every other relation image zero. All 28 polynomial terms and their source labels are exported. These are derived-map equations, not a target-cycle test alone.

F_U is nonzero with conductor-valued homotopies fixed, but it has the displayed endpoint/Q-preserving nullhomotopy after allowing zeroth-order coefficients. This illustrates precisely which boundary condition changes.

## 4. Explicit connecting obstructions on the doubled conductor

The actual normalization-module sequence determines

\[
\partial_\nu:(A\oplus A)[2]\longrightarrow I[3].
\]

For a source map F, define

\[
\mathfrak b_F=F\partial_\nu:(A\oplus A)[2]\longrightarrow N^{\mathrm{ext}}.
\]

The shift and sign convention is fixed by the displayed rephased free models. A free model for A[2] has R in degree two, the six ideal generators in degree three, the 24 ideal relations in degree four, and the 92 second relations in degree five.

On the positive copy, the explicit obstruction map is zero on the degree-two unit, equals F(a_i) on positive-sheet generators, equals F(r) on the corresponding positive-ideal relations, and is zero on the negative-ideal summand. On the negative copy the roles are exchanged. These two maps satisfy all chain equations. They are the connecting maps of the two sequences I_+ -> R_+ -> A and I_- -> R_- -> A, rather than a newly chosen pairing of unrelated modules.

The long exact mapping sequence gives an injection

\[
\operatorname{Hom}_{D(R)}(I[3],N^{\mathrm{ext}})
\longrightarrow
\operatorname{Hom}_{D(R)}((A\oplus A)[2],N^{\mathrm{ext}}),
\]

in the tested component because its preceding term Hom(tilde R[3],N^ext) is zero. Therefore the rank-31 quotient above is a lattice of independent nonzero extension obstructions. The certificate exports an integral basis of these maps, not only their dimension.

It follows that an original F in H has a homotopy-coherent extension across tilde R in N^ext exactly when it belongs to the rank-nine kernel. Such an extension is the zero normalization-sheet map equipped with the explicit homotopy on I. With homotopies restricted to N, only F=0 extends.

The rank-31 lattice is a specified subgroup of the doubled-conductor mapping group; its entire ambient cohomology has not been claimed to have rank 31.

## 5. The scalar-invisible relation classes survive this test

The sixteen strict maps intersect the killed rank-nine lattice trivially. The six relation-only maps also intersect it trivially. Thus neither the earlier strict gallery comparison nor the relation-only ambiguity is erased by the new permitted homotopies.

For the strict negative-sheet gallery map,

\[
L_{03}=[\{03,13,35\},\{03,13,35\},0]
-\beta[\{13,35\},\{13,35\},0],
\]

\[
F_-(a_i)=X_iL_{03}\quad(i\in\{02,04,24\}),
\]

with all other columns zero, the negative upper-conductor obstruction has these same generator images. Its class is nonzero. The normalization-module equations cannot realize it as a restriction of a nonzero same-degree sheet map.

A relation-only map has zero generator values and nonzero degree-four values on the mixed source relations. Its connecting obstruction has zero values on both upper-conductor units and all degree-three generators, but nonzero values on degree-four relation states. The complete ambient homotopy equation has no solution for it. Consequently knowing the scalar six-term conductor element cannot determine or eliminate these obstructions.

## 6. Equivariance

The calculation uses the previous published cellular reflection, its ordered normal signs, and natural source-generator and source-relation transport. Rotation carries the occurrence correction through 35,15,13. No rotation is imposed within a single fixed occurrence complex.

The rank-nine killed lattice is reflection-stable and has invariant rank three. Its quotient has invariant rank ten. The invariant sequence is

\[
0\longrightarrow\mathbb Z^3\longrightarrow\mathbb Z^{13}
\longrightarrow\mathbb Z^{10}\longrightarrow0.
\]

All ten nonzero diagonal factors of the invariant quotient map are one. Hence there is no finite index defect in this sequence. This conclusion is about this extension/forgetting map, not a revision of the different first-symbol quadratic-defect calculation.

The two previously computed invariant relation-only directions remain independent in the rank-ten obstruction lattice. Their vanishing generator and scalar-symbol readouts do not make them extendable.

## 7. Consequence for the physical construction

The rank-40 conductor-ideal maps cannot be treated as restrictions of arbitrary normalization-sheet operators. Restoring the sheet units is an additional condition, and it is obstructed in the current shift and coefficient realization.

Allowing zeroth-order conductor coefficients in endpoint/Q-preserving homotopies removes nine relative classes. The other 31 have explicitly constructed upper-conductor connecting obstructions. Their ten equivariant directions include the two source-relation classes invisible to the scalar symbol.

A physical realization must address this connecting obstruction using its actual variance, support operation, shift, and comparison cells. Declaring one ideal map to be selected by the normalization square is not a construction of its extension. None of these statements excludes an extraordinary or differently shifted realization, and no physical value of Delta_J is assigned.

## 8. Reproduction

Run the standalone file:

```bash
python branch_a_normalization_sheet_extension_obstruction_checker.py \
  --output branch_a_normalization_sheet_extension_obstruction_certificate.json
```

The checker has no companion-file, network, archive, or optional-library dependency. It reconstructs and replays the preceding rank-40 calculation, constructs both normalization-module resolutions, solves their full homogeneous map equations, computes all ambient homotopies of the ideal maps, and exports the doubled-conductor connecting maps and symmetry matrices.

The run checks 36,305 new identities and replays 301,266 preceding identities. An isolated run with a different Python hash seed reproduces the certificate byte-for-byte.

Mathematical payload SHA-256:

```text
f646fb67bddb9e74687dde0b635eb06821c9b47a070af98b351ee52b2caf4291
```

## Sources and conventions

Repository: andrey-kokoev/marici. Pinned commit: d1947b67a60d3e88ba77f4ca60ea02c2a306ee61.

1. `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: actual normalization modules, conductor ideal, doubled upper conductor, and scalar symbol.
2. `research/voevodsky/check_absolute_unlocalized_support_pc.rs`, blob `b967151cb0ee822e2361b9334a4ab26082c12682`: the signed radial/native differential, state supports, and symmetry conventions.
3. `research/voevodsky/check_d03_formal_support_purity.rs`, blob `acaabf367b24029d9dbfa371ee1983d392b393fa`: the fixed-nonzero-beta scope of the physical normal graph. The beta-zero extension used here remains algebraic.
4. Stacks Project Tag 0A8H: Hom-complex differential and composition signs.
5. Stacks Project Tag 064B: bounded-above projective resolutions compute maps in the derived category.
6. Stacks Project Tags 06XP and 0117: connecting morphisms and exact sequences of derived mapping groups.

The new numerical statements are obtained from the exported matrices, not from assigning desired signatures to the maps.
