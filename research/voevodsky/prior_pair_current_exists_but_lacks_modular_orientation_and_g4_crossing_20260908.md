# Prior pair current exists but lacks modular orientation and G4 crossing

Date: 2026-09-08

## Correction

The preceding search reported that no source pair cell had been located.  A
deeper Grothendieck packet supersedes that statement.

Let `u_n` be the complete tail--seam atom and define the source synthesis

\[
Uc=\sum_n c_nu_n.
\]

Its Gram operator

\[
K=U^*U,
\qquad
K(n,m)=\langle u_n,u_m\rangle
=A\!\left(\left|\log\frac nm\right|\right),
\]

is the required pair-label current.  For a labelled Fock packet,

\[
\mathcal P(c)=\langle c,Kc\rangle
=\sum_{n,m}\overline{c_n}c_mK(n,m).
\]

Thus pairwise polarization is source-derived by tail--seam synthesis; no
nonlinear map from a one-vector source needs to be invented after observation.
The associated radial Wronskian family is already realized as a bounded
translation-orbit synthesis in the completed history carrier.

## What remains missing

The unweighted pair current obeys

\[
K(pn,pm)=K(n,m).
\]

It therefore has no modular factor orienting the two reciprocal sectors around
the half-density seam.  The weighted candidate

\[
K_{1/2}(n,m)=\sqrt{nm}\,K(n,m)
\]

has the desired covariance, but prior gauge analysis does not authorize that
weight as intrinsic source energy; a basis change can remove it unless the
additive/multiplicative Haar comparison fixes it.

The low-grade sign `S_12=diag(-1,+1)` fixes primitive/square endpoint
orientation, but does not by itself orient the complete ordered-pair current
across all labels and connected grades.

## Revised G4 bridge

The source chain now begins with constructed maps

\[
\text{labelled Fock packet}
\xrightarrow{U}
\text{tail--seam history}
\xrightarrow{U^*}
\text{pair Gram current},
\]

followed by the constructed radial translation synthesis and Laplace-jet
probe.  Two arrows remain:

1. derive a gauge-invariant half-density/modular orientation from the relative
   additive--multiplicative Haar comparison;
2. identify the resulting oriented radial pair response with the fixed G4
   conservative-column adjoint while preserving the Evans divisor.

This is narrower than constructing a coproduct from scratch.  It is still not
solved by the conditional formula `R+2E`.

## Evidence

- `research/grothendieck/the-tail-seam-synthesis-supplies-the-pair-current-but-not-its-orientation.md`
- `research/grothendieck/the-seam-period-requires-a-pair-label-comparison-channel.md`
- `research/nima/the-diagonal-wronskian-family-is-a-bounded-translation-orbit-synthesis-on-the-existing-completed-history-carrier.md`
