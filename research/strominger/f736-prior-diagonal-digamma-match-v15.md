# Physical diagonal and even Tate digamma: exact constant match from prior formulas

## Sources and status

Freshly read:

- `research/strominger/archimedean-diagonal-limit-v1.md`, singular-part calculation and explicit finite part;
- `research/voevodsky/a-subtracted-gamma-shift-operator-completes-the-one-slot-euler-green-form.md`, independently subtracted digamma integral;
- the previously inspected even branch in `research/voevodsky/the-trivial-sector-arithmetic-form-is-a-tate-compression-with-explicit-leakage.md`;
- local principal-value normalization in `research/voevodsky/connes-local-theorem-lifts-every-local-weil-distribution-to-the-affiliated-logarithmic-module-operator.md`.

The following is an analytical extraction/calculation from those retained formulas. No numerical quadrature, tests or certifications were run. It matches the actual frozen even-sector packet diagonal under those prior analytical premises; it is not a completed native F736 witness.

## 1. Fix the actual diagonal test and Fourier convention

Let p=p0 be the frozen real smooth compact log packet, and set

    c(u)=integral p(v)p(v-u)dv,
    d=c(0),
    m_p(t)=integral p(u)exp(-itu)du.

Then c is real, even and supported in [-log2,log2], and

    m_c(t)=|m_p(t)|^2,
    c(u)=(1/(2pi))integral |m_p(t)|^2 exp(itu)dt.

The physical even cosine cutoff note computes

    F_physical
      =lim_(Lambda->infinity)
        [Tr(P_Lambda Q_Lambda A_p A_p*)-2d log Lambda].

Its independently derived finite-part formula is

    F_physical=d(log pi+gamma_E)
      +(1/2)integral_(-1/2)^1
          [f(x)-d 1_(|x|<=1/2)]/|x| dx
      +(1/4)integral_(-log2)^(log2) c(u)/cosh(u/2)du,

where f(x)=c(log(1+x))/sqrt(1+x).

No encoder observation Gram enters the subtraction.

## 2. Convert the physical singular subtraction to log coordinates

Put eta=1/2. For u>0 define

    k(u)=(1/4)[1/sinh(u/2)+1/cosh(u/2)]
        =exp(-u/2)/(1-exp(-2u)).

The nonsubtracted physical kernel becomes k(|u|). The symmetric x-cutoff |x|>delta corresponds to u>log(1+delta) on the positive side and u>-log(1-delta) on the negative side. Both lower thresholds equal delta+O(delta^2); replacing them by a common epsilon changes the finite part by o(1), because the kernel's sole singularity is c(0)/(2|u|).

The subtracted scalar part is

    (d/2)integral_(delta<|x|<=eta) dx/|x|
      =d log(eta/delta).

Consequently the physical formula is equivalently

    F_physical
      =d(log pi+gamma_E+log2)
        +lim_(epsilon->0+)
           [2 integral_epsilon^infinity c(u)k(u)du
             +d log epsilon].                         (P)

The extra log2 is not fitted. It is -log eta for the source's eta=1/2 subtraction. All ordinary integrals in the prior formula remain convergent; (P) is only a useful equivalent finite-part notation.

## 3. Expand the independently fixed even Tate multiplier

The independent scattering convention is

    a_infinity(t)=log pi-Re psi(1/4+it/2).

The subtracted digamma integral gives

    a_infinity(t)=log pi+gamma_E
      +integral_0^infinity
          [exp(-r/4)cos(tr/2)-exp(-r)]/(1-exp(-r))dr.

Keep the numerator subtracted before taking r->0. Pair it with |m_p(t)|^2 dt/(2pi), use the even autocorrelation identity, and set r=2u. This gives

    F_spectral
      :=(1/(2pi))integral a_infinity(t)|m_p(t)|^2dt
      =d(log pi+gamma_E)
        +2 integral_0^infinity
            [c(u)exp(-u/2)-d exp(-2u)]
              /(1-exp(-2u))du.                         (S)

The integrand is integrable near zero: c is smooth with c(0)=d and the subtracted numerator is O(u). It decays at infinity. The Schwartz Fourier factor and logarithmic multiplier make the spectral pairing finite. The identity can be justified first with the subtracted r integral regulated away from zero/infinity, then by the prior graph/Schwartz estimates. This avoids interchanging separately divergent pieces.

## 4. Calculate the normalization constant exactly

The scalar subtraction has the elementary integral

    integral_epsilon^infinity
      exp(-2u)/(1-exp(-2u))du
        =-(1/2)log(1-exp(-2epsilon)).

Thus (S) becomes

    F_spectral=d(log pi+gamma_E)
      +lim_(epsilon->0+)
         [2 integral_epsilon^infinity c(u)k(u)du
           +d log(1-exp(-2epsilon))].

Since

    log(1-exp(-2epsilon))
      =log epsilon+log2+o(1),

this is exactly (P). Therefore

    F_physical
      =(1/(2pi))integral
          [log pi-Re psi(1/4+it/2)] |m_p(t)|^2dt.        (MATCH)

The identity-supported constant agrees. There is no extra delta-at-identity correction between THESE two normalized diagonal expressions.

This also fixes the sign: the physical local Tate diagonal pairs with a_infinity, not with d_gamma=Re psi-log pi. In the half-divisor arithmetic gamma convention the corresponding regular term is -F_physical/2 on the same Fourier test. That arithmetic relation is a convention conversion, not a change to the physical cutoff calculation.

## 5. What has and has not been calculated

Calculated under the retained source formulas:

- the actual frozen p0 diagonal with the correct 2d log Lambda subtraction;
- its equality to the independently fixed even Tate spectral pairing;
- the exact log2 compensation between the physical x-subtraction and digamma subtraction;
- the sign and dt/(2pi) measure for this match.

The physical prior note already supplies the finite-cutoff error bound for convergence to this diagonal. This calculation identifies its limiting constant; it does not replace its finite remainder by zero.

Not claimed:

- a numerical value of the diagonal;
- positivity;
- all angular sectors or a full semilocal source normalization theorem;
- equality of unanchored finite-cutoff operators;
- a feature-level isometry or complete F736 face modification;
- both bottom/filler pairs over the native shared face.

The five packet diagonals coincide by the existing dilation argument, so the same constant match covers those retained diagonal entries. Extension to all polarized compact-physical tests and the exact source distribution should be stated with its own domain/normalization argument, rather than silently promoted from one packet autocorrelation. The derivation's kernel/subtraction structure gives a concrete route to that extension, but no new all-domain certificate is asserted here.

## Refined next step

Do not keep the frozen packet diagonal/PV constant as an unnamed missing normalization. The prior formulas above determine and match it analytically.

Use (MATCH), the known off-diagonal limits and the actual finite error estimates to populate the fixed-sector source-retaining carrier. Audit the general polarized-domain and regulator-family claims separately, then identify the inherited H234 modification and its inverse mate in the retained analytical target. The coupled native bottom/filler problem remains a distinct witness-level task.
