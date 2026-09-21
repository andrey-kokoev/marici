# Infinite Euler superpositions have a Hardy residual domain and a nonzero kernel

## Result

**A domain criterion and an unconditional infinite-packet construction.** On a specified class of norm-summable vertical Euler superpositions, ordinary L2 membership of the endpoint-subtracted NEGATIVE-side residual is equivalent to a half-plane Hardy H2 condition on an explicit Cauchy-transform expression.

Moreover, this domain is not trivial: a Blaschke construction gives infinitely many linearly independent nonzero source vectors whose negative-side residual vanishes identically. Thus Voevodsky's finite-Euler-packet obstruction does not extend to all norm-summable infinite superpositions.

The construction changes the SOURCE, not the response operator or its endpoint subtraction. It uses the actual xi zeros unconditionally, without assuming RH or adding zero-indexed counterterms to the operator. It does not classify the positive-side residual or give an ordinary-L2 realization for generic sources.

## 1. A summable packet class before taking transforms

Fix sigma>1 and a complex Borel measure mu on the vertical line s=s_t=sigma+i t, with

    integral (1+|t|) d|mu|(t) < infinity.

Choose 1/2<gamma<sigma-1/2. Define the actual source vector by the Bochner integral

    f_mu(u)=integral exp(-(s_t-1/2)u) dmu(t),  u>=0.

Since

    ||e_(s_t)||_(H_gamma)^2=1/[2(sigma-1/2-gamma)],

and differentiation in u multiplies by -(s_t-1/2), this integral converges in the unrestricted-trace weighted H1 source domain D_gamma. Source truncation and simple-function approximation therefore converge in that norm.

Apply the already constructed endpoint-subtracted weighted-dual response and restrict to the negative side, writing its coordinate as v>0. Its continuity gives a well-defined r_mu in L2(exp(-2 gamma v)dv), and

    r_mu=integral r_(s_t) dmu(t)

in that space. All endpoint subtractions are the fixed source functionals from Voevodsky's theorem.

This is a class of actual superposed source vectors. The coefficient measure need not be uniquely determined by its restriction to the positive half-line; no injectivity of this packet presentation is asserted.

## 2. Transform and the exact Hardy criterion

Write L(q)=xi'(q)/xi(q). The supplied one-state calculation gives

    F_s(q)=integral_0^infinity exp(-(q-1/2)v)r_s(v)dv
          =[L(q)-L(s)]/(q-s),  Re q>1.

At fixed Re s=sigma, the absolute prime-tail majorant bounds its real-space prime contribution by C_sigma(1+v)exp(v/2). The remaining gamma series is bounded near zero by a constant times |log(1-exp(-2v))| and decays at infinity. These bounds are uniform in Im s. They justify integration against the finite-variation mu and interchange with the Laplace integral for Re q>1.

Consequently

    F_mu(q)=integral [L(q)-L(s)]/(q-s) dmu(s).

The diagonal q=s is removable in this formula. For Re q<sigma define

    C_mu(q)=integral dmu(s)/(s-q),
    D_mu(q)=integral L(s)dmu(s)/(s-q).

The Euler-line logarithmic derivative has at most logarithmic growth, so these integrals are analytic in that left half-plane. On the overlap 1<Re q<sigma,

    F_mu(q)=D_mu(q)-L(q) C_mu(q).

The exact criterion is:

    r_mu belongs to ordinary L2(0,infinity)

if and only if F_mu extends holomorphically to Re q>1/2 and

    sup_(epsilon>0) (1/(2pi)) integral_R
        |F_mu(1/2+epsilon+i t)|^2 dt < infinity.

In that case the supremum equals ||r_mu||_2^2.

Necessity is the Laplace Plancherel identity followed by monotone convergence. Sufficiency is the half-plane Hardy/Paley--Wiener theorem: the extension is the Laplace transform of a unique L2 vector. It agrees with the original weighted-dual residual on a common convergence half-plane; uniqueness of the Laplace transform of their exponentially damped difference identifies the vectors.

This criterion uses the GLOBAL Hardy norm, not only a list of removable poles.

## 3. Residue conditions remain necessary

