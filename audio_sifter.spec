# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['audio_sifter.py'],
             pathex=['C:\\Users\\qvd441\\Documents\\git\\audio_sifter'],
             binaries=[(HOMEPATH + '\\PyQt5\\Qt\\bin\\*', 'PyQt5\\Qt\\bin')],
             datas=[],
             hiddenimports=["PyQt5"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='audio_sifter',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
	  icon='./src/resources/icon.ico')
