# Arb certifies uniform escape on unrestricted half-line prior balls

## Certified finite-cutoff result

At the prime cutoff P=100000, including all powers of its 9592 primes, the unchanged full finite-place response satisfies

    ||P^(-1/2)T_P E_+f - E_P E_+f||_L2(R)
      <0.72 M

for every f with unrestricted half-line H1 norm at most M>0. Here

    E_P h(u)=J_-h(u+log P)+J_+h(u-log P)

is the exact two-profile approximation from the global escape theorem. No zero boundary trace is imposed. The same certificate applies to a D_gamma prior ball of radius M, since its norm dominates ordinary half-line H1.

The actual Arb-enclosed coefficient is approximately 0.710565. A second bound on the full-line H^(1/4) prior ball gives error <4 M. All bounds include higher prime powers and the fixed archimedean response. There is no unspecified PNT constant or quadrature remainder in this finite certificate.

This is an absolute approximation guarantee for the normalized RESPONSE FIELD. It neither guarantees a relative error for arbitrarily small signals nor reconstructs a source. It does not discretize either the measured field or the two convolution profiles.

## 1. Finite discrepancy data

Use the prime measures from the quantitative escape theorem and put

    W(x)=sum_(p<=x) log(p)/sqrt(p), W(x)=0 for x<2,
    d(a)=P^(-1/2)W(P exp(-a))-2exp(-a/2),
    a_0=|d(0)|, D_1=integral_0^infinity |d(a)|da,
    D_2=(integral_0^infinity |d(a)|^2 da)^(1/2),
    kappa_1=sqrt(a_0^2+D_1^2), V=W(P)/sqrt(P)+2.

All these quantities involve only the finite list of included primes. After x=P exp(-a),

    D_1=P^(-1/2) integral_0^P |W(x)-2sqrt(x)| dx/x,
    D_2^2=P^(-1) integral_0^P (W(x)-2sqrt(x))^2 dx/x.

On a step interval [l,b] where W=w is constant, primitive functions are

    w log x-4sqrt(x),
    w^2 log x-8w sqrt(x)+4x,

respectively before taking the absolute value in the first integral. The script certifies w<2sqrt(l) on EVERY included step interval at the chosen cutoff. Thus the sign is known throughout each interval. No claim of that inequality beyond this finite range is made.

The initial interval (0,2) contributes 4sqrt(2) and 8 to the unscaled first and second integrals. Arb evaluates all logarithms, roots, prime sums and primitive differences at 192-bit precision. The tail a>log(P/2) is already included through x in (0,2).

Certified values include

    a_0 approximately 0.02880327647,
    D_1 approximately 0.22223874972,
    D_2 approximately 0.06620279032,
    kappa_1 approximately 0.22409750247,
    V approximately 3.97119672353.

These printed approximations are not substituted for the enclosing balls in any comparison.

## 2. Explicit constants for fractional full-line priors

For either centered convolution error B_P, the signed-measure identity from the preceding theorem gives

    ||B_P h||_2 <= a_0||h||_2+D_1||h'||_2
                 <=kappa_1||h||_H1.

Its L2 operator norm is at most V. Interpolation therefore bounds the sum of the two translated first-prime errors by

    2 V^(1-r) kappa_1^r ||h||_H^r, 0<r<=1.

The higher-power operator has the explicit bound

    Q_P=2 sum_(p<=P) log(p)/(p-sqrt(p)).

This is the geometric sum of every included k>=2 in both translation directions, not a truncation of those towers. At P=100000 the enclosing value is approximately 25.30960790546.

For an explicit archimedean constant set

    c_0=4+log(4pi), A_r=c_0+1/(e r).

Indeed, for Re z>0 the digamma identity is

    psi(z)=log z-integral_0^infinity exp(-zt)
                         [1/(1-exp(-t))-1/t]dt.

The bracket lies between zero and one: use 1-exp(-t)<=t and exp(t)-1>=t. At z=1/4+i xi/2 this implies |psi(z)-log z|<=4. Also

    |log|z||<=log 4+log(sqrt(1+xi^2)).

Thus the fixed multiplier obeys

    |a_infty(xi)|<=c_0+log(sqrt(1+xi^2)).

Since sup_(v>=1) log(v)/v^r=1/(e r), its H^r->L2 norm is at most A_r. No numerical maximization over an unbounded frequency axis is needed.

