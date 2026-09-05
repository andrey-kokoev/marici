$ErrorActionPreference = 'Stop'
$root = Resolve-Path (Join-Path $PSScriptRoot '../../..')
$outDir = Join-Path $root 'research/sources/nima/papers/six-point-nmhv'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
$sources = @(
  @{ Id = '1312.2007'; Uri = 'https://arxiv.org/pdf/1312.2007'; File = '1312.2007.pdf' },
  @{ Id = '1212.5605'; Uri = 'https://arxiv.org/pdf/1212.5605'; File = '1212.5605.pdf' }
)
$records = @()
foreach ($source in $sources) {
  $path = Join-Path $outDir $source.File
  Invoke-WebRequest -Uri $source.Uri -OutFile $path
  $item = Get-Item $path
  $hash = Get-FileHash -Algorithm SHA256 $path
  $records += [ordered]@{
    arxiv_id = $source.Id
    uri = $source.Uri
    relative_path = "research/sources/nima/papers/six-point-nmhv/$($source.File)"
    bytes = $item.Length
    sha256 = $hash.Hash.ToLowerInvariant()
    retrieved_at = (Get-Date).ToUniversalTime().ToString('o')
  }
}
$manifest = [ordered]@{
  schema = 'marici.nima.six_point_nmhv_source_retrieval.v1'
  retrieval_authority = 'Operator explicitly authorized external retrieval using shells.'
  sources = $records
}
$manifestPath = Join-Path $outDir 'manifest.json'
$manifest | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $manifestPath
Write-Output ($manifest | ConvertTo-Json -Depth 6 -Compress)
