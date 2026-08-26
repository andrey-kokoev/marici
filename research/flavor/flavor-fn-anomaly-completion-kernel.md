# Anomaly completion does not select the single-spurion charge gaps

Work package: WP615  
Owner: marici.Figueiredo

## Bounded question

Can anomaly cancellation independently authorize the WP614 charge vector
\(q=(3,2,0)\), or does an admitted vectorlike completion erase that selecting
power?

## Admitted source domain

Take three left-handed quark-doublet ports with arbitrary integral
Froggatt--Nielsen charges. Permit one left-handed conjugate mirror for each
port, in the conjugate Standard Model representation and with both
hypercharge and flavor charge reversed. This is a deliberately open UV
completion domain. It tests anomaly cancellation as a selector only when the
extra spectrum has not already been forbidden by an independent source law.

The audited local anomaly packet is

\[
SU(3)^2U(1)_F,\quad SU(2)^2U(1)_F,\quad U(1)_Y^2U(1)_F,
\quad U(1)_YU(1)_F^2,\quad U(1)_F^3,\quad \mathrm{grav}^2U(1)_F.
\]

For every seed field \(X\) with charges \((Y,q)\), its conjugate mirror has
\((-Y,-q)\). The two contributions cancel term by term in all six entries.
Consequently, anomaly freedom holds for every integral flavor-charge vector
on this completed domain.

## Exact hostile pair

Compare

\[
q=(3,2,0),\qquad q'=(4,1,0).
\]

They are not related by a common shift or reversal. Their charge-distance
matrices are respectively

\[
\begin{pmatrix}0&1&3\\1&0&2\\3&2&0\end{pmatrix},
\qquad
\begin{pmatrix}0&3&4\\3&0&1\\4&1&0\end{pmatrix}.
\]

Thus they predict inequivalent messenger depths and hierarchy exponents. Yet
the complete tested anomaly packet vanishes identically for both after the
same mirror-completion rule. The anomaly map therefore has a nontrivial
charge-gap kernel.

Deleting only the mirror of the third target port produces a nonzero exact
residual. This deliberate failure confirms that the checker is testing
cancellation rather than returning zero independently of its field content.

## Disposition

On the admitted mirror-completed domain, anomaly cancellation is a
compatibility condition and a completion rigidifier. It is not a selector of
the WP614 charge gaps. This does not prove that no anomaly theorem can select
\((3,2,0)\). It proves that selection requires an independently frozen chiral
spectrum or a rule forbidding the mirror kernel before anomaly equations are
invoked.

The result is the continuous-charge analogue of the earlier spectator-kernel
audit: faithfulness of the total anomaly on a complete source packet does not
imply faithfulness of its projection onto the flavor-charge block.

## Physical falsifier and remaining gate

The smallest exact falsifier of anomaly-only selection is already the hostile
pair above. The physical gate is sharper: resolve or exclude the conjugate
mirror quark doublets and the sector generating their masses. If a
source-derived representation theorem forbids those mirrors and freezes a
minimal chiral spectrum, its anomaly equations may regain selecting power and
must be recomputed on that smaller domain.

Anomaly cancellation itself has no detector instrument that distinguishes
the two charge-gap choices. The WP614 threshold test remains necessary:
resolve the flavon and the one-, two-, and three-insertion messenger paths in
one calibrated source/readout frame. A shorter 1--3 path still falsifies the
target hierarchy grammar directly.

## Reproduction

Run:

    uv run --offline python research/flavor/checkers/wp615_fn_anomaly_completion_kernel.py

The generated result is
`research/flavor/results/wp615_fn_anomaly_completion_kernel.json`.
