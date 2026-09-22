# Translated cubic observers have sharp Gaussian source growth

## Result

The translated family of Voevodsky's actual cubic residual-gap observers supplies a concrete, sharp instance of the observer-growth criterion.

Let A=2Q be the initial arithmetic vertex, keep event primes (2,3,5,7,11,13), and let A tend to infinity through admitted backgrounds. Fix 1/2<gamma<y<beta and the same spectral point iy. On the entire two-feature, six-event I^3 corner, with actual-letter source norm q_R=6!R^6||.||_Gamma, the observer norm satisfies

`a_R(A) ~ C A^(-2beta-7) exp(101 pi A^2)`,

`C=w_seam/[64*6!*y^2*R^6*pi^3*10^(beta+7/2)] >0`.

The source norm is NOT determined by testing only the original positive witness. A crossed diamond product, also an actual I^3 source in the same packet, dominates it.

In contrast, the observer norm on the independently noisy four-sector response space grows as

`constant * A^(-2y-5) exp(904 pi A^2)`.

These are different norms. The much larger response calibration norm must not be substituted for the sharp source-functional norm.

Consequences: no polynomial prior in this family's arithmetic location controls uniform observation tails. Gaussian-exponential priors have the exact threshold in section 6. No numerical calibration for these late windows is asserted.

## 1. Actual translated packets and normalization

Use `../voevodsky/two-residual-gaps-detect-the-adjacent-cubic-attachment.md`. Translate its arithmetic background, not the theta forcing. The actual selected windows are

`A_1=[log A,log(2A)]`, `A_2=[log(2A),log(6A)]`,

`B_1=[log(6A),log(30A)]`, `B_2=[log(30A),log(210A)]`.

The forgotten third diamond uses primes 11,13 and ends at 30030A. Retain every original packet/background label. For example, an infinite admitted sequence of backgrounds coprime to the six event primes suffices. The source remains the same arithmetic path category; no new kind of edge or independently copied root state is introduced.

Use the completed theta normalization

`Phi(x)=exp(x/2) sum_(n>=1) (4q_n^2-6q_n)exp(-q_n)`,

`q_n=pi n^2 exp(2x)`.

For a window [log A,log(pA)] write X(A,p) for its cosh(yx)Phi integral, mu(A,p) for its x tanh(yx) weighted mean, and

`gamma(A,p)=sqrt(w_seam)||1_window Phi||_beta`.

