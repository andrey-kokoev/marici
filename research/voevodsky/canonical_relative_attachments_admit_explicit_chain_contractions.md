# Canonical relative attachments admit explicit chain contractions

## Question

Can vanishing relative homology at canonical cube grades be strengthened from a rank calculation to an explicit contraction of the newly attached chain package?

## Claim boundary

Exact chain contractions are constructed over the rationals for canonical attachments in dimensions three through eight. The chosen basis changes are additionally tested for unimodularity, which makes the contractions integral in the tested range. A uniform combinatorial formula for the contraction remains separate.

## Relative chain decomposition

Let \(C_\bullet^{(n)}\) be the relative chain complex of cells born at \(L_n\). Write

\[
B_k=\operatorname{im}d_{k+1}
\]

and choose a coordinate complement \(S_k\) to \(\ker d_k\). Acyclicity gives

\[
C_k^{(n)}=B_k\oplus S_k
\]

and an isomorphism

\[
d_k:S_k\xrightarrow{\sim}B_{k-1}.
\]

In these split bases, define

\[
h_{k-1}:B_{k-1}\longrightarrow S_k
\]

as the inverse of \(d_k|_{S_k}\), and set \(h\) to zero on \(S_{k-1}\). Then

\[
dh+hd=1.
\]

This does more than show that homology vanishes: it gives a constructor reducing every relative cycle to an explicit higher-dimensional filler.

## Relation to the attachment recurrence

The cell-rank polynomial is

\[
A_n(x)=(1+x)^{n-2}(1+x+x^2),
\]

while the boundary-rank polynomial is \(A_{n-1}(x)\). The identity

\[
A_n(x)=(1+x)A_{n-1}(x)
\]

is the dimension shadow of a contractible interval factor. An explicit contraction tests whether the actual arithmetic boundary complex realizes that shadow rather than merely sharing its Euler characteristic.

## Pyramid operation

Given a newly born relative cycle \(z\), the filler

\[
y=h(z)
\]

satisfies

\[
dy=z
\]

when \(dz=0\). Thus the contraction is a path-and-filler operation: it takes a surface or higher boundary relation and returns a canonical result relative to the selected splitting.

The splitting depends on ordered cell bases and pivot choices. The existence of a contraction is invariant; the selected filler representative is not yet canonical under all reorderings.

## Strongest falsification attempt

For dimensions three through eight, build the exact integer relative boundary matrices. Construct bases from boundary-image columns and coordinate complements selected by pivot columns. Require every combined basis matrix to be invertible, every differential block \(S_k\to B_{k-1}\) to be invertible, and the assembled maps to satisfy \(dh+hd=1\) in every degree. Test that all basis determinants and differential-block determinants are units, so the rational contraction does not hide torsion denominators in the tested range.

## Computed result

For every dimension from three through eight, the image-plus-coordinate-complement bases are unimodular, every restricted differential block has determinant \(\pm1\), and the assembled maps satisfy

\[
dh+hd=1
\]

in every degree. Thus each tested relative package has an explicit integral contraction; no rational denominator or torsion obstruction is hidden in the rank computation.

## Disposition

The canonical attachments admit explicit split-basis integral contractions through dimension eight. The contraction turns every relative cycle into a computed higher filler. The remaining task is a uniform combinatorial contraction independent of pivot choices.
