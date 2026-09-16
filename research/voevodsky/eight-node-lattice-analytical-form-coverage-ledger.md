# Eight-node lattice analytical-form coverage ledger

## Scope correction

The eight-node tetrahedral lattice is the seventh edgewise subdivision

`esd_7(Delta^3)`.

It does **not** contain `8! = 40320` elementary tetrahedra. Its vertices are

`(a1,a2,a3,a4) in N^4`, with `a1+a2+a3+a4=7`,

so it has 120 vertices and normalized volume 343. Hence it has 343 maximal elementary tetrahedra in a unimodular edgewise triangulation.

The number `8!` can count orderings of eight independently schedulable operations, but those orderings are evaluation schedules in the localized contraction category. They are not lattice cells. Their analytical compatibility must be proved by interchange and higher-coherence cells, not by assigning 40320 unrelated operators.

## Coverage objective

To ensure that every elementary lattice cell has an analytical form, construct one homotopy-coherent simplicial map

`Phi : esd_7(Delta^3) -> N_hc(Real_S)`.

Coverage then means:

| dimension | lattice datum | required analytical datum |
|---|---|---|
| 0 | barycentric node `alpha` | typed Hermitian/Green presentation `X_alpha` |
| 1 | elementary transfer `alpha -> alpha-e_i+e_j` | closed or bounded transport `d_ij(alpha)` |
| 2 | elementary triangle | naturality/interchange homotopy between its two composites |
| 3 | elementary tetrahedron | modification filling the alternating four-face boundary |

If the target is the nerve of a strict category, the 3-cells follow from associativity after vertex, edge, and triangle coverage. In the weak/rigged setting, one modification prototype is required for each typed incidence class and boundary stratum.

## Current universal data

| datum | analytical form currently available | coverage status |
|---|---|---|
| four abstract vertices | source, geometric realization, source response, realized response | available by presentation type |
| source-retaining chart changes | `C_ij = S_j R_i` on source-generated essential images | available where source recovery is bounded |
| complete-response `C14/C41` | all-seam response and first-coordinate recovery | available on response essential image |
| canonical `C34` | pair-to-bordered response with `(rho(0),E,W,R)` | available internally |
| linking form | bounded skew operator `K_link=-J_link/2` | available |
| connected grades | separate nuclear retained graph | available |
| tetrahedral internal Stokes filler | `-R-2E+(R+2E)=0` | available, but not an independent RH criterion |
| negative polarity | dagger/reflection transport | available when the positive prototype is typed |

## First boundary prototype

The registered elementary tetrahedron is

| name | coordinate | abstract role |
|---|---|---|
| A | `(6,0,1,0)` | V1 |
| C | `(5,1,1,0)` | V2 |
| B | `(5,0,2,0)` | V3 |
| D | `(5,0,1,1)` | V4 |

Its analytical cells are:

| cell | support | analytical form | status |
|---|---|---|---|
| `C12` | `A -> C` | source-to-geometric retained transport | constructed on essential image |
| `C13` | `A -> B` | source-to-spectral/theta-history transport | constructed at form strength |
| `C14` | `A -> D` | all-seam complete response | constructed |
| `C24` | `C -> D` | bordered radial response | constructed internally |
| `C34` | `B -> D` | pair-to-bordered return | constructed internally |
| `C41` | `D -> A` | source recovery `(B,Q,A,C) -> B` | constructed on response essential image |
| `H123` | `A-C-B` | constructor naturality | source-chart derived |
| `H124` | `A-C-D` | observation naturality | source-chart derived |
| `H134` | `A-B-D` | source mate coherence | source-chart derived internally |
| `H234` | `C-B-D` | realized mate coherence | canonical Stokes realization constructed |
| `Theta` | `A-C-B-D` | alternating face filler | internally constructed |

External physical, determinant, or Evans interpretations remain comparison theorems; they do not negate internal cell coverage.

## Earliest global coverage gap

The repository does not yet provide a single barycentric formula `alpha -> X_alpha` together with globally defined transfer laws `d_ij(alpha)` whose restrictions recover all six eight-node edge factorizations.

Existing edge factorizations use different analytic stage semantics. In particular, a convenient eight-stage factorization of `C24` and the spectral-to-trace factorization of `C34` do not yet arise as restrictions of seven common global refinement transformations `d_0,...,d_6`.

Therefore one may not propagate the first boundary prototype to all 343 elementary tetrahedra yet.

## Nonredundant next construction

1. Freeze the eight global rung meanings, common to all six abstract edges.
2. For every edge `C_ij`, map its existing analytic factorization into those rungs, inserting identity/degeneracy stages where necessary.
3. Define the universal vertex presentation `X_(a1,a2,a3,a4)` as an iterated retained joint graph, not a barycentric mixture of Hilbert spaces.
4. Define each elementary `d_ij(alpha)` by the corresponding source-labelled chart transport.
5. Prove translation naturality in `alpha` and boundary restriction compatibility.
6. Classify and prove the finite set of triangle and tetrahedron incidence prototypes.
7. Generate a machine-readable census showing that every lattice cell is an instance of one proved prototype.

## Iteration-1 disposition

The combinatorial target and first boundary prototype are now fixed. The claim “8! cells” is retyped correctly: lattice coverage concerns `esd_7(Delta^3)`, while `8!` schedule orderings belong to evaluation-path coherence. The earliest executable analytical gap is the common eight-rung semantics needed to define one global simplicial map.

## Iteration 2: semantic chamber correction

Fresh inspection of the existing edge factorizations shows that equal numerical stage indices cannot be assigned one common analytic meaning. The spectral route forms a dual/canonical pair before trace realization, while the geometric route inserts cutoffs first. The direct `C14` path also combines some coarse operations in one arrow and refines others into several arrows.

The correct common index is therefore not a row number `0,...,7`. It is the order-ideal lattice of the seven typed semantic transitions:

| label | operation | analytical form |
|---|---|---|
| `A` | semilocal amplification | place-set/source extension and corresponding retained transport |
| `J` | canonical--dual comparison | paired spectral chart change and scattering phase |
| `P` | polarization | `g -> g*g*`, represented bilinearly on the pair carrier |
| `C` | cutoff insertion | physical/Fourier projections and product-cutoff operator |
| `T` | trace/finite part | trace, volume subtraction, and finite-part response |
| `E` | endpoint completion | gamma/end-wall residue and Wronskian endpoint coordinates |
| `F` | positive filler | higher cell combining the completed boundary faces |

Their dependency relations are

`A<J`, `A<C`, `J<T`, `C<T`, `P<T`, `P<E`, `T<F`, `E<F`.

A legal semantic state is a downward-closed subset of this poset. There are 18 such states. A cell is a strict chain of legal states. The exact semantic coherence census is:

