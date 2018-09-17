"""
program: textfielddemo
author: edwardstrachan
"""

from breezypythongui import EasyFrame

class NowYouSeeMe(EasyFrame):
    """Click the button and it should reverse"""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Can You See It Demo")
        
        self.first = self.addLabel(text = "Now you see me", row = 0, column = 0)
        self.second = self.addLabel(text = "", row = 1, column = 0, foreground = "green")
        # The command button
        self.click = self.addButton(text = "Click", row = 2, column = 0, columnspan = 2, command = self.clickme)

    # The event handling method for the button
    def clickme(self):
        self.first["text"] = ""
        self.second["text"] = "Now you dont!"
        self.click["state"] = "normal"
        self.click = self.addButton(text = "Click", row = 2, column = 0, columnspan = 2, command = self.clicknot)
    
    def clicknot(self):
        self.first["text"] = "Now yo see me"
        self.second["text"] = ""
        self.click["state"] = "normal"
        self.click = self.addButton(text = "Click", row = 2, column = 0, columnspan = 2, command = self.clickme)
def main():
    NowYouSeeMe().mainloop()
main()
