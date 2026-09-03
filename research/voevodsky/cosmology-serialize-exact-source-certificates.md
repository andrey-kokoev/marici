# Serialize exact source certificates

## Question

What durable object makes an exact absorption witness replayable and safe for later geometrization?

## Claim boundary

Implemented certificate schema `marici.voevodsky.exact-source-certificate.v1`. Each record requires:

- a canonical target ID derived from its descriptor;
- an ordered source-basis manifest and digest;
- the exact equation matrix and digest;
- the exact target and digest;
- a normalized sparse rational coefficient word;
- generator path, source digest, and argv command.

Replay uses exact rational arithmetic to verify `A w=target` with zero residual. Deliberate mutations test the gate: changing a coefficient produces a nonzero residual, reordering the basis without updating its digest is rejected, and `full_reconstruction=true` alone fails for missing fields.

The contract is implemented, but the 1,224 existing seed records remain unpopulated because they reference neither generating source paths nor coefficient words.

## Disposition

Replay semantics are fixed and tested. The next leaf locates the seed-generator provenance needed to regenerate actual certificates; absence of that provenance is a typed durability blocker.

## Verification

- `research/voevodsky/check_cosmology_exact_source_certificate_contract.py` — exit 0
- `research/voevodsky/results/cosmology_exact_source_certificate_contract.json` — exact replay passed; three deliberate mutations rejected
