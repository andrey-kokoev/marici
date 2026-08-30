# Coherent-Control Route Compiler

Owner: marici.Aspect

This compiler turns the synchronized acquisition contract into a typed,
clocked sequence of calibration and observation operations.

For each of six control coordinates it emits routes for gap, stiffness,
screening, and relaxation. Every acquisition binds a source, actuator,
observer, trigger tick, cycle, and calibration identity.

Admission rejects:

- two acquisitions colliding on one observer and trigger;
- calibration older than the declared acquisition window;
- an unbound hardware port;
- excessive skew within a nominally synchronized cycle;
- incomplete four-channel cycles.

The generated packet contains 24 acquisition operations plus calibration
operations. It is a route plan only: no hardware command has been dispatched.
Actual drivers must consume this packet through an authorized apparatus
adapter and return signed execution receipts.

Run:

python research/aspect/checkers/check_coherent_control_route_compiler.py
