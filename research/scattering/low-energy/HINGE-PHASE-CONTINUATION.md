# EF1 continuation: an exact spin lift, a finite-protocol obstruction, and explicit control costs

[EF1](EDGE-FACE-ANNIHILATION-CONJECTURE.md) · [contract](contracts/hinge-phase-continuation.v1.json) · [checker](check_hinge_phase_continuation.py) · [receipt](results/hinge-phase-continuation.v1.json)

## Result

1. **The existing fixed native protocol cannot implement the hinge by sequential composition alone.** This is an all-word result for its declared finite operation class, not a bounded search or a no-go for every retained constructor.
2. **A phase-compatible moving-face map is explicit.** Its source-convention spin lift is

   `U_plus = [[2-i,-1],[1,2+i]]/sqrt(6)`, with `U_minus=U_plus*`.

3. **A resource-explicit heralded logical implementation exists.** Three native payload gates plus an additional coherent controller implement U_plus with state-independent herald probability **3/8**. All other records remain in the complete unitary. This does not itself move the tetrahedron or supply its moving-face adapter.
4. **Capture remains underdetermined even after fixing the hinge and spin lift.** Explicit norm-preserving face mixers with the same spin transport give capture-label probabilities 0, 16/25 or 1. None is identified with photon production.

Thus the finite-symmetry-only realization of EF1 fails. A larger source construction or an explicitly new physical/control postulate is necessary. We do not choose a free coupling to manufacture a branching ratio.

## 1. Fresh source reconstruction, not a substituted spin convention

Read the current four-face native spinor store. Decode its actual projectors P_i over Q(sqrt(3),i), and form

```
K0 = stack(P_i),   J0=K0/sqrt(2),
N0=K0 K0*/2,       L=diag(P_i),   G=N=N0.
```

The checker reconstructs all 144 actual stored L/G/N entries and compares them with these formulas. It recomputes P_i*=P_i, P_i^2=P_i, K0* K0=2I, N0^2=N0 and L K0=N0 K0=K0.

The 24 quaternions and their multiplication/spin convention are taken from the actual producer declarations and arithmetic functions, not a guessed Pauli convention. Only those declaration statements and pure arithmetic functions are executed; producer entrypoints are never called. For every group element q, its actual face permutation and raw action T_q satisfy

```
T_q K0 = K0 U_q,   T_q* T_q=I8.
```

Closure is checked for all 24^2 products. The spatial Pauli actions form twelve rotations, with traces exactly {-1,0,3}. Their pointwise AB stabilizer is identity. The spin lifts of that stabilizer still include the central signs; a minus sign is not a moving hinge.

On the coherent doublet, every L/G/N stage is identity and every T_q acts by U_q. Hence **any finite word** of these stages and symmetry actions induces one of the same 24 logical operations. The required hinge has spatial trace 5/3, so neither lift is in this class, even projectively. This also rules out obtaining the target merely by choosing a different word length.

The conclusion does not cover new controlled sums, ancillary systems, changed input/output comparisons, geometric constructors or all other source branches. In particular it is not a resurrection of a shared-input/output obstruction as a universal impossibility theorem.

## 2. The compatible continuous path is computable, but not yet licensed

In the native convention

```
E1 = i sigma_z,   E2 = i sigma_y,
A=-(E1+E2),       A*= -A,   A^2=-2I.
```

A continuous lift of the positive AB hinge is

```
U(theta)=cos(theta/2) I + sin(theta/2) A/sqrt(2).
```

It begins at I and has U(2*pi)=-I. At cos(alpha)=1/3 it yields

```
U(alpha)=(2I-E1-E2)/sqrt(6),
source quaternion = (2,-1,-1,0)/sqrt(6).
```

The quaternion coordinates matter: in this producer, quaternion axes are not the naive Cartesian x,y,z assignment. The checker derives the Pauli action directly and obtains

```
R_plus = (1/3) [[1,-2,2],[2,2,1],[-2,1,2]].
```

The affine placement x -> M+R_plus(x-M), M=(1,0,0), fixes A and B and sends C to D. Its inverse reaches the ABC/reflected-apex configuration of the preceding audit.

Here theta=0 is a reference body frame, not an admissible incoming pair: two bodies at that same placement would overlap. For a genuine edge-contact start phi0 in (alpha,2*pi-alpha), the compatible relative spin transport is U(phi)U(phi0)*. The lift alone does not select a physical trajectory or starting distribution. The finite-symmetry edge-stabilizer obstruction persists in a rotated body frame by conjugation.

