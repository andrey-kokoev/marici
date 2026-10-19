# RH analytic completion: induced riggings, not ordinary log-tempered combs

Dictionary: `research/conjecture_net/contracts/rh-stage-dictionary.v1.json`.
Ledger/receipt: `research/voevodsky/results/rh-analytic-completion-audit-v1.json`.
Checker: `research/voevodsky/checkers/check_rh_analytic_completion_audit.py`.

Fresh controls: `uv run research/voevodsky/checkers/check_rh_analytic_completion_audit.py --replay`. Normal runs verify the retained ledger and source freshness. The mathematical extension arguments below are not proved by finite or numerical tests.

## Result and crucial distinction

The five required analytic cells have declared topologies and extension witnesses. The radial/spectral completion is an **induced rigging** transported from additive Schwartz space. Its strong anti-dual includes combs and endpoint distributions. It is not ordinary tempered distributions in log radius, and does not assign a globally convergent Mellin integral or an L2 norm to raw combs.

The often tempting stronger extension to ordinary log-tempered distributions is false: both the radial image of the constant distribution and the positive integer comb have exponential, not polynomial, growth against translated log tests. This rejected ambient-space identification is recorded as a regression boundary; the actual induced completion is specified independently by the existing U and Fourier maps.

Analytic choices remain supplied: additive self-dual Fourier normalization, half-density chart, heat/mesh conventions and the induced topology. Nothing here derives them from the twelve-arrow source, identifies a physical realization, constructs a positive Weil pullback or proves RH.

## 1. Generic finite comb domain

Let V_a be the four-dimensional generic comb span, 0<a<1, a != 1/2. Each port is tempered: for N>1, the absolutely convergent lattice sampling bound controls its value by the Schwartz seminorm p_(N,0)(phi). B_a:R^4 -> S'(R)_beta is therefore continuous.

Choose compactly supported smooth probes isolating atoms at a,1-a,0,1. The first two separate the shifted supports; the integer character rows at 0 and 1 have determinant 2i sin(2pi a), nonzero for the declared generic shifts. Thus B_a is injective. A finite-dimensional subspace of a Hausdorff locally convex space has its ordinary finite-dimensional topology and is closed. Consequently B_a is a topological isomorphism onto V_a; coordinate reconstruction on V_a is continuous. No uniform inverse is asserted as a -> 0 or 1/2: specialization changes rank.

The coefficient Gram is a chosen norm on this finite span, not the real-line L2 norm of its distributions. Full twelve-coordinate reconstruction still requires the retained hidden archive.

## 2. Explicit complete radial test space and endpoints

For ordinary functions use the already fixed unitary chart

    (U f)_epsilon(u)=exp(u/2) f(epsilon exp(u)).

Define E_r=U S(R), with the **transported Schwartz Frechet topology**, not the topology merely inherited from S(R)^2 or L2. Its seminorms are

    p_(N,k)^r(g)=sup_x (1+|x|)^N |d^k/dx^k [U^-1 g](x)|.

Here U^-1 g on x != 0 is |x|^-1/2 g_(sgn x)(log|x|); at zero it has the unique smooth extension required by g in E_r. Thus U:S(R) -> E_r is by construction a topological isomorphism and E_r is complete and nuclear. Its inclusion into L2(du)^2 is continuous and dense: U is unitary and S(R) is dense in additive L2. E_r also embeds continuously into ordinary two-channel log Schwartz space; the transported topology is stronger.

The two channels are not independent at u -> -infinity. Their asymptotic jets encode the SAME smooth additive test function:

    g_+(u) ~ exp(u/2) sum_k phi^(k)(0) exp(ku)/k!,
    g_-(u) ~ exp(u/2) sum_k (-1)^k phi^(k)(0) exp(ku)/k!.

In particular phi(0)=lim_(u->-infinity) exp(-u/2)g_+(u), equally from the minus channel. Evaluation at zero and all its derivatives are continuous for the transported seminorms. They are not lost merely because U is defined almost everywhere as a Hilbert chart.

Use continuous **anti-duals** throughout the rigging, with source pairing <T,phi>=T(conjugate phi). This is the usual distribution space after the explicit conjugation convention. For a chart A, transport by

    <A^times T, A phi>=<T,phi>.

This convention agrees with A on Hilbert states when A is unitary, and avoids silently using the wrong Fourier transpose. On test functions and duals Fourier is transported with its actual adjoint/inverse as appropriate.

U^times identifies S'(R)_beta with the strong anti-dual E_r^times. The zero atom becomes the continuous endpoint-evaluation functional above. The constant distribution becomes integration against exp(u/2) in both channels on these induced tests. Nonzero atoms have the existing |x0|^-1/2 log-atom formula. Endpoint derivatives also exist in the ambient rigging; the finite comb orbit only uses the required zero atom. No canonical splitting into arbitrary bulk and independent endpoint values is imposed.

