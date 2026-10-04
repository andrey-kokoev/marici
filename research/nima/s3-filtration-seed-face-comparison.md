# Comparing the specified S3 filtration with the actual seed faces

## Question and claim boundary

Does the filtration

\[
0\longrightarrow X\xrightarrow fY\xrightarrow{\iota_Y}X\oplus Y
\]

identify its four cofiber triangles with the repository's oriented seed faces, including maps, signs, and suspension?

**Disposition:** the signed face incidence agrees already in integral K0, and reduction modulo two gives the opposite-edge pairs when [X],[Y] are independent modulo two. The actual seed supplies directed packet occurrences and coefficient operators, not an identified stable-category diagram. The existing coordinate-support stable realization has split quotient triangles; the proposed filtration need not. A faithful identification preserving the cofiber data therefore fails in general. This is not a proof that no nonfaithful realization functor can exist.

SCC obligation: attachment transport and route compatibility between the specified stable filtration, seed occurrence complex, and coordinate-support realization. These are three different typed objects. No higher-coherence promotion or physical readout is inferred from matching incidence.

Operator direction: compare the actual four cofiber triangles with faces 012,013,023,123, rather than continue the proposed source hierarchy from numerical agreement. This packet records the comparison, not an assumption that the hierarchy closes.

## Issue and discriminating test

- **Problem:** determine whether the proposed S3-to-finite reduction connects actual seed operations or only their labels/classes.
- **Conjecture:** the selected filtration has a comparison to the existing seed that preserves its oriented faces, connecting morphisms, and suspension data.
- **Rivals:** only signed incidence agrees; mod-2 reduction loses the distinctions; the coordinate-support model is a split realization rather than a faithful image of a general arrow.
- **Risky consequence:** the comparison must preserve zero/nonzero connecting maps if faithful, not only the four additive cofiber relations.
- **Falsifier:** use independent simples X,Y in Perf(Q) x Perf(Q), with f=0. Compute the four connecting maps and compare their ranks with the split coordinate-support model. Recover the actual seed declarations from its checker rather than replacing them by an invented stable seed.
- **Surviving scope:** integral face relations and the mod-2 pairing hold. The blanket faithful stable comparison fails in the counterexample. A separately defined seed-to-stable map is absent; no weaker substitute is promoted to that map.

## 1. What the repository actually supplies

### Directed occurrence seed

[The witness-helix packet](photon-tetrahedron-octahedron-witness-helix.md), sections 1–4, defines

\[
T_1=(01,12,20)=\partial[012],\qquad
T_2=(10,03,31)=-\partial[013],
\]

and completes them with

\[
T_3=(02,23,30)=\partial[023],\qquad
T_4=(13,32,21)=-\partial[123].
\]

The executable source `checkers/check_two_triangle_half_phase.py` declares the first two triples as TwoPacket occurrences (AB,BC,CA) and (BA,AD,DB). `checkers/check_triangle_half_phase.py` constructs an invertible order-three cyclic operator on a triangle's coefficient space. Its half-phase lift obeys S cubed = Q-P and S to the sixth = I in that coefficient realization.

These are not declared connecting morphisms of stable objects. A cyclic permutation of coefficient slots and a map C -> Sigma X have different types. In particular, the existence of an invertible coefficient cycle neither forces a nonzero connecting map nor identifies categorical suspension with that cycle.

The existing witness-helix packet already limits its cofiber/incidence comparison to forgetting category, arrow directions, and suspension. Its general four-filtration cofiber display is a template, not a supplied functor attaching stable objects to the actual TwoPacket registry.

### Coordinate-support stable model

[Tate-torus cofibers](tate-torus-cofiber-and-octahedral-realization.md) uses

\[
V_S=\mathbf C[\mathbf Z^S],\qquad V_A\hookrightarrow V_B\quad(A\subseteq B).
\]

For A subset B subset C, the quotient short exact sequence has a section in the underlying vector-space model: include the delta basis indexed by Z^C minus Z^B into the quotient by Z^A. Hence it is split and its connecting morphism in the derived vector-space category is zero.

