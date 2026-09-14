# v129: candidate group/reflection split

Fresh inspection of the full comparison-fibre replay narrows the second
physical-completion gate substantially.

The native candidate already passes 31,992 checks each for closedness,
zero-class comparison, and the integral group-operation homotopy. Native-bar
and endpoint group-chain equivariance pass 20,646 and 61,932 checks, and full
relative-algebra dihedral transport passes 744 checks. The strict selected
reflection formula is `s(W)=-W+[r11,r00]`.

What remains is not an algebraic group homotopy: the target transport explicitly
reports `reflection exchanged; no physical parity selected`. Hence the group
field of module 132 is reduced to selecting the physical reflection parity and
transporting the already proved native homotopy through that selection.

Evidence is `results/candidate-group-reflection-split.json` from
`checkers/check_candidate_group_reflection_split.py`.
`rzk/157-candidate-group-reflection-split.rzk.md` passes all six declarations
without assumptions.
