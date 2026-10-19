# H7 — source matching norm and closed-sector radial Green envelope

## The source linear system, rather than an unnamed matrix norm

The entrance solver uses cell-averaged Lippmann–Schwinger equations, not simply a sampled local differential Hamiltonian. In normalized raw entrance coefficients u and retained downstream coefficients z, write

    A(K) [u;z] = [I-G(K)V_int,       g G(K) S T ;
                    -g T* S*,       D_down(K)] [u;z].

Here G is the full raw internal/radial free Green operator; V_int includes geometric and diagonal entrance-contact terms; S is the raw entrance/hinge coupling; T takes the downstream hinge trace in the source's B/sqrt(s_star) convention; and D_down retains the downstream mass/stiffness and both outgoing boundary kernels. This is the block system whose elimination of z gives the source prepared solver's `I-G V_int+g² G S Z S*`, with Z=T D_down^(-1) T*. The full block formulation does not assume D_down invertible at every energy merely because an eliminated formula is used at sampled energies.

Fix the **solver coefficient norm** ||(u,z)||²=||u||_2²+||z||_2², including unit weight on algebraic output trace slots. Use the same Euclidean norm for equation residuals. Entrance coefficients already use normalized radial-cell and internal-grid bases. This is an explicit positive norm, not the semidefinite physical occupation mass matrix. For the retained downstream occupation, M_down>=0 and

    ||error_z||_(M_down) <= sqrt(max diag(M_down)) ||error_z||_2.

The checker verifies the actual diagonal and records its largest value. This controls the retained mass-carrying reconstruction only; it does not claim to bound an entire infinite stationary scattering field in L2. Norm changes or a reduction to an effective retained Schur matrix require their own bounded reconstruction factors.

Because this A is a Green-preconditioned matching system, the earlier Hermitian-off-diagonal Schur criterion is conditional on a verified transformation. For a general block A=[[B,C],[F,D]], if ||B^-1||<=gamma, ||D^-1||<=delta, ||C||<=c and ||F||<=f, rho=gamma*c*delta*f<1 implies

    ||A^-1|| <= delta + gamma/(1-rho)
                          *sqrt(1+(delta*f)²)*sqrt(1+(c*delta)²).

This follows from the block inverse factorization and does not replace F by C* without proof. The bounds still have to be certified uniformly across radial K in [3.09,3.51].

## Source closed-channel quadrature

For rho=1 and closed spectral offset z<=-2rho, the source `rel_green` does not use its open-pole extraction. It directly quadratures the negative multiplier [z-T(k)]^-1. Let m=2^step_power=512, N=2^(tail_power+step_power)=65536, h=0.3, y_l=pi*l/m and k_l=y_l/h. The source DCT-I formula is exactly

    G_ij(z)=(1/m) sum_(l=0)^N t_l sinc(y_l/2)²
                 [cos((i-j)y_l)+cos((i+j+1)y_l)]/[z-T(k_l)],

with t_0=t_N=1/2 and other t_l=1. Here sinc(x)=sin(x)/x; the code writes the equivalent NumPy sinc(y/(2pi)).

Using the cosine addition identity, its positive quadrature Gram matrix is

    C_N=(2/m) sum_l t_l sinc(y_l/2)² c_l c_l*,
    (c_l)_i=cos((i+1/2)y_l).

## Exact Bessel bound, not a fitted numerical norm

Set L=m h. The normalized indicator functions of the first n=32 radial cells lie in L2([0,L]) and are orthonormal. Their coefficients in the orthonormal Neumann cosine basis are 1/sqrt(m) at l=0 and sqrt(2/m) sinc(y_l/2) cos((i+1/2)y_l) for l>=1. Thus C_N is a finite sum of coefficient outer products, with half weight on the last nonzero-frequency coefficient. Bessel's inequality yields

    0 <= C_N <= I_n.

This use of a finite-interval cosine basis proves a norm inequality for the source's explicit quadrature weights. It does **not** replace the physical half-line by a box or claim the quadrature is exact half-line propagation.

For the invariant omitted spectral projector Q420, suppose a **certified** lower bound H_int-E_op>=Delta>0 holds there, with Delta>=2rho so the source closed branch applies. T(k)>=0 gives

    0 <= -G_Q(K) <= Delta^(-1) C_N tensor Q420 <= Delta^(-1) I,
    ||G_Q(K)|| <= 1/Delta.

The source's reported candidate gap is about 8.92937 in the common energy reference; its numerical inertia evidence is not yet an interval-certified premise. The envelope therefore remains conditional on certifying that gap. The 548-direction complement is not invariant and must not be substituted for Q420 in this functional-calculus argument.

## Consequence for the corrected residual

In the source matching equation the full entrance residual is

    r_u = u_raw - G_full q_raw - Fin_raw,
    q_raw = V_int u_raw - g S T z.

This is not the sum of the previously measured native and interaction leakages. Those measurements diagnose why the corrected response span is not invariant. Since the incident forcing lies in the original retained spectral subspace, the invariant-complement residual is

    Q420 r_u = Q420 u_raw - G_Q Q420 q_raw.

Consequently the conditional envelope gives the computable upper bound

    ||Q420 r_u|| <= ||Q420 u_raw|| + ||Q420 q_raw||/Delta.

It may be loose and does not itself control the response error: the full A(K)^(-1) still has to be bounded. No cancellation is assumed or silently discarded in a claimed equality.

## Disposition

H7 remains open. The positive solver norm and an analytic source-quadrature closed-sector envelope are now specified. Exact raw functional-calculus evaluation, certified spectral separation and coupled inverse bounds remain. The accompanying checker verifies the DCT/Gram correspondence numerically and source constants, while the Bessel inequality and block factorization are explicit analytic arguments—not deductions from sampled eigenvalues.
