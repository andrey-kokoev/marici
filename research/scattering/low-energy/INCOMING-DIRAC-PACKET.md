# EF1 continuation: a normalizable imported incoming Dirac pair and its currents

[Contract](contracts/incoming-dirac-packet.v1.json) · [checker](check_incoming_dirac_packet.py) · [receipt](results/incoming-dirac-packet.v1.json)

## 1. Scope and conventions

Following the [full outgoing-profile projection](LOCAL-HELICITY-PROJECTION.md), construct an explicit incoming electron/positron packet in the **imported free Dirac Fock space**. This closes the mathematical packet/current gate for a declared example. It does not identify a native encounter with this state, select a physical preparation, or derive an interacting scattering operator.

Use metric (+---), dPi_m(p)=d^3p/((2*pi)^3*2*p0), canonical Dirac gamma matrices, gamma5=i*gamma0*gamma1*gamma2*gamma3. Fix the creation order b_s^dagger(p_-) d_r^dagger(p_+)|0>. There is one particle of each charge: no identical-photon 2! belongs in its norm. All masses below use a declared unit m=1, not a calibration of the physical electron mass.

Let M>2m, E=M/2, k=sqrt(E^2-m^2), and CM momenta k_-=(E,k*n), k_+=(E,-k*n). With Pauli basis chi_s and eta_r=i*sigma2*conjugate(chi_r), use

    u_s = sqrt(E+m) [chi_s; sigma.p/(E+m)*chi_s],
    v_r = sqrt(E+m) [-sigma.p/(E+m)*eta_r; eta_r].

They obey the respective free Dirac equations, ubar*u=2m, vbar*v=-2m and u^dagger*u=v^dagger*v=2E. Define a common moving spin frame by transporting the CM pair with the free Dirac representation of B(u), the rotationless boost of (1,0) to u. The individual canonical spin frames differ by their unitary spin-1/2 Wigner matrices; they are not discarded or replaced by scalar labels. Explicitly W_±=B(p_±/m)^(-1)*B(u)*B(k_±/m). Each W fixes the time axis and is a proper rotation. Products of boosts require the same spin transport, not a fresh projection onto a fixed Pauli frame.

## 2. Exact normalizable full incoming packet

The massive distinguishable-pair coarea is

    dPi_m(p_-)*dPi_m(p_+) = d^4P/(2*pi)^4 * Phi_2m(M)*dnu(n),
    Phi_2m(M)=beta(M)/(8*pi), beta(M)=sqrt(1-4*m^2/M^2),
    dnu=dOmega/(4*pi), d^4P=M^3*dM*dmu(u), P=M*u.

As before, u(q)=((1+q^2)/(1-q^2),2q/(1-q^2)) and dmu(u)=8*d^3q/(1-q^2)^3. Choose

    a(M)=1 on 3<M<4, zero otherwise,
    b(u(q))=(1-q^2)^(3/2) on (-1/4,1/4)^3, zero otherwise.

Thus integral |a|^2*dM=1 and integral |b|^2*dmu=8*(1/2)^3=1. Choose any unit four-spin vector z, constant in the CM direction. In the transported spin frame set

    Xi_sr(p_-,p_+)=(2*pi)^2*a(M)*b(u)*z_sr / sqrt(M^3*Phi_2m(M)).

Then sum_sr integral dPi_-*dPi_+*|Xi_sr|^2=1 exactly. All directions are retained coherently. The boost cube lies strictly inside the unit ball and the mass box stays strictly above 2m; all constituent momenta are bounded. Packet norm, finite energy and the vacuum-current matrix elements below are well-defined. More generally the map z -> Xi_z preserves inner products, so this is a conditional spin-coefficient-to-packet isometry. A sharp total momentum, a sharp CM direction, or a delta at M=2m would not be this L2 state. At threshold the phase volume vanishes; cancelling a zero density does not make a delta-normalized state normalizable.

This is an explicitly chosen correlated S-wave incoming pair, not a source-derived beam distribution or an assertion that arbitrary physical preparations are S waves. The mass box is illustrative, not a derived cutoff: m=1 does not calibrate a Dirac mass against the old lead hopping scale, and putting this example below the old band edge does not repair source/envelope binding. General incoming Dirac pairs have M>2m, not M<4. More general normalized mass/boost/angular functions are possible. Neither unpolarized one-body marginals nor this normalization selects the singlet fraction.

## 3. Spin-resolved vacuum-to-pair currents

These are transition matrix elements <0|:psibar*Gamma*psi:|pair>, not the expectation value of charge density in the pair. For the stated creation order their kernel is vbar_r*Gamma*u_s. With epsilon=i*sigma2 and B_j=sigma_j^T*epsilon, define orthonormal spin states

    s = (|up down>-|down up>)/sqrt(2),
    t_x = (-|up up>+|down down>)/sqrt(2),
    t_y = i*(|up up>+|down down>)/sqrt(2),
    t_z = (|up down>+|down up>)/sqrt(2).

Thus z=alpha*s+sum_j c_j*t_j with |alpha|^2+sum|c_j|^2=1. Direct Dirac algebra gives

    P_sr=vbar_r*i*gamma5*u_s = -i*M*epsilon_sr,
    J^0_sr=0,
    J^i_sr=sum_j V_ij(n)*(B_j)_sr,
    V(n)=M*I-(M-2m)*n*n^T.

The singlet has P=-i*sqrt(2)*M*alpha and zero vector current; the triplet has P=0 and J_vec=sqrt(2)*V(n)*c. These are statements inside the imported canonical-spin construction, not a proof identifying the native finite triplet with a physical Dirac preparation.

### Coherent S-wave averaging and retained D-wave kernel

