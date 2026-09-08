# Graded Hom degree windows

Source: `references/homotopy-complexes.md`, Stacks 0A8H. The Hom object is a
product of degreewise maps, not a direct sum. These definitions use explicit
index translations rather than an implicit identification of graded modules.
The linearity predicate is supplied by the coefficient-module layer.

```rzk
#lang rzk-1

#define nima-hom-family
  (I : U) (L M : I -> U) (shift : I -> I) : U
  := (i : I) -> L i -> M (shift i)

#define nima-linear-hom-family
  (I : U) (L M : I -> U) (shift : I -> I)
  (linear : (i : I) -> (L i -> M (shift i)) -> U) : U
  := Sigma (f : nima-hom-family I L M shift), (i : I) -> linear i (f i)

#define nima-hom-compose
  (I : U) (L M N : I -> U) (s t : I -> I)
  (g : nima-hom-family I M N t) (f : nima-hom-family I L M s)
  : nima-hom-family I L N (\ i -> t (s i))
  := \ i x -> g (s i) (f i x)

#define nima-hom-compose-assoc
  (I : U) (L M N P : I -> U) (s t u : I -> I)
  (h : nima-hom-family I N P u) (g : nima-hom-family I M N t)
  (f : nima-hom-family I L M s) (i : I) (x : L i)
  : h (t (s i)) (g (s i) (f i x))
    = nima-hom-compose I L N P (\ j -> t (s j)) u h
        (nima-hom-compose I L M N s t g f) i x
  := refl

#define nima-hom-transport
  (I : U) (M : I -> U) (i j : I) (p : i = j) (x : M i) : M j
  := idJ (I, i, (\ j' p' -> M j'), x, j, p)

#define nima-hom-differential-even
  (I : U) (L M : I -> U) (next shift shiftNext : I -> I)
  (target-step : (i : I) -> next (shift i) = shiftNext i)
  (source-step : (i : I) -> shift (next i) = shiftNext i)
  (dL : (i : I) -> L i -> L (next i))
  (dM : (i : I) -> M i -> M (next i))
  (sub : (i : I) -> M i -> M i -> M i)
  (f : nima-hom-family I L M shift)
  : nima-hom-family I L M shiftNext
  := \ i x -> sub (shiftNext i)
       (nima-hom-transport I M (next (shift i)) (shiftNext i) (target-step i)
         (dM (shift i) (f i x)))
       (nima-hom-transport I M (shift (next i)) (shiftNext i) (source-step i)
         (f (next i) (dL i x)))

#define nima-hom-differential-odd
  (I : U) (L M : I -> U) (next shift shiftNext : I -> I)
  (target-step : (i : I) -> next (shift i) = shiftNext i)
  (source-step : (i : I) -> shift (next i) = shiftNext i)
  (dL : (i : I) -> L i -> L (next i))
  (dM : (i : I) -> M i -> M (next i))
  (add : (i : I) -> M i -> M i -> M i)
  (f : nima-hom-family I L M shift)
  : nima-hom-family I L M shiftNext
  := \ i x -> add (shiftNext i)
       (nima-hom-transport I M (next (shift i)) (shiftNext i) (target-step i)
         (dM (shift i) (f i x)))
       (nima-hom-transport I M (shift (next i)) (shiftNext i) (source-step i)
         (f (next i) (dL i x)))
```

Even degrees use subtraction; odd degrees, including -1, use addition.
No equality of different shift maps is silently used. To assemble all degrees,
the chosen integer-index implementation must supply coherent transports.

## Square zero in a compatible operator window

On homogeneous map modules, post means d_M followed by the map and pre means
the map followed by d_L. In aligned coordinates these commute; each squares
to zero. The next theorems derive both parity cases of delta-squared from
those facts. They do not assume delta-squared itself.

