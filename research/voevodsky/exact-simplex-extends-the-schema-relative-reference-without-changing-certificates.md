# Exact simplex extends the schema-relative reference without changing certificates

## Backend replacement

The schema-relative source-space reference now has an alternative exact rational simplex backend using SymPy. It retains the same box, observation schema, accumulated rational linear frames and expected-statement semantics as the exhaustive reference.

For optimization, it solves the primal source-space LP and a separate dual LP. Explicit lower-bound rows ensure the returned dual accounts for every source constraint rather than relying on implicit nonnegativity. For infeasibility, it solves for a normalized nonnegative Farkas combination with zero normal and upper bound -1. Joint point membership adds both orientations of each requested observable equality, then solves with zero objective.

The backend is a certificate proposer. Solver output is accepted only after the separate arithmetic verifier checks it against an independently constructed expected state/query. Exact arithmetic in a library is not treated as a substitute for verification.

## Results

44 certificates at m=3,4,8,16 pass independent verification. The 22 overlapping small cases agree with the exhaustive reference on feasibility and optimum values; selected witnesses need not agree. Pure schema extension preserves old objective values. Four attacks changing schema, query, source witness and dual weights are rejected.

The recorded producer workload took about 0.55 seconds in this run. This is a local finite-workload measurement, not a asymptotic or general performance bound. The workload includes simple cap/intersection geometries, lower-dimensional membership equalities and inconsistent states; it does not stress arbitrary dense audit histories.

An initial equality-only dual LP call encountered a library matrix-shape error. Adding the vacuous, correctly dimensioned inequality 0<=0 makes the dimensions explicit without changing the LP. The resulting primal and dual certificates were independently verified.

## Costs and scope

This removes exhaustive active-set enumeration from the proposal backend. It still materializes source-space rows and dual problems, including all atom caps and retained constraints. It does not project or store the visible-image facet table, but it is not the compact generator algorithm achieved for the two-observable special case.

The reference producer assumes well-formed research inputs. This is not a hardened public API, an authenticated observation service or integration into Nima's owning runtime. The independent verifier rejects optimized Python execution because it uses assertions. Upstream analytical source admission was not freshly replayed here.

The successful replacement establishes a useful modularity fact: a different solver can produce the same semantic certificates without altering the expected-history boundary or query interpretation. General exact rational LP theory supplies mathematical closure; the controls demonstrate this implementation on the declared workloads, not a formal proof of the solver library's behavior on every input.

## Reproduction

    uv run --with sympy python research/voevodsky/checkers/check_simplex_schema_tail.py
    python research/voevodsky/checkers/verify_simplex_schema_tail.py

The verifier uses only exact rational arithmetic and the independent reference verifier, not SymPy or the simplex producer. Reference comparison requires the prior `schema-relative-tail-lp.json` artifact.

Artifacts:

- `results/simplex-schema-tail.json`
- `results/simplex-schema-tail-verification.json`
