# Equivariant carrier-edge lifts reduce the choice to spectator action

## Conditional source semantics

A directed carrier arrow i->j is currently a labelled relation, not automatically
an active permutation. Test the additional proposal that it acts by g_ij in S4,
with g_ij(i)=j, and that every relabelling p transports this operation by

    g_(p(i),p(j)) = p g_ij p^-1.

This is a conditional source-operation classification. It neither selects a
physical operation nor reinterprets the degree-one DG comparison witnesses as
permutations.

## Exactly two equivariant lifts

Fix the ordered edge0->1. Six permutations carry0 to1. Its relabelling stabilizer
is {identity,(23)}. A well-defined equivariant lift must commute with that
stabilizer. Exactly two of the six permutations do:

    (01),       (01)(23).

Conversely, each extends uniquely by conjugation to every ordered edge. Thus
there are exactly two lifts under the stated assumptions:

1. swap the endpoints and fix the two nonparticipating labels;
2. swap the endpoints and also exchange the two nonparticipating labels.

Both respect reverse-edge inversion. This is a finite classification, not a
choice among arbitrarily fitted connection matrices.

## Their loop behaviour is different

For three distinct states i,j,k, compose along i->j->k->i.

- The endpoint-swap lift returns i to itself but exchanges j and k. Every such
  triangle has nonidentity holonomy. Its edge operations generate S4; based
  triangle holonomies generate the six-element stabilizer of the basepoint.
- The double-swap lift gives the identity on every triangle. Its operations
  generate the Klein four subgroup. Choosing one root gives global frames, and
  every edge is the ratio of its endpoint frames, proving path independence.

A loop observed only through its basepoint looks identical in both cases. The
state of another labelled point separates them. This is another reason not to
infer full reference flatness from a single anchored readout.

The classification uses the full four-state carrier before reference-edge
exclusion. Eighteen ordered triangles remain after deleting0->1; the same
flat/nonflat distinction survives on every one of them. It is not an artefact
of using the excluded arrow. The symmetry claim is about the carrier, with an
exclusion marking transported when relabelling that marked construction.

## What source question now decides the conditional model?

If the source says an elementary arrow leaves uninvolved labels fixed, the first
lift is forced and reference transport is not endpoint-flat. If the source
requires path-independent endpoint transport within this permutation model,
the second lift is forced and necessarily moves the other two labels as well.

Those are different source operations. Minimal support is not silently imposed,
and flatness is not used as a fitting criterion. The operational discriminator
is the action on the two nonparticipating labels, not a scalar normalization.

The result does not show that either lift is the intended tower generator. The
missing step is to establish that the carrier arrow really acts as a permutation
and to supply its spectator action. A typed adapter to the shared-leg witnesses
and the physical rung4 observation remains necessary. The permutation groups
above are not identified with physical gauge groups.

## Verification

    python research/nima/checkers/check_equivariant_carrier_edge_lifts.py
    python research/aspect/scc/scc.py check nima-equivariant-carrier-edge-lifts

Exhaust all24 relabellings and the six base-edge transports; construct both
lifts, verify inverses, all24 ordered triangle loops and the18 surviving the
reference exclusion, generated groups, based holonomy, and the endpoint-only
observation control. Machine result:
`research/nima/results/equivariant-carrier-edge-lifts.json`.
