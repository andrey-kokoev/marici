# EF1-B: one retained centre-of-momentum completion for two and three outputs

[Contract](contracts/cm-separation-map.v1.json) · [checker](check_cm_separation_map.py) · [receipt](results/cm-separation-map.v1.json)

## Constructed result and changed hypothesis

There is now an explicit **classical momentum assignment/separation-map candidate** that takes geometric null seeds to positive-energy massless momenta summing to the incoming CM four-momentum. It uses one rule for either number of outputs, no channel-specific angular correction, and no fitted branching parameter.

This is a **new postulate EF1-B**, not a reversal of the [EF1-N refutation](NORMAL-DIRECTION-CONTACT-TEST.md). The change is explicit:

- EF1-N identified triangle normals directly with final photon directions and failed for generic edge release.
- EF1-B treats those normals as **auxiliary pre-emission data** and applies a specified momentum-space completion before interpreting final directions.

This is not a coordinate boost of the failed physical process: the incoming pair's CM frame stays fixed. Only the interpretation of the geometric seeds changes. If the seeds were already physical emitted photons, the boost/dilation would change their total momentum and require a dynamical energy/momentum source. That is not the claim here.

The construction does not yet give physical motion of triangles, a normalized photon wavepacket, a quantum isometry, a source-native operation or a contact amplitude.

## 1. A single formula

Use metric signature +--- and c=1. For each nondegenerate triangle supply its oriented normal direction n_i and a positive seed weight w_i. The examples freeze the ordered vertex tuples ACE/BDF and ADe/BDe/CDe. Relabelling must transport their orientation; re-sorting vertices or flipping normals to fit an observed direction would change the input hypothesis. The physical orientation/helicity/readout correspondence remains unproved. The baseline assigns weights proportional to its area; the same common scale is irrelevant. Define auxiliary null vectors

```
k_i=w_i(1,n_i),   |n_i|=1,
K=sum_i k_i=(A,q),   s=sqrt(A^2-|q|^2)>0.
```

Let B(K) be the rotation-free proper orthochronous boost taking K to (s,0):

```
B00=A/s,
B0j=Bj0=-q_j/s,
Bij=delta_ij+q_i*q_j/[s*(A+s)].
```

Given independently supplied incoming CM energy M>0, assign

```
p_i=(M/s) B(K) k_i.
```

Then every p_i is future null and

```
sum_i p_i=(M,0,0,0).
```

The general argument uses Lorentz invariance and positive common scaling. The checker verifies the Minkowski matrix identity, determinant +1, positive energies, nullness and total momentum exactly in the source examples. It additionally checks all twelve native projected rotations, all output permutations and common seed rescaling. The algebra gives ordinary spatial rotation covariance generally; it is not a derivation of physical Lorentz symmetry from the seed.

A single ray or a set of wholly parallel future rays has null total K and is outside the domain. It cannot complete to a massive incoming pair by this operation. Thus the procedure does not create an isolated one-photon channel by fiat.

## 2. Retention makes the momentum map invertible

The completed momenta alone forget the auxiliary total-motion frame and common seed scale. Retain K and lambda=M/s (or the equivalent inverse boost and scale), alongside the original geometry/parent records. Then

```
k_i=lambda^(-1) B(K)^(-1) p_i.
```

Exact inverse reconstruction is checked. Common seed rescaling leaves final p_i unchanged, so dropping the scale record would genuinely lose information.

This is a statement about classical kinematic data. It is not permission to copy an unknown quantum state or to declare a nonlinear, state-dependent momentum normalization a unitary quantum operation. A quantum construction would need independently specified orthogonal control/record structure, measures, amplitudes and normalizable outgoing states. Sharp rays here are kinematic points, not normalized photon wavepackets.

## 3. Two outputs: the previously obstructed example becomes a definite new prediction

For two nonparallel positive seeds the total is timelike, so the formula always gives back-to-back momenta of energy M/2. For equal-area seeds their final axis is the normalized difference of the original normal directions.

Apply the rule to the actual ACE/BDF triangles at the preceding r=2 witness. Their seed normals are orthogonal and have equal areas. In units M=1 the exact completed momenta are