| cell dimension | count |
|---:|---:|
| 0 | 18 |
| 1 | 112 |
| 2 | 353 |
| 3 | 645 |
| 4 | 716 |
| 5 | 478 |
| 6 | 177 |
| 7 | 28 |
| **all nonempty semantic cells** | **2527** |

The 28 maximal chambers are the admissible linear extensions. They replace the naive `7!` orderings. Likewise, `8!` unrestricted schedules are not typed analytical cells.

The exact census is already machine checked by:

- `research/voevodsky/checkers/check_seven_transition_order_ideal_complex.py`;
- `research/voevodsky/results/seven_transition_order_ideal_complex.json`.

### Edge factorization refinement maps

Each existing eight-node edge path must map monotonically to the 18 order ideals; repeated ideals are allowed when a fine analytic arrow refines one coarse transition. The direct `C14` path already supplies such a map:

`{A}`,
`{A,P}`,
`{A,P,J}`,
`{A,P,J,E}`,
`{A,P,J,E}`,
`{A,P,J,E}`,
`{A,P,J,E,C,T}`,
`{A,P,J,E,C,T,F}`.

This proves that an eight-node path is a refinement of a semantic chamber, not itself a maximal chamber merely because it has eight nodes.

### Revised global coverage obligation

To cover all elementary cells, it is enough to provide:

1. an analytical presentation for each of the 18 order ideals;
2. a typed analytical map for each cover relation used by the 112 semantic edges;
3. one naturality/interchange proof for each typed triangle incidence prototype;
4. the required higher fillers for the remaining incidence prototypes;
5. monotone refinement maps from all six conductor-edge factorizations into this semantic complex;
6. a simplicial map from the geometric lattice `esd_7(Delta^3)` into the semantic coherence complex.

Translation naturality then propagates the finite prototype data over all 343 geometric tetrahedra. Dagger/reflection supplies the opposite polarity where its domain and orientation hypotheses hold.

### Iteration-2 frontier

The common indexing object is now frozen: the 18-state, 2527-cell order complex, not eight rowwise stages and not `8!` unrelated schedules. The next executable task is to extract monotone order-ideal refinement maps for `C12`, `C13`, `C24`, and `C34` (with `C14` already mapped), and identify the absent sixth edge factorization `C23` or its source-chart degeneracy.

## Iteration 3: edge-refinement audit

### C13 and C12 form one aligned source branch

`C13` has the stages observer, polarization, Mellin boundary value, semilocal amplification, dual/canonical pair, source pairing, relative scattering phase, and differentiated connection. `C12` is obtained from the same stages by Hardy--Titchmarsh geometric transport. The repository proves stagewise cells `H123[r]` for every segment.

A monotone coarse typing for both paths is:

| fine stage | C13 meaning | C12 meaning | coarse ideal |
|---:|---|---|---|
| 0 | source observer | source observer | empty ideal |
| 1 | convolution polarization | represented convolution polarization | `P` |
| 2 | Mellin boundary value | geometric Mellin boundary value | `P` |
| 3 | semilocal dual amplification | Sonin-amplified geometry | `AP` |
| 4 | dual/canonical pair | dual/canonical geometric pair | `AJP` |
| 5 | paired realization | transported source pairing | `AJP` |
| 6 | relative scattering phase | relative geometric scattering | `AJP` |
| 7 | differentiated connection | geometric Weil connection | `AJP` |

Repeated ideals record analytic refinements internal to one coarse transition. This map is monotone and legal. It also gives `C23[r]` explicitly as the Hardy--Titchmarsh comparison between the two rows, so `C23` is not absent: it is a stagewise equivalence/degeneracy edge rather than an independently ordered eight-step process.

### C24 forward trace branch

The `C24` path is geometric data, integrated observer, orbit kernel, product cutoff, scalar trace, relative trace, local Weil sum, and finite-place Weil functional. Because its initial geometric vertex is the enriched endpoint of `C12`, the `A` and `J` structures are retained even when suppressed from the displayed node.

Its legal coarse typing is therefore:

| fine stage | meaning | coarse ideal |
|---:|---|---|
| 0 | enriched semilocal geometry | `AJ` |
| 1 | polarized integrated observer | `AJP` |
| 2 | orbit-kernel refinement | `AJP` |
| 3 | physical/Fourier product cutoff | `AJPC` |
| 4 | scalar cutoff trace | `AJPCT` |
| 5 | relative centered trace | `AJPCT` |
| 6 | local Weil sum plus controlled endpoint/error row | `AJPCTE` |
| 7 | finite-place Weil functional | `AJPCTE` |

The bulk filler `F` is not an edge operation on `C24`; it is attached only after adjacent face compatibility is supplied.

### C34 exposes a direction mismatch

The displayed `C34` proof runs from paired spectral connection through scalar current, local distributions, and semilocal Weil sum, and then *reverses* Connes's trace proof to reach orbit-volume and cutoff presentations. Consequently its fine order performs trace/distribution identification before cutoff realization.

This cannot be a monotone path in the contraction-poset order because the poset requires `C<T`. Assigning `T` at the local-distribution stage and `C` later would leave the order-ideal lattice.

This is not a missing analytical formula: every scalar equality on `C34` is typed. It shows that `C34` uses an invertible comparison/refinement move in the localized evaluation category, not only forward contractions. Therefore the 18-state order-ideal complex indexes forward schedules but is not by itself the full indexing infinity-category needed for all six edges.

### Required enlargement

Use the simplicial localization `P(X)=L_W Contr(X)` already defined in the evaluation-path research. Keep the 18-state order complex as the forward-contraction subcomplex, and add the authorized equivalence class `W` generated by:

- Fourier/Mellin presentation changes;
- local principal-value identities;
- Connes scalar distribution/finite-part equivalence;
- source-chart changes such as `C23`;
- associator, interchange, unitor, mate, and admitted refinement moves.

Then `C34` is a zigzag whose backward-looking scalar steps become invertible arrows in `W`; it need not violate the forward dependency order.

### Iteration-3 frontier

`C12`, `C13`, `C23`, and `C24` now have explicit semantic refinement typings. `C34` proves that global coverage cannot be certified by the forward order complex alone. The next executable task is to record every `C34` segment as either a forward contraction or a named equivalence in `W`, and do the same for `C14`. This will produce the first complete six-edge diagram in the localized contraction category.

## Iteration 4: localized six-edge segment classification

Use these arrow classes:

- `FWD`: a genuine forward contraction/observation;
- `EQ_W`: a source-authorized equivalence inverted in the localization;
- `REF_W`: an admitted refinement or regulator presentation change inverted in the localization;
- `OPEN`: an analytical lift required by the cell but not constructed.

### Direct C14 path

