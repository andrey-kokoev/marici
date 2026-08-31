# The G4 chain map is an exact divisibility identity plus an invertible complement

## Theta Koszul differential

The completed theta object is the two-term complex

\[
K_\tau:
\mathcal L_\theta
\xrightarrow{\tau}
\mathcal O,
\]

where \(\tau\) is the source Mellin dual section.  Let the closed Green
boundary pencil be

\[
C(s):H_1\to H_0.
\]

A chain map from \(K_\tau\) to \(C\) consists of holomorphic maps

\[
i(s):\mathcal L_{\theta,s}\to H_1,
\qquad
w(s):\mathbb C\to H_0
\]

satisfying one square:

\[
C(s)i(s)=w(s)\tau_s.
\]

This is the exact source divisibility identity required before taking
determinants.

## Zero-to-state implication

If \(i(s_0)\) is injective and \(\tau_{s_0}=0\), then

\[
C(s_0)i(s_0)=0.
\]

For any nonzero \(\ell\in\mathcal L_{\theta,s_0}\),

\[
0\ne i(s_0)\ell\in\ker C(s_0).
\]

Thus the Xi zero produces a forward-derived Green-domain state.  No inverse
of \(\xi\) or inspection of its zeros enters the formula.

## Why the square alone is insufficient

The pencil may have additional kernel states unrelated to \(\tau\), and its
complement may carry extra determinant zeros.  To obtain bidirectional divisor
comparison, the chain map must split off the full noninvertible part.

Require holomorphic decompositions

\[
H_1=i(\mathcal L_\theta)\oplus Q_1,
\qquad
H_0=w(\mathbb C)\oplus Q_0
\]

with bounded projections, in which

\[
C(s)=
\begin{pmatrix}
a(s)\tau_s&c_{01}(s)\\
0&C_Q(s)
\end{pmatrix}.
\]

Here \(a(s)\) is a nowhere-zero scalar line isomorphism and
\(C_Q(s):Q_1\to Q_0\) is holomorphically invertible with locally uniform
inverse bounds.

A source-authorized triangular transformation may remove \(c_{01}\) because
\(C_Q^{-1}\) is bounded on the declared domain.

## Determinant consequence

The determinant functor then gives

\[
\det C(s)
=
E(s)\tau_s,
\]

where

\[
E(s)=a(s)\det C_Q(s)
\]

is holomorphic and nowhere zero in the corresponding relative determinant
line.

In a source scalar frame,

\[
\det C(s)=E(s)\xi(s).
\]

This is the desired G4 factorization with the unit derived from an invertible
operator complement.

## Multiplicity consequence

Over the local ring at \(s_0\), the triangular normal form splits the cokernel
module as

\[
\operatorname{coker}C
\cong
\mathcal O_{s_0}/(\tau)
\oplus0.
\]

Hence

\[
\operatorname{length}_{s_0}
\operatorname{coker}C
=
\operatorname{ord}_{s_0}\xi.
\]

Generalized parameter-root chains are preserved because the splitting and
complement inverse are holomorphic through \(s_0\).

## Reciprocal condition

The maps \(i,w\), the projections onto \(Q_1,Q_0\), and the complement inverse
must commute with Fourier--Poisson reciprocal transport.  Otherwise the
factorization may preserve scalar multiplicity while reversing or mixing the
boundary orientation.

## Existing candidate data

The retained architecture already offers typed candidates:

- \(i\): the full labelled theta source state lifted through incidence and
  history graphs;
- \(w\): the complete endpoint/response output vector;
- \(C\): the maximal-isotropic closed-loop boundary pencil;
- complement control: the five G3 margins before terminal scalarization.

What is not yet proved is the differential square

\[
Ci=w\tau
\]

on the complete three-stratum domain, or that G3 controls exactly its
complement rather than a different positive Gram.

## Reduced G4 test

The mapping-cone target is now equivalent to two concrete checks:

1. **divisibility:** compute \(Ci-w\tau\) and prove it vanishes componentwise
   in primitive, square, connected, seam, endpoint, and archimedean ports;
2. **complement:** prove \(C_Q^{-1}\) exists with cutoff-uniform completed
   bounds.

The first residual is a finite/source algebra calculation.  The second is the
operator completion theorem.  Until both vanish, no RH conclusion is
authorized.
