{-# OPTIONS --safe --cubical --guardedness #-}
module SeedPortResponseDescentGate where

open import Cubical.Foundations.Prelude hiding (Path)
import ActualSeedEndpointTable as Seed
import SeedSeamPathComparisonBoundary as Paths
import SeedFirstReturnActions as Actions
import SeedCompositionPortQuotient as Ports

open Seed using (Vertex; Occurrence; source; target; A; B; C; D; AB; BC; CA; AD; DB; BA)
open Paths using (stop; step)

-- A conditional test of the EXISTING effect interpretation interface.
-- No primitive response or physical observation is selected here.
module Gate (X : Vertex → Type)
  (act : (e : Occurrence) → X (source e) → X (target e))
  (cancel : (e : Occurrence) (x y : X (source e)) → act e x ≡ act e y → x ≡ y) where
  module E = Actions.Effects X act

  -- A necessary condition for an effect reader to factor through typed ports.
  -- Exact histories continue to be retained; this condition is only about
  -- interpreting the CURRENT response as a function of the coarse port.
  PortCompatible : Type
  PortCompatible = {s t : Vertex} (p q : Ports.Positive s t)
    → Ports.read p ≡ Ports.read q → (a : X s)
    → E.run (Ports.word p) a ≡ E.run (Ports.word q) a

  single : (e : Occurrence) → Ports.Positive (source e) (target e)
  single e = Ports.nonempty e stop

  extension-same-port : (e : Occurrence) {s : Vertex}
    (p q : Ports.Positive s (source e))
    → Ports.read (Ports.join p (single e)) ≡ Ports.read (Ports.join q (single e))
  extension-same-port e p q = Ports.composition-square p (single e)
    ∙ sym (Ports.composition-square q (single e))

  extension-effect : (e : Occurrence) {s : Vertex}
    (p : Ports.Positive s (source e)) (a : X s)
    → E.run (Ports.word (Ports.join p (single e))) a ≡ act e (E.run (Ports.word p) a)
  extension-effect e p a = cong (λ w → E.run w a) (Ports.join-word p (single e))
    ∙ E.run-append (Ports.word p) (Ports.word (single e)) a

  cancel-after : PortCompatible → (e : Occurrence) {s : Vertex}
    (p q : Ports.Positive s (source e)) (a : X s)
    → E.run (Ports.word p) a ≡ E.run (Ports.word q) a
  cancel-after compatible e p q a = cancel e _ _
    (sym (extension-effect e p a)
      ∙ compatible (Ports.join p (single e)) (Ports.join q (single e))
          (extension-same-port e p q) a
      ∙ extension-effect e q a)

  -- The actual seed has an outgoing occurrence at every vertex. Hence the
  -- argument applies to ALL positive parallel paths, not only one witness.
  parallel-effects-agree : PortCompatible → {s t : Vertex}
    (p q : Ports.Positive s t) (a : X s)
    → E.run (Ports.word p) a ≡ E.run (Ports.word q) a
  parallel-effects-agree compatible {t = A} = cancel-after compatible AB
  parallel-effects-agree compatible {t = B} = cancel-after compatible BC
  parallel-effects-agree compatible {t = C} = cancel-after compatible CA
  parallel-effects-agree compatible {t = D} = cancel-after compatible DB

  forward0 forward1 : Ports.Positive A B
  forward0 = Ports.nonempty AB stop
  forward1 = Ports.nonempty AD (step DB stop)
  return0 return1 : Ports.Positive B A
  return0 = Ports.nonempty BA stop
  return1 = Ports.nonempty BC (step CA stop)

  forward-comparison : PortCompatible → E.ForwardEffectComparison
  forward-comparison compatible = parallel-effects-agree compatible forward0 forward1

  return-comparison : PortCompatible → E.ReturnEffectComparison
  return-comparison compatible = parallel-effects-agree compatible return0 return1

  -- The FOUR actual return effects agree under that hypothesis. This
  -- supplies the precise gate for any proposed downstream response reader.
  module Consequences (compatible : PortCompatible) where
    module Square = E.WithComparisons
      (forward-comparison compatible) (return-comparison compatible)

    all-corners-agree : (a : X A) → E.run Actions.r00 a ≡ E.run Actions.r11 a
    all-corners-agree a = Square.compare-00-10 a ∙ Square.compare-10-11 a

    every-reader-agrees : {Y : Type} (reader : X A → Y) (a : X A)
      → reader (E.run Actions.r00 a) ≡ reader (E.run Actions.r11 a)
    every-reader-agrees reader a = cong reader (all-corners-agree a)

-- Injectivity is weaker than invertibility. The conclusion is conditional
-- on both primitive cancellation AND factoring the response through ports.
-- Noninjective arrival updates are not covered by the cancellation premise.
-- No equality between the underlying free paths has been asserted.
