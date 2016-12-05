import glob
import os
import shutil

def get_prof():
    # initialize
    usr_prof = "../data/user_profile/"
    url = "http://ilab.yz.yamagata-u.ac.jp/HackU/user_info/user_info.txt"

    if os.path.isfile(usr_prof + "user_prof_org.txt") == False: # first download
        cmd = ["wget", "-O", usr_prof + "user_prof_org.txt", url]
        sp.call(cmd) # download "user_prof_org.txt"
        shutil.copyfile(usr_prof + "user_prof_org.txt", usr_prof + "user_prof.txt") # Saving change file -> user_prof.txt
    else: # After second
        cmd = ["wget", "-O", usr_proef + "user_prof_dl.txt", "url"]
        sp.call(cmd)# download "usr_prof_dl.txt"
        prev_modify = (os.stat(usr_prof + "user_prof_org.txt")).st_mtime
        dl_modify = (os.stat(usr_prof + "user_prof_dl.txt")).st_mtime
        if prev_modify != dl_modify: # If prof wa a chenged.
            shutil.copyfile(usr_prof + "user_prof_dl.txt", usr_prof + "user_prof.txt") # Saving New change file -> user_prof.txt


def get_trig():
    #initialize
    dirc = "./test/*"
    lsdir = glob.glob(dirc)
    new_time = 0 #float("inf")
    trigger = ""


    if len(lsdir) == 0:
        return(False)

    # Catch trigger
    for files in lsdir:
        file_name = (files.split("/")[-1])
        # If emargency trigger
        if file_name == "emargency_red.txt":
            return("red")
        elif file_name == "emargency_blue.txt":
            return("blue")
        #If normal trigger
        else:
            create_time = (os.stat(files)).st_mtime
            #get a latest trigger
            if create_time >= new_time:
                new_time = create_time
                trigger = files
    with open(trigger, "r") as f:
        f = (f.read()).strip()
    # Reset trigger
    for files in lsdir:
        os.remove(files)
    return(f) # Return trigger type
