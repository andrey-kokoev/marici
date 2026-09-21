# Exact kernel sources have growing cutoff responses escaping to both ends

## Result

Fix a nonzero zero-endpoint kernel source f from the norm-summable vertical Euler class. Cut off by PRIMES p<=P, retaining ALL powers of every included prime and the unchanged archimedean term. Write

    T_P f=Atilde_P E_+f,
    K_gamma=L2(R,exp(-2gamma|u|)du).

Although its all-prime response is exactly zero, the finite responses satisfy

    ||T_P f||_L2(R) is comparable to sqrt(P),
    ||T_P f||_Kgamma is comparable to P^(1/2-gamma).

The constants depend on the fixed nonzero source and, for the second estimate, gamma. Thus the weighted-dual response converges to zero at the displayed sharp power rate, while its ordinary L2 norm diverges. There is no ordinary weak-L2 convergence either.

Two explicit nonzero response profiles move out to u=-log P+t and u=log P+t, with amplitude sqrt(P). No endpoint subtraction, coefficient change, or preparation of a new forcing letter is involved.

## 1. Source and cutoff hypotheses

Use the class already constructed in

`research/voevodsky/infinite-euler-cancellation-gives-a-full-line-kernel-with-zero-endpoints.md`.

Specifically, choose sigma>gamma+1/2, gamma>1/2, and a first-moment finite complex measure mu on s=sigma+i t. Let

    f(x)=integral exp(-(s-1/2)x)dmu(s), x>=0,
    alpha=sigma-1/2.

Assume its actual source vector is nonzero and satisfies

    Atilde_rig E_+f=0,
    ell_+(f)=ell_-(f)=0.

The cited Blaschke sources with C(q)=q(q-1)B(q)/(sigma+2-q)^M, M>=8, meet these conditions. Finite first moment also proves f is C1 and

    |f(x)|+|f'(x)| <= A exp(-alpha x), alpha>gamma>1/2.

Differentiation under the Bochner integral is justified by that moment. In particular f belongs to D_gamma and both endpoint integrals converge absolutely.

Every T_P f is in ordinary L2: the archimedean response is in L2 on the supplied piecewise Sobolev domain, and each finite set of prime towers has absolutely summable translation coefficients on L2.

Since the full response is zero, the weighted-dual identity is

    T_P f=-sum_(p>P) sum_(k>=1) log(p)p^(-k/2)
                 [S_(k log p)+S_(-k log p)] E_+f.

The fixed gamma term has cancelled against the all-prime response, not been dropped from the finite operator. The tail series has locally convergent representatives in the regions used below, by the exponential source bound.

## 2. The PNT input and its uniform use

Write theta(X)=sum_(p<=X) log p. The prime number theorem gives theta(X)/X->1 and the Chebyshev bound theta(X)<=C X. For v>=1, set

    nu_P=(1/P) sum_(p>P) log(p) delta_(p/P).

Its distribution function is [theta(Pv)-theta(P)]/P. With

    epsilon(P)=sup_(X>=P)|theta(X)/X-1| ->0,

its difference from v-1 is bounded by epsilon(P)(v+1).

Integration by parts therefore gives convergence against the test functions below, uniformly when t ranges over a fixed compact interval I in (0,infinity). On the infinite interval the test and derivative decay as v^(-sigma) and v^(-sigma-1); sigma>1 makes the error integrable. On a bounded interval the moving endpoint is handled by the boundary term and the uniform bounded variation. No interchange based solely on pointwise PNT is used.

We also use its elementary partial-summation consequence, for any b>1,

    sum_(p>P) log(p)p^(-b) <= C_b P^(1-b).

## 3. The negative escaping profile

For u=-log P+t<0 only the positive shifts in the omitted tail survive. Its first powers give

    P^(-1/2) T_P f(-log P+t)
      =-integral_1^infinity v^(-1/2) f(t+log v)dnu_P(v)+o(1).

The omitted k>=2 terms are uniformly O(P^(-sigma)) after this normalization. Indeed their arguments are positive for large P and

    P^(-1/2) sum_(p>P,k>=2) log(p)p^(-k/2)
                            |f(k log p-log P+t)|
      <= C_I P^(alpha-1/2) sum_(p>P) log(p)p^(-2sigma)
      <= C_I P^(-sigma).

PNT now gives, uniformly on I,

    P^(-1/2) T_P f(-log P+t) -> H_-(t),

    H_-(t)=-exp(-t/2) integral_t^infinity exp(x/2)f(x)dx
           =exp(-t/2) integral_0^t exp(x/2)f(x)dx.

The last equality uses the FIXED zero endpoint ell_-(f)=0. The total local error is O_I(epsilon(P)+P^(-sigma)).

## 4. The positive escaping profile

At u=log P+t, the omitted negative shifts with k=1 involve precisely P<p<=P exp(t). For bounded positive t, omitted powers k>=2 contribute nothing in this direction once P>exp(max I). The omitted positive shifts contribute O_I(P^(1-2sigma)) after division by sqrt(P), using the source exponential bound and partial summation.

Consequently

    P^(-1/2) T_P f(log P+t)
      =-integral_1^exp(t) v^(-1/2) f(t-log v)dnu_P(v)+o(1)
      -> H_+(t),

    H_+(t)=-exp(t/2) integral_0^t exp(-x/2)f(x)dx
           =exp(t/2) integral_t^infinity exp(-x/2)f(x)dx.

