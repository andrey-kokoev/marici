# Global integer distributivity readback

The distributive theorem was already assembled in module 70 from the
all-multiplier mixed family. These typed readback aliases connect that existing
closure to the newer global interface used by the rational-normalization lane.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-left-distrib-closed
  ( x y z : MariciInt)
  : MariciIntLeftDistributes x y z
  := marici-int-mul-add-left-distrib x y z

#define marici-int-right-distrib-closed
  ( x y z : MariciInt)
  : marici-int-mul (marici-int-add y z) x
    =_{MariciInt}
    marici-int-add (marici-int-mul y x) (marici-int-mul z x)
  := marici-int-mul-add-right-distrib y z x
```

## Boundary

Global integer distributivity was not an open theorem: module 70 already
closed it. The actual remaining additive frontier is therefore raw-fraction
addition congruence and associativity using these integer laws. No duplicate
definition remains.
