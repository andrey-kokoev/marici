# The vertical endpoint class prevents the mixed Green pairing from descending to bulk times endpoint

## Descent test

Suppose the source mixed Green pairing descended to a bounded form

\[
b_S:\mathscr E_S\times\mathscr H_{end,S}\to\mathbb C.
\]

Then for source vectors \(g,h\),

\[
|b_{src}(g,h)|
\le C
\|i_{bulk}g\|_{\mathscr E_S}
\|i_{end}h\|_{\mathscr H_{end,S}}.
\]

## Vertical sequence

The endpoint graph completion contains a vertical class represented by source
vectors \(g_n\) satisfying

\[
i_{bulk}g_n\to0,
\qquad
i_{end}g_n\to e_{vert}\ne0.
\]

Choose a source endpoint test \(h\) whose Green pairing with \(e_{vert}\) is
nonzero. Continuity of the endpoint Green form gives

\[
b_{src}(g_n,h)
\longrightarrow
\omega(e_{vert},i_{end}h)
\ne0.
\]

But the proposed product bound forces

\[
|b_{src}(g_n,h)|
\le C
\|i_{bulk}g_n\|
\|i_{end}h\|
\longrightarrow0,
\]

a contradiction.

## Consequence

The mixed Green pairing does not descend to a bounded operator from the
unaugmented phase-energy bulk into the independently completed endpoint space.
The failure is exactly the vertical boundary sector, not a missing estimate.

Thus the correct object is the closure of the **joint source graph**

\[
\mathscr G_S
=
\overline{
\{(i_{bulk}g,i_{end}g):g\in\mathcal C_S\}
}^{\,\mathscr E_S\oplus\mathscr H_{end,S}},
\]

with the Green form defined on \(\mathscr G_S\). It is a relation/correspondence,
not an arbitrary operator on the full Cartesian product.

On \(\mathscr G_S\), vertical endpoint vectors are retained rather than forced
to vanish through the bulk kernel. The contour identity determines the pulled-
back form there without requiring false kernel descent.

## Revised positive target

Positive rung-four coherence must be tested on the joint graph:

\[
q_S(\xi)\ge0,
\qquad \xi\in\mathscr G_S,
\]

or on its centered subspace. A block Schur complement on
\(\mathscr E_S\oplus\mathscr H_{end,S}\) is legitimate only after choosing a
source-derived splitting of \(\mathscr G_S\); no such splitting is currently
proved.
