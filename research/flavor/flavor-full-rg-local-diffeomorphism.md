# The complete one-loop RG field is locally invertible transport (WP61, move 2/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

WP53 proved descent and nonselection for the leading common-rescaling
approximation. WP61 removes that approximation. The complete coupled one-loop
Yukawa beta field contains the self-sector and cross-sector cubic terms of
S16. It is a smooth autonomous polynomial vector field on Yukawa-pair space
and is equivariant under the full weak-basis action.

ODE uniqueness implies that, on every finite interval where forward and
reverse solutions exist, its flow is a local diffeomorphism. The exact checker
constructs the full coupled field on an exact noncommuting two-generation
slice and verifies the forward/reverse flow-jet cancellation through second
order. The differential determinant at zero RG time is exactly one.

Therefore the full field preserves the local contextual partition of
`physical16`; it transports physical points bijectively and has no locally
proper image. A global attractor or UV boundary condition would be additional
data and cannot be inferred from the beta vector field alone.

Classification: descends, transports, neither selects nor rigidifies. No
standalone physical instrument executes RG flow; measurements at specified
scales provide boundary readouts.

Verification:
`uv run --with sympy python research/flavor/checkers/wp61_full_rg_local_diffeomorphism.py`.
