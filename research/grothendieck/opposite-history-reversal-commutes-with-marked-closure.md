# Opposite-history reversal commutes with marked closure

## Result

Typed reversal is now constructed through the endpoint-decorated histories. It preserves every event mark and reverses the ordered forgotten gaps, exchanges prefix and suffix at the same arithmetic vertex, and commutes with the marked lift and all-retained extraction.

Its coefficient projection gives the order-reversing conjugation used by Voevodsky's tail-polarity comparison. This provides the structural source square, without identifying reversed arrows with forward prime events, arithmetic inverses, or Hilbert adjoints.

At the stable level, perfect-module duality gives a compatible opposite-algebra base-change square. The interval closure is reflected by dualizing interval quotients and reversing their endpoints; naive reversal of a filtration is not sufficient.

## 1. Typed reversal

For a graph E(x,y), put E^op(x,y)=E(y,x). Define

rev(e_1...e_n)=e_n^op...e_1^op.

This is a path from the old target to the old source in the opposite graph. It satisfies

rev(p q)=rev(q) rev(p), rev(rev(p))=p.

A marked arrow (e,b) reverses to (e^op,b), leaving b unchanged. Consequently a gap normal form

g_0 e_1^1 g_1 ... e_k^1 g_k

reverses to

rev(g_k) (e_k^op)^1 ... rev(g_1) (e_1^op)^1 rev(g_0).

Each gap keeps its complete arrow word and all intermediate integer labels, now traversed in the opposite category. For example the source path 2->4->12 becomes 12->4->2 in that opposite category. This does not assert that the original forward arithmetic source admits division transitions.

## 2. Lift and extraction squares

Let L and A be the additive marked lift and all-retained extraction, with L(e)=e^0+e^1, A(e^0)=0, A(e^1)=e. The opposite source has the corresponding maps L_op and A_op.

On generators, and therefore on all paths,

rev_D L=L_op rev_P,

rev_P A=A_op rev_D.

For L the summand-index map reverses the Boolean mask. For A, a path is all-retained exactly when its reversal is all-retained. The square also respects A L=id.

Over C, extend rev conjugate-linearly. The generator formulas have real coefficients, so both squares remain valid with conjugation. They are not assertions that either algebra map is a positive or isometric realization.

## 3. Cut comparison

A length-n route cut at position j reverses to a cut at n-j. Its two pieces become

(rev(suffix_j), rev(prefix_j)).

The arithmetic cut vertex is unchanged. Thus, with the tensor-factor exchange tau,

Delta_op rev=tau (rev tensor rev) Delta.

The equality holds before coefficient projection: forgotten gaps remain actual arrows and every original cut remains present. For any number of cuts the order of the cut positions and pieces reverses. Deleting and repeating cuts commute with this reflection with their reflected indices.

The existing forgotten-gap contraction is compatible with reversal: lower and upper representatives exchange, since a source cut j is sent to n-j. This is a statement about the coefficient-side marked localization, not a reason to discard the retained endpoint data upstairs.

## 4. Coefficient dagger square

For an opposite arrow labelled by a forward event e, retain the same named real chamber incidence vector v_e as its coefficient label. This is label transport, not a spatial reciprocal transformation of its forcing.

With P(e^0)=1 and P(e^1)=v_e, define P_op analogously. Then

P_op(rev(h))=(P(h))^dagger,

where dagger reverses tensor slots and conjugates coefficients. The equation holds on each generator and extends anti-multiplicatively. It is the structural coefficient operation appearing in Voevodsky's receiver-side identity A_F Z_+(h)=Z_-(h^dagger).

In particular, right multiplication on memory becomes left multiplication. Nothing in this square forces a comparison unit r to satisfy r^dagger=r^-1. Creation versus annihilation and the full reciprocal spatial source remain separate realization questions.

## 5. Formal Agda result

`agda/OppositeDecoratedHistory.agda` uses the typed route and cut definitions from the preceding formal module. It checks:

- `rev`: the target is explicitly the opposite graph;
- `rev-append`: reversal is anti-compositional;
- `rev-rev`: double reversal is the original route;
- `rev-map`: reversal commutes with arbitrary edge relabelling;
- `rev-cut-rejoin`: the reversed suffix and prefix rejoin through the original cut vertex to the reversed route.

