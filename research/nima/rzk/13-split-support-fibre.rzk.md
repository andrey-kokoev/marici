# Split support fibre and retained Q-frame

For the graded splitting K = B + Q, the fibre of the combined quotient and
endpoint restriction is written in coordinates (b,q0,q1). B is the full
short-boundary support, including V, not B/V. The differential is
(db + alpha q0, dq0, q0 - dq1), where alpha is the actual attaching block.
All coefficient modules, maps and algebra identities below are parameters.

```rzk
#lang rzk-1

#define nima-support-fibre (B Q Qnext : U) : U
  := Sigma (_ : B), Sigma (_ : Q), Qnext

#define nima-support-include
  (B Q Qnext : U) (zeroQ : Q) (zeroNext : Qnext) (b : B)
  : nima-support-fibre B Q Qnext
  := (b, (zeroQ, zeroNext))

#define nima-support-project
  (B Q Qnext : U) (sub : B -> B -> B) (alpha : Qnext -> B)
  (x : nima-support-fibre B Q Qnext) : B
  := sub (first x) (alpha (second (second x)))

#define nima-support-differential
  (B Bprev Q Qprev Qnext : U)
  (db : B -> Bprev) (dq : Q -> Qprev) (dqnext : Qnext -> Q)
  (alpha : Q -> Bprev) (add : Bprev -> Bprev -> Bprev)
  (sub : Q -> Q -> Q) (x : nima-support-fibre B Q Qnext)
  : nima-support-fibre Bprev Qprev Q
  := (add (db (first x)) (alpha (first (second x))),
       (dq (first (second x)), sub (first (second x)) (dqnext (second (second x)))))

#define nima-support-homotopy
  (B Bnext Q Qnext Qnextnext : U)
  (zeroBnext : Bnext) (zeroQnextnext : Qnextnext)
  (x : nima-support-fibre B Q Qnext)
  : nima-support-fibre Bnext Qnext Qnextnext
  := (zeroBnext, (second (second x), zeroQnextnext))

#define nima-support-triple-path
  (A B C : U) (a a' : A) (b b' : B) (c c' : C)
  (p : a = a') (q : b = b') (s : c = c')
  : (a,(b,c)) =_{nima-support-fibre A B C} (a',(b',c'))
  := nima-cochain-ap2 A (Sigma (_ : B), C) (nima-support-fibre A B C)
       (\ x y -> (x,y)) a a' (b,c) (b',c') p
       (nima-cochain-ap2 B C (Sigma (_ : B), C) (\ x y -> (x,y)) b b' c c' q s)

#define nima-support-project-include
  (B Q Qnext : U) (zeroB : B) (zeroQ : Q) (zeroNext : Qnext)
  (sub : B -> B -> B) (alpha : Qnext -> B)
  (alpha-zero : alpha zeroNext = zeroB)
  (sub-zero : (b : B) -> sub b zeroB = b) (b : B)
  : nima-support-project B Q Qnext sub alpha
      (nima-support-include B Q Qnext zeroQ zeroNext b) = b
  := nima-frame-concat B (sub b (alpha zeroNext)) (sub b zeroB) b
       (nima-frame-ap B B (sub b) (alpha zeroNext) zeroB alpha-zero) (sub-zero b)
```

## Inclusion is a chain map

```rzk
#define nima-support-include-chain
  (B Bprev Q Qprev Qnext : U)
  (db : B -> Bprev) (dq : Q -> Qprev) (dqnext : Qnext -> Q)
  (alpha : Q -> Bprev) (add : Bprev -> Bprev -> Bprev) (sub : Q -> Q -> Q)
  (zeroBprev : Bprev) (zeroQ : Q) (zeroQprev : Qprev) (zeroQnext : Qnext)
  (alpha-zero : alpha zeroQ = zeroBprev) (dq-zero : dq zeroQ = zeroQprev)
  (dqnext-zero : dqnext zeroQnext = zeroQ)
  (add-zero : (b : Bprev) -> add b zeroBprev = b)
  (sub-self : sub zeroQ zeroQ = zeroQ) (b : B)
  : nima-support-differential B Bprev Q Qprev Qnext db dq dqnext alpha add sub
      (nima-support-include B Q Qnext zeroQ zeroQnext b)
    = nima-support-include Bprev Qprev Q zeroQprev zeroQ (db b)
  := nima-support-triple-path Bprev Qprev Q
       (add (db b) (alpha zeroQ)) (db b) (dq zeroQ) zeroQprev
       (sub zeroQ (dqnext zeroQnext)) zeroQ
       (nima-frame-concat Bprev (add (db b) (alpha zeroQ)) (add (db b) zeroBprev) (db b)
         (nima-frame-ap Bprev Bprev (add (db b)) (alpha zeroQ) zeroBprev alpha-zero)
         (add-zero (db b))) dq-zero
       (nima-frame-concat Q (sub zeroQ (dqnext zeroQnext)) (sub zeroQ zeroQ) zeroQ
         (nima-frame-ap Q Q (sub zeroQ) (dqnext zeroQnext) zeroQ dqnext-zero) sub-self)
```

