# v109: soft D1 Cartier boundary

The soft-axis Cartier-boundary Rust checker was freshly replayed.

`rzk/137-soft-d1-cartier-boundary.rzk.md` records boundary orders `(3,4)` for
the odd nearby class. Its normalized Q-symbol has coefficient `-6`, which is
nonzero and invertible rationally. The odd first Cartier map is surjective at
both excluded boundary points `b=+/-1`, and the local boundary cokernel is zero.

Thus the local D1 boundary obstruction left by v108 is cleared. The checker
still does not construct or assert the global specialization map, so the full
road-Cech completion remains open at global assembly rather than local boundary
surjectivity.

The Rzk module passes all eight declarations with no assumptions.
