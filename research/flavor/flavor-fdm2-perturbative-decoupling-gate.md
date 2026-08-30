# Perturbative decoupling gate for the FDM-2 mediator (WP92)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Typed matching parameter

Restore dimensions in the WP90 tree matching. With `f=|<S>|`, mediator mass
`M`, and dimensionless real couplings `a_i,b_j`, the induced Yukawa term is

\[
\Delta Y_{ij}=\frac{\langle S\rangle}{M}a_i b_j.
\]

Define `r=f/M` after fixing the phase of the CP-broken singlet vacuum. If
`|a_i|,|b_j| <= g_max`, then

\[
|\Delta Y_{ij}|\le g_{\max}^2 r.
\]

Thus the perturbative decoupling limit `M/f -> infinity` sends the induced
flavor source to zero. A fixed order-one effect cannot be retained in that
limit without growing a coupling, growing `f`, or abandoning decoupling.

## Exact CP witness along the decoupling ray

For the WP90 matrices, replace its implicit unit matching coefficient by a
real `r >= 0`:

\[
Y_d(r)=Y_0+r(4/5+3i/5)ab.
\]

The exact checker finds

\[
\det[H_u,H_d(r)]=1152 i r^3.
\]

Every finite `r>0` remains in the CP-broken attribute, but the invariant
margin collapses cubically and the strict decoupling endpoint `r=0` is CP
even. Therefore WP90 is an algebraically valid finite-threshold selector; it
is not yet a uniformly robust heavy-mediator EFT selector.

The Schur complement is the exact zero-momentum tree matching relation for
the quadratic mediator block. Calling it an exact physical low-energy
instrument additionally requires a momentum domain `p/M << 1`, radiative
matching, and declared coupling bounds.

## Verdict and smallest falsifier

Classification: **selector at finite threshold**, neither a chart rigidifier
nor a selector with a nonzero decoupling-limit margin. The smallest exact
falsifier of the stronger claim is `r=0`, where the commutator determinant is
exactly zero. The smallest quantitative hostile family is `r=1/n`, for which
the determinant magnitude is `1152/n^3` despite remaining nonzero at every
finite `n`.

The remaining instrument gate is now sharper: specify `f/M`, perturbative
coupling bounds, the matching scale and momentum range, loop corrections,
and a minimum experimentally resolvable CP-odd margin.

Verification: `uv run --with sympy python
research/flavor/checkers/wp92_fdm2_perturbative_decoupling.py`.
