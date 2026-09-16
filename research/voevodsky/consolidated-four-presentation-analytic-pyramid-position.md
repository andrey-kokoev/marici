# Consolidated position: the four-presentation analytic pyramid

## Scope

This note consolidates the reversible presentation geometry. It distinguishes the faithful fourth presentation from its scalar finite-part readout and separates presentation coherence from positivity and completion questions.

## Four vertices

Fix the admitted observer source \(\mathsf{Obs}_S\).

### \(V_1\): source

\[
V_1=\mathsf{Obs}_S.
\]

A point is an observer \(g\), with polarized convolution observations retained as needed.

### \(V_2\): semilocal geometry

\[
V_2^{obs}=\operatorname{im}U_S.
\]

A point is an observer-generated scaling operator

\[
U_S(g).
\]

### \(V_3\): compatible canonical--dual spectrum

\[
V_3^{obs}
=
\operatorname{im}(\Omega_S^+,\Omega_S^-).
\]

A point is a compatible pair

\[
(\Omega_S^+g,\Omega_S^-g).
\]

### \(V_4\): complete response

The faithful fourth chart is

\[
V_4^{resp}=\operatorname{im}\mathscr R,
\]

where

\[
\mathscr R(g)
=(B_g,Q_g,A_g,C_g),
\]

\[
B_g(a)=g(a),
\qquad
Q_g(a)=\widehat g(a),
\]

\[
A_g(a)=\int_{-\infty}^{a}g(x)dx,
\qquad
C_g(a)=\operatorname{pv}\int
\frac{e^{-2\pi iax}g(x)}x dx.
\]

The all-seam flux coordinate satisfies

\[
B_g=g.
\]

The scalar finite-part Weil/trace functional is a readout of this presentation. It is not the fourth chart itself because it is not faithful.

## Four source charts

Define

\[
S_1g=g,
\]

\[
S_2g=U_S(g),
\]

\[
S_3g=(\Omega_S^+g,\Omega_S^-g),
\]

\[
S_4g=\mathscr R(g).
\]

Their inverses on essential images are:

\[
R_1=I,
\]

\[
R_2(T)
=\mathcal F_{C_S}^{-1}(\sigma_T),
\qquad
\mathcal F_{C_S}T\mathcal F_{C_S}^{-1}=M_{\sigma_T},
\]

\[
R_3(\xi^+,\xi^-)
=(\Omega_S^+)^{-1}\xi^+
=(\Omega_S^-)^{-1}\xi^-,
\]

\[
R_4(B,Q,A,C)=B.
\]

Thus

\[
R_iS_i=I_{\mathsf{Obs}_S},
\qquad
S_iR_i=I_{V_i^{obs}}.
\]

## Complete stock of directed edges

For every ordered pair \(i\ne j\), define

\[
\boxed{C_{ij}=S_jR_i.}
\]

| Edge | Constructor |
|---|---|
| \(C_{12}\) | \(g\mapsto U_S(g)\) |
| \(C_{21}\) | \(T\mapsto\mathcal F_{C_S}^{-1}(\sigma_T)\) |
| \(C_{13}\) | \(g\mapsto(\Omega_S^+g,\Omega_S^-g)\) |
| \(C_{31}\) | \((\xi^+,\xi^-)\mapsto(\Omega_S^+)^{-1}\xi^+\) |
| \(C_{14}\) | \(g\mapsto\mathscr R(g)\) |
| \(C_{41}\) | \((B,Q,A,C)\mapsto B\) |
| \(C_{23}\) | \(T\mapsto S_3R_2T\) |
| \(C_{32}\) | \((\xi^+,\xi^-)\mapsto U_S(R_3(\xi^+,\xi^-))\) |
| \(C_{24}\) | \(T\mapsto\mathscr R(R_2T)\) |
| \(C_{42}\) | \((B,Q,A,C)\mapsto U_S(B)\) |
| \(C_{34}\) | \((\xi^+,\xi^-)\mapsto\mathscr R(R_3(\xi^+,\xi^-))\) |
| \(C_{43}\) | \((B,Q,A,C)\mapsto(\Omega_S^+B,\Omega_S^-B)\) |

