# Entry 1221 — The Five-Site Chamber-Relative Deck Cocycle Is Strict

## Frozen object

Work on the physical $d=3$ five-edge Kummer cover from Entries 1217–1220. Let

\[
G=(\mathbb Z_2)^5
\]

act by the five independent sheet changes $y_i\mapsto-y_i$. For each chamber mask $g\in G$, let $M_g$ be the relative marked complex obtained from the same 26 source-labelled positive sections after applying $g$. Labels, their order, the $(u_1,u_2,u_3)$ orientation, and all residue conventions are frozen before transport.

This is the induced chamber package

\[
\operatorname{Ind}_{1}^{G}M_{+}
=
\bigoplus_{g\in G}M_g,
\]

not the complement of the union of the 91 distinct signed walls.

## Hard-to-vary claim

The generator $T_i$ sends $M_g$ to $M_{g\oplus e_i}$ by $y_i\mapsto-y_i$, retaining every source label and its position. Therefore

\[
T_i^*(dq_{A,g})=dq_{A,g\oplus e_i}
\]

for every one of the 26 labelled sections.  No residue permutation occurs, so no fitted orientation sign is available or needed.

The physical ambient current

\[
\Omega_{d=3}
=
\frac{du_1\wedge du_2\wedge du_3}{\sqrt{\det H}}
\]

is independent of the five Kummer sheets and is fixed by every $T_i$.

## Finite falsifier

The durable checker exhausts all 32 chamber masks and verifies

\[
T_i^2=1,
\qquad
T_iT_j=T_jT_i,
\]

together with labelled differential transport for all generators and sections.  The census is

\[
160\text{ square checks},
\qquad
320\text{ commutator checks},
\qquad
4160\text{ section-transport checks}.
\]

Every identity passes.  Hence the projective cocycle defect is zero:

\[
\boxed{
\{M_g,T_i\}
\text{ is a strict }(\mathbb Z_2)^5\text{-equivariant chamber-relative package.}
}
\]

Its compatible invariants recover the positive physical chamber by evaluation; they do not replace the package with the 91-wall union localization.

## Classification

\[
\boxed{
\text{existing Kummer coefficient cover}
+
\text{strict occurrence transport};
\quad
\text{no new carrier datum}.
}
\]

This closes the first possible descent obstruction at the presentation level.  It does **not** yet compute the relative de Rham cohomology, a Bunch–Davies integration value, or Gauss–Manin horizontality of the full marked complex.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_deck_relative_cocycle.rs`
- `research/benincasa/results/five-site-deck-relative-cocycle.json`

## Next falsifier

Construct the common induced relative de Rham complex with its actual marked-intersection differential and Gauss–Manin connection. Test whether all $T_i$ are horizontal chain maps, with the same fixed occurrence labels and residue orientations. A nonzero chain-level or connection cocycle would be coefficient descent data; only an independently forced new incidence stratum would count as a carrier failure.
