# Feedback selector noise tradeoff (WP275)

## Linear feedback experiment

Add a sensor-controller port to WP274's noisy preparation. Let \(k\geq0\) be
the feedback gain, \(R>0\) the sensor-noise intensity, \(D>0\) the source
diffusion, and \(\gamma>0\) the intrinsic damping. The stationary variance is

\[
v(k)=\frac{D+Rk^2}{\gamma+k}.
\]

Feedback increases damping, but it also feeds measurement noise into the
prepared coordinate. Exact optimization gives

\[
k_*=-\gamma+\sqrt{\gamma^2+\frac{D}{R}},
\qquad
v_{\min}=2Rk_*.
\]

The optimal gain is finite. Sending the gain to infinity makes the variance
diverge rather than vanish.

## Exact calibrated packet

For

\[
\gamma=1,
\qquad D=\frac1{100},
\qquad R=\frac1{300},
\]

the exact optimum is \(k_*=1\). Feedback improves the passive floor from
\(1/100\) to \(1/150\), but still misses the tighter target variance
\(1/200\).

## Changed experiment and authority

The sensor-controller port creates a new relational preparation experiment. It
does not reveal or select an absolute property of the original passive source.
Its refinement is physical only if the flavor-sensitive sensor, actuator,
noise, bandwidth, gain bound, cost, and stabilization are independently
derived and calibrated.

Thus linear feedback can improve a conditional approximate distribution
selector. It is neither an exact point selector nor a texture rigidifier, and
formal control gain is not executable control.

Run `uv run --with sympy python
research/flavor/checkers/wp275_feedback_selector_noise_tradeoff.py` for the
exact optimum, passive comparison, tighter-target failure, and infinite-gain
hostile test.
