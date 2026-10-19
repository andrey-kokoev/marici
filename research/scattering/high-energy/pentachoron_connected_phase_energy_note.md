# All-cell phase energy of the reconnected pentachoron boundary

Date: 2026-10-11  
Status: Conditional finite phase-record calculation. No physical electron–positron scattering claim.

## 1. Result

Replacing the two original ABE seams by their two crossed counterparts changes the native full-spinor mismatch spectrum while retaining all ten tetrahedral cells and twenty seams. In the tested positive-trace, opposite-chirality sewing convention, the connected boundary has a lower minimum mismatch cost. It still has no nonzero exactly parallel full-spinor configuration.

The local merging gate must be enlarged to include all cell records. Their native evolution does not preserve the gate's two-dimensional matching subspace. Consequently a single scalar detuning does not exactly represent the connected boundary's phase dynamics.

Keeping the previously declared five-cycle defect comparisons changes the result further: a locally mismatched input can develop a matched component and then merge. The previous strictly zero probability for that preparation was a result of the bare local gate, not a universal rule.

These are new calculations in the declared model. They do not identify the connected object with a stable particle or infer measured energy release.

## 2. Retained sources and new choices

The unchanged `pentachoron_phase_merge_bundle.zip` is included as an input. Its checker and embedded boundary-gluing checker are hash-verified before their geometry, occurrence labels, and functions are used. The script's result JSON records all input hashes and inherited repository blob identifiers.

The original repository ingredients are:

- `research/voevodsky/electron-pentachoron-attachment.md`: five marked regular-simplex vertices.
- `research/voevodsky/pentachoron-geometric-spin-interfaces.md`: intrinsic normal-fold spin lifts and the equally weighted squared full-spinor mismatch functional.
- `research/voevodsky/native-operation-energy-lift.md`: the common positive defect-energy constructor; no physical time conversion.
- `research/voevodsky/pentachoron-cycle-spin-energy-transport.md`: the supplied source five-cycle, its reflection-word spin lift, and the separately declared cycle-defect term.

The calculation preserves the previous frozen triangular-comparator pose at delta_c=atan(1/sqrt(5)). The right body is a spatial mirror. Left and right chirality are respectively + and −, as in the successful local sewing test.

**New extension:** The prior local gate only used the selected-line restriction of each cross-body fold. Here its complete positive-trace 2-by-2 unitary is used on the full cell spinor. The common inter-chirality frame identification remains a supplied sewing convention, not a globally derived Pin transformation. Another extension could give another connected spectrum.

**Retained-cycle variant:** Both original five-cycle comparison operators are kept, with the same coefficient in either topology. This preserves labeled source operations. It does not assert that either constituent cycle remains a geometric symmetry of the newly glued boundary; an exact commutator check shows that the connected seam operator breaks that symmetry. Keeping these record comparisons after reconnection is an explicit extension, not forced by boundary topology.

No QED propagator, measured particle mass, experimental branching ratio, or measured scattering energy is used in this calculation.

## 3. Phase space and energy comparison

Each of the ten retained tetrahedra carries a two-component phase record z_i. A topology sector therefore has twenty complex coordinates:

    z=(z_0,...,z_9) in C^20,    sum_i ||z_i||^2=1.

This is a direct sum of phase records, not the tensor-product Hilbert space of two independently prepared particles. In particular, its normalized minimum is not the sum of two physical rest masses.

For every oriented seam i→j, use the native transport U_ij and residual

    (D z)_ij=z_j-U_ij z_i.

Reverse transport is U_ij^dagger. Apply the same positive coefficient epsilon to every seam:

    E(z)=epsilon sum_seams ||z_j-U_ij z_i||^2
        =epsilon z^dagger L z,    L=D^dagger D,    epsilon>0.

Epsilon is an unspecified common phase-energy unit. It is not independently equated to the mechanical toy's E_*.

Original seams: a K5 adjacency on each body. Remove only (L_C,L_D) and (R_C,R_D), where the subscript is the omitted vertex. Add (L_C,R_C) and (L_D,R_D). All remaining internal folds and cell occurrences are unchanged. The actual gluing checker supplies this pairing, rather than a convenient graph being selected for its spectrum.

