# Branch-cut relative chain

## Question

Does the complete boundary of a logarithmic cut-domain primitive equal the required horn vector?

## Claim boundary

No. On the square `0<=theta,phi<=2 pi`, with `u=exp(i theta)` and `v=exp(i phi)`, the local form is

`A=log(u)dlog(v)=-theta dphi`.

Its curvature integrates to `(2 pi i)^2`. By Stokes, the entire normalized contribution `1` lies on the `theta=2 pi` cut edge; the other three edges contribute zero.

Gluing the two `theta` edges to recover the torus introduces the jump `2 pi i dlog(v)`. Its normalized `v`-period is one. Resolving that jump with local `log(v)` leaves the unit corner cocycle. The edge jump and corner are mandatory descent components: deleting either violates Stokes or Cech descent.

The Parshin comparison identifies the unit corner with the primitive triangle class. It is the terminal obstruction, not a separately supplied opposite boundary that trivializes the total class.

## Disposition

The cut-domain chain does not have complete boundary `(Xi_log,-sigma123,0,...)`; its descent data retains the unit Deligne class. The next leaf classifies the changed relative complex obtained by declaring the cut edge a boundary and tests whether comparison back to the uncut source is faithful.

## Verification

- `research/voevodsky/check_cosmology_branch_cut_relative_chain.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
