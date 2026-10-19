# Local source vertices: conditional EFT candidates and a contact-envelope obstruction

[Contract](contracts/local-source-vertex.v1.json) · [checker](check_local_source_vertex.py) · [receipt](results/local-source-vertex.v1.json)

## Result

Two explicit local, gauge-invariant, charge-neutral Wick-density candidates now give nonzero two-/three-photon current vertices with the required C signs. Their locality uses a **new imported free Dirac/Maxwell field algebra**, not native L/G/N operations. Neither is asserted to generate the preceding selected-mode mass Hamiltonian.

A separate restricted obstruction shows that its rational envelope cannot be the exact tree contact amplitude of a point current with finitely many derivatives and constant coefficients. This is not a no-go for composite source form factors, mediators, loops or local UV completions.

## 1. Imported source and photon operators

Take a charged free Dirac field psi and a free Maxwell field strength F_mu_nu on their tensor-product field algebra. Define neutral, even-fermion source bilinears

```
P=normal_order(psi_bar*i*gamma5*psi),
J_mu=normal_order(psi_bar*gamma_mu*psi).
```

Use real coefficients and Hermitian Wick ordering for the local density

```
L_int = c_s*normal_order(P*F_mu_nu*dualF^{mu_nu})
      + c_t*normal_order(J_mu*d_nu[F^{nu_mu}*(F_rho_sigma*F^{rho_sigma})]).
```

The derivative acts on the **whole** photon product, not only the first free Maxwell factor. Writing it as (d_nu F^{nu_mu})*F^2 would incorrectly set the entire cubic vertex to zero on free photon legs.

Both source bilinears are neutral under global charged U(1) and even in fermion parity. In the standard Dirac convention C=i*gamma2*gamma0, direct Clifford/transpose checks give

```
C*(i*gamma5)^T*C^(-1)=i*gamma5,
C*(gamma_mu)^T*C^(-1)=-gamma_mu.
```

Thus P is C-even and J is C-odd. F changes sign under C, so F*dualF is even and d(F*F^2) is odd. Each complete density is C-even. The gamma0-adjoint identities also verify Hermiticity of the bilinears. These are imported Dirac-field statements, **not** a conversion of the old antiunitary or a licensing of the raw Pauli-code flip.

The pseudoscalar photon operator couples a pseudoscalar current; the cubic derivative operator is a Lorentz vector to couple to J. In CM, its current amplitude is spatial/transverse. This provides local candidates, not an identification of the native finite triplet with physical spin or an incident pair preparation.

In four-dimensional canonical power counting, the density dimensions are 7 and 10, so the EFT coefficient dimensions are -3 and -6. Their ratio is dimensionful; they must not be equated to the two normalized finite-code energy coefficients without matching conventions, source states and scales. No dimensionless branch ratio follows.

## 2. Photon amplitudes and exact checks

For an on-shell photon with momentum k_i and polarization epsilon_i, strip common conventional i factors and define

```
f_i^{mu_nu}=k_i^mu*epsilon_i^nu-k_i^nu*epsilon_i^mu,
Q=sum_i k_i.
```

Overall combinatorial constants can be included in the independent EFT coefficients. The checked two-photon pseudoscalar tensor is

```
A2=epsilon_mu_nu_rho_sigma*k1^mu*epsilon1^nu*k2^rho*epsilon2^sigma.
```

The checked cubic vector is

```
A3^mu=Q_nu*sum_(i=1)^3 f_i^{nu_mu}*(f_j:f_k),
{j,k}={1,2,3} without i,
f_j:f_k=sum_(rho,sigma) eta_rho*eta_sigma*f_j^{rho_sigma}*f_k^{rho_sigma}.
```

This is the cubic photon part of the derivative operator up to its overall convention. It is symmetric under all photon permutations, and Q_mu*A3^mu=0 by antisymmetry. Every term contains all three field strengths. Replacing any polarization by its momentum gives zero, so the Ward identity is manifest for every leg, not imposed by a selected polarization gauge.

