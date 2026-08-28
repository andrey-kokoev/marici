# A flat mixed cell does not make the Bockstein line horizontal

Benincasa's 960 labelled commutation checks establish that the mixed gamma–kinematic cell has the required coherence type. They do not establish that the rank-one Bockstein line is preserved by either kinematic connection.

The minimal hostile uses a three-dimensional space with basis `b, q_x, q_y` and distinguished line `L = span(b)`. Define constant connection operators by

```text
A_x(b) = q_x,    A_y(b) = q_y,
A_x(q_x) = A_x(q_y) = A_y(q_x) = A_y(q_y) = 0.
```

Then `A_x A_y = A_y A_x = 0`, so the mixed curvature vanishes exactly. Nevertheless, the images of `b` in `V/L` are the two nonzero independent vectors `q_x` and `q_y`. Thus `L` is non-horizontal in both directions.

The next admissible calculation must therefore export, for each parameter direction, the actual connection image of the source-normalized Bockstein generator and its reduction modulo the same transported Bockstein line. Vanishing ordinary first jets or mixed commutation cannot substitute for these two quotient residuals.

The executable hostile is `checkers/check_flat_mixed_cell_nonhorizontal_line_hostile.py`.
