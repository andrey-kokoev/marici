# Reference-probe compression audit (WP384)

## Bounded question

Can a preparable low-valence probe convert WP383's formal degree-48
subtraction vertex into an executable detector response without importing new
selector authority?

## Augmented quadratic experiment

Introduce a reference probe $P$ mixed with the invariant residual channel.
At fixed momentum, write the inverse response kernel as

\[
\mathcal K=
\begin{pmatrix}D_P&h\\h&D_F\end{pmatrix}.
\]

Here $D_P$ is the calibrated probe kernel, $D_F$ is the composite-channel
kernel, and $h$ is the mixing normalization. Exact block inversion gives

\[
G_{PP}=\frac{1}{D_P-h^2/D_F}.
\]

Thus a two-point probe measurement can access the self-energy

\[
\Sigma_P=\frac{h^2}{D_F}.
\]

If $h$ is independently calibrated and nonzero, this readout reconstructs
$D_F$. The construction therefore compresses detector valence and provides
a conditional separator.

## Exact normalization kernel

Without an independent calibration of $h$, the transformation

\[
(h,D_F)\longmapsto(sh,s^2D_F)
\]

leaves the entire probe self-energy invariant. In particular, the distinct
packets $(h,D_F)=(1,1)$ and $(h,D_F)=(2,4)$ have identical readout. Algebraic
two-point access is not jointly faithful on the augmented source packet.

This is not an invariance of the original flavor experiment. Introducing and
calibrating $P$ defines a new relational experiment whose physical groupoid
is the stabilizer of the reference-port normalization. It does not recover an
absolute normalization belonging to the unreferenced experiment.

## Source-complexity boundary

Detector valence falls to two probe legs, but the microscopic mixing operator
is $PF$. Since $F$ has bifundamental field degree 24, the mixing vertex has
field degree 25. The construction therefore moves the high-degree interface
from the measured contact into the source coupling; it does not produce a
renormalizable microscopic completion.

The port also cannot select the value of $D_F$. It reads that value after
$h$ has been fixed. Consequently it is neither a numerical selector nor a
presentation rigidifier. It is a relational readout and conditional separator
on an augmented state domain.

## Disposition

WP384 supplies the exact lower-point matching map requested by WP383 but
leaves two gates: a source derivation of the degree-25 mixing and an
independent detector calibration of $h$. The smallest falsifier is the
normalization-equivalent hostile pair above.

Run `uv run --with sympy python
research/flavor/checkers/wp384_reference_probe_compression.py` to regenerate
the result.
