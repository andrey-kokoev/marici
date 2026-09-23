# Weakening composes mathematically without collapsing the path history

From the unit-square x<=1 packet, direct weakening to x<=3 adds surplus 2. Two-step weakening via x<=2 adds 1 then 1; fresh `check_weakening_path_vs_endpoint.py` confirms identical final packet bytes and digest. But two-step synthetic occurrence path `(x1,x2,x3-via)` and direct path `(x1,x3-direct)` have different lengths, intermediate IDs, terminal occurrence IDs and path digests. Mathematical composition is not equality of historical derivations.

Both paths are fictional. A mathematical proof can support a new packet candidate; it does not prove either sequence was observed or that an issuer authorized it. No Farkas row source or analytic S,A,R,C,G role assignment can be published from these fixtures.

Next test PATH-REWRITE admission: an optimizer may propose replacing a two-edge weakening chain with a direct edge for arithmetic replay, but must retain the old chain as original audit history and mark the direct edge as a new derived view, not silently delete or overwrite occurrence records.
