# Relative cochain secondary compatibility

Dependency: `11-boundary-framed-comparison.rzk.md` (path operations only).
All algebra laws below are explicit parameters, satisfied by the indicated
slices of cochain complexes of abelian groups. No physical map, primitive,
quotient computation, or Q-homotopy is assumed to exist.

## Relative differential and framed primitives

Mminus, Mzero, Nminus and Nzero denote cochain degrees -1 and 0. Ntwo
means degree -2, not +2. A primitive is a pair (t,k) satisfying both
components of D(t,k)=(f,h). The second component retains higher boundary
homotopy k.

```rzk
#lang rzk-1

#define nima-relative-differential
  (Mminus Mzero Ntwo Nminus : U)
  (dm : Mminus -> Mzero) (r : Mminus -> Nminus)
  (dn : Ntwo -> Nminus) (sub : Nminus -> Nminus -> Nminus)
  (a : Sigma (_ : Mminus), Ntwo)
  : Sigma (_ : Mzero), Nminus
  := (dm (first a), sub (r (first a)) (dn (second a)))

#define nima-cochain-framed-primitive
  (Mminus Mzero Ntwo Nminus : U)
  (dm : Mminus -> Mzero) (r : Mminus -> Nminus)
  (dn : Ntwo -> Nminus) (sub : Nminus -> Nminus -> Nminus)
  (f : Mzero) (h : Nminus) : U
  := Sigma (t : Mminus), Sigma (k : Ntwo),
       Sigma (_ : dm t = f), sub (r t) (dn k) = h

#define nima-secondary-vanishing-witness
  (Mminus Mzero Ntwo Nminus : U)
  (dm : Mminus -> Mzero) (r : Mminus -> Nminus)
  (dn : Ntwo -> Nminus) (sub : Nminus -> Nminus -> Nminus)
  (zero : Mzero) (residual : Nminus) : U
  := Sigma (z : Mminus), Sigma (_ : dm z = zero),
       Sigma (k : Ntwo), residual = sub (r z) (dn k)
```

The second type presents membership in the sum of restricted ambient cycles
and boundary boundaries. It does not construct H^-1 or its cokernel.

## Construct a framed primitive from a secondary witness

The supplied subtraction laws are abelian-group identities, not assumptions
of the secondary criterion itself. In particular shift says that subtracting
c from a+b equals a+(b-c); restore says a+(b-a)=b.

```rzk
#define nima-secondary-to-framed
  (A B K C : U)
  (addA : A -> A -> A) (addB : B -> B -> B)
  (addC subC : C -> C -> C) (zeroB : B)
  (dm : A -> B) (r : A -> C) (dn : K -> C)
  (dm-add : (x y : A) -> dm (addA x y) = addB (dm x) (dm y))
  (r-add : (x y : A) -> r (addA x y) = addC (r x) (r y))
  (unitB : (x : B) -> addB x zeroB = x)
  (shiftC : (a b c : C) -> subC (addC a b) c = addC a (subC b c))
  (restoreC : (a b : C) -> addC a (subC b a) = b)
  (f : B) (h : C) (s : A) (primitive : dm s = f)
  (w : nima-secondary-vanishing-witness A B K C dm r dn subC
         zeroB (subC h (r s)))
  : nima-cochain-framed-primitive A B K C dm r dn subC f h
  := (addA s (first w), (first (second (second w)), (
       nima-frame-concat B (dm (addA s (first w)))
         (addB (dm s) (dm (first w))) f
         (dm-add s (first w))
         (nima-frame-concat B (addB (dm s) (dm (first w)))
           (addB f (dm (first w))) f
           (nima-frame-ap B B (\ b -> addB b (dm (first w))) (dm s) f primitive)
           (nima-frame-concat B (addB f (dm (first w))) (addB f zeroB) f
             (nima-frame-ap B B (addB f) (dm (first w)) zeroB (first (second w)))
             (unitB f))),
       nima-frame-concat C
         (subC (r (addA s (first w))) (dn (first (second (second w)))))
         (subC (addC (r s) (r (first w))) (dn (first (second (second w))))) h
         (nima-frame-ap C C (\ c -> subC c (dn (first (second (second w)))))
           (r (addA s (first w))) (addC (r s) (r (first w))) (r-add s (first w)))
         (nima-frame-concat C
           (subC (addC (r s) (r (first w))) (dn (first (second (second w)))))
           (addC (r s) (subC (r (first w)) (dn (first (second (second w)))))) h
           (shiftC (r s) (r (first w)) (dn (first (second (second w)))))
           (nima-frame-concat C
             (addC (r s) (subC (r (first w)) (dn (first (second (second w))))))
             (addC (r s) (subC h (r s))) h
             (nima-frame-ap C C (addC (r s))
               (subC (r (first w)) (dn (first (second (second w))))) (subC h (r s))
               (nima-frame-rev C (subC h (r s))
                 (subC (r (first w)) (dn (first (second (second w)))))
                 (second (second (second w)))))
             (restoreC (r s) h))))))
```

## Every framed primitive gives a secondary witness

Given t, use z=t-s. Thus the criterion accounts for replacement of the
ambient primitive, rather than testing only the originally displayed s.

