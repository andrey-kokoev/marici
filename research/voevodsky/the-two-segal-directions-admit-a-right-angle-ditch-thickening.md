# The two Segal directions admit a right-angle ditch thickening

## Question

Realize the two signed normal directions as literal half-planes meeting at a right angle, while preserving the reversal that exchanges the two path-space directions.

## Local embedding

Use the ambient Euclidean space \(\mathbb R^3\) with shared axis

\[
a=(1,0,0).
\]

Choose inward normal directions

\[
\nu_+=(0,1,0),
\qquad
\nu_-=(0,0,-1).
\]

The two half-planes are

\[
P_+=\{sa+t\nu_+\mid s\in\mathbb R,
\ t\geq0\},
\]

\[
P_-=\{sa+t\nu_-\mid s\in\mathbb R,
\ t\geq0\}.
\]

Their intersection is the shared axis. Since

\[
\langle\nu_+,\nu_-\rangle=0,
\]

their dihedral angle is \(90\) degrees.

## Reversal

Define

\[
R(x,y,z)=(x,-z,-y).
\]

Then \(R^2=1\), the axis is fixed pointwise, and

\[
R(P_+)=P_-,
\qquad
R(P_-)=P_+.
\]

Choose opposite induced orientations on the common axis. Their signed boundary contributions are \(+1\) and \(-1\), so the internal shared boundary cancels when the oriented half-planes are joined.

## Attachment to the 2-Segal object

Let \(X\) be the previously constructed 2-Segal object with simplicial reversal \(r\). Attach the local ditch by product:

\[
\widetilde X_n=X_n\times(P_+\cup P_-).
\]

The combined reversal is

\[
\widetilde r_n=r_n\times R.
\]

It exchanges the initial and final path-space directions while exchanging the two geometric half-planes. The simplicial identities remain those of \(X\); the Euclidean factor supplies the right-angle and orientation data.

## Disposition

A literal local \(90\)-degree embedding now exists. It is a product thickening of the 2-Segal model, so it proves compatibility rather than necessity: the 2-Segal laws neither determine nor forbid this angle. A source-derived metric would be required to make the Euclidean thickening intrinsic.

## Verification

```text
python research/voevodsky/checkers/check_right_angle_ditch_embedding.py
```

The checker verifies orthonormality, the right angle, reflection involutivity, axis fixing, half-plane exchange, 45 exact parameter samples, and cancellation of the two induced boundary signs.

Artifacts:

- `research/voevodsky/checkers/check_right_angle_ditch_embedding.py`
- `research/voevodsky/results/right_angle_ditch_embedding.json`
