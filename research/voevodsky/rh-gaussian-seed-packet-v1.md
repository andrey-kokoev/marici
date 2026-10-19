# An arithmetic Weil packet carried into the native seed relationships

## Changed result

The attachment now consumes a **numerically computed arithmetic packet**, not
an arbitrary hostile matrix. Endpoint, gamma and prime terms are evaluated
separately from the existing explicit formula; a separate finite critical-line
zero sum supplies a consistency test.

For three frozen Gaussian tests, the arithmetic and finite-zero matrices agree
numerically to about 1.33e-52. The analytic absolute prime-tail majorant evaluates
to about 8.90e-52. The arithmetic matrix's 30-decimal rational rounding has an
**exact native signed attachment**, independently verified, and an exact
positive-definite LDL certificate.

This is one finite source packet. It does not certify the analytic integral,
exhaust the zeros, implement the arithmetic/zero operations on the two geometric
faces, or prove RH.

## Actual source tests and polarization

The source is
`research/grothendieck/explicit-two-variable-weil-heat-source-formula.md`.
Its centered half-divisor normalization and unresolved external verification
status are preserved.

Choose, before computation,

    t=1/10,
    a=(0,14,21),
    g_i(u)=exp[-t(u-a_i)^2/2].

These are Fourier-side Gaussian test components. They are not supplied zero
locations or source vertex coordinates. Their product is exactly

    g_i(u)g_j(u)
      = exp[-t(a_i-a_j)^2/4]
        exp[-t(u-(a_i+a_j)/2)^2].

Thus each packet entry is a specified scalar multiple of the repository's
shifted-Gaussian explicit formula at xi=(a_i+a_j)/2. The arithmetic packet is

    G_arith=G_endpoint+G_gamma+G_prime.

All three matrices are retained, so their individually signed contributions
are not replaced with an automatically positive factorization. Prime powers
up to 1000 are enumerated from integers; no zero data enters the arithmetic
calculation.

The zero-side scout separately computes the first sixteen positive-ordinate
critical-line zeros using mpmath. Its entry is

    G_zero,ij = (1/2) sum_(k=1..16)
                  [g_i(gamma_k)g_j(gamma_k)
                   +g_i(-gamma_k)g_j(-gamma_k)].

It is positive by construction, but is only a finite sampled zero packet. It
must not be called a complete sum over every nontrivial zero. Neither sampled
critical-line positions nor their numerical agreement with arithmetic settle
the absence of off-critical zeros.

## Numerical results and a retained failure

The first frozen implementation integrated the gamma term over broad intervals
centred at xi. Its arithmetic/zero residual was about 1.83e-23, failing the
preregistered 1e-30 gate. Repeating at 40 and 60 digits hardly changed that
residual. The failure is retained in
`results/rh-gaussian-seed-packet-v1-first-failure.json`.

The repaired implementation adds fixed cuts at zero and +/-1,2,4,8,16,32,64.
The source formula, Gaussian tests, prime cutoff, zero count and comparison
tolerance remain unchanged. A new SCC freeze preceded the repaired execution.

| Numerical check | Result |
|---|---:|
| Maximum arithmetic packet change, 40 to 60 digits | 6.09e-41 |
| Maximum arithmetic versus sixteen-zero packet difference | 1.33e-52 |
| Evaluated analytic absolute prime-tail majorant | 8.90e-52 |

The arithmetic eigenvalue scout gives approximately

    1.05353e-9, 0.449945197, 0.657368237.

These are numerical implementation results, not interval-certified errors.
The broad-partition failure illustrates why precision stability alone cannot
be promoted to a correctness certificate.

## The prime-tail bound is specified, not silently dropped

For integer cutoff N, use Lambda(n)<=log(n) and |cos|<=1. The positive majorant

    f(x)=log(x) x^-1/2 exp[-log(x)^2/(4t)]

is decreasing for x>=N=1000 at t=1/10. Consequently the omitted prime contribution
is bounded in absolute value by

    [1/(2 sqrt(pi t))] integral_N^infinity f(x) dx.

