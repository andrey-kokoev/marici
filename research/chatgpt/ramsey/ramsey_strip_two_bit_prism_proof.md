# Why R3 and F5 decode the prefix

Normalize adjacent endpoint midpoints to A,D on the folded square prism. Label columns cyclically a,b,c,d. Capitals are midpoints; lowercase letters are corners on the current rim. A ten-visit simple half-route starts A,a and ends d,D. The only internal switches are B,C. F marks a,B,C and R marks d,B,C.

With k internal switches the ten positions include 2+k midpoints and 8-k corners, distributed among k+1 rim runs. Zero switches cannot visit eight distinct corners on one rim. With one switch there are seven corners, hence runs of lengths 3 and 4. On a square a run of three connects opposite columns, and one of four connects adjacent columns by the long way. Via B the run lengths are 4 then 3 (A adjacent to B, B opposite D); via C they are 3 then 4. With two switches the six corners must divide 2+2+2 (distinct endpoint columns on each run). This forces A–B–C–D, since A–C is not adjacent.

Consequently the possible prefixes, up to initial rim, are the following (visit counting starts at A):

|switch itinerary|visits 1–7|R3|F5|step-eight reservation length|
|--|--|--|--|--|
|B,C|A a b B b c C|0|0|2|
|C via b|A a b c C c b|0|1|2|
|B|A a d c b B b|1|0|3|
|C via d|A a d c C c b|1|1|1|

The class follows from the prefix, with the previously established forced chains (ramsey_strip_turn_reservation_chain.py). No orbit census is needed to distinguish the four shapes. R3 tests first turn toward D; F5=R5 tests use of switch C at 5. Bits identify templates, not raw vertex labels or closure.