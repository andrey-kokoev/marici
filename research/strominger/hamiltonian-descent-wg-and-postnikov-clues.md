# Hamiltonian-compatible WG: a tested fixed-Gram instance and Postnikov clues

## Result and correction of scope

There IS prior mathematical continuous descent between declared rung12 and rung4 models: `research/nima/rotor-rung4-action-metric-bridge.md` constructs it in the fixed stabilizer-probe Gram tower. The earlier conversational statement that there was no Hamiltonian connection was too broad. It remains correct for an independently selected physical Hamiltonian on the original137-record T9 interface.

The existing bridge is now reused in an executable restricted Hamiltonian-compatible Witness Generator.45 new exact checks pass; the prior45-check bridge is freshly rerun as a dependency. The new checker tests direct descent, composed descent, full source/hidden retention and refusal of incompatible inputs.

This is not an independently derived source H12: the prior top generator was constructed FROM the bottom rotor. That direction of construction remains explicit.

## Prior-work search

Inspected sources, and the useful distinction each provides:

| Source | Clue | Boundary |
|---|---|---|
| `research/nima/carrier-gram-restriction-tower.md` | Actual metric-adjoint projections compose; removed orthogonal records reconstruct the input. | Gram eigenvalues are not Hamiltonian energies. |
| `research/nima/rotor-rung4-action-metric-bridge.md` | With PE=I, D12=E D4 P gives P D12=D4 P and a metric-conservative continuous extension. Explicit quadratic energy and rank-two form are available. | Declared fixed-Gram carrier, bottom-up extension; not the137-record/native interface. |
| `research/nima/whole-history-hamiltonian-prior-work-search.md` | Distinguishes continuous rotor evolution, retained provenance and autonomous history creation. | A programmed history Hamiltonian does not source-select the native programme/clock. |
| `research/nima/rung-descent-endpoint-binding.md` | Equal J4 readings can conceal different dynamical responses. | Retention alone does not make the unchanged aggregate a sufficient dynamical state. The software-policy choice has subsequently been resolved separately. |
| `research/kitaev/ascending-rungs-stabilizes-the-law-and-moves-the-problem-to-truncation.md` | Task-relative truncation requires an actual factorization, not just high-sector vanishing; Moore residuals distinguish kernel from authorized repairs. | General simplicial/hypercrossed structure does not provide this source's face maps or Hamiltonian. |
| `research/voevodsky/cosmology-descent-of-local-total-lifts.md` and `cosmology-sufficient-descent-vanishing-criteria.md` | Local witnesses can have successive Cech/Postnikov gluing obstructions; existence and uniqueness are distinct. | Those coefficient/lift spaces are different sources; their vanishing hypotheses are not supplied here. |
| `research/chatgpt/marici_native_pullback_obstruction.md`, section5 | A concrete nonzero Postnikov attachment can prevent a requested normalized lift despite an endpoint map. | Its Ext/Tor detector is not a Hamiltonian obstruction for this carrier. |
| `research/nima/checkers/check_postnikov_tower.py` | Historical numerical speculation connecting stage labels and correction factors. | It prints scalar powers and candidate numbers; it supplies no actual homotopy groups, attaching cocycles, projection maps or Hamiltonian compatibility proof. It is not a Postnikov construction certificate. |

Search was bounded to local research/docs, excluding dependency/build trees and mirrored collections. No external literature verification, global absence theorem or fresh execution of the unrelated topology/coefficient suites is claimed.

## Restricted WG contract

The state is a real finite quadratic Hamiltonian model

    (G,D,Omega,K,provenance),

with positive coefficient metric G, antisymmetric (possibly degenerate) form Omega, symmetric energy Hessian K, and common declared time parameter:

    x'=Dx,
    energy(x)=x^T K x/2,
    D^T Omega=K,
    D^T G+G D=0,
    D^T K+K D=0.

The sign convention and allowance of degenerate forms match the inspected prior rotor. This is not a general generator for arbitrary nonlinear or unbounded Hamiltonians.

Supply a proposed embedding E and projection P. The admitted interface satisfies

    PE=I,
    G_target=E^T G_source E,
    E^T G_source=G_target P.

Set N=I-EP. The decisive dynamical gate is

    P D_source N=0.

It says hidden directions cannot influence the visible derivative. If it fails, no autonomous projected generator can reproduce every source state.

The generator constructs

    D_target=P D_source E,
    Omega_target=E^T Omega_source E,
    K_target=E^T K_source E,

and verifies the target Hamiltonian equations plus the full split identities

    P D_source=D_target P,
    N D_source=D_source N,
    Omega_source=P^T Omega_target P+N^T Omega_source N,
    K_source=P^T K_target P+N^T K_source N.

The return value contains the complete source, target, E, P, N and verified identities. Reconstruction is x=E(Px)+Nx. Hidden energy and dynamics are retained, not replaced by zero. A separate two-oscillator control verifies nonzero hidden dynamics and energy.

