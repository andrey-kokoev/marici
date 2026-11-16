# NNPE successful completions: payload coherence and native geometry comparison

Date: 2026-11-02. Continuation of `nnpe_complete_reconstruction_and_native_reader.md`.

## Result and exact scope

The source's existing shared-edge coefficient comparison supplies a positive test for the two candidate successful routings. It need not be phrased as an operation failure. Under that declared scalar reading, the two-triangle (`3+3`) routing is persistently compatible precisely when two extra comparisons hold. The alternative two-plus-four (`2+4`) routing preserves the entire five-coordinate shared-edge space. Both act reversibly on one common three-coordinate subspace.

The cyclic coefficient update for the original triangles is already present in the inspected source. Applying the same coefficient-rotation convention to the alternative circuit partition is the NEW trial in this audit. It is not an operation already synthesized from the original local triangle operators. The source's directed occurrence identities and their retained histories are never identified or discarded.

On the common subspace, the two updates generate a four-state orbit. Its affine metric and proper generator action match the existing proton geometry fixture exactly, with an explicit overall factor two when the inherited paired-occurrence budget is used. This is a source-fixture correspondence, not a physical proton produced by neutron decay. The orbit is a set of coefficient states, not automatically four simultaneous spatial positions.

A separate actual-neutron source check excludes a tempting shortcut: the native simultaneous rotation of the two disjoint neutron rims does not descend through any of the nine reversed-edge identifications that would form the shared-edge source. Thus the current calculation does not establish that the shared-edge carrier is the native neutron, or that ordinary regrouping changes one particle into another.

## Sources read, reused and not executed

Fresh GitHub reads:

- `research/nima/seam-family-incidence-and-covariance-match.md`: retaining the original joint family is distinct from changing which pairings are active.
- `research/strominger/shared-seam-observability.md`: the scalar reading convention, persistent comparison theorem and maximal synchronized subspace.
- `research/nima/checkers/check_two_triangle_half_phase.py`: the actual C/S matrices, local embeddings, common fixed line and paired-occurrence metric.
- `research/voevodsky/inputs/relative-proton.json`: complete affine metric, two generators and attachment-pole seed.
- `research/voevodsky/inputs/mode-neutron.json`: complete metric, simultaneous rotation and two seeds.

The six-occurrence registry and four complete routings are retained from the preceding conversation artifact. The two geometry input JSON objects are transcribed in full from the fetched source contents and included in the bundle. The source formulas are independently reconstructed in the Python checker. No upstream Agda checking, full geometry-producer replay or repository modification is claimed.

## 1. A source comparison, not a new failure test

Keep the six distinct occurrences in the order

```
(AB, BC, CA, BA, AD, DB).
```

The inspected shared-seam model uses five independent scalar readings

```
x=(a,b,c,d,e),
q=(a,b,c,-a,d,e).
```

In this model, BA and AB have opposite coefficient readings on a common oriented support. This is not the equality `BA=inverse(AB)` between source paths. The source explicitly distinguishes occurrence identities from coefficient conventions.

The embedding `q=Jx` induces the paired-occurrence metric

```
M=J^T J=diag(2,1,1,1,1).
```

For a routing permutation sigma, the tested coefficient update is the pullback

```
(T_sigma q)_e=q_(sigma(e)).
```

On the original directed triangle this is exactly the source convention `C(a,b,c)=(b,c,a)`.

Let `h q=q_AB+q_BA`. Persistent gluing for a fixed routing means

```
h T_sigma^k Jx=0 for every k>=0.
```

Each tested routing is periodic, so a full period gives all necessary and sufficient equations. This is an exact finite argument, not extrapolation from a numerical history.

## 2. Complete compatibility domains

The preceding full-routing experiment gives four tables:

| Changed junction pairings | Circuit partition | Maximal compatible dimension in the five-coordinate reading |
|---|---|---:|
| Neither | `AB BC CA`; `BA AD DB` | 3 |
| B only | one six-occurrence circuit | 1 |
| A only | one six-occurrence circuit | 1 |
| Both | `AB BA`; `AD DB BC CA` | 5 |

For the original two triangles, the additional equations are exactly

```
b+d=0,
c+e=0.
```

These conditions are already present in the source shared-seam theorem. The new calculation compares their domain with the other complete routings. It does not claim to have newly discovered the source's synchronized subspace.

Write

```
K(a,b,c)=(a,b,c,-b,-c).
```

Then the coherent six-occurrence values are `(a,b,c,-a,-b,-c)`. Both completed routings act on this same subspace:

