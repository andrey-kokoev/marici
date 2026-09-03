# Mixed-polarization probe depth depends on domain and instrument family

## Question

Does the two-probe minimum found for four pure polarization axes persist for mixed states?

## Claim boundary

This packet studies real-plane qubit Bloch vectors with exact rational coordinates and linear effect probes. It distinguishes a finite declared state census from the ambient mixed-state disk. It does not prove full complex-qubit tomography or noisy experimental identifiability.

## Typed state domain

Represent a real polarization density state by a Bloch vector

\[
r=(r_x,r_z),
\qquad
r_x^2+r_z^2\le1.
\]

For an admitted unit effect direction \(n=(n_x,n_z)\), the positive record is

\[
p_n(r)=\frac{1+n_xr_x+n_zr_z}{2}.
\]

Probe depth is relative to both a state domain \(D\) and an admissible instrument family \(\mathcal P\). It is the minimum cardinality of \(S\subseteq\mathcal P\) for which

\[
r\longmapsto(p_n(r))_{n\in S}
\]

is injective on \(D\).

## Finite rational census

Take nine states:

\[
(0,0),\ (\pm1,0),\ (0,\pm1),\ (\pm1/2,\pm1/2).
\]

All satisfy the positivity disk condition. With only axis probes

\[
X=(1,0),
\qquad
Z=(0,1),
\]

neither singleton is faithful, while \(\{X,Z\}\) records both Bloch coordinates and separates the census. Relative to this restricted instrument family, minimal depth is two.

Now admit the rational unit direction

\[
D=(3/5,4/5).
\]

On this particular nine-state census, the nine values of \(3r_x+4r_z\) are distinct. The single probe \(D\) is therefore faithful on the finite census. The earlier two-probe minimum is not intrinsic to the finite states; it depended on the candidate probe family.

## Ambient-domain obstruction

The same single probe is not faithful on the full mixed-state disk. The distinct valid states

\[
(0,0),
\qquad
(2/5,-3/10)
\]

have the same \(D\)-record because

\[
3(2/5)+4(-3/10)=0.
\]

Every single linear effect has a nontrivial kernel direction on the two-dimensional affine Bloch plane. Two linearly independent effects recover \(r_x,r_z\) and are jointly faithful on this restricted real-plane domain.

## Consequence for the probe programme

“Minimal probe depth” is not a property of a state set alone. It is typed by

\[
(D,\mathcal P,\text{record map},\text{admitted equivalence}).
\]

A finite generic probe can separate a prescribed finite census while remaining nonfaithful on the ambient state object. Finite separation must not be promoted to tomography without an ambient-domain injectivity proof.

## Falsifiers

1. Axis-only depth two is rejected if either axis probe separates the nine states.
2. Enriched-family depth one is rejected if the diagonal records collide on the census.
3. Ambient faithfulness of the diagonal probe is rejected by the explicit kernel pair.
4. Two-probe ambient faithfulness requires linearly independent effect directions.
5. A finite census result cannot authorize continuous-state reconstruction.

## Disposition

The pure-axis result does not extend unchanged. On the finite mixed-state census, depth is two for the axis-only family but one after admitting a generic rational effect. On the ambient real mixed-state disk, one scalar effect is never faithful and two independent effects suffice. Probe depth must always name its state domain and admissible instrument family.
