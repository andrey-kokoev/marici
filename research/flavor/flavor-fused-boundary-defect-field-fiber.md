# Fused boundary-defect field fiber: WP1109

## Question

What fields must a genuinely new UV boundary defect add to the existing
quotient data?

## Constructor fiber

The defect must carry six field groups, with twenty-three named fields total:

1. **Absolute boundary lift:** seven integer exponents, counterterm basis,
   evaluation law.
2. **Integer clock lift:** \(n\), \(\sigma\), unit-orbit law
   \(B/A=6n^2\), source normalization.
3. **Oriented second-stage frame:** adjoint ray, ordered \(B\) lines, cyclic
   seed, history dilation.
4. **Independent \(\rho\):** section, line bundle, descent law, temporal
   scope, comparison node.
5. **Production and gain:** a \(6\times6\) branch-to-physical16 kernel,
   event weights, channel selection, gain \(3/2\).
6. **Physical16 descent:** quotient map, comparison normalization, frozen
   readout provenance.

These are typed fields, not values. The clock variables remain unspecified,
\(\rho\) must have weight \(-3\), and the production kernel must be a
six-by-six matrix with gain \(3/2\).

## Classification

Conditional gate. WP1109 completes the missing-data specification for a new
fused defect but does not construct the packet.

Checker: `research/flavor/checkers/wp1109_fused_boundary_defect_field_fiber.py`

Result: `results/wp1109_fused_boundary_defect_field_fiber.json`
