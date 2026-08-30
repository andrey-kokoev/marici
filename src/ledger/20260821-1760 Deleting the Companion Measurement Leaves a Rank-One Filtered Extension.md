# 1760 — Deleting the Companion Measurement Leaves a Rank-One Filtered Extension

## Declared deletion

Entry 1759 uses two first-order scalar observations. Write

\[
s=q_x(S),
\qquad
d=i(R_{01}-R_{10}).
\]

The companion and diagonal measurements give

\[
\begin{pmatrix}
s\\s+d
\end{pmatrix}
=
\begin{pmatrix}
1&0\\
1&1
\end{pmatrix}
\begin{pmatrix}s\\d\end{pmatrix}.
\]

This observation matrix has determinant one, so the complete packet
separates finite calibration transport from the supported curvature jet.

Apply the literal labelled deletion map that removes the companion
real-superposition measurement. The surviving observation is

\[
\boxed{s+d.}
\]

Its kernel is

\[
\boxed{
\mathbb Q\langle(1,-1)\rangle.
}
\]

Indeed,

\[
(s,d)\longmapsto(s+\lambda,d-\lambda)
\]

leaves every surviving first-order scalar unchanged.

## Narrow result

After companion deletion, the finite calibration term and supported residue
jet no longer split canonically. They form a rank-one filtered extension.
This is not an artifact of coordinates: it is the kernel of the declared
source-label deletion map.

The scope is conditional. No frozen cosmological source has yet been shown
to enforce this particular measurement deletion. Therefore:

- extension under the declared deletion: established;
- physical occurrence of the deletion: open;
- permission to add a replacement scalar: absent;
- new carrier stratum: unsupported.

## Durable artifacts

- research/benincasa/checkers/companion_measurement_deletion.rs
- research/benincasa/results/companion-measurement-deletion.json
- research/benincasa/companion-measurement-deletion.md

## Next falsifier

Classify source symmetries of a rank-two measurement packet. Determine
whether any invariant/anti-invariant projection deletes the companion while
retaining the diagonal family. Only such a source-derived projection would
promote the conditional extension to a physical coefficient class.
