# Syntax Selector

Sublime command to choose a syntax definition from a quick panel.

## Installation

Via [Package Control](https://packagecontrol.io/docs/usage).

## Usage

Press <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>Y</kbd> to show the syntax selector panel.

## Configuration

To open the Syntax Selector settings, run `Preferences: Syntax Selector` from the command palette or choose Preferences → Package Settings → Syntax Selector → Preferences: Syntax Selector from the menubar.

### `show_hidden_syntaxes`: boolean (default: `false`)

If `true`, show all loaded syntax definitions. If `false`, do not show hidden syntax definitions.

### `preview_on_highlight`: boolean (default: `true`)

If `true`, then when you highlight a syntax definition in the syntax selector panel, that definition will be temporarily applied to your code. If you cancel the panel, the original syntax definition will be restored.
