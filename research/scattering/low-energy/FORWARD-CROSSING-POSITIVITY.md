# Forward crossing and conditional polarization positivity

[Contract](contracts/forward-crossing-positivity.v1.json) · [checker](check_forward_crossing_positivity.py) · [receipt](results/forward-crossing-positivity.v1.json)

## 1. Crossing is not a positive polarization channel

The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) constructed positive right-cut matrices on all coherent two-beam polarization states and showed that signed IR density subtraction need not preserve positivity. Here derive the forward crossing map in the same transported helicity frame. No global dispersion law or UV completion is admitted.

Retain the order (++ , -- , +- , -+). A matrix index ab labels the outgoing pair and cd the incoming pair. Exchanging legs 2 and 4 flips their incoming/outgoing helicity signs, giving

    Gamma(A)_(ab,cd)=A_(a,-d;c,-b)
                   =(I tensor X)*A^(T2)*(I tensor X),

where X exchanges the two single-photon helicities and T2 is partial transpose on the second polarization factor. This is frame-specific notation for analytic crossing, not a native charge action or a physical quantum channel. Gamma preserves Hermiticity and trace, is self-adjoint for the trace pairing and squares to identity. It is **not positive** on arbitrary positive matrices, let alone completely positive.

This sign/phase convention is checked against the actual field-strength sections, not merely chosen from two-qubit notation. At physical forward s>0, for every ordered input pair k,l with q=k+l,

    H_s(s)=s^q*F_kl,
    H_u(s)=(-1)^q*Gamma(H_s(s)),
    H_t(s)=0 in the continuous forward limit.

Here F_kl is the full forward coefficient of the parent cut, not its J=0 projection. The checker tests all sixteen helicity sections, both odd and even q, and two rational energies. General crossing/tensor arguments are documented mathematics, not machine-formalized theorems.

For the real parity-even audited matrix F(D,O,M), Gamma interchanges D and M and leaves O unchanged. Hence

    K_even=F+Gamma(F)
      =[[D+M,2O,0,0],[2O,D+M,0,0],[0,0,D+M,0],[0,0,0,D+M]],
    K_odd=F-Gamma(F)=diag(D-M,D-M,M-D,M-D).

K_even need not be positive as an operator, even though F is positive.

## 2. Which preparations support positive even crossed sums?

A normalized positive density rho tests the crossed sum by

    Tr[rho*(M+Gamma(M))]=Tr[(rho+Gamma(rho))*M].

For arbitrary positive matrix controls M, the exact dual-cone condition for nonnegativity is

    rho+Gamma(rho) >=0.

This follows from self-duality of the positive-matrix cone. It is a statement about unrestricted matrix controls, not a claim that every such control is realizable as a UV photon spectrum. If additional axial restrictions are imposed on the controls, the dual can instead be tested after the parent's azimuth twirl.

Every product preparation satisfies the condition: for z=a tensor b,

    z^dagger*Gamma(M)*z=(a tensor X*b_conjugate)^dagger
                            *M*(a tensor X*b_conjugate)>=0.

Mixtures of product preparations do also. More generally rho with positive partial transpose is sufficient. It is **not necessary** for the even sum with the *same* M on both cuts: take rho=(3/5)*I/4+(2/5)*|Bell_plus><Bell_plus|. Gamma(rho) has a negative eigenvalue, but rho+Gamma(rho) is positive. Thus some entangled mixed preparations belong to this dual cone. If two independent positive controls were used instead of the same crossed M, the stronger rho>=0 and Gamma(rho)>=0 conditions would be required universally.

For the actual **real parity-even cut cone** D>=|O|, M>=0, a simpler exact characterization is possible. With Tr rho=1, put x=Re rho_(++,--). Then

    Tr[rho*K_even]=D+M+4*O*x.

The three extremal rays (D,O,M)=(1,1,0),(1,-1,0),(0,0,1) prove that nonnegativity for this entire cone is equivalent to

    |Re rho_(++,--)|<=1/4.

For a pure normalized vector replace rho_(++,--) by z_++*conjugate(z_--). All product vectors obey the bound. The entangled relative-phase-i Bell state also obeys it, while both real Bell states fail the *universal* restricted-cone criterion. A particular spectrum may admit more states: for the c0-only control the allowed x is x<=63/200 because its O is negative. Do not promote the restricted cone or its enlarged preparation domain to all possible UV matrices. In particular, phase-i Bell safety here is not a generic positive-partial-transpose claim.

For odd crossing, the unrestricted dual test rho-Gamma(rho)>=0 has trace zero, so it can only hold when rho=Gamma(rho), in which case the test vanishes. There is no nontrivial universal odd positive bound. In the restricted cone its universal zero condition is equal weight in the equal- and mixed-helicity diagonal sectors.

## 3. Certified negative controls, not a unitarity violation

