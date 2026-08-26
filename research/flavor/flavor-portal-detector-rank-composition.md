# Portal-detector rank composition

Work package: WP576  
Owner: marici.Figueiredo

## Admitted source surface

Freeze the universal portal domain

\[
z>0,
\qquad
\lambda_s>0,
\qquad
\lambda_H>0.
\]

Use the invariant source readouts already derived in WP561--WP562,

\[
r=z,
\qquad
q={\lambda_s z^2\over\lambda_H}.
\]

Their Jacobian with respect to the independently labelled source coordinates
((z,\lambda_s)) is

\[
A=
\begin{pmatrix}
1&0\\
2\lambda_s z/\lambda_H&z^2/\lambda_H
\end{pmatrix},
\qquad
\det A={z^2\over\lambda_H}.
\]

Unlike the order labels in WP575, these are two coordinates of an admitted
source parameter surface. The entrance has rank two throughout the nonzero-
mixing domain and collapses exactly at (z=0).

## Conditional completed detector composition

Let the completed detector response be WP574's exact normalized tangent

\[
D=
\begin{pmatrix}
1&0\\
-1&1\\
0&-1
\end{pmatrix}.
\]

If, and only if, a named physical interface identifies its two input columns
with the invariant ((r,q)) responses in a common frame, the composed source
response is (DA). With the identity detector metric,

\[
\det((DA)^TDA)={3z^4\over\lambda_H^2}>0.
\]

The positivity restriction is inherited from boundedness of the declared
singlet quartic on its isolated large-field ray. Thus no algebraic rank
obstruction remains off \(z=0\). Null deletion or free
exposure profiling can still erase a direction as in WP574; retaining the
completed record or adding calibrated exposure preserves the conditional rank.

## Authority boundary

This composition is a typed acceptance theorem, not an admitted flavor
instrument. The present artifacts separately authorize (A) as an invariant
source-coordinate map and (D) as a detector theorem. They do not authorize
the equality between the detector input frame and the ((r,q)) frame.

The missing arrow is a publication-bound portal likelihood or calibrated
transport (K) from variations in (r,q) to completed detector records. A
formal substitution (K=D) is not evidence that the experiment implements
that channel.

The smallest exact physical-domain falsifier is (z=0): the quartic column
vanishes and the composed Gram determinant is zero. The smallest authority
falsifier away from that boundary is any two detector transports that agree on
the released calibration slice but have different pullbacks along (q), as
already constructed in WP565--WP566.

## Classification

The portal surface supplies a faithful rank-two source entrance on (z>0),
not a selector. WP574 supplies a conditional rank-two completed detector
architecture, not a flavor-specific instrument. Their formal composition is
both separating and weak-basis invariant, but remains physically uninstantiated
until the common-frame interface is derived and calibrated. No presentation
rigidifier or absolute reference recovery is involved.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp576_portal_detector_rank_composition.py

The generated result is
`research/flavor/results/wp576_portal_detector_rank_composition.json`.