## Projection is a chain map

Only the attaching-block identity d alpha = - alpha d is used; it is
supplied by the square-zero law of K. The subtraction-preservation laws
are separate from that identity.

```rzk
#define nima-support-project-chain
  (B Bprev Q Qprev Qnext : U)
  (db : B -> Bprev) (dq : Q -> Qprev) (dqnext : Qnext -> Q)
  (alpha : Q -> Bprev) (alphaNext : Qnext -> B)
  (addPrev subPrev : Bprev -> Bprev -> Bprev) (negPrev : Bprev -> Bprev)
  (subB : B -> B -> B) (subQ : Q -> Q -> Q)
  (db-sub : (a b : B) -> db (subB a b) = subPrev (db a) (db b))
  (alpha-sub : (a b : Q) -> alpha (subQ a b) = subPrev (alpha a) (alpha b))
  (attaching : (q : Qnext) -> db (alphaNext q) = negPrev (alpha (dqnext q)))
  (cancel : (x a c : Bprev) -> subPrev (addPrev x a) (subPrev a c) = addPrev x c)
  (sub-neg : (x y : Bprev) -> subPrev x (negPrev y) = addPrev x y)
  (b : B) (q : Q) (u : Qnext)
  : nima-support-project Bprev Qprev Q subPrev alpha
      (nima-support-differential B Bprev Q Qprev Qnext
        db dq dqnext alpha addPrev subQ (b,(q,u)))
    = db (nima-support-project B Q Qnext subB alphaNext (b,(q,u)))
  := nima-frame-concat Bprev
       (subPrev (addPrev (db b) (alpha q)) (alpha (subQ q (dqnext u))))
       (addPrev (db b) (alpha (dqnext u))) (db (subB b (alphaNext u)))
       (nima-frame-concat Bprev
         (subPrev (addPrev (db b) (alpha q)) (alpha (subQ q (dqnext u))))
         (subPrev (addPrev (db b) (alpha q)) (subPrev (alpha q) (alpha (dqnext u))))
         (addPrev (db b) (alpha (dqnext u)))
         (nima-frame-ap Bprev Bprev (subPrev (addPrev (db b) (alpha q)))
           (alpha (subQ q (dqnext u))) (subPrev (alpha q) (alpha (dqnext u)))
           (alpha-sub q (dqnext u)))
         (cancel (db b) (alpha q) (alpha (dqnext u))))
       (nima-frame-rev Bprev (db (subB b (alphaNext u))) (addPrev (db b) (alpha (dqnext u)))
         (nima-frame-concat Bprev (db (subB b (alphaNext u)))
           (subPrev (db b) (db (alphaNext u))) (addPrev (db b) (alpha (dqnext u)))
           (db-sub b (alphaNext u))
           (nima-frame-concat Bprev (subPrev (db b) (db (alphaNext u)))
             (subPrev (db b) (negPrev (alpha (dqnext u)))) (addPrev (db b) (alpha (dqnext u)))
             (nima-frame-ap Bprev Bprev (subPrev (db b))
               (db (alphaNext u)) (negPrev (alpha (dqnext u))) (attaching u))
             (sub-neg (db b) (alpha (dqnext u))))))
```

## Contraction identity in coordinates

After the differential-of-zero laws are applied, dH+Hd has the three
components on the left below. The right side is 1-I Pi. This lemma proves
the remaining group algebra, with no contraction identity as an assumption.
Together with the displayed D and H formulas it applies in every degree.

