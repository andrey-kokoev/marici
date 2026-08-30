# 1815 — Cyclic Transport Preserves the Transverse Residue Orientation

## Question

Do Entry 1814's oriented local Gysin maps acquire a sign after transport
around the five-site occurrence atlas?

## Cyclic step

The source cyclic relabelling acts on the loop tangent geometry by the
orientation-preserving rotation through \(2\pi/5\). It transports an ordered
wall pair as

\[
(A,B)\longmapsto(\sigma A,\sigma B)
\]

without exchanging its two entries.

Therefore both the tangent orientation and the normal determinant-line
orientation have transition sign

\[
+1
\]

at every cyclic step. Five steps compose to

\[
\boxed{+1}.
\]

## Result

The \(S_2\) sign from exchanging two wall occurrences remains intrinsic, but
there is no additional \(C_5\) orientation twist. The 22 oriented Gysin
families therefore retain the cyclic representation

\[
\boxed{
\mathbb Q[C_5]^{22},
\qquad
\chi=(110,0,0,0,0).
}
\]

Thus the local maps glue over the labelled cyclic atlas with identity signed
composition.

This proves coefficient-atlas coherence. It does not prove that the physical
relative integration chain has a nonzero boundary in these supported
coefficient lines.

## Next falsifier

Audit the frozen five-cycle integration chamber and its prescribed contour
near one active transverse intersection. Determine whether its relative
boundary reaches the oriented two-wall stratum. If it does, compute the
source-normalized pairing; if it does not, classify the coefficient family as
algebraically present but physically unselected.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_pair_cyclic_orientation.py
- research/benincasa/results/five-site-g5-transverse-pair-cyclic-orientation.json
- Entries 1810, 1813, and 1814
- allocator claim: seqclaim-f3a48bcb27a8b28ba3a090ed
