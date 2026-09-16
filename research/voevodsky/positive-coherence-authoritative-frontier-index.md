# Positive coherence: authoritative frontier index

## Purpose

This index freezes the latest noncontradicted state of the semilocal positive-coherence programme. It separates established constructions, conditional implications, corrected routes, and genuinely open theorems.

The repository's Voevodsky notes were largely accumulated in checkpoint commits, so Git commit order does not provide a reliable note-by-note chronology. Authority below is determined by explicit correction links, dependency statements, and mathematical compatibility.

## 1. Signed asymptotic tetrahedron — closed

The signed semilocal realization is complete in the rapid-decay asymptotic quotient:

\[
[V_{\mathrm{loc},S}]
=[M_{-\log|x|_S}]
=[W_S]
=[\mathfrak T_{\Lambda,S}].
\]

All \(343=7^3\) cells of the seventh edgewise subdivision commute in the signed asymptotic category.

Authoritative notes:

- `the-uniform-seventh-edgewise-subdivision-is-well-typed-for-signed-asymptotic-realizations-but-not-for-positive-feature-realizations.md`
- `the-recovered-face-234-is-an-admissible-invertible-modification-in-the-rapid-decay-asymptotic-quotient.md`

This result does not imply a positive Hilbert-feature filler.

## 2. Canonical signed-to-positive local decomposition — closed

The logarithmic-module operator has the canonical layer decomposition

\[
M_{-\log|x|_S}
=(\Phi_S^{in})^*\Phi_S^{in}
-(\Phi_S^{out})^*\Phi_S^{out}.
\]

The regular Tate/reference deformation has the exact observer-weighted phase-energy Gram

\[
\|[P,M_\gamma]M_m\|_{HS}^2
=
\int\kappa_\gamma(t)|m(t)|^2dt.
\]

For a finite place set, use the placewise orthogonal energy

\[
e_S(\chi,t)
=1+\sum_{v\in S}\kappa_{v,\chi}(t).
\]

Authoritative notes:

- `the-logarithmic-module-operator-is-the-difference-of-two-canonical-positive-layer-cake-towers.md`
- `the-relative-difference-row-norm-is-the-positive-h-half-phase-energy-of-the-tate-symbol.md`
- `placewise-telescoping-of-tate-projection-pairs-gives-a-strict-local-energy-completion.md`

## 3. Global source-derived boundary Hilbert space — closed

The positive graph completion is

\[
\mathscr E_S
=
\bigoplus_\chi
L^2\left(
\mathbb R,
e_S(\chi,t)\frac{dt}{2\pi}
\right).
\]

On this space the normalized Tate multiplier

\[
\mathcal A_S=M_{w_S/e_S}
\]

is bounded and self-adjoint. Its global two-polarity feature is

\[
\Phi_S^{energy}(m)
=
\left(
\mathcal A_{S,+}^{1/2}m,
\mathcal A_{S,-}^{1/2}m
\right).
\]

Finite-character Mellin--Schwartz observers form a dense core.

Authoritative notes:

- `the-local-phase-energy-completion-turns-the-tate-form-into-a-bounded-self-adjoint-multiplier.md`
- `finite-character-mellin-schwartz-observers-are-dense-in-the-local-phase-energy-completion.md`
- `the-bounded-phase-energy-multiplier-admits-an-asymptotically-reducing-finite-packet-filtration.md`

This constructs the limiting positive boundary realization. It does not prove convergence of raw physical cutoff features to it.

## 4. Finite-cutoff polarized cell — internal commutativity closed; external Widom comparison separate

The transported eight-leg feature with fixed Krein signature gives global, packet-natural positive legs whose **difference** is the centered signed regulator:

\[
\widehat G_\alpha^T-
\widehat G_\alpha^0=D_\alpha.
\]

Unequal left/right placements are handled by Hadamard common/difference doubling.

At one lattice coordinate \(\alpha\), the Tate- and reference-polarized sub-tetrahedra are two polarizations of the same regulated relative-feature cell. With `physical` interpreted internally as this transported cell feature, their common face is part of the cell datum. Writing its feature as \(B_\alpha\), strict cell commutativity gives

\[
G_{cell,\alpha}^T
=B_\alpha^*B_\alpha+
\widehat G_\alpha^T,
\qquad
G_{cell,\alpha}^0
=B_\alpha^*B_\alpha+
\widehat G_\alpha^0,
\]

and therefore

\[
\boxed{
G_{cell,\alpha}^T-
\widehat G_\alpha^T
=
G_{cell,\alpha}^0-
\widehat G_\alpha^0
=B_\alpha^*B_\alpha
\succeq0.
}
\]

This is the local commuting 2-cell between differently polarized sub-tetrahedra at the same lattice coordinate. It is not an additional asymptotic theorem.

