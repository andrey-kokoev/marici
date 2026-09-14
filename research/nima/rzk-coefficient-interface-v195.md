# v195: raw physical Cech equality is underdetermined by the current API

A fresh source audit found that every occurrence of `rawCech` in the Rzk
physical-road modules is a polymorphic function parameter. There is no concrete
physical chart or residue definition of that function anywhere in the current
Rzk sources.

Consequently the final road equality is not derivable: the same constructed
ramified road cell, occurrence label, and selected class admit one model where
`rawCech` is the selected target and another where it is zero. The existing
interface cannot distinguish them.

This does not reopen the road-cell construction. The boundary-to-v comparison
is constructed through v194. The missing source datum is now narrower: an
occurrence-labelled local qG12 formula defining the raw physical defect as an
element of the same ramified filtered Q target. Once supplied, it can be
compared directly with the exact branch difference `d/A`.

Evidence is `results/raw-physical-cech-definition-gate.json`.
`rzk/223-raw-physical-cech-definition-gate.rzk.md` passes all eight declarations
without assumptions.
