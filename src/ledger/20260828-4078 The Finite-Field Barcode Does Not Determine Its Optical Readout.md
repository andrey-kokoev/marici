# 4078 — The Finite-Field Barcode Does Not Determine Its Optical Readout

## Status

Established as an exact hostile test for the source-labelled interaction-net barcode packet of Entry 4076.

## Question

Does the finite-field barcode packet over \(\mathbf F_{32009}\), by itself, determine a lift-independent normalized optical analysis row?

## Frozen row

Take the first source-labelled first-death analysis row from Entry 4076. It has twenty nonzero coordinates.

Choose its balanced integer lift \(a\), with every residue represented in the interval centered at zero.

Choose a second integer lift \(b\) by adding \(32009\) to one nonzero coordinate of \(a\).

Then

\[
a\equiv b\pmod{32009},
\]

and both lifts have identical labelled support.

## Exact hostile witness

The two lifts are not projectively proportional. Their normalized rank-one projectors differ by exact squared Frobenius distance

\[
\frac{1593456739118751474}
     {1975509665708737985}>0.
\]

An explicit integer input \(w\), supported on the first two labelled coordinates, satisfies

\[
a\cdot w=0,
\]

while

\[
b\cdot w=110975203.
\]

Thus the same finite-field barcode row admits two characteristic-zero lifts for which one normalized optical analyzer reports a dark input and the other reports a nonzero response.

## Narrow theorem

The finite-field source-labelled barcode packet alone does not determine a characteristic-zero projective analysis row, normalized projector, or optical response.

Finite-field canonicity and chart covariance therefore do not imply lift-independent operational compilation.

## What this does not show

This does not prove that no canonical physical lift exists.

It proves that such a lift cannot be inferred from the finite-field packet alone. It must be supplied by additional source authority, for example:

- a characteristic-zero source reduction;
- an integral lattice;
- a polarization;
- a normalized period pairing;
- a physical instrument convention independently derived from the source.

## Consequence

The correct architecture is

\[
\text{finite-field barcode}
+
\text{source-authorized lift and normalization}
\longrightarrow
\text{operational network}.
\]

The second term is genuine data, not harmless presentation.

## Next falsifier

Derive one characteristic-zero lift directly from the frozen source relations and compare it with any independently derived integral or period-normalized lift.

Agreement up to the admitted physical gauge would establish operational canonicity. Disagreement would identify the missing normalization datum.