Put z=log(N)-t. Completing the square evaluates the integral as

    exp(t/4) [2t exp(-z^2/(4t))
               +t sqrt(pi t) erfc(z/(2 sqrt(t)))].

The additional mixed-Gaussian entry prefactor is at most one, so this scalar
majorant also bounds each packet entry's prime truncation. The analytic formula
is retained; its numerical value has not been outward-rounded as a certified
interval. No analogous exhaustive-zero-tail or gamma quadrature certificate
is claimed in this turn.

## Exact finite seed attachment, with rounding explicit

Round each arithmetic entry to thirty decimal places, producing a rational
Hermitian matrix G_round. The displayed run's largest change is at most
5e-31 per entry, as expected from that rounding rule. This does not include
unknown quadrature error.

Reuse only the native source/sink directions X,Y of
`rh-seed-signed-attachment-v1.md`. With D=X^dagger X and the native analytically
derived Hermitian operator K, define

    B=X+Y D^-1 G_round.

The exact certificate establishes

    rank B=3,
    B^dagger K B=G_round.

An independent rational-realification implementation checks the entire
pullback matrix, not just selected quadratic values. An independent rational
LDL calculation verifies all three pivots positive and reconstructs G_round
exactly. Therefore positivity of **the rounded matrix** is an exact result.
It is not a rigorous positivity certificate for the unrounded analytic Weil
packet without a certified source-error enclosure.

The attachment is a labelled global coefficient map into existing native
channels. It does not yet attach each prime translation, gamma operation and
zero evaluation to an actual local face generator. That geometric operation
comparison remains different from faithful representation of the final packet.

## What this supplies for the two-triangle question

It closes one previously absent concrete object: a source-computed arithmetic
comparison matrix, with independent finite spectral scout and a coefficient
attachment. We can now compare actual term-labelled source data rather than
arbitrary Hermitian examples.

The following claims remain separate:

1. Numerical finite arithmetic/spectral consistency: tested here.
2. Exact representation and positivity of the rounded packet: verified here.
3. Certified explicit-formula normalization and analytic error/tail bounds:
   not completed here.
4. Incidence-respecting realization of the two independently sourced routes
   by the geometric seed triangles: not constructed here.
5. All-packet positive, coherent faithful completion: not established; this
   is the RH-bearing global condition.

A passing finite packet cannot be promoted across these missing connections.
The continuation `rh-gaussian-source-certification-v1.md` now certifies the
gamma integration, both infinite source tails and strictly positive LDL
pivots for this same analytic arithmetic packet. It does not certify the
exhaustive zero sum or the geometric operation attachment. The numerical
and rational-rounding claims in this packet remain at their original scope.

## Reproduction and provenance

    python research/voevodsky/checkers/check_rh_gaussian_seed_packet.py
    python research/voevodsky/checkers/verify_rh_gaussian_seed_packet.py

The producer uses an already available read-only mpmath installation under
`research/flavor/.venv/Lib/site-packages` if the default interpreter lacks it;
no dependency provisioning or source-owner execution occurs. The receipt pins
the imported package entrypoint and all consumed packets. Shared scientific
files and stores remain unchanged.

Original failure freeze:
`d1cad824d963571493377a5b04e49c83b793efaddd53c731b9e6efabb2baca49`.
Repaired implementation freeze:
`81509130a5ef1941eac464ee5865e9d84456e45b7c2b6628049bdbd46f424b3e`.

Artifacts:

- `inputs/rh-gaussian-seed-packet-v1.json`.
- `results/rh-gaussian-seed-packet-v1.json`.
- `results/rh-gaussian-seed-packet-v1-first-failure.json`.
- `results/rh-gaussian-seed-packet-v1-rounded-audit.json`.
- `scc-models/rh-gaussian-seed-packet-v1.json`.

This numerical comparison is not an RH proof or a proof that the two physical
seed faces already implement the zeta explicit formula.
