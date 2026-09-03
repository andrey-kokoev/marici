# Spurion-alignment source gate: WP1201

## Question

Can a charge-recursive potential source spurion alignment?

## DPC resolution

- **Problem:** decide whether the spurion alignment needed by the equivariant
  lift is sourced rather than declared.
- **Bold conjecture:** a charge-recursive spurion potential derives the
  aligned source.
- **Named rivals:** unaligned charged-spurion lift; recursive sum-of-squares
  potential; source completion excluding orbit-moving invariants; canonical
  positive pairing.
- **Risky consequences:** the zero locus is one \(U(1)\) orbit; gauge fixing
  gives \((v,v,v)\) and kernel \(v^2(1,2,3)\); the complex Hessian has
  rank five with only the orbit null direction; \(\epsilon v^2|s_2|^2\)
  moves the vacuum and projective ray.
- **Strongest falsification attempt:** the declared potential passes germ and
  full-fiber tests but fails completion because an allowed invariant moves
  the orbit.
- **Exact residual:** a source theorem must exclude or fix every orbit-moving
  invariant and transport the index character.
- **Disposition:** construct conditional spurion alignment; reject
  source-unavoidable selection.

Checker: `research/flavor/checkers/wp1201_spurion_alignment_source_gate.py`

Result: `results/wp1201_spurion_alignment_source_gate.json`
