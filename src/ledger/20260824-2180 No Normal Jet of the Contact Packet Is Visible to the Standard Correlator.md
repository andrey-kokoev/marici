---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2180 — No Normal Jet of the Contact Packet Is Visible to the Standard Correlator

## Exact packet form

Entries 2174–2178 show that the resolved contact packet has the form

\[
p(s)=f(s)(1,-1),
\]

where (s) denotes any finite or compactifying normal coordinate and
(f(s)) carries the contact coefficient and its Cartier order.

The standard correlator readout is the sum covector

\[
\sigma=(1,1).
\]

Therefore, identically as a function of (s),

\[
\boxed{
\sigma p(s)=f(s)-f(s)=0.
}

## All normal jets

Since the vanishing is an identity before specialization,

\[
\partial_s^m(\sigma p)ig|_{s=0}=0
\]

for every (m\ge0). Equivalently,

\[
\boxed{
\sigma\operatorname{gr}^{(m)}p=0
\qquad\text{for every normal grade }m.
}

Thus Entry 2178's nonzero Cartier interference class is not activated by
taking more derivatives of the ordinary correlator. Higher normal order
retains the hidden packet but does not change the readout covector.

## Required new datum

The difference covector

\[
\delta=(1,-1)
\]

would detect the packet:

\[
\delta p=2f.
\]

But the frozen equal-time correlator source supplies (sigma), not
(delta). A route-resolving measurement, Schwinger–Keldysh branch label,
or another controlled comparison port would be genuinely new source data.
It cannot be inferred from the existence of the hidden Cartier grade.

## Narrow conclusion

The contact interference packet is algebraically canonical and survives
resolution, but it is invisible to the standard cosmological correlator at
all ordinary and Rees normal orders.

This is stronger than saying that its boundary value vanishes: the complete
Taylor/Rees tower remains in the kernel of the fixed physical sum readout.

## Evidence

- Entries 2174–2178
- `research/benincasa/checkers/contact_interference_standard_readout_jets.rs`
- allocator claim `seqclaim-a385e2f0f96a0ee4de484455`
