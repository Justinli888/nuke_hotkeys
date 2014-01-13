from n_hotkeys import nuke_hotkeys
m=nuke.menu('Nuke')
n=m.addMenu('PyTools')
n.addCommand('Nuke Hotkeys','ex=nuke_hotkeys.NukeHotKeys()')
