# Matched private corrections attain the full cubic observer norm

## Result

At A=2, y=3, gamma=1, the FULL finite-background optimization is solved in the declared continuous-response dual. The source functional is unchanged on all 270 cubic basis products.

In the same unscaled labelled l1 sum of ordered projective response tensors used by Voevodsky's optimization theorem, the optimal observer norm is

    ||Lambda||_opt / w_seam^2
      = |S_x| / [64 N([2,20]) N([20,420])].

Here S_x is the original crossed source value per w_seam^2, and N([a,b]) is the full five-label response norm of the prepared forcing interval [log a,log b]. The intervals in this formula are unions of existing windows; they are not new event generators or new measured channels.

Fresh Arb/Acb verification gives

    3.369 * 10^537 < ||Lambda||_opt / w_seam^2
                  < 3.480 * 10^537.

The unrounded enclosure ratio is below 1.033. This is uncertainty in evaluating an EXACT optimum formula, not an unclosed optimization gap. The optimum is about 2000 times smaller than the previous one-private-row-per-visible-basis residual observer norm, in the same full data norm.

The norming observer uses 256 crossed-image shape blocks, 192 matched private correction blocks, and one reserved positive private block: 449 existing analytical blocks in total.

This is an ideal continuous-response observer. A finite numerical implementation of its norming tests, with calibration and acquisition error budgets, is not certified here. Nor is any all-depth or source-realization conclusion asserted.

## 1. Fix the protocol before identifying analytical blocks

Use the unscaled response carrier specified in

`../voevodsky/alternative-balanced-sectors-reduce-cubic-response-amplification-to-sharp-gaussian-order.md`, section 1.

Its norm is the labelled l1 sum of the ordered projective response tensors, including memory slots. Retain all five one-feature labels. The original functional retains its physical factor w_seam^2. No source Gamma norm replaces the response norm; no new shape-dependent rescaling is introduced. A protocol incorporating additional nonuniform shape weights would require a separate optimization and matching audit.

A balanced analytical block is determined by its ordered marked seams and the number of retained feature slots in each coefficient buffer. Buffer endpoints are already determined by the seams and the fixed outer corner. The actual forcing vectors in those slots are NOT additional independent noisy channel labels.

The analytical-shape checker builds each source column from the actual marked two-event paths. It retains the ordered actual forcing windows in all memory and seam slots. Expanding each buffered window as its terminal potential difference reproduces the owning terminal recorder EXACTLY, column by column.

The counts are:

- 270 source basis products;
- 256 distinct analytical blocks in each source column;
- 48960 analytical blocks in the union;
- 34560 blocks supported on one column, 11520 on two, and 2880 on four;
- 192 distinct actual event windows.

In particular, there are no within-column analytical block collisions. The earlier 108720 formal potential keys are not 108720 independent analytical measurement channels.

## 2. One unit test simultaneously norms every positive window

Put e(u)=exp(-3u), c=O(e,0), v=(0,0,0,e,0),

    C=||c||=C_even, h=||e||_Hminus=1/sqrt(8), L=xi'(7/2)/xi(7/2).

The vectors c and v occupy disjoint response coordinates. Choose a norm-one functional on the four nonresidual coordinates attaining C at c, and the norm-one residual functional attaining h at v. Their sum theta has norm one in the dual of the five-label sum norm and satisfies

    theta(c)=C, theta(v)=h.

This is an ordinary response-dual norming construction, not a source inverse or a modification of the arithmetic operator.

For an actual interval F, the prepared response is

    O Psi(F)=sqrt(2) X_F [c+(mu_F-L)v].

Every interval begins at least at log 2, and the theta density is positive. Since x tanh(3x) is increasing there,

    mu_F >= log(2)tanh(3 log(2)) > L.

The final inequality is Arb-verified. Consequently the SAME theta norms every actual window:

    N(F)=||O Psi(F)||
        =theta(O Psi(F))
        =sqrt(2) X_F [C+h(mu_F-L)].

Theta tensor theta likewise norms every ordered window-pair tensor. This positivity also makes N additive on consecutive forcing intervals. No assertion that arbitrary response vectors have additive norms is used.

## 3. An exact all-column norming certificate

Let x=18 be the crossed column v_x=mixed(2,5)mixed(3,7)forgotten(11,13). On each of its 256 analytical blocks place theta tensor theta with the source coefficient sign. Call this preliminary test J_x.

It norms Y(v_x), but shared blocks can also see other source columns. For every shared contribution on another column j, the checker finds an unused globally private block of column j carrying EXACTLY THE SAME ordered actual feature windows. Put the opposite signed test on that private block.

The feature tensors on the shared and private blocks agree as response tensors, not just in asymptotic size. Thus their contributions on column j cancel identically. A private correction changes no other column and no target block. Distinct corrections occupy distinct blocks.

The matching uses 192 private blocks. A private A_1,B_1 block for column 0 is reserved in advance and never used in the correction. The checker verifies cancellation as an integer polynomial in ordered window pairs, on ALL 270 columns:

    J_x(Y(v_j))=0 for j!=x,
    J_x(Y(v_x))=||Y(v_x)||.

Every nonzero block coefficient is +1 or -1, so ||J_x||=1. This is exact feasibility, independent of floating LP tolerances, interval moment estimates, or a witness-only cancellation hypothesis.

## 4. The crossed source gives both the lower bound and the optimal extension

Every admissible observer representing the original functional satisfies

    ||Lambda||/w_seam^2 >= |S_x|/||Y(v_x)||.

