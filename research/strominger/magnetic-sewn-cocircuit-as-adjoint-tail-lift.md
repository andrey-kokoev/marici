# The sewn cocircuit is an adjoint tail lift

Existing lift results identify the correct variance for the magnetic
separation-dependent cocircuit.

Partition a finite ordinary block into tail and boundary coordinates:

\[
F=
\begin{pmatrix}
A&B\\
C&E
\end{pmatrix},
\]

where \(A\) is the square invertible tail block. A left cocircuit
\((\lambda_t,\lambda_b)\) satisfies

\[
A^T\lambda_t+C^T\lambda_b=0,
\]

\[
B^T\lambda_t+E^T\lambda_b=0.
\]

The first equation uniquely lifts the boundary observer into the tail:

\[
\lambda_t=-A^{-T}C^T\lambda_b.
\]

Substitution gives the boundary condition

\[
(E-CA^{-1}B)^T\lambda_b=0.
\]

This is the adjoint counterpart of Kitaev's forcing-plus-endpoint tail lift.
It has exactly the properties required by the cocircuit atlas:

- the boundary state \(\lambda_b\) can have fixed dimension;
- its expanded support \(\lambda_t\) grows with the separation interval;
- invertibility of \(A\) removes the affine lift torsor;
- local lifts on overlapping intervals differ by left syzygies, whose triangle
  coherence is generated automatically;
- no separately fitted comparison cells are required.

The earlier magnetic theorem \(CA^{-1}B=0\) does not make this adjoint lift
trivial. It implies only

\[
(E-CA^{-1}B)^T=E^T.
\]

Thus the tail may carry a long nonzero observer profile while leaving the
boundary Fitting relation unchanged. This reconciles portal transparency with
the growing cocircuit widths.

## Transfers from existing research

- Kitaev: forcing plus an endpoint uniquely selects a one-sided tail lift;
  transposition supplies the observer version.
- Nima: differences of locally constructed lifts are syzygies and their
  overlap coherence telescopes automatically.
- Grothendieck: a global observer lift must precede scalar aggregation; a
  relative or line-valued target is appropriate when no global origin exists.
- Aspect: two-way auxiliary coupling changes the determinant unless the Schur
  correction is source-supplied; the vanishing magnetic correction is an
  established structural fact, not fitted compensation.
- Buzzard: matching one scalar incidence never selects the global lift or its
  pairing, so the adjoint recurrence and boundary anchor are both required.

## Immediate exact gate

For each current component block:

1. identify the maximal invertible ordinary tail block \(A\);
2. isolate its boundary matrices \(B,C,E\);
3. choose a primitive boundary cocircuit in \(\ker E^T\);
4. compute \(-A^{-T}C^T\lambda_b\);
5. verify that its support width equals the observed low/high formulas;
6. verify cutoff naturality on overlapping blocks by the generated syzygy
   differences.

A failure of invertibility, support agreement, or overlap compatibility would
falsify this lift as the explanation of the sewn cocircuit.
## Partition audit

The existing magnetic Schur extraction cannot be reused literally. It is
built from even pole depths, selected plus columns, and collision blocks with
\(q=g+d\). The current two-wedge problem uses consecutive depths, both
reflected branches, and arbitrary \(q\).

Likewise, the established Hall matching is source-natural on the even-depth
lattice but is not an authorized matching on the consecutive-depth extension.
The two-chart result still supplies the correct architecture: a preferred
source-labelled matching, with at most a small neighboring chart when its
coordinate vanishes.

The smallest missing constructor is therefore a consecutive-depth Hall
functor selecting \(A\) compatibly under cutoff enlargement. Once supplied,
the adjoint Schur formula is canonical and local lift comparisons are generated
syzygies. Without it, choosing pivot rows by Gaussian elimination would define
a computational chart, not a source-authorized lift.
## Density obstruction and required prequotient

At each consecutive depth the ordinary presentation adds two reflected branch
columns, while its union of target exponents grows by only one row. Hence no
large square tail block can contain all ordinary columns. A tail inverse is
ill-typed until the ordinary column-kernel relations have been quotiented or
a maximal independent presentation has been selected together with its
relation certificate.

The correct construction order is

\[
\text{ordinary branch presentation}
\longrightarrow
\text{kernel-relation quotient}
\longrightarrow
\text{source-natural Hall basis}
\longrightarrow
\text{adjoint tail lift}.
\]

The discarded branch combinations are not redundancy to erase silently; they
contain the tower relations. The consecutive-depth Hall functor must therefore
return both a maximal independent column set and the primitive relations of
its complement. This is the exact interface between the earlier kernel-tower
theorem and the new cocircuit lift.
