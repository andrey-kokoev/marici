# Only a source-contracted supported complex can add noncircular off-seam information

## Candidate audit

The relative determinant line needs a gauge-invariant off-seam detector. Four candidates are available: a metric, a dual pairing, a logarithmic connection, and a Fredholm index. Three are insufficient by themselves, and the fourth must be support-sensitive.

## Metric does not control a section

A Hermitian metric makes section norms frame invariant, but it does not prevent a section from vanishing. The trivial line over \(\mathbb C\) with its standard positive metric carries the section

\[
\sigma(z)=z,
\]

which vanishes at the origin.

Moreover, on a contractible open half-plane a nonvanishing transition cocycle can generally be absorbed into a varying metric. Metric existence alone is therefore too flexible. The source would need an additional monotonicity or curvature law that forces the distinguished section away from zero. No such law is presently derived.

## A dual pairing reports rather than excludes zeros

Let \(L^\vee\) be a dual line with nonzero covector \(\lambda\). Then

\[
\langle\lambda,\sigma(z)\rangle
\]

vanishes whenever \(\sigma(z)\) lies in the kernel of the readout. In a one-dimensional nondegenerate pairing this is exactly when \(\sigma(z)=0\).

Thus a dual observer provides a gauge-invariant readout but no reason for nonvanishing. Proving that the pairing never vanishes is the original problem unless the dual is produced together with an independent conservation or contraction law.

## Connection periods are the divisor

For a nonzero local section,

\[
\nabla\log\sigma
\]

has integral periods around its zeros. This is gauge invariant because a nowhere-zero gauge changes the connection by an exact logarithmic term.

But the period is the divisor charge itself. Saying that every open-sector period vanishes merely restates zero-freeness unless a source law computes the connection before the section and forces those periods to vanish.

## Global index loses the required support

A reciprocal off-seam pair has opposite sector indices. Its total Fredholm index can be zero even though each open sector contains a defect. Quotienting by seam incidence can erase the same pair.

Character resolution is necessary but still insufficient if it forgets spectral support. The obstruction must be localized before integration:

\[
\operatorname{Ind}_{\mathrm{supp}}(\mathcal C)
\]

must distinguish seam-supported cohomology from reciprocal classes supported in the two open sectors.

Support cannot be assigned by inspecting the completed zero set. It must arise from the source carrier, such as valuation polarization, normal-distance filtration, boundary versus bulk stalks, or a source-defined sheaf of complexes.

## Surviving candidate

The only candidate that can add information rather than repackage the scalar section is a source-derived family of Fredholm or Koszul complexes

\[
\mathcal C_s=(E_s,d_s)
\]

with:

1. its determinant section derived functorially from \(\mathcal C_s\);
2. source-typed support over the seam and the two open sectors;
3. explicit contracting homotopies on the open sectors,

\[
d_sh_s^\pm+h_s^\pm d_s=1;
\]

4. reciprocal sewing transporting the two contractions;
5. completion preserving the contraction identity in the rigged topology.

Then an off-seam zero would create cohomology where the source already supplies a contraction. That is a genuine contradiction rather than a reformulation of winding or positivity.

## Why this remains difficult

A scalar family \(d_s=\Xi(s)\) would trivially have the desired determinant but would be constructed backward from the answer. It is inadmissible.

Likewise, the formal inverse \(h_s=d_s^{-1}\) cannot be declared on the open sectors, because its existence is precisely what must be proved.

The complex and homotopy must instead arise from labelled theta/Tate operations before scalar projection. The known doubled tail system is a possible beginning, but its completion, seam component, primitive/square incidence, and archimedean reservoir have not yet been assembled into one Fredholm complex.

## Finite falsifiers

- Positive metric plus \(\sigma(z)=z\): metric does not exclude a zero.
- Nondegenerate dual pairing plus \(\sigma(z)=z\): the pairing reproduces the zero.
- The connection \(d\log z\): its period detects the zero but does not forbid it.
- Sector indices \(+1\) and \(-1\): total index zero hides a reciprocal pair.
- A complex manufactured from the completed scalar section: determinant agreement is circular.
- A contraction defined as the inverse of the unknown differential: acyclicity is assumed.

## DPC

A proposed off-seam detector passes only if:

1. it is constructed from labelled source operations before the scalar section;
2. it retains support before any global index or seam quotient;
3. its determinant section is derived, not fitted;
4. its open-sector contraction is explicit and source-authorized;
5. the contraction survives restricted-product completion;
6. reciprocal sewing transports rather than identifies the two supported sectors;
7. hostile symmetric divisor multipliers fail to lift to the source complex.

## Outcome

Metric, dual-pairing, connection, and global-index routes do not independently explain RH. The unique surviving architecture is a source-derived, support-sensitive complex with canonical open-sector contractions. The exact construction gate is now the assembly of the existing tail, seam, cyclic arithmetic, endpoint, and archimedean pieces into that complex without using the completed scalar section.
