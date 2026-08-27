# The five semantic gates form one axis, not the whole compiler

## Result

The sequence of semantic-pullback gates should stop at five rather than absorb
every operational requirement into a flat list.

The first axis asks whether a constructor means what the claim says:

1. source-state separation;
2. target-image admission;
3. local and global coherence;
4. distinction-preserving completion;
5. source authority when the claim carries a root or frame.

A second axis asks whether that meaningful constructor can operate under its
declared world:

- resource conservation;
- temporal and epoch validity;
- fault-model survival;
- any additional physical modality declared by the source.

An operative constructor must pass both axes. Operational failures are not new
kinds of semantic residual, and semantic validity cannot discharge them.

## Three operational hostiles

### Resource overdraft

A constructor can have a perfectly defined input and output meaning while
claiming two conserved tokens from one input token. It fails the resource law
\(1=2\), regardless of its semantic behavior.

### Expired authority

Evidence rooted in epoch 1 can be faithfully transported to an execution claim
in epoch 2. Without an authorized epoch-transition constructor, the transport
preserves content but not temporal authority.

### Wrong fault model

For three replicas with quorum size two, the minimum overlap is one. Under one
Byzantine fault, that sole overlapping replica may equivocate. The same quorum
shape that works under crash assumptions therefore fails Byzantine survival.

## Coherence correction

The third semantic gate must already include global coherence. Vanishing local
face syndromes do not guarantee a global frame when a nontrivial first
cohomology class remains. Likewise, a Beck–Chevalley comparison between two
source-authorized routes belongs to relation preservation, not to a new gate.

## Compiler shape

The correct architecture is a product of typed obligations, not a longer
single ladder:

```text
semantic validity and source authority
            ×
operational realizability
            ↓
operative constructor
```

This product is partial. Passing either factor alone does not create the final
arrow.

## Falsifier

The checker presents three constructors marked as passing all five semantic
gates. A compiler that admits any of them without separately checking resource,
epoch, and fault obligations is rejected.
