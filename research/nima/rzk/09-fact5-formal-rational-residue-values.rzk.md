# Formal rational residue values for the five-point biadjoint amplitude

This module interprets each supported cubic residue term as the inverse of its
remaining propagator.  Expressions are formal syntax; no field equality is
assumed.

```rzk
#lang rzk-1

#data MariciFact5RationalExpression
  := marici-rational-zero
  | marici-rational-inverse (channel : MariciFact5Channel)
  | marici-rational-plus
      (left right : MariciFact5RationalExpression)
```

Normalized addition removes formal zero terms during the residue fold.

```rzk
#define marici-rational-add
  ( left right : MariciFact5RationalExpression)
  : MariciFact5RationalExpression
  := match left
      ( marici-rational-zero ⇒ right
      | marici-rational-inverse c ⇒ match right
          ( marici-rational-zero ⇒ left
          | marici-rational-inverse d ⇒ marici-rational-plus left right
          | marici-rational-plus x xh y yh ⇒ marici-rational-plus left right)
      | marici-rational-plus x xh y yh ⇒ match right
          ( marici-rational-zero ⇒ left
          | marici-rational-inverse d ⇒ marici-rational-plus left right
          | marici-rational-plus z zh w wh ⇒ marici-rational-plus left right))
```

The residue of one cubic term is zero when the selected channel is absent and
is the inverse remaining propagator when present.

```rzk
#define marici-fact5-term-residue-value
  ( selected : MariciFact5Channel)
  : MariciFact5PlanarCubicTerm → MariciFact5RationalExpression
  := match selected
      ( marici-channel-13 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-rational-inverse marici-channel-14
          | marici-cubic-term-13-35 ⇒ marici-rational-inverse marici-channel-35
          | marici-cubic-term-14-24 ⇒ marici-rational-zero
          | marici-cubic-term-24-25 ⇒ marici-rational-zero
          | marici-cubic-term-25-35 ⇒ marici-rational-zero)
      | marici-channel-14 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-rational-inverse marici-channel-13
          | marici-cubic-term-13-35 ⇒ marici-rational-zero
          | marici-cubic-term-14-24 ⇒ marici-rational-inverse marici-channel-24
          | marici-cubic-term-24-25 ⇒ marici-rational-zero
          | marici-cubic-term-25-35 ⇒ marici-rational-zero)
      | marici-channel-24 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-rational-zero
          | marici-cubic-term-13-35 ⇒ marici-rational-zero
          | marici-cubic-term-14-24 ⇒ marici-rational-inverse marici-channel-14
          | marici-cubic-term-24-25 ⇒ marici-rational-inverse marici-channel-25
          | marici-cubic-term-25-35 ⇒ marici-rational-zero)
      | marici-channel-25 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-rational-zero
          | marici-cubic-term-13-35 ⇒ marici-rational-zero
          | marici-cubic-term-14-24 ⇒ marici-rational-zero
          | marici-cubic-term-24-25 ⇒ marici-rational-inverse marici-channel-24
          | marici-cubic-term-25-35 ⇒ marici-rational-inverse marici-channel-35)
      | marici-channel-35 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-rational-zero
          | marici-cubic-term-13-35 ⇒ marici-rational-inverse marici-channel-13
          | marici-cubic-term-14-24 ⇒ marici-rational-zero
          | marici-cubic-term-24-25 ⇒ marici-rational-zero
          | marici-cubic-term-25-35 ⇒ marici-rational-inverse marici-channel-25))
```

Linearity over the five planar terms is represented by a normalized fold.

```rzk
#define marici-fact5-amplitude-residue-value
  ( selected : MariciFact5Channel)
  : MariciFact5RationalExpression
  := marici-rational-add
      (marici-fact5-term-residue-value selected marici-cubic-term-13-14)
      (marici-rational-add
        (marici-fact5-term-residue-value selected marici-cubic-term-13-35)
        (marici-rational-add
          (marici-fact5-term-residue-value selected marici-cubic-term-14-24)
          (marici-rational-add
            (marici-fact5-term-residue-value selected marici-cubic-term-24-25)
            (marici-fact5-term-residue-value selected marici-cubic-term-25-35))))
```

All five residues compute to their two lower-point propagator terms.

```rzk
#define marici-fact5-residue-value-13
  : marici-fact5-amplitude-residue-value marici-channel-13
    =_{MariciFact5RationalExpression}
      marici-rational-plus
        (marici-rational-inverse marici-channel-14)
        (marici-rational-inverse marici-channel-35)
  := refl

#define marici-fact5-residue-value-14
  : marici-fact5-amplitude-residue-value marici-channel-14
    =_{MariciFact5RationalExpression}
      marici-rational-plus
        (marici-rational-inverse marici-channel-13)
        (marici-rational-inverse marici-channel-24)
  := refl

#define marici-fact5-residue-value-24
  : marici-fact5-amplitude-residue-value marici-channel-24
    =_{MariciFact5RationalExpression}
      marici-rational-plus
        (marici-rational-inverse marici-channel-14)
        (marici-rational-inverse marici-channel-25)
  := refl

#define marici-fact5-residue-value-25
  : marici-fact5-amplitude-residue-value marici-channel-25
    =_{MariciFact5RationalExpression}
      marici-rational-plus
        (marici-rational-inverse marici-channel-24)
        (marici-rational-inverse marici-channel-35)
  := refl

#define marici-fact5-residue-value-35
  : marici-fact5-amplitude-residue-value marici-channel-35
    =_{MariciFact5RationalExpression}
      marici-rational-plus
        (marici-rational-inverse marici-channel-13)
        (marici-rational-inverse marici-channel-25)
  := refl
```

## Interpretation boundary

Under the interpretation `inverse(channel d) = 1/X_d` and `plus = +`, the
first theorem reads `Res_13 m_5 = 1/X_14 + 1/X_35`.  The present module checks
the exact formal expression but does not yet construct a field-valued
interpretation or prove analytic Laurent-residue laws.