A distinct question arises only if \(G_{phys,\alpha}^{T,0}\) is reserved for an **external**, independently normalized prolate/Widom realization. The signed analytic Cech tetrahedron does not identify that external realization with the internal positive cell, because the forgetful map from positive pairs to signed forms loses common summands. Comparison with external Widom Grams remains a separate isometric-lifting theorem and must not be described as failure of lattice-cell commutativity.

Authoritative notes, in correction order:

- `the-transported-eight-leg-krein-readout-gives-an-exact-global-positive-regulator-alignment.md`
- `fixed-krein-splitting-realizes-the-signed-form-but-does-not-identify-the-physical-widom-grams.md`
- `the-analytic-cech-tetrahedron-does-not-by-itself-lift-to-the-positive-polarized-cell.md`

The second note applies only to the external-Widom reading; it does not reopen the internal polarized cell.

## 5. Correct extensive reference edge — closed

For the one-sided pure Hardy reference pair, the projections are nested. The \(2L\) mass lies in the exact Halmos mismatch strip \(H_{10}\) or \(H_{01}\), not in a generic dyadic prolate defect:

\[
\| (I-P)M_{e^{2iLs}}PM_m\|_{HS}^2
=2L\|m\|_{Pl}^2.
\]

Authoritative correction:

- `correction-the-two-L-pure-hardy-strip-is-an-exact-mismatch-sector-not-the-first-prolate-defect.md`

Any argument assigning the pure \(2L\) term to \(B(I-B)\) or to a classical Widom plunge is superseded.

## 6. Finite observer packets — closed after the declared alignment and coercivity inputs

On a fixed coercive packet, bounded centered convergence and the extensive common edge permit exact common-edge removal. The residual absolute Gram converges to the packet restriction of \(|\mathcal A_S|\).

Authoritative notes:

- `bounded-relative-gram-convergence-transfers-the-reference-widom-law-to-the-tate-regulator.md`
- `common-widom-edge-removal-closes-the-absolute-gram-gate-on-every-coercive-finite-packet.md`

Interpret the common reference edge using the corrected mismatch-strip geometry from section 5, not the obsolete pure-defect interpretation.

Finite-packet closure does not globalize by taking packetwise Jordan parts.

## 7. Global physical common-edge extraction — obstructed, not closed

Exact alignment alone does not imply

\[
(D_\alpha)_+\preceq G_\alpha^T.
\]

Noncommuting near-null modes give a two-dimensional counterexample. Exact physical extraction is equivalent to the Douglas dominations

\[
(D_\alpha)_+\preceq G_\alpha^T,
\qquad
(D_\alpha)_-\preceq G_\alpha^0.
\]

Diagnostic notes:

- `global-common-edge-removal-is-equivalent-to-two-source-douglas-dominations.md`
- `noncommuting-near-null-modes-are-the-exact-obstruction-to-global-common-edge-removal.md`

These are criteria and obstructions, not proofs that the dominations hold for the semilocal physical regulators.

## 8. Compact-tail globalization route — false

The phase-energy identity makes the Tate--Hankel map bounded, but generally noncompact. Disjointly supported normalized observers produce orthogonal Hilbert--Schmidt images.

Therefore no finite-rank filtration can satisfy

\[
\|[P,M_\gamma]M_{(I-P_n)\cdot}\|
\to0
\]

in operator norm on the phase-energy unit ball.

Authoritative correction:

- `correction-the-tate-hankel-map-is-bounded-on-phase-energy-but-not-filtration-compact.md`

The following note remains useful only for its fixed-packet angle estimate; its proposed filtration-compact global continuation is superseded:

- `the-pure-hardy-mismatch-strip-is-asymptotically-common-under-a-bounded-tate-hankel-perturbation.md`

## 9. Actual global convergence frontier — open

The viable global theorem is direct closed-form convergence of centered relative forms on the phase-energy completion, not uniform compact removal of a physical common strip.

Required evidence:

1. a regulator-independent dense common core;
2. pointwise centered-form convergence on that core;
3. regulator-uniform phase-energy graph bounds;
4. weak lower semicontinuity/liminf control;
5. recovery sequences in the phase-energy topology;
6. endpoint and radical stability;
7. separate treatment of the Sonin sector.

The repository already has the abstract admission interface for exactly this evidence:

- `coherence-pyramid-completion-interface.md`
- `coherence-pyramid-completion-interface.json`
- `checkers/check_coherence_pyramid_completion_interface.py`

That interface explicitly does not construct Mosco convergence. It refuses completion when the evidence is absent.

The current open theorem can be stated as:

\[
\underset{\alpha}{\operatorname{Mosco\!-\!lim}}\;
q_\alpha^{relative}
=
q_{|\mathcal A_S|}
\quad
\text{on }\mathscr E_S.
\]

