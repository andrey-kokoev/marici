# Inter-component raising has a universal current defect

The missing map is not arbitrary. After splitting the reflected route packet
into its two branches, the source lattice supplies a canonical input
correspondence from component \(q\) to component \(q+2\):

\[
m_-=1-g-q-a\longmapsto m_--2,
\]

\[
m_+=1-g+q-a\longmapsto m_++2.
\]

Equivalently, the minus branch is multiplied by \(\bar z^{-2}\), while the
plus branch is multiplied by \(\bar z^2\). This is branchwise and therefore
does not yet define an operation on a parity-identified readout.

## Exact intertwining defect

Write the source polynomial coefficients as

\[
c_j=
\binom gj(-1)^{g-j}
a^{\overline{g-j}}(4-a)^{\overline j}.
\]

The magnetic path column has coefficients

\[
p_0(m)=mc_0,
\]

\[
p_j(m)=(m+j)c_j+(m+j-1-g)c_{j-1}
\quad (1\le j\le g),
\]

and

\[
p_{g+1}(m)=mc_g.
\]

Hence its finite difference is independent of \(m\):

\[
p(m+2)-p(m)=2J_{g,a},
\]

where

\[
J_{g,a}=(c_0,c_1+c_0,\ldots,c_g+c_{g-1},c_g).
\]

After the canonical row alignment of the plus branch, the two route defects
are therefore

\[
M_gT_- - T_-^{\rm out}M_g=-2J_{g,a},
\]

\[
M_gT_+ - T_+^{\rm out}M_g=+2J_{g,a}.
\]

The signs are opposite, but the currents occupy the branch-specific aligned
supports. They do not cancel in the untyped scalar readout.

## Meaning

There is a source-derived inter-component correspondence, but it is not a
chain map for the magnetic readout. Its obstruction is a universal current
depending on \((g,a)\) and not on \(q\).

This gives a minimal repair criterion. A typed augmented target that retains
the branch label and one copy of \(J_{g,a}\) can represent the correspondence
and its defect. Quotienting away that current before applying the raising
operation makes the operation ill-defined.

The discrete sign incidences become natural only if a further source theorem
shows that the relevant scalar route augmentation annihilates, balances, or
otherwise accounts for this current. Without such a theorem they remain
labelled comparisons.

The unexpected point is that the missing constructor is not missing entirely.
What is missing is closure of an existing branchwise constructor under the
chosen readout.

Replay with: python research/strominger/checkers/magnetic_intercomponent_current_defect_checks.py
