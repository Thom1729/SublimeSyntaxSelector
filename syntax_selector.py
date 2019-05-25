import sublime_plugin

from sublime_lib import NamedSettingsDict, show_selection_panel, NO_SELECTION
from sublime_lib.syntax import list_syntaxes

from functools import partial


class SelectSyntaxCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = NamedSettingsDict('Syntax Selector')

        view = self.window.active_view()
        current_syntax_path = view.settings().get('syntax')

        syntaxes = [
            s for s in list_syntaxes()
            if settings['show_hidden_syntaxes'] or not s.hidden
        ]

        selected = next(
            (s for s in syntaxes if s.path == current_syntax_path),
            NO_SELECTION
        )

        def change_syntax(s):
            view.assign_syntax(s.path)

        if settings['preview_on_highlight']:
            on_cancel = partial(view.assign_syntax, current_syntax_path)
            on_highlight = change_syntax
        else:
            on_cancel = None
            on_highlight = None

        show_selection_panel(
            self.window,
            syntaxes,
            selected=selected,
            labels=lambda s: (s.name or '', s.path),
            on_select=change_syntax,
            on_cancel=on_cancel,
            on_highlight=on_highlight,
        )