with the endpoint and Sonin channels adjoined according to their independent source forms.

## 10. Sonin channel — signed form and endpoint coupling closed; positivity open

The standard Sonin atom is

\[
H_{00}=\ker P\cap\ker Q,
\]

not \(H_{11}=\operatorname{ran}P\cap\operatorname{ran}Q\).

Later work closes the formerly open signed seam in three steps:

1. restriction of the Euler connection gives the source-natural signed Sonin Green form;
2. the form is closed on the absolute-connection graph domain;
3. reflected contour deformation identifies its endpoint term with the independently constructed endpoint Green bundle.

Authoritative notes:

- `the-euler-connection-restricts-to-a-source-natural-signed-sonin-green-form.md`
- `the-sonin-green-form-is-closed-in-the-absolute-connection-graph-norm.md`
- `the-reflected-contour-green-identity-identifies-the-two-source-pullbacks-of-the-augmented-coupling.md`

The resulting augmented signed operator is

\[
\mathbb G_S=
\begin{pmatrix}
\mathcal A_S&B_S^*\\
B_S&J_{end}
\end{pmatrix}.
\]

Its construction and successor naturality are closed. Positivity is not. After the declared parity/polarity reduction, the remaining condition is the Schur--Douglas inequality

\[
\boxed{C_k\succeq b_kb_k^*.}
\]

This metric inequality, rather than existence of the Sonin Green map, is the active channel-3/4 gate.

Two proposed proof routes are already excluded:

- dyadic Halmos refinement is isometric and conserves the total Gram, so it supplies no new positive capacity for an induction;
- scalar similarity by a Sonin/Euler weight commutes with the reflected multiplier and cannot reduce its essential norm.

The Schur gate must therefore be formulated in the source-derived two-space canonical/dual pairing. Its next admissible form is a positive factorization of the differentiated paired connection, with the endpoint row attached through the constructed reflected-contour coupling.

## 11. Notes that are auxiliary rather than frontier-setting

### Finite-window reference only

- `the-universal-logarithmic-divergence-has-an-exact-folner-module-feature-and-orthogonal-residual.md`

This is an exact regular finite-window model. It is not the actual one-sided Connes cutoff feature.

### Conditional finite-packet machinery

- `normalized-gram-convergence-gives-eventual-douglas-equivalences-on-every-finite-observer-packet.md`

The implication is valid. Earlier proposed proofs of its normalized-convergence hypothesis using a bare transition Hilbert--Schmidt norm were corrected.

### Superseded bare-transition estimate

- `polynomial-characterwise-prolate-growth-and-rapid-observer-boundary-decay-give-an-o-log-sewing-bound.md`

Its own subsequent-correction section withdraws the bare transition argument.

Authoritative correction:

- `correction-the-characterwise-bare-hardy-transition-is-not-hilbert-schmidt-so-the-sqrt-log-sewing-bound-is-unproved.md`

### Two-cutoff Gram regulator

- `correction-the-full-semilocal-two-by-two-gram-block-requires-a-second-volume-cutoff-because-the-outside-leg-is-not-hilbert-schmidt.md`
- `the-regulated-positive-gram-block-requires-a-two-copy-channelwise-bulk-counterterm-not-one-outer-window-bulk.md`

These remain authoritative for finite-regulator typing. They do not provide the completed positive boundary by themselves.

## 12. Frozen next actions

No further positive-coherence note should be added unless it addresses one of these two independent open theorems:

### Regular boundary completion

Prove or falsify

\[
\underset{\alpha}{\operatorname{Mosco\!-\!lim}}\;
q_\alpha^{relative}
=
q_{|\mathcal A_S|}.
\]

using the six evidence classes required by `complete_finite_form_system`.

The immediate first task is to define the exact candidate family \(q_\alpha^{relative}\) on the common Mellin--Schwartz core and audit whether existing centered regulator comparison supplies pointwise convergence and a uniform \(\mathscr E_S\)-bound.

### Positive Sonin/endpoint coupling

With the signed augmented coupling already constructed, prove or falsify the parity-reduced Schur--Douglas condition

\[
C_k\succeq b_kb_k^*,
\]

including successor naturality of its contraction. This is a positivity theorem, not a missing Green-map construction.

These gates must remain separate.

## Disposition

The stable frontier is:

\[
\boxed{
\begin{array}{l}
\text{signed asymptotic coherence: closed},\\
\text{source-derived phase-energy boundary: closed},\\
\text{finite-cutoff positive alignment: closed},\\
\text{fixed finite-packet absolute Gram: closed},\\
\text{global physical compact-tail extraction: false},\\
\text{direct phase-energy Mosco convergence: open},\\
\text{Sonin signed Green/endpoint seam: closed},\\
\text{Sonin--endpoint positive Schur gate: open}.
\end{array}}
\]
