# Boundary assembly and coefficient interfaces

## Question and scope

Separate arbitrary overlap fillers, coefficient admissibility, normalization
problems, and scalar-specific linearity. These are conditional interfaces for
supplied complexes, actions, and maps, not a construction of polynomial rings,
homology quotients, or the physical endpoint functor. Sources are the ChatGPT
packets `source-admissible-overlap` and `source-derived-branch-comparision`.
No contraction, equivariance, or coefficient admissibility follows merely from
a chain-map equation. All definitions below have explicit parameters.

```rzk
#lang rzk-1

#define marici-pair-path
  (V E : U) (v w : V) (e f : E) (p : v = w) (q : e = f)
  : (v, e) =_{Sigma (_ : V), E} (w, f)
  := concat (Sigma (_ : V), E) (v,e) (w,e) (w,f)
    (ap V (Sigma (_ : V), E) v w (\ t -> (t,e)) p)
    (ap E (Sigma (_ : V), E) e f (\ t -> (w,t)) q)

#define marici-assemble-from-filler
  (I Ip V Vp Em E : U)
  (di : I -> Ip) (dv : V -> Vp) (de : Em -> E)
  (rho : I -> V) (rhop : Ip -> Vp) (delta : V -> E)
  (ell : I -> Em) (ellp : Ip -> E) (sub : E -> E -> E)
  (cancel : (u v : E) -> sub u (sub u v) = v)
  (chart : (x : I) -> dv (rho x) = rhop (di x))
  (filler : (x : I) -> de (ell x) = sub (delta (rho x)) (ellp (di x)))
  (x : I)
  : (dv (rho x), sub (delta (rho x)) (de (ell x)))
    =_{Sigma (_ : Vp), E} (rhop (di x), ellp (di x))
  := marici-pair-path Vp E (dv (rho x)) (rhop (di x))
    (sub (delta (rho x)) (de (ell x))) (ellp (di x)) (chart x)
    (concat E (sub (delta (rho x)) (de (ell x)))
      (sub (delta (rho x)) (sub (delta (rho x)) (ellp (di x)))) (ellp (di x))
      (ap E E (de (ell x)) (sub (delta (rho x)) (ellp (di x)))
        (sub (delta (rho x))) (filler x))
      (cancel (delta (rho x)) (ellp (di x))))
```

The filler is the subtractive form of d ell + ell d = delta rho in an
abelian group. Assembly neither chooses ell nor requires a contraction.

## Separate admissibility witnesses

Localizations are actual maps; filters are predicates indexed by a declared
grade type (not physical time); symmetry actions are supplied functions.
Group laws and filtration-order laws belong to the supplied structures and
are not inferred from the following commuting squares.

```rzk
#define marici-localization-square
  (X Y Xl Yl : U) (f : X -> Y) (fl : Xl -> Yl)
  (lx : X -> Xl) (ly : Y -> Yl) : U
  := (x : X) -> ly (f x) = fl (lx x)

#define marici-filter-preserving
  (Grade X Y : U) (FX : Grade -> X -> U) (FY : Grade -> Y -> U)
  (f : X -> Y) : U
  := (g : Grade) -> (x : X) -> FX g x -> FY g (f x)

#define marici-equivariant-map
  (G X Y : U) (ax : G -> X -> X) (ay : G -> Y -> Y)
  (f : X -> Y) : U
  := (g : G) -> (x : X) -> f (ax g x) = ay g (f x)

#define marici-admissible-map-witness
  (Grade G X Y Xl Yl : U)
  (f : X -> Y) (fl : Xl -> Yl) (lx : X -> Xl) (ly : Y -> Yl)
  (FX : Grade -> X -> U) (FY : Grade -> Y -> U)
  (ax : G -> X -> X) (ay : G -> Y -> Y) : U
  := Sigma (_ : marici-localization-square X Y Xl Yl f fl lx ly),
     Sigma (_ : marici-filter-preserving Grade X Y FX FY f),
       marici-equivariant-map G X Y ax ay f
```

A certificate is required separately for each relevant map and localization.
There is deliberately no constructor from the assembly theorem to this type.

## Kernel normalization versus endpoint normalization

Kernel markings use the common conductor value on node functions. Endpoint
cycles use sheet difference matched to road augmentation, with road unit
normalization. The relative normalization presentation has node functions in
the preceding degree; the kernel presentation does not. No coercion between
these two marking problems is defined.

