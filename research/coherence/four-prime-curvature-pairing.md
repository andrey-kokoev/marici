# The four-prime curvature pairing is nonzero before scalar trace

## Face curvature

For axes \(p\ne q\), retain the complete mixed part of the boundary anticommutator:

\[
F_{pq}
=
\{d_p,h_q\}+\{d_q,h_p\}.
\]

This combines both orientations of the \(pq\) square and contains the half-line shift residuals \(K_{q,p}\) and \(K_{p,q}\). It is an even endomorphism of the exterior-label/seam packet.

## Oriented 4-cell pairing

For four ordered axes, the three partitions into two pairs carry the Pfaffian signs. Define

\[
\mathcal P_4
=
F_{01}F_{23}
-F_{02}F_{13}
+F_{03}F_{12}.
\]

This is the first expression that uses all four prime directions and pairs square curvature with square curvature. It is the discrete candidate behind the schematic notation \(F\wedge F\).

No commutativity of the \(F_{pq}\) is assumed. The displayed order is part of the definition; a cyclic or symmetrized refinement would be a separate constructor.

## Result

In the exact 272-dimensional finite exterior/seam model,

\[
\mathcal P_4\ne0.
\]

It acts nontrivially on ten basis columns. However,

\[
\operatorname{Tr}(\mathcal P_4)=0
\]

and

\[
\operatorname{Str}(\mathcal P_4)=0.
\]

Therefore the 4-cell information is present operatorially but is erased by both naive scalar traces in this contractible finite model.

This is a useful discriminator. The correct fourth-rank object cannot be assumed to be a scalar characteristic number. It may instead be:

- a supported boundary operator;
- a relative trace class;
- a determinant-line element;
- or a class surviving only after completion or pairing with an exposed boundary state.

## Structural reading

The explicit ladder is now

\[
D^2=0,
\qquad
F=DH+HD\ne0,
\qquad
[D,F]=0,
\qquad
\mathcal P_4(F)\ne0.
\]

Thus fourth rank does not merely restate Bianchi closure. It detects intersections between independently supported square curvatures. But scalarization at this stage loses the detected operator.

The next operation should be a source-authorized relative readout

\[
\rho_\partial(\mathcal P_4),
\]

retaining the half-line support windows. Fitting an ordinary trace after seeing \(\mathcal P_4\) would destroy precisely the boundary information responsible for its nonvanishing.

## Verification

Run:

```text
python research/coherence/check_four_prime_curvature_pairing.py
```

Artifacts:

- `check_four_prime_curvature_pairing.py`
- `four-prime-curvature-pairing.v1.json`
