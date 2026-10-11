# Global fixed-flux ground state and binary spin transport

## Result

For the existing hard-source-flux fixture beta=3/5, eta=1/5, the global minimum in the four negative-face pure-amplitude sector is

    E_min = 0.1798077094008586...

The earlier one-axis variational states are the actual minimizing states. There are four minimizing rays, one for each face address. Their exact source rotations and phases are retained.

All 24 binary tetrahedral rotations act on this orbit, and all 576 group compositions close. The central full rotation acts as -I on the lifted states. However, their linear span is four-dimensional: the nonlinear ground set is not an entire two-dimensional eigenspace.

## 1. Functional and source conference form

This continues `spinor-fixed-flux-relaxation.md`, retaining its exact electric elimination and common exterior data:

    F(psi)=<psi,K psi>+c*(1+sum_i |psi_i|^4)+eta/2,
    ||psi||=1, c=beta/10=3/50.

The source kinetic operator is K=I-Q, with Q^2=I, zero diagonal and off-diagonal magnitude 1/sqrt(3). Its sourced triangle products determine a diagonal gauge in which

    Q=i*A/sqrt(3),
    A=[[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]].

The checker verifies A^2=-3I and matches every source triangle phase to this conference form. Matching the independent graph cycle phases with identical edge magnitudes ensures gauge equivalence; this does not flatten the source connection.

## 2. Exhaust the stationary density patterns

The normalized pure-state domain is compact, so a global minimum is stationary. Write rho_i=|psi_i|^2. Stationarity gives

    [diag(d_i)-Q]psi=0,
    d_i=1+2c*rho_i-lambda.

The exact determinant is

    D(d)=d0*d1*d2*d3-(1/3)*sum_(i<j) d_i*d_j+1.

For its principal cofactors C_i=partial D/partial d_i,

    C_i-C_j=(d_j-d_i)*(d_k*d_l-1/3).

If the zero eigenvalue is simple, the adjugate is proportional to psi psi^dagger. Thus rho_i=C_i/S, S=sum_i C_i !=0. Whenever d_i!=d_j,

    d_k*d_l=1/3-S/(2c).

Every unequal pair has the same complementary product.

### Three or four distinct densities are impossible here

Four distinct d values contradict the common complementary-product rule. For three distinct values, the repeated value must be zero: the only remaining pattern is (a,b,0,0), up to permutation. Its determinant and cofactor sum give

    a*b=3, S=-(a+b).

The complementary product is zero, forcing S=2c/3, hence a+b=-2c/3. But a*b=3 requires (a+b)^2>=12, whereas c^2<27 gives (a+b)^2=4c^2/9<12. Contradiction. The frozen c=3/50 satisfies that strict condition.

### A multiple zero eigenvalue cannot bypass the classification

If the kernel has dimension at least two, all principal three-by-three minors vanish. Their differences force (d_i-d_j)*(d_k*d_l-1/3)=0. A 1:3 pattern would require b^2=1/3 and b^3-b=0 simultaneously. A 2:2 pattern would require a*b=1/3 and a+b=0. Both are impossible over the reals. Three-distinct patterns also violate the complementary product. Hence all d_i are equal, and the repeated zero occurs only at d=+/-1.

Equal d values imply uniform density rho_i=1/4. Yet every pure state in either Q eigendoublet has sum rho_i^2=1/3, not 1/4. The checker verifies that identity symbolically for general complex coordinates in each eigendoublet. Thus no multiple-kernel stationary pure state exists.

Every stationary minimum therefore belongs to a two-density 1:3 or 2:2 pattern, including zero-address limits. This is an analytic exhaustion, not random minimizer sampling.

## 3. Compare the exhausted critical families

### One address versus the other three

For d=(a,b,b,b),

    D=(b^2-1)*(a*b-1).

The b=+/-1 branches with zero amplitude on the selected address are the source coherent/dark states supported on the other three sites. Their energies are respectively 0.18 and 2.18.

The a*b=1 branch reduces to the source-derived two-direction kinetic matrix [[1,-1],[-1,1]]. Its low phase branch has

    psi_i proportional to ((r+1)I-K)e_i,
    3r^4+6c*r^3-2c*r-3=0,
    1/sqrt(3)<r<1.

