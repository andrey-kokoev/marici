$ErrorActionPreference = 'Stop'

$crate = Join-Path $PSScriptRoot '..\marici-gm'
$candidate = Join-Path $PSScriptRoot '..\marked-extension-charzero-candidate.json'

Push-Location $crate
try {
    cargo build --release --features verification-prime-4 `
        --bin marked_relative_reduction_engine `
        --bin marked_extension_heldout_verify

    $env:MARICI_RECONSTRUCTION_MODE = '1'
    $env:MARICI_UV_SAMPLES = ((0..16 | ForEach-Object {
        '{0},{1}' -f (101 + 3 * $_), (157 + 7 * $_)
    }) -join ';')

    & '.\target\release\marked_relative_reduction_engine.exe' |
        & '.\target\release\marked_extension_heldout_verify.exe' $candidate '-'
}
finally {
    Remove-Item Env:MARICI_RECONSTRUCTION_MODE -ErrorAction SilentlyContinue
    Remove-Item Env:MARICI_UV_SAMPLES -ErrorAction SilentlyContinue
    Pop-Location
}