The c0-only polynomial control R=s^2 has forward eigenvalues (107/480,7/480,1/80)*s^4. Its n=2 moment at tau=1/2 is positive, but the Bell-plus expectation of M_2+Gamma(M_2) is

    -37/3840.

Its product-helicity expectation is positive. The odd n=3 sum has opposite-sign diagonal entries +/-17/320, including product preparations of both signs. These statements concern crossed sums without the overall dispersive factor 1/pi.

The same even-sum failure is certified in the infinite conditional spectral family with c0=c1=0. The parent supplies exact rational enclosures of pi^2*M_2. Propagating them to the Bell-plus value

    (-m_minus+3*m_plus)/2+m_mixed

gives a strictly negative upper endpoint. This is not a sign test using rounded floating-point numbers. There is no conflict with unitarity: Gamma is not positive, and the original right-cut moment remains positive. Nor does the counterexample exclude all entangled preparations.

## 4. The conditional forward contour statement

Consider a forward amplitude G(z) at a declared scope, after accounting for poles and a well-defined forward limit. To use its cut for a dispersion bound, additionally assume:

1. Hermitian analyticity and G(-z)=Gamma(G(z)) in this frame.
2. A finite small-z jet through degree n, with the small-circle contribution accounted for. For this audit's massless germ, n<2*k0 suffices if the retained IR cut inventory is exhaustive and the remaining matching part has a regular jet; at the first logarithmic degree it does not.
3. Vanishing large contour at the desired degree, e.g. G(z)=o(|z|^n) uniformly on the large contour, and convergent cut moments. With an N-subtracted representation, coefficients below N remain subtraction data; use n>=N when invoking that representation.
4. Positivity of the complete cut at the **same scope** as the coefficient being bounded, not a positive full-amplitude cut substituted for an arbitrary perturbative coefficient.

Under these *additional hypotheses*, the pole-accounted small-z jet coefficient obeys

    C_n=(1/pi)*integral_0^infinity
                  [F(x)+(-1)^n*Gamma(F(x))]*x^(-n-1) dx.

On the negative cut, Hermitian analyticity and crossing give Im G(-x+i0)=-Gamma(F(x)); changing variables in the contour gives the displayed (-1)^n. The small-z jet language matters: a massless branch point need not admit a holomorphic Taylor series even when its lower finite jet exists.

For an even n and a preparation in the appropriate dual cone, splitting the integral at tau gives the conditional lower bound

    pi*Tr(rho*C_n) >=Tr[rho*(M_n(tau)+Gamma(M_n(tau)))].

It requires both IR convergence and positivity of the remaining same-scope cut. If only the restricted preparation criterion is used, the remaining UV cut must additionally lie in that restricted cone. No such global physical assumptions are source-licensed here. In particular, the fixed pure-g2^4 cut below threshold is positive, but UV coefficients at this order can include signed interference with lower-order open-channel amplitudes. A full unitary amplitude's positive spectrum does not remove this perturbative-scope problem. The gate checker only verifies logical eligibility under supplied hypothetical assumptions; it does not admit them or prove a completion exists. The old leading-response subtraction count is not a derived UV-growth bound on the quartic amplitude.

## 5. Explicit cut-free matching ambiguity

Forward crossing and the retained IR cut alone cannot fix finite matching. The parent's local Bose/Ward tensor for monomial R=s^2 restricts at forward kinematics to s^2*L2, where

    L2=[[1/2,-1,0,0],[-1,1/2,0,0],[0,0,1/2,0],[0,0,0,1/2]],
    Gamma(L2)=L2.

The R=s^3 tensor similarly gives s^3*L3, with L3=diag(1,1,-1,-1)/2 and Gamma(L3)=-L3. Therefore arbitrary **quartic-order** finite counterterms

    delta B(z)=lambda2*z^2*L2+lambda3*z^3*L3

preserve crossing, Hermitian analyticity and the same cut. These independent lambda values do not change the fixed leading r_k. They shift lower regular jet coefficients without bound in the cut-only control. They are forward restrictions of actual local field-strength tensors, not arbitrary nongauge matrix polynomials; the checker verifies those restrictions. This is not a claim that every lambda admits a full unitary UV completion. It demonstrates precisely what the audited cut data leave free.

A nonzero lambda_n*z^n term contributes to the large contour for C_n and violates the extra little-o growth condition at that degree. Dropping that arc while retaining the free polynomial would be inconsistent. More-subtracted relations allow the corresponding independent subtraction coefficients. Thus the conditional contour theorem is not an unconditional matching determination.

## 6. Boundary and executable successor

No finite physical matching bound, source spectrum, native preparation, physical rate, UV completion or exact S operator is established. Independent dimensionful couplings, C1-C12, exhausted C12 effort, historical owner/hash warnings and the high-energy pause remain unchanged.

The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected.

**Next:** construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom.

```sh
python -S research/scattering/low-energy/check_forward_crossing_positivity.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_forward_crossing_positivity.py
```
