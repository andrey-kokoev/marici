# Top-down Hamiltonian candidate from the twelve-arrow carrier

## What changed

The previous Hamiltonian WG test started with the prior bottom-up lift D12=E D4 P. This new construction does NOT use D4 to create its source generator.

It instead starts from the existing unique simultaneous endpoint section of the six-edge seed:

    A -> D -> B -> C -> A.

Use the already documented induced S4 action on the twelve directed carrier arrows. The permutation sends arrow ab to c(a)c(b). Its twelve-coordinate matrix C12 determines the DECLARED angular generator

    D12=C12-C12^T.

The constructor imports no bottom rotor. It takes the source permutation, arrow labels, historical four-port chart and an explicit normalization. The checker constructs the source and executes descent BEFORE loading the prior bottom model for comparison.

54 exact checks pass. The prior45-check rotor bridge is freshly rerun as a comparison/dependency, not used to construct D12.

**Result:** an independently constructed mathematical top generator descends to the prior D4, with actual nonzero hidden dynamics and energy. This removes the bottom-up circularity for this candidate. It does not make the declared source rules physical laws or identify the carrier with the native137-record T9 state.

## Source rules and their boundaries

The source inputs are:

1. the existing seed and its cycle-cover selection objective;
2. the already documented action of vertex permutations on all twelve directed carrier arrows;
3. the fixed stabilizer-probe coefficient metric G12=10I+J;
4. the historical four-port labeling A=0,C=1,D=2,B=3;
5. the declared skew-part rule D=C-C^T;
6. the form/energy rule Omega=alpha G D, K=D^T Omega, with alpha>0.

These are explicit mathematical choices. The cycle-cover objective is not a proof that nature selects this cycle. The skew rule supplies an angular interpolation, not a logarithm reproducing the entire source permutation. Metric and alpha are not physical energy calibration.

At alpha=1/2 the target form and quadratic energy equal the prior rotor convention. At alpha=1 the same source and target dynamics have twice the energy Hessian. Thus agreement of D does NOT select an absolute Hamiltonian normalization.

All twelve arrows, including the original seed's AB and BA, remain present. The induced action does not preserve the six-edge seed as a subset. It is an action on the existing completed twelve-arrow carrier, not a proved implementation of the native six-arrow successor.

## Full top Hamiltonian state

The constructed real model satisfies

    x'=D12 x,
    Omega12=alpha G12 D12,
    K12=alpha D12^T G12 D12,
    H12(x)=x^T K12 x/2.

D12 is metric-skew, Omega12 is antisymmetric, K12 is positive semidefinite, D12^T Omega12=K12, and the flow conserves both the coefficient metric and H12. The form is presymplectic, not an asserted nondegenerate physical phase-space form.

D12 and K12 have rank6. This source differs from the prior lift, whose hidden sector was fixed.

## Direct witnessed descent

Order the four cycle-cover arrows by their source-port labels:

    AD, CA, DB, BC.

Retain the other eight arrows. E embeds these first four coordinates, and the actual fixed-Gram projection is

    (Px)_i=x_i+sum_(j>=4) x_j/14.

The verified WG returns the prior D4 and, at alpha=1/2, its Omega4 and K4. Exact generator intertwining gives

    P exp(t D12)=exp(t D4) P

for every real t in the supplied common angular parameter.

With N=I-EP, reconstruction is x=E(Px)+Nx. The hidden generator and hidden energy Hessian have rank4, and the full Hamiltonian splits as

    H12(x)=H4(Px)+H_hidden(Nx).

Neither the hidden state nor its energy is discarded. Equality of visible states still permits different total energies.

## Why the naive iteration fails

The new source contains two hidden frequency2 rotor planes. Dropping the last arrow coordinate in the ordinary chart cuts one of them:

    P12,11 D12 N12,11 != 0.

The WG therefore refuses the first naive12->11 step. This is successful verification of an obstruction, not a failed test suite.

It matters that the earlier eight-step example passed only for a DIFFERENT top generator with stationary hidden modes. Its success cannot be imported to the new source just because the direct endpoints agree.

