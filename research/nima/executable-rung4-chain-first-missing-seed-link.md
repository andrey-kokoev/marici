# Executable rung4 chain: the first missing seed link

## Selected existing example

Use `check_rung_transport_diagram.py`, the implementation explicitly matching the confirmed 12--9-->6, 11--8-->5, 10--7-->4 diagram. Do not substitute the different eight-step retained-total schedule merely because it also ends at a rung labelled four.

The checker imports `check_shared_leg_dg_realization.py`. Reading that implementation exposes the actual upstream inputs, so the verified chain can be separated from its unconstructed seed adapter.

## End-to-end ledger

| Step | Actual executable input/output | Status |
|---|---|---|
| Six-arrow seed | AB,BC,CA,AD,DB,BA | Known starting object; not consumed by this rung checker |
| Four-state slot labels | All ordered unequal pairs except (0,1), plus four state labels | Explicit fixture enumeration; not generated from the seed within this chain |
| Typed primitive maps | Eleven x:A->U, eleven y:U->B, four s:A->V, four t:V->B, d:A->B | Constructed typed graph after supplying family sizes and intermediate objects |
| Matrix preparation | x_i=I+(i/3)H, y_j=I+(j/5)K in both blocks; d=2I | Supplied fixtures, not seed-derived amplitudes |
| Comparison witnesses | Differences from chosen base legs and independent base-path/reference witnesses | Declared free DG generators with checked boundaries |
| Composite records | 121 arrow composites plus16 state composites; unit initial masses | Exact products and retained labels |
| Rung12 | The137 individual records | Explicit |
| Rungs11,10 | Source- and target-indexed retained views | Exact lossless reindexing |
| T9 | Two incoming-family promotions | Two explicit candidate endpoint policies |
| T8,T7 | Source/target presentations of T9 | Both squares checked, not independent physical generators |
| Rungs6,5,4 | Transported records and their two indexed views | Leaves, matrices and masses recover exactly |
| Rung4 readout | Member-weighted matrix mean minus fixed2I | Explicit conditional readout, not physically derived normalization |
| Follow-up composition | Compose promoted values through d^-1 | Existing probe distinguishes endpoint policies; does not physically select one |

The first missing connection is BEFORE the input of this verified rung transport: realization of the labelled shared-leg matrix preparation and comparison witnesses from the actual seed/native derivation. It is not another recovery lemma at rung4.

## What not to conceal in the seed adapter

A bijection from twelve generated seed positions to twelve ordered state pairs would address labels only. It would not derive exclusion of the chosen reference edge, the separate state branch, the two independent leg roles, matrix amplitudes, direct reference or witness realization. The matrix assignment depends on enumeration indices; no seed dynamics in the inspected implementation produces the coefficients i/3 and j/5.

The native comparison constructor supplies actual pointed equivalences and retained witnesses. The DG fixture supplies formal graded leg homotopies and assigned numerical responses. A bridge between them must explain the interpretation; identifying two uses of 'witness' is not enough. Existing two-channel work explicitly keeps the finite comparison witness separate from fixture amplitudes.

## Alternative branch control

`check_growth_rung4_readout.py` does execute a graph-to-rung4 transport, but source inspection shows its input is the four-edge paw {(0,1),(0,2),(1,2),(0,3)}, expanded to both orientations. Its eight-step retained-total schedule is not the confirmed horizontal transport diagram. It leaves physical lengths and times null. It therefore cannot silently supply the missing seed-to-shared-leg physical adapter.

The Machian body cycle starts directly from the two seed cycles and constructs geometry, but does not implement this confirmed rung diagram; its completed stability and radial-scale failures must also remain visible.

## Disposition and non-duplication rule

This is the executable chain to extend if working on the confirmed-rung response branch. Preserve its existing successful downstream tests. The unresolved upstream object is a seed-derived preparation/response interpretation with actual comparison witnesses. Do not tune its supplied matrices or claim its counts as proton/electron realization.

Prior work already tries endogenous family feedback and an adapter from conservative exchange. The natural exchange-to-family linear adapter fails; the family law preserves but does not create its means. Repeating either calculation would not fill this first link.

This audit does not establish that no seed adapter exists anywhere in the repository. It identifies exactly what this strongest inspected confirmed-diagram example imports, what it assumes, and which upstream connection is absent from its executable chain.

## Fresh verification

    python research/nima/checkers/check_rung_transport_diagram.py

Passes, including its imported shared-leg DG checks, both squares, both complete routes, all137 retained leaves/masses, fixed-reference offsets, corrupted-map and wrong-weight controls, and distinct32-versus1 final-family candidates. No new checker was written.