| segment | analytical operation | class | authority |
|---:|---|---|---|
| 0 | ordered convolution polarization | `FWD` | star-representation/pair-carrier construction |
| 1 | multiplicative Mellin transform | `EQ_W` | Fourier--Mellin presentation equivalence |
| 2 | insert logarithmic current and endpoint residue row | `FWD` | one contour differential, with residues retained |
| 3 | gamma/prime-power currents to normalized local principal values | `EQ_W` | local distribution identities |
| 4 | sum normalized local currents over places | `FWD` | semilocal codiagonal |
| 5 | Weil sum to centered product-cutoff trace modulo rapid error | `REF_W` | Connes orbit-volume/cutoff comparison |
| 6 | finite-part removal of cutoff | `FWD` | finite-part trace operation |

All seven `C14` segments have analytical forms in the localized category. Its coarse ideal map remains the already recorded degenerate monotone map.

### Spectral-to-trace C34 path

| segment | analytical operation | class | authority or gap |
|---:|---|---|---|
| 0 | paired connection to observer current | `FWD` | bounded/source-defined observer pairing |
| 1 | logarithmic derivative to gamma and prime-power expansion | `EQ_W` | convergent local Fourier expansion |
| 2 | local expansions to normalized principal values | `EQ_W` | gamma/digamma and finite-prime distribution identities |
| 3 | sum local distributions over places | `FWD` | semilocal codiagonal |
| 4 | Weil sum to orbit-volume defect | `EQ_W` at scalar/distribution strength | Connes scalar distribution identity |
| 5 | restore centered cutoff trace and controlled rapid error | `REF_W` | regulator presentation change |
| 6 | take finite part | `FWD` | finite-part trace operation |

The common affiliated operator

`L_S = multiplication by -log|x|_S`

lifts segments 0--4 above immediate scalarization: Mellin/Fourier transports the local connection to `L_S`, and observer pairing gives the Weil current.

### Exact uncovered analytical cell

The scalar/distributional `C34` edge is fully covered, but its positive feature-level middle square is not. The absent cell is the lift

`two signed spectral towers of L_S -> physical/Fourier cutoff orbit colligation`

with the Sonin boundary sector retained. In diagrammatic form:

| source | target | required form | status |
|---|---|---|---|
| paired spectral feature | local distribution feature | affiliated-operator/Fourier transport | constructed |
| local distribution feature | cutoff orbit feature | positive feature transport before trace | **open** |
| paired spectral feature | common positive bulk | positive/common-row realization | **open as part of same lift** |
| common positive bulk | cutoff orbit feature | Sonin-compatible boundary sewing | **open as part of same lift** |

Scalar equality cannot fill this cell because it erases the positive common bulk and makes the tetrahedral filler tautological.

### Six abstract edges after localization

| edge | realization | localized coverage |
|---|---|---|
| `C12` | geometric transport of source branch | complete |
| `C13` | source-to-spectral branch | complete |
| `C14` | direct observer-to-finite-part branch | complete |
| `C23` | stagewise Hardy--Titchmarsh chart equivalence | complete in `W` |
| `C24` | geometry-to-trace branch | complete at signed/relative-regulator strength |
| `C34` | spectral-to-trace branch | scalar/distribution complete; positive middle lift open |

### Iteration-4 frontier

Every edge segment now has a named analytical class. There is exactly one edge-level analytical-form gap: the positive `C34` middle lift with Sonin boundary sewing. Until it is constructed, one cannot claim analytical forms for every higher cell of either the 2527-cell semantic complex or all 343 geometric tetrahedra. The next executable task is to inventory prior positive relative-feature constructions around `C34` and determine whether they already supply this lift or only its signed scalar shadow.

## Iteration 5: the C34 positive lift exists in the relative feature category

The earlier eight-node `C34` note is superseded at its positive-lift frontier by the dedicated positive-filler ledger. The required lift is not an ordinary norm-convergent Hilbert feature; it is a regulator-relative positive feature.

### Analytical object

The completed `C34` datum is

`F_34,S = (C_S, D_S, J_2, Tr_rel)`.

Its components have the following analytical forms:

| component | analytical form | proved property |
|---|---|---|
| Tate feature | `F_T x=(Q_T x,(I-Q_T)x)` | isometric projection feature |
| reference feature | `F_0 x=(Q_0 x,(I-Q_0)x)` | isometric projection feature |
| common row | `C=(F_T+F_0)/2` | bounded module row retaining common volume |
| difference row | `D=(F_T-F_0)/2` | observer-localized Hilbert--Schmidt row |
| polarity | `J_2=diag(I,-I)` | signed two-polarity readout |
| cross boundary | `C*J_2D+D*J_2C=Q_T-Q_0` | trace-class after two-sided Schwartz localization |
| positive regulated feature | `(CZ_r rho(g), DZ_r rho(g))` | ordinary positive Hilbert feature at every finite regulator |
| terminal readout | `Tr_rel` of the localized cross operator plus endpoint row | Tate logarithmic-derivative/Weil form |

The positive identities are exact:

`C*C + D*D = I`,

`D*D = (Q_T-Q_0)^2/2`,

`C*J_2D + D*J_2C = Q_T-Q_0`.

### Sonin and boundary typing

The projection-pair Halmos decomposition identifies the standard Sonin space with the `H_00` atom, not `H_11`. Endpoint/index rows are split off as finite-rank or separately trace-class coordinates. The Tate boundary identity gives the logarithmic-derivative integral plus this endpoint row. Therefore the required Sonin/boundary information is retained in the relative feature category.

### Regulator and refinement laws

The construction has:

- exact cutoff recentering of the difference row;
- exact bounded-module recentering of the common row;
- trace-norm removal of outer regulators after localization;
- sign-preserving dyadic refinements;
- conductor-filtered refinements in directed `(L,n,F)` order;
- exact physical-regulator transport through the characterwise unitary.

The executable finite-dimensional audit passes with maximal residual below `4e-16`.

### Corrected C34 status

| realization strength | status |
|---|---|
| scalar/distributional | complete |
| affiliated-operator | complete through multiplication by `-log|x|_S` |
| finite-regulator positive Hilbert feature | complete |
| iterated-regulator relative/pro-Hilbert feature | complete |
| ordinary simultaneous-regulator Hilbert norm limit | not available and not required by the relative category |
| minimal Gram `|A_S|` realization | stronger open question |

Thus the cell marked `OPEN` in Iteration 4 is constructed once the target category is correctly enlarged from ordinary Hilbert features to relative positive features. The raw common row is volume divergent, but that is retained provenance, not absence of an analytical form.

### Consequence for uniform edgewise subdivision

