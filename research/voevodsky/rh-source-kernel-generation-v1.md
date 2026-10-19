# Iteration4: source-generated arithmetic and a verified Gaussian seam convention

## New result

The arithmetic route is now generated from its **source operators**, not from
finished term matrices. Fresh Arb integration and analytic tail bounds certify
the resulting three-Gaussian packet, and its term enclosures overlap the earlier
certificate. No zero positions enter the generation.

The primary Riemann–Weil formula was directly retrieved and inspected. Its
Fourier, endpoint, prime and divisor conventions agree with the working
Gaussian convention after evenization and one common factor four.

Consequently the **analytic arithmetic/full-divisor identity** is justified for
this Gaussian class by the cited classical theorem. That is distinct from an
independently certified numerical full-divisor evaluation, which remains absent.
Neither result makes the native seed arrows analytic arithmetic generators.

## 1. Input and the actual arithmetic operators

Use logarithmic Gaussian features

    f_i(x)=(2pi t)^(-1/2) exp[-x²/(2t)] exp(i a_i x),
    t=1/10, a_i=0,14,21.

In the Fourier convention

    Ff(u)=integral f(x) exp(-iux)dx,

these give g_i(u)=exp[-t(u-a_i)²/2]. A coefficient query c specifies f_c and

    h_c(u)=Ff_c(u) conjugate(Ff_c(conjugate(u))).

On the real axis this is |Ff_c(u)|². Off the real axis it is the analytic
polarized test, not an absolute square.

The arithmetic triangle's proposed BC evaluator now generates:

### Endpoint: two exponential moments

    A_+(f)=integral f(x) exp(x/2)dx,
    A_-(f)=integral f(x) exp(-x/2)dx,
    E(f)=Re[A_+(f) conjugate(A_-(f))].

For a feature, A_±(f_i)=exp[t(±1/2+i a_i)²/2]. These moments generate each
endpoint matrix entry before any comparison matrix is assembled.

### Gamma: Fourier multiplication

With unitary Fourier transform F_unit=(2pi)^(-1/2)F,

    G(f)=(1/2) integral
         [Re psi(1/4+iu/2)-log pi] |F_unit f(u)|² du.

The fresh implementation instead directly integrates the primary **complex**
digamma expression against the evenized test, then divides by four. No real
part is taken inside its analytic callback. The completed symmetric integral's
imaginary enclosure contains zero.

### Primes: weighted logarithmic translations

    P(f)=-sum_(n>=2) Lambda(n)/sqrt(n)
                  Re <f,T_(log n) f>,
    (T_ell f)(x)=f(x+ell).

Prime powers are generated from integers, with Lambda(p^k)=log p. Completing
the Gaussian square gives the feature overlap

    <f_i,T_ell f_j>
      = exp[-t(a_i-a_j)²/4]
        exp[-ell²/(4t)] exp[i(a_i+a_j)ell/2]
        /(2sqrt(pi t)).

The primitive records retain n, its base prime, logarithmic shift, overlap and
signed contribution. Thus negative prime contributions are not hidden inside
an automatically positive norm. All these operations are on the analytic
source test space; they are not native L/G/N stages.

## 2. Primary-source inspection, rather than a metadata assertion

Fetched `https://arxiv.org/src/2005.02996`: Bondarenko–Radchenko–Seip,
*Fourier interpolation with zeros of zeta and L-functions*, equation (1.1).
The response hash is

    5ee4bbde5a3f4396e972ed214d394f4dc237439f3a5438f02e2efbb196657a58.

It agrees with the old repository citation, but verification used the actual
response. It is a gzip-compressed single TeX file, not a tar archive. The
freshly inspected lines98–110 are retained in
`references/riemann-weil-brs-2005.02996-excerpt.md`.

The primary equation has:

- Fourier transform with exp(-2pi i x nu);
- paired prime atoms at +/-log(n)/(2pi);
- endpoint evaluations at +/-i/2;
- spectral parameters (rho-1/2)/i;
- every nontrivial zero, with multiplicity—not a critical-line-only list;
- analytic-strip and horizontal-decay hypotheses.

The prime sum and zero sum appear on the same side of the primary equation.
Solving for the zero sum produces the negative prime sign above.

## 3. Exact convention identification at the shared edge

Apply the primary theorem to

    phi(u)=h(u)+h(-u).

For the Gaussian pair,

    |exp[-t(x+iy-xi)²]|
       =exp[-t(x-xi)²+t y²].

Thus the test is entire and rapidly decays horizontally, uniformly on every
fixed closed strip. Finite linear combinations retain that admissibility.
Evenization also cancels the imaginary odd digamma contribution, avoiding any
need to interpret a non-even complex-gamma integral as the real multiplier.