The t=r^2/(1+r^2) functional is strictly convex on 1/4<t<1/2. There is one low stationary root. The opposite phase has kinetic energy at least one and cannot compete.

The minimizing density is

    (0.490386324555405,0.169871225148198,
     0.169871225148198,0.169871225148198),

with the high address permuted among the four sites. The dark fraction is 0.000092431299099.

### Two addresses versus two

For d=(a,a,b,b),

    D=(a*b-1)^2-(a-b)^2/3.

The two-site internal blocks have kinetic conference eigenvalues +/-1/sqrt(3), with cross-block strength sqrt(2/3). The lower phase branch has pair imbalance z=(rho_A_total-rho_B_total)>=0 and kinetic energy

    1-z/sqrt(3)-sqrt(2/3)*sqrt(1-z^2).

The quartic term is c*(1+z^2)/4. Its derivative is strictly increasing, giving one low root. Put z=y/sqrt(3); the stationary equation becomes

    2y^2-(1-c*y/2)^2*(3-y^2)=0, 0<y<1.

Eliminating the radical at that root gives an exact rational expression in y for the stationary energy. Rational root brackets certify

    E_2:2=0.1799010143019994...

The sign-opposed low branch has no stationary point at positive imbalance. The high phase branches have kinetic energy at least 1-1/sqrt(3)>0.4, already above the candidate total energy. A pair with zero total amplitude cannot be stationary because its cross-block coupling is invertible.

### Exact ordering

The rational intervals give

    E_1:3 < E_2:2 < E_zero-address coherent.

All remaining phase branches are higher. Compactness and the exhausted stationarity cases prove the global minimum, not merely local stability.

The interval for E_1:3 is enclosed with 100 rational bisection steps. Its lower and upper bounds both round to 0.1798077094008586, but the stored exact rational endpoints are distinct.

## 4. Exact rotation and phase transport

Reconstruct the 24 binary tetrahedral rotations on the actual stored raw spinor. Transport them through the weighted local-line embedding and decoder. The reduced actions T obey

    T K=K T,
    T e_i=zeta(T,i)*e_perm(i),
    |zeta|^2*m_perm(i)=m_i.

Consequently, for EVERY r,

    T[((r+1)I-K)e_i]
      =zeta(T,i)*[((r+1)I-K)e_perm(i)].

This polynomial identity applies to the exact algebraic minimizing root, not just its numerical approximation. The metric fixes the normalized transport phase. Site density and the unique Gauss potential transform by the same source permutation; the common exterior energy is unchanged.

All group multiplication identities are checked exactly. The central element has T=-I_4, so a full rotation retains the minus sign on each minimizing lift. Projectivizing the rays must not erase that sign from retained histories.

## 5. The nonlinear ground set is not a linear doublet

The four minimizing column vectors form the map

    ((r+1)I-K).

Its determinant is (r+1)^2*(r-1)^2, nonzero at the minimizing r. Hence the ground orbit spans all four local-line coordinates.

Only its four rays minimize the classical nonlinear functional. Arbitrary superpositions are not additional minima. The binary spinorial sign survives, but a rank-two linear ground projector does not follow from this deformed orbit.

With the existing one-unit occupation baseline, the elementary energy is 1.1798077094008586... clock units. No electron mass or neutron splitting was used to select the state or this reference baseline.

## Next carrier-level construction

Completed classical continuation: `spinor-interacting-construction.md` gives the nonorthogonal amplitude state space, conserved lead sectors and coupled dynamics. Quantization remains separate.

Construct the interacting state space and its quantum or retained-composition dynamics on this actual four-ray orbit. A ground doublet must emerge from a tested dynamics/quantization if it is required; it cannot be assigned by calling the classical orbit spin one-half. The physical implementation of the hard flux sector remains separate.

## Verify

    uv run --with sympy python research/voevodsky/checkers/check_spinor_ground_orbit.py

Results: `results/spinor_ground_orbit.json`. Symbolic checks certify the determinant/cofactor and eigendoublet-purity identities; exact rational brackets compare critical families. Exact source arithmetic verifies 24 rotation maps, 576 group products and the retained central sign. The case-exhaustion argument above supplies the global proof; no floating eigensolver or stochastic minimizer is its evidence.
