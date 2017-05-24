import sys
import os
import datetime
import subprocess

from keyhac import *


def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    if 1:
        keymap.editor = "TextEdit"
        #keymap.editor = "Sublime Text 2"

    # Setting with callable object (Advanced usage)
    if 0:
        def editor(path):
            subprocess.call([ "open", "-a", "TextEdit", path ])
        keymap.editor = editor


    # --------------------------------------------------------------------
    # Customizing the display

    # Font
    keymap.setFont( "Osaka-Mono", 16 )

    # Theme
    keymap.setTheme("black")

    # Global keymap which affects any windows
    keymap_global = keymap.defineWindowKeymap()

    # Terminal key customization
    if 1:
      keymap_terminal = keymap.defineWindowKeymap( app_name="com.apple.Terminal" )

      keymap_terminal[ "Cmd-P" ] = "Up"
      keymap_terminal[ "Cmd-N" ] = "Down"
      keymap_terminal[ "Cmd-F" ] = "Right"
      keymap_terminal[ "Cmd-B" ] = "Left"
      keymap_terminal[ "Cmd-W" ] = "Ctrl-W"
      keymap_terminal[ "Cmd-Z" ] = "Ctrl-Z"
      keymap_terminal[ "Cmd-A" ] = "Ctrl-A"
      keymap_terminal[ "Cmd-E" ] = "Ctrl-E"
      keymap_terminal[ "Cmd-K" ] = "Ctrl-K"
      keymap_terminal[ "Cmd-L" ] = "Ctrl-L"
      keymap_terminal[ "Cmd-R" ] = "Ctrl-R"
      keymap_terminal[ "Cmd-H" ] = "Ctrl-H"
      keymap_terminal[ "Cmd-M" ] = "Ctrl-M"
      keymap_terminal[ "Cmd-J" ] = "Ctrl-Shift-Tab"
      keymap_terminal[ "Cmd-Semicolon" ] = "Ctrl-Tab"
      keymap_terminal[ "BackQuote" ] = "Ctrl-C"

    # Chrome key customization
    if 1:
      keymap_chrome = keymap.defineWindowKeymap( app_name="com.google.Chrome" )

      keymap_chrome[ "Cmd-J" ] = "Cmd-Alt-Left"
      keymap_chrome[ "Cmd-Semicolon" ] = "Cmd-Alt-Right"

    # MacVim key customization
    if 1:
      keymap_macvim = keymap.defineWindowKeymap( app_name="org.vim.MacVim" ) 

      keymap_macvim[ "Cmd-W" ] = "Ctrl-W"
