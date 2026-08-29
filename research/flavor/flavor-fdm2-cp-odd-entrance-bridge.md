# The missing CP-odd entrance already exists conditionally in FDM-2: WP1017

## Question

Does the source-derived complex entrance demanded by WP1016 already exist,
and what exactly does it select on physical16?

## Admitted state domain

The domain is the proposed FDM-2 source of WP90: one complex gauge-singlet
flavon, one vectorlike down mediator, real source coefficients, and the
CP-conjugate vacuum union. This is a candidate source architecture, not an
observed UV completion.

With

\[
Y_d=Y_0+r(x+i y)ab,\qquad H_d=Y_dY_d^\dagger,
\]

the exact WP90 matrices give

\[
\det[H_u,H_d]=1920 i r^3 y(x^2+y^2).
\]

At \((x,y)=(4/5,\mathord\pm3/5)\), the source-selected vacua give

\[
\det[H_u,H_d]=\mathord\pm1152 i r^3.
\]

FDM-2 therefore supplies the CP-odd direction missing from the real
two-entrance domain. Deleting its imaginary component, \(y=0\), returns
exactly to the WP1016 obstruction \(J=0\).

## Quotient and contextual partition

The faithful coordinate is the full weak-basis orbit in physical16.
Simultaneous conjugation sends the commutator to a similar matrix, so its
determinant descends. The checker verifies a nontrivial exact orthogonal chart
change.

The source-authorized probe is the existing signed Jarlskog/CKM readout. It
partitions the candidate image into \(y>0\), \(y<0\), and \(y=0\). For finite
\(r>0\), the first two branches are physically distinct and CP violating.
All 1,210 fitted sheets have nonzero \(J\), so the qualitative proper union
survives the ensemble. It does not choose a sheet: \(r\), CP-even spectra,
and the remaining mixing coordinates stay free.

## Classification and instrument

The operation is a qualitative CP selector and a rigidifier of the
source-labelled complex entrance. It is not a numerical selector inside the
observed CP-violating ensemble.

No reference port is used. The singlet and mediator are new source objects,
so this is an enlarged proposed theory, not recovery of absolute phase. The
signed CKM invariant is an actual low-energy readout. Preparation remains
conditional on physical source existence, finite-threshold matching, and
collider-calibrated apparatus.

## Smallest exact falsifier

Set \(y=0\). Then \(\det[H_u,H_d]=0\) identically. This is the exact boundary
between WP1016 and FDM-2. Separately, \(r=0\) is WP92's decoupling falsifier
and collapses the response cubically.

## Claim boundary

This packet identifies an existing proposed-source bridge. It does not
promote FDM-2 to an observed source, derive \(r\), select CP-even physical16
coordinates, or establish the preparation instrument. Qualitative selection
of \(J\ne0\) is not a numerical flavor explanation.

## Disposition

Close the search for a source-derived CP-odd entrance as solved conditionally
by FDM-2. Keep the selector frontier open at the next arrow: derive the finite
threshold ratio and CP-even coefficient packet, then realize and calibrate the
mediator preparation experiment.

Verification: uv run --with sympy python
research/flavor/checkers/wp1017_fdm2_cp_odd_entrance_bridge.py.
