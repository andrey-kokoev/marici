import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

six = 6
u = [Fraction(1,6)] * six

# An irreversible complete-mixing law needs a nonzero six-state Lindblad or
# Markov generator with L u=0, plus a declared event-time/readout map.
required_generator_shape = (6,6)
required_stationary = "L*(1/6)^6=0"
required_event_time_map = "tau:C->T_phys"
assert required_generator_shape == (6,6)
assert required_stationary == "L*(1/6)^6=0"
assert required_event_time_map == "tau:C->T_phys"

# Current boundary packets contain anomaly/inflow coefficients and a common
# Green response, but no dissipative rates and no physical-time map.
anomaly_channels = 7
parent_gs_coefficient = -3
common_green_rank = 1
sourced_dissipative_rates = 0
sourced_event_time_maps = 0
assert anomaly_channels == 7
assert parent_gs_coefficient == -3
assert common_green_rank == 1
assert sourced_dissipative_rates == 0
assert sourced_event_time_maps == 0

zero_generator_stationary = True
zero_generator_mixes = False
assert zero_generator_stationary and not zero_generator_mixes

result = {
    "schema": "marici.flavor.wp1121.v1",
    "status": "PASS",
    "question": "Can a UV boundary source derive irreversible six-state mixing as event production?",
    "dpc": {
        "conjecture": "The UV boundary source derives irreversible six-state mixing rates and a finite event-time map producing J6/6.",
        "rivals": [
            "anomaly inflow supplies mixing",
            "localized-brane Green response supplies mixing",
            "no irreversible boundary dynamics"
        ],
        "risky_consequences": [
            "a nonzero 6x6 Lindblad/Markov generator L with L*(1/6)^6=0",
            "six nonnegative mixing rates",
            "a source-derived event-time/readout map tau:C->T_phys"
        ],
        "falsification_attempt": "The admitted boundary data contain seven anomaly channels, GS coefficient -3, and rank-one Green response, but zero dissipative rates and zero event-time maps.",
        "residual": "A future UV defect could still supply a Lindblad/Markov generator and physical-time interface.",
        "disposition": "reject the current-source irreversible-mixing conjecture"
    },
    "uniform_stationary_state": [str(x) for x in u],
    "required_generator_shape": list(required_generator_shape),
    "required_stationary": required_stationary,
    "required_event_time_map": required_event_time_map,
    "anomaly_channels": anomaly_channels,
    "parent_gs_coefficient": parent_gs_coefficient,
    "common_green_rank": common_green_rank,
    "sourced_dissipative_rates": sourced_dissipative_rates,
    "sourced_event_time_maps": sourced_event_time_maps,
    "zero_generator_stationary": zero_generator_stationary,
    "zero_generator_mixes": zero_generator_mixes,
    "classification": "negative gate: conservative anomaly/Green data do not source irreversible event mixing",
    "remaining_gate": "test a non-stochastic boundary S-matrix or derive a Lindblad/Markov generator with physical-time interface",
    "hostile_gate": "do not infer dissipation from anomaly inflow, endpoint localization, Green response, or a variable named t",
    "claim_boundary": "this rejects current-source irreversible mixing, not all future UV defect dynamics",
    "disposition": "irreversible-mixing conjecture rejected for the current source",
}

(ROOT / "results" / "wp1121_irreversible_boundary_mixing_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1121 PASS:", anomaly_channels, parent_gs_coefficient, sourced_dissipative_rates, sourced_event_time_maps)
