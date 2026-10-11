# Restart iteration 2: marked Boolean states select a frame, but not an independent response

## Fresh source inspection

Read `agda/RetainedTetrahedralPackage.agda` directly. Its two relevant specializations must not be conflated:

- `LossyDiagonal` uses `Cells (Type ...)`: its four vertex values are Bool types. There is no field choosing an inhabitant of each Bool.
- `TypedFixture` uses `TypedValue = Sigma T:TUniverse, T`. It actually retains false,true,false,true, with dependent paths transporting the chosen inhabitants.

The full constructor retains edges, triangle witnesses and the tetrahedral filler; none is replaced by the following numerical classification.

## A genuine conditional frame selector

For a pointed two-element set with counting metric, order its basis as (marked element, other element). This selects an orthonormal frame under the Boolean permutation policy without choosing a second independent mark. In the declared (false,true) coordinates its orientation is o_i=(-1)^m_i.

A compatible Boolean edge with flip bit b_ij must obey

    m_j=m_i xor b_ij.

Thus o_i o_j=(-1)^b_ij=det(u_ij). On the later edge V, the relative frame selected by these actual marks is precisely the previous self-edge attachment. Since Ad_J(V)=det(V)V,

    (o_1 o_2) Ad_J(V)=V.

The corresponding mixer fixes V tensor U. The hidden readout again equals the ordinary readout. This is a positive conditional frame selection and a negative independent-signal result, not absence of all reference data.

## Complete flat Boolean edge classification

There are eight flat assignments among the 64 choices of six Boolean edge actions. Every one has b_ij=g_i xor g_j, and all lie in one orbit of the sixteen independent vertex frame flips.

An equivariant relative sign f must satisfy

    f(g.e)=(-1)^(g_1+g_2) f(e).

Its value on the all-identity assignment determines it everywhere. Therefore the only sign-valued possibilities are

    f(e)=+det(V) or f(e)=-det(V).

The stabilizer of the all-identity assignment is the simultaneous global flip; its relative character is +1, so both possibilities are consistent. There is no third history-sensitive relative sign made solely from these flat edge actions. The negative convention changes all adapted source outputs by the same sign, not their relative distinction.

Compatible marked assignments also form a single orbit. Their ordered-basis convention gives the positive choice. Flipping an edge while keeping incompatible endpoint marks fixed is not another instance of the typed source: it violates the dependent transport condition.

## Higher-witness boundary

This does not identify the ordinary and twisted full packages or discard their histories. In the Boolean type-path interpretation, univalence identifies paths with Boolean equivalences; these form a set. Higher equality witnesses between fixed such paths therefore do not offer an additional independently variable Boolean permutation action. This is the standard type-level truncation argument, not a newly checked Agda theorem about every retained syntax or arbitrary WG relation.

An operation consuming presentation history may still differ from edge transport. Such an operation must be supplied and typed; it cannot be inferred from an unrecorded Boolean inhabitant or a new arbitrary orientation sign.

## Next executable continuation

The current result concerns factorizable source banks. The exchange generally produces a nonfactorized bank. Retain the selected endpoint marks/orientations as attachment data and test covariance and conservation of the WHOLE carrier-plus-bank update, not just its bank mixer, through the permitted three advances. The carrier half-turn has its own endpoint-relative character and must be included. This can establish whether the conditional source frame actually supports a coherent evolving system, or expose another obstruction.

Gravitational normalization remains unresolved: counting-basis frames and the above finite classification do not supply a matter/geometry coupling or a physical energy scale.

## Verification

`python research/nima/checkers/check_pointed_boolean_frame_selection.py` passes exact exhaustive controls over eight flat edge assignments, sixteen marked assignments and sixteen local Boolean frame changes. Receipt: `results/pointed-boolean-frame-selection.json`, with source digests. No Agda source or historical receipt was modified; no fresh formal closure or physical-gravity derivation is claimed.