```rzk
#define nima-hom-square-even
  (A B C : U) (post pre : A -> B) (postNext preNext : B -> C)
  (subB : B -> B -> B) (addC subC : C -> C -> C) (zeroC : C)
  (post-sub : (x y : B) -> postNext (subB x y) = subC (postNext x) (postNext y))
  (pre-sub : (x y : B) -> preNext (subB x y) = subC (preNext x) (preNext y))
  (post-square : (a : A) -> postNext (post a) = zeroC)
  (pre-square : (a : A) -> preNext (pre a) = zeroC)
  (commute : (a : A) -> postNext (pre a) = preNext (post a))
  (sub-zero : (c : C) -> subC c zeroC = c)
  (inverse : (c : C) -> addC (subC zeroC c) c = zeroC)
  (f : A)
  : addC (postNext (subB (post f) (pre f))) (preNext (subB (post f) (pre f))) = zeroC
  := nima-frame-concat C
       (addC (postNext (subB (post f) (pre f))) (preNext (subB (post f) (pre f))))
       (addC (subC (postNext (post f)) (postNext (pre f)))
         (subC (preNext (post f)) (preNext (pre f)))) zeroC
       (nima-cochain-ap2 C C C addC
         (postNext (subB (post f) (pre f))) (subC (postNext (post f)) (postNext (pre f)))
         (preNext (subB (post f) (pre f))) (subC (preNext (post f)) (preNext (pre f)))
         (post-sub (post f) (pre f)) (pre-sub (post f) (pre f)))
       (nima-frame-concat C
         (addC (subC (postNext (post f)) (postNext (pre f)))
           (subC (preNext (post f)) (preNext (pre f))))
         (addC (subC zeroC (preNext (post f))) (subC (preNext (post f)) zeroC)) zeroC
         (nima-cochain-ap2 C C C addC
           (subC (postNext (post f)) (postNext (pre f))) (subC zeroC (preNext (post f)))
           (subC (preNext (post f)) (preNext (pre f))) (subC (preNext (post f)) zeroC)
           (nima-cochain-ap2 C C C subC (postNext (post f)) zeroC
             (postNext (pre f)) (preNext (post f)) (post-square f) (commute f))
           (nima-frame-ap C C (subC (preNext (post f))) (preNext (pre f)) zeroC (pre-square f)))
         (nima-frame-concat C
           (addC (subC zeroC (preNext (post f))) (subC (preNext (post f)) zeroC))
           (addC (subC zeroC (preNext (post f))) (preNext (post f))) zeroC
           (nima-frame-ap C C (addC (subC zeroC (preNext (post f))))
             (subC (preNext (post f)) zeroC) (preNext (post f)) (sub-zero (preNext (post f))))
           (inverse (preNext (post f)))))

#define nima-hom-square-odd
  (A B C : U) (post pre : A -> B) (postNext preNext : B -> C)
  (addB : B -> B -> B) (addC subC : C -> C -> C) (zeroC : C)
  (post-add : (x y : B) -> postNext (addB x y) = addC (postNext x) (postNext y))
  (pre-add : (x y : B) -> preNext (addB x y) = addC (preNext x) (preNext y))
  (post-square : (a : A) -> postNext (post a) = zeroC)
  (pre-square : (a : A) -> preNext (pre a) = zeroC)
  (commute : (a : A) -> postNext (pre a) = preNext (post a))
  (left-zero : (c : C) -> addC zeroC c = c)
  (right-zero : (c : C) -> addC c zeroC = c)
  (self : (c : C) -> subC c c = zeroC) (f : A)
  : subC (postNext (addB (post f) (pre f))) (preNext (addB (post f) (pre f))) = zeroC
  := nima-frame-concat C
       (subC (postNext (addB (post f) (pre f))) (preNext (addB (post f) (pre f))))
       (subC (addC (postNext (post f)) (postNext (pre f)))
         (addC (preNext (post f)) (preNext (pre f)))) zeroC
       (nima-cochain-ap2 C C C subC
         (postNext (addB (post f) (pre f))) (addC (postNext (post f)) (postNext (pre f)))
         (preNext (addB (post f) (pre f))) (addC (preNext (post f)) (preNext (pre f)))
         (post-add (post f) (pre f)) (pre-add (post f) (pre f)))
       (nima-frame-concat C
         (subC (addC (postNext (post f)) (postNext (pre f)))
           (addC (preNext (post f)) (preNext (pre f))))
         (subC (addC zeroC (preNext (post f))) (addC (preNext (post f)) zeroC)) zeroC
         (nima-cochain-ap2 C C C subC
           (addC (postNext (post f)) (postNext (pre f))) (addC zeroC (preNext (post f)))
           (addC (preNext (post f)) (preNext (pre f))) (addC (preNext (post f)) zeroC)
           (nima-cochain-ap2 C C C addC (postNext (post f)) zeroC
             (postNext (pre f)) (preNext (post f)) (post-square f) (commute f))
           (nima-frame-ap C C (addC (preNext (post f))) (preNext (pre f)) zeroC (pre-square f)))
         (nima-frame-concat C
           (subC (addC zeroC (preNext (post f))) (addC (preNext (post f)) zeroC))
           (subC (preNext (post f)) (preNext (post f))) zeroC
           (nima-cochain-ap2 C C C subC
             (addC zeroC (preNext (post f))) (preNext (post f))
             (addC (preNext (post f)) zeroC) (preNext (post f))
             (left-zero (preNext (post f))) (right-zero (preNext (post f))))
           (self (preNext (post f)))))
```

