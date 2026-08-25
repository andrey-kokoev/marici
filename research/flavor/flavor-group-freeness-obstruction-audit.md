# WP149 — natural flavor-group freeness obstruction

## Bounded question

Does the canonical three-generation flavor presentation grammar naturally
supply WP148's required free order-96 source action?

## Frozen group and action

Three labelled generation coordinates admit signed permutations

\[
B_3=(\mathbb Z_2)^3\rtimes S_3,
\qquad |B_3|=2^3 3!=48.
\]

Adjoin one independent CP involution:

\[
G=B_3\times\mathbb Z_2^{\rm CP},
\qquad |G|=96.
\]

The action is frozen to the canonical linear action on \(\mathbb C^3\): signed
coordinate permutations, with CP acting by complex conjugation. This derives
the desired group order from a recognizable flavor presentation grammar
without fitting the number 96 in an energy functional.

## Exact result: the action is not free

Three independent fixed strata occur.

1. The nonidentity transposition \((12)\) fixes every vector with
   \(z_1=z_2\), including \((1,1,2)\).
2. A sign flip in the third coordinate fixes every vector with \(z_3=0\),
   including \((1,2,0)\).
3. CP fixes the entire real locus, including \((1,2,3)\).

A generic complex vector such as
\(((1+i),(2+3i),(4+5i))\) has trivial stabilizer in the exact enumeration, but
generic freeness is insufficient. WP148 requires a free action throughout the
admitted source domain so that \(X\to X/G\) is a covering. One fixed point is
enough to invalidate the Euler-multiplication theorem globally.

## Consequence for selection

The natural flavor grammar explains the arithmetic count \(96\), but it does
not derive the covering condition. On the canonical domain it is a
presentation symmetry with fixed strata, not a topology admissibility
selector. Therefore

\[
|G|=96\quad\not\Rightarrow\quad
\chi(X)=96\chi(X/G).
\]

WP148 cannot be promoted using group order alone. Orbifold Euler
characteristics or fixed-point corrections would define a different source
map and must be derived explicitly; they cannot be silently substituted for
ordinary covering multiplicativity.

## Typing

- **Admitted state domain:** the full canonical linear three-generation
  coordinate space \(\mathbb C^3\), including collision, zero-coordinate, and
  real strata.
- **Faithful quotient coordinate:** downstream flavor claims remain typed in
  `physical16`; this audit acts upstream on source geometry.
- **Source-authorized operation:** signed permutations and CP.
- **Contextual partition:** orbit types distinguished by stabilizer subgroup;
  the regular stratum and three exhibited singular strata are inequivalent.
- **Separation:** stabilizer probes distinguish strata mathematically, but no
  physical instrument is declared.
- **Selection:** none. The action does not restrict the source to a proper free
  subdomain.
- **Rigidification:** presentation symmetry only.
- **Descent:** the group action is well-defined, but the WP148 covering map
  does not descend over fixed strata as a free quotient.
- **Reference port:** removing or resolving fixed strata would change the
  source groupoid and must be stated as a new experiment.
- **Physical instrument:** absent.

## Smallest exact falsifier

The single equality

\[
(12)\cdot(1,1,2)=(1,1,2)
\]

exhibits a nonidentity stabilizer and falsifies freeness.

## Reopening condition

Construct an independently motivated source manifold on which this same
order-96 group acts freely, or derive the complete fixed-point correction and
show that it still forces \(k\in4\mathbb N\). Deleting fixed loci by fiat is
not admissible: the deletion must be source-generated, dynamically stable,
and its effect on Euler characteristic and the `physical16` pushforward must
be recomputed.

## Verification

```text
python research/flavor/checkers/wp149_flavor_group_freeness_obstruction.py
```

The dependency-free enumeration writes the generated JSON and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 9/10, confidence 9/10 that the order count would
succeed while freeness failed, expected information gain 9/10. The confound
was restriction to the canonical linear realization of the abstract group.

Frozen optionality snapshot: one signed-permutation-plus-CP action, three
fixed-stratum witnesses, one regular complex witness, 12 checks, and no
physical instrument.

Post-objective: excitement 9/10, confidence 10/10 in the bounded obstruction,
realized information gain 9/10. The group-order branch survives; the free-
covering interpretation is eliminated on the full canonical domain; three
stabilizer classes are exposed; and no source-authorized deletion, resolution,
orbifold correction, or instrument was constructed.

