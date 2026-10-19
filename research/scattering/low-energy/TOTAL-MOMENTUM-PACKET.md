# Full total-momentum photon packet with retained helicity transport

[Contract](contracts/total-momentum-packet.v1.json) · [checker](check_total_momentum_packet.py) · [receipt](results/total-momentum-packet.v1.json)

## Result and scope

The earlier relative/energy profiles now lift by an explicit isometry into **normalizable full two-/three-photon Bose-Fock states**, using the imported massless-helicity theory. All eight orthogonal modes from the [energy-tail construction](PHOTON-ENERGY-TAIL.md) are retained: two scalar helicity modes and two copies of the three-component vector profile. Mass, boost and relative phases are not traced out.

The general coefficient carrier supports an induced Lorentz representation and the photon embedding intertwines it. This is a new imported carrier, **not a Lorentz action derived on the native charged source**. Nor is it yet a lab-time intertwiner for the preceding rest-frame escape Hamiltonian.

## 1. Fock measure and timelike coarea

Fix the convention

```
dPi(p)=d^3p/[(2*pi)^3*2*|p|],
||Psi_n||^2=(1/n!)*sum_helicities integral product_i dPi(p_i)*|Psi_n|^2,
dPhi_n(P)=(2*pi)^4*delta^4(P-sum p_i)*product_i dPi(p_i).
```

Thus the ordered product disintegrates as d^4P*dPhi_n(P)/(2*pi)^4. The geometric phase volumes are the preceding ordered Phi2=1/(8*pi) and Phi3=M^2/(256*pi^3). Identical-particle factors remain explicit in the Fock norm, not silently canceled across sectors.

Except for measure-zero collinear configurations, P is future timelike. Write

```
P=M*u, M>0, u.u=1, u0>0,
u0=(1+q^2)/(1-q^2), uvec=2*q/(1-q^2), |q|<1.
```

The inverse is M=sqrt(P.P), q=uvec/(1+u0). Direct differentiation gives

```
d^4P=M^3*dM*dmu(u),
dmu(u)=d^3uvec/u0=8*d^3q/(1-q^2)^3.
```

The mass power is **three**, not zero. A CM delta at spatial P=0 is not an L2 Fock packet.

## 2. Isometry and explicit normalized example

Let chi_alpha(M) be the eight rest-frame normalized relative modes, with delta_alpha_beta Gram matrix under normalized conditional phase measure including helicities. Orthogonality of the added helicity/shape profiles was checked in the tail construction. Let B(u) be the rotationless boost sending (1,0,0,0) to u. Transport each profile by the standard photon helicity representation, giving chi_alpha(M,u) in the fiber at P=M*u; Lorentz invariance of dPhi and unit-modulus helicity transport preserve the conditional Gram matrix.

For coefficient functions f_alpha(M,u), with norm sum_alpha integral dM*dmu(u)*|f_alpha|^2, define

```
(J f)_n(p_i,lambda_i)
 =(2*pi)^2*sqrt(n!)/sqrt[M^3*Phi_n(M)]
  *sum_(alpha in sector n) f_alpha(M,u)*chi_alpha(M,u;relative).
```

Permutation symmetry is retained because each chi is Bose symmetric and M,u depend only on total momentum. Substitution into the full norm cancels (2*pi)^4, n!, Phi_n and M^3 exactly, leaving ||J f||^2=||f||^2. The construction retains coherent superpositions, including interference between old and added orthogonal profiles in other readout bases. It is an isometry onto a selected subspace, not a claim that eight profiles span photon Fock space.

Old band-channel energy amplitudes can be zero-extended beyond M=4 and lifted without changing their norms. The general construction accepts arbitrary square-integrable mass/velocity coefficients; it does not substitute a guessed amplitude for the previously unspecified outgoing scattering amplitude.

An explicit example in either added output sector uses

```
a(M)=sqrt(30)*M/(1+M)^3,
b(q)=(1-q^2)^(3/2)*indicator[-1/4,1/4]^3(q),
f_alpha(M,u(q))=z_alpha*a(M)*b(q), sum |z_alpha|^2=1.
```

The cube lies strictly inside |q|<1. The earlier beta integral gives integral |a|^2 dM=1. Also dmu*|b|^2=8*d^3q on a cube of volume 1/8, so the boost norm is exactly one. Both envelopes are declared choices, not incident-preparation or native-scale predictions.

