# Exhaustive five-gon dissection type and the face above diagonal 13

This module replaces the previously postulated three face constructors by a
classification inside the full eleven-element five-gon dissection type.

```rzk
#lang rzk-1

#data MariciFact5Dissection
  := marici-fact5-empty
  | marici-fact5-only13
  | marici-fact5-only14
  | marici-fact5-only24
  | marici-fact5-only25
  | marici-fact5-only35
  | marici-fact5-tri-13-14
  | marici-fact5-tri-13-35
  | marici-fact5-tri-14-24
  | marici-fact5-tri-24-25
  | marici-fact5-tri-25-35

#data MariciFact5Unit
  := marici-fact5-unit

#data MariciFact5Empty

#define marici-fact5-empty-elim
  ( A : U)
  ( impossible : MariciFact5Empty)
  : A
  := ind-MariciFact5Empty (\ _ → A) impossible
```

Containment of diagonal `13` is computed by exhaustive dissection analysis.
The three valid cases return a singleton witness and all other cases return the
empty type.

```rzk
#define MariciFact5Contains13
  ( dissection : MariciFact5Dissection)
  : U
  := match dissection
      ( marici-fact5-empty ⇒ MariciFact5Empty
      | marici-fact5-only13 ⇒ MariciFact5Unit
      | marici-fact5-only14 ⇒ MariciFact5Empty
      | marici-fact5-only24 ⇒ MariciFact5Empty
      | marici-fact5-only25 ⇒ MariciFact5Empty
      | marici-fact5-only35 ⇒ MariciFact5Empty
      | marici-fact5-tri-13-14 ⇒ MariciFact5Unit
      | marici-fact5-tri-13-35 ⇒ MariciFact5Unit
      | marici-fact5-tri-14-24 ⇒ MariciFact5Empty
      | marici-fact5-tri-24-25 ⇒ MariciFact5Empty
      | marici-fact5-tri-25-35 ⇒ MariciFact5Empty)
```

Encoding inserts the three-element residual face into the full dissection
type and supplies its containment witness.

```rzk
#define marici-face13-encode-dissection
  ( face : MariciFact5Face13)
  : MariciFact5Dissection
  := match face
      ( marici-face13-unrefined ⇒ marici-fact5-only13
      | marici-face13-add14 ⇒ marici-fact5-tri-13-14
      | marici-face13-add35 ⇒ marici-fact5-tri-13-35)

#define marici-face13-encode-contains
  ( face : MariciFact5Face13)
  : MariciFact5Contains13 (marici-face13-encode-dissection face)
  := match face
      ( marici-face13-unrefined ⇒ marici-fact5-unit
      | marici-face13-add14 ⇒ marici-fact5-unit
      | marici-face13-add35 ⇒ marici-fact5-unit)
```

Decoding proves exhaustion: every full five-gon dissection carrying `13` is
one of the three face constructors.  Impossible branches eliminate their empty
containment witness.

```rzk
#define marici-face13-decode
  ( dissection : MariciFact5Dissection)
  : MariciFact5Contains13 dissection → MariciFact5Face13
  := match dissection into
      (\ current → MariciFact5Contains13 current → MariciFact5Face13)
      ( marici-fact5-empty ⇒
          \ impossible → marici-fact5-empty-elim MariciFact5Face13 impossible
      | marici-fact5-only13 ⇒ \ _ → marici-face13-unrefined
      | marici-fact5-only14 ⇒
          \ impossible → marici-fact5-empty-elim MariciFact5Face13 impossible
      | marici-fact5-only24 ⇒
          \ impossible → marici-fact5-empty-elim MariciFact5Face13 impossible
      | marici-fact5-only25 ⇒
          \ impossible → marici-fact5-empty-elim MariciFact5Face13 impossible
      | marici-fact5-only35 ⇒
          \ impossible → marici-fact5-empty-elim MariciFact5Face13 impossible
      | marici-fact5-tri-13-14 ⇒ \ _ → marici-face13-add14
      | marici-fact5-tri-13-35 ⇒ \ _ → marici-face13-add35
      | marici-fact5-tri-14-24 ⇒
          \ impossible → marici-fact5-empty-elim MariciFact5Face13 impossible
      | marici-fact5-tri-24-25 ⇒
          \ impossible → marici-fact5-empty-elim MariciFact5Face13 impossible
      | marici-fact5-tri-25-35 ⇒
          \ impossible → marici-fact5-empty-elim MariciFact5Face13 impossible)
```

The face-to-dissection-to-face composite computes exactly.

```rzk
#define marici-face13-decode-encode
  ( face : MariciFact5Face13)
  : marici-face13-decode
      (marici-face13-encode-dissection face)
      (marici-face13-encode-contains face)
    =_{MariciFact5Face13} face
  := match face
      ( marici-face13-unrefined ⇒ refl
      | marici-face13-add14 ⇒ refl
      | marici-face13-add35 ⇒ refl)
```

## Boundary

The eleven constructors are an exhaustive finite fixture by declaration.  The
next generic step must derive them from finite noncrossing diagonal families;
this module does not yet prove that the declared list equals that generic type.
