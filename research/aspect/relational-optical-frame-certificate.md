# Relational certificate for optical probe frames

The preparation frame does not need an externally chosen Pauli orientation to
certify its conditioning. For pure qubit probes with Bloch vectors r_i, the
coherent-residue syndrome rows are

    a_i = (1, r_i).

Their row Gram matrix is

    K_ij = 1 + r_i dot r_j
         = 2 |inner(psi_i, psi_j)| squared.

The same identity extends to mixed qubit probes when fidelity is replaced by
the Hilbert--Schmidt overlap:

    K_ij = 2 trace(rho_i rho_j).

Thus pairwise state overlaps, including diagonal self-overlaps, determine all
singular values, rank, and condition number of the syndrome map. A common unknown unitary rotates every
Bloch vector together and leaves every fidelity unchanged. This is precisely
the gauge transport that should not alter the instrument certificate.

For the tetrahedral frame, every off-diagonal fidelity is one third. Its row
Gram matrix has diagonal two and off-diagonal two thirds, with eigenvalues
four and three copies of four-thirds.

For the selector-constrained frame consisting of one pole and an equatorial
third-turn triple, pole-equator fidelities are one half and equator-equator
fidelities are one quarter. These relational data reproduce the spectrum

    (5 - sqrt(13))/2, 3/2, 3/2, (5 + sqrt(13))/2.

This gives a gauge-free calibration route. Pairwise overlaps may be estimated
by a two-copy interference instrument such as a Hong-Ou-Mandel comparison,
conditional on independently certified photon indistinguishability. Probe
purity need not be assumed: the diagonal self-overlaps supply it. Omitting
those diagonal records would leave mixedness unresolved.

The selector itself need not coherently superpose the bypass and splitter
routes because probe settings are used on separate trials. It must instead:

1. deliver every setting to one common typed target port;
2. preserve the declared rail labels and admitted mode;
3. have stable setting-dependent loss included in the calibration record;
4. keep the pairwise overlap matrix within its preregistered uncertainty set.

This is weaker than coherent route control but stronger than an untyped manual
repatch. A setting-dependent unitary is not automatically a defect; it is a
defect exactly when it changes the certified overlap geometry.

The variable-splitter tetrahedral compiler uses two intensity transmissions

    T_plus  = (1 + 1/sqrt(3))/2,
    T_minus = (1 - 1/sqrt(3))/2

and relative phases pi/4, minus pi/4, 3pi/4, and minus 3pi/4 with the matching
latitude signs. A common downstream unitary remains gauge.

This packet compiles a relational certificate and exact settings. It does not
claim that the selector, variable splitter, two-copy overlap instrument, or
physical data already exists.