The complete explicit fractional estimate is consequently

    ||P^(-1/2)T_P h-E_P h||_2
      <=[2 V^(1-r)kappa_1^r+(Q_P+A_r)/sqrt(P)]||h||_H^r.

At r=1/4 the bracket is enclosed near 3.97640581612, and Arb verifies it is strictly less than 4.

## 3. A sharper trace-aware first-prime bound

Direct use of the fractional extension constant is unnecessary for the first-prime error on half-line H1. Put h=E_+f, g=E_+f', and tau=f(0). Distributionally,

    h'=g+tau delta_0.

Inserting this identity into the signed-tail formula for each translation direction gives a sum of:

- the mass term d(0)h;
- a convolution of g against d(t)dt, with norm at most D_1||f'||_2;
- a reflected or unreflected half-line copy of tau d, with norm |tau|D_2.

This identity can be checked in distributions; all three displayed terms are in L2, so it is also an L2 identity. In particular it does not assert differentiability of the zero extension in ordinary L2.

The unrestricted trace estimate

    |f(0)|^2<=2||f||_2||f'||_2<=||f||_H1^2

now gives, for each direction,

    ||B_P E_+f||_2 <=(kappa_1+D_2)||f||_H1.

After both output translations the first-prime remainder is bounded by twice this expression. The D_2 term explicitly pays for the zero-extension jump; it has not been silently omitted.

## 4. Explicit unrestricted extension bound for the gamma term

For 0<r<1/2, the unitary Fourier identity

    i xi hat h=hat g+tau/sqrt(2pi)

gives an elementary extension constant. On |xi|<=1 use (1+xi^2)^r<=2^r. On |xi|>1 use

    |hat h|^2<=2|hat g|^2/xi^2+|tau|^2/(pi xi^2).

Integration, together with the trace bound above, yields

    ||E_+f||_H^r <= F_r||f||_H1,
    F_r^2=2^(r+1)[1+1/(pi(1-2r))].

Therefore the gamma contribution is bounded by A_r F_r/sqrt(P) times the half-line prior norm. The higher powers need only ||E_+f||_2<=||f||_H1.

Combining this with section 3 proves the sharper half-line estimate

    ||P^(-1/2)T_P E_+f-E_P E_+f||_2
      <=[2(kappa_1+D_2)+(Q_P+A_r F_r)/sqrt(P)]||f||_H1.

At r=1/4 the certified constants are

    A_r approximately 8.00254201166,
    F_r approximately 1.97295710944,
    total bracket approximately 0.71056475849 <0.72.

This proves the announced uniform tolerance without a zero-trace restriction and without hiding an extension-operator constant.

## 5. What is and is not calibrated

All quantities in the certificate are either finite prime sums, elementary closed-form integrals, or analytic uniform upper bounds. The cutoff response still includes its exact gamma operator and all prime powers. Numerical approximation of that response, or of the profile integrals J_+ and J_-, would require an additional numerical-field error budget.

For example, on a half-line prior ball of radius M, any independently certified normalized-field/profile discretization error epsilon can be added to 0.72M. The subsequent `finite-mesh-escape-fields-have-a-certified-end-to-end-L2-budget.md` closes the finite-representation gate: 800 noisy cell averages and a finite piecewise-exponential field give a combined normalized error below 0.74M on weighted D_1 prior balls. That theorem separately controls source tails, mesh error, coefficient noise and profile tails; it does not manufacture a measured response.

The normalized error does not define a new all-prime subtraction. Multiplying by sqrt(P) converts the result into an absolute bound for the unnormalized finite response, rather than a convergent ordinary-L2 realization.

The calibrated scalar attachment certificate and its native/inherited source budgets use their own forward maps and response norms. Likewise endpoint-tightness and finite-depth tower estimates concern source approximation. This field certificate does not identify those norms, infer an inverse, or replace the source relation ideal by an arithmetic kernel.

## Reproduction

    uv run --with python-flint python research/grothendieck/checkers/certify_uniform_escape_prior_ball.py

Output:

`research/grothendieck/results/certified-uniform-escape.json`.

Every reported strict rational bound is checked against an Arb enclosure. The finite-step sign assertions are checked individually; there is no floating-point sign inference or sampled quadrature.

Input theorem:

`research/grothendieck/fractional-source-priors-make-global-escape-uniform-and-quantitative.md`.
