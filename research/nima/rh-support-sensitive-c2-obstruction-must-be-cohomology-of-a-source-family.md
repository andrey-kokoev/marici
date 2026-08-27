# A support-sensitive C2 obstruction must be cohomology of a source family

## Why labels cannot simply be assigned spectral support

A labelled source atom such as

\[
e^{-s\log n}
\]

is entire in the spectral parameter. Nonzero holomorphic source contributions
do not live at isolated spectral points. Their ordinary sheaf support is the
whole connected domain.

Therefore an off-seam support label cannot be attached directly to a prime,
prime power, seam current, or archimedean term. Isolated spectral support arises
only after those globally analytic contributions interact and a family map
loses exactness.

## Minimal algebraic model

Over a function ring `O`, a scalar section `f` defines the two-term Koszul
complex

\[
0\longrightarrow O
\xrightarrow{\;f\;}
O\longrightarrow0.
\]

Its cokernel is supported on the divisor of `f`. For

\[
f(z)=(z-a)(z-(1-a)),
\]

the cohomology has two localized components, one at each reciprocal point.
Unlike a global integer index, this support-sensitive object does not identify
the pair with a seam class.

But using `f=Xi` as the differential is tautological. It manufactures the
desired support directly from the scalar zero set and explains nothing.

## Source-derived replacement

The only noncircular version is a family complex

\[
\mathcal C_{\mathrm{src}}(s)

=

\left(
\cdots\longrightarrow E^{-1}(s)
\xrightarrow{d_{-1}(s)}
E^0(s)
\xrightarrow{d_0(s)}
E^1(s)
\longrightarrow\cdots
\right)
\]

whose bundles and differentials are generated from labelled theta/Tate
operations before the completed scalar is formed.

The determinant or torsion of this complex may then produce the scalar section,
while its cohomology sheaf records the locus where exactness fails.

## Relative seam triangle

Let `C_seam` be the independently retained seam complex with source-derived
incidence into `C_src`. Define the bulk-relative complex by the cone

\[
\mathcal C_{\mathrm{bulk}}
=
\operatorname{Cone}
\left(
\mathcal C_{\mathrm{seam}}
\longrightarrow
\mathcal C_{\mathrm{src}}
\right).
\]

Then the RH-shaped statement is

\[
\mathcal H^*(\mathcal C_{\mathrm{bulk}})
\big|_{\Re s\ne1/2}=0.
\]

This says that all cohomology is accounted for by the seam carrier and no bulk
support remains.

## Exact point of circularity

The preceding vanishing statement is still equivalent in strength to the
desired zero confinement unless the programme constructs a canonical
contracting homotopy

\[
d_sh_s+h_sd_s=1
\]

on each open half-plane from source operations.

The determinant bridge and contraction must both be forward-derived:

- the determinant bridge connects cohomology to the completed scalar;
- the contraction proves bulk exactness independently of that scalar.

Without the bridge, acyclicity says nothing about zeros. Without the
contraction, the cohomology sheaf merely repackages the divisor.

## C2 interpretation

The support-sensitive fifth tower is not a set of point labels. It is a
derived family whose higher cells are homotopies between source differentials.
Its obstruction is emergent cohomology. The seam coherencer is an actual map of
complexes, and the next-rung residue is the cohomology of its cone.

This recovers the puncture intuition in its non-topological form:

- an off-seam zero is not merely a puncture in a scalar line;
- it must correspond to an unpaired state of a source-derived family complex;
- a canonical half-plane contraction would make that state impossible.

## DPC

Require, in order:

1. source-derived bundles or modules;
2. source-derived differentials squaring to zero;
3. the retained seam subcomplex;
4. ordered incidence as a chain map;
5. a determinant or torsion bridge to the completed scalar;
6. an explicit contraction on both open half-planes;
7. continuity of the contraction through restricted-product completion;
8. rejection of central multipliers and reciprocal off-seam pairs.

Reject:

- the scalar Koszul complex with differential `Xi`;
- support labels inferred from scalar zeros;
- a complex fitted so that its determinant is `Xi`;
- finite-cutoff contractions without equicontinuity;
- a seam quotient lacking a chain-level incidence map;
- global Euler characteristic used in place of supported cohomology.

## Verdict

The sheafified relative-index route converges to one precise architecture: a
source-derived relative Fredholm or Koszul family whose bulk cone is
canonically contractible off the seam. This is structurally capable of proving
RH, but every RH-bearing part lies in the still-missing source differential,
determinant bridge, and completion-stable contraction.

