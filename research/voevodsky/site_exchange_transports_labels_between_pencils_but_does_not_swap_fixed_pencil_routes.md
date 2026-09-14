# Site exchange transports labels between pencils but does not swap fixed-pencil routes

## Global family equivariance

The homogeneous branch polynomial satisfies the exact identity

\[
G(a,b,h;x,y,z)=G(b,a,h;y,x,z).
\]

Hence site exchange defines an isomorphism of parameter-marked surfaces

\[
S_{12}:(a,b;x,y;W)\longmapsto(b,a;y,x;W).
\]

It exchanges the \(b\)-adapted and \(a\)-adapted pencils. This is an isomorphism between fibers with exchanged external parameters; it is not an automorphism of one generic fixed \((x,y,z)\) surface unless \(x=y\).

## Split-fiber labels

The \(b\)-pencil locations are

\[
\pm(y+z),
\qquad
\pm(2x+y+z).
\]

Under \(S_{12}\) they become the \(a\)-pencil locations

\[
\pm(x+z),
\qquad
\pm(2y+x+z).
\]

Because \(W\) is unchanged, the \(W=+Q\) and \(W=-Q\) component labels are preserved. With labels defined by the displayed ordered locations, site exchange sends

\[
d_i^{(b;x,y)}\longmapsto d_i^{(a;y,x)}
\]

for every \(i\). Thus its canonical cross-pencil Picard marking is the identity on the tetrahedral vertex labels, not a swap of \(\beta_{12}\) and \(\beta_{13}\).

## Orientation character of the wall tails

On differential forms,

\[
da\wedge db\longmapsto db\wedge da=-da\wedge db.
\]

This explains the compensating orientation sign in the universal second-wall construction and the opposite coefficients

\[
T_{101}=-c\,v_0,
\qquad T_{110}=+c\,v_0.
\]

The two wall tails are site-exchanged copies with an orientation-local-system sign. Their opposite \(v_{\rm alg}\) coefficients do not by themselves exhibit two independent routes inside one fixed pencil.

## Consequence

The earlier conditional hypothesis that integral site exchange swaps \(\beta_{12}\) and \(\beta_{13}\) is rejected for the canonical location-preserving marking. Site exchange instead preserves all vertex labels while moving from the \(b\)-pencil to the \(a\)-pencil.

To obtain a nontrivial fixed-pencil route action, one still needs an additional return comparison

\[
\text{the }a\text{-pencil at }(y,x,z)
\longrightarrow
\text{the }b\text{-pencil at }(x,y,z),
\]

not supplied by site exchange itself. Any route swap would have to occur in this return map.

## Updated role

The missing coherence comparison is now factored as

\[
L_b(x,y,z)
\xrightarrow{S_{12}}
L_a(y,x,z)
\xrightarrow{C_{a\to b}}
L_b(x,y,z).
\]

The first arrow is explicit, integral, label-preserving, and orientation-reversing on the de Rham volume form. All unresolved fixed-pencil route information lies in \(C_{a\to b}\).

Verification:

- `research/voevodsky/checkers/check_site_exchange_cross_pencil_equivariance.py`
- `research/voevodsky/results/site_exchange_cross_pencil_equivariance.json`
