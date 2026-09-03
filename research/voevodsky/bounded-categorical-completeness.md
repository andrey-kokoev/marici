# Bounded categorical completeness

## Question

When may the coherence-pyramid apparatus be called complete without promoting a restricted model into a global theorem?

## Claim boundary

Completeness is parameterized. This packet does not define an absolute or unbounded completeness claim.

## Parameters

A certificate must state:

- domain;
- object sorts;
- cell classes;
- law classes;
- simplicial truncation degree;
- certificate backend;
- completion scope;
- physical scope.

Without these parameters, `complete` has no stable mathematical meaning.

## Gate families

Seven gate families are required: presentation, realization, horn coverage, filler semantics, completion, cross-sector overlap, and physical readout. Gates excluded by scope must be stated as excluded rather than silently counted as passed.

## Current classification

The metric-transition Markov realization is complete through simplicial degree 4 for the declared five sorts, six cell classes, and five law classes. Its physical scope is excluded.

Cross-sector completeness fails at dimension 1 because no overlap edge is admitted. Higher cross-sector and mixed horn claims are undefined.

The RH filler is algebraically present as a relative class, but completed selection is incomplete because the cutoff system, graph topology, and coherent natural contraction are absent.

No global unbounded completeness claim is made.

## Nonimplications

The checker freezes six nonimplications, including:

- finite truncation does not imply unbounded coherence;
- relative class does not imply selected representative;
- algebraic filling does not imply completed descent;
- mathematical coherence does not imply physical readout.

## Disposition

The categorical machinery now has a machine-checkable completeness predicate. It certifies the bounded Markov statement and rejects global, cross-sector, RH-completed, and physical promotions at their first missing gates.

## Verification

- `research/voevodsky/bounded-categorical-completeness-contract-v1.json`
- `research/voevodsky/checkers/check_bounded_categorical_completeness.py`
- `research/voevodsky/results/bounded_categorical_completeness.json`