```rzk
#define marici-conductor-kernel (N R : U) (delta : N -> R) (zero : R) : U
  := Sigma (n : N), delta n = zero

#define marici-conductor-normalized
  (A R : U) (common : A -> R) (one : R) : U
  := Sigma (a : A), common a = one

#define marici-endpoint-normalized
  (N Q R : U) (delta : N -> R) (eps : Q -> R) (one : R) : U
  := Sigma (n : N), Sigma (q : Q),
       Sigma (_ : delta n = eps q), eps q = one

#define marici-relative-boundary-witness
  (A N : U) (nu : A -> N) (n : N) : U
  := Sigma (a : A), nu a = n

#define marici-node-is-relative-boundary
  (A N : U) (nu : A -> N) (a : A)
  : marici-relative-boundary-witness A N nu (nu a)
  := (a, refl)

#define marici-node-is-kernel-cycle
  (A N R : U) (nu : A -> N) (delta : N -> R) (zero : R)
  (exact-at-node : (a : A) -> delta (nu a) = zero) (a : A)
  : marici-conductor-kernel N R delta zero
  := (nu a, exact-at-node a)

#define marici-node-cannot-have-endpoint-unit
  (A N Q R : U) (nu : A -> N) (delta : N -> R) (eps : Q -> R)
  (zero one : R) (exact-at-node : (a : A) -> delta (nu a) = zero)
  (a : A) (q : Q) (closed : delta (nu a) = eps q) (normalized : eps q = one)
  : zero = one
  := concat R zero (delta (nu a)) one
    (rev R (delta (nu a)) zero (exact-at-node a))
    (concat R (delta (nu a)) (eps q) one closed normalized)
```

Thus when zero and one are distinct, a node image cannot be a normalized
endpoint cycle. A common conductor unit is not promoted to an endpoint unit.
The boundary witness is a presentation-level witness, not an implemented
homology quotient or an assertion of exactness for arbitrary nu.

## Scalar-specific linearity

Linearity is indexed by the scalar type, both actions, and addition operations.
Use S=A for A-linearity and S=R for R-linearity. The restriction theorem goes
from A to R through a supplied scalar map; there is no reverse promotion.
Ring and module axioms remain supplied by the eventual coefficient layer.

```rzk
#define marici-linear-over
  (S X Y : U) (addX : X -> X -> X) (addY : Y -> Y -> Y)
  (actX : S -> X -> X) (actY : S -> Y -> Y) (f : X -> Y) : U
  := Sigma (_ : (x y : X) -> f (addX x y) = addY (f x) (f y)),
       (s : S) -> (x : X) -> f (actX s x) = actY s (f x)

#define marici-restrict-scalars
  (R A X Y : U) (embed : R -> A)
  (addX : X -> X -> X) (addY : Y -> Y -> Y)
  (actX : A -> X -> X) (actY : A -> Y -> Y) (f : X -> Y)
  (linearA : marici-linear-over A X Y addX addY actX actY f)
  : marici-linear-over R X Y addX addY
      (\ r -> actX (embed r)) (\ r -> actY (embed r)) f
  := (first linearA, \ r x -> (second linearA) (embed r) x)

#define marici-linearity-counterexample
  (A X Y : U) (addX : X -> X -> X) (addY : Y -> Y -> Y)
  (actX : A -> X -> X) (actY : A -> Y -> Y) (f : X -> Y)
  (s : A) (x : X) (Failure : U)
  (obstruction : (f (actX s x) = actY s (f x)) -> Failure)
  (linearA : marici-linear-over A X Y addX addY actX actY f)
  : Failure
  := obstruction ((second linearA) s x)
```

The counterexample eliminator exposes the exact scalar-action equality that
must fail for the ambient R-linear splitting. It does not pretend that the
concrete polynomial counterexample has already been instantiated here.

## Disposition

Fresh headless Rzk verification passed on 2026-09-06, exit 0 with
`Everything is ok!`, together with the refactored contraction instance.
The explicit dependency closure is pinned sHoTT
`52a441cc4aaa03f3fe94ee94f70bb2874e26a6a2` files `src/hott/00-common.rzk.md`
and `src/hott/01-paths.rzk.md`, this file, then
`02a-marici-boundary-interior-chain-map.rzk.md`.
Concrete pair-local formulas, coefficient rings, and
source normalization maps still require separate instantiation. These
interfaces do not claim the full physical comparison or a zeta construction.