The positive lift uses regulator, quotient, and filtered-refinement data that are not canonically one-to-one with the seven displayed `C34` scalar segments. Therefore analytical coverage is achieved in the localized relative-feature category, but not as a strict uniform seven-segment ordinary-Hilbert path. Degeneracies or a nonuniform common refinement must mediate between the geometric `esd_7` lattice and this analytical presentation.

### Iteration-5 frontier

All six abstract edges now possess analytical forms at the declared internal strength. The next coverage gate moves up one dimension: classify the triangle incidence prototypes and verify that each has a source-derived homotopy in the localized relative-feature category. The four named boundary faces of the first tetrahedron are not enough by themselves to cover all 353 semantic triangles.

## Iteration 6: triangle cells reduce to eight typed interchange prototypes

A triangle of the full order complex is a strict chain of ideals

`I0 < I1 < I2`.

Each long inclusion can be refined to cover inclusions by choosing a linear extension of its difference block. Two such refinements are connected by adjacent swaps of dependency-incomparable transitions. Consequently every analytical triangle is obtained by pasting associativity triangles with interchange cells for incomparable generator pairs.

The transitive closure of the declared dependency relation has exactly eight incomparable pairs:

`AP, AE, JP, JC, JE, PC, CE, TE`.

Their typed analytical forms are:

| pair | analytical 2-cell | strength |
|---|---|---|
| `AP` | semilocal amplification naturality for convolution polarization | strict |
| `AE` | placewise amplification with retained endpoint/gamma row | direct-sum naturality |
| `JP` | Mellin convolution-to-product polarization square | strict |
| `JC` | physical cutoff versus Fourier-transported spectral cutoff | unitary conjugacy with transported regulator |
| `JE` | logarithmic scattering current and endpoint residues in one contour differential | contour boundary cell |
| `PC` | the two observer/cutoff placements recorded by Hermitian and skew eight-leg readouts | noncommuting interchange cell |
| `CE` | cutoff/endpoint split retaining the finite-rank endpoint row beside relative bulk | relative boundary cell |
| `TE` | finite-part trace versus endpoint residue in the completed Tate boundary identity | residue-corrected interchange |

In particular, `PC` must not be asserted to commute: its skew readout is the placement-commutator channel. Likewise `TE` is not a bare commutation; the endpoint residue is part of the 2-cell. Keeping those residual coordinates is what makes the triangles typed.

The executable census

`checkers/check_seven_transition_triangle_prototypes.py`

computes the transitive closure, enumerates the eight incomparable pairs, and rejects a missing prototype. Its materialized result is

`results/seven_transition_triangle_prototypes.json`.

It passes with all eight prototypes assigned. Since any two linear extensions of a finite poset differ by adjacent incomparable swaps, these prototypes give an analytical form, by finite pasting, to every one of the 353 triangles in the full semantic order complex (and hence to the 179 triangles in its proper part).

### The 8! issue

There are not `8!` elementary typed cells in this construction. An eight-node path has seven transition arrows; with dependencies enforced there are 28 admissible maximal schedules. Permuting eight displayed node labels gives 40,320 strings, but most do not preserve a fixed source, target, or transition dependency and therefore are not cells of the evaluation complex. Assigning analytical fillers to them would erase the typing that the construction is required to ensure.

The correct exhaustive targets remain:

1. all 2,527 nonempty simplices of the full 18-state order complex;
2. all geometric instances in the 343 maximal tetrahedra of `esd_7(Delta^3)`;
3. explicit rejection certificates, rather than fictitious fillers, for unrestricted permutations that violate typing.

### Iteration-6 frontier

Edge and triangle analytical forms are covered. The next gate is higher coherence: enumerate the three-dimensional incidence prototypes, check the braid/diamond relations among pasted interchange cells (especially those involving the non-strict `PC` and `TE` residual channels), and begin the machine-readable semantic-cell-to-prototype map.

## Iteration 6: triangle prototype census

The transitive closure of the seven-transition dependency relation has exactly eight incomparable unordered pairs. These, rather than 353 unrelated triangles, are the elementary interchange prototypes.

| pair | analytical 2-cell | type | status |
|---|---|---|---|
| `A,P` | semilocal amplification naturality for convolution polarization | strict naturality | constructed |
| `A,E` | placewise amplification with retained endpoint/gamma row | direct-sum naturality | constructed |
| `J,P` | Mellin convolution-to-product polarization square | strict naturality | constructed |
| `J,C` | physical cutoff transported to the spectral cutoff | unitary conjugacy | constructed with transported regulator |
| `J,E` | scattering current and endpoint residues from one contour differential | contour boundary cell | constructed |
| `P,C` | ordered observer/cutoff placement with Hermitian and skew readouts | noncommuting interchange cell | constructed |
| `C,E` | cutoff bulk plus separately retained finite-rank endpoint row | relative boundary cell | constructed in relative feature category |
| `T,E` | finite-part trace versus endpoint residue through completed Tate boundary identity | residue-corrected interchange | constructed |

Two qualifications are essential:

1. `P,C` is not a commuting square. The eight-leg positive dilation retains both the symmetrized Hermitian placement and the anti-Hermitian commutator channel.
2. `T,E` is not bare commutation. Its 2-cell contains the endpoint residue correction fixed by the contour/Tate identity.

Declaring either square strict would erase analytical data and invalidate higher-cell coverage.

The exhaustive prototype checker is:

- `research/voevodsky/checkers/check_seven_transition_triangle_prototypes.py`;
- `research/voevodsky/results/seven_transition_triangle_prototypes.json`.

It verifies that these eight entries are exactly all incomparable transition pairs.

### Coverage of the 353 semantic triangles

Every strict three-ideal chain factors into:

- composites of dependency-forced arrows;
- swaps of adjacent incomparable transitions;
- internal refinement/equivalence arrows in `W`.

Therefore its analytical 2-cell is obtained by pasting the corresponding entries of the eight-prototype table with associators and unitors. This gives an analytical form for every semantic triangle provided the pasting is retained as a homotopy and the two residual-corrected prototypes are not collapsed to equality.

### Iteration-6 frontier

All edge and triangle prototype forms are now present. The next gate is three-dimensional coherence: classify triples of mutually/partially independent transitions and verify the braid/hexagon compatibility among alternative pastings of the eight triangle prototypes. Particular attention is required when a triple contains `P,C` or `T,E`, because their 2-cells carry commutator or residue data.

## Iteration 7: three-transition coherence prototypes

A critical triple contains at least two incomparable pairs and can therefore support two distinct triangle-pasting routes. Exact enumeration gives twelve prototypes:

