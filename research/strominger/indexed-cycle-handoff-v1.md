# Indexed-cycle packet conjecture: two steps and a retained handoff mode

Owner: `marici.Strominger`. Status: conditional recurrence constructed; stronger inferences have exact countermodels. No physical particle assignment.

## Proposed paths

The operator proposed:

    proton:   C_i -> M_i -> C_(i+1)
    neutron:  M_i -> C_i -> M_(i+1)
    electron: M_i -> C_i -> C_(i+1)

The index denotes a **new cycle copy**, not an exponent, geometric dimension or physical time. M and C are abstract sector labels at this stage. “C” is the operator's codomain-sector notation, not every mathematical map's codomain or a verified physical codimension assignment. The first arrow is within-cycle crossing; the second is next-cycle handoff. This is a distinct recurrence proposal, not a silent replacement of the earlier port-count/chart interfaces.

[Contract](contracts/indexed-cycle-handoff.v1.json) · [checker](checkers/check_indexed_cycle_handoff.py) · [receipt](results/indexed-cycle-handoff-v1.json). Registered in `contracts/port-incidence-conjecture-net.v1.json` under `indexed_cycle_handoff`.

## 1. The process needs context beyond the current sector

A shared deterministic within-cycle map is uniquely fixed by the three paths: exchange M and C.

But one sector-only handoff cannot fit them: neutron and electron both reach intermediate C, yet require different next sectors. Thus the handoff needs at least **two contexts**—a retained packet mode or equivalent source/context information. This is not a derived physical bit or qubit.

Anchor neutron context0 and electron context1. Exhaust all32 pairs of two-sector handoff functions and proton-context choices:

* **Four** completions fit the three proposed paths.
* Exactly **one** has each context-fixed handoff bijective.
* It puts proton and neutron in context0 with exchange handoff, and electron in context1 with preserving handoff.

At this two-state scope, sector-label symmetry of each handoff is equivalent to bijectivity. Either is an additional completion assumption, not an observation already supplied by the three paths.

## 2. The minimal reversible completion

Encode M=0, C=1; let b=0 mean exchange at handoff, b=1 mean preserve there. The common two-stage law is

    within cycle:       (s,b) -> (s XOR 1,b)
    next-cycle handoff: (t,b) -> (t XOR 1 XOR b,b)
    complete cycle:     F(s,b)=(s XOR b,b).

Its marked cycle-entry states are:

| Role in this proposal | State `(sector,mode)` | Complete-cycle behavior |
|---|---|---|
| Neutron | `(M,0)` | fixed |
| Proton | `(C,0)` | fixed |
| Electron entry phase | `(M,1)` | goes to `(C,1)` |
| Electron other phase | `(C,1)` | goes to `(M,1)` |

Consequently the electron continuation is

    M_1 -> C_1 -> C_2 -> M_2 -> M_3,

**conditional on this completion**. The C-entry phase is not automatically a fourth species. Exchanging sector labels swaps the two fixed points and exchanges the electron phases. Erasing the marked half-step boundary also merges the proton/neutron alternating words up to a shift; the cycle mark must remain data if they are to be distinguished this way.

## 3. What the three paths do not imply

### Electron two-cycle return is not unconditional

The three other fitting completions use a constant-C electron handoff. They give `M -> C -> C -> C ...` at cycle entries instead of return to M. Thus the proposed first path does not alone determine its next continuation.

### Global reversibility is insufficient

After the within-cycle crossing, swap the sector with a fresh register initialized to C. The whole swap is reversible; the old sector is retained in memory, but the coarse sector handoff is constant C. An exact three-cycle circuit is bijective on all16 full states while its initialized electron sector stays C after entry.

Therefore the uniqueness result requires **bijectivity on the specified minimal sector/context state with no unretained environment**. Reversibility of a larger physical system is a weaker condition.

### Sector period does not determine spinorial phase

Both exact unitary matrices

    X = [[0,1],[1,0]],      X^2= I,
    J = [[0,-1],[1,0]],     J^2=-I

induce the same exchange of sector basis labels. They have opposite two-cycle amplitude signs. Even X has both positive and negative eigenmodes. No physical rotation, spin, charge or clock follows from the sector itinerary alone.

## 4. Actual native protocol comparison

The retained common-three-carrier L/G/N sources have return ranks1/1/2. Their actual return operators N are nonzero projectors, `N^2=N`. Every L/G/N stage fixes the active return image. Thus:

* At the frozen interpretation **one native cycle = N**, all three active payloads have period1—not an electron sector swap.
* The same nonzero raw return state occurs at differently proposed sector-labelled stages. A reader of that raw state alone cannot distinguish those labels; stage/history/context is required.
* Full L/G image dimensions are12/3,3/12,4/2. They cannot be directly identified with an invertible exchange of two equal complete state spaces.

These are scoped obstructions to particular native identifications, **not rejection of every possible indexed-cycle implementation** or a claim that other native phase operations are trivial.

## 5. An explicit compatible extension exists, but does not select the assignment

Add a two-valued tag register to each actual native active return space. Retain its original induced metric and source encoders/decoders. The tensor maps `X tensor N` and either `X tensor N` or `I tensor N` implement the crossing/handoff laws on the encoded image with exact metric preservation and recovery.

This doubles raw coordinates and active rank as a declared bookkeeping extension. It is not a pre-existing native sector operation, an identification of port count with dimension or full recovery on arbitrary raw inputs. Forgetting the tag merges distinct preparations.

Both handoff choices work on **each** source payload: all **eight** proton/neutron/electron mode assignments are compatible with the unchanged payload equations. The proposed assignment is therefore not selected by this construction. A rule such as assigning handoff mode from native return rank would need its own independent source witness; equal labels or dimensions do not provide one.

## Net disposition and next physical gate

Constructed: the indexed formal model, unique minimal reversible contextual completion and explicit tagged realization. Rejected at their stated scopes: one context-free handoff; unconditional electron two-cycle return; deriving coarse reversibility from global reversibility; inferring spinorial sign; identifying the current untagged native return projector with the sector swap.

Still missing: source-grounded **sector/context readers, cycle marking and handoff operations** that select this recurrence on the actual assemblies. Physical time/rotation and particle assignment require separate attachment. No such claim is promoted.

## Verification

**18 exact check groups pass.** The contract and checker were frozen before execution; the prospective challenge passed on its first invocation:

`research/strominger/scc-freezes/indexed-cycle-handoff-v1.e8551616119b6bf4.json`

```text
python research/aspect/scc/scc.py check indexed-cycle-handoff-v1
python research/aspect/scc/scc.py check port-incidence-net-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

Finite exhaustions and native coefficient equations use exact arithmetic. No native producer CLI, proof-assistant source or gallery was run or changed. No other-owner source/shared fixture was edited, and no commit, push or deployment was performed.
