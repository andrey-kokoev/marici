# Neutron local-input loss: a comparison-selected joint successor

Research continuation of the attached `neutron_local_input_loss_and_branch_accounting.md`.

## Result and status

Two conditional successor constructions were implemented and tested. The first converts every component outside the surviving common neutron mode into a chosen two-spinor product. It is norm preserving, but its principle would also treat a symmetric loss in all three sectors as production. It does not satisfy the stricter requirement that sector disagreement select the product branch.

The second uses one fixed linear routing for every local-input fault. It compares both the retained state and the information that must be retained to complete the lossy operation. Common components stay in a neutron-plus-memory sector; contrasting components enter a chosen proton-candidate times two-spinor sector. The latter also retains a two-valued history label. This construction is norm preserving, covariant under the retained threefold action, and gives zero product output for equal losses in all sectors.

The history label has a precise role: the two contrast records span four independent directions across the 36 source faults, while the chosen spinor pair has only two directions with the required nontrivial threefold transformation. A fixed covariant isometry into the pair alone cannot preserve all those records. Two copies of its contrast image, distinguished by one two-valued label, suffice. The label need not be an additional particle; a physical interpretation could use existing outgoing orbital, baryon, or other record degrees of freedom. None is identified here.

This is an explicitly constructed candidate, **not a source-derived beta-decay law**. The retrieved native production grammar has not been modified. Product identities, the fate of mismatch records, physical coupling, energy/momentum, and escape remain unselected. A repair-only rival passes the same norm and covariance conditions.

## What is reused, and what is new

The attached preceding audit supplies source-formula reconstruction of the 36-coordinate neutron, three sectors, twelve coordinates per sector, and all 36 whole-input-column losses. Its limitations remain: the sector-wide protocol is a specified implementation, the five-slot binding is conditional, and the unavailable generated full-five receipt was not independently replayed.

On the selected three-mode space, use

```
a = (1,1,1)/sqrt(3)
Q = [(1,-1,0)/sqrt(2), (1,1,-2)/sqrt(6)]
aa† + QQ† = I3.
```

For the loss of input weight r in sector s,

```
T_s = I3 - r |s><s|
d = sqrt(r(2-r)).
```

The missing-norm record has amplitude `d <s|x`. It is an independent output of an isometric completion on the selected input space, not a spinor or emitted particle by itself. The general completion method is standard; its physical implementation is not supplied by the mathematical theorem. See P. L. Robinson, *Julia operators and Halmos dilations*, arXiv:1803.09329.

The new construction adds a declared linear rule assigning common records to survival/repair and contrasting records to a product sector. It also declares a fixed proton-candidate output and a two-spinor pair map. These additions must not be retroactively described as native grammar operations.

## 1. Initial completion: sufficient for norm, not for a contrast trigger

Let the surviving-neutron amplitude be `S_s x = a† T_s x`. The remaining three amplitudes can be retained by

```
H_s x = (Q†T_s x, d<s|x),
S_s† S_s + H_s† H_s = I3.
```

For `0<r<1`, H_s has rank three. Its determinant is `d/sqrt(3)`; the complementary effect `H_s†H_s` has eigenvalues `1,1,r(2-r)/3`.

Choose a pair isometry J from these three amplitudes into two logical spinors. A normalized proton-candidate p0 may be attached as a fixed factor. The complete output is then

```
(S_s x)|n>  direct-sum  |p0> tensor (J H_s x).
```

This is a mathematically valid joint-product sector, not three independent particle amplitudes. It has mutually exclusive survival and product branches. The chosen labels and fixed proton factor are construction inputs, not deductions.

On the coherent input a, the product squared norm is

```
q_first(r) = 1-(1-r/3)^2 = (6r-r^2)/9.
```

For the inherited source weights this lies between 0.0054922522 and 0.1448389839. It is conditional on a supplied input-loss event, not a failure frequency or physical neutron rate.

### Spin selection remains free

The source's native order-three electron action V and source-aligned frame W were reconstructed exactly from `check_neutron_contrast_electron_transport.py`. On its contrast plane the threefold action has eigenvalues omega and omega squared. Reuse the earlier candidate B that maps these two contrast eigenvectors to same-eigenvector spinor products. It obeys

```
B†B = I2,
(V tensor V) B = B R_C3.
```

The orthogonal complement of B's image is two-dimensional and invariant under the same threefold action. It contains the pair singlet and the symmetric opposite-spin state, called `triplet_0` in this chosen spin frame. Therefore

```
j_record = cos(theta) singlet + exp(i phi) sin(theta) triplet_0
J = [B, j_record]
```

gives a family of isometries with the same norm and threefold covariance. The complete complex space of threefold intertwiners from contrast-plus-scalar to the pair has dimension four before imposing isometry.

The conditional singlet fraction on the outgoing branch is

