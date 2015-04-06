from mod_base import *

class Trim(Command):
    def __init__(self):
        pass

    def run(self, app, editor):
        line_nums = editor.get_lines_with_cursors()
        for lnum in line_nums:
            line = editor.lines[lnum]
            line.data = line.data.strip()

module = {
    "class": Trim,
    "name": "trim",
}