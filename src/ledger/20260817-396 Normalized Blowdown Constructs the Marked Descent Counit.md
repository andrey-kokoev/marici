---
id: 396
date: 2026-08-17
title: Normalized Blowdown Constructs the Marked Descent Counit
---

# Normalized Blowdown Constructs the Marked Descent Counit

Entry 395 isolated the last gate as the counit for blowdown from the
log-expanded barycentric carrier to the absolute support complex. On the
finite marked carrier, that counit is the ordinary normalized simplicial
pushforward, and it is integral.

For every old face not containing the blown-up center \((D03,x_1)\), the
blowdown fiber is a singleton. Over a face containing the center, the
nontrivial fiber consists of
\[
 h\subset h_{D03},\qquad h\subset h_{x_1}.
\]
Its order complex is a tree, its augmented cellular complex is contractible,
and all contraction coefficients are units. Hence left Kan extension of the
pulled-back occurrence cosheaf has no higher fiber homology and its counit is
objectwise primitive.

Explicitly, apply blowdown to every vertex of a barycentric flag and send a
flag to zero when two image vertices coincide. This is the standard map on
normalized simplicial chains. Because the pulled-back coefficient at a flag
is defined from the blowdown of its initial face, the occurrence lcm map for
deleting the initial vertex is preserved exactly. Thus normalized blowdown is
a chain map for the loaded occurrence differential, not merely for constant
coefficients.

## Image of the marked Morse comparison

On the seven Morse triangles, the two triangles supported entirely inside the
exceptional fiber become degenerate and vanish. The other five descend
nondegenerately. On the six terms of
\(\widetilde\xi\), the two exceptional-middle terms vanish, while the four
external terms descend to the subdivided broken path
\[
 v_+\longleftarrow E_{13}\longrightarrow m
 \longleftarrow E_{D3}\longrightarrow c.
\]
The corrected generic cycle
\[
 q_J=-[\mathrm{top},a]+[\mathrm{top},D03]
       +X_{D03}[D03,c]
\]
contains no exceptional vertex and descends unchanged. In particular its
generic component \([\mathrm{top},D03]\) survives with coefficient \(+1\).

The executable audit verifies term by term that
\[
 d\,\pi_*H_{\rm Morse}
   =\pi_*q_J-x_3\pi_*\widetilde\xi
\]
and independently verifies
\(\pi_*d=d\pi_*\) on all three marked chains.

## Consequence

The marked expanded-path comparison now has a concrete integral descent
counit into the absolute barycentric support complex. The literal
\(D03\)-road alone still has zero second transgression, as Entry 394 proved;
the nonzero term is retained by the complementary \(E_{13}\) leg and the
five-triangle descended Morse homotopy.

Combined with Entry 393, the descended comparison has the forced
Beck--Chevalley coefficients. What remains before declaring the full connector
is a final identification test: project the descended \(q_J\) roof into the
two-step support-filtration derived Hom complex and verify that its unit
\([\mathrm{top},D03]\) component represents the canonical Yoneda generator,
rather than a boundary or a different roof representative.

The executable audit is
research/voevodsky/check_d03_normalized_blowdown_counit.py.
