# Iteration 5: scoped proof transport beyond branch swaps

## Delivered construction

`merkle_witness_transport.py` transports entire polynomial equality proof DAGs between contexts by explicit variable substitution. The source judgment, target judgment, substitution and assumption-discharge proofs are bound by a Merkle certificate. Verification reconstructs the expected transported proof and checks its exact target judgment root, not merely its final polynomial value.

Every used source assumption must have a supplied target proof with exactly the substituted endpoints. Target assumptions are retained by the existing equality kernel. The transport does not silently copy an assumption label into a different context or decide that a hypothesis is true because the endpoints have convenient values.

## Worked dependent-on-assumptions family

Start with h:x=y and the congruence proof x*x=y*y. Substitute x=a+1 and y=b+1. To transport h, provide a congruence proof a+1=b+1 from the target assumption ab:a=b and reflexivity of 1. The resulting square identity remains explicitly conditional on ab.

Next substitute a=2u and b=2v. Discharge ab by a congruence proof 2u=2v from uv:u=v and reflexivity of 2. The final proof is conditional on uv.

Directly substituting x=2u+1 and y=2v+1, with the composed discharge proof, produces exactly the same final judgment hash as these two successive transports. This fixture checks route compatibility at proof structure level, not just equality of evaluated outputs. Identity substitution likewise retains the original judgment root.

Substituting both x and y by w is a different case: h becomes w=w, which has an unconditional proof. Explicitly supplying that proof legitimately discharges the old assumption. Refusing all assumption elimination would be as incorrect as allowing silent elimination.

## Proof relevance and scope

A valid target proof wrapped in symmetry twice proves the same equality, but has a different proof history. Replacing the structural transport result by that proof is rejected unless an additional comparison rule is provided. The implementation does not assume proof irrelevance.

This is general substitution for the existing Q-polynomial equality grammar and its scoped proof rules, not a dependent type theory. It handles proof families whose propositions and assumptions depend on substituted variables; it does not implement arbitrary dependent types, higher identity elimination, analytic branch monodromy, or automatic discovery of discharge proofs.

## Tests

All 21 checks passed:

- nonlinear family transport and exact source/target dependency tracking;
- two-stage/direct composition agreement and identity transport;
- explicit discharge to an unconditional target;
- missing or extra discharge proofs, missing substitutions, wrong proof endpoints and undeclared target variables rejected;
- false unconditional discharge rejected;
- a different valid target proof history distinguished from the required structural image;
- tampered certificates, honestly rehashed wrong substitutions, rebound source and missing proof objects rejected;
- JSON round trip and fresh CLI verification passed.

## API and reproduction

The constructor accepts a source proof store, target `Builder`, target variable/context declarations, a total map from source variable names to target term hashes, and a map from used source assumption labels to target proof hashes:

```text
construct(source, target_builder, variables, assumptions, substitution, discharges)
verify(transport_packet)
```

Run:

```text
python research/voevodsky/checkers/check_merkle_witness_transport.py
python research/voevodsky/checkers/merkle_witness_transport.py research/voevodsky/results/merkle_witness_transport_store.json
```

Artifacts:

- `research/voevodsky/results/merkle_witness_transport.json`: test receipt and fingerprints.
- `research/voevodsky/results/merkle_witness_transport_store.json`: first substitution with retained assumption evidence.
- `research/voevodsky/results/merkle_witness_transport_composition.json`: first, second and direct route packets for comparison.

Next: unify verification entry points and add safe reusable verification caches, hostile input tests and measured benchmarks without broadening the mathematical claims.
