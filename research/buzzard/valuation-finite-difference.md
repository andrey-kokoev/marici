# Valuation finite-difference packet

## Grothendieck source

This formalizes the convention-fixed algebraic content of Sections 8, 12,
19, and 21 of
`research/grothendieck/theta-cubic-bilinear-companion.md`.

## Formal objects

- `valuationCell tail j = tail j - tail (j+1)` is the one-prime exact
  valuation packet.
- `valuation_cells_telescope` proves that exact cells below a finite cap plus
  the overflow tail reconstruct the original source.
- `AddBilinear A C` represents the polarized companion independently of its
  analytic construction.
- `bilinear_valuationCell_expansion` is double finite-difference recovery of
  an exact valuation-pair channel from four mixed tail observations.
- `bilinear_polarization` proves that source addition forces both cross terms.
- `diagonal_only_loses_cross_repair` is the finite hostile: retaining only
  diagonal packets changes the readout of a sum.

## Assumptions and coefficient types

The source packet and target readout are arbitrary additive commutative
groups. Bilinearity is represented by an additive homomorphism into additive
homomorphisms. No order, topology, measure, differentiation, or field is
needed.

## Missing analytic interfaces

The theorem does not identify a tail route with a translated theta source;
that needs the exact theta scale law and convergence domain. It does not show
that valuation packets are seam-closed or positive, and it does not imply the
paired moment inequality. Finite-difference faithfulness, seam regularity,
and physical orientation remain distinct conditions.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
