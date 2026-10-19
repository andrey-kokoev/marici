# Local-current photon profiles: full helicity norm and retained remainder

[Contract](contracts/local-helicity-projection.v1.json) · [checker](check_local_helicity_projection.py) · [receipt](results/local-helicity-projection.v1.json)

## Result and scope

The [specific local current candidates](LOCAL-SOURCE-VERTEX.md) now have a full relative-helicity norm decomposition, not just nonzero sample amplitudes. For the cubic vector candidate, the preceding constant/shape-multiplied all-plus triplet profiles retain exactly **1/4** of its normalized conditional norm at a fixed mass where both profiles are available. The orthogonal **3/4** is retained explicitly. In particular mixed helicities carry 3/8 of the full conditional norm.

This is a profile-overlap theorem for that chosen imported Wick vertex, **not** an annihilation branch fraction, a choice of source spin statistics or a statement about every local interaction. The mass/current dependence, phase volumes, old band support and omitted profiles are not discarded. The [incoming Dirac continuation](INCOMING-DIRAC-PACKET.md) now constructs a normalizable imported pair packet and its transition currents; the [outgoing Born maps](OUTGOING-BORN-MAP.md) now retain full photon profiles and finite compact-packet strengths, with the unitarity/elastic gate explicit.

## 1. Complete helicity tensor in CM

Use the prior shape coordinates y_i=1-2*E_i/M, sum y_i=1, y_i>0, with dnu_shape=2*dy1*dy2. Let N be the oriented plane normal, n_i=k_i/E_i and t_i=N cross n_i. The same transported helicity frame is

```
epsilon_i(h_i)=(0,(t_i+i*h_i*N)/sqrt(2)), h_i=+/-1.
```

The scalar field-strength contraction has the exact identity

```
f_j:f_k = M^2*y_i if h_j=h_k,
          0 otherwise,  {i,j,k}={1,2,3}.
```

For example this follows by using t_j.t_k=n_j.n_k and the sine/cosine identities in the common plane. No helicity has been removed. Since Q=(M,0), Q.epsilon_i=0. The previous cubic tensor becomes

```
A_h^0=0,
Avec_h=M^4/(2*sqrt(2))*sum_i a_i*delta_(h_j,h_k)*(t_i+i*h_i*N),
a_i=y_i*(1-y_i).
```

The outgoing photon-state coefficients here are **complex conjugates** of this multilinear Ward tensor, as appropriate for outgoing creation polarizations. This fixes the phases used in the projections below. A different section transforms coefficient and section inversely; it does not erase a phase or change the norms.

For all-equal helicity define S=sum a_i=1-sum y_i^2 and T=sum a_i*t_i. Then

```
Avec_(h,h,h)=M^4/(2*sqrt(2))*(T+i*h*S*N),
|T|^2=S^2-12*y1*y2*y3.
```

The last identity follows from n_i.n_j=1-2*y_k/[(1-y_i)*(1-y_j)]. For a mixed-helicity assignment there is exactly one odd leg i; only its term survives. Thus the complete pointwise norms are

```
|Avec_(+,+,+)|^2=|Avec_(-,-,-)|^2
  =M^8/4*(S^2-6*y1*y2*y3),
|Avec_(odd leg i)|^2=M^8/4*a_i^2.
```

There are two mixed assignments for each odd leg, not one. Exact checks compare these formulas with all eight original Ward tensors on two nondegenerate shapes and three scales: forty-eight tensor and forty-eight pointwise norm identities.

## 2. Angular averaging and full norm

For fixed body vectors a,b, normalized SO3 Haar measure gives

```
integral (R*a)_j^* (R*b)_l dR = delta_jl*(a^*.b)/3.
```

The checker additionally verifies the relevant second moment using the native rotation group's exact second-moment quadrature. This is a check of the Haar identity for these degree-two integrands, not a promotion of finite symmetry to all continuous spin statements.

The shape integrals are

```
<S^2>=4/15,
<y1*y2*y3>=1/60,
<a_i^2>=1/30.
```

Consequently, for each unit Cartesian source-current component, including the rotation average:

| Helicity part | Squared relative norm |
|---|---|
| all plus | M^8/72 |
| all minus | M^8/72 |
| all six mixed assignments | M^8/60 |
| total | (2/45)*M^8 |

Cross-current Gram entries vanish. Dividing the full coefficient by M^4 and multiplying by sqrt(45/2) gives a three-dimensional isometry into the full assumed three-photon relative sector. This normalizes a **relative state direction** only: it does not replace the local interaction's growing M^4 amplitude by a constant physical coupling or solve its UV problem.

## 3. Exact projection onto the earlier selected triplets

The prior code chose the all-plus coefficient profiles

```
phi_j,0=sqrt(3)*N_j,
phi_j,1=sqrt(3)*N_j*h(y),
h(y)=sqrt(60)*(sum y_i^2-1/2),
<h>=0, <h^2>=1.
```

Polarization sections are understood and retained. They are orthonormal. Only the normal component of the all-plus amplitude contributes; its in-plane vector is orthogonal under the rotation integral. With outgoing coefficient conjugation,

```
<phi_l,0, A_out^j> = -i*M^4/(4*sqrt(6))*delta_lj,
<phi_l,1, A_out^j> = +i*M^4/(12*sqrt(10))*delta_lj.
```

Their unnormalized squared weights are M^8/96 and M^8/1440. Their sum is M^8/90, exactly 1/4 of the full norm (2/45)*M^8.

For the normalized full vector profile the two coherent coefficients are

