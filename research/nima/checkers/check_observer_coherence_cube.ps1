# Operator-authorized shell route; finite higher-groupoid fragment.
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'observer-coherence-cube-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & python research/nima/checkers/check_observer_coherence_cube.py
  if ($LASTEXITCODE -ne 0) { throw 'Observer cube regression failed' }
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module ObserverCoherenceCube -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Fresh higher-cell compilation failed' }
  $PositivePath = Join-Path $Results 'agda-ObserverCoherenceCube.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $Controls = @()
  foreach ($Name in @('ObserverBadRouteCollapse', 'ObserverBadTransport')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & $Agda --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    Write-Output $Text
    $Expected = if ($Name -eq 'ObserverBadRouteCollapse') { 'leftFirst != rightFirst' } else { 'false != true' }
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains($Expected) -or !$Text.Contains('refl')) {
      throw "Wrong rejection outcome: $Name"
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Expected;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='observer-higher-groupoid-fragment-checked'; finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     computational_receipt_sha256=(Get-FileHash -Algorithm SHA256 (Join-Path $Results 'observer-coherence-cube.json')).Hash;
     controls=$Controls;
     scope='Actual univalent square and cube, full-source canonical trace instance, retained route distinction and nontrivial-loop control. No full free infinity-groupoid or positivity theorem.'
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
