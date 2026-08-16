# Pair-Only Triple Coherence No-Go and the Oriented Top Gate

## Record

Date: 2026-08-15

Status: definitive scoped no-go for triple coherence in the finite
extraordinary category containing the six pair objects \(W_{ij}\) but no
triple/top object. This is not a no-go for a further enlargement by an
oriented triple correspondence. No graph admission is claimed.

## Exact obstruction

After identifying opposite orientations, the three pair objects form the
cyclic incidence complex
\[
\mathbf Z^3\xrightarrow{R-I}\mathbf Z^3.
\]
The boundary matrix has rank two and Smith form
\[
\operatorname{diag}(1,1,0).
\]
Its kernel is generated primitively by the norm
\[
N=(1,1,1).
\]

The pair-only category has no degree-two triple column whose boundary is
\(N\). Hence \(N\) is a nonzero free homology class, not a boundary. This is
the earliest failure of the attempted three-pair assembly. It precedes any
choice of a generic \(Q\) value or endpoint connector.

Tensoring the four Boolean normal states and the two conductor Tor spectator
grades does not change the differential in the pair direction. It therefore
replicates the free obstruction in eight grades. There is no integer torsion:
the obstruction is \(\mathbf Z^8\), not a hidden factor 2 or 3.

The \(D_3\) rotation fixes \(N\). Reflection reverses cyclic pair orientation,
so any filling top must carry the corresponding orientation sign. Symmetry
does not manufacture a missing boundary column.

## Minimal additional datum

The smallest saturated repair is one oriented triple object \(W_{012}\) in
each Boolean/Tor grade with
\[
dW_{012}=W_{01}+W_{12}+W_{20}.
\]
The new column is primitive, so its only Smith factor is 1. It must also carry
a normalization-provenanced comparison
\[
W_{012}\longrightarrow H_\Sigma,\qquad
dH_\Sigma=q_\Sigma-\sum_D x_D\widetilde\xi_D,
\]
and its three boundary restrictions must equal the adjacent-pair BC maps from
entry221. Merely adjoining the column algebraically would stipulate the
generic top; the geometric/top comparison must be independently constructed.

Until this top object and comparison exist, the endpoint/\(Q\) mapping fiber
cannot be instantiated, so \(p_{\partial,Q}\), its Bockstein, and the loaded
\(D_8\)/Jordan tests remain undefined.

## Executable evidence

Checker:
\`research/voevodsky/check_dp6_pair_only_triple_coherence_no_go.rs\`

SHA-256:
\`d35c2882456427de958815240eb9b167ff00a6c0f73a92fcb8cf7d0e6cff97a0\`

Fresh rustfmt, warnings-denied optimized compilation, runtime assertions, and
JSON output passed. Native PowerShell was used only because structured-command
MCP was not exposed in this session.

## Outcome contract

~~~json
{
  "claim": "The three extraordinary pair objects alone do not admit triple coherence: their cyclic boundary R-I has primitive kernel N=(1,1,1), and no top column is present to bound it.",
  "status": "falsified_scoped_pair_only_triple_coherence",
  "scope": "finite extraordinary category with W_ij pair objects and no oriented triple/top object",
  "matrix": {
    "boundary": "R-I",
    "rank": 2,
    "smith": [1,1,0],
    "kernel_generator": [1,1,1],
    "torsion": false
  },
  "graded_obstruction": {
    "boolean_states": 4,
    "tor_grades": [0,1],
    "free_rank": 8
  },
  "minimal_additional_datum": "An oriented triple object W_012 with primitive norm boundary in every Boolean/Tor grade and a normalization-provenanced map to H_Sigma/q_Sigma compatible with all three pair BC maps.",
  "downstream": {
    "endpoint_Q_mapping_fiber": "undefined",
    "p_partial_Q": "undefined",
    "Bockstein": "undefined",
    "D8_Jordan": "undefined"
  },
  "checker": "research/voevodsky/check_dp6_pair_only_triple_coherence_no_go.rs",
  "checker_sha256": "d35c2882456427de958815240eb9b167ff00a6c0f73a92fcb8cf7d0e6cff97a0"
}
~~~
