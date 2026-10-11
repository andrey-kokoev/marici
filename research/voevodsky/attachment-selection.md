# Selecting within the full attachment relation

## One explicit rule

Test the least-displacement rule

```text
minimize E = ||x_host-F_ABC||² + ||x_electron||²
```

at fixed shared coefficient value u, over the full compatible square 0<=a,b<=m, where m=min(u).

The metric is the existing Euclidean tetrahedral geometry. This is an additional variational candidate, not dynamics already encoded by the coefficient arrows. No isotope-dependent term, fitted constant, or double-well potential is introduced. The retained complex is not pruned when a configuration is selected.

## Exact solution

Let n=(1,1,-1) and w=sum(u_i POINTS[i])-n/3 for i=A,B,C. Then w is perpendicular to n. The host displacement is w-a n. After the orthogonal A/B reflection, the electron displacement is w+(1/3-4b)n. Hence

```text
E = 2||w||² + 3a² + 3(1/3-4b)².
```

The unique minimum is

```text
a*=0,
b*=min(m,1/12).
```

The number 1/12 follows from the barycentric coordinate normalization and the position of the electron barycenter. It is not fitted to a particle measurement.

The exact certificate is

```text
E(a,b)-E(0,b*)
 = 3a² + 48(b-b*)² + 96(b*-1/12)(b-b*) >= 0.
```

If b*=1/12 the last term vanishes. If b*=m<1/12, both factors in the last product are nonpositive. Equality requires a=0 and b=b*. The fiber Hessian is diag(6,96), so there is no other local minimum either.

Every positive weighting of the two squared displacements leaves these independent fiber minima unchanged. A second stable state cannot be obtained by merely retuning their relative positive weights.

## What is selected?

For each prescribed u there is one selected pair. Across the coefficient triangle these form one continuous section, a disk. The clamped and unclamped formula branches are regions of that same section, not competing states at the same readout.

At u=(1/3,1/3,1/3), the selected pair is precisely (host F_ABC, electron barycenter).

If u is also allowed to minimize, that root pair is the unique global minimum: its cost is zero, and a sum of the two squared displacements vanishes only there. This selects a focus point; it does not shrink or delete the retained tetrahedral complexes.

Thus this rule provides neither two isotope states nor a nonzero-size physical ground-state distribution.

## Relation to the source operator

A function of the matched coefficient readout alone is constant along each compatible square. It cannot distinguish its retained kernel coordinates. The least-displacement cost adds such a distinction by using full geometric positions rather than only their readouts.

This isolates the missing ingredient: a selector must act on the retained information that the coefficient map forgets. The simple convex geometric selector does act there, but selects only one minimum. Producing two stable closures requires an independently motivated operation beyond both coefficient equality and this convex cost; calling one of the existing coordinates a neutron does not supply it.

## Verification

```text
python research/voevodsky/checkers/check_attachment_selection.py
```

Twelve exact checks pass, including 325 coefficient values, the nonnegative difference identity, both clamping regimes, replay of stored cell projections, the marked pair, and a feasible decreasing projected-gradient step. The gradient step is an optimization check, not an asserted time evolution.

Artifact: `results/attachment_selection.json`. The original coefficient source and retained cell inventory are unchanged.