This statement concerns the specified underlying vector-space realization. It does not assert a splitting compatible with every hypothetical additional topology, module structure, or enriched source that has not been supplied.

The legacy checker `check_tate_torus_cofiber_octahedra.py` tests dimensions and subset rotations on 256 nested triples. It does not construct connecting maps, suspension comparisons, or enumerate the 625 weak four-stage chains of the four-coordinate Boolean lattice. Its variable named `octahedra` counts the same triple loop. The packet's abstract quotient construction can justify canonical octahedra, but this checker is not a separate morphism-level verification of that claim. No legacy source was modified in this audit.

## 2. Actual cofibers of the proposed filtration

Set C = cofib(f), let q:Y -> C and delta:C -> Sigma X be the cofiber maps, and write C_ji = cofib(A_i -> A_j). Then

| Interval label | Object |
|---|---|
| 01 | X |
| 02 | Y |
| 03 | X direct-sum Y |
| 12 | C |
| 13 | X direct-sum C |
| 23 | X |

In particular, these are six indexed occurrences, not necessarily six distinct isomorphism classes. The four triangles, in a compatible choice of standard biproduct/cofiber conventions, are

\[
X\xrightarrow fY\xrightarrow qC\xrightarrow\delta\Sigma X,
\]

\[
X\xrightarrow{(0,f)}X\oplus Y
\xrightarrow{1_X\oplus q}X\oplus C
\xrightarrow{(0,\delta)}\Sigma X,
\]

\[
Y\xrightarrow{\iota_Y}X\oplus Y
\xrightarrow{\pi_X}X\xrightarrow0\Sigma Y,
\]

\[
C\xrightarrow{\iota_C}X\oplus C
\xrightarrow{\pi_X}X\xrightarrow0\Sigma C.
\]

Thus faces 023 and 123 are always split. Faces 012 and 013 are split exactly when delta vanishes. Possible sign changes under equivalent octahedral conventions do not change these zero/nonzero distinctions.

The negative signs assigned to faces 013 and 123 in the oriented simplicial boundary negate incidence chains; they do not by themselves construct dual or reversed distinguished triangles.

## 3. Integral orientation matches; mod 2 supplies a coarser quotient

Write x=[X], y=[Y] in integral K0. The six edge classes in the order 01,02,03,12,13,23 are

\[
(x,\ y,\ x+y,\ y-x,\ y,\ x).
\]

Every face relation is already zero integrally:

\[
x+(y-x)-y=0,\qquad x+y-(x+y)=0,
\]

\[
y+x-(x+y)=0,\qquad (y-x)+x-y=0.
\]

Applying the seed's signs +,-,+,- also makes the full oriented tetrahedral boundary cancel. No mod-2 reduction is necessary for this orientation check.

Modulo two, assuming x,y independent, the fibers of the edge-class map are exactly

\[
01\mid23,\qquad02\mid13,\qquad03\mid12.
\]

The first pair is isomorphic already. The second shares its integral class without necessarily being isomorphic. For the third pair,

\[
[C_{30}]-[C_{21}]=2x,
\]

which explains precisely why reduction modulo two identifies its classes. Suspension likewise changes the integral sign but becomes invisible modulo two. None of these class equalities is an isomorphism or a morphism comparison.

## 4. Exact counterexample with independent classes

Take the stable category Perf(Q) x Perf(Q). Let X and Y be its independent degree-zero simples and choose f=0. With homological suspension raising degree by one,

\[
C=Y\oplus\Sigma X,\qquad C_{31}=X\oplus Y\oplus\Sigma X.
\]

The connecting map C -> Sigma X is the projection onto Sigma X, so the four connecting-map ranks are

\[
(1,1,0,0).
\]

The second opposite pair is Y versus X direct-sum Y direct-sum Sigma X, with different homology. The third pair is X direct-sum Y versus Y direct-sum Sigma X, also with different homology. Both pairs agree modulo two in K0 as predicted. This is a lawful counterexample to identification from the class pattern; it is not a replacement definition of the universal source.