The observer is exactly the four-sector signed product of o_0/X_F from the cubic note, with o_0=(exp(-yu),-2L_0 exp(-yu)) and L_0=(xi'/xi)(1/2+y). Its physical multiplier is w_seam^2. The scalar field conventions are unchanged; norms apply equally to the corresponding conjugate-linear evaluation convention.

## 2. Boundary Laplace estimates for the actual theta windows

For each fixed p>1, uniformly over the finite prime choices needed below,

`X(A,p) ~ pi A^(y+5/2) exp(-pi A^2)`,

`gamma(A,p) ~ 2 sqrt(w_seam) pi^(3/2)
                 (1+log A) A^(beta+7/2) exp(-pi A^2)`,

`mu(A,p)=log A+o(1)`.

Here the theta first atom has relative error O(A^(-2))+O(exp(-3pi A^2)) against 4pi^2 A^(9/2)exp(-pi A^2). Positivity and the standard theta tail majorant make this uniform for x>=log A. In the variable t=exp x, the leading X integrand is 2pi^2 t^(y+7/2)exp(-pi t^2). Boundary Laplace integration gives its displayed coefficient pi. The second cosh exponential is relatively O(A^(-2y)). The finite upper endpoint pA gives an exponentially smaller contribution.

For the squared forcing norm the leading integrand in t is

`16pi^4 (1+log t)^2 t^(2beta+8) exp(-2pi t^2)`.

Its boundary integral is asymptotic to 4pi^3(1+log A)^2 A^(2beta+7)exp(-2pi A^2). Taking the square root and restoring sqrt(w_seam) gives gamma.

The positive probability density defining mu concentrates within an x-distance O(A^(-2)) of log A. Since h_y(x)=x tanh(yx) has bounded derivative there and h_y(log A)=log A+o(1), the mean formula follows. In particular the two consecutive-window gaps tend to log 2 and log 5.

These are actual-source asymptotics, not estimates for arbitrary invented small letters.

## 3. The full minimal cubic source basis

In a two-event diamond, the ideal has one forgotten relation and one mixed-mark relation; there is no relation with two retained marks. This follows directly from the independent terminal-potential coordinates, or the two-event source presentation.

Every factor in I has length at least two. Therefore the six-event, two-feature component of I^3 is spanned by products of three two-event relations. Choose an ordered partition of the six primes into three unordered pairs and choose which one of the three factors is forgotten. This gives 90*3=270 products.

Their marked-path supports are pairwise disjoint: a path determines its unordered first, second and third two-event blocks, and its retained count in each block. Each product has 32 distinct paths with coefficient magnitude one. These products are therefore an independent basis, and their Gamma coefficient norms add without cancellation between basis elements.

Consequently the norm of ANY source functional on this component is exactly the maximum of its absolute value on these basis products divided by their q_R norms. This is an analytic norm statement justified by the actual disjoint source supports, not a sampled matrix norm.

## 4. Exactly two basis products are seen

Only the following products have a nonzero selected-sector projection:

`v_0 = mixed(2,3) mixed(5,7) forgotten(11,13)`,

`v_cross = mixed(2,5) mixed(3,7) forgotten(11,13)`.

Their four selected-sector coefficient vectors, ordered (A_1B_1,A_1B_2,A_2B_1,A_2B_2), are respectively

`(1,1,1,1)` and `(0,1,0,0)`.

To see exhaustiveness, the chosen forgotten seam 11 starting at 210A is the fifth event, fixing the final pair. The retained A_1 seam is the first event 2, whereas A_2 is the second event 3 following 2. The B_1 seam is event 5 in position three after 2,3, whereas B_2 is event 7 in position four after 2,3,5. All routes are therefore fixed except A_1B_2, where the forgotten events 3 and 5 between the two features can exchange order. That exchange gives the crossed pair partition. Vacuum buffers exclude other retained-degree distributions.

Thus the exact scalar values are

`S_0=w_seam^2/(2y^2)
       [mu(2A,3)-mu(A,2)] [mu(30A,7)-mu(6A,5)]`,

`S_cross=-w_seam^2/(2y^2)
             [mu(A,2)-L_0][mu(30A,7)-L_0]`.

The crossed product is not the original positive witness. It is an admissible source on which the SAME observer is tested. Its negative, eventually nonzero value is used only to compute the observer norm.

## 5. Exact source norm and its asymptotic

Put

`S(A;p,q)=gamma(A,p)+gamma(pA,q)+gamma(A,q)+gamma(qA,p)`.

The two source norms are exactly

`||v_0||_Gamma=2 S(A;2,3) S(6A;5,7)`,

`||v_cross||_Gamma=2 S(A;2,5) S(10A;3,7)`.

The factor two is the forgotten third diamond. Disjoint supports and section 4 prove

`a_R(A)=max(|S_0|/[6!R^6||v_0||_Gamma],
            |S_cross|/[6!R^6||v_cross||_Gamma])`.

Each S(A;p,q) is asymptotic to twice the leading gamma at A. Therefore the first ratio has order

`A^(-2beta-7)(log A)^(-2) exp(37pi A^2)`,

while |S_cross| is asymptotic to w_seam^2(log A)^2/(2y^2), and

`||v_cross||_Gamma ~32 w_seam pi^3 10^(beta+7/2)
  (1+log A)(1+log(10A)) A^(2beta+7) exp(-101pi A^2)`.

The second ratio dominates and gives exactly the constant C in the result. Uniform native/inherited comparisons at fixed event length six preserve this growth order; numerical leading constants depend on which presentation norm is chosen.

## 6. A sharp sufficient prior and a genuine obstruction

Apply `observer-growth-versus-source-priors-controls-uniform-finite-certification.md` to this fixed-shape translated family, now on its admitted I^3 homogeneous corners. Arithmetic A is a proper location parameter on this family because its event set and other type fields are fixed. This does not identify A with an arbitrary full-source label coding.

Consider prior weights

`W_(c,d)(A)=max(1, exp(c pi A^2) A^d)`.

For c>0 the maximum does not affect large A. The exact observer/prior ratio is asymptotic to

`C A^(-2beta-7-d) exp((101-c)pi A^2)`.

Hence uniform finite-packet observation on the corresponding prior ball holds:

- for c>101, for every fixed d;
- for c=101, exactly when d>-(2beta+7).

For 0<c<101 it fails with unbounded tail amplification. At c=101,d=-(2beta+7) the tail stays nonzero; below that polynomial threshold it is unbounded. Every fixed polynomial weight in A also fails. In particular W=exp(101pi A^2) is sufficient, while a weight merely comparable to a_R(A) is insufficient: their ratio must actually vanish.

The hostile source can be chosen explicitly as v_cross rescaled to spend the entire prior budget in one increasingly late corner. Every such vector is a genuine finite I^3 source. This is not a kernel of the attachment or a new source relation.

These are asymptotic existence/rate results. An explicit finite cutoff for a prescribed numerical tolerance would require certified remainder bounds, not just the asymptotic equivalences.

## 7. Response-noise calibration has a different growth rate

Measure the four selected UNscaled response tensors in the direct sum of their projective response norms. Let t_0>0 be the norm of the fixed one-slot functional y->conjugate(<E o_0,y>) on the declared response space. It is finite and independent of A. On this ambient measurement space, independent sector errors are permitted.

The observer norm is exactly

`t(A)=w_seam^2 t_0^2 max_(i,j) 1/[X_(A_i)X_(B_j)]`.

The elementary tensor functional has product norm, and the dual of the four-sector l1 sum has maximum norm. For large A the maximum is attained at A_2,B_2. Section 2 gives

`t(A) ~ [w_seam^2 t_0^2/(pi^2 60^(y+5/2))]
           A^(-2y-5) exp(904pi A^2)`.

Thus a sufficient response-noise tolerance for a fixed scalar accuracy decays at the reciprocal of this much larger rate. This is the norm of the given calibrated observer on ambient noisy responses, NOT the norm of its restriction to actual cubic source images. No arbitrary noisy tensor is asserted to lie in that image.

At the previously calibrated parameters beta=4,y=3, the source growth is A^(-15)exp(101pi A^2), while the response-test growth is A^(-11)exp(904pi A^2), up to fixed positive constants. The old four-event numerical tolerance is not transferred to these later cubic packets.

## 8. Scope

This supplies actual norm-growth input for a genuine family of residual-sensitive adjacent attachment observers, including its matching source obstruction. It keeps arithmetic coefficients, theta normalization, physical seam weights and the source ideal fixed.

It does not prove uniform nonzero margins for one infinite summable source, optimize the observer among other representatives of the same source functional, or reconstruct sources from responses. The original two-gap witness remains strictly positive; the crossed product is the separate source-norm extremizer asymptotically.

## Verification

`uv run --with sympy python research/nima/checkers/check_translated_cubic_observer_growth.py`

The checker enumerates all 270 actual minimal cubic basis products and their disjoint supports, verifies exactly the two visible products and their sector coefficients, and checks the scalar and leading-constant formulas. Actual theta asymptotics and infinite prior thresholds are proved above, not inferred from finite sampled window values.
