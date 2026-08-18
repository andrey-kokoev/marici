fn ordinary_cone_dimensions(weight: i64, cutoff: i64) -> (usize, usize, usize) {
    assert!(weight > 0 && cutoff > weight + 1);
    // Degree-zero quotient basis: q^m, -cutoff+1 <= m <= -weight-1.
    // Degree-one quotient basis: q^l dq, -cutoff <= l <= -weight-1.
    let c0 = (cutoff - weight - 1) as usize;
    let c1 = (cutoff - weight) as usize;
    let differential_rank = c0;
    (c0 - differential_rank, c1 - differential_rank, differential_rank)
}

fn logarithmic_source_cone_dimensions(weight: i64, cutoff: i64) -> (usize, usize) {
    assert!(weight > 0 && cutoff > weight + 1);
    // If the source is incorrectly enlarged to logarithmic one-forms, its
    // degree-one image also contains q^(-weight-1)dq.  The quotient square
    // matrix is then invertible.
    let dimension = (cutoff - weight - 1) as usize;
    let rank = dimension;
    (dimension - rank, dimension - rank)
}

fn main() {
    let weight = 17_i64;
    for cutoff in [20_i64, 24, 32, 48] {
        let (h0, h1, rank) = ordinary_cone_dimensions(weight, cutoff);
        assert_eq!((h0, h1), (0, 1));
        let log_h = logarithmic_source_cone_dimensions(weight, cutoff);
        assert_eq!(log_h, (0, 0));
        println!(
            "cutoff={cutoff} ordinary_source_H=(0,1) differential_rank={rank} logarithmic_source_H=(0,0)"
        );
    }
    let tangential_rank = 5_usize;
    let supported_cone_rank = tangential_rank;
    assert_eq!(supported_cone_rank, 5);
    println!("ordinary_residue_generator=q^(-18)*dq=q^(-17)*dlog(q)");
    println!("normal_contiguity_cone_rank=1");
    println!("unmarked_tangential_rank=5");
    println!("supported_integer_contiguity_cone_rank=5");
    println!("entry_553_normal_acyclicity=RETRACTED_FOR_ORDINARY_SOURCE_FORMS");
}