Put D(n)=n*n^T-I/3, aV=2*(M+m)/3 and bV=M-2m. Then V=aV*I-bV*D, with

    integral D*dnu=0,
    integral D^2*dnu=(2/9)*I.

For the prepared coherent S wave, the vector current is sqrt(2)*aV*c. Averaging |V*c|^2 instead would describe an incoherent directional mixture and give a different result. Specifically the full current kernel Gram per spatial component is

    S part: 2*aV^2 = 8*(M+m)^2/9,
    D part: 4*(M-2m)^2/9,
    total:  2*(2*M^2+4*m^2)/3.

The omitted part is a genuine possible incoming channel, not a probability loss: a normalized spin-triplet D-wave angular function c(n)=(3/sqrt(2))*D(n)*w has unit norm for unit w, is orthogonal to the constant S wave, and yields vector current -2*(M-2m)*w/3. It vanishes at threshold only. These S/D functions span the angular dependence to which this point vector current couples; an arbitrary incoming packet need not have either preparation. Their relative amplitudes can interfere coherently. In fact, put jS=sqrt(2)*aV, jD=-2*bV/3 and N=sqrt(jS^2+jD^2). The unit angular-spin state (-jD*S_j+jS*D_j)/N has zero vector transition current at each M; it is triplet, so its pseudoscalar current is also zero. Using it in the same compact mass/boost packet gives a normalizable current-null alternative. The incoherent mixture of its S/D components has strictly positive vector strength for M>2m. This is a first-order null for these chosen point currents, not a no-annihilation theorem for QED or all perturbative orders. No S/D or singlet/triplet mixture has been source-selected.

## 4. Packet Fourier currents, including phase volume

Define Jtilde_Gamma(P)=integral d^4x exp(i*P.x)*<0|:psibar*Gamma*psi:(x)|Xi>. The delta function leaves the two-body phase volume, not its reciprocal. For the declared S-wave packet put

    K(P)=(2*pi)^2*a(M)*b(u)*sqrt(Phi_2m(M)/M^3).

Then

    Ptilde(P)=K(P)*[-i*sqrt(2)*M*alpha],
    Jtilde^mu(P)=K(P)*sqrt(2)*aV*B(u)^mu_j*c_j.

The vector is transverse: P_mu*Jtilde^mu=0. Its invariant squared magnitude is -Jtilde^* . Jtilde=|K|^2*2*aV^2*||c||^2. The pseudoscalar magnitude is |K|^2*2*M^2*|alpha|^2. Neither the threshold factor nor the different mass/current powers can be absorbed into an allegedly universal branching law. The actual current phase and the coherent S-wave integral survive, and arbitrary alpha,c remain preparation data.

The checker verifies exact spinor equations and spin-channel amplitudes in nine CM cases, 27 boosted current cases including non-collinear boost products, 54 individual Wigner rotations, analytic sphere moments, the coarea/norm cancellations and hostile controls. General coarea, Dirac representation and L2 packet arguments are documented mathematics, not machine-formalized proofs. The zero/positive threshold domain is checked separately from algebra at a mass endpoint.

## 5. Next executable gate

The [outgoing Born construction](OUTGOING-BORN-MAP.md) now supplies full two-/three-photon maps and finite compact-packet transition norms, retaining the separate dimensionful couplings, Bose factors, phase volumes, mass powers, preparation dependence and orthogonal output. Its exact integrals retain the massive threshold. The [on-shell completion audit](ON-SHELL-UNITARY-COMPLETION.md) now retains those channels and constructs two unitary controls with the same Born and second-order forward terms but different finite conversion strengths. The [packet weak-coupling audit](PACKET-WEAK-COUPLING-TAIL.md) now certifies compact errors and a finite-energy unbounded packet outside the Born domain. Its model strengths have completion-dependent nonanalytic leading terms; ordinary cutoff/weak limits commute but specified rescaled limits do not. The [bright-tail domain audit](BRIGHT-TAIL-DOMAIN.md) now classifies the power/log boundaries and constructs two normalized damping controls preserving the low-mass wavefunction and tail norm, not a selected interaction form factor or an all-orders convergent series. The [complex-mass audit](COMPLEX-MASS-ANALYTICITY.md) now finds that the eta=1 scalar analytic candidate fails subthreshold open-photon contractivity, while both identity patches differ from their upper germs. Certified imaginary-mass poles map to negative s, not a general local-QFT exclusion. The [scalar dispersive response](SCALAR-DISPERSIVE-RESPONSE.md) now matches the charged-pair cut with four full-response subtractions (two after Ward factoring), retaining free s^2 and s^3 terms and a nonzero dispersive phase. It is a right-cut control, not an exact unitary or crossing-complete amplitude. The [crossed four-photon audit](CROSSED-FOUR-PHOTON.md) now supplies the leading Bose/Ward tensor and scalar cuts at +/-4. It preserves J0 parity in the photon-elastic block but gives a nonzero orthogonal-channel response, not J0-to-J2 leakage. The massive-pair-only leading response is analytic at zero, unlike the zero-phase Cayley germ. The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ. The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Neither completion is source-selected or a spacetime Hamiltonian. A finite first-order norm is not a unitary scattering operator, an irreversible rate, or an all-energy UV completion. Matching native physical preparation and an interaction form factor remains a separate evidence gate.

The previous rational-envelope obstruction is still restricted to finite-derivative, constant-coefficient point-current tree contacts. C1-C12 and exhausted C12 effort are unchanged; high-energy execution remains paused. Historical owner/hash warnings are retained. No physical outcomes or measured rates are admitted.

```sh
python -S research/scattering/low-energy/check_incoming_dirac_packet.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_incoming_dirac_packet.py
```
