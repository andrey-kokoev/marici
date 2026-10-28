# Counteroriented rival: native-source realization fails

## Target and verdict

Attack the rival in [persistent-seam-pe-falsification.md](persistent-seam-pe-falsification.md), holding the documented directed packets and elementary forward C/S fixed.

**Rejected:** the inverse-leg rival is an elementary realization of the unchanged source, or can be implemented as independent forward native clocks while remaining glued at every prefix on its full carrier.

**Survives:** its exact endpoint algebra when atomic inverse operations are admitted. This is not a refutation of that algebra, nor proof that the intended P/E source selects the original synchronized protocol.

## 1. Native successor and half-phase obstruction

The source supplies T1=(AB,BC,CA) and T2=(BA,AD,DB). Running the source packet constructor on each produces the same forward C. The declared elementary half-phase satisfies S^2=C on each leg.

The rival uses S inverse on the right. But

    (S inverse)^2 = C inverse != C.

The defect C inverse minus C has rank two; its kernel is only the common line span(1,1,1). Thus this is not the documented right half-phase except on stationary common-mode states. The native right-S intertwining with Kminus likewise has a rank-two defect.

Swapping AD and DB alone does not repair this: (BA,DB,AD) fails the source constructor's endpoint-composability check. Actually reversing the directed word gives (AB,BD,DA), which is composable but changes the retained directed occurrences and their shared-edge reading. Transport by -P then gives the inverse operator. This is a changed orientation policy, not the original retained word's forward successor.

## 2. Endpoint powers do not establish an executable glued history

Could S inverse = S^5 merely be five forward native steps? On the rival carrier R1x=v and R2x=-Pv, independent forward prefixes i,j propose a seam mismatch

    [h S^i - h S^(-j)] v.

As an identity for every v, this vanishes exactly when i+j=0 modulo 6. The exact six-phase orbit checks every possible residue, so this is not a finite-duration inference.

Allow each leg one I, S or C=S^2 per tick. Every non-idle first tick increments i+j by 1 through 4, never 6. Therefore no such first tick glues the entire rival carrier. A concrete state defeats even state-dependent choice of the first tick:

    v=(1,2,4),  x=Kminus(v)=(1,2,4,-4,-2).

The left shared-edge proposals for I,S,C are 1, 2/3, 2. The right proposals converted back to AB are 1, 8/3, 4. Only idle/idle agrees. Both-forward-S already has mismatch -2. In contrast, the original Kplus carrier passes the simultaneous native S/C control.

Endpoint pairs (S,S^5) and (C,C^2) do glue, as previously proved. Replacing these endpoints by a forward execution silently hides incompatible intermediate proposals. This attack excludes independent native-clock implementations with gluing at every prefix, not arbitrary serial rewriting: serial arbitration changes the other triangle's reading and is a different documented rival. No resets, correction maps, extra state, hidden unglued prefixes or arbitrary multi-step atomic ticks were admitted in this test.

## Consequence

The previous claim of using existing powers was an endpoint statement, insufficient to establish an elementary source binding. To keep the counteroriented rival, explicitly supply an atomic inverse operation, a reversed local orientation policy, or a different intermediate-state/gluing policy. None has yet been selected for the intended pair.

The stronger source audit excludes this rival under the unchanged native-forward interface. It does not establish physical P/E identity, eliminate the serial rival, or prove the original source-selection conjecture.

## Reproduction

`python research/strominger/checkers/check_counteroriented_rival_source.py`

All 16 exact checks passed, including source-constructor rejection, rank-two defects, the complete prefix-phase comparison, a hostile state and the original synchronization positive control. [Receipt](results/counteroriented-rival-source.json) records the matrices, all eight non-idle first-tick defects and source hashes.
