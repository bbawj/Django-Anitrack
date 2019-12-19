from HorribleDownloader import Parser


def get_anime_info():
    p = Parser()
    current_shows = p.current_shows

    show_info = []

    for show in current_shows:

        episodes = p.get_episodes(show)
        latest_ep = episodes[0]
        latest_ep_num = latest_ep["episode"]
        latest_ep_title = latest_ep["title"]

        sd_dict = latest_ep["480"]
        hd_dict = latest_ep["720"]
        fhd_dict = latest_ep["1080"]

        aniinfo_dict = {
            "title": latest_ep_title,
            "latest_ep_num": latest_ep_num,
            "ld": False,
            "sd": False,
            "hd": False,
            "fhd": False
        }

        if "XDCC" in sd_dict.keys():  #test for sd quality
            if sd_dict["XDCC"].endswith("[480p]"):
                aniinfo_dict.update({"sd" : True})
            elif sd_dict["XDCC"].endswith("[720p]"):
                aniinfo_dict.update({"hd" : True})
            elif sd_dict["XDCC"].endswith("[1080p]"):
                aniinfo_dict.update({"fhd" : True})
            elif sd_dict["XDCC"].endswith("[360p]"):
                aniinfo_dict.update({"ld" : True})
        else:
            pass

        if "XDCC" in hd_dict.keys():  #test for hd quality
            if hd_dict["XDCC"].endswith("[480p]"):
                aniinfo_dict.update({"sd" : True})
            elif hd_dict["XDCC"].endswith("[720p]"):
                aniinfo_dict.update({"hd" : True})
            elif hd_dict["XDCC"].endswith("[1080p]"):
                aniinfo_dict.update({"fhd" : True})
            elif hd_dict["XDCC"].endswith("[360p]"):
                aniinfo_dict.update({"ld" : True})
        else:
            pass

        if "XDCC" in fhd_dict.keys():  #test for sd quality
            if fhd_dict["XDCC"].endswith("[480p]"):
                aniinfo_dict.update({"sd" : True})
            elif fhd_dict["XDCC"].endswith("[720p]"):
                aniinfo_dict.update({"hd" : True})
            elif fhd_dict["XDCC"].endswith("[1080p]"):
                aniinfo_dict.update({"fhd" : True})
            elif fhd_dict["XDCC"].endswith("[360p]"):
                aniinfo_dict.update({"ld" : True})
        else:
            pass

        show_info.append(aniinfo_dict.copy())
    return show_info
