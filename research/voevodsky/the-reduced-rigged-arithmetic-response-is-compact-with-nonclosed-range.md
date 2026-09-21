# The reduced rigged arithmetic response is compact with nonclosed range

## Result

On the unrestricted half-line source D_gamma=H^1(R_+,exp(2gamma u)du), gamma>1/2, the reduced map retaining the FULL Tate response and the prescribed endpoints is compact and has infinite rank. Its range in the declared weighted-dual response space is therefore not closed.

Consequently it has no bounded inverse in the source graph norm, even after quotienting by its kernel. Explicit oscillating and escaping source packets show the loss of derivative and spatial-weight control. Kernel injectivity itself is NOT settled here.

This does not contradict the output-only equivalence on the prepared, compact-spectral exponential sector: these hostile sequences lie outside that fixed sector.

Inputs:
- `../grothendieck/the-all-prime-tate-response-converges-in-a-two-sided-weighted-dual.md`
- `endpoint-and-residual-outputs-give-an-equivalence-on-the-prepared-euler-sector.md`

## 1. The reduced map and topology

Let K_gamma=L2(R,exp(-2gamma|u|)du). Define

    T_red f=(Atilde_rig E_+f, beta_end(f))
            in Y_gamma=K_gamma direct_sum C^2.

Use the Hilbert product norm, equivalent to the previously used sum norms. Splitting the first coordinate into its positive compression and negative leakage, with the prescribed signs, is an equivalent response topology. No window residual or redundant even cross-port is included.

The endpoint map is finite rank and bounded. The question is stability of reconstructing an arbitrary D_gamma input from these responses, not from a retained source coordinate.

## 2. Compactness of each response component

First, D_gamma embeds compactly into ordinary half-line L2. On a fixed bounded interval use Rellich compactness; outside [0,R] use

    integral_R^infinity |f|^2 <= exp(-2gamma R)||f||_Hgamma^2.

Thus E_+:D_gamma->L2(R) is compact.

For the prime part, each fixed translation S_a E_+ is compact D_gamma->K_gamma: factor it through the compact L2 embedding, the unitary full-line translation, and the continuous inclusion L2->K_gamma. The prime series is an operator-norm convergent sum of these compact maps, because

    ||S_(+/-log n)E_+||_(Dgamma->Kgamma) <= n^(-gamma),
    sum Lambda(n)n^(-gamma-1/2)<infinity.

Hence the entire prime response is compact.

For the archimedean map, the multiplier a_infty(xi) has at most logarithmic growth. The weighted H1 norm bounds f,f' in L1 and the trace f(0). Integration by parts gives

    |(F E_+f)(xi)| <= C_gamma ||f||_Dgamma / |xi|,  xi!=0.

Therefore the operator norm of the frequency tail |xi|>R in Atilde_infty E_+:D_gamma->L2 is O(log R/sqrt(R)). This tends to zero. Its frequency-truncated maps factor through the compact E_+:D_gamma->L2 and a bounded multiplier, so are compact. Their norm limit is compact into L2, and hence into K_gamma.

The possible zero-extension jump is covered by the trace term; no false global H1 condition is imposed. Together with finite-rank endpoints, this proves compactness of T_red.

## 3. An explicit high-frequency hostile

Choose a nonzero real chi in C_c^infinity((a,b)), 0<a<b, and put

    f_n(u)=n^(-1) exp(i n u)chi(u).