This is a WG on inputs WITH these admissibility conditions; the executable validator rejects other inputs. It does not prove that every Hamiltonian has such a reducing interface, discover a canonical interface or authenticate caller provenance. Its assertions are exact symbolic Python checks, not dependent-type proof terms or a new Agda closure.

## What composes

Exact finite-dimensional generator intertwining implies

    P exp(t D_source)=exp(t D_target) P

for all real t, using the same supplied time parameter. It is stronger than matching a sampled tick or aggregate response. The checker additionally tests seven power-series coefficients; the all-time conclusion follows from the exact generator identity, not from those seven samples alone.

For a sequence of admitted interfaces, the projections and generator witnesses compose. Quadratic energy splits into visible and retained hidden terms; in general total source energy is NOT just the target energy evaluated on Px.

The direct prior12-to4 interface and two explicitly declared schedules recover exactly the same projection, D4, Omega4 and K4:

- eight consecutive dimension drops:12,11,10,9,8,7,6,5,4;
- six grouped operations:12,10,8,7,6,5,4.

The latter shows that six WG operations CAN suffice after a schedule is specified. It does not derive that schedule, equate a dimension with a native rung, or turn the labels9/8/7 into a sequence of WG ticks.

## What Postnikov theory contributes—and does not

For an actual space X, a Postnikov stage has a projection P_n X to P_(n-1) X and, in the usual connected setting for n>=2, fiber K(pi_n X,n). Its extension is described by a k-invariant in degree n+1, with local coefficients when the fundamental-group action is nontrivial.

These data explain retained higher distinctions and obstruction/ambiguity in lifting or gluing witnesses. Nonzero k-invariants are legitimate extension data; demanding that all vanish is NOT a general requirement for descent.

But our native rung diagram has not been identified with these Postnikov stages. For the discrete group S4, its classifying space BS4 is already K(S4,1): its higher homotopy groups vanish. Nontrivial higher stages require another specified space or higher structure. Merely naming BS4 does not produce an eight-level physical tower; calling another S4 factor pi2 would also conflict with abelianness of higher homotopy groups.

Functorial truncation can carry homotopy-coherent actions, but does not automatically carry a symplectic form, energy observable, differentiable generator or physical clock. The Hamiltonian WG relation must explicitly request those additional structures and their compatibility.

Thus the actionable Postnikov clue is: define the actual truncation/task map and test whether the dynamics factors through it, retaining the extension witnesses. In this finite linear instance, P D N=0 is the concrete dynamical factorization test. It is an analogue, not a newly proved identification with a Postnikov tower.

## Hostile controls

The checker rejects:

- a valid metric-conservative Hamiltonian coupling a hidden direction into a visible derivative;
- coordinate deletion substituted for the actual Gram projection;
- a changed Hessian violating the Hamiltonian equation;
- a stationary flow whose form has unsupported mixed visible/hidden terms;
- an interface without declared provenance.

The coupled example has equal projected initial states but different projected derivatives. That is a direct counterexample to assuming that any WG iteration or endpoint readout automatically descends Hamiltonian dynamics.

## Next source obligation

To turn this tested instance into the requested native rung12-to-rung4 bridge, supply an independently specified rung12 Hamiltonian state and the operation-preserving map from its carrier to the admitted T9 records. Then run the factorization/form/energy gates on that map. A failure must remain an obstruction; constructing H12 from H4 cannot count as an independent derivation of H4 from that source.

An actual Postnikov identification additionally needs the source space, homotopy groups/actions, projections and k-invariants, and an explanation of how native rung labels correspond to stages. Physical Hamiltonian selection, time/action units and calibration remain separate.

## Top-down follow-up

`source-arrow-hamiltonian-top-down-descent.md` now constructs a DIFFERENT top generator independently of D4, from the existing induced vertex-cycle action on twelve carrier arrows.54 checks verify direct descent and a six-step reducing-mode schedule. Its hidden rotor dynamics make the naive12->11 coordinate drop fail. The earlier schedules above remain valid for their original bottom-up source, not for this new source. Native137-record and physical Hamiltonian selection remain open.

## Verification and artifacts

    uv run research/strominger/checkers/check_hamiltonian_descent_wg.py

PASS:45 new checks; the existing45-check rotor bridge and its source-coordinate, Gram and seed-section dependencies freshly rerun. Counts are not independent evidence to be summed.

- `research/strominger/checkers/hamiltonian_descent_wg.py`
- `research/strominger/checkers/check_hamiltonian_descent_wg.py`
- `research/strominger/results/hamiltonian-descent-wg.json`

Graph report: `ev-000000015897-5a165c55-c0e4-4de1-b63b-29908c80e3ed` (proposal `ep_9dd995de-97b9-4585-8751-ce54fe5e7ce2`). This records policy-valid report provenance, not truth certification. No Git commit or push was authorized or performed for this work.

No new physical admission, native T9/Hamiltonian identification or constructed Postnikov tower is asserted.