If an A4 action were required to act transitively on the four faces by equivalences of distinguished triangles, it would preserve splitness. This example cannot admit that lift. The finite tetrahedral incidence still has A4 symmetry after forgetting those data. No such stable A4 action is actually specified by the current seed, so the result is a conditional obstruction, not a claim that an existing supplied action failed.

## 5. Comparison with the existing coordinate-support realization

Use its declared lattice window {-1,0,1} on a chain of coordinate subsets of sizes 0,1,2,3. The space dimensions are

\[
(1,3,9,27).
\]

The six quotient dimensions are

\[
(2,8,26,6,24,18).
\]

The delta bases explicitly split each of the four face sequences. All four connecting maps therefore vanish, in contrast to (1,1,0,0) in the counterexample.

Moreover, in the ungraded finite-window derived vector-space target, K0 is Z and each of these quotient classes is even: their scalar mod-2 reductions are all zero. That target does not retain the two independent source generators. This is a statement about this finite-window scalar realization, not the K0 of an unspecified enriched or infinite-dimensional category.

A nonfaithful realization may legitimately forget connecting maps or K0 generators. It cannot then be used to claim their faithful recovery from its incidence image.

## Result table and stopping condition

| Comparison | Result |
|---|---|
| Actual two seed cycles versus faces 012 and 013 | Same directed occurrences and opposite shared-edge signs |
| Four signed face relations | Pass in integral K0 |
| Opposite-edge class fibers | Pass modulo two, conditional on independent x,y |
| Opposite paired cofibers are isomorphic | False in general; explicit homology counterexample |
| Proposed filtration faithfully identifies with split support model | False in general; connecting-map obstruction |
| Seed coefficient cycle identifies categorical suspension | No map supplied; not established |
| Higher witness recursion comparison | Not established by the class reduction |

The first absent typed object is a comparison specifying stable objects and morphisms for the actual seed occurrences, together with suspension compatibility and the role of its coefficient cycle. Its acceptance test must evaluate the four displayed triangles, retain their connecting maps and signed shared-edge data, and state whether the comparison is faithful or which information it forgets. A formal rotation of a distinguished triangle lands in suspended objects; it cannot be silently substituted for a closed unsuspended packet cycle. This branch stops at that missing comparison rather than generating another label-only cube test.

The [augmentation/dephasing theorem](augmentation-fourier-dephasing-fractions.md) remains valid on its declared finite inputs. This comparison neither changes its 11/25 and 14/25 squared norms nor supplies its upstream stable-witness selection map.

## Reproduction

```text
python research/nima/checkers/check_s3_filtration_seed_faces.py
python research/aspect/scc/scc.py validate research/nima/scc-models/s3-filtration-seed-faces.json
python research/aspect/scc/scc.py check s3-filtration-seed-faces
```

Result: `results/s3-filtration-seed-faces.json`. The exact checker reads the actual seed declarations by AST, checks their coefficient-cycle order, verifies signed integral and mod-2 classes, constructs the graded counterexample, and verifies coordinate-support complement sections. The checker passed with exit code 0, including graded homology exactness of the four counterexample triangles and their connecting ranks. Execution receipt: `structured_command_execution:e_25120_1790947843306935200_136`. SCC manifest validation and its registered checker run passed; its adapter reports exit-code evidence only. No Rzk/Agda/Lean formal closure or external-reference verification is claimed.

Graph provenance: event `ev-000000015680-77215075-7d03-4c2e-b718-79d3cae36309`, proposal `ep_05ffba28-3385-401f-a500-13f19718b911`, records the claim, bounded test and report to marici.Voevodsky. Admission does not certify truth. This packet, its checker and SCC manifest are uncommitted; results are locally generated. The immediate research sequence's admitted-but-uncommitted interval is [15678,15680]. No commit, push, deployment, or alteration of the legacy cofiber/seed sources occurred.
