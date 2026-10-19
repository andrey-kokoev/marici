# Global iteration 25 (third series 5/10): complete auxiliary Frobenius polynomial

## Result and boundary

For the explicit asymmetric auxiliary eightfold P=Prym(C17/C9), the good reduction at seven has the complete degree-sixteen polynomial below. It is irreducible over Q and ordinary, so the reduction is **simple over F7**.

This is NOT geometric/absolute simplicity, a computation of the complex Prym End algebra, an exclusion of all square isogenies after extension, or a match to A or Y2. In particular F7-simple must not be substituted for geometrically simple. The conditional root census, theta dimension and all-cycle/cycle-witness gates remain unchanged.

## 1. Fresh exact extension counts

The preceding control gives smooth curves of genera seventeen and nine with a good etale double-cover Prym of dimension eight at seven. Use the same rational cyclic-four isogeny and asymmetric function z^2=x2^4+y2-2. The source elliptic curve reduces to y^2=x^3+x; the shifted intermediate reduces to v^2=u^3-u^2+u. The isogeny formulas become

    u=x+1/x-2,
    x2=u+6+1/u,
    y2=y*(1-1/x^2)*(1-1/u^2)

for the top source, omitting the first y factor at the intermediate source.

The std-only Rust counter enumerates each F_(7^n), n=1,...,8. Polynomial-basis addition and a full primitive-generator cycle provide logarithm multiplication and quadratic characters. The cycle is checked to visit every nonzero element exactly once and return to one. Thus it also certifies that the supplied quotient polynomial is irreducible and its root primitive; no preexisting finite-field package is trusted for those field choices.

Every elliptic x-coordinate is visited. For nonzero square y^2 the two y signs contribute separately; y=0 contributes once. Each fibre has size 1+chi(s). Pole fibres are handled on the smooth normalized covers: C9 has four split rational pole points, and C17 has eight, in every extension. They are not counted as affine zeros or as one point at infinity.

| n | #C9(F_(7^n)) | #C17(F_(7^n)) | Tr(Frob_7^n on H1(P)) |
|---:|---:|---:|---:|
|1|8|16|-8|
|2|96|112|-16|
|3|404|376|28|
|4|2316|2592|-276|
|5|16948|17216|-268|
|6|119088|118384|704|
|7|826316|829208|-2892|
|8|5753884|5747832|6052|

Trace is #C9-#C17, by the Frobenius-stable Jacobian/Prym isogeny decomposition. The exact field moduli, counts and cycle flags are retained in `inputs/hodge-asymmetric-frobenius-v1/counts.json`. Every checker process freshly compiles the counter with rustc -O and reruns all eight fields; a per-process cache avoids rerunning the same full enumeration for each hostile test. The run is compared exactly with the retained count input.

An independent Python implementation reproduces n=1 from the preceding prime-field checker and n=2 using direct quadratic polynomial-basis multiplication, inversion and exhaustive (x,y) pairs, not logarithm tables. It gives (96,112) over F49. Curve trace bounds and rational deck-orbit divisibilities are also checked, but those necessary bounds alone are not a correctness proof of point counts.

## 2. Polynomial reconstruction

Let s_n be the trace column and write L(T)=det(1-Frob_7*T)=sum c_k*T^k. Newton identities give

    k*c_k = -sum_(i=1)^k s_i*c_(k-i), c_0=1.

All divisions through k=8 are integral. Polarized dimension-eight Frobenius duality gives c_(16-k)=7^(8-k)*c_k, completing the polynomial. In ascending T order its coefficients are

    [1,8,40,140,453,1444,4560,13360,36360,
     93520,223440,495292,1087653,2352980,
     4705960,6588344,5764801].

Equivalently the monic characteristic polynomial is

    F(X)=X^16+8X^15+40X^14+140X^13+453X^12
         +1444X^11+4560X^10+13360X^9+36360X^8
         +93520X^7+223440X^6+495292X^5+1087653X^4
         +2352980X^3+4705960X^2+6588344X+5764801.

The constant term is 7^8, not an additional inferred input. Eight traces suffice only because the known dimension and polarization functional equation are supplied; no arbitrary sequence is turned into a curve theorem by enforcing symmetry.

## 3. Exact irreducibility certificate without an opaque factor call

Exploratory factorization was used to find two modular certificates, but the live checker verifies them with std-only exact polynomial arithmetic. Its retained monic factors multiply to F modulo each auxiliary prime. Each factor is certified irreducible by the Rabin criterion: x^(ell^d)=x modulo the factor and gcd(x^(ell^(d/r))-x,factor)=1 for each prime r dividing its degree.

At ell=5 the irreducible factor degrees are 1,1,7,7. Hence a proper rational factor could have degree only among

    1,2,7,8,9,14,15.

At ell=11 the factor degrees are 6,10, allowing proper rational factor degrees only 6 or 10. The two lists are disjoint. Since F is monic integral, a monic rational factor is integral and its degree survives each reduction. Therefore F is irreducible over Q. No irreducible degree-sixteen reduction at one prime is assumed to exist.

The full modular factor coefficients are retained in the receipt/checker, and their products and irreducibility are rechecked on every validation. Python-flint was only a discovery aid; it is not a runtime checker dependency.

## 4. Precisely which simplicity statement follows

A proper nonzero abelian subvariety defined over F7 would give a nontrivial integral factorization of the Frobenius polynomial (using the finite-field polarization/isogeny decomposition). Irreducibility therefore proves simplicity **over F7**. The middle coefficient 36360 is 2 modulo seven, so the standard middle-coefficient criterion gives ordinary reduction.

Neither assertion settles the geometric factorization over the algebraic closure: roots can become conjugate after powering Frobenius if their ratios are roots of unity. A variety simple over its finite base field can split after extension. Further eigenvalue-ratio/Frobenius-power or geometric-factor work is required before excluding a square over Qbar or the complex target's X6 factor. No such conclusion is made in this receipt.

Similarly ordinary finite reduction and point counts do not produce an exceptional algebraic cycle on the fixed complex X. No specialization/lifting transfer of finite-field cycles is licensed.

## 5. Frontier and trust

Next analyze root-of-unity ratios or Frobenius powers of this complete polynomial, or pursue actual periods/target/theta matching, the nonlifting family or direct non-divisor geometry on X. All four f-pullback exceptional channels remain required. The three unrestricted research obligations and independent review remain open; there is no Hodge verdict.

Contract: `research/conjecture_net/contracts/hodge-asymmetric-frobenius.v1.json`.
Python checker: `research/voevodsky/checkers/check_hodge_asymmetric_frobenius.py`.
Rust counter: `research/voevodsky/checkers/count_hodge_asymmetric_frobenius.rs`.
Receipt: `research/voevodsky/results/hodge-asymmetric-frobenius-v1.json`.

    python research/voevodsky/checkers/check_hodge_asymmetric_frobenius.py

Trust boundary: exact executed arithmetic with Python/Rust compiler/runtime in the computational trusted base; standard good-reduction Prym/trace and polarization facts, finite-field ordinarity and rational-factor argument. Not proof-assistant verification or independent mathematical review. The iteration-24 predecessor and pins v1-v25 are preserved unchanged.
