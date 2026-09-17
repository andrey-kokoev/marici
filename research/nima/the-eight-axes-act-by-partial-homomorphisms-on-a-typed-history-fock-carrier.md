# The eight axes act by partial homomorphisms on a typed history-Fock carrier

## Infinite typing state

Use states

\[
s=(h,v,\epsilon,i,r,c,o,X,k)
\]

recording input arity, output arity, polarity, chart phase, convolution degree, realization flag, observation flag, cutoff stage, and stable shift. The generators act by

\[
H:h\mapsto h+1,
\qquad V:v\mapsto v+1,
\qquad D:\epsilon\mapsto1-\epsilon,
\]

\[
q:(i,k)\mapsto(i+1,k),
\quad (3,k)\mapsto(0,k+1),
\]

\[
L:r\mapsto r+1,
\qquad R:X\mapsto X+1.
\]

`C` and `O` are directed one-shot transitions into realized and retained-observation states. Reapplying them is untyped; an alternative idempotent convention can make later applications identities.

This defines a partial action of the free eight-generator monoid on an infinite state set. Therefore words of arbitrary finite length are typed whenever every prefix transition exists.

## Master carrier

For each type state `s`, let `X_s` be its realified algebraic finite-packet carrier. Define

\[
\mathbb F_{typed}
=
\bigoplus_{(p,s)}e_{p,s}\otimes X_s,
\]

where `p` is a typed history ending at `s`.

Each generator has a block action from the summand at `s` to the summand at `a(s)`:

- `H,V`: tensor/Fock linearizations of the rooted and cut operations;
- `D`: the real-linear form of the antiunitary dagger;
- `q`: chart transport;
- `L`: convolution successor on its graph domain;
- `C`: forward realization graph;
- `O`: retained observation graph;
- `R`: regulator refinement/completion comparison.

Appending the history label prevents different routes from collapsing. Composition of blocks follows concatenation, so every typed word determines a partial real-linear homomorphism on the algebraic master carrier.

## Correspondence and 2-cell layer

Directed or unbounded generators are represented by their graphs rather than by assumed bounded endomorphisms. Their sequential composite is relational composition of typed graph correspondences. Different words with the same endpoints remain distinct until a declared 2-cell relates them.

In particular,

\[
qR\not=Rq,
\]

but there is a leakage 2-cell

\[
A_X=P_X\mathcal F(I-P_X).
\]

Dagger, Beck--Chevalley, successor, and endpoint identities provide the other declared 2-cells.

## Status

The repeated typing automaton was exhaustively checked through length six: 299593 words, of which 207899 are typed. It verifies the partial-action composition law, `D^2=1`, `q^4=Sigma`, iterability of `H,V,L,R`, and directedness of `C,O`. The formulas define the action for arbitrary finite length.

Every typed finite sequence has an algebraic graph-homomorphism representation. The joint-closability theorem for

\[
U_4,\quad M_aU_4,\quad OU_4,\quad OM_aU_4
\]

and the graph-stability theorems for the repeated generators promote these representations to continuous partial maps on finite joint graph domains. Taking their projective system gives the completed pro-locally-convex history representation.
