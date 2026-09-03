# External boundary-condition contract

## Question

What additional data would legitimately promote the K2 period from a mathematical invariant to a physical readout?

## Claim boundary

A valid instantiation requires nine typed fields:

1. a physical kinematic or configuration object `P`;
2. a source-derived map `P -> U(C)`;
3. a selected closed oriented two-cycle in `U(C)`;
4. a certificate that the cycle avoids the boundary and integrand singularities;
5. authority fixing the order `(u,v)` and cycle sign;
6. a physical boundary prescription, real form, or `i-epsilon` rule selecting the cycle;
7. normalization into the claimed quantity and units;
8. a typed state/effect pairing when probability or operational value is claimed;
9. a map to a stable physical record.

The first six fields determine a signed mathematical period. The remaining arrows are required for a physical readout. Failure of any field blocks the promotion.

Useful falsifiers include intersection with a pole, an orientation change without a source change, failure of the kinematic map to land in `U`, lack of homological invariance, and normalization fitted after the desired value is known.

## Disposition

None of the nine physical fields is instantiated by the audited characteristic-zero programme. The next leaf tests candidate cosmological boundary data against this contract; coordinate similarity cannot supply a missing arrow.

## Verification

- `research/voevodsky/check_cosmology_external_boundary_condition_contract.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
