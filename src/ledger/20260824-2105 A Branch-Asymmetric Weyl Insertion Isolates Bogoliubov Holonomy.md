# 2105 — A Branch-Asymmetric Weyl Insertion Isolates Bogoliubov Holonomy

## Question

Entry 2104 showed that native Schwinger–Keldysh doubling retains the
Bogoliubov phase only in its off-diagonal history sector.  Test whether a
fixed Gaussian observable exposes that phase or absorbs it into an arbitrary
insertion normalization.

## Frozen insertion

At the squeezed base point of Entry 2101,

\[
V_{qq}=\frac1{18}.
\]

Insert on the forward branch only the Weyl observable

\[
W=e^{iq}.
\]

For the centered Gaussian state, the source-normalized characteristic function
is

\[
\chi=\langle W\rangle
=\exp\left(-\frac{V_{qq}}2\right)
=e^{-1/36}.
\]

In particular, \(\chi\ne0\).

## Loop and reference amplitudes

Let

\[
g=e^{-16\pi i/9}
\]

be the state-line holonomy.  The off-diagonal amplitudes are

\[
F_{\rm loop}=g\chi,
\qquad
F_{\rm ref}=\chi.
\]

Therefore

\[
\boxed{
\frac{F_{\rm loop}}{F_{\rm ref}}=g.
}
\]

The insertion magnitude cancels exactly.  A Hermitian interference readout
contains

\[
\operatorname{Re}F_{\rm loop}
=e^{-1/36}\cos(16\pi/9),
\]

which differs from the identity-history reference.

## Narrow result

\[
\boxed{
\text{a fixed branch-asymmetric Gaussian insertion isolates the state-line
holonomy independently of its own nonzero normalization.}
}
\]

The surviving phase is therefore a genuine coefficient-plus-readout effect in
this finite SK model.  It is neither covariance data nor a new Carrier
incidence.

The architecture is now explicit:

\[
\text{SK occurrence pair}
+\text{state-line transport}
+\text{nonzero asymmetric characteristic}
\longrightarrow
\text{normalized phase readout}.
\]

## Limitation and next falsifier

The Weyl insertion was source-fixed but not yet derived from a specific
cosmological observable.  The next gate is a Bunch–Davies wavefunction or
in-in correlator whose actual external source derivative produces the same
off-diagonal characteristic.  If all admitted cosmological observables pair
only diagonally, this activation remains a valid quantum model but not a
cosmological prediction.

## Durable evidence

- `research/benincasa/checkers/bogoliubov_sk_weyl_insertion.py`
- `research/benincasa/checkers/results/bogoliubov-sk-weyl-insertion.json`
- Ledger allocation: `seqclaim-c68da2d250a52e935f45430c`

