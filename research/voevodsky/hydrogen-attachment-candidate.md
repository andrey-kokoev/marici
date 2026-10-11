# Hydrogen candidate: a neutral shell state, but an exact angular obstruction

## Question and separation of assumptions

Could the outward tetrahedral attachment represent hydrogen? Test the simplest completion that gives the attachment a state space, charge and energy, without fitting a constant to 13.6 eV.

The retained 1836-arrow core is verified unchanged. The source contributes twelve boundary triangles and their adjacency graph: twelve vertices, eighteen links, degree three. Their centers give twelve candidate attachment directions. These geometric data are derived; the following electron interpretation and dynamics are hypotheses.

- A one-excitation Hilbert space has an orthogonal basis indexed by the twelve faces, plus a separate vacuum sector.
- Core charge is assigned +1 and occupation charge -1. Total charge is Q=I-N_e. Neutrality is consequently conditional on that assignment, not a prediction of the tetrahedral geometry.
- At radial attachment scale rho>1, prescribe H(rho)=(A/rho^2-B/rho)I+(t/rho^2)L on the occupied sector, with A,B,t positive and L the unweighted adjacency Laplacian.
- The separated reference energy is zero. This is a finite shell Hamiltonian with a variational radial parameter, not a constructed radial Schrödinger operator or a proof of physical atomic binding.
- Position observables are diagonal point-site observables at the twelve attachment centers. This observation map is essential to the falsifier below.

The earlier source audit `research/nima/proton-hydrogen-helium-structure.md` already separates construction counts from energy and rejects simple universal counting rules. This experiment does not replace that distinction or infer energy from 1836.

## Conditional neutral negative-energy state

The exact graph Laplacian spectrum is:

| Eigenvalue | Multiplicity |
| --- | ---: |
| 0 | 1 |
| 1 | 3 |
| 3 | 2 |
| 4 | 3 |
| 5 | 3 |

The uniform angular state is the unique zero mode. Its variational energy is A/rho^2-B/rho. Completing the square gives a stationary minimum at rho=2A/B with value -B^2/(4A), provided the radius is admissible (rho>1). There is no negative energy when the attractive term is removed.

For the explicitly chosen dimensionless A=B=t=1, rho=2 is admissible and the ground energy is -1/4. The shell levels are -1/4, 0, 1/2, 3/4 and 1 with the multiplicities above. Only one is strictly negative. This fixed-radius finite model supplies neither the hydrogen Rydberg series nor an energy unit, electron spin or statistics. No physical Bohr radius or 13.6 eV binding is derived.

## Why twelve-face superposition does not give spherical density

At rho=1, the twelve center vectors are permutations of (7,1,-1)/9 with the sign choices inherited from the tetrahedron. Each has squared radius 17/27. Uniform probabilities have zero first moment and normalized covariance I/3: the dipole and quadrupole tests pass.

Higher moments expose the remaining tetrahedral directionality:

| Observable | Twelve-site model | Spherical distribution |
| --- | --- | --- |
| Raw xyz at rho=1 | -7/729 | 0 |
| Mean normalized x^4 (also y^4 and z^4) in uniform state | 89/289 | 1/5 |

The third-order obstruction is stronger than failure of the uniform state. **Every one of the twelve sites has xyz=-7/729.** Therefore the diagonal XYZ operator is (-7/729)I throughout the occupied sector. Any normalized pure state, unequal mixture, or choice of relative phases gives the same nonzero expectation. At common scale rho it becomes -7 rho^3/729; radial scaling cannot eliminate it.

This is an exact obstruction to spherical ground-state density under the declared point-site observation map. It does not prove that a tetrahedral internal description with a different continuous observation map can never approximate hydrogen. In particular, if the twelve points are only a numerical discretization, this is a resolution/symmetry limitation rather than a physical theorem.

## Disposition

The conditional model admits a neutral negative-energy state because charge and attractive dynamics were explicitly supplied. It **fails the simplest hydrogen interpretation**: the density remains tetrahedrally anisotropic, the shell spectrum is not hydrogen's, and spin/physical normalization are absent.

All 17 computational checks passed, including the anisotropy falsifiers. A passed test suite here means the counterexample and conditional calculations were reproduced—not that the hydrogen conjecture was confirmed.

The next useful extension would specify spatial wavefunctions or a continuous observation map for the attachment sector and test isotropy and radial dynamics. Merely changing probabilities on these same twelve point sites cannot solve the third-moment obstruction.

## Reproduction and evidence

```text
python research/voevodsky/checkers/check_hydrogen_attachment_candidate.py
```

- `research/voevodsky/results/hydrogen_attachment_candidate.json`: exact spectrum, moments, assumptions and checks.
- `research/voevodsky/results/hydrogen_attachment_candidate_model.json`: content-addressed model declaration referencing the retained focus root. Its referenced core remains in `proton_merkle_store.json`.
- `research/voevodsky/checkers/check_hydrogen_attachment_candidate.py`: rational linear algebra and model tests.

No fit to atomic data, physical particle identification, Git commit or deployment is claimed.
