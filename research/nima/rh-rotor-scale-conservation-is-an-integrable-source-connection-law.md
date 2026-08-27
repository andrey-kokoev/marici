# Rotor scale conservation is an integrable source-connection law

## Rank-one spectral comparison

Let \(A_X(s)\,ds\) be the source-derived determinant-line connection one-form
at cutoff \(X\). Along a spectral path \(\gamma:[0,1]\to S\), let

\[
\frac{dT_X}{d\lambda}
=
A_X(\gamma(\lambda))\gamma'(\lambda)T_X(\lambda),
\qquad
T_X(0)=1,
\]

where \(\lambda\) is a path coordinate with no temporal role currently
declared. Write

\[
T_X(t)=\rho_X(t)R_X(t),
\]

where \(R_X\) is a unit rotor. Then

\[
\log\rho_X(1)-\log\rho_X(0)
=
\operatorname{Re}\int_\gamma A_X(s)\,ds.
\]

The phase and scale problems have separated. Rotor coherence controls the
imaginary part of the connection. Nonvanishing is controlled by the real
part.

## Sufficient completion theorem

Suppose on every compact path family inside one open half-plane:

1. \(A_X\) is derived from the marked source germ without division by the
   completed section;
2. the path integrals of \(A_X\) converge as the cutoff grows;
3. the real path integrals have one cutoff-independent lower bound;
4. the basepoint scale is source-normalized and nonzero.

Then \(T_X\) converges to a nonzero conformal rotor comparison. The determinant
section obtained by applying that comparison to the basepoint state cannot
vanish along the path.

The theorem is elementary. Its force lies entirely in deriving the connection
and the lower bound from source operations.

## Three-stratum connection

The connection coefficient must be assembled before scalar completion from
the coupled boundary packet:

\[
A_X
=
A_{1,X}
+
A_{2,X}
+
A_{\ge3,X}
+
A_{\infty,X}
+
A_{0,X}.
\]

The connected order-three tail is the convergent part. Primitive, square,
archimedean, and zero-frequency terms must cancel their divergences at the
connection level while retaining their separate types. Cancellation only
after exponentiating a fitted scalar does not construct the comparison.

## Reciprocal cancellation is insufficient

Let the two reciprocal sector log-scales be \(L_X^+\) and \(L_X^-\).
Reciprocal sewing may force

\[
L_X^++L_X^-=0.
\]

This permits

\[
L_X^+\longrightarrow-\infty,
\qquad
L_X^-\longrightarrow+\infty.
\]

The paired scale remains one while the first sector collapses. The required
law is a lower bound for each source-directed comparison, not merely a conserved
sum.

## Noncircularity gate

The formal scalar connection

\[
A=\frac{\sigma'}{\sigma}
\]

is prohibited. Its regularity is equivalent to the desired zero exclusion.
The connection must instead descend from an operator-valued spectral
comparison on the
constructor-closed marked germ, with its determinant-line coefficient obtained
by an authorized trace, supertrace, or boundary-anomaly operation.

## Smallest falsifiers

Reject the scale-conservation route when:

1. the real connection integral tends to negative infinity although every
   finite comparison is invertible;
2. reciprocal log-scales cancel only after one collapses and the other
   diverges;
3. the connection is reconstructed from the scalar section;
4. primitive and square divergences are erased before the archimedean boundary
   relation acts;
5. cutoffwise lower bounds have no compact-uniform constant.

## DPC verdict

The rotor proposal reduces RH to one source theorem: construct the induced
determinant connection and prove a compact-uniform lower bound on its real path
integrals in each open half-plane. Phase sewing, finite invertibility, and
reciprocal scale cancellation do not imply that bound.

## Verification

`check_rh_rotor_connection_scale.py` verifies a summable connection with a
uniform nonzero scale, a harmonic connection whose finite transports collapse,
and reciprocal cancellation that hides the collapse exactly.
