# Prior-research clues for the terminal pro-horn pullback

## Search result

The repository does not contain a source-derived `C24` counterprojection with

\[
\sup_L\|P_{\gamma,L}-V_{\gamma,L}\|_1<\infty.
\]

It does, however, contain a coherent alternative: retain the crossing atom as an independent moving boundary port and form the pullback in a rigged current/graph category rather than forcing it into the Plancherel bulk row.

## Clue 1: the missing coordinate already has a source type

`the-terminal-c13-node-must-retain-the-regular-current-the-moving-index-current-and-the-fixed-endpoint-graph.md` defines

\[
C_{13,7}^{aug}=(H_S^+,H_S^-,B_S,\mu_{reg,S},\mu_{idx,S},\beta_{end,S}).
\]

At a symmetry-completed crossing,

\[
\mu_{idx,0^\pm}=\mp(\delta_\gamma+\delta_{-\gamma}).
\]

Its source pairing is exactly the observer functional missing from the ordinary geometric volume row:

\[
\langle\mu_{idx},\overline{m_h}m_g\rangle
= m_g(\gamma)\overline{m_h(\gamma)}
 +m_g(-\gamma)\overline{m_h(-\gamma)}.
\]

Point masses are continuous in `H^{-s}(I)`, `s>1/2`, and globally in the declared weighted projective distribution carrier. Thus the desired atomic functional is already source typed, but on the terminal spectral current coordinate rather than on `C24`.

## Clue 2: the physical representative exists after moving-frame transport

`exact-hardy-recentering-transports-the-hostile-model-space-rotor-into-a-stationary-semilocal-cutoff-defect.md` represents a finite crossing by a rank-two model-space projection. Under exact Hardy recentering it has rank and trace equal to two, independently of `L`, and its observer compression converges to the two atomic evaluations.

This does not prove actual-Tate divisor provenance, but it gives the correct operator realization functor from an admitted moving index current to a physical cutoff defect.

## Clue 3: the fixed endpoint port cannot absorb the crossing port

`the-moving-real-boundary-rotor-decouples-from-the-fixed-completed-endpoint-graph-at-the-crossing-limit.md` proves that the coupling from the normalized rotor plane to evaluations at `z=+/-i/2` is `O(sqrt(b))`, and its pulled-back endpoint form is `O(b)`.

Therefore the existing fixed endpoint graph cannot be reused as the counter-row. A distinct moving real-boundary port is necessary.

## Clue 4: the correct bulk architecture is multi-port

`the-minimal-joint-boundary-reservoir-is-a-two-port-weyl-matrix-whose-cross-entry-is-the-evans-observer.md` shows that source incidence and endpoint evaluation must remain separate ports of a Weyl/Green reservoir. The same principle adds the crossing evaluation as a third port:

\[
J_{\gamma}^{\times}u=
(B_f^{\times}u,E_{end}u,E_{\gamma}u).
\]

The resulting matrix-valued Weyl function retains source autocorrelation, fixed endpoints, and moving crossing evaluation without identifying their observer functionals.

## Candidate pullback

The noncircular candidate is not a scalar subtraction on `H234`. It is the homotopy pullback

\[
\widetilde H_{234}
=
H_{234}^{reg/end}
\times_{\mathscr I_\partial}
H_{134}^{idx},
\]

where both maps land in the moving-index current carrier `mathscr I_partial`:

1. `H134_idx` sends the crossing projection to its atomic boundary current;
2. the enlarged geometry/Green reservoir has a dedicated moving evaluation port whose boundary trace is the same current;
3. the pullback witness is equality of these source-derived current distributions.

At finite crossing width the witness is the Poisson profile/model-space projection identity. At the crossing it is convergence to `delta_gamma+delta_-gamma` in `H^{-s}` or the strong Schwartz dual.

## What this bypasses

This pullback bypasses the trace-norm pro-horn by changing the terminal topology from the fixed physical trace-class bornology to the rigged current/graph topology in which translated finite-window representatives define one stationary current coordinate. It preserves the atomic observer functional rather than subtracting it.

