Get-Process | Where-Object { $_.CPU -ne $null }  | Sort-Object CPU -Descending | Select-Object -First 5 Name, CPU
