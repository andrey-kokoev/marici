# Endpoint-subtracted Tate leakage is not L2 on any nonzero finite Euler packet

## Result and scope

The negative-side residual of the source-defined endpoint-subtracted all-prime Tate operator is NOT in ordinary L2 for any Euler exponential e_s with Re s>1. More strongly, its ordinary L2 domain intersects the finite span of distinct Euler exponentials only in zero.

This is unconditional. It uses the classical theorem that there are infinitely many distinct critical-line zeta zeros, not RH, positivity, or a numerical certification of zeros. The weighted-dual operator limit remains valid.

Inputs:
- `all-prime-leakage-has-a-weighted-dual-limit-and-a-source-endpoint-subtraction.md`
- `the-trivial-sector-arithmetic-form-is-a-tate-compression-with-explicit-leakage.md`
- `../grothendieck/all-prime-tate-leakage-diverges-on-the-common-euler-source-domain.md`

## 1. Fix the source and the already specified subtraction

Let

    e_s(x)=exp(-(s-1/2)x),  Re s>1.

Choose 1/2<gamma<Re s-1/2 so e_s lies in the existing unrestricted-trace source D_gamma. Its endpoint functionals are

    ell_+(e_s)=1/s,  ell_-(e_s)=1/(s-1).

Write u=-v, v>0, for the negative physical coordinate. The actual all-prime leakage is

    H_s(v)=exp((s-1/2)v) sum_(n>exp(v)) Lambda(n)n^(-s).

The strict boundary convention affects only a countable set of v. The series is absolutely convergent. The prime source endpoint subtraction is H_s(v)-exp(v/2)/(s-1).

The archimedean leakage, using the independently fixed Tate sign, is

    sum_(j>=0) exp(-(1/2+2j)v)/(s+2j).

Its j=0 term is precisely the other endpoint mode exp(-v/2)/s. Hence the FULL relative negative-side response from the preceding weighted-dual theorem is

    r_s(v)=H_s(v)-exp(v/2)/(s-1)
           +sum_(j>=1) exp(-(1/2+2j)v)/(s+2j).

The gamma remainder is in ordinary L2: at v=0 it has at worst logarithmic growth, and at infinity it decays exponentially. The source-derived prime fluctuation is the only possible negative-side L2 obstruction.

This r_s is defined by the all-prime weighted-dual limit with the prescribed endpoint response removed. We do not assume that finite-cutoff subtracted responses belong to ordinary L2; the growing endpoint subtraction already prevents that in general.

## 2. Compute the Laplace transform on its actual convergence half-plane

Use q as the shifted Laplace variable:

    F_s(q)=integral_0^infinity exp(-(q-1/2)v) r_s(v) dv,
    Re q>1.

Put P(q)=-zeta'(q)/zeta(q). Absolute convergence permits summing the actual prime powers first:

    integral exp(-(q-1/2)v) H_s(v)dv
      =sum Lambda(n)n^(-s) integral_0^(log n) exp((s-q)v)dv
      =[P(q)-P(s)]/(s-q).

At q=s this divided difference has its removable value. The endpoint term contributes -1/[(s-1)(q-1)]. The gamma remainder contributes

    sum_(j>=1) 1/[(s+2j)(q+2j)]
      =[psi(1+q/2)-psi(1+s/2)]/[2(q-s)].

Consequently

    F_s(q)=[P(q)-P(s)]/(s-q)-1/[(s-1)(q-1)]
           +[psi(1+q/2)-psi(1+s/2)]/[2(q-s)].

Here psi denotes the digamma function, not the prime counting function. All three terms have been derived from the source response; none is fitted from a Clark Gram identity.

## 3. The completed logarithmic derivative and its poles

Let

    xi(q)=1/2 q(q-1) pi^(-q/2) Gamma(q/2) zeta(q),
    L(q)=xi'(q)/xi(q).

Using psi(1+q/2)=psi(q/2)+2/q gives the exact simplification

    F_s(q)=[L(q)-L(s)]/(q-s).

The diagonal q=s is removable, with value L'(s). The source endpoint subtraction removes the q=1 pole; the combined completed expression also makes the trivial-factor cancellations explicit.

