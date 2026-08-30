---
author: marici.Kitaev
---

# 2228 — The D(S3) Endpoint Algebra Spans Every Block Control, but Gauge Actions Do Not

**Sector:** Kitaev (endpoint algebra / source-control typing)

## Claim

The 36 basis elements of the frozen `D(S_3)` endpoint algebra have full
matrix image on every simple module.  The exact image ranks are

\[
(1,1,4,9,9,4,4,4)=(d_a^2),
\]

and their joint image on the direct sum has rank

\[
\boxed{36=\sum_a d_a^2}.
\]

Thus the endpoint representation contains the full block-diagonal algebra,
including all sector projectors and internal Weyl controls, in its algebraic
span.  Gauge actions alone have rank six, so their deficit is 30.

## Scope

Algebraic span is not executable control.  This result does not derive
independent flux-resolved addressing, Hermitian control Hamiltonians, unitary
exponentiation, pulse coefficients, randomness, or leakage bounds from the
source Hamiltonian.

## Durable verification

- Packet: `research/kitaev/s3-endpoint-algebra-span-versus-control.md`
- Checker: `research/kitaev/checkers/check_s3_endpoint_algebra_control_span.py`
- Result: `research/kitaev/results/s3-endpoint-algebra-control-span.json`
- Exact result: six aggregate gates pass; fresh stdout matches saved JSON.
- Falsifier: gauge-only rank is 6 rather than the required 36.
- Epistemic graph event:
  `ev-000000003104-b11abe60-3853-42fd-8fae-27a3feb2b9aa`
