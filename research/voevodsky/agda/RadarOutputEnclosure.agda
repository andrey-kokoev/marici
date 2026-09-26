{-# OPTIONS --safe --cubical --guardedness #-}
module RadarOutputEnclosure where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Sigma.Base using (_×_)
open import NativeRadarReadout using (Time; before; center; after; Direction; x3; y4; xy5; Component; xx; xy; yy)
import NativeRadarReadout as Radar

-- Minimal ordered arithmetic laws used by the proof. These are standard
-- coefficient-model obligations, NOT an assumed output enclosure theorem.
record OrderedArithmetic : Type₁ where
  field
    A : Type
    zero : A
    nat : ℕ → A
    add mul : A → A → A
    neg : A → A
    le : A → A → Type
    reflexive : {x : A} → le x x
    transitive : {x y z : A} → le x y → le y z → le x z
    nat-positive : (n : ℕ) → le zero (nat n)
    add-monotone : {a b c d : A} → le a b → le c d → le (add a c) (add b d)
    neg-reverses : {a b : A} → le a b → le (neg b) (neg a)
    mul-left : {a b c : A} → le zero c → le a b → le (mul c a) (mul c b)
    mul-right : {a b c : A} → le zero c → le a b → le (mul a c) (mul b c)

-- The syntax is the independently evaluated finite native readout, not Code.
data Expr : Type where
  cell : Time → Direction → Expr
  plus : Expr → Expr → Expr
  minus : Expr → Expr
  times : ℕ → Expr → Expr
time-expr : Direction → Expr
time-expr d = plus (plus (cell after d) (minus (times 2 (cell center d)))) (cell before d)
native-expr : Component → Expr
native-expr xx = times 16 (time-expr x3)
native-expr xy = times 6 (plus (plus (time-expr xy5) (minus (time-expr x3))) (minus (time-expr y4)))
native-expr yy = times 9 (time-expr y4)

module Bounds (S : OrderedArithmetic) where
  open OrderedArithmetic S
  record Interval : Type where
    constructor interval
    field lower upper : A
  open Interval public
  Inside : Interval → A → Type
  Inside i x = le (lower i) x × le x (upper i)
  plus-I : Interval → Interval → Interval
  plus-I i j = interval (add (lower i) (lower j)) (add (upper i) (upper j))
  neg-I : Interval → Interval
  neg-I i = interval (neg (upper i)) (neg (lower i))
  scale-I : A → Interval → Interval
  scale-I c i = interval (mul c (lower i)) (mul c (upper i))
  square-I : Interval → Interval
  square-I i = interval (mul (lower i) (lower i)) (mul (upper i) (upper i))
  plus-sound : {i j : Interval} {x y : A} → Inside i x → Inside j y → Inside (plus-I i j) (add x y)
  plus-sound (lx , xu) (ly , yu) = add-monotone lx ly , add-monotone xu yu
  neg-sound : {i : Interval} {x : A} → Inside i x → Inside (neg-I i) (neg x)
  neg-sound (lx , xu) = neg-reverses xu , neg-reverses lx
  scale-sound : {i : Interval} {x c : A} → le zero c → Inside i x → Inside (scale-I c i) (mul c x)
  scale-sound c+ (lx , xu) = mul-left c+ lx , mul-left c+ xu
  square-sound : {i : Interval} {x : A} → le zero (lower i) → Inside i x → Inside (square-I i) (mul x x)
  square-sound {i} {x} l+ (lx , xu) =
    transitive (mul-right l+ lx) (mul-left x+ lx) ,
    transitive (mul-right x+ xu) (mul-left u+ xu)
    where
    x+ : le zero x
    x+ = transitive l+ lx
    u+ : le zero (upper i)
    u+ = transitive x+ xu

  Delay : Type
  Delay = Time → Direction → A
  Boxes : Type
  Boxes = Time → Direction → Interval
  eval : Expr → Delay → A
  eval (cell t d) x = mul (x t d) (x t d)
  eval (plus e f) x = add (eval e x) (eval f x)
  eval (minus e) x = neg (eval e x)
  eval (times n e) x = mul (nat n) (eval e x)
  enclose : Expr → Boxes → Interval
  enclose (cell t d) b = square-I (b t d)
  enclose (plus e f) b = plus-I (enclose e b) (enclose f b)
  enclose (minus e) b = neg-I (enclose e b)
  enclose (times n e) b = scale-I (nat n) (enclose e b)
  sound : (e : Expr) (b : Boxes) (x : Delay)
    → ((t : Time) (d : Direction) → le zero (lower (b t d)))
    → ((t : Time) (d : Direction) → Inside (b t d) (x t d))
    → Inside (enclose e b) (eval e x)
  sound (cell t d) b x positive inside = square-sound (positive t d) (inside t d)
  sound (plus e f) b x positive inside = plus-sound (sound e b x positive inside) (sound f b x positive inside)
  sound (minus e) b x positive inside = neg-sound (sound e b x positive inside)
  sound (times n e) b x positive inside = scale-sound (nat-positive n) (sound e b x positive inside)

  -- alpha is the NONNEGATIVE physical scale 2048/(144*(D*B)^2).
  -- The minus sign reverses endpoints and must not be dropped.
  output-box : A → Component → Boxes → Interval
  output-box alpha c b = neg-I (scale-I alpha (enclose (native-expr c) b))
  output-value : A → Component → Delay → A
  output-value alpha c x = neg (mul alpha (eval (native-expr c) x))
  output-sound : (alpha : A) (c : Component) (b : Boxes) (x : Delay)
    → le zero alpha
    → ((t : Time) (d : Direction) → le zero (lower (b t d)))
    → ((t : Time) (d : Direction) → Inside (b t d) (x t d))
    → Inside (output-box alpha c b) (output-value alpha c x)
  output-sound alpha c b x alpha+ positive inside =
    neg-sound (scale-sound alpha+ (sound (native-expr c) b x positive inside))

-- A checked concrete coefficient model, not merely an uninhabited interface.
import Cubical.Data.Int.Base as Z
import Cubical.Data.Int.Order as O
import Cubical.Data.Int.Properties as P
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver
open Z using (ℤ; pos; _+_; _·_; -_)
neg-left : (a b : ℤ) → ((- b) + a) + (- a) ≡ - b
neg-left a b = solve! ℤCommRing
neg-right : (a b : ℤ) → ((- b) + b) + (- a) ≡ - a
neg-right a b = solve! ℤCommRing
integer-neg-reverses : {a b : ℤ} → a O.≤ b → (- b) O.≤ (- a)
integer-neg-reverses {a} {b} ab = subst2 O._≤_ (neg-left a b) (neg-right a b)
  (O.≤-+o {o = - a} (O.≤-o+ {o = - b} ab))
integer-left : {a b c : ℤ} → pos 0 O.≤ c → a O.≤ b → (c · a) O.≤ (c · b)
integer-left {a} {b} {c} c+ ab = subst2 O._≤_ (P.·Comm a c) (P.·Comm b c) (O.0≤o→≤-·o c+ ab)
integers : OrderedArithmetic
OrderedArithmetic.A integers = ℤ
OrderedArithmetic.zero integers = pos 0
OrderedArithmetic.nat integers = pos
OrderedArithmetic.add integers = Z._+_
OrderedArithmetic.mul integers = Z._·_
OrderedArithmetic.neg integers = Z.-_
OrderedArithmetic.le integers = O._≤_
OrderedArithmetic.reflexive integers = O.isRefl≤
OrderedArithmetic.transitive integers = O.isTrans≤
OrderedArithmetic.nat-positive integers n = O.zero-≤pos
OrderedArithmetic.add-monotone integers = O.≤Monotone+
OrderedArithmetic.neg-reverses integers = integer-neg-reverses
OrderedArithmetic.mul-left integers = integer-left
OrderedArithmetic.mul-right integers = O.0≤o→≤-·o
module IntegerBounds = Bounds integers
clock-delay : Radar.Rows → IntegerBounds.Delay
clock-delay r t d = Z._-_ (Radar.ClockPair.reception (r t d)) (Radar.ClockPair.emission (r t d))
actual-native-expression : (r : Radar.Rows) (c : Component)
  → IntegerBounds.eval (native-expr c) (clock-delay r) ≡ Radar.native-read r c
actual-native-expression r xx = refl
actual-native-expression r xy = refl
actual-native-expression r yy = refl

-- Link absolute reception enclosures to nonnegative fine-grid delay bounds.
-- This extra guard is NOT implied merely by future recorded reception.
import Cubical.Data.Nat.Base as Nat
import RadarClockAdmission as C
record DelayCertificate {k : ℕ} {r : Radar.Rows} (c : C.ClockCertificate k r) : Type where
  field
    low-delay high-delay : C.Grid
    lower-shift : (t : Time) (d : Direction) → C.lower c t d
      ≡ (Nat.suc (C.refinement c) Nat.· (C.slot t Nat.· C.quarter-ticks c)) Nat.+ low-delay t d
    upper-shift : (t : Time) (d : Direction) → C.upper c t d
      ≡ (Nat.suc (C.refinement c) Nat.· (C.slot t Nat.· C.quarter-ticks c)) Nat.+ high-delay t d
open DelayCertificate public
module CertifiedBounds {k : ℕ} {r : Radar.Rows}
  (c : C.ClockCertificate k r) (delays : DelayCertificate c) where
  boxes : IntegerBounds.Boxes
  boxes t d = IntegerBounds.interval (pos (low-delay delays t d)) (pos (high-delay delays t d))
  positive : (t : Time) (d : Direction) → pos 0 O.≤ IntegerBounds.lower (boxes t d)
  positive t d = O.zero-≤pos
  signed-numerator-sound : (component : Component) (x : IntegerBounds.Delay)
    → ((t : Time) (d : Direction) → IntegerBounds.Inside (boxes t d) (x t d))
    → IntegerBounds.Inside (IntegerBounds.output-box (pos 2048) component boxes)
        (IntegerBounds.output-value (pos 2048) component x)
  signed-numerator-sound component x inside =
    IntegerBounds.output-sound (pos 2048) component boxes x O.zero-≤pos positive inside