The checker tests real transverse two-photon data and all eight three-photon helicity assignments on each of two nondegenerate CM configurations. It checks fifty Ward replacements, ninety-six Bose permutations, seventeen proper-Lorentz tensor covariance cases and thirty-four homogeneous rescalings. Forty-eight checks confirm that each single free Maxwell factor has zero divergence, while the whole-product derivative still gives a nonzero cubic amplitude. The equal-energy all-plus three-photon configuration has a nonzero component along the plane normal, giving an explicit nonzero vector witness.

With fixed dimensionless polarizations and external source-current components, momentum rescaling k_i -> t*k_i gives A2 -> t^2*A2 and A3 -> t^4*A3. These powers concern **amputated photon vertices**, not rates or a prepared charged-pair distribution.

The naive polarization contraction epsilon1.epsilon2 is not a substitute for A2: a Ward replacement on a gauge-equivalent polarization representative makes it nonzero. Transversality in one convenient CM gauge alone would miss that failure.

## 3. What local density does and does not establish

Assume the standard spacelike locality of the free Maxwell observable algebra, graded locality of the free Dirac algebra, and commutation of the two field species. Even Dirac bilinears, Maxwell Wick polynomials and their derivatives then commute at spacelike separation as operator-valued distributions. Real compact spacetime test-function smearing gives the corresponding formal Hermitian densities on the usual free-field test domain.

The equal-energy configuration also gives a nonzero mixed-helicity (-,-,+) vector amplitude, including its normal component. This lies outside the preceding equal-helicity three-photon code, including its added shape multiplier. Continuity at that nondegenerate interior configuration gives nonzero amplitude on an open set and hence positive conditional norm in the omitted helicity sector for a nonzero vector current after rotation integration. **This particular cubic local candidate does not close on the selected eight modes.** No normalized leakage fraction is yet calculated, and this is not an exclusion of every other local operator.

This is a conditional local algebra construction. It is **not** an essentially self-adjoint interacting Hamiltonian or a nonperturbative four-dimensional theory. The irrelevant EFT interactions require renormalization/counterterms if used beyond the stated tree vertices. Nor does a projection onto selected photon profiles inherit the full field's local commutator. Omitted helicities, momenta, particle sectors, adjoint/counter-rotating terms and virtual processes cannot simply be deleted while retaining a microcausality claim.

The source currents carry timelike Fourier momentum Q; they are not spacetime-constant backgrounds. Although the photon operators have total-derivative forms, integration by parts then differentiates the varying source, not a vanishing constant. Dirac-current conservation does not set d_nu J_mu to zero.

Nothing here derives a native Dirac field, a source-to-current matrix element, a flux, a physical incident spin density, or cluster separability of the preceding point-form mass model.

## 4. Restricted finite-derivative matching test

The earlier [unbounded envelope](PHOTON-ENERGY-TAIL.md) used, after retaining its phase-volume constants,

```
f_n(M)=sqrt(30/A_n)*M^(3-n)/(1+M)^3,
n=2,3.
```

A finite sum of **tree-level point-current contact terms**, with finitely many derivatives and constant coefficients, has polynomial amputated photon amplitudes on a fixed dimensionless shape/polarization ray. Projection against a fixed M-independent normalized relative profile leaves a polynomial in M whenever those shape integrals exist. This comparison is before the extra full-packet coarea half-density; packet normalization is not an interaction vertex.

No nonzero finite polynomial p can equal either M/(1+M)^3 or 1/(1+M)^3 on an open positive M interval. Otherwise polynomial identity would imply

```
(1+M)^3*p(M)=M^a, a=1 or 0.
```

At M=-1 the left side vanishes while the right side is -1 or +1. The negative value is an algebraic identity test, not an allowed negative-energy photon. The checker verifies the divisor root and both nonzero numerators; the proof applies to every finite degree, not just the sample polynomials.

