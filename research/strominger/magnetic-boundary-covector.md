# The even Casimir pivot is carried by a finite collision covector

Let `A` be the preceding stable Hall block and let `c` be its values on the new
plus observation row.  Define the normalized boundary covector

\[
\lambda=-cA^{-1},
\]

and give the new plus row coefficient one.  By construction,

\[
\lambda A+c=0,
\]

so this functional descends to the quotient by every old column.

For even `q=2w`, exact elimination shows that `lambda` is not spread across the
growing old matrix.  Its support is exactly

\[
\boxed{
r_+-1,\ r_+-3,\ldots,r_+-(2w-1).
}
\]

These are the `w` rows in the endpoint-collision chain.  The support is
independent of the Laurent cutoff once stability begins.

Evaluating the new plus column against the quotient covector gives

\[
\boxed{
(-1)^gqg(g+3)a^{\overline{g-1}}.
}

This places the boundary-Casimir formula inside the actual matrix elimination:

- the boundary primitive is the finite solve along the `w=q/2` collision rows;
- the quadratic Casimir is the final evaluation on the newly transported path;
- all rows outside this collision chain cancel identically.

At `q=2`, the covector has one old-row coefficient.  Deleting even that single
term leaves the raw `B1` value and fails to produce the Casimir pivot, providing
a minimal falsifier.

The checker verifies this exact support and evaluation on 164 stable extensions
with grades 2 through 8 and even depths 2 through 12. Four preferred-chart
zeros at `(g,q)=(2,12)` are classified separately. The remaining symbolic
task is now a fixed collision-chain recurrence: derive the `w` covector
coefficients recursively from the order-four column law and evaluate their
telescoping sum without using `A^{-1}`.
