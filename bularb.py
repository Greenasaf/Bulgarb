from pathlib import Path

ALL_CHANNELS_NOT_SORTED = {
    "Sport": {
        "MATCH! Futbol 3": {
            "url": ["https://www.gledaitv.fan/match-futbol-3-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/b/bf/NTV-Plus_Futbol_3_%282014%2C_prototype%29.svg/revision/latest/scale-to-width-down/250?cb=20201017144338",
        },
        "MATCH! Futbol 2": {
            "url": ["https://www.gledaitv.fan/match-futbol-2-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/1/15/NTV-Plus_Futbol_2_%282014%2C_prototype%29.svg/revision/latest/scale-to-width-down/250?cb=20201017143828",
        },
        "MATCH! Futbol 1": {
            "url": ["https://www.gledaitv.fan/match-futbol-1-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/9/98/NTV-Plus_Futbol_1_%282014%2C_prototype%29.svg/revision/latest/scale-to-width-down/250?cb=20201017143436",
        },
        "Bein Sports": {
            "url": ["https://www.gledaitv.fan/bein-sports-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/4/45/BeIN_Sports_2017_flat.svg/revision/latest/scale-to-width-down/300?cb=20230910182143",
        },
        "bTV Action": {
            "url": ["https://www.seirsanduk.com/btv-action-online.xhtml"],
            "url_hd": "",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRS6YU0bglnotgXBthpeCCGK6bGRLRA09gwYg&s",
        },
        "Diema Sport": {
            "url": [
                "https://www.seirsanduk.com/diema-sport-online.xhtml",
                "https://www.gledaitv.fan/diema-sport-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/diema-sport-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/4/45/Diema_Sport_HD.svg/revision/latest/scale-to-width-down/300?cb=20250505001930",
        },
        "Diema Sport 2": {
            "url": [
                "https://www.seirsanduk.com/diema-sport-2-online.xhtml",
                "https://www.gledaitv.fan/diema-sport-2-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/diema-sport-2-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/3/36/Diema_Sport_2_HD.svg/revision/latest/scale-to-width-down/300?cb=20250505001624",
        },
        "Diema Sport 3": {
            "url": [
                "https://www.seirsanduk.com/diema-sport-3-online.xhtml",
                "https://www.gledaitv.fan/diema-sport-3-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/diema-sport-3-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/1/17/Diema_Sport_3_HD.svg/revision/latest/scale-to-width-down/300?cb=20250505000657",
        },
        "Eurosport 1 BG": {
            "url": [
                "https://www.seirsanduk.com/eurosport-1-online.xhtml",
                "https://www.gledaitv.fan/eurosport-1-bg-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/eurosport-1-bg-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/e/e7/Eurosport_1_2022.svg/revision/latest/scale-to-width-down/300?cb=20220806090310",
        },
        "Eurosport 2 BG": {
            "url": [
                "https://www.seirsanduk.com/eurosport-2-online.xhtml",
                "https://www.gledaitv.fan/eurosport-2-bg-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/eurosport-2-bg-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/1/16/Eurosport_2_2022.svg/revision/latest/scale-to-width-down/300?cb=20220417183127",
        },
        "Max Sport 1": {
            "url": [
                "https://www.seirsanduk.com/max-sport-1-online.xhtml",
                "https://www.gledaitv.fan/max-sport-1-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/max-sport-1-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/5/5e/Max_Sport_1_HD.svg/revision/latest/scale-to-width-down/300?cb=20250505002452",
        },
        "Max Sport 2": {
            "url": [
                "https://www.seirsanduk.com/max-sport-2-online.xhtml",
                "https://www.gledaitv.fan/max-sport-2-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/max-sport-2-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/a/ac/Max_Sport_2_HD.svg/revision/latest/scale-to-width-down/300?cb=20250505002701",
        },
        "Max Sport 3": {
            "url": [
                "https://www.seirsanduk.com/max-sport-3-online.xhtml",
                "https://www.gledaitv.fan/max-sport-3-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/max-sport-3-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/61/Max_Sport_3_HD.svg/revision/latest/scale-to-width-down/300?cb=20250505002837",
        },
        "Max Sport 4": {
            "url": [
                "https://www.seirsanduk.com/max-sport-4-online.xhtml",
                "https://www.gledaitv.fan/max-sport-4-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/max-sport-4-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/62/Max_Sport_4_HD.svg/revision/latest/scale-to-width-down/300?cb=20250505003011",
        },
        "Nova Sport": {
            "url": [
                "https://www.seirsanduk.com/nova-sport-online.xhtml",
                "https://www.gledaitv.fan/nova-sport-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/nova-sport-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/9/9e/Nova_Sport_2010_flat.svg/revision/latest/scale-to-width-down/150?cb=20240731175840",
        },
        "Ring BG": {
            "url": [
                "https://www.seirsanduk.com/ring-bg-online.xhtml",
                "https://www.gledaitv.fan/ring-bg-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/ring-bg-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/0/03/Ring.svg/revision/latest/scale-to-width-down/200?cb=20210516104914",
        },
        "Sports Tv": {
            "url": ["https://www.gledaitv.fan/sports-tv-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/a/a1/Sport_TV_2023.svg/revision/latest/scale-to-width-down/300?cb=20231020131831",
        },
        "TJK Tv": {
            "url": ["https://www.gledaitv.fan/tjk-tv-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/tjk-tv-hd-live-tv.html",
            "image": "https://about.me/cdn-cgi/image/q=80,dpr=1,f=auto,fit=cover,w=1024,h=512,gravity=auto/https://assets.about.me/background/users/t/j/k/tjktvizle_1595702475_756.jpg",
        },
        "Trt Spor": {
            "url": ["https://www.gledaitv.fan/trt-spor-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/trt-spor-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/9/92/TRT_Spor_logo_%282022%29.svg/revision/latest/scale-to-width-down/300?cb=20220107231944",
        },
        "DAZN Combat": {
            "url": ["https://www.parsatv.com/name=DAZN-Combat#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/8/83/DAZN_2019_logo.svg/revision/latest/scale-to-width-down/200?cb=20210824002335",
        },
        "Red Bull TV": {
            "url": ["https://www.parsatv.com/name=Red-Bull-TV#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/3/3c/Red_Bull_TV.svg/revision/latest/scale-to-width-down/250?cb=20180423100712",
        },
        "Fuel TV": {
            "url": ["https://www.parsatv.com/name=Fuel-TV#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/6a/Fuel_TV.svg/revision/latest/scale-to-width-down/150?cb=20100323111006",
        },
        "SportItalia": {
            "url": ["https://www.parsatv.com/name=Sportitalia#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/4/4a/Logo_si.JPG/revision/latest/scale-to-width-down/200?cb=20161118191326",
        },
        "Game Plus": {
            "url": ["https://www.parsatv.com/name=Game-Plus#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/1/1a/Game_%282002%29.svg/revision/latest/scale-to-width-down/250?cb=20221221165906",
        },
        "Super Tennis": {
            "url": ["https://www.parsatv.com/name=Super-Tennis#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/4/4e/Super_Tennis_2016.svg/revision/latest/scale-to-width-down/250?cb=20201227003011",
        },
        "beIN Sports Xtra": {
            "url": ["https://www.parsatv.com/name=beIN-Sports-Xtra#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/0/0b/BeIN_Xtra.PNG/revision/latest/scale-to-width-down/300?cb=20201108180437",
        },
        "ACC Digital Network": {
            "url": ["https://www.parsatv.com/name=ACC-Digital-Network#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/66/Atlantic_Coast_Conference_2014.svg/revision/latest/scale-to-width-down/250?cb=20250612020101",
        },
        "Fifa +": {
            "url": ["https://www.parsatv.com/name=FIFA-Plus#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/9/9c/FIFA%2B_%282025%29.svg/revision/latest/scale-to-width-down/300?cb=20250521135758",
        },
        "NHL TV": {
            "url": ["https://www.parsatv.com/name=NHL-TV"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/3/3a/05_NHL_Shield.svg/revision/latest/scale-to-width-down/200?cb=20191208162044",
        },
        "Motor Vision": {
            "url": ["https://www.parsatv.com/name=Motorvision-TV#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/7/70/Motorvision_2023.svg/revision/latest/scale-to-width-down/300?cb=20230921093539",
        },
        "Canal Motor": {
            "url": ["https://www.parsatv.com/name=Canal-Motor#sport"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/8/8e/Motors_TV.svg/revision/latest/scale-to-width-down/300?cb=20100330070517",
        },
        "beIN Sports Xtra Espanol": {
            "url": ["https://www.parsatv.com/name=beIN-Sports-Xtra-Espanol#spanish"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/8/8e/Logo-bein-sport-xtra-espanol-plain.png/revision/latest/scale-to-width-down/300?cb=20240923145001",
        },
        "Sports TV": {
            "url": ["https://www.parsatv.com/name=Sports-TV#turkish"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/a/a1/Sport_TV_2023.svg/revision/latest/scale-to-width-down/300?cb=20231020131831",
        },
        "RTA Sport": {
            "url": ["https://www.parsatv.com/name=RTA-Sport#afghan"],
            "url_hd": "",
            "image": "https://i.postimg.cc/6qDg2JN8/rtasport.png",
        },
        "KTV Sport 2": {
            "url": ["https://www.parsatv.com/name=KTV-Sport-2#google_vignette"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/2/21/KTV_28UHF.png/revision/latest/scale-to-width-down/250?cb=20180715160408",
        },
        "KTV Sport": {
            "url": ["https://www.parsatv.com/name=KTV-Sport#google_vignette"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/2/21/KTV_28UHF.png/revision/latest/scale-to-width-down/250?cb=20180715160408",
        },
        "Dubai Sports 3 TV": {
            "url": ["https://www.parsatv.com/name=Dubai-Sports-3-TV#arabic"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/8/8b/Dubai_Sports_Logo_in_2023.png/revision/latest/scale-to-width-down/300?cb=20241130031009",
        },
        "Dubai Sports 2 TV": {
            "url": ["https://www.parsatv.com/name=Dubai-Sports-2"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/8/8b/Dubai_Sports_Logo_in_2023.png/revision/latest/scale-to-width-down/300?cb=20241130031009",
        },
        "Dubai Sports 1 TV": {
            "url": ["https://www.parsatv.com/name=Dubai-Sports-1"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/8/8b/Dubai_Sports_Logo_in_2023.png/revision/latest/scale-to-width-down/300?cb=20241130031009",
        },
        "GEM Sport": {
            "url": ["https://www.parsatv.com/name=GEM-Sport#persian"],
            "url_hd": "",
            "image": "https://gemgroup.tv/assets/images/channels/icon_34.png",
        },
        "Telewebion Sport 3": {
            "url": ["https://www.parsatv.com/name=Telewebion-Sport-3#persian"],
            "url_hd": "",
            "image": "https://logoyab.com/wp-content/uploads/2024/05/TELEWEBION-VARZESH-3-Logo-1030x1030.png",
        },
        "Telewebion Sport 2": {
            "url": ["https://www.parsatv.com/name=Telewebion-Sport-2#persian"],
            "url_hd": "",
            "image": "https://logoyab.com/wp-content/uploads/2024/05/TELEWEBION-VARZESH-2-Logo-1030x1030.png",
        },
        "Telewebion Sport 1": {
            "url": ["https://www.parsatv.com/name=Telewebion-Sport-1#persian"],
            "url_hd": "",
            "image": "https://logoyab.com/wp-content/uploads/2024/05/TELEWEBION-VARZESH-1-Logo-1030x1030.png",
        },
        "Abu Dhabi Sports 2": {
            "url": ["https://www.parsatv.com/name=Abu-Dhabi-Sports-2#arabic"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/66/AD_Sports_2023.png/revision/latest/scale-to-width-down/300?cb=20231008181135",
        },
        "Abu Dhabi Sports 1": {
            "url": ["https://www.parsatv.com/name=Abu-Dhabi-Sports-1#arabic"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/66/AD_Sports_2023.png/revision/latest/scale-to-width-down/300?cb=20231008181135",
        },
    },
    "Movie": {
        "AMC": {
            "url": ["https://www.gledaitv.fan/amc-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/a/ad/AMC_Networks_S21.svg/revision/latest/scale-to-width-down/200?cb=20220820072921",
        },
        "AXN": {
            "url": [
                "https://www.seirsanduk.com/axn-online-gledai-tv.xhtml",
                "https://www.gledaitv.fan/axn-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/d/dc/2016_AXN_logo.svg/revision/latest/scale-to-width-down/300?cb=20201126064846",
        },
        "bTV Action": {
            "url": ["https://www.seirsanduk.com/btv-action-online.xhtml"],
            "url_hd": "",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRS6YU0bglnotgXBthpeCCGK6bGRLRA09gwYg&s",
        },
        "bTV Cinema": {
            "url": [
                "https://www.seirsanduk.com/btv-cinema-online.xhtml",
                "https://www.gledaitv.fan/btv-cinema-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/btv-cinema-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/f/f5/BTV_Cinema_%282016%29.svg/revision/latest/scale-to-width-down/300?cb=20200125184619",
        },
        "bTV Comedy": {
            "url": [
                "https://www.seirsanduk.com/btv-comedy-online.xhtml",
                "https://www.gledaitv.fan/btv-comedy-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/btv-comedy-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/9/9f/BTV_Comedy_HD.jpg/revision/latest?cb=20240319192449",
        },
        "bTV Lady": {
            "url": [
                "https://www.seirsanduk.com/btv-lady-online.xhtml",
                "https://www.gledaitv.fan/btv-lady-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/btv-lady-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/5/51/BTV_Lady_%282016%29.svg/revision/latest/scale-to-width-down/250?cb=20200125184015",
        },
        "Diema": {
            "url": ["https://www.gledaitv.fan/diema-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/b/b2/Diema.png/revision/latest/scale-to-width-down/150?cb=20170315162656",
        },
        "Diema Family": {
            "url": [
                "https://www.seirsanduk.com/diema-family-online.xhtml",
                "https://www.gledaitv.fan/diema-family-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/7/71/Diema_Family_2019.svg/revision/latest/scale-to-width-down/150?cb=20240731170629",
        },
        "Epic Drama": {
            "url": [
                "https://www.seirsanduk.com/epic-drama-online.xhtml",
                "https://www.gledaitv.fan/epic-drama-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/1/1e/Epic_Drama_2018.svg/revision/latest/scale-to-width-down/200?cb=20191113170018",
        },
        "FilmBox Extra": {
            "url": ["https://www.gledaitv.fan/filmbox-extra-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/filmbox-extra-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/2/2c/FilmBox_Extra_HD.svg/revision/latest/scale-to-width-down/250?cb=20171210164807",
        },
        "FilmBox Stars": {
            "url": ["https://www.gledaitv.fan/filmbox-stars-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/filmbox-stars-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/6e/FilmBox_Stars.svg/revision/latest/scale-to-width-down/250?cb=20200901135021",
        },
        "Fox Life": {
            "url": ["https://www.gledaitv.fan/fox-life-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/fox-life-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/4/4e/Fox_Life.svg/revision/latest/scale-to-width-down/300?cb=20190426124214",
        },
        "Fox Crime": {
            "url": ["https://gledaibgtv.com/fox-crime-online"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/6b/Fox_Crime_logo.svg/revision/latest/scale-to-width-down/250?cb=20171230124159",
        },
        "Kino Nova": {
            "url": [
                "https://www.seirsanduk.com/kino-nova-online.xhtml",
                "https://www.gledaitv.fan/kino-nova-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/a/a6/Kinonova_re.svg/revision/latest/scale-to-width-down/250?cb=20260101161359",
        },
        "Movie Star": {
            "url": ["https://www.gledaitv.fan/movie-star-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/movie-star-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/3/30/Movie_Starz_Video_Logo_%28Fixed%29.svg/revision/latest/scale-to-width-down/300?cb=20230605025253",
        },
        "Scream": {
            "url": ["https://www.gledaitv.fan/scream-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/scream/images/f/f3/Scream_Logo_Fanfic.jpg/revision/latest/thumbnail-down/width/500/height/320?cb=20140328233314",
        },
        "STAR Channel": {
            "url": [
                "https://www.seirsanduk.com/star-channel-online.xhtml",
                "https://www.gledaitv.fan/star-channel-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/star-channel-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/c/cd/Star_Channel_2023.svg/revision/latest/scale-to-width-down/250?cb=20231209070650",
        },
        "Star Crime": {
            "url": [
                "https://www.seirsanduk.com/star-crime-online.xhtml",
                "https://www.gledaitv.fan/star-crime-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/star-crime-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/4/40/Star_Crime_2023.svg/revision/latest/scale-to-width-down/250?cb=20231208002839",
        },
        "Star Life": {
            "url": ["https://www.seirsanduk.com/star-life-online.xhtml"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/b/b9/Star_Life_2023.svg/revision/latest/scale-to-width-down/250?cb=20231209041522",
        },
    },
    "Science": {
        "Animal Planet": {
            "url": ["https://www.gledaitv.fan/animal-planet-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/animal-planet-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/e/e3/Animal_Planet_2018.svg/revision/latest/scale-to-width-down/250?cb=20210825085349",
        },
        "Discovery Channel": {
            "url": [
                "https://www.seirsanduk.com/discovery-channel-online.xhtml",
                "https://www.gledaitv.fan/discovery-channel-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/discovery-channel-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/a/a8/Discovery_Channel_2019.svg/revision/latest/scale-to-width-down/300?cb=20210519155203",
        },
        "DMAX": {
            "url": ["https://www.gledaitv.fan/dmax-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/dmax-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/c/c0/DMAX_%282026%29.svg/revision/latest/scale-to-width-down/250?cb=20260113020915",
        },
        "DocuBox": {
            "url": ["https://www.gledaitv.fan/docubox-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/docubox-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/0/02/DocuBox_%282013%29.svg/revision/latest/scale-to-width-down/250?cb=20171210215646",
        },
        "History Channel": {
            "url": ["https://www.gledaitv.fan/history-channel-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/history-channel-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/e/e8/History_2021.png/revision/latest/scale-to-width-down/200?cb=20240302050750",
        },
        "Investigation Discovery": {
            "url": [
                "https://www.seirsanduk.com/investigation-discovery-online.xhtml",
                "https://www.gledaitv.fan/investigation-discovery-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/investigation-discovery-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/0/0b/ID-2020.svg/revision/latest/scale-to-width-down/250?cb=20200413032314",
        },
        "Nat Geo Wild": {
            "url": [
                "https://www.seirsanduk.com/nat-geo-wild-online.xhtml",
                "https://www.gledaitv.fan/nat-geo-wild-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/nat-geo-wild-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/d/d9/National_Geographic_Wild_2018.svg/revision/latest/scale-to-width-down/200?cb=20180903172554",
        },
        "National Geographic": {
            "url": [
                "https://www.seirsanduk.com/national-geographic-online.xhtml",
                "https://www.gledaitv.fan/national-geographic-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/national-geographic-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/c/c6/National_Geographic_2008.svg/revision/latest/scale-to-width-down/250?cb=20170701154034",
        },
        "TLC": {
            "url": [
                "https://www.seirsanduk.com/tlc-online.xhtml",
                "https://www.gledaitv.fan/tlc-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/tlc-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/b/b1/TLC_%282021%29.svg/revision/latest/scale-to-width-down/250?cb=20220703193228",
        },
        "TRT Belgesel": {
            "url": ["https://www.gledaitv.fan/trt-belgesel-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/trt-belgesel-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/5/5e/TRT_Belgesel_%282019%29.svg/revision/latest/scale-to-width-down/300?cb=20210205141825",
        },
        "Viasat Explore": {
            "url": ["https://www.gledaitv.fan/viasat-explore-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/viasat-explore-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/e/ec/Viasat_Explore_2022.svg/revision/latest/scale-to-width-down/150?cb=20220119212514",
        },
        "Viasat History": {
            "url": ["https://www.gledaitv.fan/viasat-history-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/b/b7/Viasat_History_2022.svg/revision/latest/scale-to-width-down/150?cb=20220119212113",
        },
        "Viasat Nature": {
            "url": ["https://www.gledaitv.fan/viasat-nature-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/b/b5/Viasat_Nature_2022.svg/revision/latest/scale-to-width-down/150?cb=20220119211909",
        },
        "Yaban Tv": {
            "url": ["https://www.gledaitv.fan/yaban-tv-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/yaban-tv-hd-live-tv.html",
            "image": "https://yt3.googleusercontent.com/ytc/AIdro_ml4Ec8YVG61pHTn1Q1zwpbDv_6RmPPPtFe2e4ysRhBAoo=s900-c-k-c0x00ffffff-no-rj",
        },
    },
    "News": {
        "Bulgaria ON AIR Tv": {
            "url": [
                "https://www.seirsanduk.com/bulgaria-on-air-online.xhtml",
                "https://www.gledaitv.fan/bulgaria-on-air-tv-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/5/5f/Bgonair-new2.png/revision/latest/scale-to-width-down/210?cb=20160102175130",
        },
        "BNT 1": {
            "url": [
                "https://www.seirsanduk.com/bnt-1-online.xhtml",
                "https://www.seirsanduk.com/bnt-1-online.xhtml",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/6f/BNT_1_2018.svg/revision/latest/scale-to-width-down/300?cb=20180909194302",
        },
        "BNT 2": {
            "url": [
                "https://www.seirsanduk.com/bnt-2-online.xhtml",
                "https://www.gledaitv.fan/bnt-2-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/1/1f/BNT_2_2018.svg/revision/latest/scale-to-width-down/300?cb=20180909194412",
        },
        "BNT 3": {
            "url": [
                "https://www.seirsanduk.com/bnt-3-online.xhtml",
                "https://www.gledaitv.fan/bnt-3-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/3/32/BNT_3_2018.svg/revision/latest/scale-to-width-down/300?cb=20180909194740",
        },
        "BNT 4": {
            "url": [
                "https://www.seirsanduk.com/bnt-4-online.xhtml",
                "https://www.gledaitv.fan/bnt-4-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/e/e9/BNT_4_2018.svg/revision/latest/scale-to-width-down/300?cb=20180909194558",
        },
        "bTV": {
            "url": [
                "https://www.seirsanduk.com/btv-online.xhtml",
                "https://www.gledaitv.fan/btv-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/btv-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/e/e6/BTV_Bulgaria_2025.svg/revision/latest/scale-to-width-down/250?cb=20250701093143",
        },
        "Bulgaria 24": {
            "url": ["https://www.gledaitv.fan/bulgaria-24-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/0/09/300px-Bulgaria_24_TV.png/revision/latest?cb=20200518050332",
        },
        "Evrokom": {
            "url": [
                "https://www.seirsanduk.com/evrokom-online.xhtml",
                "https://www.gledaitv.fan/evrokom-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/a/a5/Eurokom_1996.png/revision/latest/scale-to-width-down/300?cb=20170802171200",
        },
        "Kanal 3": {
            "url": ["https://www.gledaitv.fan/kanal-3-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/3/32/Kanal3.png/revision/latest/scale-to-width-down/150?cb=20160211132831",
        },
        "Nova": {
            "url": [
                "https://www.seirsanduk.com/nova-tv-online.xhtml",
                "https://www.gledaitv.fan/nova-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/nova-hd-live-tv.html",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOGhFKRgJ9roOiXry-ysDZreZQzVYuyjXwGw&s",
        },
        "Pervyy kanal": {
            "url": ["https://www.gledaitv.fan/pervyy-kanal-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/pervyy-kanal-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/4/40/%D0%9F%D0%B5%D1%80%D0%B2%D1%8B%D0%B9_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%BE%D0%B9_2.png/revision/latest/scale-to-width-down/200?cb=20200511140953",
        },
        "VTK": {
            "url": [
                "https://www.seirsanduk.com/vtk-online.xhtml",
                "https://www.gledaitv.fan/vtk-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/f/f2/Vtk3.png/revision/latest/scale-to-width-down/220?cb=20200518050925",
        },
    },
    "Kids": {
        "Cartoon Network": {
            "url": [
                "https://www.seirsanduk.com/cartoon-network-online.xhtml",
                "https://www.gledaitv.fan/cartoon-network-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/e/ee/Cartoon_Network_2010.svg/revision/latest/scale-to-width-down/250?cb=20210726224754",
        },
        "Disney Channel": {
            "url": ["https://www.gledaitv.fan/disney-channel-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/f/f0/DISNEYCHANNEL-2025.svg/revision/latest/scale-to-width-down/300?cb=20251113064305",
        },
        "Nick Jr.": {
            "url": [
                "https://www.seirsanduk.com/nick-jr-online.xhtml",
                "https://www.gledaitv.fan/nick-jr-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/5/55/Nick_Jr..svg/revision/latest/scale-to-width-down/250?cb=20251017154510",
        },
        "Nick Toons": {
            "url": ["https://www.gledaitv.fan/nick-toons-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/69/Nicktoons_2023_Logo.svg/revision/latest/scale-to-width-down/300?cb=20240724194938",
        },
        "Nickelodeon": {
            "url": [
                "https://www.seirsanduk.com/nickelodeon-online.xhtml",
                "https://www.gledaitv.fan/nickelodeon-live-tv.html",
            ],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/0/07/Nickelodeon_%282009%29.svg/revision/latest/scale-to-width-down/350?cb=20180306141612",
        },
        "EKids": {
            "url": ["https://www.seirsanduk.com/ekids-online.xhtml"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/0/04/Ekids.png/revision/latest/scale-to-width-down/200?cb=20150912152237",
        },
        "Trt Çocuk": {
            "url": ["https://www.gledaitv.fan/trt-cocuk-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/trt-cocuk-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/1/1a/TRT_%C3%87ocuk_logo_%282021%29.svg/revision/latest/scale-to-width-down/300?cb=20211101143853",
        },
    },
    "Worldwide": {
        "24 Kitchen": {
            "url": [
                "https://www.seirsanduk.com/24-kitchen-televizia-online.xhtml",
                "https://www.gledaitv.fan/24-kitchen-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/24-kitchen-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/2/29/24_kitchen_2022_Portugal.svg/revision/latest/scale-to-width-down/300?cb=20230117133430",
        },
        "AGRO": {
            "url": ["https://www.gledaitv.fan/agro-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/b/b0/Agro-RedeGlobo.JPG/revision/latest/scale-to-width-down/400?cb=20160723011224",
        },
        "bTV Action": {
            "url": ["https://www.gledaitv.fan/btv-action-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/btv-action-hd-live-tv.html",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRS6YU0bglnotgXBthpeCCGK6bGRLRA09gwYg&s",
        },
        "Bulgaria ON AIR": {
            "url": ["https://www.gledaitv.fan/bulgaria-on-air-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/5/5f/Bgonair-new2.png/revision/latest/scale-to-width-down/210?cb=20160102175130",
        },
        "Byeaz Tv": {
            "url": ["https://www.gledaitv.fan/byeaz-tv-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/byeaz-tv-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/9/96/Beyaz_tv_2012-2022.png/revision/latest/scale-to-width-down/250?cb=20250720181730",
        },
        "Code Fashion": {
            "url": ["https://www.gledaitv.fan/code-fashion-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/60/Fashion.png/revision/latest/scale-to-width-down/200?cb=20241104092044",
        },
        "Code Health": {
            "url": ["https://www.gledaitv.fan/code-health-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/0/00/Health_2025.png/revision/latest/scale-to-width-down/200?cb=20250117165029",
        },
        "Kanal 0": {
            "url": ["https://www.gledaitv.fan/kanal-0-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/kabal/images/3/39/Site-community-image/revision/latest/thumbnail-down/width/500/height/320?cb=20240516211240",
        },
        "Kanal D": {
            "url": ["https://www.gledaitv.fan/kanal-d-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/kanal-d-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/8/86/Kanal_D_Logo_%282011-present%29_-HD-.png/revision/latest/scale-to-width-down/200?cb=20171227122658",
        },
        "Show Tv": {
            "url": ["https://www.gledaitv.fan/show-tv-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/show-tv-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/4/4b/Show_TV.svg/revision/latest/scale-to-width-down/250?cb=20161114192209",
        },
        "Star Tv": {
            "url": ["https://www.gledaitv.fan/star-tv-live-tv.html"],
            "url_hd": "https://www.gledaitv.fan/star-tv-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/2/28/Star_TV_2016.svg/revision/latest/scale-to-width-down/200?cb=20201201120714",
        },
        "TLC BG": {
            "url": ["https://www.gledaitv.fan/tlc-bg-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/b/b1/TLC_%282021%29.svg/revision/latest/scale-to-width-down/250?cb=20220703193228",
        },
        "Travel Channel": {
            "url": [
                "https://www.seirsanduk.com/travel-channel-online.xhtml",
                "https://www.gledaitv.fan/travel-channel-live-tv.html",
            ],
            "url_hd": "https://www.gledaitv.fan/travel-channel-hd-live-tv.html",
            "image": "https://static.wikia.nocookie.net/logopedia/images/8/85/Travel_Channel_2018.svg/revision/latest/scale-to-width-down/250?cb=20241104144156",
        },
        "Travel TV": {
            "url": ["https://www.seirsanduk.com/travel-tv-online.xhtml"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/5/55/Travel_2024.svg/revision/latest/scale-to-width-down/300?cb=20240815000900",
        },
        "TVN": {
            "url": ["https://www.gledaitv.fan/tvn-live-tv.html"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/6/66/TVN_Poland.svg/revision/latest/scale-to-width-down/200?cb=20170730155409",
        },
        "7/8 TV": {
            "url": ["https://www.seirsanduk.com/7-8-tv-online.xhtml"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/f/fa/7-8_TV.svg/revision/latest/scale-to-width-down/158?cb=20210516111115",
        },
        "Bloomberg": {
            "url": ["https://www.seirsanduk.com/bloomberg-tv-online.xhtml"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/2/21/Bloomberg_2015.svg/revision/latest/scale-to-width-down/300?cb=20171125073306",
        },
        "Diema": {
            "url": ["https://www.seirsanduk.com/diema-online.xhtml"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/b/b2/Diema.png/revision/latest/scale-to-width-down/150?cb=20170315162656",
        },
        "TV 1": {
            "url": ["https://www.seirsanduk.com/tv-1-online.xhtml"],
            "url_hd": "",
            "image": "https://static.wikia.nocookie.net/logopedia/images/0/00/TV_1.svg/revision/latest/scale-to-width-down/200?cb=20210107171100",
        },
    },
}

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def sanitize(text):
    return str(text).replace("\
", " ").replace("\\r", " ").strip()

def unique(seq):
    seen = set()
    out = []
    for item in seq:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out

def build_m3u(channels, group_title=None):
    lines = ["#EXTM3U"]
    for channel_name, info in channels.items():
        urls = []
        if info.get("url_hd"):
            urls.append(info["url_hd"])
        urls.extend(info.get("url", []))
        urls = unique(urls)
        for url in urls:
            name = sanitize(channel_name)
            group = sanitize(group_title) if group_title else sanitize(info.get("group", ""))
            logo = sanitize(info.get("image", ""))
            extinf = f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}"'
            if group:
                extinf += f' group-title="{group}"'
            extinf += f",{name}"
            lines.append(extinf)
            lines.append(url)
    return "\
".join(lines) + "\
"

def main():
    all_channels = {}
    for category, channels in ALL_CHANNELS_NOT_SORTED.items():
        sorted_channels = dict(sorted(channels.items(), key=lambda x: x[0].lower()))
        (OUTPUT_DIR / f"{category}.m3u").write_text(build_m3u(sorted_channels, group_title=category), encoding="utf-8")
        for name, info in sorted_channels.items():
            all_channels[f"{category} - {name}"] = {**info, "group": category}
    (OUTPUT_DIR / "all_channels.m3u").write_text(
        build_m3u(dict(sorted(all_channels.items(), key=lambda x: x[0].lower()))),
        encoding="utf-8"
    )

if __name__ == "__main__":
    main()
