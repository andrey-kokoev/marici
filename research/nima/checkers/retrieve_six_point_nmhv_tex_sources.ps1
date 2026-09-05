$ErrorActionPreference = 'Stop'
$root = Resolve-Path (Join-Path $PSScriptRoot '../../..')
$outDir = Join-Path $root 'research/sources/nima/papers/six-point-nmhv'
foreach ($id in @('1312.2007','1212.5605')) {
  $path = Join-Path $outDir "$id.eprint"
  Invoke-WebRequest -Uri "https://export.arxiv.org/e-print/$id" -OutFile $path
  $hash = Get-FileHash -Algorithm SHA256 $path
  Write-Output "$id $((Get-Item $path).Length) $($hash.Hash.ToLowerInvariant())"
}
