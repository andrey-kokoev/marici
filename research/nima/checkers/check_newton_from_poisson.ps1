# Shell runner: conditional algebra is not a real-analysis implementation.
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'newton-poisson-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & python research/nima/checkers/check_newton_from_poisson.py
  if ($LASTEXITCODE -ne 0) { throw 'Radial coefficient audit failed' }
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module NewtonRadialCoefficients -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-NewtonRadialCoefficients.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $Controls = @()
  foreach ($Name in @('NewtonBadVacuum', 'NewtonBadFlux')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & $Agda --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    Write-Output $Text
    $Expected = if ($Name -eq 'NewtonBadVacuum') { '2 != 0' } else { '12 != 11' }
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains($Expected) -or !$Text.Contains('refl')) {
      throw "Wrong rejection outcome: $Name"
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Expected;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='conditional-Poisson-to-Newton-algebra-checked'; finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     computational_receipt_sha256=(Get-FileHash -Algorithm SHA256 (Join-Path $Results 'newton-from-poisson.json')).Hash;
     runner_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash;
     controls=$Controls;
     scope='General flux cancellation and conditional calculus/RRC implication, plus radial coefficient algebra. No formal real/distributional Poisson instance or PDE uniqueness proof.'
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
