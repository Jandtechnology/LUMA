; Script Inno Setup para LUMA - Soporte en Inglés y Español
[Setup]
AppName=LUMA (Lenguaje Universal de Memoria y Alma)
AppVersion=1.0
DefaultDirName={pf}\LUMA
DefaultGroupName=LUMA
OutputDir=.
OutputBaseFilename=LUMA_Installer
Compression=lzma
SolidCompression=yes

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "launcher\run_luma.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "python\luma.py"; DestDir: "{app}\python"; Flags: ignoreversion
Source: "python\README.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "lisp\luma.lisp"; DestDir: "{app}\lisp"; Flags: ignoreversion
Source: "LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\LUMA"; Filename: "{app}\run_luma.bat"
Name: "{commondesktop}\LUMA"; Filename: "{app}\run_luma.bat"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio / Create desktop shortcut"; GroupDescription: "Opciones adicionales / Additional options:"

[Run]
Filename: "{app}\README.txt"; Description: "Ver instrucciones de uso / View usage instructions"; Flags: postinstall shellexec skipifsilent
