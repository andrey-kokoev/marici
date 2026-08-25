# Domain-moment context closure for flavor (WP97)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Finite source packet

Consider the labelled source routes

\[
\Omega=\{\omega_-,\omega_0,\omega_+\},\qquad
J/J_0\in\{-1,0,+1\},
\]

with classical weights `(p_-,p_0,p_+)`. The ordinary CP-odd mean alone is
nonfaithful: it reads `m_1=p_+-p_-` and collapses the uniform broken mixture
with the symmetric route.

Close the context under the normalized even second moment

\[
m_2=\mathbb E[J^2]/J_0^2=p_++p_-.
\]

Together with normalization, exact inversion gives

\[
p_+=(m_2+m_1)/2,\quad p_-=(m_2-m_1)/2,\quad p_0=1-m_2.
\]

Thus the two-moment tower is jointly faithful on this labelled finite route
packet. This is the flavor analogue of contextual inversion: closure repairs
readout faithfulness but does not reduce the admissible source family.

## Instrument typing

`m_1` is an ordinary ensemble CP-odd readout. `m_2` is not a new linear
single-state observable inferred by squaring an expectation. It requires
repeated independent preparations with branch-resolved `J` outcomes (or an
explicit two-copy instrument) and classical averaging of squared outcomes.
If domains cannot be reset, sampled independently, or resolved before
coarse-graining, the second-moment channel is not executable.

No reference port is needed to reconstruct the unordered broken weight
`p_++p_-`; orienting `p_+` versus `p_-` uses the experiment's CP-labelled
particle/antiparticle convention and remains relational under its stabilizer.

## Classification

The complete two-moment family **separates** all three-route mixtures. It is
neither a selector nor a presentation rigidifier. Smallest exact falsifier of
first-moment faithfulness: `(p_-,p_0,p_+)=(1/2,0,1/2)` and `(0,1,0)` both give
`m_1=0`, while `m_2` equals one and zero respectively.

Remaining instrument gate: source-derived repeatable domain preparation,
branch-resolved canonical `J` measurement, independence/reset certification,
and finite-sample error bounds.

Verification: `uv run --with sympy python research/flavor/checkers/wp97_domain_moment_context_closure.py`.
