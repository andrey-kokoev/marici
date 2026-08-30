# Primitive Ward Current Selects a Channel but Not Its Coupling

## Question

Can WP820's one-dimensional oriented integer kernel supply the unique physical
effective-charge channel demanded by WP830, and does Ward normalization then
protect the portal magnitude through thresholds?

## Canonical current channel

The incidence map

\[
B=
\begin{pmatrix}
2&-1&0\\
3&0&-1
\end{pmatrix}
\]

has the primitive kernel generator

\[
q=(1,2,3)^T.
\]

The oriented cubic inflow \(q_1^3+q_2^3+q_3^3=36\) rejects \(-q\). Thus,
conditional on the authority of \(B\) and the oriented bulk, the source does
select one primitive linear current and the positive unit contrast

\[
q_3-q_2=1.
\]

This repairs WP830's channel ambiguity at the linear Ward-current level.
Primitivity forbids arbitrary rescaling of the charge vector.

## Spectral response

In the finite equal-weight current packet, the active spectral index is

\[
S=q^Tq=14.
\]

The normalized current two-point strength has the form

\[
C=Se^2.
\]

For a frozen complete spectrum and \(e>0\), this record is injective in the
coupling. It is therefore a legitimate formal magnitude readout, unlike an
unnamed effective-charge channel. It still reads the realized coupling; it
does not select its numerical value.

## Threshold fiber

Add an anomaly-neutral vectorlike pair with current charges \((r,-r)\). It
contributes zero to both linear and cubic anomalies but changes the spectral
index by

\[
2r^2.
\]

Continuity of the same Ward-current response across decoupling allows

\[
(14+2r^2)e_{\rm high}^2=14e_{\rm low}^2,
\qquad
e_{\rm low}=\sqrt{\frac{14+2r^2}{14}}e_{\rm high}.
\]

For the unit pair, the coupling and hence the unit portal contrast change by
\(\sqrt{8/7}\). Ward identity and anomaly matching preserve the current and
its charge assignments, not the numerical effective coupling.

The inverse readout also has an exact open-spectrum fiber:

\[
(S,e)=(14,1),
\qquad
(S,e)=\left(16,\sqrt{\frac78}\right)
\]

produce the same current record \(C=14\).

## Contextual classification

The admitted state domain consists of the WP820 oriented rank-one current
kernel, positive coupling, and anomaly-neutral vectorlike spectral
completions. The faithful coordinate is the primitive current together with
the complete active spectral index and coupling.

On a fixed spectrum, the unique current record separates positive coupling
values. On the open completion domain it identifies only \(Se^2\). Therefore:

- the operation selects a current channel;
- it rigidifies the primitive charge and sign;
- it does not select coupling magnitude or an RG basin;
- its numerical threshold survival fails;
- its current correlator is not yet a calibrated `physical16` instrument.

## Smallest exact falsifier

The packets \((14,1)\) and \((16,\sqrt{7/8})\) share current response 14.
The latter differs only by the smallest anomaly-neutral vectorlike completion.
This is the first exact hostile after granting a unique primitive Ward current.

## Required source principle

The remaining constructor must make the full active spectrum, including every
anomaly-neutral sector and its mass, unavoidable; derive a controlled
interacting RG basin for its canonically normalized current; and carry the
current correlator through thresholds into one calibrated physical16
instrument. Current uniqueness alone supplies none of those arrows.

## Disposition

Progressive channel selection with a negative magnitude result. The oriented
primitive kernel supplies the canonical current missing in WP830, but Ward
normalization and anomaly matching do not fix the coupling or protect it
through spectral thresholds.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp831_primitive_ward_current_threshold_fiber.py
```
