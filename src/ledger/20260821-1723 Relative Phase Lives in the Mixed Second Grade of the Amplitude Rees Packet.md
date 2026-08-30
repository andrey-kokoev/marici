# 1723 — Relative Phase Lives in the Mixed Second Grade of the Amplitude Rees Packet

## Two-jet falsifier

Entry 1722 leaves open whether two amplitude directions entering the same
zero-probability outcome require higher coherence data.  Freeze

\[
|\chi(\varepsilon,\eta)\rangle
=\varepsilon|u\rangle+\eta|v\rangle.
\]

## Complete second grade

The unnormalized selected density expands as

\[
\boxed{
|\chi\rangle\langle\chi|
=\varepsilon^2|u\rangle\langle u|
+\varepsilon\eta
\bigl(|u\rangle\langle v|+|v\rangle\langle u|\bigr)
+\eta^2|v\rangle\langle v|.
}
\]

The three labelled Rees bidegrees are

\[
(2,0),\qquad(1,1),\qquad(0,2).
\]

Replacing \(|v\rangle\) by \(-|v\rangle\) leaves both diagonal positive rays
unchanged but reverses the mixed \((1,1)\) coefficient.  Hence separate summed
positive blocks lose relative phase, while the complete second-grade packet
retains it.

## Narrow result

No grade beyond total degree two is required in the tested model.  The correct
exceptional coefficient object is the complete Hermitian square of the
labelled amplitude-normal module, including its mixed occurrence.  This is the
quantum analogue of the complete symmetric-square covariance packet from
Entries 1698–1700.

No new Cut carrier stratum appears.

## Durable artifacts

- `research/benincasa/checkers/two_amplitude_jet_hermitian_square.rs`
- `research/benincasa/results/two-amplitude-jet-hermitian-square.json`
- `research/benincasa/two-amplitude-jet-hermitian-square.md`

## Next falsifier

Test Cut functoriality of the complete Hermitian-square packet.  Under a
labelled amplitude map \(f\), verify that density specialization is
\(f\otimes\bar f\), including mixed normals and partial trace.  Any failure of
naturality would require a genuine quantum coefficient coherence map.
