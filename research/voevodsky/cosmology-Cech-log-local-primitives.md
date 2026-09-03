# Cech logarithmic local primitives

## Question

What exactly prevents `log(u) dlog(v)` from globalizing to the missing degree-one primitive?

## Claim boundary

On a logarithm branch, set

`A_i=log_i(u) dlog(v)`.

Then `dA_i=Xi_log`. On an overlap where the two logarithms differ by `2 pi i n_ij`, the primitives differ by

`A_i-A_j=2 pi i n_ij dlog(v)`.

Integrating that jump around a positive `v`-circle gives `(2 pi i)^2 n_ij`. Resolving the overlap form with local branches of `log(v)` produces corner jumps `(2 pi i)^2 n_ij m_jk`; unit windings yield the primitive integer cocycle one.

This double monodromy is simultaneously the normalized torus period, integral Tate generator, double residue, and oriented triangle class. It obstructs a single-valued global primitive.

Choosing branch cuts makes `A_i` single-valued only on a cut domain. The jump faces and corner terms restore the same global Cech–Deligne cocycle; omitting them changes the complex.

## Disposition

The local logarithmic primitive repackages rather than fills `(Xi_log,-sigma123)`. The next leaf audits the complete boundary of a cut-domain relative chain, including every jump and corner component.

## Verification

- `research/voevodsky/check_cosmology_Cech_log_local_primitives.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
