# 1081 — The Three-Site Physical Residue Link Is a Six-Cycle

## Question

Entry 1080 closed the two-site route: its degree-one corner class belongs to
spurious connection walls rather than to the physical connected-subgraph
factorization complex. The next finite falsifier is the three-site integrand,
where equation (51) of arXiv:2408.16386v2 contains overlapping physical
denominator supports from the outset.

What is the labelled normal link compiled by the six source terms?

## Frozen source terms

Every term in equation (51) contains the four common denominators

\[
q_{\mathcal G},
\qquad
q_{\mathfrak g_1},
\qquad
q_{\mathfrak g_2},
\qquad
q_{\mathfrak g_3}.
\]

The remaining labelled pairs are exactly

\[
\begin{aligned}
&(q_{\mathcal G_{12}},q_{\mathfrak g_{23}}),
&&(q_{\mathcal G_{12}},q_{\mathfrak g_{31}}),\\
&(q_{\mathcal G_{23}},q_{\mathfrak g_{31}}),
&&(q_{\mathcal G_{23}},q_{\mathfrak g_{12}}),\\
&(q_{\mathcal G_{31}},q_{\mathfrak g_{12}}),
&&(q_{\mathcal G_{31}},q_{\mathfrak g_{23}}).
\end{aligned}
\]

No additional pair is admitted.

## Labelled normal link

Ordering the six noncommon vertices as

\[
q_{\mathcal G_{12}},
q_{\mathfrak g_{23}},
q_{\mathcal G_{31}},
q_{\mathfrak g_{12}},
q_{\mathcal G_{23}},
q_{\mathfrak g_{31}},
\]

the source pairs are precisely the consecutive edges, including the closing
edge. Hence the normal link is

\[
\boxed{\operatorname{Lk}_{\rm phys}=C_6.}
\]

The complete denominator nerve is the join

\[
\Delta^3 * C_6,
\]

where \(\Delta^3\) is the common four-pole simplex. It is contractible because
each common vertex is a cone point. The nontrivial information is therefore in
the normal link, not in the absolute nerve.

## Exact computation

For the oriented incidence map

\[
\partial_1:C_1(C_6)\longrightarrow C_0(C_6),
\]

the durable Rust checker gives

\[
\operatorname{rank}\partial_1=5,
\qquad
\dim H_0(C_6)=1,
\qquad
\dim H_1(C_6)=1.
\]

The cyclic occurrence action

\[
12\mapsto23\mapsto31\mapsto12
\]

acts as an orientation-preserving rotation of the hexagon. Therefore its
character on the fundamental cycle is

\[
\chi_{H_1}(\sigma)=+1.
\]

## Narrow result

\[
\boxed{
\text{The three-site physical factorization supports have a canonical
cyclic-invariant rank-one normal-link class.}
}
\]

Unlike the bubble corner line, this class is compiled directly from physical
connected-subgraph denominators printed in the source. This is stronger
carrier evidence, but it is not yet a physical activation theorem.

## Remaining gate

The source terms determine the support nerve but not yet the coefficient of
the oriented fundamental cycle under ordered sequential residues. We must
derive the six residue maps, including Poincaré-residue signs and occurrence
orientations, and evaluate their signed composition around \(C_6\).

Possible outcomes:

- nonzero cycle functional: a source-defined physical degree-one readout;
- exact/cancelling cycle: a physical support class invisible to the integrand;
- incompatible residue targets: the link class exists only at carrier level.

No conclusion should be drawn from the rank-one link alone.

## Durable artifacts

- `research/benincasa/check_three_site_physical_residue_link.rs`
- `research/benincasa/three-site-physical-residue-link.json`