The edge family is arbitrary, so it can be the marked family Bool times E. In particular, keeping or dropping the Boolean edge label is covered by relabelling naturality. The additive L/A squares are proved above and checked on the finite source; rational linear sums and the all-mask additive lift are not newly formalized as vector-space operations in this module.

Fresh command:

    agda --transliterate --safe --cubical --guardedness --no-libraries \
      -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
      -i research/grothendieck/agda \
      research/grothendieck/agda/OppositeDecoratedHistory.agda

Compilation succeeds. The imported decorated-history module retains its documented indexed-pattern computation warnings; no new inverse-arrow axiom, hole, or postulate is used. Log: `results/opposite-decorated-history-agda.log`.

## 6. Opposite stable realization

Keep R=Q[P], S=Q[D] and their split algebra maps l:R->S, a:S->R. Their opposites give the same split construction between R^op and S^op, identified with the path algebras of the reversed source and marked graphs.

For perfect left modules, let

D_R(M)=RHom_R(M,R),

viewed as a perfect left R^op-module. This is a contravariant exact equivalence with inverse D_(R^op); finite-projective duality supplies the natural double-dual equivalence. No scalar product is chosen.

Let F=S tensor_R^L - be the previous marked extension of scalars and F_op its opposite-algebra version. For perfect M,

D_S(F M) equivalent to RHom_R(M,S)
          equivalent to RHom_R(M,R) tensor_R^L S
          equivalent to F_op(D_R M).

The first equivalence is derived tensor–Hom adjunction; the second uses perfection of M. Hence the exact duality square is

D_S F equivalent to F_op D_R.

Likewise D_R G equivalent to G_op D_S for the extraction base change G, and the opposite split identity is G_op F_op equivalent to id.

These equivalences are natural and preserve the split source realization. Over C, coefficient conjugation can be adjoined using the real path-algebra basis, giving a conjugate-linear version with the conjugate opposite algebra correctly identified. This is algebraic perfect-module duality, not the Fock Hilbert adjoint and not an identification of its objects with the analytical receiver.

## 7. Correct interval-closure polarity

Contravariant exact duality takes a cofiber attachment u:A->B to a fiber attachment:

D(cofib u) equivalent to fib(Du)
             equivalent to cofib(Du)[-1].

For a full interval diagram X in S_n(Perf(R)), define its reflected dual by

X^vee(i,j)=D_R(X(n-j,n-i)).

For i<=j<=k, the original cofiber sequence is

X(n-k,n-j) -> X(n-k,n-i) -> X(n-j,n-i).

Duality reverses it into

X^vee(i,j) -> X^vee(i,k) -> X^vee(j,k),

again a cofiber sequence. Diagonal objects remain zero. Therefore X^vee is a complete interval diagram in S_n(Perf(R^op)). Its filtration objects are duals of tail quotients, not simply the original filtration objects read backwards.

For an ordinal map alpha:[m]->[n], restrictions intertwine after reflecting alpha to alpha^rev(j)=n-alpha(m-j). Thus the comparison respects the cut system with its correct variance rather than asserting commutation with unchanged cut indices.

The base-change duality square applies pointwise, so marked stable realization commutes with this reflected interval closure. This is the precise stable counterpart of reversing the typed cut diagram.

These derived and interval-category claims are mathematical proofs here, not an Agda verification of perfect-module duality.

## 8. Verification and boundary

`python research/grothendieck/checkers/check_opposite_decorated_history.py`

Exact finite checks pass on 168 source routes, 1,040 marked histories, and 4,176 cuts: involution, gap and mark reversal, L/A squares, cut-factor exchange at the same vertex, coefficient dagger including Gaussian-integer conjugation, and rejection of opposite routes declared as forward arithmetic.

Constructed: the source/opposite comparison and its compatible marked and stable realizations.

Not constructed: a map identifying algebraic module duality with the analytical tail receiver, inverse arithmetic events in the original source, or the spatial reciprocal involution. Those are not consequences of this structural reversal.

Receiver-side reference: `research/voevodsky/clark-tail-polarity-gives-an-exact-dagger-between-history-receivers.md`.