At any nontrivial zero rho of multiplicity m_rho, its remaining residue is

    Res_(q=rho) F_s(q)=m_rho/(rho-s)=-m_rho/(s-rho).

It is nonzero because Re s>1 whereas 0<Re rho<1. Thus the prescribed endpoint subtraction removes the continuum/pole modes, NOT the nontrivial-zero modes.

This is meromorphic continuation of a calculated Laplace transform. It is not a claim that the original source attachment or its Clark observations have acquired unrestricted critical-line domains.

## 4. A boundary pole is incompatible with an L2 Laplace transform

Suppose r_s belonged to L2(0,infinity). Its Laplace transform would be holomorphic for Re q>1/2 and obey, by Cauchy--Schwarz,

    |F_s(1/2+epsilon+i t)| <= ||r_s||_2/sqrt(2 epsilon),
    epsilon>0.

It agrees with the expression in section 3 on Re q>1 and hence with its meromorphic continuation wherever applicable. Any nonremovable pole inside Re q>1/2 already contradicts holomorphy.

Now choose a critical-line zero rho=1/2+i t. Such zeros exist unconditionally. If interior poles have not already contradicted the assumption, continuation to the positive side of this boundary point gives

    F_s(rho+epsilon)=-m_rho/[(s-rho)epsilon]+O(1).

This grows as epsilon^(-1), contradicting the L2 bound epsilon^(-1/2). Therefore r_s is not in ordinary L2.

No limiting interchange on the critical line was used: the contradiction uses holomorphy and the norm estimate that L2 membership itself would force.

## 5. No nonzero finite Euler packet repairs the obstruction

Let f=sum_(j=1)^N c_j e_(s_j), with distinct s_j and Re s_j>1. Choose one admissible gamma for this finite collection. Linearity gives the residual transform

    F_f(q)=sum_j c_j [L(q)-L(s_j)]/(q-s_j).

At a nontrivial zero rho its residue is

    -m_rho sum_j c_j/(s_j-rho).

Ordinary L2 membership would require this coefficient to vanish at every critical-line zero. There are infinitely many distinct such zeros by the classical critical-line theorem. The rational function

    C(rho)=sum_j c_j/(s_j-rho)

cannot have infinitely many distinct zeros unless it vanishes identically. Uniqueness of partial fractions then gives c_j=0 for every j.

Thus the ordinary negative-side L2 residual domain has trivial intersection with the nonzero finite Euler span. Repeated spectral parameters are combined before applying this statement.

The prepared full-theta states are nonzero scalar multiples sqrt(2)xi(s)e_s in this Euler region. Since xi(s) does not vanish for Re s>1, the same obstruction applies to every nonzero finite packet of those states. This does not concern independently added root factors or window-residual channels.

## 6. Consequences and remaining boundary

Closed:
- an exact source-derived Laplace transform after both endpoint modes are subtracted;
- identification of every surviving zero residue;
- failure of ordinary L2 even after subtraction on each prepared Euler state;
- failure on every nonzero finite Euler packet.

The all-prime weighted-dual operator comparison therefore cannot be strengthened to an ordinary full-line L2 comparison on the declared prepared Euler family using only its prescribed endpoint subtraction. The negative-side obstruction already suffices; no analysis of the positive-side residual can remove it.

Still available: the proven weighted-dual domain, or a genuinely different distributional/spectral realization with its own domain theorem. No zero-indexed counterterms are introduced here. Arbitrary non-Euler sources and infinite superpositions have not been classified by this finite-packet theorem.

The window residual in Nima's labelled attachment comparison remains a different object. Retaining it repairs window moment information, not these Tate zero poles.

## Verification

`uv run --with sympy --with mpmath python research/voevodsky/checkers/check_euler_residual_laplace_obstruction.py`

Passes exact symbolic completion, endpoint-pole cancellation, zero-residue and finite-packet partial-fraction identities. Numerical critical-zero fixtures check the sign and scaling only. The infinite obstruction follows from the analytic argument and the classical critical-line zero theorem, not those fixtures.
