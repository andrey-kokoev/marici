# A certified single-prime sine tail controls the source odd endpoint without prolate eigenvectors

## Question

Can the explicit source endpoint coefficients be paired with a certified bulk high-mode estimate in the same basis, instead of changing to an uncomputed concentration eigenbasis?

Active obligation: a quantitative fixed-support range/Schur comparison. The candidate is a direct Fourier-band leakage bound on the odd sine tail. The rival treats the conditional c_N in the previous packet as already known or discards the low–high coupling.

## Source convention and fixed support

Use the recorded gamma-minus-prime symbol

\[
a_L(u)=\frac{\operatorname{Re}\psi(1/4+iu/2)-\log\pi}{4\pi}
-\sum_{\log n\le2L}\frac{\Lambda(n)}{\sqrt n}\cos(u\log n),
\]

with the source note's unitary Fourier quadratic-form convention. Fix L=7/20. Since 2<exp(7/10)<3, the only prime-power term is n=2. This is a fixed-support theorem, not a bound uniform in the source cutoff.

The source symbol and its Fourier interpretation are from `research/voevodsky/combined-gamma-prime-symbol-localizes-the-bad-frequency-set.md`. The exterior bound below uses `research/voevodsky/binets-digamma-integral-certifies-the-safe-cutoff.md`.

## Certified global and exterior symbol bounds

For a>0, the digamma series gives

\[
\operatorname{Re}\psi(a+iy)-\psi(a)
=\sum_{m\ge0}\frac{y^2}{(m+a)((m+a)^2+y^2)}\ge0.
\]

Use psi(1/4)=-gamma-pi/2-3 log 2. The elementary bounds gamma<1, pi<22/7, log 2<7/10, log pi<23/20 and pi>3 imply the gamma term is greater than -1/2. Also log 2/sqrt(2)<497/1000<1/2. Thus

\[
a_L(u)>-1\qquad(u\in\mathbb R).
\]

At R=10000, the recorded Binet estimate gives

\[
m_\Gamma(R)>\frac{30869859979}{52800000000}
>\frac{497}{1000}+\frac1{20}.
\]

The same lower bound holds for |u|>=R: in the Binet estimate log|z| increases and both error upper bounds decrease with |Im z|. Therefore

\[
a_L(u)>\delta=\frac1{20}\quad (|u|\ge10000).
\]

These inequalities use no root isolation or numerical digamma evaluation.

## Direct sine-tail concentration estimate

On odd L2(-L,L), take e_n(x)=sin(beta_n x)/sqrt(L), beta_n=n pi/L. Let P_>N be the projection onto n>N. For the unitary Fourier transform,

\[
|\widehat e_n(u)|^2
=\frac{2\beta_n^2\sin^2(uL)}{\pi L(\beta_n^2-u^2)^2}.
\]

If beta_(N+1)>=2R, then for |u|<=R,

\[
|\widehat e_n(u)|^2\le\frac{32}{9\pi L\beta_n^2}.
\]

Let B_R denote frequency-band restriction composed with Fourier extension of the interval function. Summing the nonnegative diagonal entries bounds the norm of its tail compression:

\[
\|B_RP_{>N}\|^2
\le\sum_{n>N}\int_{-R}^{R}|\widehat e_n(u)|^2du
\le\frac{64RL}{9\pi^3N}.
\]

The last step uses sum_(n>N) n^-2<=1/N. This controls arbitrary linear combinations in the tail, not merely each basis vector independently.

For N=40000, pi>3 gives

\[
\|B_RP_{>N}\|^2<\frac{28}{1215}<\frac1{42}.
\]

The frequency separation beta_(N+1)>2R also follows from pi>3.

## Actual bulk tail lower bound

For f in the odd sine tail and the source form domain, splitting its Fourier norm across the band gives

\[
q_L(f)\ge\delta\|f\|^2-(1+\delta)\|B_Rf\|^2
\ge\frac{209}{8100}\|f\|^2.
\]

Thus the compressed high block D is bounded below by c_N=209/8100>1/40. The form is defined by the recorded symbol, not a Dirichlet surrogate. Its semibounded closed realization is obtained by restricting the weighted Fourier form to the closed odd, supported subspace and then to the finite-codimension tail. The sine basis lies in this form domain.

This supplies the formerly conditional bulk bound at this particular support and cutoff. It does not prove positivity of the full source bulk.

## Unnormalized endpoint contribution

Retain b_L(x)=sqrt(2)sinh(x/2). The preceding endpoint calculation gives

\[
\|P_{>N}b_L\|^2
\le\frac{8L\sinh^2(L/2)}{\pi^2N}.
\]

For 0<t<1, the power series implies sinh t<=t/(1-t^2). With t=7/40, this is sinh(7/40)<=280/1551. Hence

\[
\|P_{>N}b_L\|^2<\frac{686}{2706301125},
\]

and the actual compressed-bulk inverse satisfies

\[
\langle b_>,D^{-1}b_>\rangle
<\frac{2744}{279317005}<\frac1{100000}.
\]

No endpoint normalization was used to manufacture this small number. If the full physical row has a further source coefficient, it must multiply this estimate with the appropriate squared modulus.

## What remains in the finite Schur problem

Let C have low/high blocks A,B,D in this same odd basis. The full leverage still depends on

\[
S=A-B^*D^{-1}B,
\qquad b_{eff}=b_<-B^*D^{-1}b_>.
\]

The present theorem controls D and the direct endpoint tail. It has not computed A, certified B, or proved S positive. In particular a small tail endpoint contribution does not allow replacement of S by A.

The retained low odd block has dimension 40000. No such matrix was assembled, and no feasibility or positivity claim follows from giving its dimension. Sharper band estimates may reduce it, but changing the cutoff requires a fresh certified bound.

All statements use the fixed logarithmic-position source symbol. Comparison with the fully augmented two-space Sonin form, support exhaustion, and the prolate Mosco theorem retain their separate obligations.

## Disposition and verification

Constructed: a certified source bulk high-mode margin and endpoint inverse-tail bound in the same explicit sine basis. This advances beyond the prior conditional endpoint estimate without introducing prolate eigenvectors or fitting a bulk energy.

`python research/nima/checkers/check_single_prime_sine_tail_certificate.py` exits 0; ten exact rational checks pass. Result: `research/nima/results/single-prime-sine-tail-certificate.json`. The analytic input is the displayed Fourier estimate and the cited Binet/source-symbol formulas; the checker verifies the rational constants, not a numerical continuum discretization.
