# -*- mode: python -*-

block_cipher = None


a = Analysis(['rem.py'],
             pathex=['C:\\Users\\ankit\\Documents\\c++\\Reminding\\rem.py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('icon.ico','C:\\Users\\ankit\\Documents\\c++\\Reminding\\icon.ico', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='remindingYou',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='C:\\Users\\ankit\\Documents\\c++\\Reminding\\iconScript.ico')