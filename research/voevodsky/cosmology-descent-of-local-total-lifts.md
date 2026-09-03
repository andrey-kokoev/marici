# Descent of local total lifts

## Question

What obstructs gluing the split local total lifts?

## Claim boundary

Let `L` be the homotopy fiber of total-to-special mapping spaces over `tau0`. Local lifts `tau_i` are sections of the resulting `L`-torsor. On overlaps,

`Delta_ij=tau_j-tau_i`

lies in the kernel of restriction and satisfies the Cech cocycle identity.

For an abelian connective model, the primary obstruction is `[Delta]` in `H1(pi0 L)`. If it vanishes, chosen overlap paths can still have a triple-overlap defect in `H2(pi1 L)`. Higher coherences lie in `H^(q+1)(pi_q L)`. Equivalently, the totalization of the Cech nerve of local lift spaces must be nonempty.

Coordinate changes have the form

`x_beta=A_ab x_alpha+t Q_ab(x,t)`.

The normal cone sees `A_ab`; the `t`-dependent terms control the total-lift cocycle. A common coefficient line kills the special-fiber ratio obstruction but not necessarily these terms.

No global atlas, transition maps, or total comparison complex is materialized, so these classes cannot be evaluated.

## Disposition

Global total promotion is a Cech/Postnikov descent problem. The relative special-fiber lift is unaffected. The next leaf identifies sufficient geometric conditions forcing all descent obstructions to vanish.

## Verification

- `research/voevodsky/check_cosmology_descent_of_local_total_lifts.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
