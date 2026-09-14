# v110: soft D1 derived Cartier strictification

Three Rust calculations were freshly replayed for the remaining soft D1 map.

`rzk/138-soft-d1-derived-cartier-strictification.rzk.md` records why ordinary
reduction is incorrectly typed: the odd exact image has order one and does not
descend to the doubled `(z^2)` carrier. It does descend to the reduced `(z)`
carrier. The correct receiver is the derived two-term Cartier complex
`[R/(z) --z--> R]`, which accepts both even and odd maps without adding carrier
data.

The A2 principal-sector action `(f,p) -> (a^2 f, a^2 p - h(f))` is a strict
chain map, with the principal cell retained.

This constructs the local derived chain-map strictification. Its homotopy-fibre
cohomology and global road-Cech identification remain uncomputed.

The Rzk module passes all eight declarations with no assumptions.
