# Cyclic theta stabilization rigidly selects the boundary phase

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact phase-rigidity theorem with an open source bridge

## The distinction that removes the phase family

A maximal abelian Weyl algebra together with a cyclic theta vector does not
select a Cayley phase if the vector is merely observed. The result changes if
the boundary unitary must stabilize that vector.

Let

\[
M\cong L^\infty(Y,\mu)
\]

act by multiplication on \(L^2(Y,\mu)\), and let \(\Omega\) be cyclic for
\(M\). Cyclicity means \(\Omega(y)\ne0\) almost everywhere. For a unitary
multiplier \(U=M_u\), the stabilization equation

\[
U\Omega=\Omega
\]

implies

\[
(u(y)-1)\Omega(y)=0
\]

almost everywhere. Hence \(u=1\) almost everywhere and \(U=1\).

## What this explains

Observation retains an entire phase circle. Stabilization collapses it to a
single phase. The missing fifth relation may therefore be neither another
state nor another positivity form. It may be an incidence law saying that
the rational boundary transport fixes the completed theta vacuum.

In geometric-algebra language, the plane and rotor family are already
present. A fixed spinor selects the identity rotor in its stabilizer.

## Source bridge still required

The theorem does not authorize the stabilization equation. The theta/Tate
construction must independently prove that its rational boundary unitary
fixes the completed theta state. It is insufficient that:

- the state is cyclic;
- the state is Fourier invariant; or
- its scalar matrix coefficient satisfies a functional equation.

The required equation must hold before determinant compression and across
the primitive, square, seam, and archimedean channels.

There is also a chart issue. The selected unitary is the identity, which lies
at the pole of the ordinary inverse Cayley formula. It should therefore be
kept as a closed Lagrangian graph relation rather than forced into an
unbounded operator chart.

## Sharp falsifier

Find a nonidentity unitary in the source boundary algebra that fixes the full
completed theta state. If the theta vector is genuinely cyclic, none exists.
If such a unitary is found, then either the vector is not cyclic on the true
boundary algebra or the declared algebra has hidden multiplicity.

The latter possibility is important: with spectral multiplicity greater than
one, a vector can be cyclic only after the multiplicity space is included.
Thus the next audit is whether the completed theta vacuum is cyclic for the
full rational Weyl boundary algebra, not merely for its scalar quotient.

## Scope

Phase rigidity under cyclic stabilization is exact. Its application to the
adelic theta boundary remains conditional on deriving both cyclicity and the
stabilization equation from the labelled source.

## Verification

The checker solves the stabilizer equations on a finite full-support spectral
chart and obtains only the identity phase.
