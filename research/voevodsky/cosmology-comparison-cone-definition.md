# Comparison-cone definition

## Question

Is `(Xi_log,-sigma123)` exact after defining the correct top-weight comparison object?

## Claim boundary

Let `A_log` be the weight-four, total-degree-two logarithmic residue complex of the three-line pair, and let `B_flag` be the shifted cellular flag complex of the boundary triangle. Ordered iterated residue defines

`Res:A_log -> B_flag`.

The orientation audit proves `Res([Xi_log])=[sigma123]` with coefficient one. Their minimal models are each `Z` concentrated in total degree two, and `Res` is the identity. Its standard comparison cone is therefore acyclic.

Equivalently, the cone formally adjoins a degree-one comparison cell `tau` with

`d tau=(Xi_log,-sigma123)`.

This establishes abstract pair exactness in the top-weight comparison cone. It does not source `tau`. The cell belongs to the cone constructor; treating its formal existence as a rank-26, higher-Chow, or physical horn repeats the abstract insertion that the programme forbids.

A zero comparison provides the deliberate failure: its cone retains two nonzero classes. The unit residue map is exactly what makes the actual comparison cone acyclic.

## Disposition

The pair is formally exact in the comparison cone. The remaining scientific question is whether an admitted degree-one source maps to the formal cell. The next leaf tests rank-26, motivic, and relative source lifts without treating cone existence as authority.

## Verification

- `research/voevodsky/check_cosmology_comparison_cone_definition.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