```
p_ACE=(1/2,-1/6,-1/3,1/3),
p_BDF=(1/2, 1/6, 1/3,-1/3).
```

The predicted oriented axis is (-1,-2,2)/3. This entails substantial reorientation from the old normal directions; it does not evade the preceding narrow-cone exclusion. Deriving a physical process that performs the assignment remains necessary.

For the full original equal-area hinge template, the preceding parameter r gives final first direction

```
-sign(r)*(1,r,-r)/sqrt(1+2*r^2),   r!=0,
```

with the opposite direction for the other output. Both are perpendicular to the AB hinge axis. The checker verifies the equal squared-area polynomials and the normal-difference polynomial for the whole rational hinge family. The axis formula follows from those identities, not from a separately fitted emission angle. The existing prototype two-triangle extraction and its source/phase authorization remain conjectural.

## 4. Three outputs: balanced geometry is a fixed shape, unequal weights expose a missing input

For the symmetric face-sharing ADe/BDe/CDe construction with baseline equal-area weights, K has zero spatial part already. The map retains the 120-degree directions and gives energies M/3. It does not magically produce an unequal spectrum from unchanged symmetric input.

For a controlled sensitivity test, allow positive weights w1,w2,w3 on those same three directions. Writing

```
S=w1*w2+w1*w3+w2*w3,
E_i/M=w_i*(w_j+w_k)/(2*S),   {i,j,k}={1,2,3},
```

gives the completed energies. The checker constructs an exact unequal example:

```
(w1,w2,w3)=(1,2,1/3)
=> (E1,E2,E3)/M=(7/18,4/9,1/6).
```

Every interior massless three-body energy shape, 0<E_i/M<1/2 with sum one, is represented by positive weight ratios. Indeed, set e_i=E_i/M and take

```
w_i proportional to 1/(1-2*e_i).
```

Substitution recovers the shape. This follows equivalently from pairwise invariants

```
2*p_i.p_j/M^2 = w_i*w_j/S = 1-2*e_k.
```

This is a parameterization of allowed energy shapes, **not a predicted distribution**. The inverse would let one fit any interior energy shape. Using it on observations and calling the resulting weights a derivation would be circular. The baseline symmetric geometry still selects equal weights; any different preparation/phase weights must be independently supplied or derived before testing an unequal spectrum. No Lorentz-invariant phase-space density or Jacobian-weighted emission probability has been derived here.

## 5. Relative quantum continuation now constructed

The [relative-measure continuation](RELATIVE-PHOTON-MEASURE.md) now derives the weight-ratio/Dalitz Jacobian and an explicit half-density coordinate unitary, with normalized Bose-symmetric relative profiles and a phase-sensitive interference test. These are conditional fixed-total-momentum states in an imported photon framework, not full Fock wavepackets or a native-input emission isometry. Distinct normalized profiles give different energy variances, so the measure still does not select the physical spectrum.

## 6. What this does and does not settle

We have constructed a concrete, retained, momentum-conserving **kinematic map**, rather than leaving output directions entirely unspecified. Its choice is still additional physics: proper rest boosting and dilation do not make it uniquely mandated by the native source. A different proposed separation map must be judged by independent source justification and held-out consequences, not just by conservation.

To turn EF1-B into an interaction theory, derive or explicitly postulate and test:

1. the source operation implementing separation and its compatibility with retained phase/geometry;
2. a quantum output embedding with the correct symmetrized photon spaces, normalizable profiles and measure;
3. independently selected seed weights or preparation dependence;
4. the contact generator and amplitudes selecting two versus three outputs.

The map neither chooses photon multiplicity nor supplies a branching ratio. In particular the earlier 3/8 controller herald probability and the working 372 ratio play no role.

The owner receipts, EF1-N's scoped rejection, C1–C12, exhausted C12 budget and paused high-energy execution are preserved. Finite-field checks support the displayed examples; the general kinematic and shape arguments are documented mathematics, not machine-formalized proofs or independent physical evidence.

```sh
python -S research/scattering/low-energy/check_cm_separation_map.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_cm_separation_map.py
```
