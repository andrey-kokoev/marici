# Muon–tau visible-mass shape (WP253)

## Preregistered physical probe

Retain WP251 unchanged and choose the coherent offline pair minimizing summed
trigger-match `Delta R`. Measure its visible invariant mass in bins fixed
before inspection:

\[
[0,50,80,110,140,200,\infty)\ \mathrm{GeV}.
\]

The 140-GeV signal pilot gives `[11,199,159,20,0,0]`. The combined raw
DY+top+W pilot gives `[11,19,2,1,3,3]`.

## Exact contextual result

The six-bin signal/background response has rank two. Its ordinary rate
projection—summing the bins—has rank one. One exact nonzero minor is already
enough, and the tail support is especially hostile:

\[
m_{\mu\tau_h}\ge140\ \mathrm{GeV}:\qquad (S_{140},B)=(0,6).
\]

Thus this source-derived physical shape probe separates the 140-GeV signal
pilot from the admitted simulated-background pilot even though the rate readout
cannot. It is a finite-pilot instance of complementary probes repairing a
nonfaithful projection.

## Claim boundary

WP253 does not establish discovery power, precision weighted shapes, QCD
control, or separation of the two flavor-source poles. It supplies one
signal/background shape direction. The next exact gate is to import the frozen
130- and 160-GeV signal pilots and test whether their columns remain independent
after adjoining background and declared uncertainties.

Run `uv run --with sympy python
research/flavor/checkers/wp253_mu_tau_visible_mass_shape.py` for the exact rank,
rate collapse, and deliberate proportionality failure.