```
-i*sqrt(15)/8, +i/8.
```

The shape identity S=1/2-h/sqrt(60) proves that these two modes span the **entire all-plus normal component**, not its in-plane component or other helicities. The complete normalized partition is

| Component | Norm weight |
|---|---|
| selected old normal mode | 15/64 |
| selected added normal mode | 1/64 |
| all-plus in-plane remainder | 1/16 |
| all-minus remainder | 5/16 |
| mixed-helicity remainder | 3/8 |
| total | 1 |

The last three sum to 3/4 and remain part of the state. Throwing them away and renormalizing would change the specified local vertex. Explicitly write r_j=Ahat_j-(-i*sqrt(15)/8)*phi_j,0-(i/8)*phi_j,1. Its Gram matrix is (3/4)*I, so R_j=(2/sqrt(3))*r_j is one additional orthonormal triplet. The full candidate has coherent coordinates (-i*sqrt(15)/8, i/8, sqrt(3)/2) in these three triplet blocks. Thus a retained relative-profile completion exists without deleting any amplitude. This does not close the full local field algebra or lift the old band's mass restriction; it is a profile completion for this one current vertex.

## 4. Two-photon pseudoscalar and band-support qualification

In the transported reference frame with k1,2=(M/2)*(1,0,0,+/-1), the conjugated two-photon tensor is

```
A_out(h1,h2)=i*h1*M^2/2 if h1=h2,
             0 otherwise.
```

Its full conditional squared norm is M^4/2. The normalized scalar state is i*(|++>-|-->)/sqrt(2). Both helicity modes occur coherently; the selected old ++ and added -- scalar modes span this relative profile. This is not a source-selected singlet ensemble or a two-/three-photon branching law.

The preceding **dynamical** old channels had mass support only 0<M<4, while the added channels had unbounded support. The relative modes can be compared at any M, but that support restriction must not be silently removed. With the actual old-band support:

| Mass interval | Two-photon fraction in old/added profile range | Three-photon fraction in old/added profile range |
|---|---|---|
| 0<M<4 | 1 | 1/4 |
| M>4 | 1/2 | 1/64 |

For M>4 the old constant normal mode is unavailable; only the added h mode remains for three photons. Band endpoints have zero mass measure and do not alter this table. These are conditional subspace overlaps, **not** amplitudes generated by the old Hamiltonian, capture probabilities or photon multiplicity rates.

The actual phase-volume factors Phi2 and Phi3=M^2/(256*pi^3), the EFT coefficient dimensions, source matrix elements and incident flux must still be retained when forming unnormalized observables. The norm decomposition alone cannot select their relative strengths or justify the earlier rational mass envelope.

## 5. Next executable gate and evidence scope

The [incoming Dirac packet](INCOMING-DIRAC-PACKET.md) now retains threshold, spin transport and mass/boost measure, and evaluates its pseudoscalar/vector currents, including the coherent S-wave and possible D-wave contribution. The [outgoing Born maps](OUTGOING-BORN-MAP.md) now supply finite transition norms for the declared compact packet, retaining full profiles, separate dimensionful couplings, photon phase volumes, Bose factors and preparation dependence. The [on-shell completion audit](ON-SHELL-UNITARY-COMPLETION.md) now retains these channels in two unitary controls sharing the Born and second-order terms but not finite conversion strengths. The [packet weak-coupling audit](PACKET-WEAK-COUPLING-TAIL.md) now certifies compact errors and a finite-energy unbounded packet outside the Born domain, with completion-dependent nonanalytic strengths. Ordinary cutoff/weak limits commute; specified rescaled limits do not. The [bright-tail domain audit](BRIGHT-TAIL-DOMAIN.md) now classifies the power/log boundaries and constructs two normalized damping controls preserving the low-mass wavefunction and tail norm, without selecting a form factor or inferring a convergent all-orders series. The [complex-mass audit](COMPLEX-MASS-ANALYTICITY.md) now finds that the eta=1 scalar analytic candidate fails subthreshold open-photon contractivity, while both identity patches differ from their upper germs. Certified imaginary-mass poles map to negative s, not a general local-QFT exclusion. The [scalar dispersive response](SCALAR-DISPERSIVE-RESPONSE.md) now matches the charged-pair cut with four full-response subtractions (two after Ward factoring), retaining free s^2 and s^3 terms and a nonzero dispersive phase. It is a right-cut control, not an exact unitary or crossing-complete amplitude. The [crossed four-photon audit](CROSSED-FOUR-PHOTON.md) now supplies the leading Bose/Ward tensor and scalar cuts at +/-4. It preserves J0 parity in the photon-elastic block but gives a nonzero orthogonal-channel response, not J0-to-J2 leakage. The massive-pair-only leading response is analytic at zero, unlike the zero-phase Cayley germ. The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ. The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom; on-shell unitarity is not local dynamics. A first-order map is not a unitary scattering operator. Any identification with a native encounter and any UV form-factor selection require independent source evidence.

The checker verifies exact polynomial shape integrals, coherent projection coefficients, full-helicity tensor/norm identities, rotation second moments and scalar helicity amplitudes. The general helicity and Haar arguments are documented mathematics, not machine-formalized proofs. This construction does not make the projected algebra local or construct an interacting QFT Hamiltonian.

C1–C12, exhausted C12 effort, paused high-energy execution and historical owner warnings are unchanged. No physical outcome, spectrum, annihilation rate or branching ratio is admitted.

```sh
python -S research/scattering/low-energy/check_local_helicity_projection.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_local_helicity_projection.py
```
