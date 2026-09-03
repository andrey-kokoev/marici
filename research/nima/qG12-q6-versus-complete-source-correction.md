# `q_G12` `Q6` versus complete-source correction

## Question

Can the marked-relative `Q6` basis certificate be reconstructed as the quotient carrying the complete sewn physical source?

## Result

No. The proposed reconstruction conflated two distinct localization presentations.

The shared-three-wall presentation has the exact rank sequence

\[
0\longrightarrow M_9\longrightarrow M_{15}\longrightarrow Q_6\longrightarrow0,
\]

where the six quotient directions are the source-ordered wall increments `1+2+3`. This sequence proves liftability of the closed three-wall cocycle and identifies the rank-nine absolute ambiguity.

The literal unsplit source form, however, belongs to the complete five-pole post-residue complex retaining both occurrence divisors. Its deletion–restriction sequence has ranks

\[
0\longrightarrow M_{15}\longrightarrow M_{35}
\longrightarrow M_{20}\longrightarrow0.
\]

The complete source class is a canonical relative basepoint mapping to `rho_phys` in this rank-twenty localization fiber. Ledger Entry 658 explicitly prohibits substituting the `9→15→6` shared-wall ranks for the complete `15→35→20` source ranks.

## Consequence

A `Q6` basis certificate cannot by itself transport the literal physical source or prove lower-graph factorization. Projecting the complete five-pole class to the three-wall quotient would first require a typed forgetful/base-change map that removes the two occurrence divisors while preserving their unsplit sum, orientation, normalization, and Čech boundary.

No such map is supplied by the rank statements. The deletion–restriction split artifact records only the necessary Euler identity `35=15+20` and explicitly does not assert the derived base-change maps.

## First missing arrow

The first missing arrow is the source-labelled comparison

\[
F_{5\to3}:C_{\rm phys}^{(5\ pole)}\longrightarrow C_W^{(3\ wall)}
\]

or its induced cohomology map, together with a commuting square for the complete boundary `rho_phys`. Only after constructing this map can a six-dimensional wall quotient be used without discarding occurrence data.

## Strongest falsification attempt

Identify the rank-six tensor restriction with the complete physical residue quotient using equal or nearby ranks. This fails twice: the complete quotient has rank twenty, not six, and the tensor polynomial quotient has no typed map from the five-pole relative complex. Dimension matching was applied to the wrong object.

## Acceptance test

1. freeze source-labelled presentations for the rank-35 complete complex and rank-15 deletion complex;
2. expose the rank-20 quotient pivots and coordinates of the unsplit source;
3. construct the forgetful/base-change map to the shared-three-wall presentation;
4. verify that the two occurrence terms are combined before projection;
5. prove the boundary square commutes and retains all three oriented wall residues;
6. use a split occurrence term as a deliberate failure of source invariance.

## Disposition

The requested `Q6` reconstruction is rejected as the wrong interface for the complete physical source. The programme must first construct the rank-35 to rank-20 source presentation and its typed base change to the shared-wall complex.

## Evidence

- `src/ledger/20260818-658 The Literal Source Bases the Relative Lift but Not an Absolute T7 Projection.md`
- `src/ledger/20260818-650 The Physical Wall Cocycle Has No Canonical T7 Lift.md`
- `research/benincasa/deletion_restriction_base_change_split.json`
- `research/benincasa/source-bases-localization-fiber.json`
