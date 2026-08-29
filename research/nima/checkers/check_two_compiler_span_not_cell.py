import json


def scalar_projection(record):
    return record["bargmann"]


def main():
    loop_records = [
        {"bargmann": [0.0, 0.1924500897], "attenuation": 0.0},
        {"bargmann": [0.0, 0.1924500897], "attenuation": 0.1},
    ]
    shift_records = [
        {"bargmann": [0.0, 0.1924500897], "distinguishability": 0.0},
        {"bargmann": [0.0, 0.1924500897], "distinguishability": 0.1},
    ]

    loop_same_scalar = scalar_projection(loop_records[0]) == scalar_projection(
        loop_records[1]
    )
    shift_same_scalar = scalar_projection(shift_records[0]) == scalar_projection(
        shift_records[1]
    )
    loop_records_distinct = loop_records[0] != loop_records[1]
    shift_records_distinct = shift_records[0] != shift_records[1]

    assert loop_same_scalar and loop_records_distinct
    assert shift_same_scalar and shift_records_distinct
    assert scalar_projection(loop_records[0]) == scalar_projection(shift_records[0])

    print(
        json.dumps(
            {
                "schema": "marici.two_compiler_span_not_cell.v1",
                "checks": {
                    "loop_projection_nonfaithful": True,
                    "shift_projection_nonfaithful": True,
                    "common_scalar_agreement": True,
                    "complete_record_comparison_supplied": False,
                },
                "verdict": "common_readout_span_only",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