Here the last equality uses ell_+(f)=0. Convergence is uniform on I, with error O_I(epsilon(P)+P^(1-2sigma)). The moving integration endpoint causes no problem: f and f' are bounded on the compact interval, and the PNT integration-by-parts boundary term is controlled uniformly.

Both profiles are nontrivial. They satisfy

    H_-'=-H_-/2+f,
    H_+'= H_+/2-f.

Identical vanishing of either on (0,infinity) would force f=0. Thus each has a compact interval on which its squared integral is strictly positive. The endpoint identities also show both profiles decay at least as exp(-alpha t) as t->infinity.

## 5. Ordinary L2 divergence, with matching upper bound

Choose I=[a,b] in (0,infinity) such that integral_I |H_-|^2>0. Uniform local convergence yields

    (1/P) integral_(-log P+I) |T_P f(u)|^2 du
      -> integral_I |H_-(t)|^2 dt >0.

This proves ||T_P f||_2>=c_f sqrt(P) for all sufficiently large P. The positive profile independently gives another escaping response window.

For the upper bound, unitarity of translations on ordinary L2 gives

    ||T_P f||_2
      <= ||Atilde_infty E_+f||_2
         +2||f||_2 sum_(p<=P) log(p)/(sqrt(p)-1).

Partial summation of theta(X)<=C X gives

    sum_(p<=P) log(p)/sqrt(p)=O(sqrt(P)),
    sum_(p<=P) log(p)/p=O(log P).

Since 1/(sqrt(p)-1)=p^(-1/2)+O(p^(-1)) uniformly for primes, the upper bound is O_f(sqrt(P)). This proves the asserted two-sided norm order, not just failure of convergence.

The local profiles alone do not determine a global leading coefficient. The subsequent `global-prime-cutoff-escape-has-an-exact-universal-L2-law.md` closes that gate by proving a global two-profile expansion. It gives the exact coefficient 2 integral |hat(E_+f)(xi)|^2/(1/4+xi^2) dxi, and extends the ordinary-L2 law to every fixed vector in the archimedean domain.

## 6. The weighted norm decays at the sharp power rate

On the same negative escaping window, |u|=log P-t. Therefore

    P^(2gamma-1) integral_(-log P+I)
                    exp(-2gamma|u|)|T_P f(u)|^2 du
      -> integral_I exp(2gamma t)|H_-(t)|^2 dt >0.

This supplies the lower bound c_(f,gamma) P^(1/2-gamma) for the K_gamma norm. On the positive window the corresponding limiting weight is exp(-2gamma t).

For the matching upper bound use the unchanged translation estimate

    ||S_(+/-k log p)||_(H_+->Kgamma) <= p^(-k gamma).

Since the full response is zero,

    ||T_P f||_Kgamma
      <=2||f||_Hgamma sum_(p>P,k>=1) log(p)p^(-k(gamma+1/2))
      <=C_gamma ||f||_Hgamma P^(1/2-gamma).

This last step uses the same Chebyshev partial-summation estimate and the geometric sum over powers. It sharpens the earlier elementary log-containing cutoff majorant without changing the topology or the operator.

## 7. Scope and compatibility

This result concerns canonical prime cutoffs p<=P, with ALL their powers retained, acting on a fixed raw kernel source. It proves a strong distinction:

- the all-prime raw response is exactly zero;
- its finite responses are ordinary L2 vectors with norms growing as sqrt(P);
- those same vectors converge to zero in the specified weighted-dual norm.

The endpoints vanish on the SOURCE, so unsubtracted and prescribed endpoint-subtracted finite responses coincide here. No new subtraction makes the divergence disappear. Unbounded ordinary L2 norms also exclude weak convergence or a weakly convergent subsequence along P->infinity.

This is not a new arithmetic-invisible prepared letter. Voevodsky's `the-raw-arithmetic-kernel-does-not-survive-actual-letter-preparation.md` remains applicable: re-preparation produces a visible holomorphic endpoint family. No edge window, source relation, or attachment quotient is changed.

The weighted-dual cutoff and labelled-noise certificates for actual attachment observations remain valid. Divergence in the stronger ordinary L2 norm does not contradict convergence of bounded test/dual observations in their declared topology.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_kernel_cutoff_escape.py`

Passed exact endpoint-zero fixture integrals, both profile signs and ODEs, omitted-power exponents, and moving-window weight scaling. Numerical first-prime sums through P=100000 agree with the fixture profiles (maximum final-grid absolute error below 0.00073). The fixture is NOT asserted to be an arithmetic kernel source. Infinite kernel existence is supplied by the Blaschke theorem; actual escape follows from PNT and the operator estimates proved above.

Related inputs:

- `research/grothendieck/the-all-prime-tate-response-converges-in-a-two-sided-weighted-dual.md`;
- `research/voevodsky/infinite-euler-cancellation-gives-a-full-line-kernel-with-zero-endpoints.md`;
- `research/grothendieck/full-residual-reflection-confirms-the-infinite-euler-kernel.md`;
- `research/voevodsky/the-raw-arithmetic-kernel-does-not-survive-actual-letter-preparation.md`;
- `research/voevodsky/the-nonzero-attachment-observer-has-a-linear-labelled-noise-certificate.md`.