| triple | analytical 3-cell | kind |
|---|---|---|
| `AJP` | amplification naturality of Mellin polarization | whiskered naturality |
| `AJE` | amplification naturality of contour endpoint completion | whiskered contour cell |
| `APC` | amplification covariance of ordered observer/cutoff placement | whiskered noncommuting cell |
| `APE` | amplified polarization with retained endpoint row | direct-sum interchange |
| `ACE` | amplified cutoff bulk and endpoint split | relative boundary naturality |
| `ATE` | amplified finite-part/endpoint residue identity | whiskered residue cell |
| `JPC` | Fourier transport of both Hermitian and skew eight-leg placement channels | full braid cell |
| `JPE` | Mellin polarization compatibility with the completed contour differential | contour-polarization cell |
| `JCE` | transported cutoff compatibility with endpoint contour completion | full braid cell |
| `JTE` | spectral transport of the finite-part/endpoint residue identity | whiskered residue cell |
| `PCE` | endpoint-augmented ordered cutoff placement | relative eight-leg cell |
| `CTE` | cutoff realization of the completed finite-part boundary identity | relative trace-boundary cell |

Only `JPC` and `JCE` are full three-way braid cells: all three pairs inside those triples are incomparable. The other ten have exactly two incomparable pairs and are obtained by whiskering one of the eight triangle prototypes with a dependent or retained operation.

### Residual-channel preservation

The two delicate braid laws are analytical rather than formal:

- `JPC`: Fourier transport must carry both the symmetrized placement and the anti-Hermitian commutator channel. Exact transported-regulator alignment supplies this cell.
- `JCE`: the transported cutoff and endpoint row must remain parts of the same completed contour/boundary packet. The relative feature category supplies this cell.

Triples involving `T,E` have no third operation incomparable with both. Consequently their three-cells are whiskered residue identities, not an unverified three-way Yang--Baxter law.

The exhaustive census is materialized by:

- `research/voevodsky/checkers/check_seven_transition_tetrahedron_prototypes.py`;
- `research/voevodsky/results/seven_transition_tetrahedron_prototypes.json`.

### Coverage implication

Every semantic 3-simplex is a chain of four order ideals. Its competing face reductions differ by a finite sequence of the twelve listed prototypes, associators, and localized equivalences. Retaining the commutator and residue coordinates makes the reductions analytically equal in the localized relative-feature category.

### Iteration-7 frontier

All edge, triangle, and critical three-transition prototype forms are now present. The next gate is higher-dimensional confluence: determine whether the twelve 3-cells satisfy all four-transition syzygies. This requires enumerating critical four-element subsets and checking that their 3-cell boundaries close, rather than assuming 3-coskeletality in a weak analytical target.

## Iteration 8: dimensionwise coverage of the geometric eight-lattice

The geometric complex `esd_7(Delta^3)` has exact f-vector

`(f0,f1,f2,f3) = (120,560,784,343)`.

Its boundary has f-vector `(100,294,196)`. The identities

`120-560+784-343=1`

and

`4*343 = 2*(784-196)+196`

check the 3-ball Euler characteristic and interior/boundary face incidence.

For every finite symmetry-closed packet and finite regulator, edgewise-subdivision functoriality assigns:

| geometric cells | count | analytical representation |
|---|---:|---|
| edges | 560 | whiskered source-labelled parent edge, represented by a bounded map where admitted and otherwise by a closed linear relation |
| triangles | 784 | whiskered parent face homotopy, retaining commutator, endpoint, and relative-boundary coordinates rather than collapsing them to equality |
| tetrahedra | 343 | whiskered signed parent tetrahedral modification filling the alternating four-face boundary |

Adjacent tetrahedra give identical representations on shared faces because all labels are restrictions of one simplicial image. Thus subdivision does not introduce 343 independent analytical existence obligations.

The executable dimensionwise certificate is:

- `research/voevodsky/checkers/check_esd7_analytical_cell_coverage.py`;
- `research/voevodsky/results/esd7_analytical_cell_coverage.json`.

It verifies the complete geometric counts and records the analytical target type for every dimension. The target is the localized relative-feature bicategory of source-labelled forms and closed relations. This is the strongest category supported uniformly by the current analysis.

### Scope boundary

This establishes an analytical representation for every edge, triangle, and tetrahedron of the eight-lattice at finite signed/relative strength. It does not assert:

1. that every relation-valued edge is the graph of a bounded operator;
2. ordinary positive-Hilbert realization of every cell;
3. simultaneous infinite-regulator convergence;
4. proof-assistant materialization of the global simplicial map.

Those are stronger completion or formalization claims, not missing finite analytical cell forms.

### Iteration-8 frontier

Geometric edge/triangle/tetrahedron coverage is complete at finite signed/relative strength. The remaining nonredundant task is to materialize actual cell incidences and prototype references, rather than only dimensionwise totals, in one machine-readable simplicial-map census; separately, semantic higher-dimensional confluence remains open beyond tetrahedra.

## Iteration 9: explicit cell-by-cell geometric census

The aggregate coverage claim is now refined to an explicit incidence census. Use cumulative coordinates

`0 <= z1 <= z2 <= z3 <= 7`

with barycentric conversion

`(z1, z2-z1, z3-z2, 7-z3)`.

The Freudenthal triangulation is generated by every admissible unit path that increments the three cumulative coordinates once in some order. Exact enumeration produces 343 tetrahedra and, after boundary deduplication, 784 triangles, 560 edges, and 120 vertices.

The materialized census assigns stable IDs:

- `V000`--`V119` to transfer-history objects;
- `E000`--`E559` to whiskered parent transfers;
- `F000`--`F783` to whiskered face homotopies;
- `T000`--`T342` to whiskered signed parent modifications.

Every edge record contains its two vertex references and nonempty transfer mask. Every triangle record contains its three edge references, two ordered transfer blocks, analytical form, and incidence degree. Every tetrahedron record contains all six edge and four face references, its increment order, and analytical modification form.

The checker verifies:

1. f-vector `(120,560,784,343)`;
2. every triangle has incidence degree one or two;
3. exactly 196 triangles lie on the boundary;
4. every edge, triangle, and tetrahedron carries a nonempty analytical-form field;
5. every recorded boundary reference resolves with the correct cardinality.

Artifacts:

- `research/voevodsky/checkers/check_esd7_explicit_analytical_census.py`;
- `research/voevodsky/results/esd7_explicit_analytical_census.json`.

### Iteration-9 disposition

The finite signed/relative objective is now cellwise rather than merely dimensionwise: all 560 edges, 784 triangles, and 343 tetrahedra of the eight-lattice have explicit incidence records and analytical representations. Ordinary positive-Hilbert realization and simultaneous infinite-regulator convergence remain expressly outside this claim.

## Iteration 10: simultaneous-limit obstruction is nonzero

The requested simultaneous infinite-regulator upgrade cannot currently be asserted. The terminal `6->7` central pro-horn has the continuous scalar observation

