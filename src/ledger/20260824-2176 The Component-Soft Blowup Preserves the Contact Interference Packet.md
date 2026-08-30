---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2176 — The Component-Soft Blowup Preserves the Contact Interference Packet

## Question

Entry 2174 proves that the generic contact kernel has the nonzero route
packet

\[
(A,B)=(8C,-8C).
\]

At the component-soft corner

\[
q=y=0,
\]

the displayed factors

\[
P=C\frac yq,
\qquad
v=2\frac qy
\]

cannot be specialized separately. The correct test pulls back their complete
composition to

\[
\operatorname{Bl}_{(q,y)}.
\]

## The (q)-chart

Put

\[
y=qt.
\]

Then

\[
P=Ct,
\qquad
v=\frac2t.
\]

The zero and pole cancel in the composed grade-two route:

\[
A=4Pv=8C.
\]

Together with the fully deleted route,

\[
B=-8C,
\]

the strict packet is

\[
(A,B)=(8C,-8C).
\]

## The (y)-chart

Put

\[
q=ys.
\]

Then

\[
P=\frac C s,
\qquad
v=2s,
\]

and again

\[
A=4Pv=8C,
\qquad
B=-8C.
\]

The two strict transforms agree on (st=1). Therefore the packet descends
globally across the exceptional projective line.

## Result

Away from deeper contact support (C=0),

\[
\boxed{
(A,B)|_{E}=(8C,-8C)\ne(0,0).
}

Thus the component-soft blowup does not turn the generic null readout into
route loss. It preserves a nonzero exceptional destructive-interference
packet.

The Tor packet of Entries 2160–2166 still exists as the associated grade of
the separately resolved zero/pole factors. Entry 2176 shows that this Tor
grade is not the complete physical route packet: after composing the
source-defined adapter, the interference class remains regular and nonzero.

## Architectural consequence

This is a concrete instance of a general warning:

\[
\boxed{
\text{factorwise route failure}
\not\Rightarrow
\text{failure of the composed physical route}.
}
\]

The blowup retains both pieces:

- a factorization-sensitive Cartier/Tor grade;
- a regular composed interference packet.

Their relation is extension data of the resolved adapter, not a new Carrier
stratum.

## Scope and next falsifier

The statement is exact for the scalar contact-normal adapter and assumes
that (C) remains nonzero. At (C=0), both strict routes vanish and genuine
route loss may occur. The next finite test is therefore the deeper locus

\[
q=y=C=0,
\]

using the source-derived contact denominator and the physical incidence of
that locus.

## Evidence

- Entries 2159–2160 and 2174
- `research/benincasa/checkers/contact_interference_rees_specialization.rs`
- allocator claim `seqclaim-d56c6d7c290f67579f15621e`
