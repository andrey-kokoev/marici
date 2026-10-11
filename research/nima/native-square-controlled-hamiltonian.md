# Hamiltonian realization of the retained square: generator versus controller

**Closed successor comparison (7 October 2026):**
`tick-unitary-image-nonuniqueness.md` reuses this implementation and proves
non-uniqueness of the entire state image, even modulo arbitrary parameters
and overall phase, in an explicitly declared unitary annotation class.
Its rival is not tensor-local between corners; no physical selection or
analytic interpretation of the dependent native return section is inferred.
The existence and return-orientation results below remain unchanged.

## Question and frozen test

The operator asks to test whether Hamiltonian evolution is a realization of the retained witnessed-process framework. SCC obligations: forward realization, attachment transport and route/coherencer compatibility. We use the ACTUAL Bool-negation square from `ObserverCoherenceCube.Geometry`, not the unrelated charge/mass labels.

The rotor branch already constructed a conditional Hamiltonian in `retained-rotor-generator.md`. Repeating that calculation would not answer whether the current square and reflected return admit the required realization.

Conjecture: the source's two commuting involutions admit self-adjoint generators reproducing their square, and their witnessed return admits a Hamiltonian realization. Stronger rival: one autonomous Hamiltonian on the bare realized state is already sufficient for the full reflected traversal. Another rival: source endpoint operations uniquely select that generator.

### Source operations and declared enlargement

Use the orthonormal basis |00>, |01>, |10>, |11> of C^4. This is a declared complex linearization of the finite source set, not a claim that WG selected complex amplitudes or a physical Hilbert space.

Let L flip the first bit and R flip the second. The formal source audit proves these are the actual source expandLeft and expandRight operations and verifies their complete four-input tables, involutions and route equality. Their permutation matrices are commuting self-adjoint unitaries in the counting inner product.

Define

    P_L=(I-L)/2,  P_R=(I-R)/2,
    H0=P_L+P_R.

These are source-derived matrix expressions AFTER the declared linearization. The continuous exponential is an additional analytic enlargement:

    E(a,b)=exp(-i*a*P_L) exp(-i*b*P_R).

The parameters a,b are dimensionless realization angles, not a physical clock. At a,b in {0,pi}, E gives exactly the source square's four corner operations. Along a=b=theta, H0 generates the forward diagonal.

### Required checks

Test projector identities, self-adjointness, all corner attachments, unitarity, route composition, and a real canonical symplectic realization. Then compare the actual reflected square E(pi-a,pi-b) with positive continuation, and test a competing logarithm 3*P_L+P_R against the same source corner data.

The return comparison must keep the whole reflected section; matching its endpoint alone is not an acceptable substitute. Any failure must be retained rather than changing the prescribed return after seeing it.

## Disposition

### A Hamiltonian realization exists

The exact projector decomposition gives spectrum (0,1,1,2) for H0. It is self-adjoint and positive. The commuting spectral projectors establish unitarity and composition for arbitrary real realization angles; 36 exact sixth-root phase pairs give regression coverage. All four source corner operations and both route orders are reproduced.

For psi=q+i*p, choose the standard real symplectic form on R^8. The same generator is realized by the classical quadratic Hamiltonian

    E(q,p)=(q^T H0 q+p^T H0 p)/2,
    q'=H0 p, p'=-H0 q.

The checker verifies the Hamiltonian-gradient and infinitesimal symplectic identities exactly. This normalization is stated explicitly: E is half the Hermitian quadratic form when the real coordinates are Re(psi),Im(psi). No physical hbar or energy unit is inferred.

Thus this finite witnessed square has both a unitary and a canonical Hamiltonian realization after the declared linearization and exponential enlargement. It is no longer just an analogy. The native operation table is freshly Agda-checked; the Hamiltonian algebra is independently exact-checked in Python, not claimed as an Agda formalization of analysis.

### The return reveals an orientation/control distinction

Along the forward diagonal, i*dpsi/dtheta=H0*psi. The reflected section visits E(pi-s,pi-s), so differentiation in increasing s gives i*dpsi/ds=-H0*psi.

If that return is EXECUTED as a second positive-parameter leg, the same state is visited with opposite velocities. At a tested interior point, the squared difference of i-scaled velocities is exactly 6. No autonomous vector field on that same bare state can assign both velocities. The consistent controlled Hamiltonian along a chosen square path is

    H(s)=a'(s)*P_L+b'(s)*P_R.

The leg record determines the relevant orientation; parameter rates remain supplied. Merely continuing H0 in the positive direction reaches the same final identity but follows a different return section: the tested squared state discrepancy is 9/4.

This obstruction is conditional on treating the inverse witness as another forward execution leg. If the reflected section is instead an inverse comparison parametrized in the opposite direction, the SAME autonomous group supplies it by negative parameter. The source record itself does not force an inverse certificate to be an extra chronological execution. The earlier completion-count convention does not settle this intermediate orientation policy.

### Endpoint data do not select the Hamiltonian

The preregistered alternative 3*P_L+P_R passes the same corner tests. A stronger rival, 3*H0, also respects interchange of the identical source axes and is positive, with spectrum (0,3,3,6). It still reproduces all source corners. At the same declared intermediate first-axis angle pi/3, the |00> probability from |00> is 3/4 for the original branch and 0 for the rival.

Hence positivity, the corner witnesses and axis symmetry do not select a unique logarithm. Requiring particular intermediate transport, a primitive-return convention or a rate would add information. Such requirements are not silently inferred from the finite source action. A continuous nonconstant evolution also cannot stay inside the original finite permutation group; analytic enlargement is essential.

### What this establishes about the proposed hierarchy

The retained framework carries the source operations, alternative schedules, inverse witnesses and completion history. A Hamiltonian realization turns specified operations and parameter paths into state transformations. Those state transformations do not by themselves retain all the process history; the preceding square-cone bridge keeps it separately.

This is a checked instance of Hamiltonian realization of retained processes, not a universal equivalence of WG and Hamiltonian mechanics. If the return is used as an additional forward leg, the larger retained record supplies information a bare-state autonomous generator lacks. If it is only an inverse certificate, that extra dynamical demand should not be imposed.

The uniform vector is in the kernel of H0. No excitation of the earlier unperturbed twelve-mode body, charge/mass law, physical clock or autonomous tick-production mechanism follows from this four-state realization.

Verification:

- `pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeSquareHamiltonianSkeleton -Fresh`
- `python research/nima/checkers/check_native_square_controlled_hamiltonian.py`
- Receipts: `results/agda-NativeSquareHamiltonianSkeleton.json` and `results/native-square-controlled-hamiltonian.json`.
- Owner-local SCC model: `scc-models/native-square-controlled-hamiltonian.json`.

The existing source constructors and rotor implementation were not changed. The operator stimulus and bounded report to marici.Sontag were policy-admitted under proposal `ep_69b0dd24-d751-4932-8905-6c1cbc27935c`; admission is not truth certification. This work remains uncommitted. No unique physical Hamiltonian or autonomous realization of every retained history is claimed.
