# Boundary-framed comparisons

This standalone Rzk module implements the homotopy-fibre interface. X and Y
must be supplied mapping **spaces**, including the required support, scalar,
filtration, variance and symmetry constraints. It does not construct those
spaces from chain complexes or identify a physical Gysin map. The path h is
input data, not chosen from strict endpoint values.

```rzk
#lang rzk-1

#define nima-frame-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (y' = z) -> (x = z)),
       (\ q' -> q'), y, p) q

#define nima-frame-rev
  (A : U) (x y : A) (p : x = y) : y = x
  := idJ (A, x, (\ y' p' -> y' = x), refl, y, p)

#define nima-frame-ap
  (A B : U) (f : A -> B) (x y : A) (p : x = y) : f x = f y
  := idJ (A, x, (\ y' p' -> f x = f y'), refl, y, p)

#define nima-framed-lift
  (X Y : U) (r : X -> Y) (theta : Y) : U
  := Sigma (f : X), r f = theta

#define nima-framed-comparison
  (X Y : U) (r : X -> Y) (theta : Y)
  (a b : nima-framed-lift X Y r theta) : U
  := Sigma (p : first a = first b),
       nima-frame-concat Y (r (first a)) (r (first b)) theta
         (nima-frame-ap X Y r (first a) (first b) p) (second b)
       = second a
```

A comparison includes the ambient path and the comparison between boundary
paths. The next two functions prove necessity and sufficiency of these data
for equality in the fibre; no uniqueness of the boundary path is assumed.

```rzk
#define nima-framed-path-from-comparison
  (X Y : U) (r : X -> Y) (theta : Y)
  (f : X) (h : r f = theta) (g : X) (k : r g = theta)
  (p : f = g)
  (c : nima-frame-concat Y (r f) (r g) theta
         (nima-frame-ap X Y r f g p) k = h)
  : (f,h) =_{nima-framed-lift X Y r theta} (g,k)
  := idJ (X, f,
       (\ g' p' -> (k' : r g' = theta) ->
         (nima-frame-concat Y (r f) (r g') theta
           (nima-frame-ap X Y r f g' p') k' = h) ->
         (f,h) =_{nima-framed-lift X Y r theta} (g',k')),
       (\ k' c' -> nima-frame-rev (nima-framed-lift X Y r theta)
         (f,k') (f,h)
         (nima-frame-ap (r f = theta) (nima-framed-lift X Y r theta)
           (\ t -> (f,t)) k' h c')),
       g, p) k c

#define nima-framed-comparison-from-path
  (X Y : U) (r : X -> Y) (theta : Y)
  (a b : nima-framed-lift X Y r theta) (p : a = b)
  : nima-framed-comparison X Y r theta a b
  := idJ (nima-framed-lift X Y r theta, a,
       (\ b' p' -> nima-framed-comparison X Y r theta a b'),
       (refl,refl), b, p)

#define nima-framed-path
  (X Y : U) (r : X -> Y) (theta : Y)
  (a b : nima-framed-lift X Y r theta)
  (c : nima-framed-comparison X Y r theta a b) : a = b
  := nima-framed-path-from-comparison X Y r theta
       (first a) (second a) (first b) (second b) (first c) (second c)
```

An ambient nullhomotopy supplies a boundary path, but does not identify that
path with the independently prescribed h. A reference zero is explicit:
a nonzero boundary frame need not admit one.

```rzk
#define nima-induced-frame
  (X Y : U) (r : X -> Y) (theta : Y)
  (zero f : X) (hzero : r zero = theta) (s : f = zero)
  : r f = theta
  := nima-frame-concat Y (r f) (r zero) theta
       (nima-frame-ap X Y r f zero s) hzero

#define nima-framed-null-from-compatible-primitive
  (X Y : U) (r : X -> Y) (theta : Y)
  (zero f : X) (hzero : r zero = theta) (h : r f = theta)
  (s : f = zero)
  (compatible : nima-induced-frame X Y r theta zero f hzero s = h)
  : (f,h) =_{nima-framed-lift X Y r theta} (zero,hzero)
  := nima-framed-path-from-comparison X Y r theta
       f h zero hzero s compatible

#define nima-induced-frame-is-null
  (X Y : U) (r : X -> Y) (theta : Y)
  (zero f : X) (hzero : r zero = theta) (s : f = zero)
  : (f,nima-induced-frame X Y r theta zero f hzero s)
    =_{nima-framed-lift X Y r theta} (zero,hzero)
  := nima-framed-null-from-compatible-primitive X Y r theta
       zero f hzero (nima-induced-frame X Y r theta zero f hzero s) s refl

#define nima-framed-obstruction
  (X Y Failure : U) (r : X -> Y) (theta : Y)
  (a b : nima-framed-lift X Y r theta)
  (exclude : nima-framed-comparison X Y r theta a b -> Failure)
  (p : a = b) : Failure
  := exclude (nima-framed-comparison-from-path X Y r theta a b p)
```

The obstruction eliminator requires exclusion of **all** compatible ambient
paths. Failure for one chosen primitive does not suffice.

## Explicit transport of prescribed frames

Transport to a revised boundary object requires its supplied path. No
constructor selects a Q-homotopy from endpoint scalar equalities.

```rzk
#define nima-transport-frame
  (X Y : U) (r : X -> Y) (theta theta' : Y) (q : theta = theta')
  (a : nima-framed-lift X Y r theta)
  : nima-framed-lift X Y r theta'
  := (first a, nima-frame-concat Y (r (first a)) theta theta' (second a) q)
```

The chain-level realization of the compatibility test is the secondary
residue h-r(s), modulo restrictions of closed ambient homotopies and higher
boundary boundaries. That quotient, its R/(Delta) instance, the Rees
recomputation, and the 222-to-208 support contraction are not asserted as
formal theorems by this module.
