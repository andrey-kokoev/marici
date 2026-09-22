# Translated cubic reconstruction is compact and requires quantitative tail priors

## Result

The certified 270-row inverse does NOT extend to a uniformly stable inverse in raw scalar l1 noise as arithmetic backgrounds grow. This failure already occurs at fixed depth three; increasing depth is not needed.

On the specified labelled family of translated cubic packets:

- the actual-letter inverse grows like A^4;
- the unweighted path inverse grows like exp(c A^2) times inverse polynomial/logarithmic factors;
- the forward observation map is injective and compact in either corresponding source Banach norm, so its inverse on its range is not continuous in raw l1;
- an explicit background-moment prior gives conditional recovery: a Holder rate in the actual-letter norm, but only a logarithmic rate in the path norm.

The two rates have matching deterministic-noise lower bounds in their respective prior classes. These are statements about this fixed acquisition protocol, not impossibility results for every conceivable observer family.

## 1. A precisely restricted source family

Translate the same six-event two-feature cubic packet to admitted arithmetic backgrounds A>=2, retaining the actual background/outer-corner labels. One may use an unbounded integer family coprime to the event primes. At each A use the same 270 disjoint-support basis products v_(A,j) and their private scalar readings.

Different backgrounds have different outer corners, so the source norms add. The labelled observation map is diagonal:

`z_(A,j)=E_(A,j) a_(A,j)`,

where x=sum_(A,j) a_(A,j)v_(A,j). No off-packet source is admitted in this theorem, and no source-module closure of this restricted family is claimed.

Put w=w_seam and normalize the actual-letter target norm by the fixed physical constant:

`q(x)=Q_1(x)/w`.

On this family every source term has six events, so Q_R=R^6 Q_1. The alternative target norm is the unweighted marked-path norm

`p(x)=32 sum_(A,j)|a_(A,j)|`.

At fixed length this also controls the older common-path seminorms up to their fixed radius/polynomial multipliers. A finite source belongs to both domains, but uniform bounds in one norm do not imply uniform bounds in the other.

## 2. Exact inverse ratios and their asymptotics

For a column whose two mixed diamonds begin at sA and tA, the preceding certificate gives

`c_Gamma(A,j)=7200 (S_(sA)/K_(sA))(S_(tA)/K_(tA))`,

`c_path(A,j)=160/[K_(sA)K_(tA)]`.

Here S is the sum of four actual forcing H4 norms, and K=J-LX is the actual first-edge residual moment. These are inverse ratios to q and p, respectively, from the unscaled scalar l1 data norm.

The already proved completed-theta boundary asymptotics imply, for fixed prime multipliers,

`S_a ~4pi^(3/2)(1+log a)a^(15/2)exp(-pi a^2)`,

`K_a ~pi a^(11/2)(log a-L)exp(-pi a^2)`.

There are only finitely many column types, so these estimates are uniform over the 270 columns. Consequently

`c_Gamma(A,j) ~115200pi (st)^2 A^4`,

`c_path(A,j) ~[160/(pi^2(st)^(11/2))]
                  A^(-11)(log A)^(-2)exp(pi(s^2+t^2)A^2)`.

The exact integer audit finds the unique maxima of both st and s^2+t^2 at

`forgotten(11,13) mixed(5,7) mixed(2,3)`,

with s=143, t=5005. Thus st=715715 and s^2+t^2=25070474. For sufficiently large A this is the worst inverse column in both norms. The independent A=2 certificate already established that it is worst there as well; no claim about every intermediate maximizing background is needed.

## 3. Explicit bounds valid at EVERY admitted background

The asymptotics are supplemented by uniform inequalities, not used as finite numerical bounds.

Let G(a)=||1_[log a,infinity)Phi||_H4, q_0=pi a^2, and

`H_0(a)=1+16exp(-3q_0)/[1-(3/2)^4exp(-5q_0)]`.

The positive completed-theta majorant and

`1+x <=(1+log a)(1+v/q_0)`

in the boundary variable v give, with alpha=2-19/(8pi)>0,

`G(a)<=sqrt(8pi^3/alpha) H_0(2)
       (1+log a)a^(15/2)exp(-pi a^2)`.

Indeed the scaled squared integrand is bounded by its starting-value prefactor times exp(-alpha v). Each of the four diamond windows is a subset of [log a,infinity), so S_a<=4G(a).

For the residual lower bound, the certified L>0 and

`log(2)tanh(3log(2))-L >(1+log(2))/4`

imply x tanh(3x)-L >=(1+x)/4 for every x>=log 2. The ratio on the left to 1+x is increasing. Integrate just the first theta atom over 0<=v<=1, which is inside every prime-multiplier window. This gives

`K_a >= k_0(1+log a)a^(11/2)exp(-pi a^2)`,

`k_0=pi(1-exp(-1))/8`.

Hence S_a/K_a<=D a^2, where

`D=32sqrt(8pi/alpha)H_0(2)/(1-exp(-1))`.