```rzk
#define nima-support-contraction-coordinates
  (B Q Qnext : U)
  (zeroB : B) (zeroQ : Q) (zeroNext : Qnext)
  (addB subB : B -> B -> B) (addQ subQ : Q -> Q -> Q)
  (addNext subNext : Qnext -> Qnext -> Qnext)
  (alpha : Qnext -> B) (dq : Qnext -> Q)
  (left-zeroB : (b : B) -> addB zeroB b = b)
  (cancelB : (b a : B) -> subB b (subB b a) = a)
  (restoreQ : (a b : Q) -> addQ a (subQ b a) = b)
  (sub-zeroQ : (q : Q) -> subQ q zeroQ = q)
  (add-zeroNext : (q : Qnext) -> addNext q zeroNext = q)
  (sub-zeroNext : (q : Qnext) -> subNext q zeroNext = q)
  (b : B) (q : Q) (u : Qnext)
  : (addB zeroB (alpha u), (addQ (dq u) (subQ q (dq u)), addNext u zeroNext))
    =_{nima-support-fibre B Q Qnext}
    (subB b (subB b (alpha u)), (subQ q zeroQ, subNext u zeroNext))
  := nima-support-triple-path B Q Qnext
       (addB zeroB (alpha u)) (subB b (subB b (alpha u)))
       (addQ (dq u) (subQ q (dq u))) (subQ q zeroQ)
       (addNext u zeroNext) (subNext u zeroNext)
       (nima-frame-concat B (addB zeroB (alpha u)) (alpha u) (subB b (subB b (alpha u)))
         (left-zeroB (alpha u))
         (nima-frame-rev B (subB b (subB b (alpha u))) (alpha u) (cancelB b (alpha u))))
       (nima-frame-concat Q (addQ (dq u) (subQ q (dq u))) q (subQ q zeroQ)
         (restoreQ (dq u) q) (nima-frame-rev Q (subQ q zeroQ) q (sub-zeroQ q)))
       (nima-frame-concat Qnext (addNext u zeroNext) u (subNext u zeroNext)
         (add-zeroNext u) (nima-frame-rev Qnext (subNext u zeroNext) u (sub-zeroNext u)))

#define nima-support-homotopy-square
  (B Bnext Bnextnext Q Qnext Qnextnext Qnextnextnext : U)
  (zeroBnext : Bnext) (zeroBnextnext : Bnextnext)
  (zeroQnextnext : Qnextnext) (zeroQnextnextnext : Qnextnextnext)
  (x : nima-support-fibre B Q Qnext)
  : nima-support-homotopy Bnext Bnextnext Qnext Qnextnext Qnextnextnext
      zeroBnextnext zeroQnextnextnext
      (nima-support-homotopy B Bnext Q Qnext Qnextnext zeroBnext zeroQnextnext x)
    = (zeroBnextnext, (zeroQnextnext, zeroQnextnextnext))
  := refl
```

The H-squared expression is literally zero, without omitting any Q term.

```rzk
#define nima-support-homotopy-include
  (B Bnext Q Qnext Qnextnext : U)
  (zeroBnext : Bnext) (zeroQ : Q) (zeroQnext : Qnext) (zeroQnextnext : Qnextnext)
  (b : B)
  : nima-support-homotopy B Bnext Q Qnext Qnextnext zeroBnext zeroQnextnext
      (nima-support-include B Q Qnext zeroQ zeroQnext b)
    = (zeroBnext, (zeroQnext, zeroQnextnext))
  := refl

#define nima-support-project-homotopy
  (B Bnext Q Qnext Qnextnext : U)
  (zeroBnext : Bnext) (zeroQnextnext : Qnextnext)
  (sub : Bnext -> Bnext -> Bnext) (alpha : Qnextnext -> Bnext)
  (alpha-zero : alpha zeroQnextnext = zeroBnext)
  (self : sub zeroBnext zeroBnext = zeroBnext)
  (x : nima-support-fibre B Q Qnext)
  : nima-support-project Bnext Qnext Qnextnext sub alpha
      (nima-support-homotopy B Bnext Q Qnext Qnextnext zeroBnext zeroQnextnext x)
    = zeroBnext
  := nima-frame-concat Bnext (sub zeroBnext (alpha zeroQnextnext))
       (sub zeroBnext zeroBnext) zeroBnext
       (nima-frame-ap Bnext Bnext (sub zeroBnext) (alpha zeroQnextnext) zeroBnext alpha-zero) self
```

## Assembled homotopy law

This theorem applies the actual differential and homotopy maps, including
their differential-of-zero terms, and reduces to the coordinate lemma.

