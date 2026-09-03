# Locate seed-generator provenance

## Question

Do authoritative generators retain enough transient state to emit replayable source certificates?

## Result

Git history ties the nonmarked-K generator and the three result families to commit `fff26499944bd3a9912078dccaed12ffae6c263f`. Exact-path Git logs return no commits for the visible IBP and q generators; they are untracked. The visible generators are:

- `research/voevodsky/check_cosmology_IBP_corrected_transport_exact_seeds.py`
- `research/voevodsky/check_cosmology_nonmarked_K_exact_seeds.py`
- `research/voevodsky/check_cosmology_q_exact_seeds.py`

Each visible file imports the same raw-relation constructor, derivative-row adapter, source DAG, exact CRT lift, and exact rational solver. Immediately before summary serialization, each retains ordered basis origins, exact lifted rows, exact target, equation columns, rational coefficients, rank, and exact reconstruction.

The coefficient words are therefore recoverable without changing the algebra once mutation authority is established. Only the nonmarked-K generator has Git provenance. Basis IDs are the existing origin tuples `(T|S_K|Q,index)`. Canonical target IDs derive from seed descriptors. Sparse words are the nonzero coefficient entries in ordered origins.

## Scope

This establishes algebraic serialization provenance, not geometric support, a source differential, DNC specialization, or transport beyond the existing constructor law.

## Disposition

Populate actual seed certificates by patching these generators and replaying all 1,224 records.

## Verification

- `research/voevodsky/check_cosmology_seed_generator_provenance.py` — exit 0 after repairing tuple-target AST collection
- `research/voevodsky/results/cosmology_seed_generator_provenance.json` — three generator paths and source digests recorded
