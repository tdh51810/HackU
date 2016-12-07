import random

def kill():
    userdata = eval(open("../data/user_profile/user_prof.txt","r").read())
    kill_list = ["父親","母親","祖父","祖母","兄","姉","弟","妹","叔父","叔母","いとこ"]

    #いとこから優先して◯す
    if int(userdata["いとこ"]) >= 1 :
        userdata["いとこ"] = int(userdata["いとこ"]) - 1
        userdata["いとこ"] = str(userdata["いとこ"])
        number = 10
        updata_prof(userdata)
        return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

    else :
    #叔父、叔母をランダムで選ぶ
        if int(userdata["叔母"]) and int(userdata["叔父"]) >= 1 :
            rand_kill = random.randint(1,2)

            if rand_kill == 1 :
                userdata["叔母"] = int(userdata["叔母"]) - 1
                userdata["叔母"] = str(userdata["叔母"])
                number = 9
                updata_prof(userdata)
                return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

            elif rand_kill == 2 :
                userdata["叔父"] = int(userdata["叔父"]) - 1
                userdata["叔父"] = str(userdata["叔父"])
                number = 8
                updata_prof(userdata)
                return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")
        else :
            #叔父叔母個別
            if int(userdata["叔母"]) >= 1 :
                userdata["叔母"] = int(userdata["叔母"]) - 1
                userdata["叔母"] = str(userdata["叔母"])
                number = 9
                updata_prof(userdata)
                return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

            elif int(userdata["叔父"]) >= 1 :
                userdata["叔父"] = int(userdata["叔父"]) - 1
                userdata["叔父"] = str(userdata["叔父"])
                number = 8
                updata_prof(userdata)
                return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")
            else :
                #祖父、祖母をランダムで選ぶ
                if int(userdata["祖母"]) and int(userdata["祖父"]) >= 1 :
                    rand_kill = random.randint(1,2)

                    if rand_kill == 1 :
                        userdata["祖母"] = int(userdata["祖母"]) - 1
                        userdata["祖母"] = str(userdata["祖母"])
                        number = 3
                        updata_prof(userdata)
                        return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

                    elif rand_kill == 2 :
                        userdata["祖父"] = int(userdata["祖父"]) - 1
                        userdata["祖父"] = str(userdata["祖父"])
                        number = 2
                        updata_prof(userdata)
                        return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

                else :
                    #祖父祖母個別
                    if int(userdata["祖母"]) >= 1 :
                        userdata["祖母"] = int(userdata["祖母"]) - 1
                        userdata["祖母"] = str(userdata["祖母"])
                        number = 3
                        updata_prof(userdata)
                        return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

                    elif int(userdata["祖父"]) >= 1 :
                        userdata["祖父"] = int(userdata["祖父"]) - 1
                        userdata["祖父"] = str(userdata["祖父"])
                        number = 2
                        updata_prof(userdata)
                        return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

                    else :
                        #父、母をランダムで選ぶ
                        if int(userdata["母親"]) and int(userdata["父親"]) >= 1 :
                            rand_kill = random.randint(1,2)

                            if rand_kill == 1 :
                                userdata["母親"] = int(userdata["母親"]) - 1
                                userdata["母親"] = str(userdata["母親"])
                                number = 1
                                updata_prof(userdata)
                                return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

                            elif rand_kill == 2 :
                                userdata["父親"] = int(userdata["父親"]) - 1
                                userdata["父親"] = str(userdata["父親"])
                                number = 0
                                updata_prof(userdata)
                                return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

                        else :
                            #父母個別
                            if int(userdata["母親"]) >= 1 :
                                userdata["母親"] = int(userdata["母親"]) - 1
                                userdata["母親"] = str(userdata["母親"])
                                number = 1
                                updata_prof(userdata)
                                return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

                            elif int(userdata["父親"]) >= 1 :
                                userdata["父親"] = int(userdata["父親"]) - 1
                                userdata["父親"] = str(userdata["父親"])
                                number = 0
                                updata_prof(userdata)
                                return(kill_list[number]+"が亡くなったので、本日は休ませていただきます。")

                            else :
                                return("ERROR：親戚の残りがありません！")


def updata_prof(userdata):
    userdata2 = open("../data/user_profile/user_prof.txt","w")
    userdata0 = str(userdata)
    userdata2.write(userdata0)
    userdata2.close()