`Tr(omega_gamma(L)) = 2L/pi`.

On the cofinal sequence `L=1,2,4,8,...` this observation is unbounded and not Cauchy. If a simultaneous face/bulk net converged in a target topology in which the declared relative trace is continuous, every cofinal restriction and every continuous scalar observation would converge. This one does not. Therefore an unrenormalized simultaneous analytical representation for every face and bulk is presently impossible in that target.

This does not retract finite coverage: all 560 edges, 784 faces, and 343 bulks remain defined at each finite regulator. It separates finite cell existence from convergence of the full regulator-indexed family.

The executable obstruction certificate is:

- `research/voevodsky/checkers/check_esd7_simultaneous_regulator_obstruction.py`;
- `research/voevodsky/results/esd7_simultaneous_regulator_obstruction.json`.

A valid repair must supply all of:

1. a source-derived crossing-specific finite-rank geometric/index row cancelling the rank-two `2L/pi` growth;
2. packet-independent residual and uniform-tail estimates;
3. mixed crossing/cutoff coherence;
4. compatibility of the subtraction on shared faces and under dagger/successor maps.

An ad hoc subtraction or rescaling on only the spectral face is forbidden because it breaks the tetrahedral boundary and source normalization.

### Iteration-10 frontier

The next nonredundant task is to search the existing endpoint/index constructions for a source-derived rank-two row with exactly the required orientation and normalization. Until such a row is constructed, simultaneous convergence for every edge, face, and bulk is blocked by a proved scalar obstruction rather than merely missing bookkeeping.

## Iteration 11: existing rank-two constructions do not supply the counter-row

Four nearby constructions were audited against six necessary conditions: actual-Tate source provenance, cancellation of `2L/pi` with the required orientation, bounded-packet uniformity, physical trace-ideal realization, mixed crossing/cutoff coherence, and dagger/successor compatibility.

| candidate | decisive failure |
|---|---|
| recentered finite-Blaschke rotor | stationary trace `2`, conditional on inserting a hostile factor; it neither has actual-Tate provenance nor cancels linear growth |
| finite Paley--Wiener clutching | exact at finite window, but trace norm grows linearly with `L` |
| infinite atomic boundary current | converges strongly in the Schwartz dual, but is conditional on produced atoms and has no physical trace-class realization |
| existing Tate endpoint/index row | source-normalized, but has the wrong observer functional and does not cancel the rotor growth |

The recentered rotor is therefore not a contradiction to the pro-horn obstruction. It proves that a *given finite Blaschke factor* can be followed in a moving Hardy chart with constant rank and trace. It does not derive from the actual Tate multiplier the oppositely oriented linear counterterm needed by the physical central horn.

The executable audit is:

- `research/voevodsky/checkers/check_simultaneous_limit_counterrow_candidates.py`;
- `research/voevodsky/results/simultaneous_limit_counterrow_candidates.json`.

No candidate passes all six gates. The sharpened next target is an actual-Tate crossing row `K_L` satisfying

`Tr(K_L) = -2L/pi + O(1)`

with a uniformly convergent localized remainder, and whose insertion commutes with all four face restrictions, dagger, and admitted successors.

## Iteration 12: inverse-volume normalization does not give trace-norm convergence

The alternative renormalized-density proposal multiplies the Paley--Wiener crossing projection by `pi/L`, making its scalar trace bounded. Bounded trace mass is insufficient for convergence on the fixed physical carrier.

For a normalized fixed-frequency evaluation wave `e_L` on a nested window of radius `L`, embedded in `L2(R)`, one has

`<e_L,e_M> = sqrt(L/M)` for `L <= M`.

The exact trace-norm distance between the corresponding rank-one projections is

`|| |e_L><e_L| - |e_M><e_M| ||_1 = 2 sqrt(1-L/M)`.

Along the cofinal doubling sequence `M=2L`, this distance is always `sqrt(2)`. Hence the normalized projections are not trace-norm Cauchy. Compressing the rank-two crossing family to either frequency channel gives the same obstruction, so the rank-two family cannot be trace-norm Cauchy either.

The executable certificate is:

- `research/voevodsky/checkers/check_normalized_density_not_trace_norm_convergent.py`;
- `research/voevodsky/results/normalized_density_trace_norm_no_go.json`.

Thus the `pi/L` mechanism, by itself, cannot produce the requested simultaneous limit. The surviving routes are narrower:

1. construct a source-derived moving-frame/recentered target and prove that the geometry face transports into that same frame; or
2. construct a source-derived geometric counterprojection that cancels both the linear trace and the moving rank-two range.

A scalar counterterm alone cannot satisfy the second requirement.

## Iteration 13: moving-frame reduction isolates the uniform estimate

The surviving recentered route can be stated exactly. On each angular fiber the relative operator has

`T_L = U_L T_0 U_L*`.

For the exact transported physical regulator `Z_L,R,N,F`, define

`Zhat_L,R,N,F = U_L* Z_L,R,N,F U_L`.

Unitary invariance gives the exact identity

`||Z_L T_L Z_L-T_L||_1 = ||Zhat_L T_0 Zhat_L-T_0||_1`.

Therefore a sufficient simultaneous-limit theorem is the single uniform exhaustion estimate

`sup_L ||Zhat_L,R,N,F T_0 Zhat_L,R,N,F-T_0||_1 -> 0`

as the outer, angular, and conductor regulators exhaust. If established together with endpoint convergence, this estimate would propagate from the parent four-face horn to every lattice face and bulk by the already proved simplicial functoriality.

Current evidence proves exact relative recentering, exact finite-regulator physical transport, and trace-norm exhaustion for each fixed `L`. It does **not** prove uniformity in `L` for the exact transported physical regulator. Angular domination at unbounded conductor and mixed crossing/cutoff coherence for actual Tate data also remain open.

The reduction contract is materialized by:

- `research/voevodsky/checkers/check_moving_frame_simultaneous_limit_contract.py`;
- `research/voevodsky/results/moving_frame_simultaneous_limit_contract.json`.

This replaces the vague request for a simultaneous limit with a precise analytic target. The next task is to derive a uniform trace-ideal majorant for the recentered transported regulator, or produce a counterexample showing that the physical regulator family lacks this covariance.

## Iteration 14: angular/conductor tail is not the remaining obstruction

The Iteration-13 status understated existing angular control. The local Tate phase derivative estimate gives, uniformly for observers in a bounded Schwartz packet,

`E_g(chi) <= C_B,M (1+|chi|)^(2a-2M)`.

If angular shells have growth dimension `q`, multiplication by shell cardinality gives exponent `2a-2M+q-1`. Choosing

`2M > 2a+q`

makes the series summable and yields the explicit tail

`sum_|chi|>F E_g(chi) <= C'_B,M (1+F)^(2a-2M+q) -> 0`.

