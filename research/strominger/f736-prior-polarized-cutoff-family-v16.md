# Derived one-sector polarized normalization and cutoff-family estimate from the prior physical kernel

## Scope and sources

This is an analytical extraction extending the existing kernel/subtraction argument to its actual compact smooth test domain. Inputs freshly inspected:

- `research/strominger/archimedean-cutoff-entry-v1.md`, exact ordered cosine-cutoff/dilation kernel;
- `research/strominger/archimedean-diagonal-limit-v1.md`, singular subtraction and its Mellin constant;
- `research/strominger/f736-prior-diagonal-digamma-match-v15.md`, matched even Tate normalization;
- prior subtracted-digamma and intrinsic response results cited there and in v13.

No tests, numerical integration or formal certification were run. The result below is conditional on the retained physical kernel and source-normalization premises. It concerns the actual even archimedean sector, not all semilocal or native F736 witnesses.

## 1. Use a general observer, not only the frozen autocorrelation

Let D=C_c^infinity(R) in the log variable, with its usual LF topology. For c in D define the unitary-dilation observer

    A_c=integral c(u) U_(exp u)du.

The fixed-cutoff trace-class estimate from v12 permits interchange with the compact L1 observer integral. Hence the prior exact dilation trace kernel gives

    tau_Lambda(c)=Tr(P_Lambda Q_Lambda A_c)
      =integral c(u) K_Lambda(exp u)du.

Put a=2 pi Lambda^2, d=c(0), and

    f(x)=c(log(1+x))/sqrt(1+x), x>-1,
    f(x)=0 otherwise.

Since c has compact support, f is smooth compactly supported away from x=-1. The exact kernel splits

    tau_Lambda(c)=I_c(a)+J_c(a),

    I_c(a)=(1/pi)integral f(x)Si(ax)/x dx,
    J_c(a)=(1/pi)integral
      c(u) exp(u/2)/(1+exp u) Si(a(1+exp u))du.

No evenness or reality of c is required for these linear identities.

## 2. The general finite-part distribution

Subtract d times the indicator |x|<=eta, with eta=1/2. Near zero f(x)-d=O(x); all resulting finite-part integrals converge ordinarily after this subtraction. The same source Si-integral constant used for the frozen diagonal yields the limit distribution W_even(c).

For u>0 let

    k(u)=exp(-u/2)/(1-exp(-2u)).

Converting the positive and negative x branches separately gives

    W_even(c)=d(log pi+gamma_E)
      +integral_0^infinity
        [exp(-u/2)(c(u)+c(-u))-2d exp(-2u)]
          /(1-exp(-2u))du.                             (W)

This is the general, not necessarily even, version of the v15 diagonal match. The numerator is O(u) at zero; the remaining tail is integrable. The source subtraction gives the same compensating log2 constant as before, so no arbitrary delta-at-identity parameter is introduced.

The subtracted digamma integral and Fourier inversion identify

    W_even(c)=(1/(2pi))integral
      [log pi-Re psi(1/4+it/2)] m_c(t)dt.              (S)

The multiplier is even, so the pairing depends on c(u)+c(-u), as (W) requires. On a compact-support stage, (W) is bounded by a finite first-order test seminorm; (S) is convergent because m_c is Schwartz and the multiplier has logarithmic growth.

The argument uses regulated subtracted integrals before exchanging limits; the two individually divergent pieces at u=0 are never integrated separately.

## 3. General polarization is now explicit

For g,h in D put

    c=g*h_star,
    h_star(u)=conjugate(h(-u)).

Then

    m_c=m_g conjugate(m_h),
    c(0)=integral g(v)conjugate(h(v))dv.

Consequently the actual ordered centered trace has the limit

    Tr(P_Lambda Q_Lambda A_g A_h*)
      -2 log Lambda integral g(v)conjugate(h(v))dv
      -> (1/(2pi))integral a_infinity(t)
            m_g(t)conjugate(m_h(t))dt,

where a_infinity=log pi-Re psi(1/4+it/2).

The normalization applies to arbitrary compact smooth polarized source pairs in THIS sector, not merely the five encoded packets. At finite cutoff the ordered form is retained; its Hermitian limit does not justify deleting its finite skew placement.

Convolution carries fixed support stages to their sum/difference stage. Do not declare one fixed compact-support stage to be a convolution algebra. The full LF source D is closed under these operations.

## 4. Rapid error comes from cutoff differentiation, not the crude nuclear bound