It does **not** prove trace-norm convergence of the unrecentered physical projections. That no-go remains valid.

## Three-port Weyl architecture now constructed

Let

\[
J_\gamma^\times u=(B_f^\times u,E_{end}u,E_\gamma u),
\qquad
J_\gamma=(B_f,E_{end}^\times,E_\gamma^\times).
\]

On any common closed selfadjoint graph realization with resolvent `R_z`, set

\[
M_\gamma(z)=J_\gamma^\times R_zJ_\gamma.
\]

The resolvent identity gives

\[
M_\gamma(z)-M_\gamma(w)^*
=(z-\bar w)J_\gamma^\times R_w^*R_zJ_\gamma.
\]

Thus the moving index channel can coexist with source and fixed-endpoint ports in one Green identity without being identified with either. An exact rational three-port model, with independent ports and nonzero moving-port cross entries, is verified by:

- `research/voevodsky/checkers/check_three_port_moving_index_weyl_identity.py`;
- `research/voevodsky/results/three_port_moving_index_weyl_identity.json`.

This closes the algebraic architecture of the proposed pullback. It does not yet supply the actual-Tate moving port.

## Moving evaluation port on a graph rung

On `H^1(R)` define

\[
E_\gamma f=(f(\gamma),f(-\gamma)).
\]

With the unitary Fourier convention, Cauchy--Schwarz gives

\[
|f(x)|^2
\le
\frac1{2\pi}
\left(\int_{\mathbb R}\frac{d\xi}{1+\xi^2}\right)
\|f\|_{H^1}^2
=
\frac12\|f\|_{H^1}^2.
\]

Therefore

\[
\boxed{\|E_\gamma f\|_{\mathbb C^2}^2\le\|f\|_{H^1}^2}
\]

uniformly in the moving position `gamma`. Dagger exchanges the two coordinates, and a source successor acts diagonally by its two evaluation amplitudes. Combined with the local argument-principle theorem, a transverse zero/pole path supplies the Poisson current converging to the corresponding evaluation atom.

Artifacts:

- `research/voevodsky/checkers/check_moving_evaluation_port_graph_bound.py`;
- `research/voevodsky/results/moving_evaluation_port_graph_bound.json`.

Thus the abstract moving port and its uniform graph continuity are constructed. Its arithmetic label is source-derived whenever `gamma=x(0)`, multiplicity, and orientation come from a declared transverse divisor path of the scattering family.

## Canonical deformation derived from the fixed Tate multiplier

The missing deformation need not be externally invented. For the fixed meromorphic Tate multiplier `M`, define

