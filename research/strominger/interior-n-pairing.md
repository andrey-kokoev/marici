# Interior N cancellation trial — single edge-7 octahedron

The single octahedron has 231 N cells: 146 surface and 85 interior. Native inversion pairs the actual interior cells into 42 pairs plus the self-dual central cell `neutron:1,1,1,0`.

For test scalar amplitudes a,b on a pair, define common mode m=(a+b)/2 and contrast d=(a-b)/2. Reconstruction is exact: a=m+d, b=m−d. The pair net is 2m, while its squared amplitude norm is 2(m²+d²). Cancellation of the net does not erase the contrast or remove either cell.

| Explicit test data | Interior net | Squared amplitude norm |
|---|---:|---:|
| All 85 amplitudes +1 | 85 | 85 |
| Every pair +1/−1; centre +1 | 1 | 85 |
| Linear odd amplitude along the declared N axis | 0 | 832 |

The second test's pair order is only a bookkeeping sign convention. It is not derived from geometry or signed-state transport. The third test uses the geometric amplitude `(centroid-c)·(1,-1,1,-1)`: 30 pairs are active; 12 pairs lie in the zero-amplitude plane; the centre is also zero.

There are 43 scalar common/fixed modes and 42 scalar contrast modes, still 85 scalar degrees of freedom. Restricting to an odd field would discard the common modes by an additional constraint; this trial does not justify doing so. The geometric inversion itself preserves N cell type and does not require negative amplitudes.

Thus uniform N occupancy does not cancel. If one additionally left all 146 surface amplitudes at +1 and imposed the paired interior test, the total amplitude would be 147, not a derived neutron inventory. The displayed whole-cell count remains 231 N throughout. No Pb-208 count is inferred.

## Viewer and checks

In **Single octahedron — edge 7, no belt**, open **Interior N pairing trial**. It shows the pairing and the three scalar-net results without changing geometry, wiring or count tables. It does not colour cells by a presumed physical sign.

- `research/strominger/interior-n-pairing.mjs`: source-cell pairing, invertible mean/contrast transformation and explicit test states.
- `scripts/probe-interior-n-cancellation.mjs`: reproducible headless report.
- `tests/interior-n-pairing.test.mjs`: actual inversion witnesses, reconstruction, norm retention, sign-convention independence of the net, and the non-cancelling uniform counterexample.
- Browser regression checks verify the trial readout and unchanged cell inventory.

Open question: can an admitted N-state evolution select an odd or antiphase field? Without that rule, the cancellation is conditional, not a consequence of the cellulation.
