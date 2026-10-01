# Spatial placement at one complete seed-phase return

## Result

The existing spatial realization was tested on actual labelled vertex/triangle positions, not on the signed amplitude contrast of the previous test.

- The global S4 word (ABC)^3 restores every tested spatial frame exactly, with zero translation.
- The native three-step continuation also restores the seed coefficient vector, but its 26 retained endpoint paths are NOT that one global permutation word.
- Mapping those paths into the existing S4 spatial realization requires their actual comparison witnesses. The bare six TwoPacket records do not contain them.
- Two already classified equivariant witness policies give different spatial returns for the same closed labelled path. The full area realization can exchange the two bodies even though the endpoint label returns. This is a rotation/body exchange, not translational propagation.

Thus the question has been narrowed to a concrete missing attachment: the supplied per-edge comparison witness and its compatibility with the phase update. A new clock or a new spatial carrier was not constructed.

## Existing sources inspected

1. `agda/WholePackageResolution.agda`: `compare-rule` takes complete source/target packages, an actual equivalence e, and proof that e transports the marked value. It does not construct e from two labels.
2. `retained-pointed-comparison-groupoid.md`: the finite S4 realization has six possible pointed witnesses per ordered endpoint pair and retains comparison parents.
3. `equivariant-edge-lifts-and-spectator-policy.md`: exactly two fully relabelling-equivariant edge policies satisfy the stated pointed-permutation requirements.
4. `seed-edge-action-extension-obstruction.md`: a global triangle successor is not the same operation as holonomy around a pointed triangle traversal.
5. `twenty-four-triangle-shared-seed.md`: actual placements use the area representation rho(g)=det(R_g)R_g and X_g=rho(g)X_0, giving the two tetrahedral bodies T and -T.
6. `stagewise-positive-atlas-witness.md`: the existing coefficient-network stages retain an immutable spatial atlas; phase coefficients and geometric chart data are distinct fields. Arbitrary phase processing is not itself a position update.

These are specific audited realizations. This is not a claim that every possible native spatial construction must factor through this finite S4 representation. No fresh Agda compilation was performed; the existing finite source-constructor audit and exact spatial checkers were rerun.

## First test: global permutation-cycle placement

For the already defined global operation g=(ABC), the spatial action is known. Apply rho(g) three times to each of the 24 existing labelled triangle placements. Every vertex and face-centre position returns exactly:

    rho(g)^3 X_p = X_p.

Full word history remains (g,g,g), not the empty word, and the attached phase clock does not reset. Nevertheless this spatial decoder depends on the composite permutation, so it reports the same placement.

All existing body placements have the same centre. Their matrices are orthogonal and, in the area representation, proper. Repeated group operations can rotate or exchange the bodies but cannot produce a translational drift of their centre. A translated copy is rejected by the existing placement inventory.

## Second test: the native continuation is a different input

From the current seed, three prefix extensions give:

    same six coefficient summary,
    clock advance pi under the specified rotor attachment,
    26 retained paths: 10 endpoint-closed and 16 endpoint-open.

The first primitive belongs to preparation; the three appended primitives are the timed continuation. No branch is selected or discarded.

An endpoint path i->j supplies neither its S4 action on the other two labels nor its complete body-frame transport. For each appended arrow there are six pointed witnesses g with g(i)=j. For each three-step path:

- 216 witness histories are compatible with the endpoints;
- they give six possible composite permutations;
- each composite occurs 36 times;
- the area realization gives six labelled body placements and two possible final anchor positions.

The audit exhausts 26*216=5616 assignments. These are counts of possible supplied witness data, NOT probabilities or new emission events. Once actual witnesses are supplied, composition and the spatial placement are definite; the checker rejects attempts to realize a path without them.

## A closed path distinguishes the policies

Prepare AB, so the starting continuation anchor is B=(1,-1,-1). Append

    BC, CA, AB.

The based route is B->C->A->B. Both previously classified policies respect these endpoints and all relabellings.

### Endpoints swapped, other labels fixed

Use (ij) on each edge i->j. The composite is

    (AB)(CA)(BC)=(AC),

which fixes the label B. In the STANDARD tetrahedral action, B stays at B. But the existing AREA realization uses

    rho(AC)=[[0,0,1],[0,-1,0],[1,0,0]],
    rho(AC) B=-B=(-1,1,1).

The closed label path exchanges the body branch T -> -T and moves the area anchor by (-2,2,2). Ignoring the body sign would incorrectly report that this spatial anchor returned.

This operation is a half-turn about an axis through the common origin. The body centre remains fixed. Repeating the same loop returns the placement because rho(AC)^2=I. It is not a translation accumulating on successive cycles.

### Endpoints and the other pair both swapped

Use (ij)(kl), where k,l are the other labels. The same triangle composite is identity. The complete labelled placement and anchor B return after this loop.

### What the difference proves

The same seed coefficients, phase-return time and endpoint word admit different full spatial placements unless the actual comparison witness is retained. The alternatives are not new fitted transport models: they are the two previously classified equivariant policies, used here as a concrete distinction test. Neither is silently selected as the physical operation.

The first policy's primitive actions generate S4; the second's generate the Klein four group. Requiring the primitive edge operations themselves to generate all of S4 would distinguish them within this class. That requirement is stronger than saying that S4 acts by relabelling, and has not been imported as an unstated selection rule.

## Keep the operation types separate

A complete pointed B->B traversal must fix B as a label. The global successor (ABC) does not. Therefore the global cyclic vertex action cannot simply be assigned as the composite of this pointed loop.

Likewise, the current phase clock timestamps the native coefficient update. The candidate per-edge spatial witnesses have not yet been proved to implement that phase evolution jointly. Assigning a witness and checking its geometry is not, by itself, the missing joint dynamical theorem.

Retained parent trees are preserved by the existing pointed comparison model. Two bracketings have equal composite placement and equal leaf sequence but different parent trees. Neither frame return nor position return erases those records.

## Verdict for the propagation question

For the supplied global S4 placement map, a complete global phase cycle has no net translation. For the native endpoint histories, phase return alone does not determine spatial return: actual comparison witnesses are needed. Even a displaced area anchor can be a bounded body-exchange rotation rather than a translating excitation.

The previous fixed-tetrahedron displacement bound was correctly scoped to its projection. The full existing two-body area realization has a larger placement inventory and can change the body sign; it still supplies no accumulated translational drift by itself.

This is not a proof that a richer retained spatial construction cannot propagate. It identifies the precise attachment required before the photon seed can be evaluated through one.

## Verification

    uv run --with sympy python research/nima/checkers/check_photon_spatial_phase_return.py

The command reruns the phase-clock/native-continuation audit, the pointed-witness and equivariant-policy audits, and the existing two-body geometry checker. It then checks actual spatial returns, all witness assignments, body-sign controls, retained-parent composition, and rejection of missing or incompatible witnesses. Source hashes and all 26 path results are recorded.

Report: `results/photon-spatial-phase-return.json`.

## Next concrete source attachment

Extract or supply the actual equivalence carried by each primitive continuation, including its action on uninvolved labels. Check that these witnesses reproduce the retained phase update on the intended fibre. If the intended spatial realization instead reads more history than the composite S4 action, identify that existing reader explicitly and preserve its extra input; do not manufacture a drift vector from winding alone.