For the weighted H1 norm,

    ||f_n||_Dgamma^2
      =||chi||_Hgamma^2
       +n^(-2)(||chi||_Hgamma^2+||chi'||_Hgamma^2).

Thus the graph norm tends to a positive constant while ||f_n||_Hgamma=O(1/n). The prime and endpoint responses are O(1/n), using their H_gamma bounds.

Fourier translation of the fixed Schwartz transform of chi and logarithmic growth of a_infty give

    ||Atilde_infty E_+f_n||_L2 = O(log(2+n)/n).

Consequently ||T_red f_n||_Ygamma tends to zero. Normalizing f_n gives a unit graph-norm sequence with vanishing output. This sequence is weakly null in D_gamma, consistently with compactness.

The failure is not caused by leaving the spatial region, changing endpoint conventions, or discarding negative-side leakage.

## 4. Even the original weighted L2 source norm is not controlled

Fix a compact smooth bump chi on the positive half-line and translate it to the right with its source weight normalized:

    g_R(u)=exp(-gamma R)chi(u-R),  R->infinity.

Its H_gamma and D_gamma norms are independent of R. Its ordinary L2 norm tends to zero. Every fixed finite prime response therefore tends to zero in K_gamma. Uniform prime-tail operator bounds on H_gamma pass this statement to the all-prime response.

The archimedean multiplier commutes with full-line translation, so

    ||Atilde_infty E_+g_R||_L2
      =exp(-gamma R)||Atilde_infty E_+chi||_L2 ->0.

The endpoints satisfy exactly

    ell_+(g_R)=exp(-(gamma+1/2)R)ell_+(chi),
    ell_-(g_R)=exp(-(gamma-1/2)R)ell_-(chi).

They also tend to zero. Thus no estimate ||f||_Hgamma <= C||T_red f|| holds on the whole source domain. Dropping just the derivative from the desired inverse norm does not repair the problem.

## 5. Infinite rank: compactness is not just a finite-dimensional collapse

Fix a bounded open interval I in the positive half-line. Localize the full response to inputs C_c^infinity(I) and outputs L2(I). It is symmetric on this dense test domain in the original unweighted pairing, by the rigged Tate theorem.

A finite-rank symmetric operator from a dense domain in a Hilbert space into that Hilbert space is bounded in the underlying Hilbert norm. To see this, choose finitely many domain test vectors whose pairings separate its finite-dimensional range. Symmetry expresses the corresponding output coordinates as bounded pairings of the input against their fixed operator images. Finite-dimensional norm equivalence finishes the bound.

Now take h_n=exp(i n u)chi(u), with chi supported in I. Its L2 norm is constant. The prime form is uniformly bounded, since ||h_n||_Hgamma is constant and the prime map H_gamma->K_gamma is bounded. In contrast, Stirling's asymptotic for the independent gamma multiplier gives

    <E_+h_n,Atilde_infty E_+h_n>_0
      =-log(n)||chi||_2^2+O(1).

Indeed a_infty(xi)=log(2pi)-log|xi|+o(1) at high frequency, and the fixed Schwartz transform of chi controls the shifted integral. The localized full response form is therefore unbounded on this L2-bounded sequence.

This contradicts finite rank of the localized symmetric operator. Hence the full response, and thus T_red, has infinite rank.

## 6. Nonclosed range and what can actually be recovered

A compact operator between Hilbert spaces with closed range has finite-dimensional range: restrict to the orthogonal complement of its kernel and apply the bounded inverse theorem; compactness would make the unit ball of that complement compact. Section 5 excludes finite rank here.

Therefore Ran(T_red) is NOT closed in Y_gamma. Equivalently there is no constant C with

    dist_Dgamma(f,ker T_red) <= C||T_red f||_Ygamma.

This strengthens the explicit hostiles: even reconstruction modulo the kernel is unstable in the original graph quotient norm. It does not establish that the kernel is zero or produce a nonzero kernel vector.

There is a canonical weaker recoverable topology: on D_gamma/ker T_red use the response norm ||T_red f||_Ygamma. Its completion is isometric to the closure of the actual output range. This is a precise RESPONSE completion, not an independently identified Sobolev space and not a proof of source recovery before quotienting. The examples rule out identifying it with either of the two original source norms above.

Finding an independent analytic description of that completion, or deciding injectivity on arbitrary sources, remains a distinct problem. We do not rename the response seminorm as a new operator-domain equivalence.

## 7. Relation to the prepared-sector theorem

On a fixed compact Euler spectral family, u(z)=a(z)exp(i z x), the endpoint output already controls the whole even profile with a uniform reconstruction constant. That excludes both the unbounded-frequency and escaping-support mechanisms used here. The prepared output equivalence and its nonzero attachment observation survive unchanged.

On the unrestricted domain, even keeping BOTH response sides and endpoints does not yield a stable arithmetic reconstruction theorem. Adding the ordinary L2 demand would impose the separate already-proved zero-pole obstruction on prepared Euler responses as well.

No positivity, perfect duality, or Tate-only injectivity claim follows from this result.

## Subsequent kernel resolution

`infinite-euler-cancellation-gives-a-full-line-kernel-with-zero-endpoints.md` settles the injectivity question left open here. Polynomial endpoint factors in the admitted Blaschke source construction give an infinite-dimensional kernel of T_red on every D_gamma. The compactness and nonclosed-range conclusions remain unchanged. This is not a kernel of the five-label response retaining weak copies of the inputs.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_reduced_response_instability.py`

Checks the exact high-frequency tail integral, oscillating graph-norm identity, translated endpoint factors and prime-tail majorant. The compactness, infinite-rank and closed-range arguments are the analytic proofs above, not finite numerical rank tests.
