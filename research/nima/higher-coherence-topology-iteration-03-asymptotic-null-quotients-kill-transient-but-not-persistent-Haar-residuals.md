# Higher-coherence topology iteration 03: asymptotic-null quotients kill transient but not persistent Haar residuals

## Candidate topology

Encode a coherence tower by bounded stage sequences

\[
\ell^\infty(C_N)
\]

and quotient by an asymptotic null ideal, first in the standard corona model

\[
\mathcal Q
=
\ell^\infty(C_N)/c_0(C_N).
\]

A residual that is nonzero only at finitely many stages becomes zero. More
generally, any residual whose norm tends to zero is absorbed by the quotient.
This is a genuine topology in which higher cones can push transient errors to
infinity.

## Persistent fixed-prime class

Once stage `N_p` contains prime `p`, compatibility carries its Haar residual to
every later stage. In a fixed normalized coordinate it has tail

\[
(0,\ldots,0,r_p(z),r_p(z),r_p(z),\ldots),
\]

where

\[
r_p(z)
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)E_p(b_z).
\]

Its class modulo `c_0` is zero exactly when `r_p(z)=0`. Indeed, its distance to
the null ideal is `|r_p(z)|` in the scalar coordinate. Thus

\[
[r_p]_{\mathcal Q}=0
\quad\Longleftrightarrow\quad
r_p(z)=0.
\]

The quotient removes finite-stage bookkeeping errors but not a compatible
nonzero tail.

## Other asymptotic ideals

The same obstruction survives common variants:

- modulo finite-support sequences: a constant tail survives;
- modulo Cesaro-null sequences: its mean is `r_p`;
- modulo density-zero support: its support is cofinite;
- modulo rapidly decreasing tails: it is not decreasing;
- modulo compact vectors in a Calkin-type completion: its diagonal essential
  value remains `r_p`.

Any proper asymptotic ideal that retains the constant unit must retain this
persistent residual.

## What would kill it

To make the constant tail zero, the ideal must contain the unit in the
prime-`p` residual coordinate. Then it also kills every constant positive
energy tail, including the retained state norm

\[
(E_p(b_z),E_p(b_z),\ldots).
\]

The quotient can no longer distinguish the nonzero Xi state from zero. This
violates the required noncollapse and positivity hypotheses.

## Derived-limit possibility

A tower may have each finite residual exact while its normalized potentials
escape, producing a nonzero `lim^1` obstruction. Passing to a quotient can hide
the unbounded potentials, but it does not provide a bounded contracting
homotopy. Conversely, declaring the derived obstruction zero requires exactly
the compatible bounded higher filler that was missing.

Thus derived limits diagnose higher-coherence failure; they do not erase a
persistent scalar observation for free.

## Verdict for topology 3

Asymptotic-null quotient topologies are useful for discarding transient cutoff
artifacts and finite-stage cone choices. They do not absorb the compatible
relative-Haar residual unless they also annihilate the constant positive state
energy.

Hence this route yields a dichotomy:

1. retain the unit and retain the RH-strength residual;
2. kill the unit and lose faithful positive observation.

The next nonredundant topology to test is a weak/distributional topology in
which the residual may converge to zero against a restricted test class while
the state remains nonzero in a larger rigged carrier.