The fixed-cutoff trace-norm estimate in v12 grows exponentially and cannot supply a useful family estimate. The exact kernel gives a different argument.

Differentiate I_c with respect to a:

    a I_c'(a)=(1/pi) S_f(a),
    S_f(a)=integral f(x)sin(ax)/x dx.

The smooth Dirichlet integral has limit S_f(infinity)=pi d. Also

    S_f'(a)=integral f(x)cos(ax)dx,

which is Schwartz in a. Therefore S_f(a)-pi d is rapidly decreasing, with every order controlled by finitely many compact-test seminorms of f. Integrating

    derivative[I_c(a)-d log a]
      =[S_f(a)-pi d]/(pi a)

from a to infinity gives rapid convergence to its finite-part constant, with the same bounded-packet control.

For J_c,

    a J_c'(a)=(1/pi)integral
      c(u) exp(u/2)/(1+exp u)
      sin(a(1+exp u))du.

On a fixed compact source support, the phase derivative exp u is bounded away from zero. Repeated integration by parts gives rapid decrease in a, controlled by finitely many derivatives of c. Since J_c has its dominated-convergence limit, integrating its derivative from a to infinity gives the same rapid convergence.

Thus for every fixed compact K and every N there are a finite derivative order m and constant C_K,N with

    |tau_Lambda(c)-2 c(0)log Lambda-W_even(c)|
      <=C_K,N p_K,m(c) Lambda^(-N), Lambda>=2.        (R)

Here the power a=2 pi Lambda^2 converts arbitrary decay order in a into arbitrary decay order in Lambda. The constants depend on the support stage and order, not on a selected finite packet. The usual integration-by-parts estimates give the seminorm bounds; no numerical quadrature enters.

This improves the earlier coarse O((log Lambda)/Lambda^2) estimate for particular packet entries without contradicting it: that estimate simply did not exploit smooth oscillatory cancellation to arbitrary order.

## 5. Regulator-family topology at the stated strength

Define the actual remainder

    E_Lambda(c)=tau_Lambda(c)-2 c(0)log Lambda-W_even(c).

For the family seminorms

    q_N(E)=sup_(Lambda>=2) Lambda^N |E_Lambda|,

(R) makes c->E(c) continuous on each compact-support test stage and hence continuous as a linear map from the LF source into the corresponding rapidly decreasing FAMILY space. The raw trace family is the exact sum of affine logarithmic volume, constant W_even and this rapid remainder.

This is scalar/distributional family continuity on the source test topology. It is NOT a uniform trace-norm bound for the uncentered operator family, an all-path outer/angular limit, or a bound on an independently completed physical Hilbert source.

The polarized family follows by continuous convolution on bounded pairs of source stages. Pair-linearization is optional and retains its own tensor-domain hypotheses.

## 6. Implication for the source-retaining carrier

In this sector the proposed comparison graph can now use actual continuous coordinates

    c, physical_half_density(c), R(physical_half_density(c)),
    A_c, W_even(c), volume_family(c), E_family(c), endpoint_pair(c),

with the intrinsic response topology, fixed-cutoff operator topology, and the specifically stated scalar family topology. For polarized amplitudes evaluate these coordinates on c=g*h_star while retaining g,h where the task needs their individual endpoints/history. Do not disguise that pair dependence as linearity on one amplitude.

The graph theorem gives a closed source-retaining carrier for the continuous linear coordinate map on c. The source recovery maps are the stated projections/half-density inverse. The actual complete Hermitian-presentation and source-functor indices must still be retained when comparing to the five word objects.

The raw fixed-cutoff skew/ordered data remain separate coordinates; (R) only identifies their limiting polarized signed form. It does not itself select the intended analytical H736 or its higher comparison with native retained presentations.

## Boundaries and disposition

The prior exact physical kernel, singular subtraction and independently fixed digamma formula yield a derived one-sector GENERAL compact-test normalization and a bounded-packet rapid scalar remainder, not just a frozen-diagonal identity.

This addresses substantial analytical components of the open normalization/carrier tasks at a precisely stated sector and topology. It is not a fresh formal/numerical certification, all-sector semilocal theorem, source-forgetting operator inverse, positive-feature isometry, native modification-boundary identification or coupled F736 bottom/filler construction.

The next useful construction is to assemble these actual coordinate maps and source round trips, then give the modification-level interpretation and inverse mate with the same retained finite data. Do not re-open the generic compact-test scalar normalization as though these formulas supplied no extension beyond p0.
