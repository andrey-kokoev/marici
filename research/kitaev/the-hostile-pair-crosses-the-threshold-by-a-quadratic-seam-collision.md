# The Hostile Pair Crosses the Threshold by a Quadratic Seam Collision

For

\[
F_c(z)=\cosh z+c\cosh 2z,
\]

the hostile pair reaches \(z=i\pi\) at \(c=1\). This is not annihilation of
the divisor. It is a multiplicity-two collision followed by continuation
along the seam.

Set

\[
z=i\pi+w,
\qquad
c=1+\delta.
\]

Then

\[
F_{1+\delta}(i\pi+w)
=-\cosh w+(1+\delta)\cosh 2w
\]

and hence

\[
F_{1+\delta}(i\pi+w)
=\delta+left(\frac32+2\delta\right)w^2+O(w^4).
\]

At the collision point,

\[
F=0,
\qquad
F_z=0,
\qquad
F_{zz}=3,
\qquad
F_c=1.
\]

The local Weierstrass equation is therefore

\[
w^2=-\frac23\delta+O(\delta^2).
\]

For \(\delta<0\), the two roots have real transverse displacement

\[
w_\pm
=\pm\sqrt{\frac{2(1-c)}3}+O((1-c)^{3/2}),
\]

and are off the seam. For \(\delta>0\), they have imaginary tangent
displacement

\[
w_\pm
=\pm i\sqrt{\frac{2(c-1)}3}+O((c-1)^{3/2}),
\]

and both lie on the seam.

## Exact continuation

With

\[
a(c)=\frac{1+\sqrt{1+8c^2}}{4c},
\]

one has \(a(c)>1\) for \(0<c<1\) and \(0<a(c)<1\) for \(c>1\). Thus the
same negative root \(\cosh z=-a(c)\) gives

\[
z_\pm(c)=\pm\operatorname{arcosh}a(c)+i\pi
\]

below threshold, while above threshold it gives

\[
z_\pm(c)=i\pi\pm i\arccos a(c).
\]

The divisor multiplicity is conserved through the collision. What changes is
the real form occupied by the two local branches: transverse real displacement
becomes tangent imaginary displacement.

Both one-sided squared displacements have the same coefficient:

\[
\lim_{c\uparrow1}
\frac{\operatorname{arcosh}(a(c))^2}{1-c}
=\frac23,
\]

\[
\lim_{c\downarrow1}
\frac{\arccos(a(c))^2}{c-1}
=\frac23.
\]

Individual branch velocity diverges at collision:

\[
\alpha'(c)\sim-rac1{\sqrt{6(1-c)}}.
\]

Hence the simple-zero implicit velocity is not the correct coordinate at the
threshold. The squared transverse distance is regular:

\[
\frac{d}{dc}\alpha(c)^2\longrightarrow-\frac23.
\]

## Compiler consequence

The regular local datum is not a labelled zero velocity but the quadratic
divisor packet: multiplicity, seam normal, and the sign of the unfolding
coefficient

\[
-\frac{2F_c}{F_{zz}}.
\]

Here it equals \(-2/3\). Its sign decides whether the split branches point
normal to the seam or tangent along it. This datum survives relabelling of the
two roots and remains finite when their individual velocities diverge.

For an actual completion theorem, the source must provide a parameterized
holomorphic family and prove that every relevant collision has the required
even multiplicity and unfolding sign. A scalar endpoint showing a multiple
zero supplies neither its incoming direction nor its unfolding coefficient.

## Falsifiers

- Treating the two hostile zeros as annihilated at \(c=1\).
- Applying the simple-zero velocity formula at the double zero.
- Using a labelled branch velocity as a continuous threshold observable.
- Ignoring the above-threshold seam continuation.
- Claiming the collision normal form without checking \(F_c\) and
  \(F_{zz}\).
- Importing this unfolding sign into theta/Tate completion without deriving
  the corresponding source jet.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to identify the exact local event hidden by the seam
threshold.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The event is a quadratic real-to-imaginary branch rotation, and the
regular compiler coordinate is the divisor jet rather than zero velocity.