Let R_0 be the signed theta-tensor test on the reserved positive block, and let n_0=N(A_1)N(B_1). Then R_0 sees only column 0 and R_0(Y(v_0))=n_0. Define

    Lambda/w_seam^2
      =(S_x/||Y(v_x)||) J_x + (S_0/n_0) R_0.

Its source values are exactly S_0,S_x and 268 zeros. Its two terms have disjoint block supports, hence

    ||Lambda||/w_seam^2
      =max(|S_x|/||Y(v_x)||, |S_0|/n_0).

Arb certifies that the second term is less than 10^(-340) times the first. Therefore the lower bound is attained. If using the original conjugate-linear first-slot convention, conjugate the resulting linear observer; the source identities and operator norm are unchanged.

This proves optimality over the ENTIRE continuous full-output dual, not merely over the selected 449 blocks or the fixed residual-test family.

## 5. Evaluate the exact crossed image norm

A mixed two-event diamond has four marked paths and two cuts per path. Each of its four actual retained windows occurs in two derivative terms. A forgotten diamond has four scalar derivative terms.

There are no within-column shape collisions. Thus for the two mixed blocks of v_x,

    ||Y(v_x)||=16 (sum_first_four_windows N(F))
                  (sum_second_four_windows N(G)).

The two paths of the first diamond each partition [log 2,log 20]. Additivity from section 2 gives a first sum equal to 2N([2,20]). Similarly the second sum is 2N([20,420]). This proves

    ||Y(v_x)||=64 N([2,20])N([20,420]).

The scalar unions simplify the norm calculation only. The observer still measures and tests the original distinct blocks.

## 6. Rigorous evaluation of C_even

The all-prime even response is evaluated in its declared weighted-dual norm, never in undamped ordinary L2. Write s=7/2, beta=gamma+1/2=3/2 and L(q)=xi'(q)/xi(q).

The supplied endpoint-subtracted residual transforms, with the prescribed endpoints restored, give the UNSUBTRACTED half-line transforms

    H_+(q)=-(L(s)+L(q))/(s+q-1)
              +1/[s(q-1)]+1/[(s-1)q],

    H_-(q)=(L(q)-L(s))/(q-s)
              +1/[(s-1)(q-1)]+1/(sq).

These follow from `full-residual-reflection-confirms-the-infinite-euler-kernel.md` and its owning full-line calculation. The signs of the O labels do not affect their norms. Weighted Laplace Plancherel and real conjugation symmetry give

    ||bulk_+||^2=(1/pi) integral_0^infinity |H_+(beta+it)|^2 dt,
    ||bulk_-||^2=(1/pi) integral_0^infinity |H_-(beta+it)|^2 dt.

Hence

    C_even=||bulk_+||+||bulk_-||
              +sqrt(1/s^2+1/(s-1)^2)+1/sqrt(8).

The checker encloses every real frequency cell through T=2048 with Acb, using the zeta power series for its derivative. It does not use point samples as integral bounds or take a complex absolute value inside an analytic quadrature callback.

For completeness the infinite tail is explicit. For Re z>0,

    psi(z)-log z=-integral_0^infinity exp(-zt)b(t)dt,
    b(t)=1/(1-exp(-t))-1/t.

Here b(0)=1/2, b(infinity)=1, and b'(t)>=0. One integration by parts yields

    |psi(z)-log z| <= 1/|z|.

On beta+it, Euler absolute convergence gives |zeta'/zeta|<=P_beta=-zeta'(beta)/zeta(beta). For t>=T,

    |L(beta+it)| <= (1/2)log t + c_L,

    c_L=P_beta+3/T-(1/2)log(2pi)+pi/4
                         +(1/4)log(1+(beta/T)^2).

Put A_tail=c_L+|L(s)|+1/s+1/(s-1) and Q=A_tail+(1/2)log T. Each squared half-line norm has remaining tail at most

    (Q^2+Q+1/2)/(pi T).

This needs no zero-location hypothesis and no prime cutoff approximation. The resulting C_even enclosure is contained in the printed ball [2.0 +/- 0.0309].

The final checker freshly recomputes this norm enclosure, the original source values, and the completed-theta data for both union intervals. Its unrounded optimal-norm endpoints are approximately

    3.36929111288014 * 10^537,
    3.47990386225722 * 10^537.

## 7. Discovery, scope and remaining implementation work

The finite LP was useful for discovery: its leading-window numerical solution selected the crossed column itself as the norm witness. That numerical proposal is explicitly marked uncertified. The proof above instead uses exact window matching and a separate all-prime norm enclosure; no leading-window approximation survives in the final certificate.

The optimum here is over continuous response-dual tests. No claim is made that the norming waveforms lie in a smaller smooth graph-test core, or that a finitely sampled implementation attains the ideal value. Such an implementation needs its own approximation, calibration, and noise budget.

This result neither reconstructs private measurements from old noisy data nor uses frame consistency to certify correctness. Nima's `frame-discrepancy-observers-form-a-compatible-consistency-tower.md` still concerns consistency under already admitted transitions; a shared bias remains invisible there. The present scalar observer is constructed directly on existing measured response blocks. No corrected tower, extension class, summable source realization or depth-uniform bound is inferred.

## Verification and artifacts

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_exact_full_cubic_observer_norm.py

This freshly checks source-block descent, every matching cancellation, the all-prime norm weight, original source values, and the sharp lower/upper comparison.

Artifacts:

- `results/cubic-analytical-shapes.json`;
- `results/exact-cubic-norming-rows.json` (all 192 matches and reserved row);
- `results/even-response-norm.json`;
- `results/exact-full-cubic-observer-norm.json`.

Optional numerical discovery:

    uv run --with sympy --with numpy --with scipy python research/grothendieck/checkers/propose_full_cubic_observer_lp.py
