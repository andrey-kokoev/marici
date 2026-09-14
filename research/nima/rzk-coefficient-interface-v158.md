# v158: strict L2 cutoff projection system

The compatibility problem was moved from noncanonical Smith bases back to the
labelled chain matrices. Exact-rational columns were compared under degree
projection for D16->12, D20->16, D24->20, and D28->24.

Every shared labelled column projects identically. Every newly appearing source
column has zero output in the lower-degree target. The lattice with generator
`u/2` is preserved. Thus the actual labelled L2 matrices form a strict filtered
projection system through D28.

This is stronger and more useful than trying to nest Smith invariant-factor
lists: chain-level cutoff maps are canonical even when Smith bases are not. The
remaining derived task is to lift saturation cells along these projections, not
to invent compatibility maps for unrelated diagonalizations.

Evidence is `results/L2-cutoff-projection-compatibility.json` from
`checkers/check_L2_cutoff-projection-compatibility.py`.
`rzk/186-l2-cutoff-projection-system.rzk.md` passes all six declarations without
assumptions.
