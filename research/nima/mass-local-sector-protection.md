# Local transition protection does not protect the numerical mass gap

## Fresh obligation and assumptions

The primitive-quotient rotor construction and its dependencies are freshly
rerun. It supplied physical states

    |k,...,k;n_e>,    Q=k-n_e,

but allowed a charge-preserving operator changing both k and n_e. This trial asks
whether microscopic locality can exclude that operation without postulating a
separate conserved particle number. This is a conditional forward-realization
result, not a derivation of the required locality from spacetime.

Assumptions:

1. The Gauss constraints n_s=n_t are EXACT, not finite penalty terms.
2. The microscopic tensor factors are the1836 internal rotors and one elementary
   rotor. Hamiltonian terms have support on fewer than1837 of these factors.
3. The physical Hamiltonian preserves Q and the constrained Hilbert space.
4. No additional gauge-field/matter degrees of freedom alter these constraints.

The support notion is locality in the chosen rotor tensor product. The comparison
graph does not establish that this is physical spatial locality.

## Exact support theorem

For two distinct physical basis states with the same Q,

    k-n_e = l-m_e,

k and l must differ, and n_e and m_e must differ by the same amount. Every internal
rotor changes, as does the elementary rotor. The two configurations differ on all
N+1=1837 tensor factors.

Any operator omitting even one of these factors has zero matrix element between
them: its untouched factor contributes an orthogonal charge-basis overlap.
Therefore every strictly smaller-support Hamiltonian term has zero off-diagonal
matrix elements inside a fixed-Q block. Together with charge conservation, the
exact constrained evolution preserves k and n_e separately.

This supplies a conditional particle-sector separation from exact constraints
and locality, rather than adding conservation of k as a separate axiom. The
bound is sharp: the collective charge-preserving operator

    exp[-i(sum_s theta_s + theta_e)]

changes (k,n_e)=(1,0) to (0,-1) and acts on all1837 rotors.

Without Q conservation, changing only the elementary rotor takes one site.
With finite Gauss penalties, virtual excursions outside the constrained space
can permit conversions at higher order. The exact statement does not apply to
that softened model, nor to an expanded gauge theory with additional local
charged fields. No decay rate or relativistic particle identification is proved.

## The energy gap is locally distinguishable

A single operator n_s^2 has different diagonal matrix elements in the collective
state (1,0) and the elementary antiparticle state (0,-1). It can shift their
relative energy without changing either charge or sector. Thus the1837-factor
transition distance is NOT a quantum error-correcting distance protecting all
errors: a one-site diagonal perturbation already acts nontrivially.

A symmetry-preserving family makes the distinction explicit. In elementary-gap
units add

    delta H = epsilon * sum_(state-comparison slots) n_s^2.

This is a sum of one-site terms, preserves all declared Gauss laws and typed
relabelings, and cannot cause sector conversion. Nevertheless it changes the
collective/elementary energy ratio to

    1836 + 108*epsilon.

At epsilon=1 the equally protected unit-charged collective state has ratio1944.
At epsilon=0 it has1836. Protection against conversion has not fixed the energy.

## Why the obvious larger symmetry does not fix normalization

One might demand a permutation symmetry exchanging the elementary rotor with an
internal rotor to equate their microscopic charging coefficients. Such a swap
takes |1,...,1;0> outside the Gauss subspace: one internal charge becomes0.
It is not a symmetry of the present constrained physical model.

Closing the Gauss constraints under all such swaps instead imposes n_e=k too.
Then Q=k-n_e vanishes on every surviving state, removing the desired charged
sectors. A permutation-symmetric parent theory with a dynamically selected
constraint phase remains possible, but is a new construction, not an available
symmetry of this model.

Exchanging the two PHYSICAL rotor coordinates k and n_e is different. It reverses
Q; invariance of A*k^2+C*n_e^2 under that exchange forces A=C, giving equal gaps
rather than ratio1836. Neither simple symmetry extension supplies the wanted law.

## Verification and frontier

    python research/nima/checkers/check_mass_local_sector_protection.py
    python research/aspect/scc/scc.py check nima-mass-local-sector-protection

Exact charge-window tests cover small rotor families and the full1837-factor
configuration. The general support result follows from tensor-factor
orthogonality, not from finite sampling of operators. Report:
`results/mass-local-sector-protection.json`.

The candidate now has consistent unit charges and a conditional local sector
protection mechanism. What remains unselected is its energy law: the same
protection admits a continuous family of mass ratios. Source exact Gauss laws,
physical locality and the charging action before identifying a proton/electron
mass explanation. Reasserting equal coefficients would restate the target.
