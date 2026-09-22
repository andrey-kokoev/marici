# Valid triangular faces need not fill a typed coherence tetrahedron

## Result

The next coherence layer now has a portable finite fixture. It retains four triangular face witnesses and verifies their compatibility around a tetrahedron, rather than merely checking six edge maps.

Two examples are verified across two coordinate stages:

- **FILLED:** the two face pastings differ by the boundary of an explicit degree-two filler;
- **OBSTRUCTED:** every face is valid, but no admitted module-linear degree-two filler can identify the two pastings.

A further negative test has a valid filled tetrahedron at each stage but incompatible transport of the chosen witnesses between stages.

This demonstrates a genuine obligation beyond commuting matrices. It is NOT yet an identification of the main productization, observer, comparison and higher-comparison towers with four concrete domain presentations.

## 1. Typed setting, not four untyped labels

The verifier first runs Voevodsky's independent structural gain-square verifier on the complete structural fixture at each stage. See `../voevodsky/whole-row-gain-squares-have-a-portable-typed-structural-certificate.md`.

The upper module E has basis `(b,a,n,l,z)` and commuting square-zero actions

`left_t: b -> a, n -> l`,

`right_t: b -> n, a -> l, z -> l`.

At each of the four presentations form the homological chain complex

`C_2=E --left_t--> C_1=E --left_t--> C_0=E`.

The equation `left_t^2=0` is independently checked. Each degree retains the structural subspaces K, M, N and L. Every edge, face component and filler must intertwine BOTH actions and preserve all four subspaces.

These are complexes in a declared filtered-module setting. The fixture's joint-action ideal is not identified with the physical observer's ideal. Nor is this new three-term complex identified with the original filtered pushout extension; that extension remains independently checked by the structural verifier.

The four vertices, ordered `(00,10,01,11)`, are presentations of this SAME complex. They are not four sequential operations. Their six comparison maps are bound to the common source coordinates by

`F_ij D_i = D_j`.

Thus the additional diagonal and cross edge of the tetrahedron cannot be supplied as arbitrary matrices unrelated to the structural source.

## 2. Four faces retain their witnesses

For each i<j<k a face supplies degree-one components

`H_ijk,0 : C_i,0 -> C_k,1`,

`H_ijk,1 : C_i,1 -> C_k,2`.

They must satisfy

`delta(H_ijk) = F_jk F_ij - F_ik`,

where `delta(H)=dH+Hd`. All three degree components of this equation are checked, as are the module and filtration conditions.

Even when the edge composites agree strictly, H need not be zero. Forgetting H after checking a face would discard exactly the data needed for the next coherence level.

## 3. The tetrahedral boundary and its filler

There are two face pastings comparing the triple edge composite with F_03. Their difference is

`Omega = F_23 H_012 + H_023 - H_123 F_01 - H_013`.

The verifier independently checks that Omega is closed. A filled tetrahedron supplies

`K_0 : C_0,0 -> C_3,2`

with

`delta(K)=dK-Kd=Omega`.

In components this means

`d_3 K_0 = Omega_0`,

`-K_0 d_0 = Omega_1`.

The signs and source/target types are explicit. This is a degree-two homotopy between the two degree-one face pastings, not another equality of edge-product matrices.

## 4. A filled example and a provably unfillable boundary

Write `F=F_03` and `L_i=left_t` at vertex i. Set all face witnesses to zero except H_023.

For the filled example choose

`H_023,0=L_3 F`,

`H_023,1=-F L_0`,

`K_0=F`.

These maps preserve the declared subspaces and intertwine both actions. The nonzero tetrahedral boundary is exactly delta(K).

For the obstructed example change only the sign of the second face component:

`H_023,0=L_3 F`,

`H_023,1=+F L_0`.

All four faces still pass: the relevant face differentials vanish because the left action squares to zero. But every admitted K must be module-linear, so

`L_3 K = K L_0`.

Consequently every possible delta(K) has component sum zero. The proposed boundary instead satisfies

`Omega_0+Omega_1=2 L_3 F != 0`.

A rational nonzero matrix entry certifies this obstruction. It rules out ANY filler in the declared module-linear class, not just one guessed matrix. The obstruction test is sufficient, not a complete classification of arbitrary boundaries.

Thus strictly commuting edge maps and four valid chosen faces do not guarantee a filled tetrahedron. One could choose different faces, such as all-zero faces; the obstruction concerns the specified witnesses, not the existence of some coherent choice for the underlying strict diagram.

## 5. Two stages of the higher-coherence data

The second stage uses the upper coordinate gain

`Q=diag(2,3,5,7,11)`.

Its complete structural presentation is transformed and independently reverified. The stage maps must transport:

1. all four source identifications;
2. all six comparison edges;
3. all four face witnesses, component by component;
4. the tetrahedral boundary;
5. the chosen filler, when present.

Both the filled and obstructed examples survive this re-expression.

A negative test doubles the nonzero face and filler only at the second stage. Each stage still independently has a valid filled tetrahedron. Nevertheless the declared stage maps do not transport the chosen witnesses, so the tower certificate is rejected.

This rejection concerns the explicit STRICT witness-transport contract. It does not rule out a more flexible comparison supplied with additional higher homotopies. Such prism/further-cell data are not admitted by this version.

## 6. What this does and does not settle for the four towers

The implemented hierarchy is now explicit:

- objects/presentations;
- comparison maps;
- witnessed triangular comparisons;
- tetrahedral compatibility of those witnesses;
- strict transport of that data across a finite list of stages.

The checker supports up to eight supplied stages. It does not infer an infinite tower theorem or certify arbitrary further coherence levels.

The next application gate is to identify actual objects, six comparisons and four face witnesses belonging to the productization/observer/comparison construction. Merely labelling the fixture vertices with those names would not discharge that gate. The same distinction applies to numerical source/observer squares: this fixture does not automatically identify their coordinates or certificates with these chain complexes.

## Verification

Generate and test:

`python research/nima/checkers/check_tetrahedral_coherence.py`

Independently verify the filled example:

`python research/nima/certificates/verify_tetrahedral_coherence.py research/nima/results/tetrahedral-coherence-filled.json research/voevodsky/certificates/verify_structural_gain_square.py`

Replace `filled` by `obstructed` to verify the certified obstruction. An OBSTRUCTED result means the obstruction certificate is valid, NOT that a coherent filler was found.

The trusted code consists of the tetrahedral verifier and the owning structural verifier. Both examples pass isolated execution with those two files and the supplied JSON alone. Neither producer nor solver is imported by the verifiers.

The tests reject eight corruptions, including a wrong filler, attempted filling of the obstructed boundary, mismatched stage witnesses, a bad face, an incorrect edge, an invalid obstruction entry, a physical-scope overclaim and unchanged action matrices after a gain.

Artifacts:

- `research/nima/results/tetrahedral-coherence-filled.json`
- `research/nima/results/tetrahedral-coherence-obstructed.json`
- `research/nima/results/tetrahedral-coherence-tests.json`
