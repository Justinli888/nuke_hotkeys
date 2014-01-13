Script prompts for hotkeys nuke

Put this folder (/n_hotkeys) in your Nuke/plugins path and add this line to your menu.py: 

from n_hotkeys import nuke_hotkeys
m=nuke.menu('Nuke')
n=m.addMenu('PyTools')
n.addCommand('Nuke Hotkeys','ex=nuke_hotkeys.NukeHotKeys()')