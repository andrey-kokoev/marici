# Operator-authorized shell route; fixed-fixture certificate plus rejection controls.
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'newtonian-tidal-formal-audit.json'
# A failed rerun must not leave an old aggregate success receipt.
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & python research/nima/checkers/export_newtonian_tidal.py
  if ($LASTEXITCODE -ne 0) { throw 'Export failed' }
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module NewtonianTidalCertificate -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-NewtonianTidalCertificate.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  & python research/nima/checkers/check_newtonian_potential_routes.py
  if ($LASTEXITCODE -ne 0) { throw 'Independent potential route failed' }
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module NewtonianTidalRoutes -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Route comparison compilation failed' }
  $RoutePath = Join-Path $Results 'agda-NewtonianTidalRoutes.json'
  $Route = Get-Content $RoutePath -Raw | ConvertFrom-Json
  if (!$Route.passed -or !$Route.ignore_interfaces) { throw 'Fresh route receipt absent' }
  $Controls = @()
  foreach ($Name in @('NewtonianBadTensor', 'NewtonianBadReciprocal', 'NewtonianBadProductRule')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & $Agda --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    Write-Output $Text
    $Expected = switch ($Name) {
      'NewtonianBadTensor' { '228 != 229' }
      'NewtonianBadReciprocal' { '1728 != 1729' }
      'NewtonianBadProductRule' { '2 != 1' }
    }
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains($Expected) -or !$Text.Contains('refl')) {
      throw "Wrong negative-control outcome: $Name"
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Expected;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='fixed-Newtonian-two-route-RRC-comparison-checked'; finished_at=[DateTime]::UtcNow.ToString('o');
     route_receipt_sha256=(Get-FileHash -Algorithm SHA256 $RoutePath).Hash;
     potential_check_sha256=(Get-FileHash -Algorithm SHA256 (Join-Path $Results 'newtonian-potential-routes.json')).Hash;
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     export_receipt_sha256=(Get-FileHash -Algorithm SHA256 (Join-Path $Results 'newtonian-tidal-export.json')).Hash;
     controls=$Controls;
     scope='Fixed potential-jet versus geometric-tensor equality, affine invariance and retained RRC comparison. Newtonian potential, jet calculus interpretation and acceleration law supplied; no continuum calculus formalization.'
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
