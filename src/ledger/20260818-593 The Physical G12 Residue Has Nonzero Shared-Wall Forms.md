---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Physical G12 Residue Has Nonzero Shared-Wall Forms

## Residue form

After the (q_{G_{12}}) residue, the source-unsplit denominator form is

\[
\omega_{m phys}
=
\frac{da\wedge db}
{\sqrt{K_E}\,q_{g_1}q_{g_2}q_{g_3}}
\left(\frac1{q_{g_{23}}}+\frac1{q_{g_{31}}}\right).
\]

Entry 591 proves cancellation on the occurrence exceptional divisor.  Entry
592 shows that descent to the q-only nine-master module additionally requires
the localization residues on the three shared walls.

## Exact wall numerators

Combining the two occurrence fractions before taking residues gives

\[
\frac{q_{g_{23}}+q_{g_{31}}}{q_{g_{23}}q_{g_{31}}}.
\]

On the three shared walls its numerator restricts to

\[
\begin{array}{c|c|c}
\text{wall}&\text{restriction}&\text{residue orientation}\\
\hline
q_{g_1}=0&a+z-x&-da\\
q_{g_2}=0&b+z-y&+db\\
q_{g_3}=0&-E&+db.
\end{array}
\]

All three are nonzero at generic nonsoft kinematics.  Thus the source sum
does not cancel the shared-wall residues at the level of logarithmic forms.

## Narrow conclusion

There is no regular form-level removal of all lower walls.  In particular,
the occurrence cancellation of Entry 591 is not sufficient to produce a
q-only representative.

This does not yet prove that the localization boundary is nonzero in
cohomology.  Each wall restriction lies on a reducible double-cover curve;
its one-form may be exact after normalization, and different conductor/node
values may cancel in the Čech complex.  The remaining calculation is exactly
the normalization/conductor reduction

\[
\bigoplus_i H^1(W_i)(-1)
\longrightarrow
\bigoplus_{i<j}H^0(W_i\cap W_j)(-2).
\]

If the resulting class survives, the physical residue is intrinsically
relative and has no canonical infinity-Gysin image.  If it dies, the
resulting q-only lift is the first admissible input to (R_\infty).

## Evidence

- `research/benincasa/physical_g12_shared_wall_residues.py`;
- `research/benincasa/physical-g12-shared-wall-residues.json`;
- Entries 591--592.

## Outcome contract

~~~json
{
  "claim": "The source-unsplit occurrence sum cancels the logarithmic residues on all three shared lower walls.",
  "status": "falsified",
  "shared_wall_numerators": ["a+z-x", "b+z-y", "-E"],
  "generic_form_level_residues_nonzero": 3,
  "cohomological_localization_boundary_computed": false,
  "next_experiment": "Reduce the three wall one-forms on their normalization/conductor complexes and compute the Cech-compatible localization class."
}
~~~