## A six-step schedule that actually works

The checker constructs an explicit rational, invertible reducing-mode frame B. Its first four columns are still E. The remaining columns comprise:

- two hidden invariant rotor pairs (four coordinates);
- four hidden stationary coordinates.

The complete frame is stored in the results JSON. Its inverse retains all original arrow coefficients; this is a declared coordinate change, not a physical preparation/reset or free optical control.

After that chart change, six WG reductions work:

    12 -> 11 -> 10 -> 9 -> 8 -> 6 -> 4.

The first four steps remove stationary directions into retained records; the last two remove whole rotor pairs. The composite projection, D4, Omega4 and K4 exactly equal direct descent.

This is SIX REDUCTION applications AFTER a supplied reversible frame change. It is not six arbitrary coordinate drops, not six native T9 operations, and not a proof of six physical ticks. The choice and implementation of the frame are not erased from the resource/provenance boundary.

## Source permutation versus angular flow

C12 has three alternating modes and determinant-1. The rotor fixes those alternating modes, whereas the source permutation changes their signs. Exactly, with A=-D12^2/4 and the rank3 alternating projector M,

    exp(pi D12/4)=I-A+D12/2,
    exp(pi D12/4)-C12=2M.

Thus the new angular Hamiltonian is not a realization of the entire original discrete tick. Its omitted alternating information remains in the source state, but executing its sign change requires another explicitly supplied mechanism. The prior active-sector limitation survives the top-down construction.

## Postnikov and native-interface gates remain

This finite reducing-space model realizes the dynamical factorization clue found in the Postnikov search. It does not supply an actual source space, homotopy groups/actions, k-invariants or an identification of its coefficient dimensions with Postnikov stages.

Likewise it does not supply the operation-preserving map from this twelve-arrow Hamiltonian carrier to the original137-record T9 source and authorized rung4 readout. No such map is inferred from shared labels, dimensions, metric entries or equality with the prior D4.

The next native bridge must specify that map and test dynamics, form, energy and observation compatibility on the complete state. The physical bridge additionally needs selection of the cycle/skew/normalization rules, clock/action units, apparatus and retained-environment handling.

## Native interface follow-up

`native-t9-hamiltonian-closure-gate.md` tests this candidate on the actual137-record T9 input.30 checks confirm an obstruction: the counted eleven-arrow set omits AB and is not invariant under the source cycle. An explicit23-slot retained completion supports a conservative coefficient-field step, but the original native packet alone is not dynamically sufficient. Matching its137 records and even a2I missing corner does not choose that completion. This is not an autonomous native Hamiltonian or a physical/Postnikov identification.

## Verification

    uv run research/strominger/checkers/check_source_arrow_hamiltonian_descent.py

54 exact checks pass: fresh seed enumeration, independent top construction, exact direct and six-step witnesses, all12 reconstruction columns, continuous-series coefficients, nonstationary hidden sectors, normalization freedom, failed naive drop and the alternating/full-tick boundary. The prior45-check bridge also reruns; counts are not independent evidence to sum.

Artifacts:

- `research/strominger/checkers/source_arrow_hamiltonian.py`
- `research/strominger/checkers/check_source_arrow_hamiltonian_descent.py`
- `research/strominger/results/source-arrow-hamiltonian-descent.json`

Prior source pointers:

- `research/nima/checkers/check_seed_endpoint_sections.py`
- `research/nima/carrier-probe-adapter-and-state-reference.md`
- `research/nima/rotor-rung4-action-metric-bridge.md`
- `research/strominger/hamiltonian-descent-wg-and-postnikov-clues.md`

Graph report: `ev-000000015898-b05453a8-561e-4060-b07e-7eead1747646` (proposal `ep_ecbcce8c-c708-42f2-9578-839ddd78258f`). Admission records scoped provenance, not truth certification. This work is uncommitted; no commit or push was authorized or performed.

No new Agda closure, physical selection, native T9/Hamiltonian identification or constructed Postnikov tower is claimed.
