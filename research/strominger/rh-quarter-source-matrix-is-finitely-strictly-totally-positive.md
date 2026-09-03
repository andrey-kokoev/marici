# Quarter source matrix is finitely strictly totally positive

## Question

Does determinant-specific total positivity provide the missing source structure behind recurrence positivity?

## Claim boundary

The test exhausts every minor only for matrix size seven and shifts zero through four. It does not prove total positivity at arbitrary size or shift.

## Disposition

All 17,155 exact minors are strictly positive. The census includes every minor size from one through seven; no zero or negative source minor occurs. A deliberate row reversal gives a negative determinant, confirming that sign orientation is tested rather than discarded. This finite structural evidence supports determinant-specific total positivity as the source of recurrence positivity, unlike generic positive recurrence data. The next executable leaf is `quarter-source-matrix-neville-pivots`, testing whether positive Neville-elimination pivots expose a factorization suitable for an all-size proof.
