# 4076 — The Interaction-Net Persistence Barcode Has a Source-Labelled Chart-Covariant Basis

## Status

Established over the frozen field \(\mathbf F_{32009}\) for the homogeneous interaction-net quotient presentations at \(K\)-depths \(3,4,5,6\), in the independently constructed \(G_{12}\) and \(G_{31}\) residue charts.

This entry upgrades the rank-only persistence profile of Entries 4026, 4034, 4039, and 4042 to an explicit source-labelled barcode packet.

## Frozen source objects

The construction retains:

- the exact depth-3 ordered source-label list of length \(4800\);
- the exact depth-4 ordered source-label list of length \(9120\);
- quotient reduction by the complete source exact relations;
- the source-derived \(G_{12}\to G_{31}\) chart map
  \[
  (i,j)\longmapsto(j,i)
  \]
  on retained fiber exponents;
- the Poincaré-residue orientation sign \(-1\);
- no fitted optical normalization or post hoc basis selection.

The durable export is:

'research/benincasa/results/interaction-net-barcode-basis-export-p32009.json'.

## Exact barcode basis

The depth-3 quotient has rank \(53\). An adapted source-labelled basis decomposes it as

\[
Q_3=D_4\oplus D_5\oplus P_6,
\]

where

\[
\dim D_4=20,\qquad \dim D_5=6,\qquad \dim P_6=27.
\]

The three blocks have exact meanings:

- \(D_4=\ker(T_{34})\): twenty first-death classes;
- \(D_4\oplus D_5=\ker(T_{35})=\ker(T_{36})\): six additional second-death classes;
- \(P_6\) complements \(\ker(T_{36})\): twenty-seven through-depth-6 survivors.

The transition ranks are

\[
\operatorname{rank}T_{34}=33,\qquad
\operatorname{rank}T_{35}=\operatorname{rank}T_{36}=27.
\]

Thus the kernel dimensions are \(20,26,26\).

## Depth-4 emergence

The depth-4 quotient has rank \(1386\).

The transported depth-3 image has rank \(33\). Greedy exact reduction in the frozen depth-4 source-label order produces a complementary emergence block of rank

\[
1386-33=1353.
\]

The export records all \(1353\) emergence rows explicitly. They are not inferred as unused labels: each row is admitted only when it raises the quotient span relative to the full transported image.

## Dual analysis rows

The packet includes:

- \(53\) dual rows for the adapted depth-3 basis;
- \(1353\) coordinate duals for the declared depth-4 emergence complement.

Exact finite-field pairing gives the identity on both blocks.

Therefore the packet supplies both synthesis and analysis data. It is sufficient for finite-field compilation of the barcode as a labelled linear network.

## Independent chart covariance

The \(G_{31}\) quotient presentations were reconstructed independently rather than obtained by transporting \(G_{12}\) matrices.

After applying the source-derived exponent swap and residue sign, the chart transports have ranks \(53\) and \(1386\) at depths \(3\) and \(4\), respectively.

They preserve \(20|6|27\) at depth \(3\), and \(33|1353\) at depth \(4\).

Hence the barcode filtration is occurrence-chart covariant. It is not an artifact of one serialized residue chart.

## Verification

The independent checker verifies:

- exact label counts \(4800\) and \(9120\);
- sparse-row normalization;
- adapted-basis rank \(53\);
- the \(20|6|27\) block counts;
- transition ranks \(33,27,27\);
- every declared death/survival condition;
- emergence rank \(1353\);
- both dual-pairing identities;
- chart ranks \(53,1386\);
- preservation of both chart flags.

Aspect's contract checker independently passes all synthetic hostile gates and reports the export shape valid.

## Narrow theorem

For the frozen interaction-net quotient family over \(\mathbf F_{32009}\), the depth-\(3\) through depth-\(6\) persistence profile admits an explicit source-labelled barcode basis whose death filtration, depth-\(4\) emergence complement, dual analysis rows, and \(G_{12}\leftrightarrow G_{31}\) chart transports satisfy all predeclared exact identities.

## Prohibited inference

The finite-field rows are not yet physical optical amplitudes.

A physical compilation still requires an independently chosen integral or complex lift, normalization, unitary dilation, and readout convention. None is supplied by the finite-field barcode theorem itself.

## Next falsifier

Construct two independently normalized characteristic-zero lifts of the same source-labelled packet and test whether their block-leakage and transition observables agree after the allowed physical gauge.

If they do not, optical behavior depends on extra lift data even though the algebraic barcode is canonical.

If they do, the source-labelled barcode may admit a lift-independent operational compilation.
