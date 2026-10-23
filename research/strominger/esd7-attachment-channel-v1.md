# Source-generated esd7 attachment channel

## Result

The [new producer and incremental assembler](checkers/esd7_attachment_channel.py) construct the **complete geometric esd7 complex** without loading its census:

-120 vertices,560 edges,784 triangles and343 tetrahedra;
-stable shared references and signed simplex boundaries;
-all588 interior faces cancel in the oriented total boundary;
-the196 exterior faces remain;
-boundary squared vanishes on every cell.

The separately loaded census agrees with every generated labelled cell and its incidence. This is a geometric construction result, **not yet the proposed114-record channel or the full analytical/field realization**.

## Actual attachment grammar

The source rule is the existing ordered-chamber Freudenthal construction in `research/voevodsky/checkers/check_esd7_explicit_analytical_census.py`:

    0 <= z1 <= z2 <= z3 <= R
    barycentric = (z1, z2-z1, z3-z2, R-z3).

An attachment supplies an integer base point, an ordering of the three coordinate increments and a unique occurrence ID. The decoder derives the four vertices, interns every vertex/edge/face/tetrahedron, computes orientation, and checks shared-face cancellation. The producer enumerates admissible placements from the rule, not from an existing cell list. Closing requires exactly the placements admitted by that rule.

At R=7 this gives **345 records: one opening,343 attachments, one closing**. The same implementation is tested at R=1,2,3,4. This is not a343-entry stored schedule and not a claim about physical time. These geometric `attach` records are not being invented as new verified PN/NE particle operations.

All lower-dimensional cells are shared by coordinate identity. Distinct construction occurrences remain in the ordered log. Reversing attachment order preserves the full labelled complex while changing that log. Prefixes expose their current faces; unfinished prefixes are not claimed to be complete coherence objects.

## Native regression binding

All five physical bodies of the [previous native channel](native-retained-channel-v1.md) embed in generated tetrahedra using the already source-bound affine embedding `x -> 2-x`. Every physical interface in that fixture embeds in a generated shared face. No census lookup is used for this binding: the lookup is against the independently generated output.

The previous native channel and its44-channel sewing equations remain a separate regression. Embedding those five bodies does **not** extend their field equations to every generated tetrahedron.

## Coherence is retained as an obligation, not asserted

Each triangle references a composite of two shared edge maps and a direct edge map with matching endpoints. Each tetrahedron references its four shared face-homotopy obligations and the typed tetrahedral comparison

    H_ACD (d_CD * H_ABC) = H_ABD (H_BCD * d_AB).

These are the required slots and equation, **not supplied analytical maps or a checked filler**. All784 face homotopies and343 tetrahedral coherence obligations remain explicitly undischarged. Signed boundary cancellation is not a substitute for these equations.

## Checks and reproduction

```sh
node research/strominger/checkers/check_native_retained_channel.mjs
python research/strominger/checkers/check_esd7_attachment_channel.py
```

[Verification receipt](results/esd7-attachment-channel-verification.json):25 checks, including independent labelled census comparison, shared signed incidence, native embedding, arbitrary attachment order, smaller scales, and rejection of malformed axes, out-of-chamber cells, duplicate occurrences/cells, missing attachments, completed-target injection and incomplete closure. A failed decoder cannot resume.

Artifacts:

- [Generated channel](results/esd7-geometric-attachment-channel.json).
- [Generated complex, prefixes and pending coherence obligations](results/esd7-channel-generated-assembly.json).

The target census is read only by the checker after construction. The pure producer/decoder module performs no file I/O. The previous native fixture is also only a checker input.

## Remaining frontier

The esd7 attachment construction task remains open, with this geometric substep recorded as conditionally verified:

1. Identify a source-backed114-record producer/attachment convention, or a precise obstruction to that proposal. Truncating this345-record stream fails, but that does not refute a different114-record grammar. Grouping records solely to reach a desired count is not a construction.
2. Bind the retained analytical face and tetrahedral witnesses, rather than merely their incidence slots.
3. Extend the native field/readout transport to the resulting full complex and test all interfaces.
4. Only then test whether the assembler's updates realize the proposed evolution.