All are analytic chart transitions for the declared essential-image topologies.

## Single inner bulk

Define the joint graph

\[
\boxed{
\mathcal B_S
=\operatorname{im}\Psi_S,
}
\]

with

\[
\boxed{
\Psi_S(g)
=
\left(
S_1g,S_2g,S_3g,S_4g
\right).
}
\]

The four chart projections are

\[
\pi_i:\mathcal B_S\to V_i^{obs}.
\]

They satisfy

\[
C_{ij}=\pi_j\pi_i^{-1}.
\]

Thus \(\mathcal B_S\) is one analytic object realizing the entire inner presentation bulk.

## Strict coherence

Every triangle commutes strictly:

\[
C_{jk}C_{ij}
=S_kR_jS_jR_i
=S_kR_i
=C_{ik}.
\]

Every tetrahedral route reduces to

\[
C_{i\ell}=S_\ell R_i.
\]

Hence the inner tetrahedral coherence follows from ordinary associativity of chart transition.

## Scalar readout

Let

\[
\rho_4:V_4^{resp}\to\mathbb C
\]

denote the completed Weil/finite-part trace readout. Then the old scalar fourth presentation is

\[
V_4^{scalar}=\rho_4(V_4^{resp}).
\]

The map \(\rho_4\) is generally noninjective. Therefore:

- \(V_4^{resp}\) supports \(C_{41},C_{42},C_{43}\);
- \(V_4^{scalar}\) does not.

No reverse constructor should be attributed to the scalar shadow.

## Edgewise subdivision status

The complete twelve-edge presentation tetrahedron is constructed on essential images. This does not automatically identify arbitrary analytic stage labels on independently chosen eight-node edge factorizations.

Current fine-stage status:

- \(C_{13}\): explicit eight-node factorization;
- \(C_{24}\): explicit eight-node factorization;
- \(C_{12}\): stagewise geometric transport along the \(H_{123}\) triangulation, now assembled as an enriched chain;
- \(C_{14}\): one observer-valued path, but its segment numbering is not uniformly aligned;
- \(C_{34}\): relative/signed factorization exists, with stronger positive realizations requiring their declared regulator topology;
- \(C_{23}\): supplied analytically by the compatible Hardy--Titchmarsh chart transition, but no independently standardized eight-node segmentation has been fixed.

Therefore the bulk tetrahedron is analytically coherent while a canonical uniform semantic interpretation of all 120 edgewise-subdivision nodes remains a separate refinement problem.

## Positivity boundary

Reversibility of presentation charts does not prove positivity of the scalar Weil form. The positive phase-energy boundary, physical cutoff comparison, radical descent, and Sonin Green channel are additional structures.

They must not be conflated with existence of the presentation bulk.

## Authoritative dependencies

- `c21-is-fourier-inversion-on-the-observer-generated-geometric-image.md`
- `c31-is-unitary-reconstruction-from-the-compatible-canonical-dual-pair.md`
- `c32-is-the-unitary-spectral-inverse-followed-by-the-integrated-representation.md`
- `all-seam-flux-makes-the-function-valued-v4-faithful-and-gives-an-analytic-c41.md`
- `the-complete-response-retract-closes-local-seam-endpoint-stability-and-radical-descent-for-the-resolved-joint-graph.md`
- `source-derived-fourier-sewing-identification-closure-ledger.md`

## Disposition

The consolidated analytic presentation is

\[
\boxed{
\mathcal B_S
\cong
V_1^{obs}
\cong
V_2^{obs}
\cong
V_3^{obs}
\cong
V_4^{resp},
}
\]

with all twelve directed chart transitions and strict triangular and tetrahedral coherence. The scalar finite-part trace is a nonfaithful terminal readout, not a reversible vertex chart.