```rzk
#define nima-framed-to-secondary
  (A B K C : U)
  (subA : A -> A -> A) (subB : B -> B -> B)
  (subC : C -> C -> C) (zeroB : B)
  (dm : A -> B) (r : A -> C) (dn : K -> C)
  (dm-sub : (x y : A) -> dm (subA x y) = subB (dm x) (dm y))
  (r-sub : (x y : A) -> r (subA x y) = subC (r x) (r y))
  (selfB : (b : B) -> subB b b = zeroB)
  (swapC : (a b c : C) -> subC (subC a b) c = subC (subC a c) b)
  (f : B) (h : C) (s : A) (primitive : dm s = f)
  (v : nima-cochain-framed-primitive A B K C dm r dn subC f h)
  : nima-secondary-vanishing-witness A B K C dm r dn subC
      zeroB (subC h (r s))
  := (subA (first v) s, (
       nima-frame-concat B (dm (subA (first v) s))
         (subB (dm (first v)) (dm s)) zeroB
         (dm-sub (first v) s)
         (nima-frame-concat B (subB (dm (first v)) (dm s)) (subB f (dm s)) zeroB
           (nima-frame-ap B B (\ b -> subB b (dm s)) (dm (first v)) f
             (first (second (second v))))
           (nima-frame-concat B (subB f (dm s)) (subB f f) zeroB
             (nima-frame-ap B B (subB f) (dm s) f primitive) (selfB f))),
       (first (second v),
       nima-frame-concat C (subC h (r s))
         (subC (subC (r (first v)) (dn (first (second v)))) (r s))
         (subC (r (subA (first v) s)) (dn (first (second v))))
         (nima-frame-ap C C (\ c -> subC c (r s)) h
           (subC (r (first v)) (dn (first (second v))))
           (nima-frame-rev C (subC (r (first v)) (dn (first (second v)))) h
             (second (second (second v)))))
         (nima-frame-concat C
           (subC (subC (r (first v)) (dn (first (second v)))) (r s))
           (subC (subC (r (first v)) (r s)) (dn (first (second v))))
           (subC (r (subA (first v) s)) (dn (first (second v))))
           (swapC (r (first v)) (dn (first (second v))) (r s))
           (nima-frame-ap C C (\ c -> subC c (dn (first (second v))))
             (subC (r (first v)) (r s)) (r (subA (first v) s))
             (nima-frame-rev C (r (subA (first v) s)) (subC (r (first v)) (r s))
               (r-sub (first v) s)))))))
```

These functions establish existence in both directions, not an equivalence
of the untruncated witness spaces and not uniqueness of nullhomotopies.

## Closedness and the adjacent square-zero identity

The restriction-square and differential laws are supplied separately. They
are necessary to interpret the algebraic witness types as cochain cycles.

```rzk
#define nima-cochain-ap2
  (A B C : U) (op : A -> B -> C)
  (a a' : A) (b b' : B) (p : a = a') (q : b = b')
  : op a b = op a' b'
  := nima-frame-concat C (op a b) (op a' b) (op a' b')
       (nima-frame-ap A C (\ x -> op x b) a a' p)
       (nima-frame-ap B C (op a') b b' q)

#define nima-secondary-residual-closed
  (A B C E : U)
  (dm : A -> B) (r : A -> C) (rzero : B -> E) (dn : C -> E)
  (subC : C -> C -> C) (subE : E -> E -> E) (zeroE : E)
  (dn-sub : (x y : C) -> dn (subC x y) = subE (dn x) (dn y))
  (square : (a : A) -> dn (r a) = rzero (dm a))
  (selfE : (e : E) -> subE e e = zeroE)
  (f : B) (h : C) (closed : rzero f = dn h)
  (s : A) (primitive : dm s = f)
  : dn (subC h (r s)) = zeroE
  := nima-frame-concat E (dn (subC h (r s))) (subE (dn h) (dn (r s))) zeroE
       (dn-sub h (r s))
       (nima-frame-concat E (subE (dn h) (dn (r s)))
         (subE (rzero f) (rzero f)) zeroE
         (nima-cochain-ap2 E E E subE (dn h) (rzero f) (dn (r s)) (rzero f)
           (nima-frame-rev E (rzero f) (dn h) closed)
           (nima-frame-concat E (dn (r s)) (rzero (dm s)) (rzero f)
             (square s) (nima-frame-ap B E rzero (dm s) f primitive)))
         (selfE (rzero f)))

#define nima-relative-square-boundary
  (A B K C E : U)
  (dm : A -> B) (r : A -> C) (rzero : B -> E)
  (dminus : K -> C) (dn : C -> E)
  (subC : C -> C -> C) (subE : E -> E -> E) (zeroE : E)
  (dn-sub : (x y : C) -> dn (subC x y) = subE (dn x) (dn y))
  (square : (a : A) -> dn (r a) = rzero (dm a))
  (dd : (k : K) -> dn (dminus k) = zeroE)
  (right-zero : (e : E) -> subE e zeroE = e)
  (selfE : (e : E) -> subE e e = zeroE)
  (s : A) (k : K)
  : subE (rzero (dm s)) (dn (subC (r s) (dminus k))) = zeroE
  := nima-frame-concat E
       (subE (rzero (dm s)) (dn (subC (r s) (dminus k))))
       (subE (rzero (dm s)) (rzero (dm s))) zeroE
       (nima-frame-ap E E (subE (rzero (dm s)))
         (dn (subC (r s) (dminus k))) (rzero (dm s))
         (nima-frame-concat E (dn (subC (r s) (dminus k)))
           (subE (dn (r s)) (dn (dminus k))) (rzero (dm s))
           (dn-sub (r s) (dminus k))
           (nima-frame-concat E (subE (dn (r s)) (dn (dminus k)))
             (subE (rzero (dm s)) zeroE) (rzero (dm s))
             (nima-cochain-ap2 E E E subE (dn (r s)) (rzero (dm s))
               (dn (dminus k)) zeroE (square s) (dd k))
             (right-zero (rzero (dm s))))))
       (selfE (rzero (dm s)))
```

The other component of the relative square is the supplied ambient d-squared
law. This is a degree-window adapter, not a construction of an unbounded
complex, a homology quotient, or a derived mapping-space realization.
