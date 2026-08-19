# 880 — The Adjacent Five-Point String Pairing Requires Half-Monodromy

## Record

Date: 2026-08-18

Status: exact one-entry off-diagonal twisted-cycle factorization test. This extends Entry 879 from a chamber self-intersection to two distinct adjacent five-point chambers.

## Frozen comparison

Use the source twisted cycles

\[
\widetilde{\mathsf C}(12345),
\qquad
\widetilde{\mathsf C}(13245).
\]

They share exactly the facet \((23)\). The induced four-point boundary has endpoint channels \((45)\) and \((51)\).

The source loading across the common facet contributes

\[
\frac{q_{23}^{1/2}}{q_{23}-1}
=
-\frac{i}{2\sin(\pi s_{23})},
\qquad
q_{23}=e^{2\pi i s_{23}}.
\]

The boundary self-intersection contributes

\[
\frac{i}{2}
\left(
\frac1{\tan(\pi s_{45})}
+
\frac1{\tan(\pi s_{51})}
\right).
\]

Multiplication gives

\[
\boxed{
\frac1{4\sin(\pi s_{23})}
\left(
\frac1{\tan(\pi s_{45})}
+
\frac1{\tan(\pi s_{51})}
\right)
}
\]

which equals the source expression

\[
-\left(\frac{i}{2}\right)^2
\frac1{\sin(\pi s_{23})}
\left(
\frac1{\tan(\pi s_{45})}
+
\frac1{\tan(\pi s_{51})}
\right).
\]

## Interpretation

The shared facet and its product boundary determine the carrier part. They do not determine the answer alone. The off-diagonal pairing also requires:

1. the Koba--Nielsen square-root transport \(q_{23}^{1/2}\);
2. the induced orientation of the shared facet;
3. the four-point twisted self-intersection on that facet.

Thus the surviving architecture is more precise than “shared associahedron”:

\[
\boxed{
\text{shared face/Gysin carrier calculus}
+
\text{string-specific branch transport and twisted pairing}.
}
\]

No new carrier incidence generator is needed for this adjacent entry. But the coefficient object is indispensable and cannot be reconstructed from the carrier alone.

## Epistemic boundary

Established:

- exact shared-facet reduction for one adjacent pair;
- source half-monodromy and orientation normalization;
- exact agreement with the primary five-point formula.

Not established:

- the full \(2\times2\) five-point basis matrix;
- basis-change/circuit identities;
- nonadjacent vanishing from the same compiled complex;
- all-arity string KLT assembly.

## Next falsifier

Compile a complete two-cycle basis packet at five points and require simultaneously:

- both diagonal entries from face self-intersections;
- the adjacent off-diagonal entries from shared-facet reductions;
- zero for a nonadjacent chamber pair;
- invertibility away from the declared resonance divisors;
- the correct \(\alpha'\to0\) biadjoint limit.

Only that matrix-level closure should update the conjecture beyond the present representative test.

## Certificate

Run:

```text
cargo run --quiet --bin string_five_point_adjacent_intersection
```

Artifacts:

- `research/benincasa/marici-gm/src/bin/string_five_point_adjacent_intersection.rs`
- `research/benincasa/string-five-point-adjacent-intersection.json`

## Source

Sebastian Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*, arXiv:1706.08527, Section 4.3, pp. 28--29.
