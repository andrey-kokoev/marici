# WP148 — free-action topology-selector audit

## Bounded question

Can WP147's modulus-four admissibility condition be derived from source
geometry rather than inserted as a discrete selector parameter?

## Frozen source mechanism

Admit finite-CW-type source geometries \(X\) carrying a free action of a
finite group \(G\). For a free finite action, the quotient map is a
\(|G|\)-sheeted covering, so Euler characteristic is multiplicative:

\[
\chi(X)=|G|\chi(X/G).
\]

Freeze \(|G|=96\). With WP144's topology coordinate
\(k=\chi(X)/24\), this gives

\[
k=4\chi(X/G).
\]

On the admitted positive quotient-Euler domain
\(\chi(X/G)\in\mathbb N_{>0}\), the WP147 congruence is therefore a theorem:

\[
k\in4\mathbb N.
\]

The minimal quotient class \(\chi(X/G)=1\) produces \(k=4\), whose WP140
threshold is accessible. This is a source-geometric restriction of the
admissible topology domain, not a potential fitted to a desired integer.

## Exact cellular witness

Take quotient cell counts

\[
(c_0,c_1,c_2)=(5,7,3),
\qquad \chi(X/G)=5-7+3=1.
\]

A free order-96 lift has 96 copies of every cell, hence
\(\chi(X)=96\) and \(k=4\). The checker verifies the multiplication and the
resulting accessibility using integer and rational arithmetic only.

## Two hostile gates

### Group-order authority

The same theorem with a free group of order 24 yields

\[
k=\chi(X/G),
\]

so the same quotient witness gives inaccessible \(k=1\). Free-action geometry
derives the modulus from \(|G|\), but does not explain why the source group has
order 96 rather than 24.

### Freeness

The covering theorem fails for actions with stabilizers. Starting from the
order-96 free packet, add one positive even-dimensional orbit with stabilizer
order four. Its orbit has size \(96/4=24\), giving

\[
\chi(X)=96+24=120,
\qquad k=5.
\]

The topology coordinate remains integral but is no longer divisible by four.
Thus freeness is load-bearing and must be preserved across the entire admitted
source domain, not checked on one preferred geometry.

## Typing and classification

- **Admitted source domain:** positive-Euler finite-CW-type geometries with a
  free action of one frozen order-96 group.
- **Faithful flavor quotient:** `physical16`, reached through WP144's
  topology-to-flux-to-flavor map.
- **Source-authorized operation:** restriction to free \(G\)-geometries and
  quotient by the free action.
- **Contextual partition:** admitted free order-96 geometries versus rejected
  geometries; quotient Euler characteristic still labels a countable admitted
  family.
- **Selection:** proper topology-subspace selection. With the WP145 weight,
  the zero-temperature limit selects \(k=4\); finite temperature remains an
  accessible ensemble.
- **Separation:** the threshold predicate is constant on the admitted family
  and does not identify its members.
- **Rigidification:** none.
- **Descent:** Euler characteristic and covering degree are invariant under
  source presentation equivalence; the resulting flavor packet descends under
  full weak-basis equivalence.
- **Reference port:** unnecessary for the mathematical selector.
- **Physical instrument:** absent.

## Claim boundary

WP148 upgrades WP147's arithmetic projector to a conditional topological
theorem. It does **not** establish that flavor dynamics supplies an order-96
free symmetry, that the symmetry is anomaly-free, or that all admitted UV
deformations preserve freeness. Consequently it is not yet an unconditional
flavor selector.

## Smallest exact falsifiers

1. Free order 24 with \(\chi(X/G)=1\) gives inaccessible \(k=1\).
2. Order 96 with one stabilizer-four orbit gives \(k=5\), violating the
   modulus-four conclusion.

Either witness blocks promotion if group order or freeness is not independently
authorized.

## Reopening condition

Derive a particular order-96 group action from the declared UV flavor source,
prove that it acts freely and anomaly-freely on the complete admitted geometry
family, and show that allowed deformations cannot enter a fixed-point stratum.
Only then can the derived congruence carry unconditional selector authority.
The physical detector gate remains separate.

## Verification

```text
python research/flavor/checkers/wp148_free_action_topology_selector.py
```

The dependency-free checker writes the generated JSON and requires 12/12
exact checks.

## Process calibration

Pre-objective: excitement 9/10, confidence 9/10, expected information gain
9/10. The immediate reason was that covering-space multiplicativity provides
a real structural derivation of a congruence. Confounds were the unproved
physical origin of the group and stability of freeness.

Frozen optionality snapshot: one free order-96 branch, one free order-24
hostile branch, one non-free order-96 hostile branch, 12 checks, one quotient
map, and no physical instrument.

Post-objective: excitement 9/10, confidence 10/10 in the conditional theorem,
realized information gain 9/10. The modulus-four relation is now derived from
a covering degree rather than postulated. Two assumptions became explicit and
independently falsifiable: group order and freeness. The non-free branch was
retyped as outside the covering theorem, not silently absorbed. No physical
group origin, anomaly proof, open-domain freeness theorem, or instrument was
constructed.

