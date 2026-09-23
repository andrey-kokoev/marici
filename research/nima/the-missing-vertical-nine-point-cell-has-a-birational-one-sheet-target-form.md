# The missing vertical sector has a birational one-sheet arbitrary-Y form

The strictly positive vertical-column-2 neighbor **V**, absent from the positive images of both relabelled four-mass cells A and E on open sectors, admits a simpler **generic one-sheet** target pushforward.

Delete its identically zero physical column 3 and work over the eight retained external rows. V has a rank-one triple of columns `(2,3,4)` in this retained indexing. Its five **necessary** vanishing 2×2 minors are `(1,2),(2,3),(1,3),(4,5),(6,7)` in **zero-based** eight-column indexing. For a rank-two kernel shift `C₀+T K` with four free entries of `T` and `q=det T`, all five minor equations become linear in `(T₁₁,T₁₂,T₂₁,T₂₂,q)`. At **three exact positive regular targets** the 5×4 coefficient matrix has rank 4, and the unique left-null equation is respectively `581q/30=0`, `371q/20=0`, `903q/50=0`. The uniquely determined solution is the original V source. The nonzero left-null coefficient and rank are open conditions: **on a nonempty regular V-image open**, all candidate inverse sources are unique and rational in the target and external data (conditional on satisfying `q=det T`).

For arbitrary first-pivot `Y=[I₂|B]`, use the exact `SL(6)` recentering `z=Z_ret,last4−Z_ret,first2·B`, `h=Z_ret,first2`. The **oriented one-sheet** V coefficient on this open is

```
+det(C_V h)^4 /
 [w₂w₄w₅w₆w₇w₈u(t−u) · det(d(C_V z)/d(w₂,w₄,w₅,w₆,w₇,w₈,t,u))].
```

Its rational inverse is obtained by the five-minor linear lift; the complete fermionic numerator is `(C_V χ_ret)^8`. The coefficient was evaluated and is **nonzero** at each of three exact positive V targets. This constructs a concrete new sourced form sector **outside A∪E**, not a global nine-point triangulation, contour prescription, or full canonical form.

Checker: `research/nima/checkers/check_nine_point_vertical_cell_fibre_degree.py`; result: `research/nima/results/nine-point-vertical-cell-fibre-degree.json`.
