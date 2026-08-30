# Toric-code braiding, mixed boundaries, and one local perturbation

Status: finite-cutoff theorem for the displayed cellulations and the single
specified perturbation.  This packet covers WP7--WP9.

## WP7: transport and mutual braiding

For a primal path `gamma`, `Z(gamma)` anticommutes with precisely the endpoint
stars because its commutator vector is `d1 gamma`.  Extending the path changes
the endpoint framing; closing it removes the local syndrome.  On the `L=3`
torus the checked three-edge history has endpoint counts `2,2,0`, while the
closed final loop is not a plaquette repair.

An electric and magnetic worldline with mod-two intersection one obey

\[
Z(\gamma)X(\gamma^*)=-X(\gamma^*)Z(\gamma).
\]

The checker realizes this using a contractible closed `Z` braid and a
crossing dual `X` worldline; the phase is `-1`.  A disjoint control has phase
`+1`.  Open-string transport therefore requires endpoint data, while a
closed supported cycle has invariant intersection holonomy.  Carrier
geometry supplies support, boundary, and intersection; the quantum lens
turns parity into an operator phase.

## WP8: hostile mixed-boundary test

Use an annular square cellulation (a finite cylinder embedded in the plane).
The inner boundary is rough and the outer boundary smooth.  Before boundary
condensation its absolute primal homology has dimension one.  Admit the rough
boundary subcomplex `R` as a legal relation and use

\[
H_1(K,R)=\ker d_1^{rel}/\operatorname{im}d_2^{rel}.
\]

For circumferences `3 <= L <= 6` and width two, the checker obtains
`dim H1(K)=1` but `dim H1(K,R)=0`.  The rough circumference projects to zero;
the homologous outer loop becomes a relative face repair.  Thus boundary
condensation really can fill a formerly global readout port, but only through
the explicit quotient/projection maps.  Merely naming a boundary does not
change the observable algebra.  Exchanging primal/dual and rough/smooth
gives the complementary magnetic statement.

This is consistent with Bravyi--Kitaev's description of mixed-boundary
surface codes by relative homology (arXiv `quant-ph/9811052`).

## WP9: explicitly bounded perturbation

Set `J_e=J_m=h=1` and perturb one frozen toric Hamiltonian by

\[
H'=H_0-X_{e_0}.
\]

The cellulation, `d1 d2=0`, and homology remain exact: they do not depend on
Hamiltonian coefficients.  Spectrally, `X_e0` anticommutes with exactly the
two adjacent plaquette terms, so those individual syndrome eigenvalues are
not conserved.  In the equal-plaquette sector the affected exact block is

\[
\begin{pmatrix}-2&-1\\-1&2\end{pmatrix},\qquad
\det(\lambda I-M)=\lambda^2-5.
\]

The source quantity controlling local mixing is therefore the unperturbed
two-defect energy `4J_m` together with `h`, through
`sqrt(4J_m^2+h^2)`.  For this specially chosen single-edge Pauli, logical
representatives can be deformed away from `e0`, so the ground degeneracy
remains exactly four.  This is not a generic perturbative-stability theorem.
Generic bounded local perturbations require spectral-flow/Lieb--Robinson
control and generally give a narrow low-energy band rather than exact
commuting-projector syndromes; see Bravyi--Hastings--Michalakis,
arXiv `1001.0344`.

## Falsifiers and limits

The transport result fails if endpoint syndrome differs from the commutator
vector or odd intersection does not produce `-1`.  The boundary result fails
if the relative composite is nonzero or the killed absolute class survives
the relative quotient.  The perturbation result fails if `X_e0` touches
other than two plaquettes or the local block polynomial differs from
`lambda^2-5` at the frozen couplings.

No claim here covers non-Abelian braiding, finite-temperature memory,
arbitrary perturbations, or an unbounded thermodynamic limit.

