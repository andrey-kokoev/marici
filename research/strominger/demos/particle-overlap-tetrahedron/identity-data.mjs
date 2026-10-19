// Generated from the verified attachment receipt; do not hand-edit.
export default {
  "schema": "marici.identity-viewer-data.v1",
  "source_receipt": "research/strominger/results/cmc-mcm-identity-attachment/verification.json",
  "receipt_sha256": "9d9accfe1d2915090f2ceb5ba2507f0703a518f9a09ee9a39145a03a3b78dba6",
  "verified_checks": 53,
  "original_walk": [
    "C0",
    "M0",
    "C1",
    "M1",
    "C1",
    "C2"
  ],
  "exact_points": {
    "C0": [
      "1",
      "1",
      "1",
      "0"
    ],
    "M0": [
      "1",
      "-1",
      "-1",
      "0"
    ],
    "C1": [
      "-1",
      "1",
      "-1",
      "0"
    ],
    "M1": [
      "-1",
      "-1",
      "1",
      "0"
    ],
    "C2": [
      "0",
      "0",
      "0",
      "1"
    ]
  },
  "windows": [
    {
      "role": "proton",
      "ordered_vertices": [
        "C0",
        "M0",
        "C1"
      ],
      "anchor": [
        "1/3",
        "1/3",
        "-1/3",
        "0"
      ],
      "walk_occurrence_ids": [
        "walk:0",
        "walk:1"
      ],
      "explicit_extra_closure": {
        "label": "declared-geometric-closure:proton",
        "source": "C1",
        "target": "C0"
      },
      "modes": {
        "common": {
          "label": "identity:1",
          "eigenvalue": {
            "real": "1",
            "imaginary_sqrt3_coefficient": "0"
          },
          "source_window": {
            "root": "record4:0",
            "ordered_occurrences": [
              "walk:0",
              "walk:1",
              "declared-geometric-closure:proton"
            ]
          }
        },
        "positive": {
          "label": "identity:2",
          "eigenvalue": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "1/2"
          },
          "source_window": {
            "root": "record4:0",
            "ordered_occurrences": [
              "walk:0",
              "walk:1",
              "declared-geometric-closure:proton"
            ]
          }
        },
        "negative": {
          "label": "identity:3",
          "eigenvalue": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "-1/2"
          },
          "source_window": {
            "root": "record4:0",
            "ordered_occurrences": [
              "walk:0",
              "walk:1",
              "declared-geometric-closure:proton"
            ]
          }
        }
      }
    },
    {
      "role": "neutron",
      "ordered_vertices": [
        "M0",
        "C1",
        "M1"
      ],
      "anchor": [
        "-1/3",
        "-1/3",
        "-1/3",
        "0"
      ],
      "walk_occurrence_ids": [
        "walk:1",
        "walk:2"
      ],
      "explicit_extra_closure": {
        "label": "declared-geometric-closure:neutron",
        "source": "M1",
        "target": "M0"
      },
      "modes": {
        "common": {
          "label": "identity:6",
          "eigenvalue": {
            "real": "1",
            "imaginary_sqrt3_coefficient": "0"
          },
          "source_window": {
            "root": "record4:5",
            "ordered_occurrences": [
              "walk:1",
              "walk:2",
              "declared-geometric-closure:neutron"
            ]
          }
        },
        "positive": {
          "label": "identity:7",
          "eigenvalue": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "1/2"
          },
          "source_window": {
            "root": "record4:5",
            "ordered_occurrences": [
              "walk:1",
              "walk:2",
              "declared-geometric-closure:neutron"
            ]
          }
        },
        "negative": {
          "label": "identity:8",
          "eigenvalue": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "-1/2"
          },
          "source_window": {
            "root": "record4:5",
            "ordered_occurrences": [
              "walk:1",
              "walk:2",
              "declared-geometric-closure:neutron"
            ]
          }
        }
      }
    },
    {
      "role": "electron",
      "ordered_vertices": [
        "M1",
        "C1",
        "C2"
      ],
      "anchor": [
        "-2/3",
        "0",
        "0",
        "1/3"
      ],
      "walk_occurrence_ids": [
        "walk:3",
        "walk:4"
      ],
      "explicit_extra_closure": {
        "label": "declared-geometric-closure:electron",
        "source": "C2",
        "target": "M1"
      },
      "modes": {
        "common": {
          "label": "identity:11",
          "eigenvalue": {
            "real": "1",
            "imaginary_sqrt3_coefficient": "0"
          },
          "source_window": {
            "root": "record4:10",
            "ordered_occurrences": [
              "walk:3",
              "walk:4",
              "declared-geometric-closure:electron"
            ]
          }
        },
        "positive": {
          "label": "identity:12",
          "eigenvalue": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "1/2"
          },
          "source_window": {
            "root": "record4:10",
            "ordered_occurrences": [
              "walk:3",
              "walk:4",
              "declared-geometric-closure:electron"
            ]
          }
        },
        "negative": {
          "label": "identity:13",
          "eigenvalue": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "-1/2"
          },
          "source_window": {
            "root": "record4:10",
            "ordered_occurrences": [
              "walk:3",
              "walk:4",
              "declared-geometric-closure:electron"
            ]
          }
        }
      }
    }
  ],
  "transitions": [
    {
      "from": "proton",
      "to": "neutron",
      "anchor_displacement": [
        "-2/3",
        "-2/3",
        "0",
        "0"
      ],
      "mode_transport": {
        "common": {
          "target_mode": "common",
          "phase": {
            "real": "1",
            "imaginary_sqrt3_coefficient": "0"
          }
        },
        "positive": {
          "target_mode": "positive",
          "phase": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "1/2"
          }
        },
        "negative": {
          "target_mode": "negative",
          "phase": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "-1/2"
          }
        }
      },
      "cyclic_target_convention": "forward"
    },
    {
      "from": "neutron",
      "to": "electron",
      "anchor_displacement": [
        "-1/3",
        "1/3",
        "1/3",
        "1/3"
      ],
      "mode_transport": {
        "common": {
          "target_mode": "common",
          "phase": {
            "real": "1",
            "imaginary_sqrt3_coefficient": "0"
          }
        },
        "positive": {
          "target_mode": "negative",
          "phase": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "-1/2"
          }
        },
        "negative": {
          "target_mode": "positive",
          "phase": {
            "real": "-1/2",
            "imaginary_sqrt3_coefficient": "1/2"
          }
        }
      },
      "cyclic_target_convention": "inverse: two retained forward cycles"
    }
  ],
  "scope": "Verified source geometry and conditional adapters, not physical particle identification or an isometry of every display chart."
};