At a nontrivial zero rho of multiplicity m_rho, C_mu and D_mu are analytic because Re rho<1<sigma. The residue is

    Res_(q=rho) F_mu(q)=-m_rho C_mu(rho).

L2 membership therefore forces C_mu(rho)=0 for zeros with Re rho>1/2. It forces the same cancellation at critical-line zeros: otherwise the pole grows as epsilon^(-1), exceeding the epsilon^(-1/2) bound forced by an L2 Laplace transform.

These are necessary conditions. Replacing the Hardy criterion by them alone would require a further global growth theorem.

## 4. Construct a nonzero source whose residual is zero

For a concrete construction take the packet line sigma=2 and, for example, gamma=1. Use the classical facts that xi is entire of order one, all its zeros lie in 0<Re rho<1, and

    sum_rho |rho|^(-2) < infinity,

counting multiplicity. Its Hadamard logarithmic derivative is

    L(q)=b_xi+sum_rho [1/(q-rho)+1/rho].

### 4.1 A bounded Blaschke factor

Reflect each zero in the line Re q=3:

    rho_star=6-conjugate(rho).

Let B be the half-plane Blaschke product in Re q<3, with the same zeros and multiplicities as xi, normalized by B(0)>0. It exists because

    sum_rho (3-Re rho)/(1+|rho|^2) < infinity.

Equivalently use the factors (q-rho)/(q-rho_star) with unit phases, or conjugate-paired factors. The product is locally uniformly convergent, |B|<=1 in that half-plane, and B(0) is nonzero. No numerical zero locations are needed.

For an integer M>=6 put

    C(q)=B(q)/(4-q)^M.

Then C is analytic on Re q<3 and O((1+|q|)^(-M)) on Re q<=2.

### 4.2 Control L C, not merely its poles

The logarithmic derivative of B satisfies

    B'/B=sum_rho [1/(q-rho)-1/(q-rho_star)].

Hence, away from the zeros and then by analytic continuation after multiplication by B,

    B L=B'+B P,

    P(q)=b_xi+sum_rho [1/rho+1/(q-rho_star)].

For Re q<=2 the reflected poles have real part >5. The summands satisfy an upper bound of the form

    |1/rho+1/(q-rho_star)|
      <= C (1+|q|)^2 / |rho|^2.

Indeed their numerator is q+rho-rho_star, its extra real term is bounded by six, and |q-rho_star|>=3. Thus P(q)=O((1+|q|)^2), uniformly on this half-plane. Cauchy's estimate for the bounded analytic B gives a uniform bound on B' there.

It follows that L C extends analytically across every xi zero and

    |L(q) C(q)| <= C_1 (1+|q|)^(2-M),  Re q<=2.

This decay is the essential global estimate enabling the following contour argument. Pole cancellation by itself would not suffice.

### 4.3 Actual summable Euler coefficients

Define

    dmu(t)=C(2+i t) dt/(2pi).

Its total variation and first absolute moment are finite. Therefore it defines a legitimate Bochner source f_mu in D_1 by section 1. Also L(2+i t)C(2+i t) is integrable.

Cauchy's formula, closing to the LEFT of Re q=2 and using the proved decay, gives for Re q<2

    C_mu(q)=C(q),
    D_mu(q)=L(q) C(q).

The second identity uses the analytic continuation of L C across its cancelled zeros. Therefore

    F_mu(q)=0

on 1<Re q<2. Laplace uniqueness gives

    r_mu=0 almost everywhere.

The source itself is NOT zero. Direct integration of its source exponentials gives

    integral_0^infinity exp((q-1/2)u) f_mu(u)du=C_mu(q)=C(q),

for Re q<2. At q=0 this equals B(0)/4^M !=0.

Varying M over integers >=6 gives linearly independent C functions, hence linearly independent source vectors. This constructs an infinite-dimensional subspace of the negative residual's kernel within the declared summable Euler class.

## 5. Why finite packets cannot do this

For a finite Euler packet, C_mu is rational. Vanishing at infinitely many critical-line zeros forces it to vanish identically, as Voevodsky proved.

