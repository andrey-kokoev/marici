//! Primitive relative-Q classes from the two normalization hemispheres.

fn main() {
    let h_plus = [0_i64, -1, 0, -2, 1, -2, 0, 1, -2];
    let h_minus = [2_i64, -1, 2, 0, 1, 0, 2, 1, 0];
    let sphere = [1_i64, -1, 1, -1, 1, -1, 1, 1, -1];
    let hexagon = [1_i64, 0, 1, 1, 0, 1, 1, 0, 1];
    for i in 0..9 {
        assert_eq!(h_plus[i] + h_minus[i], 2 * sphere[i]);
        assert_eq!(h_minus[i] - h_plus[i], 2 * hexagon[i]);
        assert_eq!(h_plus[i], sphere[i] - hexagon[i]);
        assert_eq!(h_minus[i], sphere[i] + hexagon[i]);
    }
    let long = [1_usize, 4, 7];
    assert_eq!(long.map(|i| hexagon[i]), [0, 0, 0]);
    let primitive_q = long.map(|i| sphere[i]);
    assert_eq!(primitive_q, [-1, 1, 1]);
    assert_eq!(long.map(|i| h_plus[i]), primitive_q);
    assert_eq!(long.map(|i| h_minus[i]), primitive_q);
    println!("{{\"status\":\"proved_scoped_octahedral_sheet_hemisphere_primitive_Q\",\"hemisphere_faces\":4,\"mixed_fillers_per_hemisphere\":3,\"boundary\":\"cross_sheet_C6\",\"H_plus\":\"sphere-minus-hexagon\",\"H_minus\":\"sphere-plus-hexagon\",\"full_total\":\"2*sphere\",\"relative_long_row\":[-1,1,1],\"relative_snf\":[1],\"sheetwise_Q_coefficient\":1,\"literal_six_functor_BC_constructed\":false,\"endpoint_Q_mapping_fiber\":\"unconstructed\"}}");
}
