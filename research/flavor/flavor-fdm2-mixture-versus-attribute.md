# Branchwise CP breaking versus the mixed source state (WP96)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Two different output types

Let the two FDM-2 vacua be `omega_+` and `omega_-`, with CP exchanging them
and a faithful CP-odd quotient readout

\[
J(\omega_+)=J_0,qquad J(\omega_-)=-J_0,qquad J_0\ne0.
\]

The WP88 uniform orientation coin has two inequivalent interpretations:

1. a single-run branch record whose output lies in the attribute
   `{omega_+,omega_-}`;
2. the unconditioned source state
   `rho_mix=(omega_++omega_-)/2`.

The first is branchwise CP broken. The second is CP invariant. Every linear
CP-odd readout vanishes on it:

\[
\mathbb E_{\rho_{mix}}J=0,
\]

although the even fluctuation remains `E[J^2]=J_0^2`.

## Contextual partition

The odd-mean probe partitions the uniform broken mixture together with a
genuinely symmetric `J=0` source. The full branch-resolved outcome law
separates them: the mixture yields support at `+/-J_0`, while the symmetric
source yields a point mass at zero. This complementary information is legal
only if the source dynamics supplies a persistent domain/branch record and an
instrument can correlate the flavor readout with it.

No reference port reveals an absolute CP orientation. Conditioning on a
domain record defines a relational experiment over the stabilizer of that
record. Without conditioning, FDM-2 selects the CP-broken **support
attribute**, but not a CP-asymmetric ensemble state or a sign of `J`.

## Verdict and falsifier

Classification: branchwise **selector**, neither rigidifier nor selector of a
CP-asymmetric unconditioned state. The smallest exact falsifier of the latter
claim is the uniform two-point law itself: `E[J]=0` exactly.

Remaining instrument gate: demonstrate domain formation and persistence,
compile a domain-resolved flavor measurement, state its stabilizer groupoid,
and show that coarse graining, domain walls, or reset do not erase the branch
record before the canonical WP93 readout.

Verification: `uv run --with sympy python research/flavor/checkers/wp96_fdm2_mixture_attribute.py`.
