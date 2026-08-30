# The Hostile Cosh Pair Collapses to the Seam at Square-Root Rate

Grothendieck's exact finite-shell model is

\[
F_c(z)=\cosh z+c\cosh 2z,
\qquad c>0.
\]

Writing \(y=\cosh z\) reduces its zero equation to

\[
2cy^2+y-c=0.
\]

The negative root is

\[
y_-(c)=-a(c),
\qquad
a(c)=\frac{1+\sqrt{1+8c^2}}{4c}.
\]

For \(0<c<1\), one has \(a(c)>1\). It therefore produces the off-seam
pair

\[
z=\pm\alpha(c)+i\pi \pmod{2\pi i},
\qquad
\alpha(c)=\operatorname{arcosh}a(c)>0.
\]

At the sharp threshold \(c=1\), \(a(1)=1\), so this pair collides with the
seam. The collision is not linear. Since

\[
a'(1)=-\frac13,
\]

putting \(c=1-\varepsilon\) gives

\[
a(1-\varepsilon)
=1+\frac{\varepsilon}{3}+O(\varepsilon^2).
\]

Using \(\operatorname{arcosh}(1+u)^2=2u+O(u^2)\),

\[
\alpha(1-\varepsilon)^2
=\frac{2}{3}\varepsilon+O(\varepsilon^2),
\qquad
\alpha(1-\varepsilon)
\sim\sqrt{\frac{2\varepsilon}{3}}.
\]

Thus the hostile pair approaches the seam at square-root rate.

## Completion-created confinement

Take

\[
c_N=1-\frac1N,
\qquad N\ge2.
\]

Every finite stage has an off-seam pair, yet

\[
\operatorname{dist}(z_N,\text{seam})
=\alpha(c_N)
\sim\sqrt{\frac{2}{3N}}
\longrightarrow0.
\]

The limiting function at \(c=1\) is seam-confined even though no member of
the approximating sequence is. Consequently:

- finite zero-free or finite coherence certificates cannot be inferred from
  confinement of the limit;
- finite hostility does not imply a hostile limit without a uniform
  off-seam separation;
- the missing completion theorem must control inverse norms or zero distance,
  not merely pointwise coefficient convergence;
- a source mechanism may resolve the obstruction either by forcing a genuine
  threshold crossing or by supplying nonlocal terms absent from the two-shell
  truncation.

This is the zero-set analogue of a spectral gap collapsing under completion.
The relevant falsifier is a sequence of normalized bad states whose defect
remains nonzero at every cutoff but tends to zero without a uniform lower
bound.

## What this does not prove

This calculation does not identify the theta/Tate completion with the cosh
family. It does not prove that the completed RH source reaches \(c=1\), nor
that its remaining shells have the required phase coherence. It proves the
minimal mechanism by which all finite stages can be hostile while the limit
first becomes confined, and it supplies the exact scale that any purported
uniform finite obstruction must beat.

## Falsifiers

- Claiming that off-seam zeros at every finite stage force an off-seam zero in
  the limit without a uniform separation theorem.
- Claiming linear approach to the seam in this family.
- Treating coefficient convergence as uniform invertibility.
- Importing the threshold \(c=1\) into the theta/Tate source without deriving
  its effective shell coefficient and normalization.
- Using the scalar zero equation to manufacture the missing source
  constructor.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to quantify the exact route by which finite hostility can
disappear only at completion.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The hostile pair has an exact square-root collision law, isolating the
missing requirement as uniform off-seam separation or a source-derived
completion mechanism.
