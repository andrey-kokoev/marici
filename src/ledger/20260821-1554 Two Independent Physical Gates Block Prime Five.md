---
author: marici.Nima
---

# 1554 — Two Independent Physical Gates Block Prime Five

## Status

Bounded falsification of the two existing source-derived (C_5) candidates,
using Entry 1256 and rerun exact five-point disk checkers. This is not a
universal exclusion of prime five.

## Five-site carrier candidate

The five-cycle canonical function has 36 free cyclic term orbits. But Entry
1256 proves that an exact (C_5)-orbit of five momentum-conserving resultants
in physical three-space lies in the real two-dimensional rotation
representation. Therefore

\[
\operatorname{rank}\operatorname{Gram}(P_1,\ldots,P_5)\le2.
\]

The cyclic algebraic family is not a physical rank-three carrier. This
candidate fails before coefficient descent or readout is considered.

## Five-point disk-readout candidate

The five-point disk has the physical dihedral source action

\[
D_5=\langle r,s\mid r^5=s^2=1, srs=r^{-1}\rangle,
\qquad [D_5,D_5]=\langle r\rangle\cong C_5.
\]

The exact group checker verifies all 100 products and finds

\[
\chi(r)=+1.
\]

More strongly, the exact reflection calculation transports the
Parke--Taylor cocycle and oriented chamber together. Their two signs cancel,
so the complete period pairing is invariant. The physical readout therefore
descends functorially under cyclic rotations; the source does not define a
five-copy transfer followed by an occurrence trace.

This candidate reaches a physical pairing but fails the trace gate:

\[
\boxed{
C_5\text{ acts trivially on the paired readout before any averaging.}
}
\]

Introducing a Reynolds sum over five cyclic presentations would manufacture
a factor of five rather than derive one.

## Two different failures

\[
\begin{array}{c|c|c}
\text{candidate}&\text{passed}&\text{failed}\\
\hline
\text{five-site cycle}&\text{source }C_5\text{ incidence}
&\text{physical fixed-carrier rank}\\
\text{five-point disk}&\text{physical mixed-variance pairing}
&\text{source trace/transfer requirement}.
\end{array}
\]

Hence the present inventory remains

\[
\boxed{
\operatorname{Bad}_{\rm physically\ established}=\{2,3\},
\qquad 5\text{ not established}.
}
\]

This supports Entry 1553's four-gate sieve: group order becomes physically
arithmetic only after the symmetry acts in-place on an admissible physical
object and the source readout actually uses norm/trace descent.

## Durable evidence

- Entry 1256;
- `research/nima/check_phase_i_string_disk_readout_d5.py`;
- `research/nima/check_five_point_disk_reflection_pairing.py`;
- `research/nima/results/phase-i-string-disk-readout-d5.json`;
- `research/nima/results/five-point-disk-reflection-pairing.json`;
- allocator claim `seqclaim-a0ccf8dffcca6755a646d5cd`.
