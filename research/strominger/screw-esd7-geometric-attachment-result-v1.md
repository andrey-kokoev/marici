# Registered screw-to-esd7 geometric attachment: occupied cells fit, full context does not

## Fresh state and registration

Revision31 required an actual attachment, not another sewing check. The F006
source gate also distinguishes analytical face data from geometric labels. This
attempt therefore chose and registered the literal shared-lattice interpretation
in revision32 BEFORE execution. Contract:
`contracts/screw-esd7-geometric-attachment-attempt.v1.json`.

Source: the freshly replayed24-body screw patch and all retained chart aliases.
Target: the actual343 primitive tetrahedra from `assembleComponents(7)`, not a
cell-count surrogate. Allowed maps are signed coordinate permutations followed
by an integer translation preserving sum(x)=1. No rescaling, deformation,
independent body relocation or particle reassignment is permitted.

## Sharp envelope test

For sign s in{+1,-1}, let m_i=max(s*x_i) over the required vertices. Before
translation their coordinate sum is s. In these coordinate directions, the
smallest containing simplex has edge resolution

    k_min = sum(m_i) - s.

For the target x_i<=2, a translation must satisfy

    t_i <= 2-m_perm(i),    sum(t)=1-s.

Its total available slack is7-k_min. Negative slack proves impossibility for
ALL translations of that orientation, including nonintegral ones. Otherwise all
integer placements are obtained from the nonnegative four-part compositions of
that slack. Coordinate permutations cannot change k_min.

## Result

| Required data | Positive sign minimum k | Negative sign minimum k |
| --- | ---: | ---: |
| Occupied primitive vertices only |7|6|
| Occupied vertices plus all retained reference aliases |8|8|

Thus all48 registered signed orientations fail the fully internalized reference
condition at k=7. This is not because the occupied patch is too large.

The occupied-only diagnostic finds **40 exact primitive embeddings** into the
actual target triangulation. Every one has external reference context; some need
only one distinct reference vertex outside the envelope. The artifact lists all
placements and every excluded reference coordinate, rather than hiding or
clipping those coordinates. Source histories, species and coefficients are not
changed to obtain these placements.

A positive control embeds the generated target into itself in its identity frame.
All source construction prefixes were also checked: there is no prefix whose
occupied geometry alone exceeds k=7 in both sign classes.

## Concrete minimal external-reference witness

In the diagnostic frame `x -> -x + (-3,2,2,1)`, all24 occupied primitives
are actual esd7 primitives. Only one distinct reference lies outside:

    source C0 = (0,1,-1,1) -> (-3,1,3,0).

Its third coordinate is3, violating the target bound x_2<=2. It is C0 in
neutron chart-5 (packet5) and electron chart-15 (packet15). The retained
NE interface15 goes from packet5 to packet15; reader-phase interface5 enters
packet5 from packet1. Neither occupied interface face contains this reference.
This is an external reference-context obligation, NOT a failed occupied contact
or a failed44-channel sewing square. The witness includes inverse coordinate
reconstruction, both alias owners and their retained packet/interface IDs.

This frame minimizes external reference count among the enumerated occupied
embeddings for diagnostic purposes only; it is not a physical frame selection.

## Disposition

The registered fully internalized geometric attachment fails. A useful partial
attachment succeeds: occupied primitives fit exactly while reference data must
remain outside the finite geometric carrier. The earlier reference-only-P work
already cautions that reference context need not be occupied, but does not by
itself supply every needed external-domain/analytical witness.

**Next nonredundant test:** register a relative attachment using one explicitly
selected occupied embedding while retaining its complete external-reference
ledger. Verify inverse reconstruction, native face/occurrence maps and the
boundary of the analytical domain. Selection among the40 placements is a declared
frame choice, not a physical preference or isotope selector. Do not pretend that
retaining external context makes it an internal esd7 vertex.

No actual F006 analytical edge operator or homotopy follows. A coherence-
presentation map, larger carrier, other map family or full Pb construction is
not refuted by this result.

## Reproduce

```sh
node research/strominger/checkers/check_screw_esd7_geometric_attachment.mjs
```

Eleven checks pass. Full bounds, all admissible occupied placements, external
reference coordinates and actual construction-prefix diagnostics are in
`results/screw-esd7-geometric-attachment/attempt.json`; its live-source receipt is
`results/screw-esd7-geometric-attachment/verification.json`.
