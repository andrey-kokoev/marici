# Scope of the missed-edge test

All 276 two-repair occurrences in `results/ramsey_four_port_repair_shared.json` have the same coverage property: each triple of rows misses precisely the same two outside sites. Their edge is blue. Suppressing witnesses that use both sites leaves no blue seven on three or four new ports. The singles and pairs already pass. This suppression is a witness test, not permission to recolor the pentagon.

The converse is false even with a permitted pairing. On square `137,138,147,148` and cycle `2–5–6–10–9–2`, take `359,479,{4,8,10},{5,8,10}`. Each triple misses outside sites 2 and 6. Their edge is blue, yet the four ports attach with all mutual links blue. Checked by enumerating the independent old vertex sets of size `7-n` common to each subset of `n=2,3,4` ports after verifying single-row legality. Thus the missed edge locates a necessary witness component, not the other vertices needed to complete each obstruction.