The factorized fixed-b subspace is not closed under general boosts. The **full** f(M,u) carrier is needed for a Lorentz representation; transforming a packet transforms its envelope too. This cube happens to be invariant under the native tetrahedral spatial rotations, which are signed coordinate permutations, but is not invariant under arbitrary rotations.

Omitting the mass half-density M^(-3/2) is not harmless: for this a, the would-be norm contains integral M^3*|a(M)|^2 dM, which diverges logarithmically. Energy-fiber normalization alone did not give a Fock packet.

## 3. Helicity transport and induced Lorentz action

The canonical boost has B00=u0, B0i=Bi0=ui, Bij=delta_ij+ui*uj/(1+u0). For a null momentum k and transverse radiation-gauge polarization epsilon=(0,e), apply a proper orthochronous Lorentz matrix L, then restore radiation gauge:

```
k'=L*k,
epsilon'=L*epsilon-[(L*epsilon)^0/k'^0]*k'.
```

The result has zero time component, k'.epsilon'=0, unit Hermitian transverse norm and unchanged helicity. Relative to a chosen normalized helicity frame at k', it differs by a unit phase zeta. Products of these phases transport n-photon wavefunctions. Changing section changes the phases covariantly; it is not permissible to discard them. Gauge-restored transport composes exactly, since the removed terms are multiples of the null momentum.

The checker uses noncollinear boosts and both helicities, verifies this projection and composition, and compares to a minimal spatial-rotation frame to verify |zeta|=1. One noncollinear witness has zeta=(2303-96*i)/2305, explicitly not one. This is a target-photon calculation, not a native operation implementing gauge transport.

For general L set

```
W(L,u)=B(L*u)^(-1)*L*B(u).
```

It fixes the rest time axis and is an SO(3) rotation. Its cocycle is W(L2*L1,u)=W(L2,L1*u)*W(L1,u). The two scalar modes carry D0=1, and each triplet carries D1(W). On the full coefficient carrier,

```
(T(L)f)(M,u)=D[W(L,L^(-1)*u)]*f(M,L^(-1)*u).
```

Invariance of dmu and unitarity of D make T unitary. The already constructed continuous relative scalar/vector profiles imply U_photon(L)*J=J*T(L), with the helicity gauge phases retained. This analytic induced-representation argument does **not** identify the original finite native triplet with physical total spin one; it starts from the explicitly imported photon profiles and their coefficient carrier.

## 4. Lab translations are a distinct remaining gate

On this photon carrier the total four-momentum is multiplication by M*u, so

```
H_lab=M*u0, Pvec=M*uvec, invariant_mass=M.
```

For M=1, q=(1/8,0,0), u0=65/63. Hence lab photon energy is 65/63, not one. The packet map intertwines these free multiplication observables with the actual summed photon four-momentum, but **does not** intertwine the earlier rest Hamiltonian's parameter t with lab time merely by appending b(u).

A source model with actual boosts, commuting conserved total four-momentum and a correctly lifted escape wave operator still needs construction. Native source licensing, physical electron/positron preparation, contact locality, envelope selection, calibration and detector probabilities are separate obligations. No emission rate or branching law follows from this norm isometry.

## 5. Verification and next executable gate

Exact checks cover twelve mass/boost Jacobians, twenty-four boosted on-shell output configurations, nontrivial Wigner rotations and their cocycle, six helicity/gauge transports, and all twenty-four native rotation actions on the boost envelope. Norm factors and the logarithmically divergent omitted-half-density control are checked algebraically. The full coarea/isometry and induced-representation arguments are documented mathematics, not machine-formalized proofs or a numerical packet simulation.

The [covariant escape lift](COVARIANT-ESCAPE-LIFT.md) now constructs that active completion using the additional postulate P^mu=u^mu*H_rest, with correct lab wave operators and retained bound/spectator records. It distinguishes bound invariant mass from continuous lab energy and fixed-origin time from co-moving proper time. Next test local source/operator support and cluster assumptions rather than promoting Poincare covariance to native field dynamics. Expose any additional source/Poincare postulate rather than calling a target Fock packet a native interaction. Physical source binding remains required even if that conditional lift succeeds.

C1–C12, exhausted C12 effort, paused high-energy execution and owner/hash warnings remain unchanged. No physical outcome has been admitted.

```sh
python -S research/scattering/low-energy/check_total_momentum_packet.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_total_momentum_packet.py
```