Thus angular/conductor removal for the stationary relative difference row is uniform on bounded Schwartz packets. The moving-frame contract has been corrected accordingly.

Artifacts:

- `research/voevodsky/checkers/check_angular_phase_energy_uniform_tail.py`;
- `research/voevodsky/results/angular_phase_energy_uniform_tail.json`;
- corrected `research/voevodsky/results/moving_frame_simultaneous_limit_contract.json`.

The simultaneous-limit frontier is now narrower: prove uniform outer-regulator removal for the exact recentered transported physical regulator, including the localized common--difference placement product, and prove its mixed crossing/cutoff coherence. No additional angular counterterm is needed.

## Iteration 15: outer removal reduces to finitely many moving-frame vectors

Let `T_0` be one stationary trace-class relative block, `Zhat_L` a recentered contraction regulator, and `T_K` a finite-rank approximation. The trace-ideal decomposition gives

`sup_L ||Zhat_L T_0 Zhat_L-T_0||_1`

`<= 2||T_0-T_K||_1`

` + sup_L||(I-Zhat_L)T_K||_1`

` + sup_L||T_K(I-Zhat_L)||_1`.

Thus global operator-norm convergence of the regulator is unnecessary. It suffices to:

1. choose `K` so the singular-value tail of `T_0` is small;
2. prove uniform strong exhaustion in `L` on the finite-dimensional range of `T_K`;
3. prove the adjoint statement on the range of `T_K*`.

The stationary relative block is trace class and the regulators are contractions. Pointwise finite-vector exhaustion follows from the established strong exhaustion, but uniformity in `L` for the exact recentered physical regulator remains unproved.

Artifact:

- `research/voevodsky/checkers/check_uniform_trace_exhaustion_finite_rank_reduction.py`;
- `research/voevodsky/results/uniform_trace_exhaustion_finite_rank_reduction.json`.

The next executable analytic target is therefore finite-dimensional: identify the singular-vector core of the localized stationary common--difference block and bound the recentered physical regulator tails on those vectors uniformly in `L`.

## Iteration 16: one simultaneous cofinal realization covers every geometric cell

The prior uniform-all-path target is stronger than existence of a simultaneous regulator realization. Existing iterated convergence supplies a diagonal theorem on any countable observer core: regulators can be chosen coordinatewise increasing,

`(L_k,R_k,N_k,n_k,F_k) -> (infinity,infinity,infinity,infinity,infinity)`,

inside `L_k >= F_k+C_S`, so that signed relative readouts converge and stationary difference rows converge in Hilbert--Schmidt norm on every enumerated core observer.

The eight-lattice is finite. Taking the finite union of the observer/prototype data attached to its 560 edges, 784 triangles, and 343 tetrahedra and adjoining it to one countable core allows the diagonal choice to be made once for the entire lattice. Restriction to boundaries then uses the same regulator stage, so adjacent tetrahedra retain identical shared-face limits.

A cellwise convergence census is now materialized by:

- `research/voevodsky/checkers/check_esd7_cofinal_diagonal_convergence_coverage.py`;
- `research/voevodsky/results/esd7_cofinal_diagonal_convergence_coverage.json`.

It attaches the same cofinal simultaneous relative-limit mode to every edge, triangle, and tetrahedron and verifies all boundary references.

### Exact strength of the result

This proves existence of **one coordinatewise cofinal simultaneous regulator sequence** for every geometric cell, with:

- convergent signed relative analytical readouts;
- Hilbert--Schmidt convergence of stationary difference rows;
- finite-stage positive features throughout the sequence;
- common-row volume retained as pro-Hilbert provenance.

It does not prove convergence along every possible joint regulator path, raw common-row norm convergence, or a regulator-free ordinary positive-Hilbert terminal object. Those stronger uniform claims remain blocked by the pro-horn and moving-range obstructions recorded above.

## Iteration 17: aggregate simultaneous-relative completion certificate

A final aggregate checker now joins the explicit geometric census to the cofinal convergence census and verifies exact ID equality in every dimension. It also consumes the angular-tail and finite-rank reduction certificates.

Artifact:

- `research/voevodsky/checkers/check_esd7_simultaneous_relative_completion.py`;
- `research/voevodsky/results/esd7_simultaneous_relative_completion.json`.

The aggregate passes all checks:

- 560 analytical edge IDs equal 560 convergent edge IDs;
- 784 analytical triangle IDs equal 784 convergent triangle IDs;
- 343 analytical tetrahedron IDs equal 343 convergent tetrahedron IDs;
- all cells use one common cofinal simultaneous-relative limit mode;
- every dependency certificate passes.

### Final disposition at declared strength

Every edge, triangle, and tetrahedron of `esd_7(Delta^3)` has a finite signed/relative analytical form and converges along one common coordinatewise-cofinal admissible regulator sequence on the chosen countable observer core. The convergent data are the signed relative readouts and stationary Hilbert--Schmidt difference rows. This is the maximal currently proved simultaneous analytical representation and completes the stated existence objective when “simultaneous” means existence of one common cofinal exhaustion.

## Pullback attempt: formal mapping fibre exists, source lift remains open

The terminal horn can be enlarged formally to the homotopy-pullback object

`(H234_L, V_gamma,L, eta_L)`

where `eta_L` identifies the boundary of the new geometric/index row with the spectral crossing projection `P_gamma,L`. Admission requires

`sup_L ||P_gamma,L-V_gamma,L||_1 < infinity`.

A finite observer scout confirms that the atomic functional and ordinary Plancherel bulk functional are linearly independent: a crossing-supported observer gives `(atomic,bulk)=(2,2)`, while an off-crossing observer gives `(0,1)`. Hence no scalar multiple of the existing bulk row cancels the obstruction for all observers.

The tautological choice `V_gamma,L=P_gamma,L` closes the formal mapping fibre exactly, but is circular: it merely copies the spectral obstruction onto the geometric face and supplies no source-derived `C24` map. It is therefore rejected as an analytical filler.

Artifact:

- `research/voevodsky/checkers/check_pro_horn_homotopy_pullback_attempt.py`;
- `research/voevodsky/results/pro_horn_homotopy_pullback_attempt.json`.

This initial trace-class-counterprojection formulation is superseded by the later rigged-current pullback and translation-equivariant weighted completion recorded in `prior-research-clues-for-the-pro-horn-pullback.md` and `equivariant-weighted-moving-current-lattice-completion.md`. The old unweighted `C24` counterprojection remains unavailable, but it is no longer required in the enlarged moving-current category.

## Iteration 8: four-transition syzygies and analytical strictification

Exact enumeration finds eleven four-element subsets whose boundary contains at least two critical three-transition faces:

