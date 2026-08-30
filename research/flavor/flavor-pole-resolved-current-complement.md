# Pole-resolved flavor-current complement: WP456

## Question

How does the WP453 hostile current coefficient decompose across WP448's independently frozen triplet and quintet poles, and where may WP449's widths legally enter?

## Exact source-derived ports

Keep the WP447 vacuum fixed and use WP453's rotated hostile Yukawa pair. For the mass-basis (1 to 2) transition, let (v_a) be the eight complex generator entries. Contracting this transition bilinearly with the two source projectors gives

\[
v^TP_1v=-\frac14,
\qquad
v^TP_3v=\frac14.
\]

These are Delta-F equals two amplitude residues, not positive spectral probabilities; the transpose is required because the four-quark amplitude contains two same-orientation transition currents.

The pole-resolved response before the overall current-current sign is

\[
\mathcal A_{12}(s)=\frac{g_F^2}{4}
\left[
-\frac1{s-g_F^2\mu^2}
+\frac1{s-3g_F^2\mu^2}
\right].
\]

The two residue coordinates sum to zero. Consequently the leading (1/s) term cancels at high energy, but the unequal pole masses retain a nonzero low-energy response:

\[
v^TK^{-1}v=-\frac14+\frac1{12}=-\frac16.
\]

This reproduces WP453 exactly. A projection that merges the poles before preserving their mass labels loses the information; either resolved pole is a source-derived complementary port for the other.

## Width typing

WP449 independently freezes the conditional leading ratio

\[
\alpha=\frac{\Gamma_r}{m_r}=\frac{g_F^2}{4\pi}
\]

for both multiplets. Near the poles, the declared fixed-width model gives

\[
\mathcal A_{12}^{\rm pole}(s)=\frac{g_F^2}{4}
\left[
-\frac1{s-(1-i\alpha)g_F^2\mu^2}
+\frac1{s-3(1-i\alpha)g_F^2\mu^2}
\right].
\]

This is a resonance-domain line shape only. Extending it to (s=0) would multiply the exact real Wilson response by (1-i\alpha)^{-1}. That spurious absorptive term contradicts the tree-level zero-momentum matching and therefore marks the boundary of the fixed-width approximation. Low-energy kaon matching uses WP448's real inverse mass kernel; collider line shapes may use WP449's widths only on their declared near-pole support.

## Contextual partition and classification

On the WP453 hostile pair, the pole-resolved current family distinguishes the two extended-theory orientations even though `physical16` does not. For the rotated member it additionally distinguishes the triplet and quintet contributions. It is a source-derived complementary probe family, neither a vacuum selector nor a presentation rigidifier.

No reference port has been added. A resolved collider scan would be a new high-energy experiment but would measure relational pole locations, widths, and flavor-tagged residues already defined by the source action. Executable control and detector reach remain unproved.

## Smallest exact falsifiers

- Either transition residue differs from (-1/4,+1/4).
- Their mass-weighted sum fails to reproduce (-1/6).
- A single unresolved residue is claimed to reproduce both pole neighborhoods.
- A constant-width continuation is used at zero momentum without producing the forbidden imaginary Wilson coefficient.

The remaining physical-instrument gate is a detector-level flavor-tagged two-pole response with resolution, luminosity, backgrounds, and support uncertainties frozen independently of the desired rank.
