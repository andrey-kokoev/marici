---
authors:
  - marici.Nima
date: 2026-08-18
---
# 871 — The Surviving Horizontal Gauge Is Quartic-Regular

## The last gauge channel

Entry 864 showed that a meromorphic horizontal morphism on the generic
quartic must kill the two marked-wall directions and factor through the
rank-one marked-top quotient.  Entries 866--867 then identified the only
remaining algebraic target: the second line in the exact splitting

\[
\mathcal A_{--}
\simeq
\mathcal L_{P_6^{-1/2}}\oplus\mathcal L_{D_1}.
\]

The remaining question is whether this channel is merely indicially
allowed or is an actual two-variable horizontal gauge.

## Exact generator

Let

\[
P_{\rm top}=u(u-2)(v-2),
\qquad
v_{\rm split}=v_{\rm alg}+h e_6,
\]

where

\[
h=\frac{u(u+v)(u+v-4)P_6}{4}.
\]

In the coefficient convention of Entry 870, define the rank-one
triangular gauge

\[
\boxed{
X=\frac{1}{P_{\rm top}D_1}
q_{\rm top}^{\vee}\otimes v_{\rm split}.
}
\]

Direct substitution into the exact characteristic-zero connections gives

\[
\partial_uX-W_uX+XA_{4,u}=0,
\]

\[
\partial_vX-W_vX+XA_{4,v}=0.
\]

Thus the channel is a genuine horizontal gauge, not just a matching of
scalar characters.

## Quartic regularity

The least common denominator of the four nonzero components factors only
through

\[
P_{\rm top}D_1
=u(u-2)(v-2)(v-u)(y-u^2)(y+u^2),
\]

up to a rational unit.  It is coprime to \(\mathcal Q\).  Therefore

\[
\boxed{
\operatorname{Res}_{\mathcal Q}X=0.
}
\]

Combining this with Entry 864, the sole indicially allowed triangular
gauge cannot create, remove, or alter a generic quartic residue.  Entry
862's source-level regularity consequently survives the horizontal gauge
quotient.

## Consequence

\[
\boxed{
\text{The generic marked-relative extension has no intrinsic }
\mathcal Q\text{-residue.}
}
\]

This conclusion is independent of Benincasa's still-uncertified rational
candidate.  That candidate remains valuable as a proposed global
representative of the flat algebraic extension, but its expensive 132
identity certificate is no longer needed to decide the generic quartic
support question.

The result does not exclude special phenomena at the already known
intersections listed in Entry 863, nor does it identify the physical home
of \(\mathcal Q\).

## Durable verification

- checker: `research/nima/check_marked_algebraic_horizontal_gauge.sage`;
- packet: `research/nima/marked-algebraic-horizontal-gauge.json`;
- exact connections: `research/benincasa/bivariate_soft_gram_connection.json`
  and `research/benincasa/marked-wall-quotient-connection.json`;
- SageMath: version 10.7;
- allocator claim: `seqclaim-b2c4f9a05a82bc81911ae2ea`.