```
F_singlet = [3(2-r)/(6-r)] cos(theta)^2.
```

The record can therefore produce a mostly singlet state or an entirely triplet state without changing the neutron-survival amplitude or the total pair weight. This is a direct counterexample to selecting physical pair content from norm and this symmetry alone.

### Rejected universal interpretation

If equal input losses occur in every sector, the retained state is `(1-r)a`: it has no sector contrast. Nonetheless its missing norm is `2r-r^2`. A general policy that emits every missing-norm record would produce an outgoing branch even here. To preserve the intended disagreement trigger, it must retain symmetric missing-norm information as repair memory instead.

This is an extra requirement being tested, not an established fact that all symmetric physical faults are harmless.

## 2. Fixed comparison-selected construction

Allow loss parameters r_0,r_1,r_2 in [0,1] and define

```
T = diag(1-r_0, 1-r_1, 1-r_2)
D = diag(sqrt(r_0(2-r_0)), sqrt(r_1(2-r_1)), sqrt(r_2(2-r_2)))
T†T + D†D = I3.
```

The completed local output is `(Tx,Dx)`. Retaining the location of the missing input gives three completion-record coordinates, rather than selecting a different anonymous scalar port separately for each sector. These coordinates transform by the same threefold permutation as the retained field. No stochastic law on the loss parameters is assumed.

Use one fixed routing, independent of r_s and of the failed coordinate:

```
N(x) = |n> tensor [ (a†Tx)|0>_m + (a†Dx)|1>_m ]

P(x) = |p0> tensor [ BQ†Tx tensor |0>_h
                    + BQ†Dx tensor |1>_h ].
```

Here the two factors encoded by B are logical electron and neutral-partner candidates. The labels m and h distinguish retained-data and completion-record amplitudes. On the product side, h is a two-valued history degree of freedom, not a newly claimed emitted particle. The state spaces are

```
(H_N tensor C2_memory)
  direct-sum
(span(p0) tensor C2_E tensor C2_R tensor C2_history).
```

The 10-by-6 routing from completed local data is an isometry. Composing it with the 6-by-3 local completion gives a 10-by-3 isometry. Its norm identity follows directly:

```
||N(x)||^2 + ||P(x)||^2
 = ||aa†Tx||^2 + ||QQ†Tx||^2
   + ||aa†Dx||^2 + ||QQ†Dx||^2
 = ||Tx||^2 + ||Dx||^2
 = ||x||^2.
```

There is no surviving neutron occupation in the declared product sector. This is a state-space declaration of a replacement branch; it does not implement the native additive occupancy generator's missing retirement operation.

## 3. Why the additional history label cannot simply be dropped

For initial state a, a single-sector event produces the contrast record

```
z_(s,r) = ( -r Q†e_s, sqrt(r(2-r)) Q†e_s ) / sqrt(3).
```

The 36 source events span four dimensions. An exact witness takes sectors 0,1 and two unequal source weights r_1,r_2. Writing d_i=sqrt(r_i(2-r_i)), the four-column determinant is

```
(r_1 d_2 - r_2 d_1)^2 / 27.
```

It is nonzero for distinct weights in (0,1), since `d/r=sqrt(2/r-1)` is strictly decreasing.

Under the threefold group, these four amplitudes contain two copies each of the omega and omega-squared characters. A single pair with action V tensor V contains only one copy of each, together with two invariant directions. Any equivariant linear map from the four contrast amplitudes to that pair must therefore have rank at most two. The code verifies the complete intertwiner space and its annihilation by the two invariant target readers.

Consequently a fixed lossless pair-only map is impossible **under this selected representation, a fixed scalar proton factor, and no further transforming output degrees of freedom**. This is not an obstruction to beta decay in general. A binary history multiplicity supplies the missing copies. Additional proton spin, orbital modes, or a different physical representation could also change the conclusion.

The claim is about one fixed linear routing across faults. It does not forbid fault-dependent maps that secretly use extra control information; those must account for that control rather than erase it.

## 4. Conditional weight and controls

For the coherent initial state a, the squared norm of the joint branch is

```
q(r_0,r_1,r_2)
 = 1 - [mean(1-r_s)]^2 - [mean(sqrt(r_s(2-r_s)))]^2
 = (1/9) sum_(s<t) [ (r_s-r_t)^2
                    +(sqrt(r_s(2-r_s))-sqrt(r_t(2-r_t)))^2 ].
```

It vanishes exactly when all three r_s are equal. For one missing input in one sector,

```
q_single(r) = 4r/9.
```

The normalized source weights and resulting conditional weights are:

| Input weight r | Multiplicity per sector | q_single |
|---|---:|---:|
| 37/4485 | 2 | 0.003666542797 |
| 740/44551 | 4 | 0.007382300934 |
| 155557/1336530 | 4 | 0.051728314699 |
| 135/598 | 2 | 0.100334448161 |

