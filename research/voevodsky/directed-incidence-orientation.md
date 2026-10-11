# Directed incidence determines triangle orientation: conditional construction test

## Proposed rule

Fix a spatial volume orientation Ω, and let d be the directed displacement between the new tetrahedron's body center and a face center. On that face define the alternating form

```text
β_d(u,v) = χ Ω(d,u,v).
```

χ is one fixed global sign. Orient each triangle so β_d evaluated on its ordered tangent edges is positive. Hold the source's cyclic character ω fixed.

This explicitly couples the direction of generation to cyclic orientation. It is a proposed construction law, not a theorem about an unoriented tetrahedron.

## Calibration against the actual source

The retained source's twelve oriented triangles have outward geometric normals. The source itself does not specify incoming radial generation.

If we assign the source the proposed incoming traversal, d points from face center to body center. Matching its existing triangle orientations fixes χ=-1 once, globally. The new outgoing traversal then uses the same χ and the same Ω, not a second calibration.

On every source triangle the exact pairing is:

| Traversal and triangle order | β value |
|---|---:|
| Incoming, source order | 4/3 |
| Outgoing, source order | -4/3 |
| Outgoing, reversed order | 4/3 |

Thus reversing d forces reversal of the triangle orientation **under this rule**. This uses the same spatial coordinates and does not rotate a camera or rename vertices.

## Cycle and coefficient consequences

For source coordinates X=(F,A,B), the reversed orientation uses X'=(F,B,A). If C is the original cyclic-coordinate operator, then

```text
X' C X'^(-1) = (X C X^(-1))^(-1).
```

With the same selected character ω:

```text
X' (1,ω,ω²) = conjugate[X (1,ω,ω²)].
```

The checker verifies both identities on all twelve source triangles. This connects directed incidence, cyclic inversion, and conjugated modes without separately instructing the coefficients to conjugate. It relies on the declared orientation coupling and the fixed character.

## Shared-edge consistency

The source surface and its globally reversed surface both have zero oriented boundary. Exhausting all 2^12=4096 choices of triangle signs gives exactly two coherent orientations: the original global orientation and its global reversal. No mixed choice is coherent.

Reversing only one triangle creates three shared-edge defects, each with signed multiplicity ±2. This is a concrete negative control, not an inserted glue object.

Refining the twelve triangles along their outer-edge midpoints gives the 24 boundary triangles of the flag construction. Both global orientations remain coherent. The refinement has 14 vertices, 36 edges, and 24 triangles. Its orientation-constraint graph is connected, so the shared-edge equations again fix every sign once one triangle's sign is chosen.

This refinement check concerns orientation consistency. It does not introduce 24 new independently selected coefficient modes in place of the source's twelve.

## Does outward growth force this rule?

No. A competing coherent rule orients triangles using the body's fixed outward normal, independently of traversal direction. Under that rule, radial arrows may reverse while triangle cycles remain unchanged. The checker verifies that this alternative satisfies the same shared-edge consistency condition.

Therefore:

- The proposed directed-incidence coupling **survives the consistency test**.
- It determines cyclic reversal once its global calibration and character are fixed.
- Outward generation and shared-edge consistency alone **do not select this coupling** over the fixed-boundary alternative.

The earlier demand that incidence geometry alone must force the coupling is not met. The coupling can instead remain an explicit conjectured law, whose consequences are to be tested without changing it between isotope cases.

## Consequence for the programme

We now have one explicit, internally consistent candidate rule for outward electron generation, including its cyclic coefficient action. It is not an isotope construction. The two coherent orientations are not automatically hydrogen and deuterium.

Its assembled return is the conjugate/transpose candidate already computed, so the previous rigid-attachment mismatch still applies. The next test requires an attachment law for the generated complex, not relabelling orientation defects as neutrons or automatically inserting the fitted phase map.

## Verification

```text
python research/voevodsky/checkers/check_directed_incidence_orientation.py
```

Fifteen exact checks pass. Artifact: `results/directed_incidence_orientation.json`, including the rule, calibration, all twelve pairing values, 4096-case orientation audit, negative-control edge defects, and source/checker hashes. The source remains unchanged.