## A target chain map induces a Hom chain map

Use op=sub in even degree and op=add in odd degree. This derives the
restriction-square law needed by v7 from the actual target chain square and
linearity, instead of assuming the Hom restriction square separately.

```rzk
#define nima-hom-postcompose-chain
  (S Snext T Tnext V Vnext : U)
  (ds : S -> Snext) (dt : T -> Tnext) (du : V -> Vnext)
  (r : T -> V) (rNext : Tnext -> Vnext)
  (opT : Tnext -> Tnext -> Tnext) (opU : Vnext -> Vnext -> Vnext)
  (square : (y : T) -> du (r y) = rNext (dt y))
  (preserve : (a b : Tnext) -> rNext (opT a b) = opU (rNext a) (rNext b))
  (f : S -> T) (fNext : Snext -> Tnext) (x : S)
  : opU (du (r (f x))) (rNext (fNext (ds x)))
    = rNext (opT (dt (f x)) (fNext (ds x)))
  := nima-frame-concat Vnext
       (opU (du (r (f x))) (rNext (fNext (ds x))))
       (opU (rNext (dt (f x))) (rNext (fNext (ds x))))
       (rNext (opT (dt (f x)) (fNext (ds x))))
       (nima-frame-ap Vnext Vnext (\ y -> opU y (rNext (fNext (ds x))))
         (du (r (f x))) (rNext (dt (f x))) (square (f x)))
       (nima-frame-rev Vnext (rNext (opT (dt (f x)) (fNext (ds x))))
         (opU (rNext (dt (f x))) (rNext (fNext (ds x))))
         (preserve (dt (f x)) (fNext (ds x))))
```

## Postcomposition transfers a contraction

For h(f)=H composed with f, the odd degree of H forces the source terms to
cancel. The following are the even and odd degree components of
 delta h + h delta = 1 - (I Pi) postcomposition. They use the target
contraction, not a Hom-contraction hypothesis. No source contraction is needed.
The equality is pointwise, without a function-extensionality assumption.

