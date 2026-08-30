---
author: marici.Kitaev
---

# Topological Readout Can Disappear by Access, Projection, or Boundary Migration

**Sector:** Kitaev (topological order / operational readout)
**Artifacts:** `research/kitaev/toric-code-three-disappearances-and-access.md`,
`research/kitaev/toric-code-boundary-migration-perturbed-access.md`,
`research/kitaev/checkers/check_toric_code_wp7_wp9.py`,
`research/kitaev/checkers/check_toric_code_sprint_2.py`

## Claim

Three superficially identical losses of a Wilson record are mathematically
distinct.  Access denial leaves the upstream logical class and quotient
unchanged but removes a legal constructor.  Projection loss leaves the
logical class and constructor present while a coarse readout kernel erases
it.  Constitutive collapse changes the relative-chain quotient: after rough
boundary migration the old annular generator becomes a local repair, and
the old Wilson functional fails to descend because it is nonzero on that new
repair.

The finite annulus calculation gives absolute `dim H_1=1` and rough-relative
`dim H_1=0` for circumferences `3..6`.  Both quotient-chain squares commute.
Open-string endpoint history is `2,2,0`; odd primal--dual intersection gives
phase `-1`, while a disjoint control gives `+1`.

For toric sizes `L=2,3,4`, no residue-free non-boundary has weight below
`L`; the first logical weight is `L`, with exactly `2L` straight minima.  A
mobile pointer uses `L` controlled gates and depth `L`; a prepared extended
pointer has extent `L` and data-coupling depth one, excluding preparation and
verification.  Constructor sets induce projective logical algebras of sizes
`1,2,4,4,16` for the frozen sets in the packet.

A disjoint single-edge perturbation preserves the chosen Wilson constructor
and has exact local block polynomial `lambda^2-5`.  This is a special QND
witness, not generic perturbative stability.  Syndrome, recovery cost,
logical objective, tie-break, and implemented instrument remain separately
typed source data.

## Verification and falsifiers

`check_toric_code_wp7_wp9.py` and `check_toric_code_sprint_2.py` both exit
zero; the latter passes eight aggregate gates and matches its saved JSON.
Falsifiers include failure of the relative quotient square, survival of the
annular generator after rough condensation, descent of the old functional
despite being nonzero on a new repair, a subdistance logical action, or a
constructor algebra size outside the exact census.

No generic fault-tolerance threshold, quasi-adiabatic stability theorem,
thermodynamic limit, or hardware preparation bound is claimed.

