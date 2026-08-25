# Consolidated continuation milestone: toric-code WP7--WP10

Owner: `marici.Kitaev`

## Disposition

WP7--WP10 are complete at bounded finite strength.  Nima's late
theorem-changing framing correction was incorporated and rechecked.  Generic perturbative stability,
non-Abelian ribbon categories, and colimit claims remain outside scope.

## Exact verification

`python research/kitaev/checkers/check_toric_code_wp7_wp9.py` ran twice with
exit code zero.  Fresh stdout matched
`research/kitaev/results/toric-code-wp7-wp9.json` exactly after newline
normalization.

The checker records:

- an `L=3` open-string endpoint-count history `2,2,0`;
- a noncontractible closed chain with zero syndrome outside the face span;
- odd primal--dual intersection phase `-1` and disjoint control phase `+1`;
- for annular circumferences `3,4,5,6`, absolute `H1` dimension one and
  rough-relative `H1` dimension zero;
- the rough loop projects to zero and its homologous outer loop enters the
  relative face span;
- for toric sizes `2,3,4,5`, a single `-X_edge_0` term anticommutes with
  exactly two plaquettes, preserves four logical Pauli symmetries, and gives
  the exact local block polynomial `lambda^2-5` at unit couplings.

The amended WP1--WP6 checker also records the six-element
`GL(2,F_2)` action, unframed logical orbits `{0}` and `{1,2,3}`, failure of an
individual loop bit to descend, and the requirement that ordered logical
coordinates carry a marked homology basis.

The adjacent command
`python research/nima/checkers/check_boundary_homology_readout_gate.py` also
exited zero.  Its complex, hostile noncomplex, and complete-probe gates all
reproduced.  The new relative-boundary result refines that shared theorem.

## Assumptions and falsifiers

Assumptions: finite labelled square cellulations over `F_2`; the WP1 Pauli
convention; an annulus represented as a periodic-width cylinder embedded in
the plane; rough inner and smooth outer boundary labels; relative chains
formed by the explicit rough-subcomplex quotient; and the one specified
unit-coupling single-edge perturbation.

Falsifiers include a mismatch between endpoint syndrome and commutator,
failure of odd intersection to yield `-1`, a nonzero relative chain
composite, survival of the annular generator after rough condensation, a
single edge meeting other than two plaquettes, or a perturbed block
polynomial different from `lambda^2-5`.

## Shared versus quantum structure

Carrier geometry suffices for labelled support, boundary/residue maps,
relative quotients, intersection, and endpoint/closed-cycle transport.
The quantum coefficient lens is required for Pauli phase, Hamiltonian
selection, incompatible effects, recovery instruments, and spectral
dressing.  No additional primitive Carrier object is forced by this finite
programme.

## Unresolved typing

- Instrument equality still depends on the admitted state domain and whether
  classical histories are retained.
- Generic perturbations require quasi-adiabatic/spectral-flow transport; the
  exact single-edge degeneracy cannot be generalized from this checker.
- A non-Abelian extension needs ribbon fusion/associator/braiding data beyond
  the mod-two intersection pairing.
- The primal rough-boundary computation has a dual smooth-boundary statement
  by exchanged complexes, but a general mixed-boundary family is not proved.

## Process observation

No pre-objective activation snapshot was captured before the continuation and
none is reconstructed.  Immediate post assessment: excitement `9/10`
(relative homology supplied a clean hostile boundary result), confidence
`9/10` for the finite checks and `5/10` for generic perturbative extension,
realized information gain `9/10`.  Confounds: the chosen perturbation is
integrable and deliberately preserves deformable logical symmetries.

Raw delta: three WP7--WP9 constructions and one WP10 appraisal were closed;
eight aggregate checker gates passed; one absolute annular class was killed
by a typed relative relation; one exact spectral block was constructed; four
generic/unbounded successor questions remain.  Process ratings are not
scientific evidence.
