# Resolution invariance of the exceptional triangle obstruction

## Theorem

Blowing up a stratum of an SNC boundary induces a stellar subdivision of its dual complex. For the exceptional triangle, blowing up a pairwise crossing subdivides one edge: both the vertex and edge counts increase by one. Connectedness and Euler characteristic zero are preserved, so integral first homology remains `Z`. Blowing up a Cartier boundary component is an isomorphism and changes nothing.

Consequently every toroidal/log resolution obtained from the same exceptional boundary pair retains the primitive triangle cycle. No such resolution creates a two-cell filling it.

## Verification

The graph invariant was checked through 100 successive edge subdivisions. The final graph had 103 vertices, 103 edges, no faces, and first Betti number one.

## Disposition

The resolution-invariance leaf is completed. Repeated blow-ups of SNC strata cannot construct the missing total lift. The next branch must test genuinely new source geometry that changes the incidence homotopy type—rather than another resolution of the same pair—and supplies both a face over the cycle and a chain map to `(Xi_log,-sigma123)`.

A relative-face or Cayley-Menger cone is admissible only if derived from such source geometry. Formally coning the cycle without that provenance is the prohibited abstract `tau_p` insertion.

## Reproducibility

- `research/voevodsky/check_cosmology_exceptional_triangle_resolution_invariance.py`
- `research/voevodsky/results/cosmology_exceptional_triangle_resolution_invariance.json`
