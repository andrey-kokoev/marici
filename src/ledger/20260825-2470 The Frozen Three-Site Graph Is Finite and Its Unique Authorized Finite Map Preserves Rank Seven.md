---
author: marici.Benincasa
date: 2026-08-25
---

# 2470 — The Frozen Three-Site Graph Is Finite and Its Unique Authorized Finite Map Preserves Rank Seven

## Question

Classify the source-authorized finite-renormalization maps of the one-loop
three-site marked-relative system and determine their action on the
rank-seven interaction quotient.

Sequence claim: `seqclaim-5732c7ec015ec87059c1023c`.

## Initial source audit

The primary source, arXiv:2408.16386v2, defines a regulated twisted-period
family.  Its general equation (6) omits coupling-dependent factors and leaves
the numerator degree and polynomial interaction variable.  It contains no
action-level counterterm basis or finite renormalization condition.

At the level of cyclic loop polynomials, covariance and normalization leave
the two-plane

\[
\left\langle
C_4=L_1+L_2+L_3,
\quad
C_2=D_1+D_2+D_3
\right\rangle.
\]

These functions depend on the loop coordinates (a,b,c).  They are not
spacetime-local counterterms and cannot be quotiented as scheme freedom.  A
local counterterm enters through the loop-independent contact port.  The
fixed-cycle audit gives

\[
\operatorname{rank}(\text{responses})=10,
\qquad
\operatorname{rank}(1\oplus\text{responses})=11,
\]

so that contact port has zero intersection with the interaction-response
image.

## Graph-local finiteness

That conditional ambiguity is not active for the frozen graph itself.  On
the source physical cycle

\[
\Gamma_\ell=\mathbb R^3,
\]

the weakest density used by the complete rank-seven score test is

\[
\rho(\ell)
=
\frac{1}{q_{\mathfrak g_1}q_{\mathfrak g_2}
q_{\mathfrak g_3}q_{\mathcal G_{23}}}.
\]

For generic positive nonsoft energies, every wall is positive and grows
linearly with (r=|\ell|).  Therefore

\[
d^3\ell\,\rho(\ell)=O(r^{-2})\,dr
\]

at infinity.

The normal derivatives required by the interaction tower do not worsen this
infinity degree.  At a moving norm center, the worst third normal derivative
is (O(r^{-2})), integrable against (r^2dr).  Hence the base integral and
the complete cubic score tower share the open convergence strip

\[
\boxed{2<\operatorname{Re}d<4.}
\]

The source specialization

\[
d=3+2\epsilon,
\qquad \epsilon=0,
\]

lies strictly inside this strip.  It is not a UV pole requiring subtraction.

## Classification of authorized maps

The graph-local counterterm space is therefore

\[
\boxed{\mathcal C_{\rm graph}=0.}
\]

The complete set of source-authorized finite maps is the singleton

\[
\boxed{\mathcal R_{\rm graph}=\{\operatorname{ev}_{\epsilon=0}\}.}
\]

The genuine graph-local scheme group is trivial.  The map induced on the
rank-seven interaction quotient is the identity, so

\[
\boxed{\operatorname{rank}\mathcal O_{\rm finite}=7.}
\]

Contextual faithfulness therefore upgrades from regulated to
scheme-independent finite form within the exact frozen graph-local scope.

## Required distinction

An action-level theory can possess field, coupling, or lower-point
counterterms whose insertions affect this graph even when the graph integral
is finite.  The frozen source does not specify that action or its
renormalization conditions.  Such inherited counterterms define a new
source enlargement; they are not scheme transformations of the frozen graph
period.

Consequently:

\[
\boxed{
\text{graph-local finite theorem: proved;}
\qquad
\text{full action-level finite theorem: not typed by this source.}
}
\]

No Carrier modification is involved in either statement.

## Durable evidence

- `research/benincasa/check_renormalization_source_identifiability.py`;
- `research/benincasa/renormalization-source-identifiability.json`;
- `research/benincasa/check_rank7_local_contact_quotient.py`;
- `research/benincasa/rank7-local-contact-quotient.json`;
- `research/benincasa/check_three_site_uv_finiteness.py`;
- `research/benincasa/three-site-uv-finiteness.json`;
- `research/benincasa/check_source_authorized_renormalization_completion.py`;
- `research/benincasa/source-authorized-renormalization-completion.json`;
- `research/benincasa/source-authorized-renormalization-provenance.md`;
- Entries 2463--2464.

All exact completion gates pass.

## Next enlargement

Freeze one action-level primary source, including its field content,
interaction and derivative orders, regulator, lower-point counterterms, and
physical renormalization conditions.  Derive its contact and coefficient
maps without confusing loop-coordinate polynomials with local counterterms.
