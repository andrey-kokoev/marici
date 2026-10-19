# Unbounded photon-energy tail: cutoff bound weight is not robust

[Contract](contracts/photon-energy-tail.v1.json) · [checker](check_photon_energy_tail.py) · [receipt](results/photon-energy-tail.v1.json)

## Result

The [Jacobi completion](CONTACT-ESCAPE-CONTINUUM.md) admits an arbitrarily small, positive-energy, symmetry-compatible unbounded tail that removes its accessible point sector. The triplet's retained norm 1/sqrt(5) and local pair plateau 1/5 are therefore **not robust under opening additional continuum support**. For every nonzero tail in the declared positive regime, local pair survival tends to zero and the active initial norm has a complete free outgoing asymptote.

Finite-time evolution nevertheless differs in operator norm by at most |delta*t|. Small-tail and long-time limits do not commute. This is a conditional spectral result, not a physical capture refutation or an annihilation rate.

## 1. Photon phase-volume normalization, not a fitted rate

The preceding relative-photon construction uses normalized profiles psi_n(E;relative) at timelike CM momentum (E,0), E>0. In its ordered-particle convention the integrated phase volumes are

```
Phi2(E)=1/(8*pi),
Phi3(E)=E^2/(256*pi^3).
```

Write them as A_n*E^(2n-4), keeping A_n explicit. If identical-particle factorials are included in the unnormalized measure, they remain in A_n and in the amplitude below. They cannot be discarded when comparing unnormalized rates.

Choose the added, dimensionless-unit envelope

```
w(E)=30*E^2/(1+E)^6, E>0,
f_n(E)=sqrt(30/A_n)*E^(3-n)/(1+E)^3.
```

Then |f_n(E)|^2*Phi_n(E)=w(E), for both n=2 and n=3. Thus each energy-profile vector f_n*psi_n has norm one in the declared direct integral dE*dPhi_n(E), with no lost phase-volume factor. This is an explicit measure-compatible amplitude, **not** a source-derived one. The scale in 1+E is an uncalibrated model unit, not a measured cutoff or native length.

Exact beta integrals give

```
integral w(E) dE=1,
integral w(E)/E dE=3/2,
integral E*w(E) dE=3/2,
integral E^2*w(E) dE=6.
```

A constant bare amplitude instead has divergent norm under both phase volumes: integral dE for two photons and integral E^2 dE for three. It therefore does not define this bounded rank-one source vertex. This is **not** a no-go for every singular/renormalized self-adjoint interaction; such an alternative needs its own domain, counterterms and source assumptions.

## 2. Do not duplicate physical output modes

The old band and new tail channels must be orthogonal even where their energy supports overlap.

- Choose the old two-photon scalar in equal ++ helicity and the added scalar in equal -- helicity. They are orthogonal, both have total J=0 in the imported photon theory, and retain the same C sign.
- For three photons keep the old equal-helicity triplet psi_j=sqrt(3)*N_j*section. Multiply it for the added channel by

```
h(y)=sqrt(60)*(sum_i y_i^2-1/2).
```

Under the preceding normalized uniform shape measure 2*dy1*dy2, integral h=0 and integral |h|^2=1. The N_j rotation integral factors from the shape integral. Hence old and added triplets are orthogonal and both have identity Gram matrices. The multiplier is permutation-symmetric and rotation-invariant, preserving the earlier odd section cocycle, C and native rotation action. All phases remain in the state; no coherence is erased by treating these orthogonal profiles as channel coordinates.

This gives a genuine direct-sum embedding into the assumed relative photon sectors rather than counting the same photon state twice. It still does not license the source CAR/C postulates or bind them to an actual incident pair.

## 3. Unbounded, self-adjoint Hamiltonian

For each source component use source a, old band lead b, and new energy wavefunction c(E). Keep the old source energy epsilon=3 and band coupling g_s^2=1/4 or g_t^2=2. Add

```
H_delta = H_band direct_sum M_E
          +delta*(|source><v|+|v><source|),
(M_E c)(E)=E*c(E),
v(E)=sqrt(w(E)).
```

The added scalar coupling is the same on each of the three triplet components. In four-channel notation the coupling map is delta times an isometry, so its operator norm is |delta|, not sqrt(4)*|delta|. Charge, C, fermion parity and native rotations are inherited. The old bands, all tail profiles, twelve typed fermion spectators and sixty raw-complement records are retained.

M_E is unbounded self-adjoint on its standard multiplication domain. The new interaction is bounded finite rank, so H_delta is self-adjoint on the unchanged free domain. Completing the energy square in quadratic-form sense adds

```
||sqrt(E)*(c+delta*a*v/E)||^2
```

and subtracts delta^2*|a|^2*integral w/E. Together with the preceding band square, positivity follows from

```
epsilon-g^2-(3/2)*delta^2>0.
```

