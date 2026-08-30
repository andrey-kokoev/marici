# The Fourier–Tate jet shear is a frame connection, not a local invariant

## Question

Is the off-seam rank-one shear in the prolonged Fourier–Tate jet an intrinsic
obstruction, or can it be moved by changing the scalar source frame?

## Reflection transition

Write the scalar functional transition as

\[
F(s)=\gamma(s)F(1-s),
\]

with

\[
\gamma(s)\gamma(1-s)=1.
\]

Its first-jet shear is controlled by

\[
\operatorname{Im}\left(\frac{\gamma'}{\gamma}\right).
\]

## Source-frame change

Choose a nonvanishing scalar frame (b(s)) and define

\[
F_b(s)=b(s)F(s).
\]

The transition in the new frame is

\[
\gamma_b(s)
=
\frac{b(s)}{b(1-s)}\gamma(s).
\]

Writing

\[
\kappa(s)=\frac{b'(s)}{b(s)},
\]

its logarithmic derivative transforms as

\[
\frac{\gamma_b'}{\gamma_b}(s)
=
\frac{\gamma'}{\gamma}(s)
+\kappa(s)+\kappa(1-s).
\]

Therefore the off-seam shear coefficient is frame-dependent.

## Local trivialization

On a simply connected reflection-stable domain where (gamma) is nonzero and
has a single-valued logarithm (ell=\log\gamma), the cocycle law permits the
branch choice

\[
\ell(1-s)=-\ell(s).
\]

Set

\[
b(s)=e^{-\ell(s)/2}.
\]

Then

\[
\frac{b(s)}{b(1-s)}=\gamma(s)^{-1},
\]

and hence

\[
\gamma_b(s)=1.
\]

In this frame the prolonged jet action is bare reflection,

\[
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]

and the rank-one shear vanishes identically.

Thus the shear is locally a connection coefficient, not a frame-independent
obstruction.

## What remains invariant

The following data can obstruct a global trivializing frame:

1. zeros and poles of (gamma);
2. monodromy of its logarithm or square root;
3. incompatibility with the Real structure;
4. failure of cutoff frames to form one cocycle;
5. a frozen source normalization, vacuum, or tensor unit that forbids the
   required rescaling;
6. loss of continuity in the completed source topology.

The reflection sign on the Clark polarization also survives. Removing the
connection shear does not turn reflection into an isometry; bare reflection
remains an anti-isometry.

## Real-compatible gauges

If the frame respects the Real structure,

\[
b(\overline s)=\overline{b(s)},
\]

then on the fixed seam the quotient

\[
\frac{b(s)}{b(1-s)}
\]

has unit modulus. Such a gauge preserves the unitary seam property. An
arbitrary complex rescaling need not.

Therefore seam unitarity is stable under authorized Real gauges, while the
off-seam connection coefficient still changes.

## Consequence for positivity arguments

The sign or size of the raw off-seam shear cannot support an invariant
positivity theorem until the source frame is frozen. A proof must use one of:

1. the canonical Tate normalization and its derived connection;
2. a gauge-invariant holonomy or divisor statement;
3. a comparison between two independently fixed source frames;
4. a completed curvature whose transformation law cancels the frame term.

Choosing a gauge because it makes the shear favorable is unauthorized
fitting.

## Constructor interpretation

The scalar transition is a line-bundle cocycle. The first-jet shear is its
connection in a chosen frame. The ordered jet records both reflection and
connection. The determinant line records the cocycle and its global
holonomy. A scalar point value records neither reconstruction datum.

This explains why the coefficient lenses separate precisely at derivative
order one.

## Falsifier certificate

    {
      "code": "fourier_tate_shear_treated_as_frame_invariant",
      "original_transition": "gamma",
      "frame_change": "b",
      "new_transition": "b(s) gamma(s) / b(1-s)",
      "local_trivialization_available": true,
      "global_obstruction_not_yet_classified": true
    }

## Disposition

The off-seam rank-one Fourier–Tate jet shear is locally removable and must be
typed as a connection coefficient. The invariant frontier is global:
divisor, monodromy, Real structure, cutoff coherence, source normalization,
and completion.

## Claim boundary

This is a local holomorphic frame theorem away from zeros and poles. It does
not prove existence of a global Real-compatible square-root frame, authorize
a change of Tate normalization, or show that a completed connection has
bounded holonomy.
