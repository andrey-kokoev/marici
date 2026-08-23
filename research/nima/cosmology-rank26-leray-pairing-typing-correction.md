# The rank-26 physical readout is a twisted Leray pairing

The stabilized coefficient object is the rank-26 twisted cohomology of the
five-mark complement on

\[
q_{\mathcal G_{12}}=E+y_{12}=0,
\qquad (a,b)=(y_{23},y_{31}).
\]

The literal positive chamber does not meet this surface directly: there
\(E>0\) and \(y_{12}\geq0\). Entry 180 nevertheless supplies the canonical
adapter. The published negative-imaginary prescription transports the
positive Cayley--Menger germ through the convex tube \(T_-\) to a unique local
Leray residue germ

\[
\Gamma_E^{\rm res}: K_0(a,b)\geq0,\qquad w=+\sqrt{K_0(a,b)},
\]

oriented by \(da\wedge db\) and with multiplicity one. Hence the typed
comparison is

\[
\boxed{H^2_{\rm dR}(S_E\setminus W;\mathcal K)\times
H^{\rm rel,tw}_2(S_E\setminus W;\mathcal K^\vee)\longrightarrow\mathbb C.}
\]

## Superseded gate

Auditing ordinary boundary traces of every integration-by-parts primitive is
not the correct prerequisite. The interval identity
\(\int_{[0,1]}dx=1\) concerns an ordinary chain with boundary; it does not
decide pairing with a source-oriented twisted relative Leray cycle, whose
boundary, branch, and regularization are part of the duality datum.

The unmarked Cayley--Menger census remains useful geometry, but it does not by
itself obstruct the rank-26 pairing.

## Correct frontier

The local dual object exists canonically. Missing from the stabilized finite
presentation is its explicit period covector

\[
\operatorname{Per}_{\Gamma_E^{\rm res}}:H^2_{26}\longrightarrow\mathbb C.
\]

The next construction must retain the source-labelled rank-26 basis and
evaluate or transport this canonical germ. Globally, its variation around
generic \(\mathcal Q=0\) is not unresolved: the simultaneous-resolution
theorem gives

\[
T_{\mathcal Q}=1,\qquad
N_{\mathcal Q}=0,\qquad
\operatorname{Var}_{\mathcal Q}(\Gamma_{\rm phys}^{\rm res})=0.
\]

Therefore the missing covector cannot reopen \(\mathcal Q\) as intrinsic
physical support.  Its purpose is to determine which parts of the nonsplit
rank-26 coefficient system the physical contour observes, and with what
source normalization.  Coordinate pairing, direct positive-chamber
restriction, post-hoc addition of an absolute cycle, and fitting a
\(\mathcal Q\)-degenerate response matrix are inadmissible.

The subsequent half-twist audit sharpens “transport”: although the bounded
generic and physical presentations both have dimension 26, their relation
spaces differ. See
`cosmology-rank26-half-twist-relation-lattice-obstruction.md`. A derived
contiguity or limiting-lattice comparison must precede the period covector.

Evidence: `published_boundary_value_leray_uniqueness.md`,
`research/benincasa/q_sheet_resolution_certificate.md`,
`check_nine_master_griffiths_dwork.py`, and
`results/physical_marked_rank26_geometry.json`.
