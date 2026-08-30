# Charged-cycle contact descent

## Bounded question

If the charged scalar in WP638 is not kinematically accessible, does exact
tree elimination erase the charged-cycle response or transport it to a
light-field contact operator?

## Source current and elimination

Write the WP638 interaction on the real sign slice as

\[
\mathcal L_{\rm int}=\chi J+\chi^\dagger J^\dagger,
\qquad
J=(L_A+L_B)\mathcal O_6,
\]

where

\[
\mathcal O_6=\bar Q_L\widetilde H^uSXd_R.
\]

The light operator has canonical dimension six and hypercharge minus one.
Together with \(Y_\chi=1\), the source vertex is neutral. Eliminating a
positive-mass charged scalar at zero momentum gives

\[
\mathcal L_{\rm contact}=-{|L_A+L_B|^2\over m_\chi^2}
\mathcal O_6^\dagger\mathcal O_6.
\]

The contact operator has dimension twelve and its coefficient has mass
dimension minus eight. It is neutral and invariant under a common rephasing
of the charged source current. Thus the response descends under the declared
source rephasings without treating an absolute charged phase as observable.

## Exact contextual partition

On the unit real slice, relative sign plus gives contact magnitude four at
\(m_\chi=1\), while relative sign minus gives zero. The charged-cycle
distinction therefore survives removal of the charged pole.

The cycle invariant alone is not a faithful coordinate for this response.
Holding \(\mathcal I_\chi=1\) fixed while changing \(m_\chi\) from one to two
changes the contact magnitude from four to one. The admitted response family
is partitioned by both the relative path coordinate and the charged-scalar
mass normalization.

## Classification and physical gate

This is a source-derived contact descent, not a flavor selector. It neither
chooses \(\mathcal I_\chi\) nor selects a point of `physical16`; it enlarges
the low-energy theory by a dimension-twelve interaction. It is also not yet a
physical instrument. Instrument authority requires a declared light-particle
scattering or decay channel, momentum-dependent matching, Standard Model
interference where allowed, running and mixing, hadronic matrix elements,
detector acceptance, and a calibrated likelihood. If all accessible records
depend only on a squared coefficient, the sign of the total matched current
remains unidentifiable even though its destructive zero is testable.

## Reproduction

Run:

    python research/flavor/checkers/wp639_charged_cycle_contact_descent.py

The generated result is
`research/flavor/results/wp639_charged_cycle_contact_descent.json`.
