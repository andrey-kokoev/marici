# Two channels first permit source interference instead of inserted zeros

Let the smallest non-scalar oriented boundary map be

```
Q(T) = [a(T) b(T); c(T) d(T)].                          (1)
```

Then `det Q=ad-bc`. This is the first rank at which a determinant can vanish
although every entry remains nonzero. A zero can therefore arise from
interference between two complete source matchings rather than from placing
the target zero in one scalar entry.

When all entries are nonzero, the zero equation is

```
R(T):=a(T)d(T)/(b(T)c(T))=1.                            (2)
```

Independent oriented basis changes multiply rows and columns. Their factors
cancel in `R`, making it the multiplicative holonomy around the smallest
bipartite four-cycle.

## Coupled Hermitian normal form

On the real height line, impose

```
Q(T)=[A(T) P(T); conjugate(P(T)) D(T)],                 (3)
```

with `A,D` real. Then `det Q=AD-|P|^2` is real and can cross zero simply.
The chiral lift `H_Q=[0 Q*;Q 0]` is self-adjoint and
`det(Q*Q)=|det Q|^2`. The example `Q(T)=[[T,1],[1,1]]` has no vanishing entry
at `T=1`, but `det Q=T-1` crosses there and its Gram determinant has a double
zero.

## Noncircularity conditions

Rank two remains tautological if one entry is set equal to Xi. A candidate
passes the interference gate only if:

1. all four entries are independently defined from source correspondences;
2. no entry or basis uses Xi values or zero ordinates;
3. the four-cycle ratio is invariant under the admitted source gauge;
4. neither matching product `ad` nor `bc` vanishes at candidate zeros;
5. `ad=bc` follows from coupled arithmetic--archimedean transport.

Condition 4 separates cancellation from hidden rank-one encoding.

## Prime--archimedean placement and next target

The minimal promising placement assigns one matching to archimedean
propagation and the crossed matching to arithmetic propagation. The zero
equation compares two independently normalized routes through the
coefficient--Betti square, instead of multiplying reciprocal scalar phases.

Construct a two-object relative correspondence square whose two composites
give `ad` and `bc`, with the Mackey norm fixing normalization and the
archimedean polarization fixing reality. Commutativity or simultaneous
diagonalizability is an early falsifier because it splits the square back
into scalar lanes. No current source theorem supplies these entries or
identifies their unit holonomy with Riemann zeros.
