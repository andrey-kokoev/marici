# 1759 — The Complete Measurement Packet Splits the Diagonal Rees Mixing

## Diagonal pullback

Entry 1758 keeps the calibration normal \(x\) and measurement normal
\(\delta\) separate. Write the regularized curvature polynomial as

\[
xK_x=R+xS+x^2T,
\]

where \(R=R_{\rm par}\).

Pull the measurement family to the diagonal

\[
\delta=x.
\]

The degenerating fourth scalar then has first coefficient

\[
\boxed{
q_x(S)+i(R_{01}-R_{10}).
}
\]

Taken alone, this coefficient mixes:

- the finite calibration-curvature part \(S\);
- the measurement first jet of the supported residue \(R\).

Thus an isolated diagonal scalar does not preserve the bi-Rees separation.

## Companion subtraction

The complete labelled packet also contains the nondegenerating
real-superposition measurement \(q_x\). Applied to the same regularized
curvature family, its first calibration coefficient is exactly

\[
q_x(S).
\]

Therefore the source-labelled difference is

\[
\boxed{
\bigl[q_{\rm diagonal}\bigr]_{x^1}
-\bigl[q_x(xK_x)\bigr]_{x^1}
=i(R_{01}-R_{10}).
}
\]

This is precisely the missing residue direction of Entry 1758.

## Narrow result

Diagonal specialization mixes support and readout filtrations, but the
complete labelled scalar packet carries its own canonical finite-part
subtraction. Consequently no filtered extension ambiguity remains after
retaining all source measurements.

The distinction is sharp:

- isolated diagonal scalar: insufficient;
- complete labelled packet: sufficient;
- fitted subtraction: unnecessary;
- new carrier stratum: absent.

## Durable artifacts

- research/benincasa/checkers/diagonal_parabolic_measurement_rees.rs
- research/benincasa/results/diagonal-parabolic-measurement-rees.json
- research/benincasa/diagonal-parabolic-measurement-rees.md

## Next falsifier

Delete the companion real-superposition measurement by a physical symmetry
or support restriction. Test whether another source effect supplies the same
finite-part subtraction; if none does, the diagonal packet should retain a
genuine rank-one filtered extension.