Therefore the exact chosen envelope is **not supplied by these or any finite-derivative constant-coefficient point-current tree vertices alone**. It needs additional source structure, propagation/mediators, nonlocal effective smearing, loop amplitudes, or a separately prepared envelope. Such effects may arise in an underlying local theory; they are not excluded. Actual electron/positron current matrix elements also depend on preparation and are outside the fixed external-current hypothesis.

The bare local candidates grow with energy and do not by themselves solve the UV normalization/self-adjointness problem previously exposed. An independently selected source form factor or UV completion is still needed. Fitting one to the desired spectrum or multiplicity ratio would not be a native derivation.

## 5. Next executable gate

The [full helicity projection](LOCAL-HELICITY-PROJECTION.md) now computes the conditional norms and coherent overlaps. The cubic candidate's prior all-plus profile span retains 1/4 and leaves 3/4 orthogonal, with mixed helicities carrying 3/8; the old band support is retained separately. These are profile overlaps, not photon multiplicity fractions. The [incoming Dirac packet](INCOMING-DIRAC-PACKET.md) now supplies that calculation for a declared normalizable imported S-wave preparation, retaining threshold, spin transport, mass/boost measure and the possible D-wave current kernel. The [outgoing Born maps](OUTGOING-BORN-MAP.md) now retain those full profiles and finite compact-packet strengths with phase volumes, Bose factors and separate dimensionful couplings, not a unitary scattering construction. The [on-shell completion audit](ON-SHELL-UNITARY-COMPLETION.md) now retains those channels in two unitary controls sharing the Born and second-order forward terms but not finite conversion strengths. The [packet weak-coupling audit](PACKET-WEAK-COUPLING-TAIL.md) now certifies compact errors and a finite-energy unbounded packet outside the Born domain, with completion-dependent nonanalytic strengths. Ordinary cutoff/weak limits commute; specified rescaled limits do not. The [bright-tail domain audit](BRIGHT-TAIL-DOMAIN.md) now classifies the power/log boundaries and constructs two normalized damping controls preserving the low-mass wavefunction and tail norm. They restore finite-order Born recovery, not a selected interaction form factor or a convergent all-orders series. The [complex-mass audit](COMPLEX-MASS-ANALYTICITY.md) now finds that the eta=1 scalar analytic candidate fails subthreshold open-photon contractivity, while both identity patches differ from their upper germs. Certified imaginary-mass poles map to negative s, not a general local-QFT exclusion. The [scalar dispersive response](SCALAR-DISPERSIVE-RESPONSE.md) now matches the charged-pair cut with four full-response subtractions (two after Ward factoring), retaining free s^2 and s^3 terms and a nonzero dispersive phase. It is a right-cut control, not an exact unitary or crossing-complete amplitude. The [crossed four-photon audit](CROSSED-FOUR-PHOTON.md) now supplies the leading Bose/Ward tensor and scalar cuts at +/-4. It preserves J0 parity in the photon-elastic block but gives a nonzero orthogonal-channel response, not J0-to-J2 leakage. The massive-pair-only leading response is analytic at zero, unlike the zero-phase Cayley germ. The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ. The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. These controls are not a local scattering Hamiltonian. Test whether any actual native encounter licenses that source and supplies its spectral form factor. This can distinguish a source-selected amplitude from the earlier freely chosen envelope; it must not assume the selected eight modes form an invariant local algebra.

Exact matrix/tensor checks support the analytic Ward, charge and restricted polynomial arguments. Local distributional commutation is conditional on the stated imported field theory and is not machine-formalized. No physical outcome, rate, spectrum or branching ratio is admitted. C1–C12, exhausted C12 effort, paused high-energy execution and historical warnings are unchanged.

```sh
python -S research/scattering/low-energy/check_local_source_vertex.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_local_source_vertex.py
```
