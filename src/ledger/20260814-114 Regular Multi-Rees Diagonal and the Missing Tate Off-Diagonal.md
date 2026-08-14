# Regular Multi-Rees Diagonal and the Missing Tate Off-Diagonal

## Record

Date: 2026-08-14

Status: one proved coefficient theorem and one sharp blocker. Independent,
labelled Rees parameters give the smallest integral regular deformation that
retains all three Cartier \(\operatorname{Tor}_1\) lines. They do not produce
the nonzero off-diagonal \(1-r\) extension. The remaining construction is one
marked spatial extraordinary class \(\lambda_{\rm ex}\), not another carrier
cell or rational splitting.

## The regular coefficient deformation

A tempting common-parameter correspondence is

\[
A_t=
\mathbb Z[t,x_i,q_i^{\pm1}]
/
(q_i-1-tx_i),
\qquad i\in\{1,3,5\}.
\]

It is an integral deformation of the unit section of \(\mathbb G_m\), but it
is the wrong supported coefficient object. The pulled-back normal sequence

\[
(tx_1,tx_3,tx_5)
\]

is not regular because all three entries contain the same factor \(t\). Its
Koszul homology contains the nonzero class represented by

\[
z=x_3e_1-x_1e_3,
\]

with \(tz\) a boundary. Equivalently, the pulled-back support contains the
extra vertical component

\[
V(tJ_+)=V(t)\cup V(J_+).
\]

Removing that component by inverting \(t\) would erase the specialization
data. The common-parameter model is therefore rejected.

The regular replacement is the labelled multi-Rees correspondence

\[
\boxed{
A_{\rm mR}
=
\mathbb Z[t_i,x_i,q_i^{\pm1}]
/
(q_i-1-t_ix_i),
\qquad i\in\{1,3,5\},
}
\]

with \(D_3\) permuting the triples \((t_i,x_i,q_i)\). The sequence

\[
(t_1x_1,t_3x_3,t_5x_5)
\]

is regular. For the reciprocal packet,

\[
u_i^\vee=q_i^{-1}-1=-q_i^{-1}t_ix_i,
\]

and the integral Laurent-unit change

\[
\overline h_i^\vee=-q_i h_i^\vee
\]

gives

\[
d\overline h_i^\vee=t_ix_i p_i^\vee.
\]

Thus the original and reciprocal one-normal differentials have the same
regular multi-Rees diagonal. Applying the labelled \(x_i\)-Cartier maps
retains, rather than divides out, the three conormal lines \([t_i]\). This is
the canonical coefficient-level selection of the three occurrence
\(\operatorname{Tor}_1\) copies. No \(x_i\), \(u_i\), \(t_i\), or integer is
inverted.

This theorem is deliberately coefficient-level. The original and reciprocal
support variances and their endpoint pairing units remain explicit.

## The unique carrier shadow

At the carrier level, let \(P_{H_0}\) be the abstract three-tag module and
\(P_{\operatorname{Tor}_1}\) the abstract three-road module. Conditional on
a marked global identification of the actual local Cartier \(H_0\) and
\(\operatorname{Tor}_1\) lines with these two modules, integral
\(D_3\)-equivariance gives

\[
\operatorname{Hom}_{\mathbb Z[D_3]}
(P_{H_0},P_{\operatorname{Tor}_1})
=\mathbb Z(1-r).
\]

Saturation and the positive carrier orientations select the primitive
coefficient \(+1\). Hence the only possible fully based carrier target is

\[
\boxed{
0\longrightarrow\mathbb Z_{\rm or}
\xrightarrow{N_{\rm tag}}P_{H_0}
\xrightarrow{1-r}P_{\operatorname{Tor}_1}
\xrightarrow{\epsilon}\mathbb Z
\longrightarrow0.
}
\]

This classifies the entry-102 Tate window; it does not derive the marked
global identification from the multi-Rees diagonal. The generic class remains

\[
q_\Sigma=N_{\rm road}
\in P_{\operatorname{Tor}_1},
\qquad
\epsilon(q_\Sigma)=3.
\]

It is not identified with the reflection-odd tag norm.

The regular excess wedge also gives the integral evaluation/transfer pair

\[
\epsilon_{\rm ex}:P_{\rm tag}\to\mathbb Z_{\rm or},
\qquad
\Delta_{\rm ex}=\epsilon_{\rm ex}^{\vee},
\qquad
\epsilon_{\rm ex}\Delta_{\rm ex}=3.
\]

This pair is not a consecutive differential. If

\[
K=\ker\epsilon_{\rm ex},
\qquad
A_2^{\rm road}=\ker\epsilon,
\]

then the restriction

\[
(1-r)|_K:K\longrightarrow A_2^{\rm road}
\]

has Smith factors \((1,3)\). Therefore the split excess kernel is not the
saturated peripheral lattice. Identifying them would reintroduce exactly the
forbidden division by three.

## The missing off-diagonal class

Each established derived Cartier base change is split:

\[
R/(x_i)\otimes_R^L C
\simeq[C\xrightarrow0C].
\]