Since additive Fourier is a continuous automorphism of S(R), W_r=U F U^-1 is a continuous automorphism of E_r; its strong anti-dual action is continuous. It has exactly the Fourier-coupled endpoint laws F delta_0=1 and F 1=delta_0. This is a completion from actual source test functions, not a freely completed endpoint fixture.

### Why ordinary log-tempered space is wrong

For T=1, the radial density is exp(u/2) on each channel. Pairing with a fixed nonnegative bump translated by R grows as c exp(R/2). A tempered distribution admits only a polynomial bound in R on such translated fixed bumps. Hence this density is not log-tempered.

For the positive integer comb, U^times T restricted to compactly supported log tests has weights n^-1/2 at log n. Take a fixed bump >=1 on [0,log 2], translated by log m. The block m <= n <= 2m contributes at least (m+1)/sqrt(2m), growing as sqrt(m), not a polynomial in log m. Thus that comb image is not log-tempered either. These functionals ARE continuous on E_r, whose seminorms on those translating bumps grow exponentially. There is no contradiction.

Compactly supported log tests alone also cannot see delta_0: their inverse additive tests vanish near zero. Passing only to D'(R)^2 would therefore forget the endpoint unless additional source-induced data were retained. E_r keeps it intrinsically.

## 3. Mellin/Fourier completion and exact gamma operation

Let V=(2pi)^(-1/2) M_log be normalized log Fourier, acting diagonally on both channels. Define E_s=V E_r with transported Frechet topology. It is complete and dense in L2(dt)^2; V:E_r -> E_s is a topological isomorphism. Its strong anti-dual is the spectral distributional target. It is not asserted to equal all ordinary S'(t)^2, nor to consist only of meromorphic functions.

The scalar normalization of V cancels from the operator square, so the existing gamma matrix G(t) is unchanged. The prior operation audit derived on compactly supported smooth log inputs, with Abel regulator delta>0,

    m_(sigma,delta)(t)=Gamma(1/2-it)(delta+2pi i sigma)^(-1/2+it),
    H=G(t)R_t, R_t f(t)=f(-t).

For real t, the even/odd gamma branches have modulus one. Indeed q(t)q(-t)=1/[2 cosh(pi t)] by Euler reflection; the cosine and sine reflected products equal cosh(pi t)/2. The even reflected multiplier is its conjugate; the odd one is minus its conjugate. Their products +1 and -1 therefore both imply modulus one. The normalized parity basis is unitary, so G(t) is unitary and H is bounded of norm one on L2.

The Abel multipliers are uniformly bounded for 0<delta<=1: |Gamma(1/2-it)|^2=pi/cosh(pi t), |arg(delta+2pi i sigma)|<pi/2, and the modulus of the rate is >=2pi. This gives a constant bound independent of t and delta (each scalar multiplier is <=1). Dominated convergence supplies strong L2 convergence of the regulated multipliers to m_sigma. The regulated integral is absolutely integrable for compact log inputs; its sum-kernel substitution produces the reflected t argument. The resulting identity

    V W_r=H V

holds on that dense core and extends to all L2 by boundedness and Plancherel. This is a standard analytic density argument, not a sampled matrix extrapolation.

Now H maps E_s continuously onto E_s, because on this image

    H=V U F U^-1 V^-1

and F is continuous on additive Schwartz space. Its adjoint is the corresponding inverse, also continuous. Thus the same operation extends to E_s^times by anti-duality and commutes with the transported source maps, including delta_0 and 1. G(t)G(-t) is channel swap; four Fourier operations return exactly.

This supplies a genuine completed **test/dual operator** square for raw combs. It does NOT interpret a raw comb as a Hilbert vector, permit point evaluation of every spectral functional, or manufacture an ordinary integral against exp(-itu). The generic Hurwitz/polylogarithm descriptions are separate meromorphically continued readouts of the designated comb seeds. Their initial absolute-convergence regions and endpoint subtraction remain required; they are not assigned to arbitrary l2 packets.

## 4. Lattice continuity, bonding and strong Gaussian limit

For fixed h>0, c in l2(Z) and phi in S(R),

    |sum_n c_n phi(hn)|
      <= ||c||_2 [sum_n |phi(hn)|^2]^(1/2)
      <= C_(h,N) ||c||_2 p_(N,0)(phi), N>1/2.

Consequently j_h:l2(Z) -> S'(R)_beta is continuous, uniformly on bounded sets of tests. The constant depends on h; no mesh-independent unweighted bound is claimed as h -> 0.

