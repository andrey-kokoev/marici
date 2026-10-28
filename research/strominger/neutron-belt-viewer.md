# Neutron belt inspection in the normal-ray viewer

Select **Neutron interior — annular belt**, or click **Inspect neutron interior** in the double-ESD7 panel.

The inspector reuses `research/voevodsky/results/four_six_center_cones.json` and the opposite-circulation signs and sector pairing from `research/voevodsky/results/mode_flux_charge.json`. The adapter converts physical XYZ coordinates isometrically into the viewer's sum-one chart.

- Six original tetrahedral cones, three paired sectors.
- Teal/violet distinguish positive/negative circulation; they are not P/E assignments.
- Eighteen outer-panel direction arrows visualize the signed face cycles.
- Two cap cones remain excluded, exactly as in the source.
- No additional plane is removed.
- No internal particles are added to the main graph's counts.

The source's 1836 value counts intrinsic protocol transfers. The viewer displays the carrier and circulation pattern, not all 1836 coefficient arrows. Assigning this carrier to an individual parent N and implementing an active branch converter remain open. Passive interface identification is not that converter.

Verification:

```
node --test tests/neutron-belt-process.test.mjs
node scripts/prepare-normal-ray.mjs
node scripts/test-neutron-belt.mjs
```
