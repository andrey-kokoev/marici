# The dyadic k-successor subdivides terminal bulk isometrically and does not add positive capacity

## Audit result

The proposed recursion

\[
C_{k+1}=S_k^*C_kS_k+Y_k^*Y_k
\]

is not the recursion implemented by the existing dyadic Halmos refinement if
\(S_k^*C_kS_k\) is meant to retain the entire old bulk. That would double-count
the part of the old terminal slot used to create the new defect row.

## Exact refinement

At depth \(k\), separate the persistent slots from the current terminal bulk
slot:

\[
X_k u=(A_ku,z_ku).
\]

For the relevant positive contraction \(T_k\), the next stage is

\[
\boxed{
X_{k+1}u=
\left(
A_ku,
T_kz_ku,
(I-T_k^2)^{1/2}z_ku
\right).}
\]

The terminal splitting map

\[
W_{T_k}z=
(T_kz,(I-T_k^2)^{1/2}z)
\]

is an isometry because

\[
W_{T_k}^*W_{T_k}
=T_k^2+(I-T_k^2)=I.
\]

Consequently

\[
\boxed{X_{k+1}^*X_{k+1}=X_k^*X_k.}
\]

The new defect square is paid for by shrinking the old terminal bulk:

\[
\|z_k u\|^2
=
\|T_kz_ku\|^2+
\|(I-T_k^2)^{1/2}z_ku\|^2.
\]

It is not additional positive capacity.

## Symmetry completion

Applying the pyramid symmetries produces the corresponding orbit of terminal
splittings, but each orbit member obeys the same conservation law. Therefore
symmetry completion refines the presentation of the Gram; it does not add a
new positive Gram to it.

With signs copied to every descendant, the signed readout is also preserved:

\[
R_k^*R_k=I,
\qquad
R_k^*J_{k+1}R_k=J_k.
\]

Thus the correct statement is

\[
\boxed{
(k+1)\text{-state}
=
\text{an isometric subdivision of the }k\text{-state},}
\]

not “the old state plus a new positive shell.”

## Consequence for the 4-simplex idea

The 4-simplex still expresses coherence of “refine then fill” versus “fill then
refine,” but its dyadic fifth face has zero net Gram increment. Hence it cannot
by itself prove

\[
C_k-\beta_k^*\beta_k\succeq0
\]

by monotone accumulation of defect squares.

The previous base-case-plus-positive-increment proposal is therefore withdrawn
for the existing dyadic \(k\)-axis.

## Where a genuine increment may occur

Positive accretion can only come from a non-isometric direction, such as:

- enlarging the physical cutoff window;
- adjoining a conductor/place with its source-derived energy weight;
- enlarging the endpoint graph norm;
- adding an independently normalized bulk channel.

If the intended \(k\)-axis denotes one of those operations rather than dyadic
Halmos depth, its successor law must be written separately and its positive
increment proved from that operation.

## Correct remaining use of dyadic refinement

Dyadic refinement remains valuable because it:

1. exposes exact endpoint atoms and generic-angle defect rows;
2. preserves positive and signed Grams exactly;
3. makes terminal-tail estimates explicit;
4. commutes with conductor restriction at fixed cutoff.

It localizes the Schur inequality into microscopic rows but does not create the
inequality.
