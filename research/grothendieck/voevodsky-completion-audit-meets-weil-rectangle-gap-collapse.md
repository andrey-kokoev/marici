# Voevodsky completion audit meets the Weil rectangle gap collapse

## Question

Do the existing Voevodsky semibounded-form and radial-source audits supply a route from finite Weil rectangles to an RH-bearing completed positive form?

## Prior results recovered

Voevodsky's completion theorem gives a valid sufficient mechanism for an unbounded mixed bridge: closed nonnegative forms on a common invariant domain, a coercive pivot, a cross form with strict relative bound below one, and domain-preserving composition. KLMN then yields a closed positive Schur form. The radial-source audit finds that the proposed `R_zeta` realization has none of the first required source objects: no independently derived common core, no intertwiner, no tested factorization, and no closure/radical/dense-range identification.

These are not stylistic conditions. The audit supplies countermodels in which core equality does not identify closures, finite positivity develops a limiting radical, or an injective dense-range map has zero reduced minimum modulus.

## Contact with the completed Weil rectangle

Each parity block of the normalized `2x3` rectangle has the form

`[[a,b],[b,d]]`.

Its Schur relative-bound parameter is

`theta=b^2/(ad)`.

Strict positivity is exactly `theta<1`; the parity determinant is

`D=ad(1-theta)`.

The source-side Gaussian scout finds both determinants positive at every sampled smoothing parameter, but exponentially approaching zero with rate approximately `242.1357`. Therefore

`theta_+(t) -> 1`,

`theta_-(t) -> 1`

along the narrow spectral regime. The collapse is explained by domination by one conjugate spectral pair, whose parity blocks have rank one.

Thus Voevodsky's strict-relative-bound theorem can certify each fixed rectangle only if its source hypotheses are independently established. It cannot by itself pass to the relevant completion with a uniform constant `theta<1`: the observed spectral-gap asymptotic forces the best constant toward one.

## Consequence

The two programmes meet at the same obstruction in different languages:

- the rectangle programme sees exponentially collapsing parity determinants;
- the completion audit sees loss of coercivity and formation of a limiting radical;
- the radial audit sees no source-derived intertwiner or common closed domain that could identify and quotient that radical coherently.

A proof strategy demanding uniform coercivity is therefore mismatched to the actual zeta spectral asymptotics. The viable replacement must permit a controlled limiting radical and prove that quotienting by it is cutoff-compatible. This requires:

1. a source-derived common core and `R_zeta`-type intertwiner;
2. closability of the completed Weil form on that core;
3. explicit identification of the rank-two asymptotic radical;
4. convergence of quotient forms after removing that radical;
5. no additional radical appearing in higher spectral sectors.

## Candidate idea from Voevodsky's broader method

The reusable categorical idea is not that descent creates positivity. It is that a comparison should be represented as a source-derived map between typed quotients, with closure, radical, and coherence checked independently. For the Weil rectangles, the spectral-wedge formula identifies the finite radical exactly as parity-vector collinearity. This suggests a filtered quotient system whose transition maps preserve wedge classes rather than raw Gram coordinates.

The missing arithmetic datum remains a source-side transition map between cutoff quotient spaces. Equal dimensions, positive samples, or agreement of normalized correlations do not construct it.

## Disposition

Voevodsky's work rules out a naive completion of the sampled finite positivity and supplies the correct acceptance tests. It does not currently provide an RH proof route because the common core and intertwiner are absent and uniform Schur coercivity is false in the observed regime. The nonredundant next target is a cutoff-compatible quotient-by-rank-two-radical construction derived directly from the completed explicit formula.

## Sources

- `research/voevodsky/unbounded-r-zeta-identity-typing-audit.md`
- `research/voevodsky/r-zeta-source-adequacy-audit.md`
- `research/voevodsky/semibounded-form-mixed-completion.md`
- `research/grothendieck/rectangle-parity-determinants-detect-spectral-gap.md`
- `research/grothendieck/rectangle-parity-determinants-are-spectral-wedge-sums.md`
