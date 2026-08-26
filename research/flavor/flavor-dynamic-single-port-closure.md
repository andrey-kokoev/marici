# Dynamic single-port closure (WP278)

## Source-generated time tower

WP276 and WP277 close only static one-port sensing and actuation. Introduce the
source drift

\[
A=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
C=\begin{pmatrix}1&0\end{pmatrix},
\qquad
B=\begin{pmatrix}1\\0\end{pmatrix}.
\]

Both instantaneous ports have rank one. The time-resolved observation tower is

\[
\begin{pmatrix}C\\CA\end{pmatrix}
=\begin{pmatrix}1&0\\0&1\end{pmatrix},
\]

so the readout pair \((y,\dot y)=(z_1,z_2)\) reconstructs the complete state.
The control tower

\[
\begin{pmatrix}B&AB\end{pmatrix}
=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\]

also has rank two.

## Exact stabilization

With one-input state feedback \(K=(2,0)\), the closed-loop characteristic
polynomial is \((\lambda+1)^2\). A one-output observer with gain
\(L=(2,0)^T\) has the same stable error polynomial. One sensor and one actuator
therefore suffice dynamically because the source drift rotates the hidden
direction into each port.

## Classification and authority

This is a conditional positive architecture: a source-generated time tower can
restore information and control absent from every instantaneous projection.
It uses neither an invented complementary row nor an external reference port.
But algebraic matrices are not yet executable flavor control. Progress requires
a dynamical flavon substrate realizing the drift, a time-resolved sensor,
actuator coupling, clock, bandwidth, noise calibration, and repeatable
stabilization on `physical16`.

Run `uv run --with sympy python
research/flavor/checkers/wp278_dynamic_single_port_closure.py` for exact
observability, reconstruction, controllability, feedback, and observer checks.
