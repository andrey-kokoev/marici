# Machian metric from stabilizer Gram

## Core idea

Our 4-point carrier \(X = \text{Bool}\times\text{Bool}\) has automorphism group \(S_4\) (all permutations of the four points). The **stabilizer** of a point \(p\) is the subgroup \(\text{Stab}(p) \subset S_4\) that fixes \(p\). For the anchor point \((0,0)\), this is \(S_3\)—the 6 permutations of the three remaining points.

The **Gram matrix** of the stabilizer fillers at \(p\) IS the local relational geometry at \(p\). No external spatial metric is needed. The stabilizer action determines which directions at \(p\) are distinguishable, which are rotated into each other, and which are fixed.

## What the checker confirms

For the 4-point carrier:

- Automorphism group size: 24 = \(|S_4|\)
- Stabilizer of \((0,0)\): 6 = \(|S_3|\)
- The 6 stabilizer fillers act as all permutations of the remaining 3 points \(\{1,2,3\}\)
- Their Gram matrix (6×6) defines the inner product on the space of probe responses at the anchor point

## The Machian claim

For a larger carrier (finite lattice of \(N\) points), the stabilizer of a point approximates the Euclidean or Lorentz group as \(N \to \infty\). The Gram matrix of stabilizer fillers approaches the spatial metric tensor at that point. Specifically:

\[
g_{ab}(p) = \lim_{N\to\infty} \langle f_a | f_b \rangle_{\text{Stab}(p)}
\]

where \(f_a, f_b\) are stabilizer fillers that generate translations/rotations in directions \(a, b\).

The Einstein equations become consistency conditions on the stabilizer Gram across the carrier: the curvature of the "metric" \(g_{ab}(p)\) is determined by the failure of stabilizer Gram matrices at neighboring points to be isomorphic.

## What this changes

| Before | After |
|---|---|
| Space is a pre-existing manifold | Space is the stabilizer Gram at each point |
| Metric is a field on a manifold | Metric is the correlation of probe responses |
| Diffeomorphisms are maps between points | Diffeomorphisms are automorphisms of the carrier |
| Curvature = failure of parallel transport | Curvature = failure of stabilizer Gram compatibility |

## Signature resolved: Euclidean + connection = Lorentzian

The stabilizer Gram always gives Euclidean signature (+++). The temporal direction comes from the connection:

\[
g_{\text{spacetime}} = g_{\text{stabilizer}}^{(+++)} \oplus g_{\alpha}^{(-)}
\]

where \(d\alpha = -\Omega/\kappa\) contributes the \() factor via the symplectic curvature. 

| Component | Source | Signature |
|---|---|---|
| Spatial | Stabilizer Gram on carrier neighbors | +++ |
| Temporal | Connection curvature \(d\alpha = -\Omega/\kappa\) | − |
| Full | Combined | + + + − = Lorentzian |

No external Minkowski metric needed. The Lorentzian structure is the combination of two carrier-intrinsic objects: the stabilizer Gram and the connection.

## Verification

```text
python research/nima/checkers/check_machian_metric.py
```

Artifact: `results/machian-metric-test.json`.