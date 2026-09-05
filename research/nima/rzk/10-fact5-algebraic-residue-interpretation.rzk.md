# Algebraic interpretation of five-point residue expressions

Formal residue expressions are evaluated in an arbitrary carrier with zero,
addition, and a supplied inverse-propagator value for each channel.  No field
laws are needed for the five computed identities.

```rzk
#lang rzk-1

#define marici-evaluate-fact5-rational-expression
  ( A : U)
  ( zero : A)
  ( add : A → A → A)
  ( inverse-propagator : MariciFact5Channel → A)
  ( expression : MariciFact5RationalExpression)
  : A
  := match expression
      ( marici-rational-zero ⇒ zero
      | marici-rational-inverse channel ⇒ inverse-propagator channel
      | marici-rational-plus left left-value right right-value ⇒
          add left-value right-value)
```

Evaluation sends each checked formal residue to the corresponding sum of two
lower-point inverse propagators.

```rzk
#define marici-evaluated-fact5-residue-13
  ( A : U)
  ( zero : A)
  ( add : A → A → A)
  ( inverse-propagator : MariciFact5Channel → A)
  : marici-evaluate-fact5-rational-expression A zero add inverse-propagator
      (marici-fact5-amplitude-residue-value marici-channel-13)
    =_{A} add
      (inverse-propagator marici-channel-14)
      (inverse-propagator marici-channel-35)
  := refl

#define marici-evaluated-fact5-residue-14
  ( A : U)
  ( zero : A)
  ( add : A → A → A)
  ( inverse-propagator : MariciFact5Channel → A)
  : marici-evaluate-fact5-rational-expression A zero add inverse-propagator
      (marici-fact5-amplitude-residue-value marici-channel-14)
    =_{A} add
      (inverse-propagator marici-channel-13)
      (inverse-propagator marici-channel-24)
  := refl

#define marici-evaluated-fact5-residue-24
  ( A : U)
  ( zero : A)
  ( add : A → A → A)
  ( inverse-propagator : MariciFact5Channel → A)
  : marici-evaluate-fact5-rational-expression A zero add inverse-propagator
      (marici-fact5-amplitude-residue-value marici-channel-24)
    =_{A} add
      (inverse-propagator marici-channel-14)
      (inverse-propagator marici-channel-25)
  := refl

#define marici-evaluated-fact5-residue-25
  ( A : U)
  ( zero : A)
  ( add : A → A → A)
  ( inverse-propagator : MariciFact5Channel → A)
  : marici-evaluate-fact5-rational-expression A zero add inverse-propagator
      (marici-fact5-amplitude-residue-value marici-channel-25)
    =_{A} add
      (inverse-propagator marici-channel-24)
      (inverse-propagator marici-channel-35)
  := refl

#define marici-evaluated-fact5-residue-35
  ( A : U)
  ( zero : A)
  ( add : A → A → A)
  ( inverse-propagator : MariciFact5Channel → A)
  : marici-evaluate-fact5-rational-expression A zero add inverse-propagator
      (marici-fact5-amplitude-residue-value marici-channel-35)
    =_{A} add
      (inverse-propagator marici-channel-13)
      (inverse-propagator marici-channel-25)
  := refl
```

## Interpretation boundary

Taking `A` to be a rational-function field and `inverse-propagator(d)` to be
`1/X_d` yields the standard five-point biadjoint residue values.  This module
proves interpretation of the formal syntax in any supplied algebra, but it does
not construct that rational-function field or an analytic residue operator.