Consequently their direct sum has zero \(H_0\)-to-
\(\operatorname{Tor}_1\) differential. The multi-Rees equations select and
orient the coefficient lines, but they do not turn that zero differential
into \(1-r\). Inserting the carrier matrix at this point would fit the
desired answer.

The first unconstructed datum is therefore

\[
\boxed{
\lambda_{\rm ex}:
P_{\rm Cart,H_0}\dashrightarrow P_{\rm Cart,\operatorname{Tor}_1},
\qquad
\operatorname{gr}_{\rm car}\lambda_{\rm ex}=1-r,
}
\]

realized by a marked spatial multi-Rees extraordinary pull--push. It must
carry every \([t_i]\) line, reproduce the three entry-100 excess generators,
and be compatible with the actual support filtration and its Yoneda cone
roof.

At the integral carrier level the obstruction is now a single class

\[
\boxed{
\omega=ho(e_F)-\beta_\triangle
\in
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})
\simeq\mathbb Z/3.
}
\]

The identity \(\epsilon(q_\Sigma)=3\) proves only that three times any such
obstruction vanishes; it does not prove \(\omega=0\). If \(\omega=0\), the
coherent lifts form a torsor under

\[
\operatorname{Ext}^1_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})
\simeq\mathbb Z/2.
\]

The positive normal and whole-gallery orientations are the candidate
geometric datum that should select this parity coherence. They cannot be
used until \(\lambda_{\rm ex}\) itself has been constructed.

## Evidence

New exact certificate:

- `research/voevodsky/check_positive_cartier_tate_costalk.rs`, SHA-256
  `3820fe6ce63cae922aba86151867d787ca781a48d3c112832918f84ee880ccab`.

The checker proves the conditional carrier Hom classification, exact abstract
Tate window,
dihedral signs, common-parameter torsion, regular multi-Rees diagonal,
reciprocal normalization, retention of the Rees conormal lines, the
\((1,3)\) excess-lattice Smith obstruction, and failure of a strict extension
diagram morphism. Entries 100, 102, 105, 112, and 113 supply the inherited
local traces, Tate class, absolute filtration, whole-gallery maps, and mixed
generic/special block.

Reproduce with `rustfmt --check`, `rustc --edition 2021 -D warnings -O`, and
execution of the certificate. Its JSON result and `git diff --check` pass.

## Boundary and consequence

- The multi-Rees correspondence is not an identity-base substitution between
  independent occurrence and monodromy variables.
- It proves a regular coefficient diagonal, not the spatial Beck--Chevalley
  transformation.
- The inherited \(1-r\) carrier is classified uniquely but is not thereby
  lifted to the split local costalks.
- Ordinary restriction of \(e_F\) remains zero, while the desired local tuple
  is nonzero.
- No full \(G_{03}^{\rm Cousin}\), negative-sheet assembly, physical-Cut
  theorem, or CHY identification follows yet.

The next discriminating experiment is singular: construct
\(\lambda_{\rm ex}\) on one marked multi-Rees support correspondence, compute
\(\omega\), and, only if it vanishes, use the positive orientation to test the
remaining parity coherence. Rotation then supplies the other two roads.

## Outcome contract

```json
{
  "claim": "Independent D3-permuted Rees parameters give a regular integral coefficient diagonal q_i-1=t_i x_i that retains every Cartier Tor1 and conormal line; a common parameter is nonregular. The unique possible carrier extension is the full N_tag/(1-r)/epsilon Tate window, but the multi-Rees coefficient geometry does not construct its off-diagonal 1-r Beck-Chevalley class.",
  "status": "inconclusive",
  "assumptions": [
    "The ordinary Cartier tag maps and orientations are those of entries 100 and 112.",
    "Occurrence, monodromy, Rees, and integer parameters remain uninverted.",
    "The coefficient diagonal is not promoted to a spatial correspondence without an explicit extraordinary pull-push."
  ],
  "evidence_refs": [
    "research/voevodsky/check_positive_cartier_tate_costalk.rs",
    "ledger entries 100, 102, 105, 112, and 113"
  ],
  "factorization_test": {
    "common_parameter": "falsified by nonregular t-torsion",
    "multi_Rees_diagonal": "proved regular and D3-equivariant",
    "Tor1_and_conormal_lines": "retained",
    "carrier_extension": "unique candidate N_tag/(1-r)/epsilon window after the unconstructed marked global identification",
    "excess_kernel_to_peripheral": "Smith (1,3), not an isomorphism",
    "lambda_ex": "unconstructed",
    "omega_in_Z_mod_3": "uncomputed",
    "parity_torsor": "unselected",
    "full_G03_Cousin": "unconstructed"
  },
  "counterevidence": [
    "The local derived Cartier packets are split and contain no intrinsic 1-r differential.",
    "The excess augmentation and its dual norm are an evaluation/transfer pair, not consecutive Tate differentials.",
    "The literal support restriction of e_F is zero."
  ],
  "next_experiment": "Construct the marked spatial multi-Rees extraordinary class lambda_ex with carrier 1-r, then compute rho(e_F)-beta_triangle and the residual parity coherence while retaining q_Sigma."
}
```
