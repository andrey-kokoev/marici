# Neutron as compatibility filler: first local prototype

## Proposed interpretation

The neutron is a compatibility filler for proton/electron role exchange,
rather than an independently appended body. Test the compatibility part first,
using actual maps from the current phase-first assembly.

## Fixed-chart construction

For each actual native P→N→E packet, write its full five-slot maps as

    A : V_P -> V_N,
    C : V_N -> V_E.

Both are invertible coordinate permutations. Use B=V_N with the fixed neutron
chart, all geometric aliases and absolute occurrence origin retained. Define

    f(p)=A(p),   g(e)=C^(-1)(e),
    K = { (p,e,w) | w certifies A(p)=C^(-1)(e) }.

The right leg is an inverse coefficient comparison, NOT an asserted native
E→N realization command. Endpoint histories remain separate fields in K.
At nonzero origins the retained native interface witnesses are explicitly
labelled as origin-zero templates; endpoint/base frames carry the selected
origin. This is not a full proof of shifted native occurrence coherence.

The compatibility condition checks all five slots, not merely a visible face
or its common spectral component. For fixed charts, each compatible pair has
one mediating coefficient vector n, and that n recovers both endpoint vectors.

This is a strict/discrete-base pullback prototype. It is not a formal general
homotopy-pullback construction. In particular it does not yet admit arbitrary
nontrivial comparison paths in the base.

## Fresh execution

The current helium-4 reference contains **2 native P→N→E packets**. Tested:

- generic nonzero complex data and all five basis vectors;
- absolute origins 0, 1 and 7;
- **36 compatible cases**, recovering the exact native neutron packet;
- **4 rejected cases**: changed coefficients and mismatched absolute origins;
- histories that differ remain different complete pullback records, even when
  their common base values agree.

The test uses the owning phase-first APIs directly. It does not alter them.

## What swapping establishes—and does not

Every pullback has a canonical exchange of its two diagram legs:

    (p,e,w) -> (e,p,w^(-1)).

The implementation retains endpoint tags, reverses comparison direction and
checks that two exchanges restore the complete presentation exactly. This is
symmetry between the original diagram and the diagram with its legs reversed.

It is NOT yet a duality converting a proton object into an electron object in
the original diagram. Such a duality must additionally act on their native
marks, occurrences, geometric roles and histories. The current reference has
no native reverse electron-to-neutron edge for these packets. Inverting its
coefficient permutation does not supply that missing realization command.

## Interpretation

The compatibility part works locally: native neutron coefficient data mediates
the proton/electron pair without losing context or history.

But the base was deliberately chosen to be the existing neutron chart. Thus
this is a consistency test of the proposed interpretation, not an independent
derivation of neutron geometry, necessity, multiplicity or particle counts.
The fixed-chart coefficient solution is structurally guaranteed by the two
invertible maps; its successful execution is not evidence for a new physical
law.

The remaining substantive tests are a nontrivial source-backed species duality
and its compatibility with phase histories and the global branch comparisons.
No 400-branch lift or Pb-208 identification is claimed.

## Reproduce

```sh
node research/realization-tower/check_neutron_pullback.mjs
```

Receipt: [results/neutron-pullback-v1.json](results/neutron-pullback-v1.json).
