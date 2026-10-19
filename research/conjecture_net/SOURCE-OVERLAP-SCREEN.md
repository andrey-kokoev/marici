# Cross-source overlap: a restricted obstruction and a safe package

Contract: `contracts/source-overlap-screen.v1.json`.
Implementation: `source_overlap_screen.py`.

## The simplest direct identification fails

Ask whether one fixed linear map L can identify the full Bool witness with the retained exchange source while assigning native left/right flips P_L,P_R to individual exchange ports E_a,E_b:

`E_a L=L P_L`, `E_b L=L P_R`.

This is a **global, fixed-fibre, single-port assignment screen**. It is a necessary operator-law test for that particular proposal, not a theorem about all endpoint-dependent attachments, word-valued bindings, dilations, new controls or physical common carriers. It forgets port endpoints for the screen; actually typed overlap maps would have additional obligations.

The Bool representation has four one-dimensional joint character spaces (++,+−,−+,−−). The existing exchange encoder gives `E_i=I16⊕T_i`. For distinct ports a,b, the only simultaneous T_a,T_b character space is ++, with mismatch dimension four. All other character spaces vanish. Thus every L annihilates three Bool character directions and has rank at most **one**. Anchors add sixteen possible invariant output directions, but not extra source characters: the full intertwiner-space dimension is twenty and every map still has rank at most one.

If both flips are assigned to the same port, ++ and −− survive. The maximum map rank is **two**, still less than four. This is a parity quotient, not a faithful realization of the independent native flips.

The audit solves the joint eigenspaces exactly for **all 36 ordered port assignments**, checks a complete intertwiner basis against both equations, and derives rank bounds from the complete source character decomposition. It does not confuse the dimension of a space of maps with the rank of an individual map.

### Why the obstruction is sourced

Write `K=G^-1`, where G is the positive mismatch metric. The negative eigendirection of T_i is K e_i. Its G inner product with K e_j is K_ij. The feature rule gives `K_ii=2` and every off-diagonal K_ij positive. Distinct negative eigendirections are independent and nonorthogonal: there is no simultaneous −− direction and no −+ or +− direction. Only the common fixed complement remains.

This is stronger than merely observing that the target operators do not commute. It identifies exactly which source information the attempted overlap would erase. A common invariant vector can be transported; the full Bool dynamics cannot be identified by these single-port assignments.

## Bounded word-valued test: actual typed loops

The next screen considers every **nonempty closed typed word through length twelve** of the discrete source port updates, based at each actual source vertex A,B,C,D: **840 words**. It does not range over newly chosen continuous spectral durations. A necessary condition to transport even one full native flip is a target −1 eigenspace of dimension at least two, because each native flip has a two-dimensional negative eigenspace.

For these 840 target loop operators, exact elimination gives negative eigenspace dimension zero in 520 cases and one in 320 cases. None meets that necessary condition. Conserved anchors add only positive eigendirections and do not repair the deficit. Thus no loop in this finite family can realize a full native flip by an injective fixed-fibre intertwiner.

This exhausts the stated finite horizon, **not all possible word bindings**. Longer words, endpoint-dependent attachments, a different target or independently justified extra operations remain open. No floating-point eigenvalue tolerance is used.

## Positive result: an indexed coproduct, not a physical identification

The two existing instances can be packaged faithfully in

`V_package=C4⊕C22`, `M_package=I4⊕M_exchange`.

The coordinate inclusions J_B,J_E are isometries for their source metrics. Native operations lift as `P⊕I22`; exchange operations lift as `I4⊕E_i`. Consequently `lift(T) J=J T`, and each source's identities and composition laws are preserved. The same spectral rule extends each lifted metric involution. Quadratic readouts pull back along the inclusions, and retained records carry their unchanged source data plus a component tag.

This is a **source-indexed package of alternatives**, not a tensor-product model of simultaneously prepared systems. The audit does not authorize cross-component superpositions, instruments, arrows or free actuation. A mixed-component executable word is rejected. Inactive components are retained, rather than silently deleted.

The lifted families commute across blocks **because the package makes them disjoint**. That is a packaging convention, not a new native commutation relation or evidence of physical decoupling. This construction shows a shared structural implementation can preserve both models, but it does not supply overlap maps between them or explain their common physical origin. Calling an arbitrary direct sum a universal carrier would evade the programme's source-derivation requirement.

## Next admissible gates

1. Supply a sourced attachment relation or observable overlap that is stronger than conservation of an uncalibrated scalar norm.
2. Specify a word-valued or endpoint-dependent port binding and its retained-record/coherencer laws. The single-port and length-twelve fixed-fibre screens do not settle longer words or endpoint-dependent cases.
3. Supply and justify an actual cross-component coupling/control or a common preparation/instrument model; do not obtain it merely by allowing every matrix on C26.

The programme remains open, with null outcomes. Both this screen and its package are audit-only mathematical work, not a new operator-admitted proof link or physical-source bridge.

```sh
python research/conjecture_net/check_source_overlap_screen.py
python research/conjecture_net/test_source_overlap_screen.py
```
