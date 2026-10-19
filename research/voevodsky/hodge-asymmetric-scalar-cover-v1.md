# Global iteration 23 (third series 3/10): an asymmetric scalar cover control

## Constructed, not matched to the target

Replace the previous even branch function by

    s=x2^4+y2-2

on Eprime: y2^2=x2(x2-1)(x2-25). The smooth double cover z^2=s and the preceding cyclic-four elliptic isogeny give an actual smooth connected etale tower of genera 17,9,5. The fixed-origin elliptic inversion used in the preceding square-fourfold exclusion **does not lift** to this new top curve.

This removes that particular shortcut, not every possible square decomposition. No isogeny to fixed A or Y2, simplicity, endomorphism algebra, theta-singularity dimension or exceptional algebraic cycle is established. The positive node is a scoped auxiliary-cover control, not a completed algebraic-witness search.

## 1. Eight simple branch points, not an assumption of genericity

Write p(t)=t^4-2, f(t)=t(t-1)(t-25). The norm of p(x2)+y2 from the elliptic function field to Q(x2) is

    B0(t)=p(t)^2-f(t)
         =t^8-4t^4-t^3+26t^2-25t+4.

Exact rational polynomial gcd checks give gcd(B0,B0')=1 and gcd(B0,f)=1. Thus B0 has eight distinct roots, none a two-torsion x-coordinate. At each root exactly one point of Eprime is a zero of s, namely y2=-p(x2), and y2 is nonzero. All zeros are simple. At elliptic infinity s has pole order eight, dominated by x2^4; there is no branch there. The normalization C5 has genus five.

Pull back along E1->Eprime and E->Eprime from the previous audit. They are etale isogenies of degree two and four. The pulled functions have respectively sixteen and thirty-two simple zeros, so are not squares. Thus the fibre products C9 and C17 are smooth and connected, with genera nine and seventeen by Hurwitz. Their maps to C5 form an actual etale cyclic-four tower. The top double cover C17->E is a different map from C17->C9; do not confuse their involutions.

## 2. Exact normalized source equations

Retain the preceding rational isogeny

    x2=N/D, y2=y*R/D^2,
    E: y^2=e(x)=x^3+7x^2+x,
    N=x^4+9x^3+16x^2+9x+1,
    D=x*(x-1)^2,
    R=(x^2-1)*(x^4-4x^3-30x^2-4x+1).

With w=D^2*z, the top function field is

    y^2=e(x),
    w^2=A(x)+y*B(x),
    A=N^4-2D^4, B=R*D^2.

The polynomial norm F=A^2-e*B^2 has degree thirty-two and equals exactly D^8*B0(N/D), with denominators cleared. This identity is checked coefficientwise, not by sample points. Degree-preserving modular gcd certificates show gcd(F,F')=1 over Q: F is monic and has gcd one after reduction at each recorded prime. This is an exact characteristic-zero squarefreeness certificate via Gauss's lemma, not an inference from sampled geometric fibres. Always take smooth projective normalization rather than a potentially singular affine model at poles.

## 3. Why the old fixed-origin lift is impossible

On Eprime, elliptic inversion sends y2 to -y2. A point in both branch supports of p+y2 and p-y2 would satisfy p=y2=0. But gcd(p,f)=1. The two eight-point branch supports are disjoint. Pullback by the etale psi preserves that disjointness and simplicity.

For the quadratic extension defining C17 over E, an automorphism a of E lifts if and only if a^*s/s is a square in its function field. For a=[-1], the ratio has an odd pole at every zero of s and an odd zero at every zero of a^*s. The supports are disjoint. The ratio therefore cannot be a square, so fixed-origin inversion on E has **no lift at all**, even allowing z to be multiplied by a rational function. In particular the preceding tau:(Q,z)->(-Q,z) is not an automorphism here.

This is not the bielliptic involution z->-z: that involution still exists and is the commuting scalar lift. Nor is it a theorem about every translated inversion Q->a-Q, every curve automorphism, or abstract endomorphisms/correspondences of the Prym. A square-fourfold isogeny could in principle exist without this curve lift. End^0(P), geometric simplicity and the target isogeny class remain unknown.

## 4. Exact good-reduction point profiles

The checker enumerates rational points at five recorded good primes. It requires smooth elliptic reduction and a squarefree branch norm avoiding elliptic two-torsion. For the source degree-thirty-two norm it also records modular squarefreeness certificates. These are finite-field point enumerations with exact modular arithmetic.

For each elliptic point away from poles the fibre size is 1+chi(s), including the single point at a branch zero. At poles z/x2^2 tends to +1 or -1, so there are **two split points per pole**, not one point or an affine zero. The numbers of pole-fibre points for C5,C9,C17 are respectively 2,4,8, since the isogeny kernels are rational at these primes.

The primitive eightfold trace is

    Tr(Frob_p|H1(P)) = #C9(Fp)-#C17(Fp).

The checker also verifies divisibility of C17 counts by four and C9 counts by two, from the free rational deck actions, and the dimension-eight trace bound. The complete numerical profiles are retained in `results/hodge-asymmetric-scalar-cover-v1.json`.

These are **n=1 traces only**. They do not determine the degree-sixteen Weil polynomial, absolute factors, End, simplicity, target isogeny, or any Hodge class. In particular no transfer of finite-field algebraic cycles to the fixed complex X is asserted. A fuller extension-field computation could give a rigorous factor obstruction for this auxiliary example, but has not been done here.

## 5. Remaining work and scope

This supplies an actual asymmetric scalar test tower for further Frobenius/period investigation. The fixed-origin inversion obstruction is established; other inversion centers and automorphisms need separate tests. Seek full Frobenius polynomials and geometric factor obstructions or actual period data. Direct non-divisor geometry on X, the 512 nonlifting roots and nonbielliptic/other Prym cases remain available.

The prior conditional label census remains 516 / 258 inverse pairs: no entire root class is removed or matched by choosing one branch section. Theta dimension remains unknown. All four f-pullback exceptional channels are still required for a proposed cycle. The three unrestricted research obligations and independent review remain open; no Hodge verdict is supplied.

Contract: `research/conjecture_net/contracts/hodge-asymmetric-scalar-cover.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_asymmetric_scalar_cover.py`.
Receipt: `research/voevodsky/results/hodge-asymmetric-scalar-cover-v1.json`.

    python research/voevodsky/checkers/check_hodge_asymmetric_scalar_cover.py

Trust boundary: written complex-cover and odd-valuation argument, exact polynomial and finite-field controls, standard normalization/isogeny/Hurwitz and trace identities. No formal verification, independent review or new exhaustive literature claim. The iteration-22 predecessor and pins v1-v23 are retained unchanged.