Here v/E belongs to L2 as well, so the displayed expression has no hidden infrared-domain divergence. For triplet coupling g^2=2 the allowed strict range is 0<delta^2<2/3. Singlet positivity is weaker. Checked examples delta=1/4 and 1/8 have triplet margins 29/32 and 125/128. These are test parameters, not inferred strengths. The bare source still is not a sharp energy eigenstate: Var_H(e0)=g^2+delta^2.

## 4. Why the cutoff bound state disappears

Let S(z)=integral w(E)/(E-z) dE. The source resolvent is

```
G_delta(z)=1/[3-z-g^2*m(z)-delta^2*S(z)].
```

For every E>0, Im S(E+i0)=pi*w(E)>0. Therefore a nonzero tail removes any real positive source pole, including the old E_b=2+sqrt(5)>4. Equivalently an eigenvector with source amplitude a!=0 would require c(E) proportional to v(E)/(E-E_b), which is not square integrable because v(E_b)!=0. If a=0, the free outputs themselves have no point eigenvectors. Positivity excludes negative levels and the strict threshold margin excludes a zero level.

For completeness the tail transform has an explicit boundary description. Put a=1+z and

```
I_n(a)=-[log(1-a)+sum_(k=1)^n a^k/k]/a^(n+1),
S(z)=30*[I_3(a)-2*I_4(a)+I_5(a)].
```

The removable a=0 value is understood by its integral. On the upper positive cut log(-E-i0)=log(E)-i*pi, yielding precisely the stated positive density; at E=1 its real part is -1/2. These rational/log boundary values are continuous locally on E>0, including the old band endpoint once the tail is present, with a nonvanishing imaginary denominator. At zero the denominator has the positive form margin. Stieltjes inversion excludes singular-continuous source measure as well as point masses.

The reducing subspace generated by the source is thus purely ac. Its orthogonal complement is an uncoupled combination of the original free continua, also ac; it is not a missing dark point sector. Finite-rank trace-class scattering theory then gives complete free outgoing asymptotes with full active norm. In particular local source amplitude tends to zero. No complex resonance location or exponential decay rate is asserted without a separate calculation.

This outgoing statement concerns the declared energy-channel model. Physical spatial photon escape from a localized encounter still needs a full total-momentum packet and a spatial source binding.

## 5. Small finite-time error does not protect late retention

Compare H_delta to H_0 on the **same** Hilbert space, retaining the decoupled tail at delta=0. On this enlarged space the old bound eigenvalue is embedded in a decoupled continuum at delta=0, not isolated above the full essential spectrum. Bounded-perturbation Duhamel gives

```
||U_delta(t)-U_0(t)|| <= min(2,|delta*t|),
|P_pair_delta(t)-P_pair_0(t)| <= min(1,2*|delta*t|).
```

For an initially triplet contact state,

```
lim_(t->infinity) P_pair_0(t)=1/5,
lim_(t->infinity) P_pair_delta(t)=0 for every delta>0 in the positive regime.
```

Hence lim_delta->0 lim_t->infinity is zero, while the reversed limits give 1/5. The asymptotic survival difference remains 1/5 even as the perturbation norm tends to zero. Finite-time error bounds are not uniform-in-time stability certificates for point-projector weights.

For an initial encoded pair with singlet weight p, eventual outgoing two-/three-sector norms in this restricted opened model are p and 1-p. Neither p nor the form factors nor delta is source-selected. The division of outgoing norm between old and new orthogonal profiles requires its spectral amplitudes; it is not inferred from the disappearance of a bound state. No ratio or lifetime is calibrated.

## 6. Verification and next gate

The checker verifies exact beta moments, the orthogonal Bose shape multiplier, phase-volume powers, tail boundary imaginary coefficients, positive margins, native symmetry, and scoped hostile controls. Self-adjointness, absence of singular spectra, local source decay and complete wave operators are analytic arguments using the stated theorems, not machine-formalized or deduced from a finite discretization.

The [total-momentum construction](TOTAL-MOMENTUM-PACKET.md) now supplies a normalizable full Bose-Fock packet and an eight-mode coarea isometry, retaining mass/boost measure and helicity transport. Its imported Lorentz coefficient carrier is not the native source, and CM mass is not lab energy. The [covariant lift](COVARIANT-ESCAPE-LIFT.md) now supplies active conserved four-momentum and lab wave operators under additional velocity/mass postulates. Next audit local source/cluster support; covariance does not establish microcausality. Independently bind the incident source, the envelope/scale, coupling strengths, thresholds and physical propagation. The present continuum family demonstrates nonuniqueness and cutoff sensitivity; it does not supply those native principles.

C1–C12 and exhausted C12 effort are unchanged; high-energy execution remains paused. Owner/hash warnings remain intact. No physical outcome, capture probability, annihilation rate or branching ratio is admitted.

```sh
python -S research/scattering/low-energy/check_photon_energy_tail.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_photon_energy_tail.py
```