```rzk
#define nima-hom-postcontraction-even
  (S Snext Tprev T Tnext : U)
  (ds : S -> Snext) (dtprev : Tprev -> T) (dt : T -> Tnext)
  (H : T -> Tprev) (Hnext : Tnext -> T) (ip : T -> T)
  (add sub : T -> T -> T) (subNext : Tnext -> Tnext -> Tnext)
  (H-sub : (a b : Tnext) -> Hnext (subNext a b) = sub (Hnext a) (Hnext b))
  (cancel : (a b c : T) -> add (add a c) (sub b c) = add a b)
  (target-contraction : (y : T) -> add (dtprev (H y)) (Hnext (dt y)) = sub y (ip y))
  (f : S -> T) (fNext : Snext -> Tnext) (x : S)
  : add (add (dtprev (H (f x))) (Hnext (fNext (ds x))))
      (Hnext (subNext (dt (f x)) (fNext (ds x))))
    = sub (f x) (ip (f x))
  := nima-frame-concat T
       (add (add (dtprev (H (f x))) (Hnext (fNext (ds x))))
         (Hnext (subNext (dt (f x)) (fNext (ds x)))))
       (add (add (dtprev (H (f x))) (Hnext (fNext (ds x))))
         (sub (Hnext (dt (f x))) (Hnext (fNext (ds x)))))
       (sub (f x) (ip (f x)))
       (nima-frame-ap T T (add (add (dtprev (H (f x))) (Hnext (fNext (ds x)))))
         (Hnext (subNext (dt (f x)) (fNext (ds x))))
         (sub (Hnext (dt (f x))) (Hnext (fNext (ds x))))
         (H-sub (dt (f x)) (fNext (ds x))))
       (nima-frame-concat T
         (add (add (dtprev (H (f x))) (Hnext (fNext (ds x))))
           (sub (Hnext (dt (f x))) (Hnext (fNext (ds x)))))
         (add (dtprev (H (f x))) (Hnext (dt (f x)))) (sub (f x) (ip (f x)))
         (cancel (dtprev (H (f x))) (Hnext (dt (f x))) (Hnext (fNext (ds x))))
         (target-contraction (f x)))

#define nima-hom-postcontraction-odd
  (S Snext Tprev T Tnext : U)
  (ds : S -> Snext) (dtprev : Tprev -> T) (dt : T -> Tnext)
  (H : T -> Tprev) (Hnext : Tnext -> T) (ip : T -> T)
  (add sub : T -> T -> T) (addNext : Tnext -> Tnext -> Tnext)
  (H-add : (a b : Tnext) -> Hnext (addNext a b) = add (Hnext a) (Hnext b))
  (cancel : (a b c : T) -> add (sub a c) (add b c) = add a b)
  (target-contraction : (y : T) -> add (dtprev (H y)) (Hnext (dt y)) = sub y (ip y))
  (f : S -> T) (fNext : Snext -> Tnext) (x : S)
  : add (sub (dtprev (H (f x))) (Hnext (fNext (ds x))))
      (Hnext (addNext (dt (f x)) (fNext (ds x))))
    = sub (f x) (ip (f x))
  := nima-frame-concat T
       (add (sub (dtprev (H (f x))) (Hnext (fNext (ds x))))
         (Hnext (addNext (dt (f x)) (fNext (ds x)))))
       (add (sub (dtprev (H (f x))) (Hnext (fNext (ds x))))
         (add (Hnext (dt (f x))) (Hnext (fNext (ds x)))))
       (sub (f x) (ip (f x)))
       (nima-frame-ap T T (add (sub (dtprev (H (f x))) (Hnext (fNext (ds x)))))
         (Hnext (addNext (dt (f x)) (fNext (ds x))))
         (add (Hnext (dt (f x))) (Hnext (fNext (ds x))))
         (H-add (dt (f x)) (fNext (ds x))))
       (nima-frame-concat T
         (add (sub (dtprev (H (f x))) (Hnext (fNext (ds x))))
           (add (Hnext (dt (f x))) (Hnext (fNext (ds x)))))
         (add (dtprev (H (f x))) (Hnext (dt (f x)))) (sub (f x) (ip (f x)))
         (cancel (dtprev (H (f x))) (Hnext (dt (f x))) (Hnext (fNext (ds x))))
         (target-contraction (f x)))
```

These operator hypotheses must be derived from the component module laws
and coherent degree alignment when instantiating the family definitions.
The module does not identify arbitrary product-valued functions with linear
maps, implement an integer group, or replace Hom by RHom.
