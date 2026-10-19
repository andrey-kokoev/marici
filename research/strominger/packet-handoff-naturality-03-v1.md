# Packet handoff ground naturality — iteration 3/10

Owner: `marici.Strominger`. **Iteration complete; objective in progress.**

[Live conjecture net](contracts/packet-handoff-naturality-conjecture-net.v1.json) · [contract](contracts/packet-handoff-naturality-03.v1.json) · [checker](checkers/check_packet_handoff_naturality_03.py) · [receipt](results/packet-handoff-naturality-03-v1.json).

## 1. Fresh descent into primitive constructors

The proton's pure source assembler was called **in memory** on its actual six directed arrows and coordinates. It regenerated all **1836 typed endpoints and coefficients exactly**, matching the historical native manifest. No producer entrypoint or write-capable CLI was run.

The neutron's actual selected plane numerators, repeated sector metric and denominator-aware arrows reconstruct its L/G/N operators. Electron's actual four face projectors reconstruct L and G=N. The inspected producer code gives the same L,G,N stage order, not a special electron G-entry rule.

Typing distinction: proton's stored arrows explicitly name `raw/local/aligned` endpoints. Neutron/electron stores retain stage tags and coordinate indices. For them the three-phase endpoint cover below is a **declared conservative elaboration** of the supplied staged protocol, not an independently observed clock or an inferred physical time.

## 2. Primitive endpoint types need not be changed to realize the words

Retain three DIFFERENT full objects:

    R = full raw space
    X = Image(L), with its derived metric
    Y = Image(G), with its derived metric.

Their actual rectangular primitive maps are

    L_typed = D_L L : R -> X
    G_typed = D_G G K_L : X -> Y
    N_typed = N K_G : Y -> R.

For every complete input basis, encoding the destination equals the actual native projected raw output. All linear raw-reader squares therefore commute. Source-bound proton/neutron generators and all24 electron native operations intertwine all three rectangular maps, including the raw target.

| Source | R | X | Y |
|---|---:|---:|---:|
| Proton | 36 | 12 | 3 |
| Neutron | 36 | 3 | 12 |
| Electron | 8 | 4 | 2 |

No `D_L N` endpoint readout adapter is used here. **N still lands in R.**

How can R and X have the same M/C role despite different dimensions? They are sections over the same native local port **base family**, before and after local rank-one fiber selection. Proton has twelve local triples, neutron three sector-wide twelves, electron four face spin pairs. Their ambient fibers and legitimate preparation/readout tasks remain different.

Extend iteration2's tested smaller/larger image-channel role convention to this base family. This is an explicit macro-role convention, **not literal physical main/codimension**:

    Proton/electron: R:C, X:C, Y:M
    Neutron:        R:M, X:M, Y:C.

Now the proposed two-arrow words have exact primitive realizations:

| Candidate | Native states | Commands | Role word |
|---|---|---|---|
| Proton | X12 -> Y3 -> R36 | G,N | C,M,C |
| Neutron | X3 -> Y12 -> R36 | G,N | M,C,M |
| Electron | Y2 -> R8 -> X4 | N,L | M,C,C |

This improves iteration2: no primitive endpoint retyping is needed. But **M/C cannot simultaneously mean a single fixed full state space**. In particular, proton's initial C12 and final C36 are not interchangeable preparation objects just because their base-family label agrees.

Exact nonzero raw-minus-L witnesses show why. Their local image is zero but their raw reader is nonzero; the lost ranks are24/33/4. No silent raw/local equivalence is admitted.

## 3. The primitive phase/history obstruction is now exact

The staged protocol is

    R --L--> X --G--> Y --N--> R.

A phase-guarded history records source identity, initial primitive phase, and every command. It rejects G from R, repeated L, an incorrect initial phase and a changed source binding. Every three-edge cycle returns to the same TYPE and induces the appropriate active-return projector on its entire input space.

All proposed words are legal **windows**, but their origins differ: local X for both baryons, aligned Y for electron. Proton also has the electron's M:C:C window; electron also has proton's C:M:C window. The source-driven proton manifest starts its constructor at raw R; neither electron's native seed/archive nor the inspected staged producers contain a special alignment-entry mark selecting the proposed relative origins.

**Do not confuse window realization with an iterable two-arrow cycle.** Two atomic arrows shift phase by2 modulo3. Repeating that strobe has minimal phase AND role period **3 for all three sources**. It does not give a proton/neutron fixed role and an electron two-cycle under the same atomic sampling rule.

Exhaustion of all five partitions of three phases gives another exact result: the only quotient preserving both M/C observations and deterministic next-phase evolution has **three states**. The two coarse M/C labels alone are not a Markov state at this native atomic clock. This is a source-protocol result, not the earlier abstract two-context reversible tag model, and not a physical-clock deduction.

## 4. Equal matrices and old archives cannot supply the missing phase law

Electron's G and N have the same64 weighted coordinate entries, but they occupy different stage occurrences and have different primitive domains/targets in the declared cover. Erasing their stage tags reduces144 weighted occurrences to80; erasing weights too leaves64 coordinate pairs. These are different tasks/counts, not an optimized equivalent phase protocol.

All stages fix each active return state. An empty history and a full LGN history therefore have the same raw endpoint, but remain different histories. The active payload alone does not recover the primitive phase mark: it admits all three marked phase lifts.

The existing shared image-word API accepts arbitrary stage words such as G,N,L and evaluates them to identity on the active return. Baryon image interfaces likewise accept G from their prepared raw seed while retaining its command history. That is **correct at their stated active-image/endomorphism scope**, not a bug. Those APIs do not enforce occurrence-level phase composability and cannot be treated as already implementing the primitive phase guard.

The electron archive contains source hash, initial spinor and native spin word, not an alignment-entry field. Its actual source/packet recovery was freshly exercised. Recording a history does not choose an unrecorded origin or reset policy.

## 5. Disposition and next hard test

Constructed: native base-family role windows, full-reader rectangular stage maps, and an explicit source/phase/history guard.

Rejected **at scope**: interpreting these windows as a stationary two-atomic-arrow recurrence, identifying phase-erased equal matrices with primitive occurrences, or claiming the inspected producers select electron's shifted entry.

Still open: a source-selected coarse event boundary, common physical M/C meaning and native indexed handoff law. The period result does not exclude a differently justified sampling/reset rule; such a rule must be supplied and checked rather than inferred from a short role word.

**Iteration4 executable frontier:** `geometric-base-versus-fiber-role-naturality`. Test whether the capacity-selected M modules really are geometric main spaces. Using the actual native coefficient and spatial generator representations, compute equivariant Hom spaces and invertibility obstructions. Compare proton's transported alignment module, neutron's sector-placement module and electron's spinor doublet—including its central minus sign—with their geometric main carriers. This targets the remaining meaning of M, not another fitted phase predicate.

## Verification

**24 exact check groups pass**, with the model frozen before its first successful check and a subsequent frozen replay passing:

`research/strominger/scc-freezes/packet-handoff-naturality-03-v1.55f6b92a4e70f6e7.json`.

The challenge is a replay of the same frozen checker, not independent peer review.

```text
python research/aspect/scc/scc.py check packet-handoff-naturality-03-v1
python research/aspect/scc/scc.py check packet-handoff-naturality-net-v1
python research/aspect/scc/scc.py check port-incidence-net-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

The pure proton source assembler was replayed without writes. Native producer entrypoints, proof-assistant compilers and external publication were not run. No other-owner/shared fixture edit, commit, push, physical identification or new clock is claimed.
