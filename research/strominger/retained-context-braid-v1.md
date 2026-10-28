# Retaining contexts closes the L/R action on eight references

## Constructed result

The five-slot failure can be repaired at the **reader-transport level** without deleting an old context or inventing an amplitude. Closing the actual reference support under L and R grows it

```
5 -> 6 -> 7 -> 8,
```

then stops. The result is the four central tetrahedral vertices plus the four outside contexts obtained by native P completion, one for each face. The action is an exact geometric isometry on these eight references.

This gives a context-covariant extension and a strict comparison diagram compatible with the native PN/NE maps. It does **not** yet generate the drawn P/N/E layers: the resulting simultaneous transport of field and reader preserves their local readout.

## Source-derived support, candidate transport operation

The initial native chart has central references

```
v0=(1,0,0,0), v1=(0,1,0,0), v2=(0,0,1,0), v3=(0,0,0,1)
```

and outside reference

```
u0=(-1,1,0,1).
```

The recovered/declared frame operations act by coordinate permutations

```
L=[3,2,1,0], R=[0,3,2,1].
```

Support closure first discovers

```
u0 --L--> u3=(1,0,1,-1)
   u3 --R--> u1=(1,-1,1,0)
   u1 --L--> u2=(0,1,-1,1).
```

Each ui is independently reproduced by the native P completion in the corresponding transported marking. No new FCC site or fitted geometry is introduced. The eight-reference action preserves every pairwise squared distance. All eight generated frames transport the complete source P/N/E charts, including the E chart's additional geometric mark.

The geometric support is source-constructed. Admitting its simultaneous field/reader transport as a new operation remains an explicit experimental extension, not a claim that the original five-slot grammar already contained L and R.

## How the missing reader comparison is represented

Let a be the coefficient bank indexed by all eight references. For a frame g, transport the bank by the induced reference permutation and transport the reader by the same g. Then

```
read_g(transport_g(a)) = read_identity(a).
```

This retains every coefficient and supplies a concrete invertible transport between the marked readers. The original five-slot input determines only five bank entries; the other three remain **independent symbolic parameters**. Neither zeros nor equal-value copies are silently inserted.

A passive change of reader at a fixed field is different. Two banks can agree on all five original entries and differ on the reversed reader's outside coefficient. The checker retains that counterexample. Thus the new transport law does not derive a unique eight-entry preparation from the old packet.

## Compatibility with actual native operations

The native PN and NE transfers preserve their named five-reference set and act by their source-defined coefficient permutations. Embed each in the corresponding five positions of the eight-reference bank, leaving the complement retained.

For every one of the eight frame actions g and every full-bank basis vector, the checker verifies

```
transport_g ∘ PN = PN_g ∘ transport_g
transport_g ∘ NE = NE_g ∘ transport_g.
```

The source charts and outside marks are independently regenerated in each frame by `GenerativeAssemblyRules`. The native five-slot readout agrees exactly with bank restriction after both transfers. Full algebraic inverse recovery holds; this does not add a native inverse-NE arrow or onward action at the terminal E packet.

These are actual coefficient/interface naturality squares, not merely equal endpoint counts.

## A strict context-transport simplex witness

Use four lifted chart occurrences 0,1,2,3. Assign each oriented edge i->j the complete-bank transport `q^(j-i)` with grade change j-i. All four triangular face comparisons are strict equalities on all eight basis vectors. The two tetrahedral reductions from 0 to 3 therefore agree.

This constructs a **strict witness for this context-transport diagram**. It is not an analytic filler for arbitrary native homotopies, nor a proof that the three physical tetrahedra themselves provide these maps automatically.

The earlier actual incidence target remains

```
T242 -- F538 -- T184 -- F403 -- T174,
```

with common edge E368. The context bank supplies a representation in which its old/reversed-reader comparison can be discussed without identifying distinct fifth references. Binding the complete split/leaf evolution to that incidence target remains separate.

## LRRR and the retained braid discrepancy survive

On the bank, one chronological LRRR block gives q. Four blocks return bank coefficients and the finite frame, but retain grade +1 and all sixteen leaf-action records; the three context-split events per block remain in the earlier seven-event schedule.

LRLR and RLRL still have equal finite coefficient actions and differ by one Sigma in the retained grade. The larger bank does not erase that discrepancy.

## What this does not generate

The checker compares native common/positive/negative spectral readouts in all transported frames. They are unchanged when the field and reader move together. Thus this operation is currently a covariant re-presentation, not a mechanism selecting new P/N/E surface occupations.

The next operation-level binding must decide which split/leaf events are native attachments and which are reader transport, using the same bank. It must also supply or derive the preparation of exposed context values. Merely iterating the verified coordinate action cannot produce the layer words.

## Reproduce

```
node research/strominger/checkers/check_retained_context_braid.mjs
```

**14 exact check groups pass**, including the passive-reader ambiguity and the unchanged-readout control.

- Executable experimental model: `retained-context-braid-model.mjs`
- Receipt: `results/retained-context-braid-v1.json`
- Prior obstruction and actual span: [binary-simplex-native-binding-v1.md](binary-simplex-native-binding-v1.md)
- Retained seven-event schedule: [binary-simplex-braid-v1.md](binary-simplex-braid-v1.md)

No production native rule or Three.js layer definition is changed.
