# `q_G12` independent lower-graph object audit

## Question

Is there a source-derived, independently normalized lower-graph object for comparison with each sewn shared-wall residue `rho_i`?

## Search result

The frozen artifacts define the upper object and its wall data:

- the unsplit five-pole source form;
- the `q_G12` Poincaré residue;
- oriented residues on `q_g1`, `q_g2`, and `q_g3`;
- exact Čech closure;
- reduced Cayley–Menger factors and analytic conductor normalization.

No independent lower-graph artifact was found. In particular, no file or ledger claim declares, for any `q_gi`, all of:

1. a graph contraction/deletion operation producing a lower graph;
2. its source denominator set and occurrence labels;
3. its integration measure and orientation;
4. its own Cayley–Menger square-root branch;
5. its source normalization;
6. a comparison map from the upper wall class.

The available `tensor-marked-wall-localization` object is an interaction numerator quotient at `q_G12`, not a lower-graph wavefunction coefficient. The wall cocycle itself is a relative boundary class and cannot serve as its own independently normalized target.

## Typing consequence

A rational identity between an upper residue and a proposed lower expression would be circular if the lower expression is defined by taking that residue. Physical factorization requires the target to be constructed from lower-graph source data first, followed by a separately proved comparison arrow.

The label “lower graph” is itself underdetermined here. A shared wall may encode a graph contraction, a deletion face, a cut object, or a product of source components. These alternatives generally have different denominator sets, measures, orientations, and normalizations.

## First missing object

The first missing object is a source-level graph morphism

\[
\kappa_i:G_{12}\longrightarrow G_i^{\rm lower}
\]

for each wall, together with a constructor `Omega(G_i^lower)` independent of the upper residue. Only then can one define and test

\[
N_i(\rho_i)=\Omega(G_i^{\rm lower})
\]

with a noncircular normalization map `N_i`.

## Strongest falsification attempt

Treat the nonzero rational wall numerator as the lower-graph object. This reproduces the upper residue tautologically but fails independence: it supplies no lower graph, source measure, square-root branch, or normalization. It therefore proves only wall localization, not factorization.

## Acceptance test

For each `q_gi`:

1. declare the source graph operation and resulting labelled graph;
2. construct its form without using the upper residue;
3. freeze orientation, measure, occurrence sum, and square-root branch;
4. normalize from its own source integral;
5. compare with the conductor-reduced upper wall class;
6. alter one lower-graph orientation or normalization as a deliberate failure.

## Disposition

No independently normalized lower-graph source object is currently materialized. The physical factorization comparison is blocked before cohomological matching, at the missing graph morphism and lower-source constructor.

## Evidence

- `research/nima/qG12-sewn-residue-factorization-square.md`
- `research/benincasa/physical-g12-shared-wall-residues.json`
- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`
- `research/benincasa/tensor-marked-wall-localization.json`
