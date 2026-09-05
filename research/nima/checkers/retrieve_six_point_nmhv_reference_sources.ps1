$ErrorActionPreference = 'Stop'
$root = Resolve-Path (Join-Path $PSScriptRoot '../../..')
$outDir = Join-Path $root 'research/sources/nima/papers/six-point-nmhv'
foreach ($id in @('0907.5418','1008.2958')) {
  $pdf = Join-Path $outDir "$id.pdf"
  $src = Join-Path $outDir "$id.eprint"
  Invoke-WebRequest -Uri "https://arxiv.org/pdf/$id" -OutFile $pdf
  Invoke-WebRequest -Uri "https://export.arxiv.org/e-print/$id" -OutFile $src
  Write-Output "$id pdf=$((Get-FileHash -Algorithm SHA256 $pdf).Hash.ToLowerInvariant()) eprint=$((Get-FileHash -Algorithm SHA256 $src).Hash.ToLowerInvariant())"
}
