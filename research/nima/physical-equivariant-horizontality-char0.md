# Physical three-chart descent is horizontal by labelled naturality

## Result

The horizontal part of the three-chart descent does not require reconstruction
of a connection matrix on the bounded rank-21 presentation.  The charts

\[
G_{12}\longrightarrow G_{23}\longrightarrow G_{31}\longrightarrow G_{12}
\]

are obtained from one labelled Cayley--Menger family by an integral order-three
relabeling of sites, edge variables, marked denominators, and residue
orientations.  Pullback by this algebraic isomorphism commutes with the relative
de Rham differential.  Because the base coordinates are relabeled at the same
time, functoriality of relative de Rham cohomology also gives

\[
T\,\nabla_{G_{12}}=\nabla_{G_{23}}\,T,
\]

and cyclically for the other two edges.  The three orientation signs are (+1):
the cyclic relabeling is even and its third power is the identity.  The physical
numerator occurrence (q_{\mathfrak g_{23}}+q_{\mathfrak g_{31}}) is transported
to the corresponding labelled pair in each next chart.  Consequently its
cyclic diagonal section is horizontal in the equivariant direct-sum object.

This is a characteristic-zero statement: it is defined over \(\mathbb Z\) and
uses only pullback, the chain rule, and labelled permutation.  Finite-field
matrices remain useful presentation checks, but they are not the foundation of
the horizontality claim.

## Scope boundary

This does **not** promote the calibrated finite-field census to a theorem that
the global physical marked-relative cohomology has rank 21.  The current typing
is:

\[
\boxed{
\text{exact characteristic-zero equivariant horizontality}
+
\text{bounded replicated rank-21 cyclicity}
}
\]

Nor does naturality add a physical chain or select a new supported class.  It
only proves that the already source-defined cyclic section is transported
canonically once the marked-relative objects exist.

## Verification

`checkers/check_physical_equivariant_horizontality_char0.py` verifies over exact
integers that the chart/site/edge permutations have order three, the marked
occurrence orbits close, the orientation Jacobian is (+1), and pullback obeys
the polynomial chain rule.  Its durable packet is
`results/physical_equivariant_horizontality_char0.json`.
