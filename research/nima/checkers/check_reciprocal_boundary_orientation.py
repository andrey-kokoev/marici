import json


sizes = [2, 3, 5, 8]
records = []

for size in sizes:
    boundary = [0] * size
    boundary[0] = 1
    boundary[-1] = -1
    reflected = list(reversed(boundary))

    assert reflected == [-value for value in boundary]

    symmetric_readout = boundary[0] + boundary[-1]
    odd_readout = boundary[0] - boundary[-1]
    reflected_odd_readout = reflected[0] - reflected[-1]

    assert symmetric_readout == 0
    assert odd_readout == 2
    assert reflected_odd_readout == -odd_readout

    records.append(
        {
            "size": size,
            "boundary": boundary,
            "reflected_boundary": reflected,
            "symmetric_readout": symmetric_readout,
            "odd_readout": odd_readout,
            "reflected_odd_readout": reflected_odd_readout,
        }
    )

result = {
    "schema": "marici.nima.reciprocal-boundary-orientation.v1",
    "records": records,
    "reflection_flips_boundary_commutator": True,
    "unpointed_invariant_linear_readout_must_vanish": True,
    "odd_endpoint_character_detects_orientation": True,
    "reciprocal_sewing_alone_orients_anomaly": False,
    "next_gate": "source_derived_endpoint_gamma_odd_character",
}
print(json.dumps(result, indent=2, sort_keys=True))

