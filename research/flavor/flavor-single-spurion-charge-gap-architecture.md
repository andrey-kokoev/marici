# A single-spurion charge grammar forces the flavor hierarchy powers

Work package: WP614  
Owner: marici.Figueiredo

## Conditional source architecture

Take one Froggatt--Nielsen-type flavon spurion

\[
\epsilon={\langle\phi\rangle\over M}
\]

and three ordered flavor charges

\[
q=(3,2,0).
\]

If a transition between ports (i,j) requires one spurion insertion per unit
charge gap, its amplitude exponent is

\[
n_{ij}=|q_i-q_j|.
\]

The resulting matrix is

\[
n=\begin{pmatrix}
0&1&3\\
1&0&2\\
3&2&0
\end{pmatrix}.
\]

This is exactly the Wolfenstein hierarchy pattern. In particular,
(n_{13}=n_{12}+n_{23}), so the long transition is a three-link composite of
the one- and two-link gaps. Once the charges and one-spurion grammar are
admitted, these powers cannot be varied continuously.

## CP scaling

Write the standard mixing sines as

\[
s_{12}=c_{12}\epsilon,
\qquad
s_{23}=c_{23}\epsilon^2,
\qquad
s_{13}=c_{13}\epsilon^3.
\]

Exact CKM unitarity gives

\[
J=\epsilon^6 c_{12}c_{23}c_{13}
\sqrt{1-c_{12}^2\epsilon^2}
\sqrt{1-c_{23}^2\epsilon^4}
(1-c_{13}^2\epsilon^6)\sin\delta.
\]

Thus the discrete charge grammar forces the small CP scale (J=O(\epsilon^6))
without inserting the observed (J) itself. With (epsilon=|V_{us}|), all
six quoted off-diagonal magnitudes and the central (J) have residual
coefficients between (0.2) and (5). The architecture is compatible with
the observed hierarchy at the order-one level.

## Exact remaining fibers

The exponent law is not a numerical selector. At fixed charges,
(epsilon=1/5), and unit magnitude coefficients, the choices

\[
\delta=0,
\qquad
\delta=\pi/2
\]

give respectively (J=0) and (J\ne0). Likewise changing (c_{13}) from one
to two doubles the leading 1--3 amplitude without changing any charge,
representation or messenger depth.

Therefore the architecture is:

- a conditional hierarchy selector;
- a messenger-topology rigidifier;
- not a numerical `physical16` selector;
- not a CP selector.

It explains why small quantities occur at powers (1,2,3,6), but not their
order-one coefficients or the CP phase.

## Source-authority gate

The charge vector is currently recognized from the observed hierarchy. That
is not independent source authority. A progressive completion must derive
((3,2,0)), up to a common shift and reversal, from anomaly cancellation,
representation theory, a source vacuum, or another pre-flavor rule.

The existing renormalizable messenger programme shows how finite messenger
chains can generate flavon words, but its degree-two grammar spans arbitrary
matrices once coefficients are free. WP614 instead requires a single charge
grammar that forbids shorter paths and relates messenger depth across all
three transitions.

## Independently executable criticism

The threshold experiment must test constructor topology rather than infer
powers from one low-energy point. It should resolve:

- the flavon and its charge-changing coupling;
- one-, two-, and three-stage vectorlike messenger paths;
- absence of a shorter path for the 1--3 operator;
- the matched low-energy coefficients in the same source/readout frame.

The smallest topology falsifier is a 1--3 operator generated with fewer than
three spurion insertions. A second falsifier is any independently calibrated
Wilson coefficient outside the declared order-one corridor. CP violation
requires a separate source-derived phase mechanism and sign-sensitive
interference instrument.

No such resolved threshold experiment is currently admitted. The packet
therefore identifies the strongest conditional source architecture and its
physical test, not a completed explanation.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp614_single_spurion_charge_gap_architecture.py

The generated result is
research/flavor/results/wp614_single_spurion_charge_gap_architecture.json.
