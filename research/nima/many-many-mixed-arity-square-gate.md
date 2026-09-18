# Many-many mixed-arity square gate

Let `U` be unary input formation, `M` many-input formation, `V` unary output formation, and `N` many-output formation. The first mixed-arity square compares

$$
V\circ M
\qquad\text{and}\qquad
N\circ U.
$$

On the labelled common core, require a typed comparison cell

$$
\beta_{MN}:V M\Longrightarrow N U
$$

preserving prime, shell, ordered-pair, endpoint, and wall/jump coordinates.

The second square compares

$$
V\circ U
\qquad\text{and}\qquad
N\circ M,
$$

with its own cell `beta_UN`. Their shared boundary restrictions must agree with the order-exchange cell `beta` and with the Hadamard transport.

The square equations are checked before scalar codiagonalization. Any nonzero discrepancy is retained as a relative face-curvature class and must satisfy the three-direction Bianchi relation.

Status: first mixed-arity square gate specified; source maps and comparison cells remain open.