The obstruction also extends to finite-variation mixtures on any COMPACT Euler spectral set. For such a measure, C_mu(1/w)/w is analytic near w=0, with Taylor coefficients equal, up to sign, to its holomorphic moments integral s^j dmu. Critical-zero cancellation gives zeros at w=1/rho tending to zero. The identity theorem forces all these moments to vanish. Expanding the exponential under the compactly supported integral then gives f_mu=0. This conclusion concerns the source vector; it need not identify an arbitrary complex-plane coefficient measure uniquely.

Our example therefore requires genuinely unbounded spectral support. Here C_mu is a nonzero bounded-half-plane analytic function with an infinite Blaschke zero set. The zero set has no finite accumulation point inside that half-plane and satisfies its Blaschke condition. The rational-function argument does not apply.

The source uses an actual infinite, absolutely Bochner-integrable spectral superposition. It is not an unrestricted formal coefficient family. If expressed using prepared states sqrt(2)xi(s)e_s, the coefficients are divided by the nonzero xi(s) on Re s=2; their required norm-weighted Bochner integral remains the same. No assertion of finite UNWEIGHTED total variation of those rescaled coefficients is made.

This construction may be viewed as a source-selected cancellation of all zero residues. It changes neither the independently defined Tate response nor either endpoint mode. It is not a renormalization by zero-indexed output counterterms.

## 6. Exact boundary of the improvement

The theorem establishes an iff Hardy criterion on the stated vertical-superposition class and an explicit nonzero kernel. It does not show that the residual of every infinite packet is L2: finite packets in the same general setting remain obstructed, and the global Hardy norm remains required.

The subsequent positive-side calculation is now complete: Voevodsky's `infinite-euler-cancellation-gives-a-full-line-kernel-with-zero-endpoints.md` and the independent check `full-residual-reflection-confirms-the-infinite-euler-kernel.md` give F_+(q)=-F_-(1-q). Our kernel therefore vanishes on BOTH sides. In the declared vertical-superposition class a full ordinary-L2 relative response must be zero. Adding q(q-1) to the source Cauchy numerator, with sufficient denominator decay, kills both endpoints and yields an infinite-dimensional kernel of the reduced Tate/endpoint output. None of this asserts positivity, L2 cutoff convergence, or a kernel of the five-label output retaining weak input copies.

Nima's two-slot test/dual comparison and Voevodsky's retained-port graph lift continue to use their declared weighted-dual response topology. The present source construction does not remove their leakage labels, identify leakage with the window-moment residual, or provide arbitrary infinite-spectral tensor/current bounds. Their explicit finite nonzero attachment witness remains unchanged.

Voevodsky's subsequent `endpoint-and-residual-outputs-give-an-equivalence-on-the-prepared-euler-sector.md` proves output-only recovery on the labelled compact exponential-profile sector. It does not contradict this kernel: our construction is an aggregated infinite superposition with unbounded spectral support, and only its endpoint-subtracted negative response vanishes. Its endpoint output ell_+(f_mu)=C(0) is explicitly NONZERO. We do not claim a kernel of the full labelled endpoint/residual output map.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_infinite_euler_residual_domain.py`

Passed exact Hardy/Laplace normalization, residue signs, reflected Blaschke boundary modulus, logarithmic-derivative cancellation, and proper Cauchy-data fixtures. The fixture zeros are NOT claimed zeta zeros. The infinite construction is proved using the classical Hadamard product, the half-plane Blaschke theorem, Cauchy integration, and Laplace uniqueness above.

References:

- `research/voevodsky/endpoint-subtracted-tate-leakage-is-not-L2-on-any-nonzero-finite-euler-packet.md`;
- `research/voevodsky/all-prime-leakage-has-a-weighted-dual-limit-and-a-source-endpoint-subtraction.md`;
- `research/grothendieck/the-all-prime-tate-response-converges-in-a-two-sided-weighted-dual.md`;
- `research/nima/the-two-slot-residual-attachment-has-a-rigged-tate-comparison.md`;
- `research/voevodsky/the-rigged-tate-response-lifts-the-residual-labelled-nonzero-attachment.md`;
- `research/voevodsky/endpoint-and-residual-outputs-give-an-equivalence-on-the-prepared-euler-sector.md`.
