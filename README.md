# Directory-Browser

The GUI Directory Viewer is a modular Python application designed to provide a graphical interface for exploring directory structures and inspecting file/folder metadata. Built with reusability in mind, it can function as a standalone utility or be embedded into larger projects that require directory visualization. Built using PySide6.

## GUI options located in gui_config.py:
- MAINWINDOW_SIZE_X, MAINWINDOW_SIZE_Y: Resize default window XY size (default: 1200, 800)
- FOLDERS_ONLY: Limit directory viewer (left panel) to only display folders (default: False)
- STATIC_SCROLLABLE_AREA: A boolean indicating whether the scrollable area on the right panel is static (True) or unique for each item (False). (default: True)

## Set scrollable area (right panel) content:
- Default/Static Widget: Go to directory_browser_gui.MainWindow.setup_default_scrollable_area. If STATIC_SCROLLABLE_AREA is set to false this will be replaced with directory_browser_gui.MainWindow.selected_item_details_widget.
- File/Folder details widget: Go to directory_browser_gui.MainWindow.selected_item_details_widget. It's currently based on the selected File/Folder path.

## Set what happens when the "Execute" button is pressed:
Got to the function: directory_browser_gui.MainWindow.execute_action