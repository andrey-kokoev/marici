# Tate naturality closes on coefficients but not yet on support

Date: 2026-08-23

## Coefficient square

Both the cosmological cyclic soft star and the string road/contact extension
use the integral augmentation lattice

\[
I_{\mathbb Z}=\ker(\mathbb Z[C_3]\to\mathbb Z)
\]

and its coinvariant quotient

\[
T=I_{\mathbb Z}/(g-1)I_{\mathbb Z}\cong\mathbb Z/3.
\]

On the cosmology side, cyclic soft specialization is the identity on the
three labelled integral generators and therefore induces \(1_T\).  The
canonical Tate bridge is the identity between the two augmentation-ideal
presentations.  Consequently the coefficient square

\[
\begin{CD}
T_{\rm cosm} @>{\overline G_{\rm soft}}>> T_{\rm cosm}\
@V{\tau_{\rm Tate}}V{\simeq}V
@VV{\simeq}V\
T_{\rm road} @>>{1}> T_{\rm road}
\end{CD}
\]

commutes integrally.

This is a genuine naturality theorem for the frozen coefficient calculus.  It
does not yet define a cross-sector supported geometric map.

## Why the geometric square is not yet formable

The two sectors have different support realizations.

Cosmology supplies three independently constructed codimension-one soft Gysin
maps.  Their cyclic atlas preserves normal and residue orientations and
assembles them into the regular three-arm endpoint module.

The string candidate instead starts with a codimension-three Koszul source
and proposes

\[
f_+\longmapsto
\tau_A K_{\rm rel},
\qquad
\tau_A=\frac1{u_1u_3u_5}.
\]

The weighted three-road checker proves that, if this top arrow exists, its
three displayed road restrictions form a strict \(D_3\)-equivariant chain
map.  Read alone, that checker reports the local attachments as absent.
However, later scoped theorems refine that boundary:

- Entry 100 independently constructs all three labelled local derived Cousin
  traces, including excess, twist, occurrence, endpoint, and physical-normal
  data;
- Entry 131 identifies each source packet with the actual road-face Cartier
  costalk by a unique positively normalized Bockstein-compatible purity map;
- Entry 381 confirms that the one-road target purity and both endpoint
  restrictions are closed.

The remaining obstruction is global rather than local.  The checker still
proves that its formal star is not the full unlocalized Tate window:

- the bottom homology becomes \(R_0/(u_4,u_0,u_2)\);
- global conjugation to unit incidence would invert all even normals and erase
  the supported fibre;
- the intrinsic filtered comparison
  \(\alpha_+:\mathcal S_+^{\rm cond}\to C_{\rm abs}^{v_+}\) is not
  supplied;
- the three proved local traces have not been shown to be restrictions of
  that one global morphism;
- the common scalar-to-road realization with its nonzero generic \(Q\)-leg
  remains unconstructed.

Thus

\[
\boxed{
\text{coefficient naturality: proved}
\qquad
\text{road-face supported naturality: proved locally};
\quad
\text{global supported-PC naturality: untyped/open}.
}
\]

## Cross-sector explanation

The common order-three coefficient object does not force a common geometric
realization.  Cosmology reaches it by a direct sum of source-defined
codimension-one boundary maps.  String theory already has the three local
road traces and their Cartier purity comparisons, but still requires one
filtered codimension-three global class whose restrictions are those traces
and whose generic leg is retained.

This is a concrete instance of

\[
\text{shared calculus}
+\text{sector-specific support geometry}.
\]

It also explains why quotient matching alone repeatedly looked persuasive:
after support is forgotten, both sectors really do carry the same Tate
coefficient.  The unresolved information is exactly the higher supported
gluing cell.

## Sharp next gate

Construct the source-derived filtered comparison

\[
\alpha_+:
\mathcal S_+^{\rm cond}
\longrightarrow
C_{\rm abs}^{v_+}
\]

in the bounded, exhaustive, separated, \(D_3\)-stable filtration, without
inverting the Rees parameter, any normal, or three.  Its associated grade
must be the weighted star; its three codimension-one restrictions must be
the already proved local road traces; and the resulting scalar-to-road
realization must retain its generic \(Q\)-leg.  Only that calculation can
promote the facewise theorem to a global supported cross-sector naturality
square.

## Durable evidence

- research/nima/rs2-the-canonical-c3-tate-bridge-exists.md;
- research/nima/rs3-the-cyclic-soft-star-activates-the-tate-line-as-a-supported-vector.md;
- research/voevodsky/check_cyclic_road_extension_class.py;
- research/voevodsky/check_weighted_three_road_star.rs;
- ledger Entries 100, 101, 131, and 381;
- live rerun of the weighted three-road checker on 2026-08-23.
