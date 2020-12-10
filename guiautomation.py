from pywinauto import Desktop, Application
app = Application(backend="uia").start("zoom --url=https://auhsdschools.zoom.us/j/7753695672?pwd=NTB1V1FRYTRnalBlYlBidnhXdDd2dz09#success")
#geet = app.start("zoom --url=https://auhsdschools.zoom.us/j/7753695672?pwd=NTB1V1FRYTRnalBlYlBidnhXdDd2dz09#success")

#dialog
#dialog = geet.child_window(title="Zoom Cloud Meetings", control_type="window")
dialog = Desktop(backend="uia").window(title="Zoom Cloud Meetings")
dialog.print_control_identifiers()

#dlg = app.window(title_re="Zoom Meetings")
#dlg.print_ctrl_ids()
#dlg = app.child_window(title="zoom", classname="zoomclass")




