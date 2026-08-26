# Optical stabilized behavioral congruence

## Question

When may two optical preparations or instrument histories be identified, and what evidence is required when a protocol gains new downstream analyzers?

## Finite presentation

Use five physical polarization continuations: horizontal, vertical, diagonal, antidiagonal, and an extinguished state. Include two presentation labels for the same diagonal continuation. The authorized future contexts are ideal analyzers in the four live polarization directions.

The immediate protocol reports only whether a continuation is live. It therefore identifies all four live rays. Partition refinement repeatedly records, for every authorized analyzer, both the transmission probability and the successor behavioral class.

The stable partition separates the four physical rays, retains the extinguished state, and continues to identify the two duplicate diagonal presentations. It is the greatest equivalence compatible with both readout and every authorized future analyzer.

## Equal scalar hostile

Two reciprocal selective words applied to a maximally mixed input have equal total probability one quarter:

- horizontal then diagonal leaves a diagonal continuation;
- diagonal then horizontal leaves a horizontal continuation.

A downstream horizontal analyzer assigns conditional probabilities one half and one. The old scalar class therefore splits under the refined protocol.

## Canonical downgrade, no canonical upgrade

Every stable behavioral class maps canonically to its old coarse live-or-dead class by forgetting analyzer responses. The reverse direction is not canonical: the old live class contains four distinct stable classes.

The same obstruction appears at instrument level. A scalar action with total probability one quarter admits at least two positive continuation lifts, one preparing the horizontal ray and one preparing the diagonal ray. Both reproduce the old scalar law; the downstream analyzer separates them. Extra source or calibration data must select a lift.

## Preservation gate

An old labelled operation can migrate to the refined protocol only if it preserves refined equivalence. The checker includes two duplicate diagonal presentations. A lawful operation sends both to the same successor class. A hostile label-dependent operation sends them to horizontal and vertical successors while preserving the old live scalar output. It fails to descend through the stabilized quotient.

Thus a commuting downgrade square and matching old statistics are not sufficient. Migration requires both:

1. preservation of the refined behavioral congruence;
2. source evidence selecting a continuation lift when the old scalar action is underdetermined.

## Relation to the shared frontier

This is an optical realization of Nima's stabilized-congruence criterion and Sontag's contextual source-task equivalence. It adds a physical distinction between coarse detector statistics and downstream polarization capability.

## Claim boundary

This is a finite exact theorem for ideal polarization rays and projective analyzers. It does not prove stabilization for continuous state spaces, noisy instruments, infinite context families, or completion limits. Duplicate presentation labels are a finite gauge witness, not a claim about microscopic identity.

## Verification

Run:

```text
python research/aspect/checkers/check_optical_stabilized_behavioral_congruence.py
```

The checker is dependency-free and uses exact rational probabilities and matrices.
