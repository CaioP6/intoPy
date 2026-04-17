import os
import subprocess

# Caminho da pasta de rede (UNC)
folder_path = r"\\192.168.4.4\te - ipi\Softwares"

# Caminho da área de trabalho do usuário (fixo conforme solicitado)
desktop_path = r"C:\Users\cviana\OneDrive - União Social Camiliana\Área de Trabalho"

# Nome do atalho (sem extensão)
shortcut_name = "Paxta"

# Caminho final do arquivo .lnk
shortcut_lnk = os.path.join(desktop_path, f"{os.path.splitext(shortcut_name)[0]}.lnk")

# Garante que a área de trabalho exista
if not os.path.isdir(desktop_path):
    raise FileNotFoundError(f"Área de trabalho não encontrada: {desktop_path}")

# Script PowerShell para criar o .lnk
ps_script = f'''
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_lnk}")
$Shortcut.TargetPath = "{folder_path}"
$Shortcut.WorkingDirectory = "{os.path.dirname(folder_path) if os.path.dirname(folder_path) else folder_path}"
$Shortcut.WindowStyle = 1
$Shortcut.Description = "Atalho para {folder_path}"
$Shortcut.Save()
'''

# Executa o PowerShell para criar o .lnk
result = subprocess.run(
    ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_script],
    capture_output=True,
    text=True
)

# Verificação de sucesso
if result.returncode != 0:
    print("Falha ao criar o atalho .lnk.")
    print("Erro do PowerShell:")
    print(result.stderr)
else:
    if os.path.exists(shortcut_lnk):
        print(f"Atalho .lnk criado em: {shortcut_lnk}")
    else:
        print("PowerShell executou sem erro, mas o arquivo .lnk não foi encontrado.")
