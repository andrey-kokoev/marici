# `q_G12` soft normalization authority audit

## Question

Does the current source packet define an epsilon or conductor normalization with an `X1`-soft weight that can compare the grade `-2` `q_g2` class with the grade `-1` `q_g1` and `q_g3` classes?

## Source audit

The exact sewn source is

\[
\frac{da\wedge db}{\sqrt{K_E}\,q_{g1}q_{g2}q_{g3}}
\left(\frac1{q_{g23}}+\frac1{q_{g31}}\right).
\]

`research/benincasa/physical-g12-shared-wall-residues.json` explicitly records `normalization/conductor reduction of each wall one-form and their Cech sum` as the remaining test and sets `cohomological_nonvanishing_inferred` to false. It provides no epsilon factor, conductor normalization map, or normal Jacobian.

The source-reachable quotient result at `research/benincasa/results/source-reachable-relation-quotient-hilbert-g12-k4-p32009.json`, lines 839–840, sets both `normalized_quotient_occurrence_coefficients` and `normalized_quotient_k_coefficients` to null. It also reports that relation reduction does not preserve the combined grade.

Repository occurrences of epsilon in the Benincasa sector describe analytic regulator chamber substitutions such as `E -> E-i epsilon_E`. Those prescriptions select boundary-value chambers; they do not define a multiplicative `x`-weighted normalization of the sewn wall forms.

## First missing typed object

The first missing object is a source-authorized map

\[
N_{\epsilon}:\operatorname{Gr}^{W}_{-2}(\Omega_{q_{g2}})
\longrightarrow
\operatorname{Gr}^{W}_{-1}(\Omega_{\rm sewn}),
\]

together with its `x`-weight, normal Jacobian, branch convention, and compatibility with the `q_g1`–`q_g2` node. No existing result constructs this map.

## Failed consequence

Without `N_epsilon`, the grade `-2` residue cannot be compared or added to grade `-1` residues. Multiplication by `x` would produce the desired grade shift, but choosing that factor from the target grade would insert the conclusion rather than derive it.

## Acceptance test

A valid normalization packet must:

1. derive the factor from the parent integral, action, or regulated chain;
2. state its exact `x` valuation and coefficient;
3. include the normal-coordinate Jacobian on all three wall occurrences;
4. preserve the unsplit occurrence labels through the map;
5. reproduce the established `q_g1`–`q_g3` opposite residue match;
6. predict the normalized `q_g1`–`q_g2` node residues before inspecting them;
7. fail explicitly if the regulator chamber changes the proposed coefficient.

## Disposition

No source-derived epsilon/conductor grade-changing normalization is present. The algebraic grades `(-1,-2,-1)` and the nonzero `q_g2` logarithmic class remain the strongest authorized result. This branch is blocked at the missing map above; further coefficient fitting is prohibited until a source packet supplies it.

## Evidence

- `research/benincasa/physical-g12-shared-wall-residues.json`
- `research/benincasa/physical_g12_conductor_obstruction.py`
- `research/benincasa/results/source-reachable-relation-quotient-hilbert-g12-k4-p32009.json`
- `research/nima/qG12-unsplit-leading-wall-log-sum.md`