Both operators have twenty seams, degree four at every cell, twenty complex dimensions, trace 80, and squared trace 400. The reconnection does not add a scalar energy because the graph has changed.

## 4. Exact seam-only spectrum

For the original pair:

    lambda=4-sqrt(6),             multiplicity 8,
    mu=4+2sqrt(6)/3,              multiplicity 12.

For the connected boundary, each of the following has multiplicity four:

| Eigenvalue | Approximation |
|---|---:|
| Smallest quartic root | 1.179647481673 |
| Second quartic root | 2.145425605690 |
| Third quartic root | 4.710776049226 |
| mu | 5.632993161855 |
| Fourth quartic root | 6.331157701555 |

The rounded quartic values are for display; the JSON contains the freshly computed spectrum and exact rational root intervals.

Writing a=sqrt(6), the quartic is

    f(x)=x^4+(-16+2a/3)x^3+(266/3-8a)x^2
         +(-592/3+86a/3)x+(442/3-88a/3).

The checker proves exactly

    (L_C-mu I) f(L_C)=0.

It also checks the trace/Newton identities, which establish the multiplicity four of each distinct root. Four disjoint positive rational intervals have exact sign changes for f over Q(sqrt(6)); because f has degree four, they enclose all four simple roots. The remaining eigenvalue mu is explicitly located between the third and fourth intervals. Thus the spectrum is not inferred solely by grouping close floating-point eigenvalues.

The normalized minimum changes by

    min E_connected - min E_original
       = -0.370862775544 epsilon  (approximately).

This is a difference between minima under the same phase-record norm. It is not proof that an arbitrary incoming state loses that energy or can relax into the connected minimum.

A stronger control is exact. With dL=L_C-L_O:

    dL^3=2 dL,
    tr(dL)=0,
    tr(dL^2)=16.

Hence dL has eigenvalues −sqrt(2), 0, +sqrt(2), with multiplicities 4, 12, 4. It is indefinite. Reconnection lowers the cost of some phase patterns and raises the cost of others, with no overall ordering of the two operators.

## 5. Keep the declared source-cycle energy

For each body, reconstruct the four-dimensional source rotation from its reflection word. Its spin lift S gives

    (T z)_(c+1)=S z_c,
    T^dagger T=I,    T^5=-I.

The exact checks include the cycle's action on all five actual vertices and spin covariance on all six independent bivectors. They also recover commutation with the original seam operator.

On the two-body record space, keep

    X=2I-T-T^dagger=(T-I)^dagger(T-I),
    H_O=epsilon(L_O+X),
    H_C=epsilon(L_C+X).

The positive defect term is the source's additional comparison law. T itself is not assumed to be a physical clock, nor is its step identified with Hamiltonian time evolution.

| Phase-energy construction | Original minimum / epsilon | Connected minimum / epsilon | Difference / epsilon |
|---|---:|---:|---:|
| Native seams only | 1.550510257217 | 1.179647481673 | −0.370862775544 |
| Seams plus retained cycles | 1.932476268467 | 1.705360384484 | −0.227115883983 |

The first original-cycle minimum is exactly (11−2sqrt(6)−sqrt(5))/2 and has multiplicity four in the disconnected record model. The connected-cycle minimum is numerical, has multiplicity two, and is checked by two eigenvalue routines and the full eigenpair residual. The matrices and positive-defect identities are exact. No physical spin identification follows from these multiplicities.

Changing the sign of both cross-seam lifts is a whole-right-body phase change and preserves the spectrum. Changing only one crosses a different loop-holonomy convention and changes the spectrum, despite leaving the seam count unchanged. That control is not a reason to tune a lift sign: the default remains the predecessor's fixed positive-trace convention.

## 6. Lift the phase-compatible gate to all cells

Let P be the rank-two matching projector from the prior local gate, embedded into the four selected ABE occurrence lines inside C^20. In these common raw occurrence coordinates the connected branch's matched/mismatch encoding is decoded back to the same retained records. Its matching transfer is P itself; no cell information is removed.

On the two topology sectors define

    J = [[I-P, P],
         [P,   I-P]],
    J^dagger=J,    J^2=I.

The old and connected record spaces each have twenty coordinates, so the full gate is forty-dimensional. Its positive defect energy uses the same coefficient:

    H_gate=epsilon (J-I)^dagger(J-I)
          =2epsilon(I-J).