Every primary term acquires the same factor four relative to the working
half-divisor convention:

| Term | Primary/working factor |
|---|---:|
| Endpoint | 4 |
| Gamma integral | 4 |
| Gamma log-pi constant | 4 |
| Paired prime cosine | 4 |
| Full signed divisor after reflection | 4 |

The coefficient ratios are checked exactly; a factor-two alternative is
rejected. The Gaussian endpoint and prime Fourier/translation identities are
also independently checked with rigorous balls.

Unconditional reflection rho->1-rho sends the spectral parameter u->-u and
preserves multiplicities. Therefore

    (1/4) sum_rho phi((rho-1/2)/i)
       =(1/2) sum_rho h((rho-1/2)/i).

No RH assumption is used here. This closes the formerly pending primary
coefficient-convention gate **for this Gaussian test class**. It does not
retroactively change historical receipts, certify an arbitrary compact-test
closure or enumerate the divisor.

## 4. Fresh generation and certified finite arithmetic

The producer opens no previous term matrix or zero list during generation.
Only after all terms and interval LDL pivots are produced does it read the old
source certificate for comparison.

- All prime powers through1000 are generated directly.
- The infinite prime tail is enclosed using the existing decreasing
  log-Gaussian majorant, independently evaluated with Arb.
- The primary complex gamma integral is certified on [-64,64].
- Its tail uses |psi(1/4+iu/2)-log pi|<=16+2u².

For the last bound, the digamma series gives |Re psi|<=10+2u²; its imaginary
series is bounded by first term2 plus integral<2; log pi<2. Combining both
Gaussian lobes and both tails gives the reported bound, below1e-70 for every
entry. No finite integral is treated as the entire gamma term.

All generated endpoint/gamma/prime enclosures overlap their earlier reported
counterparts. Fresh interval LDL pivots are strictly positive. This certifies
one three-test span, not positivity for the complete RH test domain.

## 5. What now survives in both native structures

Freshly reconstruct the proton and neutron metric-native operators. For each
newly generated term take its exact dyadic midpoint matrix G_j and use the
signed source/sink attachment

    B_j=X+Y D^-1 G_j.

Each weighted signed pullback is checked in both structures, together with the
properly combined total midpoint. Thus the finite source-generated terms, not
just an arbitrary supplied total matrix, have faithful signed representations
in both carriers.

The midpoint matrices are not asserted to equal the transcendental analytic
source matrices. The general signed-attachment identity also applies
mathematically to their exact analytic entries over C, but those exact state
preparations are not supplied as native generator executions.

The source-level arithmetic/full-divisor equality is now the classical
explicit-formula theorem in an inspected convention. The remaining spectral
execution obligation is an **independent full-divisor computation/enclosure**,
not proving the known explicit formula from a few numerical zeros.

## 6. Why analytic source operations are genuine additional structure

At t=1/10 and a0=0 the exact endpoint entry is

    E00=exp(1/40).

It is transcendental by Lindemann's theorem. The stored proton/neutron
coefficients, metrics and algebraic test descriptors are algebraic. Any finite
composition of only those algebraic matrix primitives and algebraic readouts
remains algebraic, so it cannot generate this exact endpoint value.

This is a narrowly stated field-closure obstruction. It excludes neither
certified rational approximation algorithms nor supplied analytic input
states, new phase oracles, functional test carriers or infinite limits.
Those are exactly the extra structures that must be named. Encoding the
endpoint in an externally prepared state proves representability, not
source generation by a bare seed.

## 7. Verification and next step

    python research/voevodsky/checkers/check_rh_source_kernel_generation.py

All exact/Arb checks pass. Primary retrieval initially tried a tar reader and
plain UTF-8 decoding before correctly recognizing gzip-compressed TeX; this
was a retrieval-format issue, not a changed scientific formula. Source-owner
stores remain read-only.

Fresh SCC challenge passes at fingerprint
`27f8b61e91ba0024287252b7587c9121b7d757348927b4eb7d979b14191e34ec`.

Artifacts:

- `inputs/rh-source-kernel-generation-v1.json`.
- `results/rh-source-kernel-generation-v1.json`.
- `scc-models/rh-source-kernel-generation-v1.json`.
- the primary excerpt under `references/`.

**Next nonredundant step:** independently realize the spectral triangle using
a certified full-divisor window and tail, or a contour-residue evaluator in
this now verified convention. Keep off-critical zeros admitted. A positive
critical-line scout is not that operation.

The original native-face implementation and all-test positivity remain open.
No particle dynamics, mass calculation or RH proof is introduced.