If continuous control is admitted, a Hermitian generator is

```
H(t)=hbar * theta_dot(t) * (sigma_y+sigma_z)/(2*sqrt(2)).
```

This identifies a sufficient Hamiltonian, not one derived from the native fixed protocol. Geometry fixes the axis and endpoint angle, not theta_dot, dwell time, energy scale or capture coupling. A continuum of possible states is not automatic operational availability of every unitary between them.

For the material face labels, put

```
P_i(theta)=U(theta) P_i U(theta)*,
J_theta=stack(P_i(theta))/sqrt(2),
V_theta=diag(U(theta),U(theta),U(theta),U(theta)).
```

Then the exact joint phase/moving-frame identity is

```
J_theta U(theta)=V_theta J0,
J_theta* J_theta=I,
V_theta N0 V_theta*=N_theta.
```

This transports one native spinor with one moving tetrahedron; it does not construct an incoming electron–positron pair or a charge-conjugation identification. The endpoint identities are checked against the actual stored projectors; the all-theta identities follow algebraically by conjugation. N_alpha differs from N0. Implementing the logical U in the fixed encoding is therefore **not** already implementing the moving-face comparison or spatial hinge. This extra operation remains visible.

## 3. A complete conditional controller, without discarded failures

An explicit sufficient additional resource is a three-level coherent controller. Prepare its zero state with the real orthogonal matrix

```
P = [[1/sqrt(2),  1/sqrt(2),  0],
     [1/2,       -1/2,        1/sqrt(2)],
     [1/2,       -1/2,       -1/sqrt(2)]].
```

Select the native logical payloads `I,-E1,-E2` on its three states and unprepare. The full six-dimensional unitary is

```
W=(P* tensor I) diag(I,-E1,-E2) (P tensor I).
```

Its three output-controller blocks on an initially zero controller are

```
B0=(2I-E1-E2)/4,         B0*B0=(3/8)I,
B1=(2I+E1+E2)/4,         B1*B1=(3/8)I,
B2=(E2-E1)/(2sqrt(2)),   B2*B2=(1/4)I.
```

The checker verifies the whole unitary and all three effects, not just B0. Herald zero produces exactly U_plus on every logical input; herald one produces U_minus, not the chosen U_plus. The controller can remain coherent and W* reverses the entire operation. Measuring a flag does not make its other outcomes disappear.

PREP, coherent controlled-SELECT and flag readout are additional capabilities. Native payload matrices alone do not authorize their controlled implementation. The checker also constructs the full **24-dimensional raw/controller unitary** by replacing the three logical payloads with their actual eight-coordinate T_q actions. It verifies its unitarity on all raw inputs and its intertwining with W through `I3 tensor K0`. The native rejected complement is therefore not discarded. This lift still requires the controller. The moving-face adapter and actual spatial motion are further obligations.

**3/8 is a herald probability for this supplied control algorithm, not a capture rate, a three-photon probability or an annihilation branching ratio.** No event-count interpretation is assigned to these controller dimensions.

## 4. Even compatible unitary transport does not fix capture

At a designated face-contact stage, append a retained release/capture-label mixer

```
C(t)=[[a,-b],[b,a]],
a=(1-t^2)/(1+t^2),  b=2t/(1+t^2).
```

It is unitary, retains both records and commutes with the spin action on a separate factor. The same spatial/spin endpoint admits t=0,1/2,1 with capture-label probabilities 0,16/25,1. These are countermodels to inferring a probability from the hinge and covariance alone, not source-generated capture models or photon factorizations.

The task is now concrete: **license or derive the extra controller/moving-face operation, and independently specify the contact conversion operator.** A source rule might select or exclude these extensions. Without one, selecting a mixer or angular tolerance because it fits a desired ratio would replace explanation with calibration.

## Verification boundary

The exact finite-field calculation checks source reconstruction, finite closure/intertwiners, the source-convention spin lift, moving-frame identities, a complete controller and the distinct unitary mixer examples. The all-word induction and continuous-path interpretation are documented mathematics, not machine-formalized proofs. Source owner stores and receipts are not overwritten. Their current producer hash comparison is reported separately; a stored passing receipt is not promoted to all-ancestor freshness.

EF1 remains proposed and untested physically. C1–C12, budgets and paused high-energy execution are unchanged.

```sh
python -S research/scattering/low-energy/check_hinge_phase_continuation.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_hinge_phase_continuation.py
```