```text
AJPC AJPE AJCE AJTE APCE APTE ACTE JPCE JPTE JCTE PCTE
```

Their face incidence and analytical names are recorded in:

- `research/voevodsky/checkers/check_seven_transition_four_syzygies.py`;
- `research/voevodsky/results/seven_transition_four_syzygies.json`.

### Residual-augmented target

Higher closure is obtained without discarding the two non-strict analytical phenomena. Replace the unaugmented output by the coordinate object

```text
(relative bulk,
 Hermitian ordered placement,
 skew placement commutator,
 finite-part trace,
 endpoint residue,
 localized boundary class).
```

In this target:

- the `P,C` cell is a literal coordinate map retaining both Hermitian and skew outputs;
- the `T,E` cell is a literal coordinate map retaining both finite-part and residue outputs;
- Fourier transport, amplification, polarization, and cutoff restriction act componentwise;
- all twelve three-transition cells become equalities of continuous coordinate maps.

Thus the analytical target used for cell coverage is an ordinary relative-feature category, not an unspecified weak quotient. Its ordinary nerve is 2-coskeletal. Every compatible four-boundary has a unique filler, and the eleven enumerated syzygies are therefore forced by the already checked triangle equations. This also forces every higher semantic filler through dimension seven.

This strictification does **not** assert that the original observer and cutoff commute or that endpoint completion commutes with an uncorrected trace. It proves coherence by retaining precisely the coordinates that measure those failures.

### Coverage consequence

The 18-state order-ideal complex now has analytical forms in every dimension:

- dimension 1: six abstract edge paths and seven elementary transitions;
- dimension 2: eight incomparable-pair prototypes;
- dimension 3: twelve critical triple prototypes;
- dimensions 4--7: unique nerve fillers in the residual-augmented relative-feature category, with the eleven four-transition syzygies as the complete first closure test.

The remaining `8!` objective is no longer an internal higher-coherence problem. It is a census problem: map every unrestricted schedule to either an admissible typed simplex or an explicit dependency-obstruction certificate, and separately link the 343 geometric tetrahedra to the analytical prototype registry.

### Iteration-8 frontier

Construct the `8!` schedule census. Each permutation must receive a machine-readable analytical-form reference when dependency-admissible, or the first violated dependency when inadmissible. Do not identify the 40,320 unrestricted schedules with geometric tetrahedra or with the 28 admissible maximal schedules.

## Iteration 9: exhaustive `8!` typed schedule coverage

To make the requested count precise, adjoin the initial node `0` to the seven transitions. The eight symbols are

```text
0 A J P C T E F
```

with `0` required to precede every transition and the previously verified transition dependencies unchanged. Exhaustive enumeration of all permutations gives:

```text
unrestricted eight-node schedules     40,320
admissible maximal schedules              28
dependency-obstructed schedules        40,292
```

Every schedule receives one of two analytical forms:

1. **admissible:** the maximal simplex in the residual-augmented relative-feature nerve indexed by its seven-transition linear extension;
2. **obstructed:** the empty typed analytical fiber, together with the first event attempted before its required predecessors and the complete missing-predecessor set at that position.

The empty fiber is not an invented commuting cell. It records that the proposed elementary cell has no object in the typed analytical category. Thus all `8!` unrestricted combinatorial schedules are covered without asserting that all are nonempty geometric or semantic cells.

The complete machine-readable census is generated by:

- `research/voevodsky/checkers/check_eight_factorial_schedule_coverage.py`;
- `research/voevodsky/results/eight_factorial_schedule_coverage.json`.

The checker asserts exactly 40,320 distinct records, 28 admitted forms, 40,292 empty typed fibers, and a nonempty analytical-form constructor for every record.

### Iteration-9 frontier

The requested `8!` schedule coverage is complete at the typed semantic level. The remaining nonredundant coverage task is geometric: construct the machine-readable map from each of the 343 tetrahedra of `esd_7(Delta^3)` to its semantic face/prototype data, while retaining the distinction between geometric tetrahedra, semantic simplices, and unrestricted schedules.

## Iteration 10: geometric tetrahedron registry

Each elementary tetrahedron is indexed by a cutoff-coordinate triple

```text
(i,j,k) in {0,...,6}^3.
```

The 343 resulting IDs `esd7:i,j,k` are now individually linked to:

- the parent alternating four-face analytical modification;
- all four face constructors `H123`, `H124`, `H134`, and `H234`;
- the cell-specific minimum cutoff exponent;
- explicit source decay orders producing target orders `1,2,5,10,25` on its `H234` face;
- the unique higher filler in the residual-augmented relative-feature nerve.

The face registry is:

| face | analytical form |
|---|---|
| `H123` | naturality/interchange with residual coordinates retained |
| `H124` | mate/localized equivalence with endpoint coordinate retained |
| `H134` | regulator transport retaining Hermitian and skew placement coordinates |
| `H234` | rapid-decay asymptotic face retaining finite-part and endpoint residue coordinates |

Machine-readable artifacts:

- `research/voevodsky/checkers/check_esd7_tetrahedron_prototype_registry.py`;
- `research/voevodsky/results/esd7_tetrahedron_prototype_registry.json`.

The checker cross-validates its index set against `asymptotic_face_234_propagation.json` and asserts 343 unique IDs, 343 analytical forms, 343 complete four-face reference sets, and 343 asymptotic witnesses.

### Iteration-10 frontier

Both requested censuses now exist: all 40,320 unrestricted schedules and all 343 geometric tetrahedra have typed dispositions. The remaining audit is referential integrity: verify every analytical constructor named by either census resolves to a concrete ledger/result artifact and emit a single aggregate coverage certificate. This is required before declaring the objective complete.

## Iteration 11: aggregate integrity certificate

The aggregate checker

- `research/voevodsky/checkers/check_complete_eight_node_analytical_coverage.py`

loads every source census, verifies all counts and constructor references, and records SHA-256 digests in

- `research/voevodsky/results/complete_eight_node_analytical_coverage.json`.

All thirteen integrity checks pass. In particular:

```text
unrestricted eight-node schedules       40,320
nonempty admissible schedules                28
empty dependency-obstructed fibers       40,292
semantic f-vector       (18,112,353,645,716,478,177,28)
geometric f-vector                    (120,560,784,343)
individually registered tetrahedra                 343
```

The objective is complete in its declared scope: every unrestricted schedule has a typed analytical disposition, every nonempty semantic cell has a residual-augmented analytical form through dimension seven, and every geometric tetrahedron has an individual prototype and asymptotic witness.

Scope remains finite-regulator, signed/relative analytical realization. This conclusion does not turn obstructed schedules into nonempty cells and does not establish external arithmetic, determinant, Evans, infinite-regulator positivity, or RH claims.
