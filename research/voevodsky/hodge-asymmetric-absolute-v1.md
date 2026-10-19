# Global iteration 26 (third series 6/10): one scalar Prym is absolutely simple

## Result

For the particular cyclic-four scalar cover with z^2=x2^4+y2-2 and the fixed rational elliptic isogeny used in iterations23-25, its eight-dimensional Prym P is **geometrically simple over C**. Consequently it is not isogenous to A=X6 times B2, to the principal model Y2, or to a square of fourfolds, even unpolarized and after extension of the field of definition.

This rejects one auxiliary target transplant, not the fixed Hodge candidate, not every asymmetric section, and not all four remaining scalar root labels. End^0(P), actual theta dimension and the 512 nonlifting labels remain open. The 516-label conditional census does not change: it was necessary-condition data, not a list of these specific branch sections or successful targets.

## 1. Fresh predecessor and the root-ratio obstruction

The iteration25 checker recompiles its std-only Rust counter and reenumerates all fields through F_(7^8). Its exact Newton/modular-factor certificates give the irreducible degree-sixteen polynomial

    f(X)=X^16+8X^15+40X^14+140X^13+453X^12
         +1444X^11+4560X^10+13360X^9+36360X^8
         +93520X^7+223440X^6+495292X^5+1087653X^4
         +2352980X^3+4705960X^2+6588344X+5764801.

Let alpha_1,...,alpha_16 be its distinct roots. Define the rational, monic ratio polynomial

    R(T)=product_(i,j)(T-alpha_i/alpha_j), degree256.

The sixteen diagonal ratios are one and must NOT be excluded. Any nontrivial root-of-unity ratio has a primitive order m>1 and forces Phi_m to divide R over Q.

In fact R belongs to Z[1/7][T]: take the integral companion matrix C of f. Its determinant is 7^8, so C inverse has entries in Z[1/7]; R is the characteristic polynomial of C tensor C inverse. Thus reduction modulo every auxiliary prime other than seven preserves divisibility by a monic cyclotomic polynomial.

## 2. Complete order bound, not a numerical cutoff

Necessarily phi(m)<=256. For a prime power p^a, the factor in phi(m)^2/m is p^(a-2)*(p-1)^2. Each such factor is at least one, except p=2,a=1, when it is one half. Therefore phi(m)^2>=m/2, and m<=131072.

An exact totient sieve through that proven bound gives 504 possible m>1, with largest value1050. Every one is checked. Cyclotomic polynomials are generated over the integers by exact monic division of T^m-1 by the preceding divisor cyclotomics, not approximate roots or a guessed list of small orders.

## 3. Two exact modular witnesses

Let s_k=sum alpha_i^k. The polarized Frobenius reciprocity alpha ->7/alpha gives

    sum_(i,j)(alpha_i/alpha_j)^k = s_k^2 / 7^k.

The degree-sixteen recurrence computes s_k through k=256 modulo ell. Newton identities then compute R modulo ell; ell>256 makes every division invertible.

This reconstruction is independently checked as a whole polynomial, not by a few random evaluations. For n=16,

    Res_X(f(X),f(tX)) = f(0)^n * R(t).

A direct 32-by-32 Sylvester determinant computes the left side for each t=0,...,256. Both sides have degree at most256, so these257 distinct evaluations certify their polynomial identity modulo each ell. No resultant/factor library is needed.

- Modulo409, gcd(R,Phi_m)=1 excludes501 orders. Only41,136,408 survive this modular test.
- Modulo419, all three remaining orders have gcd one.

Survival at one auxiliary prime is only an inconclusive modular coincidence, not an actual root-of-unity ratio. Each order has at least one exact coprimality witness. Were Phi_m a rational factor of R, it would remain a factor at every admissible prime, contradicting its witness. Thus no quotient of two distinct roots is a root of unity.

The receipt retains both complete modular ratio polynomials, each excluded-order list, the residual orders and the257-point determinant verification count. Every process recomputes the arithmetic; per-process caching avoids repeating the same pure certificate in every hostile regression.

## 4. Absolute simplicity of the good reduction

For every positive r, alpha_i ->alpha_i^r is injective, since a collision would make a nontrivial quotient a root of unity. Galois acts transitively on the original roots by irreducibility of f. It therefore still acts transitively on the sixteen distinct r-th powers. The characteristic polynomial of Frobenius_(7^r) is consequently irreducible over Q for every r.

A proper abelian subvariety defined over F_(7^r) would give a nontrivial integral factorization of that characteristic polynomial, using the polarization/isogeny decomposition. None exists. Every abelian subvariety over the algebraic closure of a finite field is defined over some finite extension. Hence the reduction P_barF7 is absolutely simple. Ordinarity from iteration25 is compatible with this argument but is not needed as an extra simplicity hypothesis.

## 5. Correct specialization direction and the complex consequence

The preceding explicit branch and elliptic discriminant checks ensure good reduction at seven of both curves and the etale double-cover Prym. The degree-two maps are prime to seven. The identity component of the norm kernel extends to the dimension-eight abelian Prym over the good-reduction base. This good-reduction input is essential; we are not specializing an arbitrary complex analytic torus.

Suppose P over Qbar were not simple. A nontrivial rational idempotent e in End^0(P) would split a proper abelian factor, by Poincare complete reducibility. Define e over a finite number field extension and choose a place above seven. Endomorphisms extend over the good abelian model, and specialization on rational endomorphisms is injective. One way to see injectivity is to use a Tate module at a prime different from seven: smooth proper base change identifies generic and special Tate modules, and their action is faithful for abelian-variety endomorphisms. Thus e specializes to a nonzero, nonidentity idempotent of End^0(P_barF7), contradicting absolute simplicity there.

Therefore P_Qbar is simple. Geometric abelian factors and homomorphisms do not arise newly on extending an algebraically closed characteristic-zero field to C, so P_C is simple as well. This uses the direction **absolutely simple good reduction implies absolutely simple generic fibre**. The converse is not asserted; a simple complex variety can have nonsimple reduction.

The target A=X6 times B2 has a proper dimension-six abelian subvariety. Y2 is isogenous to A by the existing degree2304 construction. Simplicity is isogeny invariant. This particular P cannot be isogenous to either target and cannot be a fourfold square. The conclusion concerns abstract isogenies, not only curve-induced correspondences, dihedral automorphisms, Gaussian-linear maps or chosen polarizations.

No algebraic cycle is lifted from the finite field to the fixed complex X. No Hodge verdict or arbitrary-cycle annihilation follows.

## 6. Next executable frontier and trust

Stop target-matching this particular simple eightfold. Other scalar level isogenies and branch sections may lie on special decomposition loci; they are not excluded by a single simple example. Seek actual 6+2 correspondences/decomposition criteria there, examine the 512 nonlifting labels, compute target theta data, or pursue direct non-divisor cycles on the original X. Keep all four exceptional transfer channels.

Contract: `research/conjecture_net/contracts/hodge-asymmetric-absolute.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_asymmetric_absolute.py`.
Receipt: `research/voevodsky/results/hodge-asymmetric-absolute-v1.json`.

    python research/voevodsky/checkers/check_hodge_asymmetric_absolute.py

Trust: exact Python modular/integer arithmetic, fresh predecessor Rust enumeration, plus the written algebraic arguments and standard good-reduction, Frobenius, polarization and faithful-specialization facts. Not proof-assistant verification or independent review. Iteration25 and immutable pins v1-v26 remain unchanged.
