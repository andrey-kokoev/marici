# The Euler gamma–endpoint operator reconstructs the two Clark sheets

## Result and strength

**One-slot Euler-chart operator comparison on a declared common domain.** A renormalized translation integral defines the gamma operator on a weighted Sobolev core and is closable. Two bounded translation resolvents realize the elementary endpoints, with exactly their prescribed swap form. Adding Voevodsky's independently defined prime operator produces a closed arithmetic operator on its graph domain.

On the fixed completed-theta even-port states, a fixed graph-to-two-sheet map reconstructs the actual normalized Clark features. Thus the comparison is vector-valued, not only an equality of scalar kernels.

This does not identify the graph domain with that of the independently prescribed semilocal Tate operator, prove positivity, or continue the prime Dirichlet operator series to the critical line.

## 1. Common core and pairing

Retain the Clark feature variable u>=0, distinct from the forcing variable x. Fix gamma>1/2 and use

H_gamma=L2(R_+,exp(2 gamma u)du),

D_gamma^1={f in H_gamma : weak f' in H_gamma}.

The Sobolev norm is sqrt(||f||_gamma^2+||f'||_gamma^2). Smooth functions compactly supported in [0,infinity), allowed to be nonzero at zero, are dense in D_gamma^1 and H_gamma. No zero-trace condition is imposed on source states.

Use T_a f(u)=f(u+a). As in the prime construction,

||T_a||<=exp(-gamma a),

||T_a f-f||_gamma<=a||f'||_gamma.

Every physical form below uses the ORIGINAL unweighted half-line pairing < , >_0. Weighted norms control the domain only.

## 2. Gamma operator from its archimedean integral

Write gamma_E for Euler's constant and put

c_Gamma=-(gamma_E+log pi)/2.

Define, initially on D_gamma^1,

G f=c_Gamma f+integral_(0,infinity)
       [exp(-2a)f-exp(-a/2)T_a f]/[1-exp(-2a)] da.

The integral and its counterterm are the standard archimedean digamma representation, fixed before evaluating a Clark state:

(psi(s/2)-log pi)/2
 =c_Gamma+integral_(0,infinity)
       [exp(-2a)-exp(-s a)]/[1-exp(-2a)] da,  Re s>0.

The counterterm is essential at a=0. It is not an adjustable boundary or metric parameter.

Here is a direct Bochner-integrability estimate. Put d0=1-exp(-2), sigma0=gamma+1/2. For 0<a<=1,

||exp(-2a)f-exp(-a/2)T_a f||_gamma
 <= a[(3/2)||f||_gamma+||f'||_gamma],

1-exp(-2a)>=d0 a.

For a>=1 the numerator norm is at most

[exp(-2a)+exp(-sigma0 a)]||f||_gamma.

Thus G:D_gamma^1->H_gamma is bounded. For 0<epsilon<=1<=L, keep the constant c_Gamma and truncate the integral to [epsilon,L]. Then

||(G-G_(epsilon,L))f||_gamma
 <= epsilon[(3/2)||f||_gamma+||f'||_gamma]/d0
    +[exp(-2L)/2+exp(-sigma0 L)/sigma0]||f||_gamma/d0.

This is operator convergence from the Sobolev core norm to H_gamma. It is not an assertion of operator-norm convergence on H_gamma itself.

## 3. Closability without selecting a self-adjoint boundary condition

The weighted adjoint is

T_a^* h(u)=exp(-2 gamma a) 1_(u>=a) h(u-a).

For h smooth and compactly supported inside (0,infinity), the formal adjoint integral

G^dagger h=c_Gamma h+integral
 [exp(-2a)h-exp(-a/2)T_a^*h]/[1-exp(-2a)] da

converges in H_gamma. Near zero use the right-shift generator -h'-2 gamma h; its norm controls T_a^*h-h by a times that norm. The preceding tail estimate is unchanged.

Bochner integration gives

<h,Gf>_gamma=<G^dagger h,f>_gamma.

Such h form a dense subspace of H_gamma. Hence the adjoint of G is densely defined and G is closable. Denote its closure by Gbar. Approximation in D_gamma^1 also shows that the smooth up-to-zero source core is a core for this closure.

The zero-trace test functions used to prove adjoint density do not impose a zero boundary value on the original domain. In particular the exponential source states below are admitted.

## 4. Endpoint resolvents and the exact swap attachment

Define two bounded operators on H_gamma,

R_+=integral_(0,infinity) exp(-a/2)T_a da,

R_-=integral_(0,infinity) exp(a/2)T_a da.

Their norms are at most 1/(gamma+1/2) and 1/(gamma-1/2), respectively. Let B_end=R_++R_-.

The endpoint functionals are independently defined Laplace traces

ell_+(f)=integral exp(-u/2)f(u)du,

ell_-(f)=integral exp(u/2)f(u)du.

They are bounded on H_gamma, with norms 1/sqrt(2 gamma+1) and 1/sqrt(2 gamma-1). They are also R_+f(0) and R_-f(0), interpreted through these integrals.

Fubini gives, for all f,g in H_gamma,

<f,B_end g>_0+<B_end f,g>_0
 =conjugate(ell_+(f))ell_-(g)+conjugate(ell_-(f))ell_+(g).

Indeed R_c and its unweighted transpose have combined kernel exp(-c|u-v|). Summing c=1/2 and c=-1/2 gives

exp((u-v)/2)+exp(-(u-v)/2),

the separated kernel of the displayed swap form. Weighted integrability with gamma>1/2 justifies the integrations.

Thus the prescribed endpoint swap matrix is retained. In parity coordinates it still has one positive and one negative square. No positive replacement is made.

## 5. Add the independently specified prime operator

Use Voevodsky's norm-convergent operator

V=sum_(n>=2) Lambda(n)n^(-1/2)T_(log n)

on H_gamma. Define

L_arith=Gbar+B_end-V,

Dom(L_arith)=Dom(Gbar).

Since B_end and V are bounded, L_arith is closed. Let D_arith be this domain with graph norm

||f||_arith^2=||f||_gamma^2+||L_arith f||_gamma^2.

It is a Hilbert space, and the common Sobolev core is dense in this graph norm. The gamma, endpoint, and prime forms are individually continuous there:

q_Gamma(f,g)=<f,Gbar g>_0+<Gbar f,g>_0,

q_end(f,g)=conjugate(ell_+f)ell_-g+conjugate(ell_-f)ell_+g,

q_prime(f,g)=-<f,Vg>_0-<Vf,g>_0.

Their sum is

q_arith(f,g)=<f,L_arith g>_0+<L_arith f,g>_0.

It is a bounded Hermitian form on D_arith, of norm at most one for the displayed graph norm. In particular it has a bounded self-adjoint Riesz representative on that CONTROL Hilbert space. This does not assert that L_arith itself is self-adjoint or select an unbounded self-adjoint Green realization on H_gamma.

## 6. Exact action on Euler exponential states

Set s=1/2-i z and e_s(u)=exp(-(s-1/2)u). If Re s>gamma+1/2, then e_s belongs to D_gamma^1 and hence D_arith. The source translation rules give

R_+ e_s=(1/s)e_s,

R_- e_s=(1/(s-1))e_s,

Gbar e_s=[psi(s/2)-log pi]e_s/2,

V e_s=P(s)e_s,  P(s)=sum Lambda(n)n^(-s).

Therefore

L_arith e_s=L(s)e_s,

L(s)=1/s+1/(s-1)-(log pi)/2+psi(s/2)/2-P(s)
    =xi'(s)/xi(s)

on this Euler chart. Each component was defined before this evaluation.

For t=conjugate(s_w), the ORIGINAL pairing is

<e_(s_w),e_(s_z)>_0=1/(s_z+t-1).

Thus q_Gamma gives exactly K_Gamma, q_prime gives K_prime, and the endpoint swap gives K_end in the frozen crosswalk. Using the weighted pairing here would incorrectly replace the denominator by s_z+t-1-2 gamma.

## 7. A vector-valued two-sheet comparison

Define the fixed graph map

C_arith f=((f+L_arith f)/sqrt(2), (f-L_arith f)/sqrt(2))

from D_arith to H_0 direct_sum H_0. It is bounded. With J=diag(1,-1),

<C_arith f,J C_arith g>_0=q_arith(f,g).

This identity follows by expansion; it introduces no fitted signed form.

For the prescribed completed theta source, the already fixed even-sheet projection is

U_Phi(z)=sqrt(2)X(z)e_(s_z),  X(z)=xi(s_z).

Since X'(z)=-i L(s_z)X(z), its normalized amplitudes satisfy

E=X+iX'=X(1+L),

E_star=X-iX'=X(1-L).

Consequently

C_arith U_Phi(z)=(E(z)e_(s_z), E_star(z)e_(s_z)).

This is the actual normalized Clark feature pair. The independently constructed arithmetic operator therefore reconstructs both sheets from the source-defined even port, not merely their scalar polarization. Finite spectral packets follow by linearity, with every spectral pair retained.

On a compact spectral set gamma<eta<=Im z<=Y<beta and |z|<=Z, Voevodsky's even-port forcing bound into H_gamma gains only sqrt(1+Z^2) to become a bound into D_gamma^1. The preceding operator estimate then controls C_arith on those source states. This permits source approximation in that topology.

The exact reconstruction with L=xi'/xi is asserted for the prescribed completed theta forcing. An arbitrary shell forcing has its own even transform; its derivative is not generally L times that transform. Theta-truncated source states can approximate the completed identity, but are not declared to satisfy the exact xi identity at every finite cutoff.

## 8. Boundaries and relation to subsequent inputs

Constructed here: a source-defined gamma operator with explicit cutoff bounds and closability, bounded endpoint resolvents, a common closed graph domain with the prime operator, the exact signed endpoint/gamma/prime form, and the two-sheet completed-theta comparison on the Euler chart.

Still separate:

- identification with the independently specified semilocal Tate/endpoint operator and its domain;
- a positive-semidefinite packet inequality or stable inverse;
- critical-line continuation of these operator realizations;
- an identification of source bulk/forcing channels with gamma/prime channels;
- a completed tensor-Hom equivalence or a multi-seam arithmetic operator theorem.

Voevodsky's new relative theta-tail control resolves the earlier actual-letter substitution gate; it does not change the Euler-chart restriction here. Nima's factorial observer-dual square retains its own declared strong dual and representable-mate graph domain. The graph map above is not a surjectivity assertion for that observer dual or a replacement for its prescribed beta. Nima's subsequent two-seam incidence obstruction proves that the representable-mate domain is proper; Voevodsky's actual-letter normalization obstruction preserves analytical dual nonsurjectivity even after forcing normalization. The one-slot arithmetic graph construction makes neither of those obstructions disappear.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_euler_gamma_endpoint_operator.py`

Passed 12 exact gamma integral fixtures, the small-shift limit, weighted-adjoint and endpoint-resolvent identities, rejection of the weighted denominator, and the exact two-sheet polarization and theta reconstruction identities. Closability and common-domain assertions follow from the estimates and adjoint argument above, not from finite spectral samples.

References:

- `research/voevodsky/the-euler-prime-channel-has-a-source-defined-shift-operator-comparison.md`;
- `research/grothendieck/clark-sewing-to-the-endpoint-gamma-prime-green-kernel.md`;
- `research/voevodsky/clark-source-interface-domain-and-positivity-audit.md`;
- `research/voevodsky/relative-theta-tail-control-preserves-the-actual-letter-fox-domain.md`;
- `research/nima/the-factorial-attachment-has-a-continuous-observer-dual-square.md`.
