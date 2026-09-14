# The four-front odd line closes endpoint trace faithfulness

Date: 2026-09-08

## Explicit evaluation

Prior research proves that the analytic four-front packet `b_p` has reciprocal
half-density trace

\[
\operatorname{Tr}_{\rm end}b_p=(-m_p,m_p),
\]

where, for `L=log p`,

\[
m_p=2e^{1/(16\pi)}\left(\sinh L-\sinh\frac L2\right)>0.
\]

Applying the uniquely forced endpoint comparison gives

\[
A_p(b_p)
=V_p^{-1}(-m_p,m_p)
=\frac{2m_p}{1-p^{-1}}(-1,1).
\]

It is nonzero for every prime and remains entirely in the reciprocal-odd line.
Therefore the analytic endpoint trace and the unique comparison `A_p` are
faithful on the strict four-front source line.  Reflection orientation and
prime labels are retained.

## Corrected frontier

The endpoint trace-faithfulness question is not globally open: it is closed on
the strict primitive/square analytic line needed by the local low-grade cell.
The next implication is the labelled arithmetic mate square.  One must prove
that the retained primitive/square Euler generator maps to this same odd line,
with the already forced coefficient

\[
\lambda_{p,\le2}^{(1/2)}
=\frac{-\kappa_p^{(\le2)}}{2s_p^{(1/2)}}.
\]

That theorem must preserve the primitive/square labels and exclude the
connected `k>=3` tail from this strict cell.  Scalar equality alone does not
establish the mate square.

The result does not assert faithfulness on the entire Adams source relation or
close the later radical/pushout gates.

## Evidence

- `check_marici_rh_four_front_endpoint_candidate_20260908.py`
- `marici_rh_four_front_endpoint_candidate_certificate_20260908.json`
- `research/nima/the-analytic-half-density-window-to-wronskian-leg-is-now-closed.md`
