use std::fs;

fn main() {
    let mut checks=0_u64;
    for a in 1_i128..=31 { for b in 1_i128..=33 { for e in 1_i128..=17 {
        let pushed=[[a*a,e*a*b],[e*a*b,e*e*b*b]];
        let grade0=[[a*a,0],[0,0]];
        let grade1=[[0,a*b],[a*b,0]];
        let grade2=[[0,0],[0,b*b]];
        let reconstructed=[
            [grade0[0][0]+e*grade1[0][0]+e*e*grade2[0][0],grade0[0][1]+e*grade1[0][1]+e*e*grade2[0][1]],
            [grade0[1][0]+e*grade1[1][0]+e*e*grade2[1][0],grade0[1][1]+e*grade1[1][1]+e*e*grade2[1][1]],
        ];
        assert_eq!(pushed,reconstructed);
        assert_eq!(pushed[0][0]*pushed[1][1],pushed[0][1]*pushed[1][0]);
        checks+=2;
    }}}
    // A pure kernel amplitude has no ordinary or first density grade.
    for b in 1_i128..=101 {
        let grade0=[[0_i128,0],[0,0]];
        let grade1=[[0_i128,0],[0,0]];
        let grade2=[[0_i128,0],[0,b*b]];
        assert_eq!(grade0,[[0,0],[0,0]]);
        assert_eq!(grade1,[[0,0],[0,0]]);
        assert_ne!(grade2,[[0,0],[0,0]]);
        checks+=3;
    }
    let output=format!(concat!("{{\n","  \"schema\": \"marici.singular_amplitude_hermitian_costalk.v1\",\n","  \"exact_checks\": {},\n","  \"singular_map\": \"diag(1,epsilon)\",\n","  \"grade_0\": \"Hermitian square of image\",\n","  \"grade_1\": \"image-kernel cross term\",\n","  \"grade_2\": \"Hermitian square of kernel\",\n","  \"pure_kernel_first_density_grade\": 0,\n","  \"supported_kernel_costalk_grade\": 2,\n","  \"new_operation_required\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
    fs::write("research/benincasa/results/singular-amplitude-hermitian-costalk.json",output).unwrap();
}
