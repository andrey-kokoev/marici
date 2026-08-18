use std::{env, fs, time::Instant};

use symbolica::{
    domains::finite_field::{FiniteFieldCore, Zp64},
    tensors::matrix::{Matrix, MatrixError},
};

fn read_u64(bytes: &[u8], offset: &mut usize) -> u64 {
    let value = u64::from_le_bytes(bytes[*offset..*offset + 8].try_into().unwrap());
    *offset += 8;
    value
}

fn main() {
    let path = env::args().nth(1).expect("usage: gysin_complete_resonant_rank MATRIX.bin");
    let bytes = fs::read(&path).expect("cannot read matrix");
    assert_eq!(&bytes[..8], b"MGSRANK1");
    let mut offset = 8;
    let prime = read_u64(&bytes, &mut offset);
    let rows = read_u64(&bytes, &mut offset) as u32;
    let columns = read_u64(&bytes, &mut offset) as u32;
    let unknowns = read_u64(&bytes, &mut offset) as u32;
    let degree = read_u64(&bytes, &mut offset);
    assert_eq!(columns, unknowns + 1);
    assert_eq!(bytes.len(), offset + rows as usize * columns as usize * 8);

    let field = Zp64::new(prime);
    let mut coefficients = Vec::with_capacity(rows as usize * unknowns as usize);
    let mut rhs = Vec::with_capacity(rows as usize);
    for _ in 0..rows {
        for _ in 0..unknowns {
            coefficients.push(field.to_element(read_u64(&bytes, &mut offset)));
        }
        rhs.push(field.to_element(read_u64(&bytes, &mut offset)));
    }
    let matrix = Matrix::from_linear(coefficients, rows, unknowns, field.clone())
        .expect("invalid coefficient matrix");
    let target = Matrix::from_linear(rhs, rows, 1, field.clone())
        .expect("invalid target vector");

    let started = Instant::now();
    let outcome = match matrix.solve(&target) {
        Ok(_) => "split",
        Err(MatrixError::Inconsistent) => "inconsistent",
        Err(MatrixError::Underdetermined { .. }) => "underdetermined",
        Err(error) => panic!("unexpected solve error: {error}"),
    };
    println!(
        "{{\"schema\":\"marici.nima.gysin_complete_resonant_rank.v1\",\"degree\":{degree},\"prime\":{prime},\"rows\":{rows},\"unknowns\":{unknowns},\"outcome\":\"{outcome}\",\"elapsed_seconds\":{:.6}}}",
        started.elapsed().as_secs_f64()
    );
}
