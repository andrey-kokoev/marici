# Two-parameter phenomenological repair of FDM-2 (WP114)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

WP113's no-overlap result is scoped to fixed coupling normalization. Enlarge
only to

\[
a\mapsto\alpha a,qquad M\text{ variable},
\]

with `Y0,b,z` unchanged. A bounded scan followed by the rational witness

\[
\alpha=27/40,qquad M=15/2
\]

gives, from the full `4x4` canonical calculation,

\[
|J_{full}|=3.16350121\times10^{-5},
\]

first- and second-row deficits

\[
(d_1,d_2)=(0.00366261,0.02138882),
\]

and direct `|V_tb|=0.96272462`.

Using the PDG direct values from the 2025 CKM review, this point passes the
same permissive first-row three-sigma cap `0.0037`, the second-row two-sigma
lower sum `1.001-2(0.012)=0.977`, and the direct single-top two-sigma lower
value `1.010-2(0.027)=0.956`. It also exceeds the complete fitted ensemble
minimum `|J|=3.14132882e-5`.

Source: https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf .

This proves that WP113 is not a structural one-mediator no-go. It does **not**
produce a flavor selector: `alpha,M` were located by scanning the desired
phenomenological readouts. The rational point is a fitted repair witness, and
the margins are narrow. Treating it as source authority would violate the
rule against fitting a projector or selector from its desired answer.

Classification: phenomenologically admissible witness under the declared
loose checks; neither source selector nor texture rigidifier. Smallest
falsifier of selector status is its construction history—the parameter pair
depends on the external `J` and CKM constraints. Remaining gate: an
independent UV relation or dynamics that fixes `alpha,M` before these
readouts, plus collider, threshold, thermal, and full global-fit tests.

Verification: `uv run --with numpy python
research/flavor/checkers/wp114_fdm2_two_parameter_repair.py`.