\[
\mathcal S_a(z)=\frac{M(z+ia)}{M^\#(z-ia)}.
\]

For real `t`, the denominator is `overline{M(t+ia)}`, so `|mathcal S_a(t)|=1` wherever defined. A divisor point

\[
\rho=x+i\beta
\]

of `M` becomes a divisor point `x+i(beta-a)` of the shifted numerator. It crosses the real boundary transversely at the source-derived parameter `a=beta`, with normal velocity `-1`. The local argument-principle theorem then supplies its multiplicity, orientation, Poisson current, and delta-current limit without assuming a location theorem for the divisor.

Artifacts:

- `research/voevodsky/checkers/check_vertical_tate_scattering_deformation.py`;
- `research/voevodsky/results/vertical_tate_scattering_deformation.json`.

This supplies the actual-Tate moving labels locally, away from simultaneous collisions and poles; contour cutoffs isolate finite crossing packets.

## Uniform Green-to-evaluation bound

For the full-line translation generator `D=-i partial_t`, the Fourier multiplier of `R_z=(D-z)^-1` gives, on `|Re z|<=A` and `|Im z|>=eta>0`,

\[
\|R_zf\|_{H^1}^2
\le
\left(2+\frac{1+2A^2}{\eta^2}\right)\|f\|_2^2.
\]

Combining this with the uniform pair-evaluation estimate yields

\[
\|E_\gamma R_zf\|_{\mathbb C^2}^2
\le
\left(2+\frac{1+2A^2}{\eta^2}\right)\|f\|_2^2,
\]

uniformly in both the moving crossing location `gamma` and the vertical deformation parameter `a`. Existing research identifies the causal history descriptor with this full-line translation generator; the crossing deformation is therefore placed in the boundary port/current, not in an `a`-dependent singular bulk generator.

Artifacts:

- `research/voevodsky/checkers/check_green_resolvent_to_moving_evaluation_bound.py`;
- `research/voevodsky/results/green_resolvent_moving_evaluation_bound.json`.

## Index-current identification and current-level pasting

For multiplicity `m` and oriented normal velocity `sigma`, set

\[
A_\gamma=m\sigma(\delta_\gamma+\delta_{-\gamma}),
\qquad
J_{idx}=m\sigma I_2.
\]

Then, with the declared linear-first pairing convention,

\[
\boxed{
\langle A_\gamma,\overline{m_h}m_g\rangle
=
\langle E_\gamma g,J_{idx}E_\gamma h\rangle_{\mathbb C^2}.
}
\]

Thus the index block is exactly

\[
E_\gamma^*J_{idx}E_\gamma,
\]

not an arbitrary source--crossing Weyl transfer entry. For the vertical deformation, `sigma=-1`; the argument-principle jump is `Delta nu=-2A_gamma`. Dagger swaps the two port coordinates and preserves their symmetric Gram.

Artifacts:

- `research/voevodsky/checkers/check_moving_port_gram_equals_index_current.py`;
- `research/voevodsky/results/moving_port_gram_index_current.json`.

At the rigged-current level this closes the pullback square:

1. `H134_idx` maps the spectral crossing projection to `A_gamma`;
2. the enlarged `H234` maps its moving boundary port to `E_gamma^*J_idxE_gamma`, the same current form;
3. `H124` supplies the exact Hardy/physical transport of the finite-width model-space representative;
4. the local argument principle identifies its boundary limit and orientation.

Therefore the homotopy pullback is analytically admitted in the moving-current graph category. It does not promote the unrecentered physical projections to a trace-norm convergent family.

## Globalization and lattice registration

For the vertically shifted completed divisor, define the symmetry-completed oriented current

\[
\mu_{idx}
=
\sum_\rho m_\rho\sigma_\rho
(\delta_{\operatorname{Re}\rho}+\delta_{-\operatorname{Re}\rho}).
\]

Polynomial divisor counting implies `mu_idx in S'(R)_beta`; symmetric finite truncations converge strongly and uniformly on bounded Schwartz observer packets. Polynomially bounded successors preserve this class, and reflection preserves the symmetry-completed current. Finite collisions are handled by adjoining the limiting atom to the Poisson profile, so the current coordinate is continuous in the completed deformation chart.

The enriched parent pullback

\[
H_{234}^{reg/end/mov}
\times_{\mathscr I_\partial}
H_{134}^{idx}
\]

is transported through the edgewise subdivision by the same whiskering maps as the original signed parent tetrahedron. Since every elementary face label is a restriction of this one parent current, adjacent tetrahedra receive identical moving-current data on shared faces. Dagger and admitted successor naturality commute termwise with finite truncation and therefore with the strong-dual limit.

Aggregate artifact:

- `research/voevodsky/checkers/check_global_moving_current_pullback_contract.py`;
- `research/voevodsky/results/global_moving_current_pullback_contract.json`.

## Disposition

The pro-horn pullback is now globally constructed and subdivision-natural in the rigged-current/observer-localized category, under local finiteness and polynomial divisor counting. It does not assert an unlocalized trace-class infinite projection or all-path physical trace-norm convergence; those stronger statements remain false or unproved in the original carrier.
4. Show exact compatibility with `H124` physical transport and the `H234` relative trace.
5. Prove dagger, successor, and shared-face naturality.
6. Extend from finite crossings to locally finite divisor currents using the existing polynomial-counting theorem.

## Disposition

Prior research points to a viable pullback around the obstruction, but in a rigged moving-current category, not as a trace-class counterprojection on the old `C24` carrier. The first missing object is the actual-Tate moving evaluation port and its joint Green identity.