For periodic lifting, write its distribution pairing as the normalized-torus pairing of f with

    phi_h(theta)=h^-1 sum_k phi((theta+k)/h), 0<=theta<=1.

The same rapid-decay bounds control ||phi_h||_2 by C_h p_(N,0)(phi). Thus L_h:L2(T) -> S'(R)_beta is continuous. Finite packets are dense in l2, lattice Fourier is unitary, and real Fourier is continuous on S'(R)_beta. The finite identity F_R j_h=L_h F_lattice therefore extends to these stated spaces. Neither atoms nor nonzero periodic lifts are identified with L2(R) vectors. Finite convolution remains a finite-packet operation; no false l2 convolution-algebra closure is inferred.

For any fixed finite channel dimension D, the sampling proof uses N>D/2 and the periodized test is h^-D sum_(k in Z^D) phi((theta+k)/h). The corresponding square is in S'(R^D), not S'(R). This preserves channel permutations and proves the multichannel continuity statement without choosing a zeta coordinate. The two-channel radial/spectral discussion above is the declared one-coordinate route, not an automatic reduction of that multichannel source.

Dyadic bonding n -> 2n is an l2 isometry and satisfies j_(h/2)i=j_h. The induced radial and spectral maps are topological isomorphisms on strong duals, so these bonding squares transport as well.

For fixed t>0, set f(x)=exp(-pi t x^2)phi(x). The rectangle-rule estimate is

    |h sum_n f(hn)-integral_R f(x)dx| <= h ||f'||_1.

It follows by integrating |f(hn)-f(x)| on each mesh interval and summing. Gaussian decay bounds ||f'||_1 uniformly for phi in a bounded Schwartz set. Hence the sampled Gaussian measures converge in the STRONG tempered-distribution topology, not merely pointwise on individual tests. Continuity of Fourier, U^times and (VU)^times transports that limit. This fixes the required topology/limit witness without importing a unitary l2-to-L2(R) embedding.

## 5. Theta, endpoints and analytic continuation

Use the supplied unit unshifted comb, Gaussian and self-dual measure. Poisson summation on Schwartz Gaussians gives theta(t)=t^-1/2 theta(1/t). For Re(s)>1 the absolutely convergent half-theta Mellin integral is Lambda(s)=pi^(-s/2)Gamma(s/2)zeta(s).

After splitting at t=1,

    Lambda(s)=1/[s(s-1)]
       +1/2 integral_1^infinity (theta(t)-1)
                   [t^(s/2)+t^((1-s)/2)] dt/t.

For t>=1, theta(t)-1=2 sum_(n>=1)exp(-pi n^2 t) <= C exp(-pi t). On every compact s-set, both powers and all s-derivatives are bounded by polynomial powers of t and log t. Gaussian decay supplies an integrable uniform majorant. The tail integral is therefore entire, including differentiation/limit transport, by the standard parameter-integral theorem.

The endpoint monomials carry D_s=diag(s,s-1); its determinant s(s-1) cancels exactly the pole packet. Thus xi(s)=s(s-1)Lambda(s)/2 is entire and has endpoint constant 1/2. Reflection swaps the two endpoint modes and preserves the completed expression. The zero-removed comb is not Fourier fixed: F(Delta-delta_0)=Delta-1, retained by the rigging above.

These are analytic witnesses under declared conventions, not laws derived solely from the finite carrier. Rank-one coefficient specialization and all source/history archives stay as recorded. No zero-location theorem follows from entire continuation or reflection.

## Cell ledger and verification boundary

- `generic-domain`: continuous finite-dimensional tempered realization and continuous coordinate inverse at generic shifts.
- `radial-endpoint-domain`: complete induced Frechet test space, strong dual transport and source-coupled zero endpoint.
- `mellin-domain`: dense-core bounded extension, induced complete spectral rigging and anti-dual operator square, not ordinary raw-comb Mellin integration.
- `lattice-continuity`: fixed-mesh l2/torus continuity, bonding and strong Gaussian/Fourier limits.
- `theta-completion`: absolute-convergence start, entire tail with uniform majorant and exact pole/endpoint normalization.

The fresh checker replays the lattice and Riemann suites with unchanged pinned receipts and independently checks parity/adjoint algebra, inverse half-density differentiation, endpoint jets, Gaussian L1 error constants, pole cancellation and normalization. Structural hostiles reject ordinary log-tempered/Hilbert substitution, endpoint loss and unjustified all-packet pointwise Mellin claims. These checks support the note; they do not replace the functional-analysis and parameter-integral arguments, and no formal compiler closure is claimed.