For a frozen activated contact and the retained-cycle variant, the complete operator is

    H/epsilon = [[L_O+X+2P, -2P],
                 [-2P,     L_C+X+2P]].

Omit X for the seam-only variant. The result is Hermitian and positive; every unmatched coordinate remains in the state space. Native evolution may populate other modes rather than erasing them.

The exact commutators show that neither native topology operator preserves im(P). It would therefore be incorrect to replace the connected operator by its lowest eigenvalue and insert that value as a single detuning into the previous two-level formula. Such a reduction needs its own invariant-subspace or controlled-approximation argument.

## 7. Frozen-contact transition test

Use equal-strength phase records at the C-omitted seam, with relative phases measured after the geometric transport mu=(sqrt(10)+i sqrt(6))/4. These are specified local input records, not ground-state electron or unpolarized beam preparations.

For one illustrative pulse, retain the same normalization as the earlier gate:

    epsilon=pi hbar/(4 tau),    T=tau,
    s=epsilon T/hbar=pi/4.

No relation between tau, the classical contact window, or c is asserted. The pulse duration is a comparison benchmark, not a physical collision-speed prediction.

| Initial relative phase | Bare local gate | Native seams | Native seams plus retained cycles |
|---|---:|---:|---:|
| 0 | 1 | 0.474789109162 | 0.373948319383 |
| pi/2 | 0.5 | 0.237394554581 | 0.163824074469 |
| pi | 0 | 0 | 0.014787733599 |

The probabilities are the final squared norm in the connected-topology record sector. The matrix exponential, independent spectral propagation, DOP853, and RK45 integrations agree. Full norm conservation and invariance under consistently transformed local phase frames are checked.

The initially opposed input illustrates a genuine new mechanism, not numerical noise. Let D_dark be the selected mismatch projector. For seams alone,

    P L_O D_dark=0,

and the original quadratic spectral identity implies P exp(−is L_O)D_dark=0. These particular initial mismatch records therefore remain unable to activate the gate in the seam-only model.

With retained cycles, the exact identity is instead

    D_dark (L_O+X) P (L_O+X) D_dark = D_dark/12.

For any normalized input in that two-dimensional selected mismatch sector, the connected probability begins as

    P_connected(s)=s^4/12+O(s^5).

Internal phase evolution first develops a matched component; the topology gate then transfers it. The count of geometric reconnection instructions has not changed.

## 8. Energy accounting and scope

During the constant pulse, the full Hamiltonian and its expectation are conserved. However, activating and deactivating the prescribed gate performs work. The calculation separately records switch-on work, switch-off work, and the resulting change in native phase energy, and verifies their balance.

This is not an autonomous mechanical collision. Translational momentum has not supplied the switching work, and no post-gluing geometry or trajectory has been integrated. A lower connected minimum cannot be called emitted radiation or kinetic energy release in this calculation.

Remaining boundaries:

- The opposite-chirality full-spinor cross-seam comparison is still a declared extension in fixed source frames.
- Exact all-seam parallel matching still fails; the least-mismatch functional is the admitted replacement, not proof that every geometric seam has zero mismatch.
- Normalized phase-record spectra are not physical two-particle rest energies.
- The entire two-particle tensor-product preparation and asymptotic scattering construction remain absent.
- No stability, photon multiplicity, relativistic speed scale, or 372:1 result is inferred.

The next constructive target is a joint position–phase Hamiltonian with a defined post-reconnection geometry and a common energy reference, so contact activation exchanges energy with motion instead of being prescribed externally.

## 9. Reproduction

Unzip the new bundle and run:

```sh
python pentachoron_connected_phase_energy.py
```

The unchanged predecessor bundle is included beside the script. Dependencies are NumPy, SciPy and SymPy. No network access is required. The result JSON contains exact matrices, rational root brackets, source hashes, numerical spectra, transition probabilities, switching-work balances, and the complete check ledger.

The exact calculations use rational arithmetic in Q(sqrt(2),sqrt(3),sqrt(5),i). The connected-cycle spectrum and finite-pulse integrations are numerical checks with recorded residuals; they are not presented as exact closed-form eigenvalues or experimental uncertainties.
