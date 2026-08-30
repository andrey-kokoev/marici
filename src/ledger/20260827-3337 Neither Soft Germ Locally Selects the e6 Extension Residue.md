# 3337 — Neither Soft Germ Locally Selects the e6 Extension Residue

## Question

Entry 3332 shows that diagonal occurrence descent cannot insert the unique
two-soft logarithmic class into (B_{e_6,q_0}). Does the full cleared
rank-twelve source module at least fix either local residue of that coordinate?

## Source-direct Laurent test

The rank-twelve reduction engine exports all 132 cleared source identities with
372 primitive coefficients. The Laurent harness was generalized, without
changing its existing default (u)-axis behavior, to expand in

\[
t=v-v_0
\]

at fixed (u=0), while differentiating in the (v) direction.

For each soft center

\[
v_0=0\quad(X_3=0),
\qquad
v_0=2\quad(X_2=0),
\]

the calculation retained Laurent orders (-2) through (3), all three
quotient generators, and every primitive coordinate. Polynomial source
coefficients were reconstructed through degree sixteen and checked at a held-out
point.

The tests were repeated at the two independent primes

\[
2305843009213693951,
\qquad
2305843009213693921.
\]

## Exact modular ranks

At (v=0), the Laurent system has rank

\[
555.
\]

At (v=2), it has rank

\[
520.
\]

Both ranks replicate exactly at both primes. In neither system is the target
coordinate

\[
\operatorname{Res}_{v=v_0}(B_v)_{e_6,q_0}
\]

a pivot. Therefore it is not merely a pivot with free-column contamination; it
is itself a free Laurent coordinate.

## Result

Neither soft germ locally selects the (e_6,q_0) residue. The full cleared
source equations admit local primitive freedom at both (X_3=0) and (X_2=0).

This rules out two proposed shortcuts:

- deriving the candidate residue from one soft germ;
- deriving the opposite pair by independently computing two locally fixed
  residues.

## Scope

The result is local. It does not exclude a global rational section whose single
denominator and numerator correlate the two free germs. In particular, the
global no-infinity condition of Entry 3328 is invisible to two independent
local Laurent solution spaces.

The status is now:

- unique admissible global logarithmic line: established;
- source coefficient (C_2): established;
- local residue selection at either soft germ: falsified;
- global source correlation of the residue pair: open.

## Next falsifier

Restrict the cleared source system to (u=0) and solve one global polynomial
module with common denominator

\[
v(v-2).
\]

Test the residue-difference functional directly. If it remains free, the
rank-twelve source equations do not select the candidate even globally. If it
is fixed, verify the result at unused primes and by exact cleared polynomial
identities.

## Verification

Harness:
`research/benincasa/checkers/audit_marked_extension_source_laurent_lead.py`.

Aggregate checker:
`research/benincasa/checkers/audit_two_soft_source_residue_freedom.py`.

Aggregate packet:
`research/benincasa/results/two_soft_source_residue_freedom.json`.

Allocator claim: `seqclaim-3a1d53648f49cb66bc46ce42`.
