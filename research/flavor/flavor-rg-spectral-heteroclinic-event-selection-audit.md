# RG-Spectral Heteroclinic Event-Selection Audit

## Question

If the spectral path is literally an RG trajectory, can global regularity
select one oriented physical threshold event with fixed magnitude, basin, and
readout?

## One coupled RG-spectral trajectory

Take the autonomous dimensionless flow

\[
\frac{du}{dt}=u(1-u),
\qquad
u_A(t)=\frac{1}{1+Ae^{-t}},
\qquad A>0.
\]

Every solution in the open interval is monotone and globally regular, with

\[
\lim_{t\to-\infty}u_A(t)=0,
\qquad
\lim_{t\to+\infty}u_A(t)=1.
\]

Thus the entire open interval is a basin connecting the two fixed points.
Define the spectral path by the source-symmetric function

\[
H_A(t)=u_A(t)-\frac12.
\]

It has one positive transverse zero,

\[
t_*=\log A,
\qquad
u_A(t_*)=\frac12,
\qquad
\frac{dH_A}{dt}(t_*)=\frac14.
\]

Conditional on the logistic vector field and symmetric spectral zero, this
single source dynamics fixes:

- positive crossing orientation;
- dimensionless portal magnitude \(u_*=1/2\);
- a global open basin;
- topological survival of one transverse crossing.

This is the strongest integrated selector in the branch so far.

## Autonomous translation modulus

Global endpoint regularity does not select \(A\). Time translation gives

\[
u_A(t+\delta)=u_{Ae^{-\delta}}(t).
\]

All positive \(A\) describe the same unparameterized heteroclinic orbit with a
different placement relative to the RG clock. If \(\mu=\mu_0e^t\), the physical
crossing scale is

\[
\mu_*=\mu_0A.
\]

Endpoint regularity selects the orbit but not its absolute event scale. The
modulus is equivalent to one boundary value,

\[
A=\frac{1-u(0)}{u(0)}.
\]

Therefore a boundary condition or reference clock is still required.

## Threshold criterion

For a general threshold criterion \(u=c\), the event occurs at

\[
t_c=\log\frac{Ac}{1-c}.
\]

Changing \(c\) from \(1/2\) to \(3/4\) moves the event by \(\log3\) while
retaining positive crossing orientation. The symmetric value \(c=1/2\) needs
source authority; radiative or detector corrections cannot be assumed to
preserve it.

## Reference clock and physical readout

The condition \(u(0)=1/2\) sets \(A=1\), but it does so by defining the RG
origin at the crossing. This is a relational clock attachment, not a dynamical
prediction of \(\mu_*\). It changes the experiment from an autonomous orbit to
an orbit compared with an external scale.

A detector record \(r=s\mu_*=s\mu_0A\) has the exact pair
\((A,s)=(1,2)\) and \((2,1)\). The source currently supplies neither gain
calibration nor a physical16 map.

## Aspect germ audit

The native object contains the oriented bulk, RG vector field, spectral
function, global endpoint contract, reference clock, mediator, threshold
event, physical16 map, and detector. Orientation, conditional dimensionless
magnitude, and the open basin pass. Trajectory-phase selection, absolute event
scale, threshold-criterion authority, quotient descent, and detector
calibration remain open.

## Classification and falsifiers

The coupled heteroclinic is a genuine conditional selector of sign,
dimensionless magnitude, and basin. It is not yet a selector of absolute
threshold scale or physical readout.

The smallest exact falsifiers are:

1. \(A=1\) and \(A=2\), which satisfy identical endpoint regularity while
   crossing at different scales;
2. the autonomous translation identity;
3. \(c=1/2\) and \(3/4\), which retain crossing orientation while moving the
   event;
4. the event-scale/detector-gain pair.

## Deutschian appraisal

Making the spectral path an RG trajectory is a real explanatory improvement:
the crossing, its sign, its dimensionless value, and its basin are no longer
separate structures. The remaining freedom is the universal phase modulus of
an autonomous heteroclinic.

To remove it without convention, the source needs a second physical event or
boundary condition that is independently fixed and whose separation from the
crossing is predicted. A cosmological formation event, compact RG interval,
or quantized finite-volume boundary could supply such an anchor, but it would
define a relational experiment. That same anchor must calibrate the detector
and map the event into physical16.

## Disposition

Progressive integrated selector. Sign, dimensionless magnitude, spectral
orientation, and global basin close conditionally; absolute event scale,
threshold criterion, quotient descent, and instrumentation remain open.
