# The source retains a comparison witness, not a chosen flat section

## Constructor audit

`WholePackageResolution.agda` takes both complete boundary packages and a
supplied pointed equivalence as inputs to `compare-rule`. It does not invent
that equivalence. `WholePackageSigmaPi.agda` stores it in the comparison code,
with both boundary values and their compatibility witness. Composition retains
both parent comparison packages and the composite equivalence.

Thus the source permits both fixed-package and boundary-changing comparisons.
The fixed fourQ swap is one supplied witness, not the universal edge constructor.
The appropriate source-level response is to retain the actual witness rather
than choose flatness for the whole type.

## Exact finite realization

Take four copies Q_i of the same four-element carrier, distinguished by value i.
A comparison Q_i->Q_j is a permutation g with g(i)=j. These form the action
groupoid S4 acting on four points:

- four objects;
- six witnesses for every ordered endpoint pair;
-96 current comparison payloads, of which72 change endpoints.

Composition is ordinary ordered permutation composition with matching middle
boundary. Inverses exist. Parent histories remain additional retained records;
two triple bracketings have equal composite payload and equal flattened leaf
word, but different parent trees. No history is erased by the groupoid equality.

These are counts in the finite witness model, not replacements for the137
comparison slots or physical degree-of-freedom counts.

## A minimal faithful witness coordinate

Choose root0 and frame permutations tau_i carrying0 to i. For an arrow g:i->j,
write

    h = tau_j^-1 g tau_i,
    g = tau_j h tau_i^-1.

Here h fixes0 and belongs to its six-element stabilizer S3. Retaining endpoints
and h reconstructs the full arrow. Composable arrows satisfy

    h_composite = h_second h_first.

An endpoint-only record loses six possible witness values. Full labelled-state
observations separate every pair in that fiber. In this finite representation,
a faithful endpoint-enriched record therefore needs six distinguishable witness
states per endpoint pair (or may simply store the original permutation).

Changing frames tau_i to tau_i u_i, with u_i fixing0, gives

    h_new = u_j^-1 h_old u_i.

This changes coordinates, not the recovered arrow. A based loop changes by
conjugation. Its nonidentity holonomy cannot become identity through this frame
change. Setting all h to identity instead selects a special flat section and
removes possible source witnesses; it is not generally a coordinate choice.

## What this resolves

We need not impose a universal flat/nonflat choice before using the comparison
constructor. Supply the source equivalence, retain its witness coordinate and
parents, and calculate the loop response of the actual route. A flat sector can
be recognized afterward if its loop data support that descent.

The remaining task is an adapter, not a new arbitrary connection: relate these
source endpoint types and supplied equivalences to the137-slot matrix response
model while preserving witness distinctions. That identification, a particular
filler assignment to all carrier edges, and the physical rung4 metric are not
established by this finite realization. S3 here is an isotropy group of a finite
comparison model, not an identified physical gauge symmetry.

## Verification

    python research/nima/checkers/check_retained_pointed_comparison_groupoid.py
    python research/aspect/scc/scc.py check nima-retained-pointed-comparison-groupoid

The checker audits constructor source fragments and hashes, enumerates all96
payloads and composable pairs, verifies inversion and witness reconstruction,
checks all single-port frame changes, separates endpoint fibers, and verifies
retained triple histories on a nonidentity loop. It is an exact finite source
realization, not a fresh Agda compilation.

Machine result: `research/nima/results/retained-pointed-comparison-groupoid.json`.
