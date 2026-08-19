fn add(left: &[[i64; 6]; 2], right: &[[i64; 6]; 2]) -> [[i64; 6]; 2] {
    let mut out = [[0; 6]; 2];
    for i in 0..2 {
        for j in 0..6 {
            out[i][j] = left[i][j] + right[i][j];
        }
    }
    out
}

fn sub(left: &[[i64; 6]; 2], right: &[[i64; 6]; 2]) -> [[i64; 6]; 2] {
    let mut out = [[0; 6]; 2];
    for i in 0..2 {
        for j in 0..6 {
            out[i][j] = left[i][j] - right[i][j];
        }
    }
    out
}

fn main() {
    // Entry 924 gives a zero ordinary coefficient on the common coarsening.
    // The exact v7 audit gives one common source row after Cartier
    // regularization. Distinct nonzero values keep the test generic.
    let r = [2, 3, 5, 7, 11, 13];
    let zero = [0; 6];

    // Source-normalized target directions:
    // x=(1,-1), y=(0,1), and reflected z=(1,0).
    let m_x = [r, r.map(|value| -value)];
    let m_y = [zero, r];
    let m_z = [r, zero];
    assert_eq!(sub(&add(&m_x, &m_y), &m_z), [[0; 6]; 2]);

    // The three scalar target columns span rank two and have the unique
    // primitive relation x+y-z=0.
    let target_x = [1_i64, -1_i64];
    let target_y = [0_i64, 1_i64];
    let target_z = [1_i64, 0_i64];
    assert_eq!(
        [
            target_x[0] + target_y[0] - target_z[0],
            target_x[1] + target_y[1] - target_z[1],
        ],
        [0, 0]
    );
    let xy_minor = target_x[0] * target_y[1] - target_x[1] * target_y[0];
    assert_eq!(xy_minor, 1);

    // The link has three pairwise incompatible vertices and no edge or
    // two-cell whose boundary could realize this syzygy.
    let link_vertices = 3;
    let link_edges = 0;
    let link_two_cells = 0;

    println!(
        "{{\"schema\":\"marici.benincasa.string_six_point_normal_symbol_syzygy.v1\",\"common_coarsening\":[\"s14\",\"s235\"],\"common_source_vector\":true,\"source_ratio_x_to_y\":1,\"target_directions\":{{\"x\":[1,-1],\"y\":[0,1],\"z\":[1,0]}},\"target_rank\":2,\"primitive_syzygy\":[1,1,-1],\"matrix_identity\":\"M_x+M_y-M_z=0\",\"link_vertices\":{},\"link_edges\":{},\"link_two_cells\":{},\"carrier_boundary_realizes_syzygy\":false,\"classification\":\"coefficient normal-symbol syzygy without carrier filling\"}}",
        link_vertices, link_edges, link_two_cells
    );
}
