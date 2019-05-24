import sublime_plugin


from sublime_lib import NamedSettingsDict, show_selection_panel
from sublime_lib.syntax import list_syntaxes


class SelectSyntaxCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = NamedSettingsDict('Syntax Selector')

        view = self.window.active_view()
        selected_syntax = view.settings().get('syntax')

        syntaxes = [
            s for s in list_syntaxes()
            if settings['show_hidden_syntaxes'] or not s.hidden
        ]

        selected = next(s for s in syntaxes if s.path == selected_syntax)
        show_selection_panel(
            self.window,
            syntaxes,
            selected=selected,
            labels=lambda s: (s.name or '', s.path),
            on_select=lambda s: view.assign_syntax(s.path),
            on_cancel=lambda: view.assign_syntax(selected_syntax),
            on_highlight=(lambda s: view.assign_syntax(s.path)) if settings['preview_on_highlight'] else None
        )
