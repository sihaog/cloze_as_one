import os
import re
from aqt import mw
from anki.hooks import wrap, addHook
from .consts import addon_path

# Hotkey definitions
olc_hotkey = "Ctrl+Shift+D"  # Cloze generation/preview

icon_path = os.path.join(addon_path, "icon", "cloze_as_one.png")
tooltip = "Edit clozes as one ({})".format(
    olc_hotkey)


def onClozeAsOneButton(editor):
    js_replace = """
        contents = currentField.innerHTML
        var contents_old = String(contents);
        var contents_new = contents_old.replace(/\{\{c\d::/g, "\{\{c1::");
        currentField.innerHTML = contents_new;
    """
    editor.web.eval(js_replace)



def onSetupEditorButtons21(buttons, editor):
    """Add buttons and hotkeys"""

    # bind to editor.olc_hotkey_generate because anki21 passes
    # editor instance by default
    b = editor.addButton(icon_path, "OlCloze", onClozeAsOneButton,
                         tooltip, keys=olc_hotkey)
    buttons.append(b)

    return buttons

addHook("setupEditorButtons", onSetupEditorButtons21)