```
C(a,b,c)=(b,c,a)              # 3+3 completion
R(a,b,c)=(-a,c,-b)            # 2+4 trial completion
```

They satisfy

```
C^3=I, R^4=I,
C^T C=R^T R=I,
K^T M K=2I.
```

Thus every finite supplied sequence of these WHOLE compatible updates retains the common subspace and its inherited budget. Both can be valid on the same nonzero data. For example `(a,b,c)=(2,3,5)` goes to `(3,5,2)` under C or `(-2,5,-3)` under R. Both have paired budget 76. Neither is called a faulty output.

This establishes successful alternatives under the trial operation set, not autonomous choice between them.

## 3. Eligibility is not a rare event supplied by this model

The full five-coordinate `2+4` update is

```
R5(a,b,c,d,e)=(-a,c,d,e,b).
```

The two prospective triangle-completion comparison values transform as

```
(b+d,c+e) -> (c+e,b+d).
```

They are swapped, so their joint zero condition and squared norm are invariant. Consequently, repeating this fixed `2+4` law cannot turn an ineligible input into an eligible one, and cannot make an eligible one ineligible. An alternative can already be available while the ordinary continuation remains available. A context-changing operation or a realization-selection law is a distinct question.

The two additional equations do not give two failure probabilities, an independence assumption, a codimension-based event probability, or a microscopic clock. No probability distribution on payloads was supplied.

## 4. Intermediate junction updates require their own check

A full routing is not the same as a temporally staged change of its two local pairings. The intermediate six-circuit updates are valid permutations, but their maximal repeatedly compatible shared-edge subspaces have dimension one.

That does NOT mean every transient use of an intermediate routing is forbidden. The checker separately imposes coherence after every executed intermediate step, then requires the exit to lie in the common three-coordinate carrier.

Starting within that common carrier, the compatible input dimensions for zero through six intermediate steps are

```
3, 2, 1, 0, 0, 0, 0
```

for either choice of the first changed junction. For exactly one intermediate step the condition is `a+b=0`. Two steps impose another independent equation; three steps leave only zero in this restricted trial.

This is a timing/compatibility statement for the specified coefficient-update convention. It does not establish a physical time, prohibit a different intermediate carrier, or force simultaneous switching. It prevents treating a graph-edit sequence as an automatically compatible payload execution.

## 5. A four-state orbit, compared with the actual proton fixture

The source's common triangle mode is proportional to

```
v0=(1,1,1).
```

The group generated by C and R has exactly 24 matrices. Its determinant-positive part has 12 matrices and is generated by C and R^2. Both have the four-state orbit

```
v0=( 1, 1, 1)
v1=( 1,-1,-1)
v2=(-1, 1,-1)
v3=(-1,-1, 1).
```

In the standard coordinate dot product the Gram matrix is `4I4-J4`: each squared norm is 3 and each distinct inner product is -1. Every pair distance squared is 8. In the inherited paired-occurrence metric `2I3`, these norms and distances are doubled. The overall amplitude of the common mode is not fixed by invariance; v0 above chooses its unit coefficient representative, not a physical energy normalization.

The freshly retrieved `relative-proton.json` contains

```
G_p = [[8,4,4],[4,8,4],[4,4,8]]

A_1 = [[-1,-1,-1],[1,0,0],[0,0,1]],  t_1=(1,0,0)
A_2 = [[0,0,1],[0,1,0],[-1,-1,-1]],  t_2=(0,0,1)

seed=(0,0,0), role=attachment_pole.
```

Define the affine comparison

```
F(x)=v0+B x,
B=[[0,-2,-2],[-2,0,-2],[-2,-2,0]].
```

The exact equations are

```
B^T B=G_p,
B^T (2I) B=2 G_p,
F(A_1 x+t_1)=R^2 C F(x),
F(A_2 x+t_2)=C R^2 F(x).
```

The two transformed native generators are respectively

```
[[0,1,0],[0,0,-1],[-1,0,0]],
[[0,-1,0],[0,0,-1],[1,0,0]].
```

The checker generates both complete finite groups and verifies equality of the transformed native group with the 12-element proper subgroup above. The seed maps to v0. Hence this is an explicit metric-and-action comparison, not an inference from both objects having four vertices.

R itself has determinant -1. It must not be presented as an already admitted proper spatial generator. The proper comparison uses R^2 and C. Further, coefficient-state orbits are not automatically simultaneous spatial points: this affine match does not produce an independently propagating proton, identify a mass, construct a spinor or establish decay products.

## 6. The proposed R action has not been compiled from the inspected source menu

