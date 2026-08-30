---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2174 — The Generic Contact Kernel Is a Destructive-Interference Packet

## Frozen readout channels

Entry 2158's three normal readout channels each receive two labelled routes.
For the channel complementary to vertex (i), they are

\[
A_{jk}=4P_{jk}v_{jk},
\qquad
B_{jk}=-8C_jC_kv_{123},
\]

where the first route comes from the corresponding grade-two deletion
sector and the second from the fully deleted contact product.

Entry 2159 fixes

\[
v_{jk}=\frac{2q_{jk}}{y_{jk}},
\qquad
v_{123}=1,
\qquad
\frac{C_jC_k}{P_{jk}}=\frac{q_{jk}}{y_{jk}}.
\]

## Pre-aggregation packet

Substitution before applying the sum readout gives

\[
A_{jk}
=4P_{jk}\frac{2q_{jk}}{y_{jk}}
=8C_jC_k,
\]

\[
B_{jk}=-8C_jC_k.
\]

Therefore, on the generic locus

\[
q_{jk}y_{jk}C_jC_k\ne0,
\]

the labelled route packet is

\[
\boxed{
(A_{jk},B_{jk})
=
(8C_jC_k,-8C_jC_k)
\ne(0,0),
}
\]

while

\[
\boxed{A_{jk}+B_{jk}=0.}
\]

This holds independently in all three cyclic channels.

## Classification

By Entry 2172's mechanism sequence, the canonical generic contact kernel
lies in

\[
\boxed{
\operatorname{im}\widetilde T\cap\ker\sigma,
}

not in \(\ker\widetilde T\). It is therefore a genuine
destructive-interference packet rather than route loss.

This is the direct cosmological analogue of Strominger's magnetic packet
\((A,-A)\) with both routes nonzero. The difference is that the cosmological
kernel line moves rationally with kinematics before source factorization;
the factorization identity converts its route values to the canonical
contact packet above.

## Relation to the component-soft corner

Entries 2160–2166 concern the specialization where a component route and
its soft normalization fail simultaneously. Entry 2174 shows what is being
specialized: a generic nonzero interference packet.

It does not follow that the supported Tor class is ordinary route loss.
The complete Rees specialization must determine whether the nonzero packet:

1. limits to zero before aggregation;
2. survives as an exceptional interference class; or
3. produces an extension between those two mechanisms.

That is now the finite successor test.

## Scope

This is an exact scalar-integrand statement in the three contact-normal
channels. It does not establish a physical period relation, because the
common Bunch–Davies relative chain and its exceptional specialization remain
unconstructed.

## Evidence

- Entries 2158–2159 and 2172
- `research/benincasa/checkers/contact_kernel_route_packet.rs`
- allocator claim `seqclaim-44271247509d829eeb512787`
