# No-refit precommitment (WP405)

## Purpose

WP405 freezes WP403's completed grammar, nine benchmark parameters,
calibration contexts, withheld contexts, exact predictions, and rejection rule
before any physical binding or observation. The canonical contract has SHA-256
digest
`76735f9cc00c9829fd88f1c3cab85d91f9f0c502106eb7649eb9453cccfa89ef`.

The calibration records are three joint static contexts, two absorptive
contexts, and two extra-pole residual contexts. The reserved records are

- $(H,A_\star)=(4,7/4)$ at $c=3$;
- $A=(-5+30i)/37$ at $(c,\omega)=(2,2)$;
- extra-pole residual $1/5$ at $\omega=2$.

Any incompatible reserved record rejects the packet. Parameters may not be
refitted and a new correction or mediator may not be appended to rescue it.
Such a modification is a separately precommitted successor theory.

## Authority boundary

This is a prospective integrity contract, not an experimental result. It does
not turn the formal $c$ coordinate into an executable setting and does not
claim that any reserved record has been measured. WP404's apparatus gate must
close first.

Run `uv run python
research/flavor/checkers/wp405_no_refit_precommitment.py` to verify the digest
and regenerate the JSON result.
