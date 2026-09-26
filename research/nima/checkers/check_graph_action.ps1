# Exact finite action-selection audit and fresh formal closure, via shell.
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'graph-action-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & python research/nima/checkers/check_graph_action_selection.py
  if ($LASTEXITCODE -ne 0) { throw 'Action-selection audit failed' }
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module GraphAction -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-GraphAction.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $Controls = @()
  foreach ($Name in @('GraphActionBadScreening', 'GraphActionBadDerivative')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & $Agda --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    Write-Output $Text
    $Expected = if ($Name -eq 'GraphActionBadScreening') { '4 != 0' } else { '2 != 1' }
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains($Expected) -or !$Text.Contains('refl')) {
      throw "Wrong rejection outcome: $Name"
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Expected;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='graph-action-comparison-checked-selection-not-unique'; finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     computational_receipt_sha256=(Get-FileHash -Algorithm SHA256 (Join-Path $Results 'graph-action-selection.json')).Hash;
     runner_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash;
     controls=$Controls;
     scope='Finite polynomial action/variation comparison retained in RRC. Locality, additivity and shift covariance do not exclude quartic actions. Quadraticity and stationarity remain supplied.'
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