```rzk
#define nima-support-fibre-op
  (B Q Qnext : U)
  (opB : B -> B -> B) (opQ : Q -> Q -> Q) (opNext : Qnext -> Qnext -> Qnext)
  (x y : nima-support-fibre B Q Qnext) : nima-support-fibre B Q Qnext
  := (opB (first x) (first y),
       (opQ (first (second x)) (first (second y)),
        opNext (second (second x)) (second (second y))))

#define nima-support-homotopy-law
  (Bprev B Bnext Qprev Q Qnext Qnextnext : U)
  (db : B -> Bprev) (dbnext : Bnext -> B)
  (dq : Q -> Qprev) (dqnext : Qnext -> Q) (dqnextnext : Qnextnext -> Qnext)
  (alpha : Q -> Bprev) (alphaNext : Qnext -> B)
  (addPrev : Bprev -> Bprev -> Bprev)
  (addB subB : B -> B -> B) (addQ subQ : Q -> Q -> Q)
  (addNext subNext : Qnext -> Qnext -> Qnext)
  (zeroB : B) (zeroBnext : Bnext) (zeroQ : Q)
  (zeroNext : Qnext) (zeroNextnext : Qnextnext)
  (db-zero : dbnext zeroBnext = zeroB)
  (dq-zero : dqnextnext zeroNextnext = zeroNext)
  (left-zeroB : (b : B) -> addB zeroB b = b)
  (right-zeroB : (b : B) -> addB b zeroB = b)
  (cancelB : (b a : B) -> subB b (subB b a) = a)
  (restoreQ : (a b : Q) -> addQ a (subQ b a) = b)
  (sub-zeroQ : (q : Q) -> subQ q zeroQ = q)
  (add-zeroNext : (q : Qnext) -> addNext q zeroNext = q)
  (sub-zeroNext : (q : Qnext) -> subNext q zeroNext = q)
  (b : B) (q : Q) (u : Qnext)
  : nima-support-fibre-op B Q Qnext addB addQ addNext
      (nima-support-differential Bnext B Qnext Q Qnextnext
        dbnext dqnext dqnextnext alphaNext addB subNext
        (nima-support-homotopy B Bnext Q Qnext Qnextnext zeroBnext zeroNextnext (b,(q,u))))
      (nima-support-homotopy Bprev B Qprev Q Qnext zeroB zeroNext
        (nima-support-differential B Bprev Q Qprev Qnext db dq dqnext alpha addPrev subQ (b,(q,u))))
    = nima-support-fibre-op B Q Qnext subB subQ subNext (b,(q,u))
      (nima-support-include B Q Qnext zeroQ zeroNext
        (nima-support-project B Q Qnext subB alphaNext (b,(q,u))))
  := nima-frame-concat (nima-support-fibre B Q Qnext)
       (addB (addB (dbnext zeroBnext) (alphaNext u)) zeroB,
         (addQ (dqnext u) (subQ q (dqnext u)),
          addNext (subNext u (dqnextnext zeroNextnext)) zeroNext))
       (addB zeroB (alphaNext u),
         (addQ (dqnext u) (subQ q (dqnext u)), addNext u zeroNext))
       (subB b (subB b (alphaNext u)), (subQ q zeroQ, subNext u zeroNext))
       (nima-support-triple-path B Q Qnext
         (addB (addB (dbnext zeroBnext) (alphaNext u)) zeroB) (addB zeroB (alphaNext u))
         (addQ (dqnext u) (subQ q (dqnext u))) (addQ (dqnext u) (subQ q (dqnext u)))
         (addNext (subNext u (dqnextnext zeroNextnext)) zeroNext) (addNext u zeroNext)
         (nima-frame-concat B (addB (addB (dbnext zeroBnext) (alphaNext u)) zeroB)
           (addB (addB zeroB (alphaNext u)) zeroB) (addB zeroB (alphaNext u))
           (nima-frame-ap B B (\ x -> addB (addB x (alphaNext u)) zeroB)
             (dbnext zeroBnext) zeroB db-zero)
           (right-zeroB (addB zeroB (alphaNext u)))) refl
         (nima-frame-ap Qnext Qnext (\ x -> addNext x zeroNext)
           (subNext u (dqnextnext zeroNextnext)) u
           (nima-frame-concat Qnext (subNext u (dqnextnext zeroNextnext)) (subNext u zeroNext) u
             (nima-frame-ap Qnext Qnext (subNext u) (dqnextnext zeroNextnext) zeroNext dq-zero)
             (sub-zeroNext u))))
       (nima-support-contraction-coordinates B Q Qnext zeroB zeroQ zeroNext
         addB subB addQ subQ addNext subNext alphaNext dqnext
         left-zeroB cancelB restoreQ sub-zeroQ add-zeroNext sub-zeroNext b q u)
```

## Dependence on the retained Q-homotopy

Changing only q1 changes the support representative by minus alpha of that
change. This is the structural comparison needed to evaluate the incoming
physical Q-homotopy, not a choice of that homotopy.

```rzk
#define nima-support-frame-change
  (B Q Qnext : U) (subB : B -> B -> B) (subQ : Qnext -> Qnext -> Qnext)
  (alpha : Qnext -> B)
  (alpha-sub : (x y : Qnext) -> alpha (subQ x y) = subB (alpha x) (alpha y))
  (difference : (b x y : B) -> subB (subB b x) (subB b y) = subB y x)
  (b : B) (q : Q) (u v : Qnext)
  : subB (nima-support-project B Q Qnext subB alpha (b,(q,u)))
      (nima-support-project B Q Qnext subB alpha (b,(q,v)))
    = alpha (subQ v u)
  := nima-frame-concat B
       (subB (subB b (alpha u)) (subB b (alpha v))) (subB (alpha v) (alpha u))
       (alpha (subQ v u)) (difference b (alpha u) (alpha v))
       (nima-frame-rev B (alpha (subQ v u)) (subB (alpha v) (alpha u)) (alpha-sub v u))
```
