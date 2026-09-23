# A balanced-gain adapter preserves raw audits and retention policy

## Delivered adapter

The modular difference interface now has a separate balanced-positive-gain adapter. It certifies a shared chart, normalizes evidence and caps, delegates block composition to the existing engine, and converts query answers and witnesses back to raw atom coordinates.

Independent replay passes 11 states, 28 raw threshold answers, four raw source fillings and four archive-backed re-exposures. Seven certificate mutations are rejected. The original modular regression also passes.

## Chart admission is not source feasibility

A raw evidence row has the form

    x_v <= g*x_u + b,  g>0.

Gain rows connect non-anchor raw atoms; source bounds use the zero anchor separately. The adapter propagates positive rational scales satisfying s_v=g*s_u through the undirected gain graph, using reciprocal gains on reversed edges.

If two assignments conflict, it exports a closed walk whose signed gain product is not one. Independent verification checks the walk and product. The outcome is UNSUPPORTED with reason UNBALANCED_CHART, not INCONSISTENT.

Three deliberately unbalanced controls have independently checked feasible raw source witnesses. They demonstrate why a chart failure cannot be used as an emptiness certificate. A separate balanced example has a certified cross-block negative cycle and is genuinely INCONSISTENT.

## Exact normalization using the existing engine

Normalize each connected component so its minimum scale is one. Thus every scale is at least one, and z_v=x_v/s_v satisfies

    z_v-z_u <= b/s_v,
    0 <= z_v <= cap_v/s_v.

The unchanged difference engine supplies its ordinary ambient cap z_v<=cap_v. Because s_v>=1, that bound is redundant once the adapter adds the tighter cap_v/s_v row. The represented normalized source is therefore EXACTLY the scaled raw box, not a box with silently altered raw caps.

Both blocks inherit one global chart. Each transformed row, shared boundary mapping and normalized cap is independently checked. The normalized binding includes the digest of the raw expected state, including its retention policy and complete evidence.

A valid normalized source vector maps back by x_v=s_v*z_v. Conversely every admitted raw source maps into the normalized carrier. This is a change of representation, not a new observed value or a claim of unchanged conditioning under rescaled norms.

## Raw query semantics

Public membership divides the supplied raw coordinates by their certified scales before querying the difference summary. Fine fillings multiply the returned normalized source coordinates back by the same scales.

For a public raw atom v, the exact feasible interval is

    [-s_v*D(v,0), s_v*D(0,v)].

Shortest-path potentials attain both endpoints; the existing exact block-extension theorem supplies compatible source fillings. Raw threshold queries x_v<=h retain the caller's original h. Their three nonempty statuses follow the same weak-inequality rules as the precision interface. Compilation reports inconsistency before constructing a live query object.

The controls include nonunit integer scales and a fractional chart with scales 3/2, 5/3, 1 and 7/4. Requests are frozen as raw thresholds before compilation. A mutation replacing a requested raw threshold with a scaled one is rejected even if a status could coincidentally agree.

## Retention and re-exposure

Archive-backed adapters retain the raw fine specification and the normalized backend's fine specification. Re-exposure promotes the requested source nodes to boundaries and recompiles from the same raw evidence. It does not obtain missing audit values from a selected witness.

Public-only adapters retain no fine specification in either wrapper or backend. They support public membership and thresholds, but refuse hidden-coordinate exposure and fine filling. Six such continuation refusals are checked by the producer. Policy changes and changed expected histories are rejected by independent certificate verification.

The wrapper still retains its scale vector, including hidden-node scales. This is not a constant-size live representation claim. Nor is the API a confidentiality boundary: exported migration packets and experimental archives contain fine information. Unsupported continuation means this live object's contract does not promise it.

## Scope and costs

The shared chart and shortest-path proofs do not cover arbitrary moment rows, nonpositive gains or unbalanced general two-variable inequalities. Malformed inputs raise errors; unsupported chart structure and certified emptiness remain distinct outcomes.

The observed maximum scale numerator/denominator size is three bits in this workload. General rational gain products can be much larger. Scale storage, normalized evidence, duplicated archive specifications, migration proofs and arithmetic work remain separate from boundary-row counts. No accuracy equivalence under changed norms or total archive compression is claimed.

The independent checker imports the existing difference-proof verifier, not the chart constructor or closure algorithm. It checks chart equations, component normalization, scaled caps, raw inequalities, public thresholds, re-exposure statements and negative-cycle evidence. Source admission is inherited from the owning box; no fresh upstream admission proof or measurement authentication is supplied.

## Reproduction

    python research/nima/checkers/check_balanced_gain_adapter.py
    python research/nima/checkers/verify_balanced_gain_adapter.py

Implementation: `research/nima/checkers/balanced_gain_adapter.py`.

Artifacts: `research/nima/results/balanced-gain-adapter*`.
