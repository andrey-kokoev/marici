# 1551 — The Bulk--Bulk Second Grade Has Only External Frequency Support

## Hard-to-vary claim

In the one-cubic-operator finite-time truncation, the exact lower-endpoint
expansion of the ordered bulk--bulk triangle at order \(\eta_0^2\) has
frequency support

\[
\boxed{\{-2p,0,2p\}}.
\]

No internal \(q\)- or \(k\)-frequency remains after distributing the outer
and inner commutators and combining equal labelled terms.

## Endpoint derivation

The nested integral has two relevant grade-two routes:

1. evaluate the inner primitive at its upper endpoint and the resulting outer
   primitive at \(\eta_0\);
2. evaluate both primitives at \(\eta_0\).

The apparently harder route in which an inner grade-two lower endpoint
multiplies a fixed upper primitive is absent: none of the 256 raw labelled
terms has both zero inner frequency and the required inner power.

For nonzero combined frequency, grade two forces the maximal powers
\(n_1=n_2=1\). When the combined outer frequency vanishes, however, the
first subleading inner primitive produces an outer \(t^1\) term and therefore
also contributes at grade two. No logarithmic or exponential-integral
convention is required. The original checker omitted this subleading
zero-frequency route; restoring it changes \(c_0\) but not the support or
reality claims.

At

\[
(p,q,k,\eta)=(1.1,0.8,0.9,-0.15),
\]

the coefficients are

\[
c_{-2p}=5.223358086752969-0.01539203954428399i,
\]

\[
c_0=0.8794467614727285,
\]

\[
c_{2p}=5.223358086752969+0.01539203954428399i.
\]

## Artifacts

- `research/benincasa/checkers/finite_time_bulk_bulk_route_census.rs`
- `research/benincasa/results/finite-time-bulk-bulk-grade.json`

## Narrow conclusion

Entries 1548, 1549, and 1551 now establish the source-required
\(\{0,\pm2p\}\) frequency type separately in every one-loop sector.  This is
a structural closure result, not yet coefficient matching to Eq. (19).

## Next falsifier

Add the three source-normalized sector packets coefficientwise, including the
bulk counterterm contribution, and compare the oscillatory and nonoscillatory
coefficients with the exact \(J_i\) combination in Eq. (19).  Any mismatch
must be localized to a printed normalization, contour sign, endpoint
insertion, or counterterm convention; the frequency carrier is no longer an
available repair.