Fresh Arb bounds give D approximately 227.54, strictly below 256. Therefore

`max_j c_Gamma(A,j) <= C_* A^4`,

`C_*=7200*256^2*715715^2=241708913185259520000`.

Also k_0^2(1+log 2)^2*2^11>160, which gives the convenient uniform bound

`max_j c_path(A,j) <=exp(c A^2)`,

`c=pi*25070474`.

These are conservative explicit bounds. They do not replace the sharper finite-background certificates.

## 4. Injective but compact: why the unconditional inverse fails

Identify either source Banach space with l1 by multiplying coefficients by their source norm weights. Observation then becomes a diagonal operator whose entries are 1/c_Gamma(A,j) or 1/c_path(A,j).

Every entry is positive, but the entries tend to zero as A tends to infinity, uniformly over the finite column types. Finite-background truncations therefore converge in operator norm to the full map: it is compact and injective.

Its image contains every finite-support data vector, but its inverse is unbounded. Explicitly, normalize the worst-column source at A to source norm one. Its data norm tends to zero while its source norm remains one. This also rules out continuity of the inverse on its range in the raw l1 topology.

The source itself is never invisible here; its signal becomes arbitrarily small relative to the specified source error. Thus kernel separation and stability are different gates.

For completeness the exact realized-data spaces are

`{z: sum_(A,j)c_Gamma(A,j)|z_(A,j)|<infinity}`

and

`{z: sum_(A,j)c_path(A,j)|z_(A,j)|<infinity}`.

In those weighted data norms the inverse is isometric. That observation does NOT improve physical acquisition: it places correspondingly stronger requirements on late-background noise.

## 5. Conditional recovery with an explicit background prior

Assume total raw scalar noise ||e||_1<=epsilon. Reconstruct exactly on backgrounds A<=H and set the other coefficients to zero. The retained set is finite.

For actual-letter recovery impose the declared prior

`sum_A A^eta q(x_A)<=M`, with eta>0.

Then

`q(reconstruction error)<=C_* H^4 epsilon+M H^(-eta)`.

For H=(M/(C_*epsilon))^(1/(eta+4))>=2 this yields

`q(error)<=2 M^(4/(eta+4))(C_*epsilon)^(eta/(eta+4))`.

For path-coefficient recovery instead impose

`sum_A A^eta p(x_A)<=M`.

Then

`p(reconstruction error)<=exp(c H^2)epsilon+M H^(-eta)`.

For sufficiently small epsilon so that H=sqrt(log(M/epsilon)/(2c))>=2,

`p(error)<=sqrt(M epsilon)
          +M[2c/log(M/epsilon)]^(eta/2)`.

These are different prior classes and different error guarantees. They must not be conflated into one uniform joint-prior assertion. Mere membership in the common-path domain is weaker than a prescribed uniform common-path budget.

The moment A^eta is an explicitly chosen prior on this restricted, completely labelled family. It is not automatically the previously constructed global convex height. To use another height one must supply its comparison with A.

## 6. The rates cannot simply be improved for these prior classes

Compare zero with a single worst-column source at background A having target norm M A^(-eta). Both satisfy the corresponding moment prior. Their scalar-data distance is

`M A^(-eta)/c_target(A)`.

At noise radius half this distance, the midpoint data are consistent with both sources. Every estimator therefore has worst-case source error at least M A^(-eta)/2.

For q, c_Gamma(A) is asymptotic to a positive constant times A^4. This gives the same Holder exponent eta/(eta+4) as the upper bound. For p, log(c_path(A)) is asymptotic to c A^2, giving the same logarithmic order [log(1/epsilon)]^(-eta/2).

These lower bounds already hold along an admitted unbounded sequence of finite sources. Thus they do not depend on constructing a nonsummable source or an inconsistent observer state. Additional stronger priors or a different acquisition protocol could change the conclusion.

## 7. Meaning for the all-depth conjecture

Uniform raw-noise reconstruction fails even before depth grows. Finite separation, corrected-frame coherence and summable realization cannot repair this analytical obstruction by themselves.

A viable general reconstruction theorem must specify:

- the target source norm or topology;
- the independently justified source-tail prior;
- the actual acquisition-error norm;
- the cutoff/regularization rule and its quantitative error modulus.

This note provides such a theorem on one infinite labelled source family, including matching limitations. It neither proves faithfulness on the entire source nor rules out improved sensor designs. Calibration and implementation errors must still be included in the effective scalar error, as in the preceding finite certificate.

## Verification

`uv run --with python-flint --with sympy python research/nima/checkers/check_translated_reconstruction_stability.py`

Artifact: `research/nima/results/translated-reconstruction-stability.json`.

The checker verifies all 270 integer start patterns, the unique leading maxima and the explicit uniform theta/residual constants with Arb. Compactness, the conditional error estimates and deterministic-noise lower bounds are the analytical arguments above; they are not inferred from finite sampled condition numbers.
