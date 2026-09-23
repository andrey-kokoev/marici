# Strictifying a redundant Farkas row kills its positive surplus

In K=[0,1], append the redundant row `x<=2` to `-x<=0, x<=1`. The add multiplier M duplicates the second row, with nonnegative surplus c=(0,0,1); the drop multiplier N discards the third row. `NM=I_2`, but `MN!=I_3`. There are TWO tempting row quotients, and neither is a free analytic equivalence:

1. Quotient the three-row module by ker(N)=span(e3). Then MN becomes the identity modulo this kernel, but c=e3 is a strictly positive surplus erased by the quotient. The certificate's bound margin has been lost, not transported.
2. Quotient by the linear normal syzygy span(e3-e2), since duplicated normals give A'^T(e3-e2)=0. The drop map N does NOT annihilate that syzygy (`N(e3-e2)=-e2`), so the proof retraction does not even descend as the proposed map. Moreover the surplus e3 is not in this syzygy, so bound constants do not become equal under it.

Fresh `python research/voevodsky/checkers/check_farkas_syzygy_surplus.py` passes exact rational matrix/surplus controls. This is a minimal obstruction to two NAIVE strictifications, not a theorem forbidding all enriched positive chain constructions. A viable enriched target would have to retain both quotient-comparison homotopy and nonnegative surplus as a separate grade, with explicit descent and reciprocal compatibility, before any analytic closed-cone claim. The requested S/A/C/G source-derived role map remains absent; this result cannot substitute for it.
