import os
import shutil

def get_prof():
    # initialize
    usr_prof = "../data/usr_prof/"
    url = "http://ilab.yz.yamagata-u.ac.jp/HackU/user_info/user_info.txt"

    if os.path.isfile(usr_prof + "usr_prof_org.txt") == False: # first download
        cmd = ["wget", "-O", usr_prof + "usr_prof_org.txt", url]
        sp.call(cmd) # download "usr_prof_org.txt"
        shutil.copyfile(usr_prof + "usr_prof_org.txt", usr_prof + "usr_prof.txt") # Saving change file -> usr_prof.txt
    else: # After second
        cmd = ["wget", "-O", usr_prof + "usr_prof_dl.txt", "url"]
        sp.call(cmd)# download "usr_prof_dl.txt"
        prev_modify = (os.stat(usr_prof + "usr_prof_org.txt")).st_mtime
        dl_modify = (os.stat(usr_prof + "usr_prof_dl.txt")).st_mtime
        if prev_modify != dl_modify: # If prof wa a chenged.
            shutil.copyfile(usr_prof + "usr_prof_dl.txt", usr_prof + "usr_prof.txt") # Saving New change file -> usr_prof.txt