The source's separately embedded triangle operations C1,C2,S1,S2 fix

```
w=(1,1,1,-1,-1).
```

Its reference exchange sends w to -w. Every word in these named operations and their inverses therefore preserves `span(w)`. By contrast,

```
R5 w=(-1,1,-1,-1,1),
```

which is not on that line. R5^2 also moves it off the line.

This gives an exact all-word obstruction to constructing the proposed rerouted coefficient action from that SPECIFIC operation menu on the same five-coordinate carrier. It is not a statement that no native rule, larger retained carrier, geometric realization or other local operation could implement it. In particular, the proper action has an exact counterpart in the separately supplied proton geometry fixture; those two operational interfaces must not be silently identified.

The native family/context audit supplies a parallel warning: reindexing the two original triangle rows retains their joint relation. It does not change their active pairing into the complementary two-cycle/four-cycle relation. A re-pairing operation still needs an actual rule or binding.

## 7. Actual neutron-source binding control

The current `mode-neutron.json` has metric `diag(3,1,1)`, the single rotation

```
[[-1/2,0,-1/2],[0,1,0],[3/2,0,-1/2]],
```

and seeds `(0,7/20,1)` and `(0,-7/20,-1)`. Exact generation gives six distinct points in two disjoint three-cycles. This is not the four-vertex shared-edge source used above.

A natural attempted bridge is to identify one oppositely directed edge from each rim, retaining all six arrow occurrences. Nine such marked choices exist. Each makes four vertex classes and gives the shared-edge incidence pattern. None respects the unchanged simultaneous native rotation.

For example, with rim indices U0,U1,U2 and L0,L1,L2, identify

```
U0~L1, U1~L0.
```

The original rotation sends the first identified pair to `U1,L2`, which are not identified. Thus the induced action is not well defined on the four quotient classes. Closing BOTH original identifications under the rotation forces all six vertices into one class. The same occurs for all nine reversed-edge choices.

All 203 partitions of six points were also checked. Exactly eight are invariant under the native simultaneous rotation. There ARE two invariant four-class partitions, but each collapses an entire rim to one class and keeps the other rim's three vertices separate. Neither is the required shared-edge-two-triangle identification. This scope distinction prevents an unwarranted universal 'no four-vertex quotient' claim.

Same-orientation edge identifications are a separate control: their rotation closure makes three classes, not four.

These results exclude only a fixed-action quotient shortcut. They do not exclude a realization process that jointly reconstructs the incidence and its action while retaining ancestry. They also do not prove that the user's four-leg NNPE junctions must be identified with the geometric rim vertices. That binding is precisely one of the unresolved objects.

## 8. Consequence for the requested mechanism

The successful-completion framing now has an explicit payload-level implementation test: the alternative triangle completion requires two additional compatibility relations, and both completed updates preserve a common carrier when those relations hold. No damaged arrow is required.

The four-state orbit has an exact correspondence with the native proton fixture, but it is not an independently derived neutron-to-proton operation. The source-to-source bridge must account for the different initial incidence/action data and for why the rerouted operation is actually admitted. The comparison does not establish independent electron and neutral-partner outputs, physical conservation readers, autonomous selection, escape or lifetime.

The next precise construction is a common retained parent whose different successful realizations produce the native neutron source and the candidate charged-output source, WITH their respective incidence and action witnesses. It cannot be replaced by a colour change on one fixed graph, a quotient that lacks a descended action, or a supplied probability for which branch wins.

## Reproduction

```
python completion_coherence.py
python neutron_source_binding.py
```

Python 3.10+ and SymPy. All decisions use exact integers/rationals. The first script passes 69 named checks, including the four persistent-coherence kernels, transient-stage controls, complete generated action, metric factors, native-generator intertwiners and source-menu invariant. The second checks the actual neutron fixture, all 203 set partitions and all nine reversed-edge bindings. No thresholded eigensolver, sampled approximation, measured lifetime or fitted physical scale is used.

Artifacts: `results.json`, `neutron_source_binding_results.json`, both transcribed source inputs, the two checkers and `run.log`. The checker hashes are recorded in their corresponding results.

Source URLs:

- https://github.com/andrey-kokoev/marici/blob/main/research/strominger/shared-seam-observability.md
- https://github.com/andrey-kokoev/marici/blob/main/research/nima/checkers/check_two_triangle_half_phase.py
- https://github.com/andrey-kokoev/marici/blob/main/research/nima/seam-family-incidence-and-covariance-match.md
- https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/inputs/relative-proton.json
- https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/inputs/mode-neutron.json
