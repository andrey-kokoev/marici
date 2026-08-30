# Nontrivial-flux orbit selector (WP316)

## Topological domain restriction

Declare a source topology in which the trivial flux sector is absent:

\[
n\in\mathbb Z\setminus\{0\}.
\]

The parameter-free positive energy (E(n)=n^2) then has exactly two literal
minima, (n=\pm1). If upstream exchange identifies (n\sim-n), these form the
single quotient orbit (|n|=1). Thus topology plus energy genuinely selects a
discrete source orbit without a continuous or fitted coefficient.

## Ordered-ratio fiber

The two representatives predict

\[
t_{-1}=1+\sqrt2,
\qquad
t_1=\sqrt2-1,
\]

which are reciprocal. The unordered reciprocal pair is a singleton prediction
on the exchange quotient. The ordered up/down ratio remains twofold.

Choosing one sign requires an orientation or labelled port. That port changes
the experiment and reduces the groupoid to its oriented stabilizer; it does not
recover a pre-existing absolute sign.

## Classification

WP316 is a genuine parameter-free discrete selector on the declared
nontrivial-flux exchange quotient. It is not yet an ordered `physical16`
selector. Physical admission requires a source theorem excluding (n=0), a
legal upstream exchange quotient, and a typed orientation experiment before
matching to labelled Standard Model sectors.

Run `uv run --with sympy python
research/flavor/checkers/wp316_nontrivial_flux_orbit_selector.py` to regenerate
the exact orbit audit.
