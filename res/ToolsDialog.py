#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade not found on Tue Aug 15 12:41:20 2017
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
if items:
    self.add_items(items)
# end wxGlade


class ToolsDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ToolsDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.label = wx.TextCtrl(self, wx.ID_ANY, "")
        self.primary_bitmap = wx.TextCtrl(self, wx.ID_ANY, "")
        self.primary_bitmap_button = wx.Button(self, wx.ID_ANY, "...")
        self.disabled_bitmap = wx.TextCtrl(self, wx.ID_ANY, "")
        self.disabled_bitmap_button = wx.Button(self, wx.ID_ANY, "...")
        self.event_handler = wx.TextCtrl(self, wx.ID_ANY, "")
        self.name = wx.TextCtrl(self, wx.ID_ANY, "")
        self.help_str = wx.TextCtrl(self, wx.ID_ANY, "")
        self.id = wx.TextCtrl(self, wx.ID_ANY, "")
        self.check_radio = wx.RadioBox(self, wx.ID_ANY, "Type", choices=["Normal", "Checkable", "Radio"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.ok = wx.Button(self, wx.ID_OK, "")
        self.cancel = wx.Button(self, wx.ID_CANCEL, "")
        self.move_up = wx.Button(self, wx.ID_ANY, "Up")
        self.move_down = wx.Button(self, wx.ID_ANY, "Down")
        self.add = wx.Button(self, wx.ID_ANY, "&Add")
        self.remove = wx.Button(self, wx.ID_ANY, "&Remove")
        self.add_sep = wx.Button(self, wx.ID_ANY, "Add Separator")
        self.items = wx.ListCtrl(self, wx.ID_ANY, style=wx.BORDER_DEFAULT | wx.BORDER_SUNKEN | wx.LC_EDIT_LABELS | wx.LC_REPORT | wx.LC_SINGLE_SEL)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.update_item, self.label)
        self.Bind(wx.EVT_TEXT, self.update_item, self.primary_bitmap)
        self.Bind(wx.EVT_BUTTON, self.move_item_up, self.primary_bitmap_button)
        self.Bind(wx.EVT_TEXT, self.update_item, self.disabled_bitmap)
        self.Bind(wx.EVT_BUTTON, self.move_item_up, self.disabled_bitmap_button)
        self.Bind(wx.EVT_TEXT, self.update_item, self.event_handler)
        self.Bind(wx.EVT_TEXT, self.update_item, self.name)
        self.Bind(wx.EVT_TEXT, self.update_item, self.help_str)
        self.Bind(wx.EVT_TEXT, self.update_item, self.id)
        self.Bind(wx.EVT_RADIOBOX, self.update_item, self.check_radio)
        self.Bind(wx.EVT_BUTTON, self.move_item_up, self.move_up)
        self.Bind(wx.EVT_BUTTON, self.move_item_down, self.move_down)
        self.Bind(wx.EVT_BUTTON, self.add_item, self.add)
        self.Bind(wx.EVT_BUTTON, self.remove_item, self.remove)
        self.Bind(wx.EVT_BUTTON, self.add_separator, self.add_sep)
        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.on_label_edited, self.items)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.show_item, self.items)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ToolsDialog.__set_properties
        self.SetTitle("Menu Editor")
        self.check_radio.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ToolsDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.FlexGridSizer(7, 2, 0, 0)
        sizer_primary_bitmap = wx.BoxSizer(wx.HORIZONTAL)
        sizer_primary_bitmap = wx.BoxSizer(wx.HORIZONTAL)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Label:")
        grid_sizer.Add(label_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        grid_sizer.Add(self.label, 1, wx.EXPAND, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, "Primary Bitmap:")
        grid_sizer.Add(label_11, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        sizer_primary_bitmap.Add(self.primary_bitmap, 1, 0, 0)
        sizer_primary_bitmap.Add(self.primary_bitmap_button, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 0)
        grid_sizer.Add(sizer_primary_bitmap, 1, wx.EXPAND, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, "Disabled Bitmap:")
        grid_sizer.Add(label_12, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        sizer_primary_bitmap.Add(self.disabled_bitmap, 1, 0, 0)
        sizer_primary_bitmap.Add(self.disabled_bitmap_button, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 0)
        grid_sizer.Add(sizer_primary_bitmap, 1, wx.EXPAND, 0)
        label_7 = wx.StaticText(self, wx.ID_ANY, "Event Handler:")
        grid_sizer.Add(label_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        grid_sizer.Add(self.event_handler, 1, wx.EXPAND, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, "(Attribute) Name:")
        grid_sizer.Add(label_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        grid_sizer.Add(self.name, 1, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, "Help String:")
        grid_sizer.Add(label_9, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        grid_sizer.Add(self.help_str, 1, wx.EXPAND, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, "ID:")
        grid_sizer.Add(label_10, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        grid_sizer.Add(self.id, 0, 0, 0)
        grid_sizer.AddGrowableCol(1)
        sizer_5.Add(grid_sizer, 2, wx.EXPAND, 0)
        sizer_5.Add(self.check_radio, 0, wx.ALL, 4)
        sizer_5.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_6.Add(self.ok, 0, wx.ALL, 5)
        sizer_6.Add(self.cancel, 0, wx.ALL, 5)
        sizer_5.Add(sizer_6, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_5, 0, wx.EXPAND, 0)
        sizer_2.Add(self.move_up, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 8)
        sizer_2.Add(self.move_down, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 8)
        sizer_2.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.add, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 8)
        sizer_2.Add(self.remove, 0, wx.BOTTOM | wx.TOP, 8)
        sizer_2.Add(self.add_sep, 0, wx.ALL, 8)
        sizer_2.Add((20, 20), 2, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_1.Add(self.items, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def update_item(self, event):  # wxGlade: ToolsDialog.<event_handler>
        print("Event handler 'update_item' not implemented!")
        event.Skip()

    def move_item_up(self, event):  # wxGlade: ToolsDialog.<event_handler>
        print("Event handler 'move_item_up' not implemented!")
        event.Skip()

    def move_item_down(self, event):  # wxGlade: ToolsDialog.<event_handler>
        print("Event handler 'move_item_down' not implemented!")
        event.Skip()

    def add_item(self, event):  # wxGlade: ToolsDialog.<event_handler>
        print("Event handler 'add_item' not implemented!")
        event.Skip()

    def remove_item(self, event):  # wxGlade: ToolsDialog.<event_handler>
        print("Event handler 'remove_item' not implemented!")
        event.Skip()

    def add_separator(self, event):  # wxGlade: ToolsDialog.<event_handler>
        print("Event handler 'add_separator' not implemented!")
        event.Skip()

    def on_label_edited(self, event):  # wxGlade: ToolsDialog.<event_handler>
        print("Event handler 'on_label_edited' not implemented!")
        event.Skip()

    def show_item(self, event):  # wxGlade: ToolsDialog.<event_handler>
        print("Event handler 'show_item' not implemented!")
        event.Skip()

# end of class ToolsDialog
class MyApp(wx.App):
    def OnInit(self):
        self.dialog = ToolsDialog(None, wx.ID_ANY, "")
        self.SetTopWindow(self.dialog)
        self.dialog.ShowModal()
        self.dialog.Destroy()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()