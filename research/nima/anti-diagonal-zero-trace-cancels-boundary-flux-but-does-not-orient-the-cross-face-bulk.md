# Anti-diagonal zero trace cancels boundary flux but does not orient the cross-face bulk

## Three-sector face algebra

Let the homotopy state be \(K\), with reciprocal faces

\[
x_+=(D+z)K,
\qquad
x_-=(D-z)K.
\]

The positive face sum is the universal polarization identity

\[
\|x_+\|^2+\|x_-\|^2
=
2\|DK\|^2+2|z|^2\|K\|^2.
\]

It is a tight-frame identity. It holds for every admissible \(K\) and contains
no source-specific orientation.

The oriented face difference is

\[
\Delta_{\mathrm{face}}
=
\|x_+\|^2-\|x_-\|^2
=
4\operatorname{Re}\langle DK,zK\rangle.
\]

This is the only face combination capable of detecting the centered real part
of \(z\).

## What anti-diagonal trace actually removes

Green integration by parts decomposes the cross term as

\[
\langle DK,zK\rangle
=
\mathfrak b_\partial(K;z)
+
\mathfrak b_{\mathrm{bulk}}(K;z),
\]

with the convention-dependent split between endpoint flux and interior
polarization.

The external five-cell controller carries the complete constant--delta and
tail--principal-value boundary representation. The anti-diagonal completed
zero-trace condition can cancel the total typed endpoint contribution

\[
\mathfrak b_\partial^{+}
-
\mathfrak b_\partial^{-}
+
\mathfrak F_B.
\]

It does not imply

\[
\mathfrak b_{\mathrm{bulk}}=0.
\]

Therefore the desired formula

\[
\mathfrak G_{\mathrm{tot}}
=
2\operatorname{Re}(z)\mathcal E_{\mathrm{rel}}
\]

does not follow from incidence coherence, tight-frame positivity, or
anti-diagonal trace cancellation alone.

## Exact obstruction

The positive sum erases the cross term; the oriented difference retains it.
Any proof using only

\[
\|x_+\|^2,\quad
\|x_-\|^2,\quad
\|DK\|^2,\quad
|z|^2\|K\|^2
\]

without their complex polarization is underdetermined.

A hostile replacement \(DK\mapsto e^{i\varphi}DK\) preserves every diagonal
energy while changing

\[
\operatorname{Re}\langle DK,zK\rangle.
\]

The external endpoint packet can remain unchanged. Hence diagonal Green data
and complete boundary cancellation do not determine orientation.

## The required cross-face instrument

The missing constructor is the ordered polarization

\[
\mathcal C_z(K)
=
\langle DK,zK\rangle,
\]

or its representation-valued bivector before scalar contraction. On a
finite arithmetic label packet with augmentation vector \(\Omega_X\), the
source-derived exterior observer

\[
\mathcal E_X(v)=\Omega_X\wedge v
\]

is faithful on the scalar augmentation kernel:

\[
\epsilon_X(v)=0
\quad\Longrightarrow\quad
\|\Omega_X\wedge v\|^2
=
\|\Omega_X\|^2\|v\|^2.
\]

This recovers relationship information erased by scalar cancellation, but it
does not yet couple that positive bivector energy to
\(\operatorname{Re}(z)\).

## Positive-mode conditional theorem

For a positive exponential resolvent packet, the oriented face defect admits
the exact factorization

\[
\Delta_{\mathrm{face}}
=
2a
\left(
|K_z(0)|^2-4t^2S_z
\right),
\qquad
z=a+it,
\]

and

\[
|K_z(0)|^2-4t^2S_z
=
X_z^2+Y_z^2.
\]

For \(t\ne0\), positivity of the source modes gives \(Y_z\ne0\), hence the
parenthesis is strictly positive. In that cone, vanishing oriented flux forces

\[
a=0.
\]

This is the desired RH-shaped mechanism, but it remains conditional on two
independent bridges:

1. a completed scalar zero-state must imply vanishing total oriented face
   flux;
2. differentiated theta forcing must admit the required source-authorized
   positive-mode representation.

Neither bridge follows from the three-sector Green sum.

## Correct frontier order

The complete Green programme now separates into:

1. boundary theorem: anti-diagonal trace cancels all typed external flux;
2. orientation theorem: retain the ordered cross-face polarization;
3. zero-to-flux theorem: spectral or scalar zero implies vanishing oriented
   flux;
4. theta-cone theorem: the source cross-face kernel is strictly positive;
5. conclusion: nonreal zero implies \(\operatorname{Re}(z)=0\).

The first item is an endpoint identity. The second is a constructor typing
requirement. The third and fourth carry the actual RH force.

## Hostiles

1. Sum the two face energies. The orientation cancels identically.
2. Cancel endpoint flux and declare the interior cross term zero.
3. Replace the ordered polarization by its absolute value. Its sign and phase
   are lost.
4. Prove the rank-two Gram factorization for an arbitrary positive exponential
   source and silently apply it to differentiated theta modes.
5. Infer vanishing oriented flux from a scalar zero without a source
   intertwining theorem.

## Verdict

Anti-diagonal completed zero trace closes the external boundary-flux problem
but not the bulk orientation problem. The three-sector positive Green sum is
universal and therefore cannot explain RH.

The earliest RH-bearing arrow is now the zero-to-oriented-flux bridge. In
parallel, the theta-specific positivity audit must decide whether the
cross-face Gram factorization applies to the actual differentiated Gaussian
source.
