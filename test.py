import cv2
from gui_automation import GuiAuto
import windows_gui_automation

image_path = "breakoutroom1.png"
ga = GuiAuto()
if ga.detect(cv2.imread(image_path), 0.95):
    ga.click()
