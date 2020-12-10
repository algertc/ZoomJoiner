from pywinauto import Desktop, Application
app = Application(backend="uia").start("zoom --url=https://auhsdschools.zoom.us/j/7753695672?pwd=NTB1V1FRYTRnalBlYlBidnhXdDd2dz09#success")

#dialog
dialog = Desktop(backend="uia").window(title="Zoom Cloud Meetings", top_level_only=False)
dialog.print_control_identifiers()

signIn = dialog.child_window(title="Sign In", auto_id="Button5", control_type="Button")
signIn.click()
#clicks
#dialog.child_window(title="Sign In", auto_id="Sign InButton", control_type="Button").click()


