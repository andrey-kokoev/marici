# Torsion-corrected single generator

## Question

What must one integral generator satisfy, and does any known candidate do so?

## Claim boundary

If an integer multiple `a h` fills the target, then `a n=1` and `a r=-1`. The only possibilities are

- `a=1`, with free vector `(n,r)=(1,-1)`;
- `a=-1`, with free vector `(-1,1)`.

Because the sign layer has order two, both orientations require the same primary decoration `epsilon_Z=(0,0,1)`. The two residual sign coordinates and every additional boundary component must vanish. The element must also be globally sourced in total degree one.

No materialized candidate passes. Rank-26 and higher-face candidates have zero `Xi_log` coefficient; `{u,v}` has the right primitive class but degree two; logarithmic primitives are local and retain descent residuals.

Diagonal symbols can alter signs only in motivic degree two. They cannot correct a missing degree-one generator without a separately sourced degree-one torsion element and typed addition map.

## Disposition

The one-generator integral contract is exact and currently uninstantiated. The next leaf determines whether the relevant higher-Chow or relative degree contains any sourced order-two correction elements.

## Verification

- `research/voevodsky/check_cosmology_torsion_corrected_single_generator.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
