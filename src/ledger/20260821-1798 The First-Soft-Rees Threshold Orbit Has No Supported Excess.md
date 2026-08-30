# 1798 — The First-Soft-Rees Threshold Orbit Has No Supported Excess

## Question

Entry 1797 leaves one first-soft-Rees logarithmic class at the
total-energy/site-soft boundary of a representative physical threshold. Does
cyclic assembly leave an additional supported class?

## Labelled specialization

Entry 1794 identifies the generic logarithmic lines as one free regular
\(C_5\)-orbit:

\[
\mathcal V_{\log}\simeq\mathbb Q[C_5].
\]

Entry 1797 produces one nonzero first-Rees line at the corresponding labelled
soft corner. Cyclic transport produces five such lines:

\[
\mathcal V_{\rm soft}^{(1)}\simeq\mathbb Q[C_5].
\]

The source \(i0\) orientation, residue order, and radial leading coefficient
are transported simultaneously. Consequently the specialization has the
form

\[
\operatorname{Sp}^{(1)}_{\rm soft}
=
c\,I_5,
\qquad c\neq0.
\]

The common unit \(c\) is irrelevant to kernel and cokernel and is not fitted
occurrence by occurrence.

## Exact cone

The specialization commutes with the cyclic generator and has rank five:

\[
\ker\operatorname{Sp}^{(1)}_{\rm soft}=0,
\qquad
\operatorname{coker}\operatorname{Sp}^{(1)}_{\rm soft}=0.
\]

Therefore

\[
\boxed{
H^\bullet\operatorname{Cone}
\left(
\mathcal V_{\log}
\xrightarrow{\operatorname{Sp}^{(1)}_{\rm soft}}
\mathcal V_{\rm soft}^{(1)}
\right)
=0.
}
\]

## Result

The first-soft-Rees orbit is exactly the boundary specialization of the
generic logarithmic orbit. It leaves no supported kernel, cokernel, or
non-regular cyclic character.

This closes the total-energy/site-soft boundary of the physical five-site
threshold within the tested source family:

\[
\text{existing carrier corner}
+
\text{existing Rees specialization}
+
\text{sector-specific logarithmic coefficient}.
\]

No new carrier or coherence generator is required.

## Next falsifier

Move from total-energy support to the independent one-wall closure
intersections of \(\mathscr D_{g_5}\). Determine whether the generic
logarithmic line remains Morse, moves to a higher Rees grade, or is killed by
an occurrence character.

## Evidence

- research/benincasa/checkers/five_site_g5_soft_rees_orbit_cone.py
- research/benincasa/results/five-site-g5-soft-rees-orbit-cone.json
- Entries 1794 and 1797
- allocator claim: seqclaim-dd6460e4765366bc454c51af
