# The first physical wall jet is locally compatible but globally needs a principal cell

The three shared physical walls have the exact normal sequence

\[
0\longrightarrow T_{\rm fiber}
\xrightarrow{J}N_{W_1}\oplus N_{W_2}\oplus N_{W_3}
\xrightarrow{\lambda}P\longrightarrow0,
\]

where

\[
J=\begin{pmatrix}0&1\\1&0\\1&1\end{pmatrix},
\qquad
\lambda=(-1,-1,1),
\qquad \dim P=1.
\]

The wall equations themselves contain the inhomogeneous relation

\[
-q_1-q_2+q_3=p,
\qquad p=x+y+3z.
\]

Thus the cokernel direction is not fitted from linear algebra.  It is the
source-labelled base function \(p\) completing the three wall generators to
the exact inhomogeneous relation

\[
(-1,-1,1,-1)\cdot(q_1,q_2,q_3,p)=0.
\]

The induced first-order base-motion class is represented in this frame by

\[
\kappa(dx,dy,dz)=dx+dy+3dz\in P.
\]

Its scalar expression changes with wall normalizations; its nonvanishing as a
cokernel class does not.

## Three separately certified layers

1. **Local residue compatibility.**  For each wall separately, the moving-wall
   double-pole correction makes bulk differentiation commute with residue.
   The source checker verifies this at exact rational samples for three twists.

2. **Boundary closure.**  The oriented pairwise residues of the literal
   localization boundary cancel, and their first total-energy derivatives
   remain pairwise closed.

3. **Failure of one homogeneous lift.**  A single two-component fiber
   correction cannot preserve all three wall normals under generic base
   motion.  The residual class is precisely \(\kappa\in P\).

These statements are compatible.  The first uses a wall-specific local normal
correction; the third forbids replacing all such corrections by one global
homogeneous horizontal lift.

There is a further geometric identification.  On every pairwise wall
intersection, the remaining wall restricts to \(p\) up to orientation:

\[
q_3|_{W_1\cap W_2}=p,
\qquad
q_2|_{W_1\cap W_3}=-p,
\qquad
q_1|_{W_2\cap W_3}=-p.
\]

Therefore \(p=0\) is exactly the triple-incidence divisor.  The factors of
\(p\) already present in the certified pair-residue norms are its analytic
shadow.  It would be mistyped to adjoin an unrelated rank-one coefficient
line merely because the homogeneous normal lift has a one-dimensional
cokernel.

## Exact conclusion

The first-jet packet has the source-derived shape

\[
T_{\rm base}\xrightarrow{\kappa}P
\qquad\text{over}\qquad
0\to T_{\rm fiber}\to N_{\rm walls}\to P\to0.
\]

Consequently three homogeneous wall covectors alone are not closed under
transport.  The geometrically derived completion is the triple Čech/nearby-
cycle term supported on \(p=0\), not a freely chosen principal coefficient.

The incidence parameter is therefore constructed, and its derivative realizes
\(\kappa=dp\).  This does **not** yet construct the triple Čech nearby-cycle
term or prove that the resulting twisted bulk-to-wall total differential
squares to zero.  Thus the honest frontier is now one geometrically typed
supported calculation, not an unspecified rank-20 connection:

\[
\boxed{\text{construct the triple Čech nearby cycle on }p=0.}
\]

Only after that construction may one compute the dynamic terminal readout
quotient or attach physical meaning to its horizontal orbit.

## Reproducibility

- `research/nima/checkers/check_cosmology_augmented_wall_first_jet_packet.py`
- `research/nima/results/cosmology_augmented_wall_first_jet_packet.json`
- `research/nima/checkers/check_cosmology_source_principal_wall_cell.py`
- `research/nima/results/cosmology_source_principal_wall_cell.json`

The packet reuses, without strengthening, the local certificates in:

- `research/benincasa/physical_bulk_wall_connection_residue.py`
- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`
- `research/benincasa/check_physical_wall_first_gauss_manin_cech.py`
