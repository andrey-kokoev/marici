# Live calibration-epoch interlock

## Result

A finite two-clock optical frequency instrument can be exactly observable and still return a confidently wrong source class when its phase frame is stale. A live epoch interlock rejects the record before decoding; an independently certified reference tone can refresh the phase origin.

## Source and labelled ports

The source frequency is certified to lie in (X=\{0,\ldots,19\}). Two labelled sampling ports record residues modulo 4 and modulo 5. The calibration manifest contains the rates, port order, phase origins, and timebase epoch.

At captured epoch 0, both phase origins are zero. At live epoch 1, the modulo-5 clock has shifted by one unit. Source 1 then produces the ordered record

\[
(1\bmod4,(1+1)\bmod5)=(1,2).
\]

## Constructor order and calibration frame

The valid procedure binds both physical clocks to a live calibration epoch, validates the record's epoch token, samples the source, and only then applies the decoder. The stale decoder

\[
d_0(a,b)=5a+16b\pmod{20}
\]

maps ((1,2)) to 17. This is not a noisy or low-confidence output. In the stale frame, source 17 produces exactly the same record.

The live decoder subtracts the declared phase displacement:

\[
d_1(a,b)=5a+16(b-1)\pmod{20},
\]

and recovers source 1.

## Conserved information and detector kernel

The ordered residue pair preserves all CRT information relative to a fixed frame. It contains no bit identifying which calibration epoch generated it. Consequently the unknown source record cannot self-calibrate: ((1,2)) is compatible with two different source-frame pairs.

The interlock compares the captured manifest epoch with the live clock epoch before decoding. A mismatch is a rejected execution, not an alternative frequency estimate.

## Independent refresh operation

An independently certified zero-frequency reference produces ((0,1)) at live epoch 1 and identifies the modulo-5 displacement. Refreshing from that reference recovers source 1. The reference preparation is a distinct source operation; treating the unknown signal itself as the reference would be circular.

## Smallest hostile

The hostile instrument retains both coprime clocks, the band, port labels, and the mathematically correct epoch-0 decoder, but omits live epoch validation. It accepts the shifted record and asserts source 17 instead of source 1.

## Completion and authority boundary

This exact interlock separates observability from calibration standing. It does not certify that the physical source lies in the band, authorize clock operation, handle stochastic drift, or extend the CRT theorem to continuous frequency.

## Reproduction

Run:

    python research/aspect/checkers/live_calibration_epoch_interlock.py
