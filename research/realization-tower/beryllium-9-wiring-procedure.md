# Be-9: Wiring single procedure

- Start: eight strand pairs, sixteen straight wires in the XY plane, viewed
  along its normal.
- Step 1: two straight half-bundles meet at one central point. The upper
  endpoint order is reversed for the 180° turn. Every conductor passes through
  the same midpoint, retaining its identity and colour. No spiral, distributed
  torsion or curved transition is inserted.

Step 2 has been removed. Previously saved Step 2 selections restore Step 1.
This view currently displays the start and completed operation, not an animated
intermediate rotation.

Checks: `node --test tests/beryllium-9-wiring-procedure.test.mjs` and
`node scripts/test-beryllium-9-wiring-procedure.mjs`.