The decimals are supplied for scale; `comparison_selected_census.json` contains exact fractions. They are not probabilities that the input failures occur. Using squared norm as a production probability additionally requires adopting this constructed instrument and its physical product readout.

For a single-sector event, the pair/history state factors as

```
[ B Q†e_s / sqrt(2/3) ]
 tensor
[ -r|0> + sqrt(r(2-r))|1> ] / sqrt(2r).
```

The two logical spinors in the first factor are maximally entangled, symmetric under their logical swap, and orthogonal to the singlet. Each has reduced density I2/2. These are correlations of the chosen B map, not observed electron/antineutrino helicity predictions. The retained C3 covariance does not establish full spatial-rotation or Lorentz covariance.

### Physical-survival warning

Even the endpoint r_0=r_1=r_2=1 routes the initial common information entirely into the neutron-labelled memory sector in this mathematical model. That does not establish that a neutron survives loss of all local inputs. It makes explicit why retaining a complete information record and physically rebuilding the particle are different operations.

## 5. A source-selection freedom still survives

The same records can all be retained as memory of an intact neutron, with no particle production. More generally, split the contrast routing between ordinary neutron memory and the candidate product channel:

```
repair contrast amplitude = sqrt(1-eta) times the contrast records
product amplitude = sqrt(eta) times P(x),  0<=eta<=1.
```

Norm and threefold covariance hold for every eta, including zero. Thus

```
q_production = eta q_single
```

for the one-input event. Eta is not derived or fitted. The explicit family establishes that the local defect, reversibility and tested symmetry do not uniquely choose replacement over repair.

This is the remaining source-level target: an operation that decides where the comparison record is physically carried and replaces the neutron occupation when it enters the outgoing channel. The electron/partner contact source separately states that zero and nonzero coupling strengths both satisfy its covariance, consistent with this audit's counterexample.

## 6. What was actually checked

`joint_successor_audit.py`:

- Exact symbolic norm identity, source C3 action/frame, pair intertwiners, complement rank, and invariant-subspace dimension.
- All 36 native whole-input losses, four choices of pair-record spin routing each, and 100 arbitrary normalized input checks.
- Complete finite unitary extensions and inverse recovery. These establish reversibility, not decay/escape.
- Largest numerical residual below 4.7e-16.

`comparison_selected_successor.py`:

- Exact rank-four determinant witness and pair-only intertwiner obstruction.
- All 36 native whole-input losses, 12 matched-three-sector loss controls, no-fault and complete-uniform-loss controls.
- 200 additional randomly selected three-sector loss vectors, checking the general variance formula and covariance. These are implementation controls, not a probability law for nature.
- Fixed routing isometry, selected-subspace agreement with the actual source-formula 36-coordinate local fault, conditional pair/history factorization, and logical partial traces.
- Repair-only and variable-routing rivals.
- Largest numerical residual below 7.4e-16.

Exact scalar/symmetry identities provide the general claims. Numerical controls do not establish completeness over all possible native construction laws or 2^432 coefficient masks.

## Source provenance

The prior audit is included unchanged under `source/`; the executed code imports only its pure `geometry()` function. New source reads were:

- `research/strominger/checkers/check_neutron_contrast_electron_transport.py`, blob `c867127a1291a52e38876e168575a2798376fb7b`: retained V and W, contrast identities and physical-dynamics qualification.
- `research/strominger/checkers/check_neutrino_spinor_rim_contact.py`, blob `3239141eb58db335dfef520d0e4064dbca273346`: source electron/partner encoders and singlet contact. The present code works on the logical pair and does not claim a fresh replay of the raw-rim producer.
- `research/strominger/neutrino-rim-attachment-and-contact.md`, blob `16bdf106fdfde62276d23d68ec7a75a3ca0a4c0c`: contact/covariance scope and absence of a derived physical weak-production law.

All repository reads were read-only. No upstream source, generated receipt, production constructor, or proof-assistant file was modified. The p0 factor is a chosen normalized proton-candidate output; its native raw vector and physical species identity were not recomputed or established in this audit.

Primary mathematical background: P. L. Robinson, *Julia operators and Halmos dilations* (2018), https://arxiv.org/abs/1803.09329. The successor formulas, covariance census, rank witness and negative controls here are independent calculations, not results attributed to that paper.

## Reproduction

Python 3.10 or newer with NumPy and SymPy:

```sh
python joint_successor_audit.py
python comparison_selected_successor.py
```

Both scripts write receipts beside themselves. No network, repository checkout or private credentials are required. The bundle includes the input reconstruction, previous receipts, new exact-fraction censuses and run logs. No microscopic failure rate, Planck period, measured lifetime, or adjustable energy scale was used.
