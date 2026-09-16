# Automated analytical frontier census

The executable frontier scanner is

```text
python research/voevodsky/checkers/check_coherence_pyramid_analytical_frontier.py
```

It joins:

- the computad signature;
- declared cells and coherence laws;
- overlay global status;
- the explicit analytical-realization registry;
- the certificate dependency DAG and current certificate state.

Its materialized report is

```text
research/voevodsky/results/coherence-pyramid-analytical-frontier.json
```

## Conservative realization rule

A generator is analytically realized only when

```json
{
  "kind": "edge | face | law",
  "id": "exact declared generator name",
  "status": "realized",
  "source": "path to evidence"
}
```

appears in `coherence-pyramid-analytical-realization-registry.json`.

A theorem elsewhere in the repository is not silently promoted. It is reported as `realized_unlinked` until a typed linkage to a declared computad generator is supplied.

## Output classes

The report lists:

- every declared edge and its source/target sorts;
- every declared face, boundary, and required law;
- every coherence law;
- realization status and evidence path;
- minimal missing-certificate antichains;
- analytically realized fragments not linked to the global computad.

## Current census

The current global signature has four edges, six faces, and five law classes. None has an explicit global analytical-realization linkage. Two substantial analytic fragments are detected but deliberately left unpromoted:

1. the verified analytic Markov equipment fragment;
2. the relative semilocal `C_34` sewing feature.

This does not say those analyses are absent. It says the repository currently lacks typed records identifying them with individual global computad generators.

## Claim boundary

The scanner is complete relative to the declared JSON signature and registry. It cannot discover an undeclared edge from prose, decide a theorem, or infer that two differently named carriers are equivalent. Those actions require a source-derived linkage record and its own checker.
