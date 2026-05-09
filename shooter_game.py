#Создай собственный Шутер!


# game.py
from pygame import * # nonknouaeM Bce dyHkunn wa 6n6nmoTekw pygame (oha HyxHa ANA coanaHun wrp)

from random import randint # nionknouaeM 中yHkumo randint，uTo6bl reHepwpoeaTb cnyuaiihale umcna (ana KoopnnHhaTeparoe)

from time import time as timer # Monknwuaem dyHkumio ana pa6oTb co BpemeHem W naeM ei kopoTkoe uma timer

# nonrpyxkaeM oOTnenbHO 中yHKUWWM ANA paboT co upwToM

font.init() # BknouaeM wHcTpyMeHT nna pa6oTbl c TekcTom B urpe

font1 = font.Font(None, 80) # CoanaeM Kkpynhaii upwT (pasMep 86) ana Hannwcei no6enpl u nopaxenna

win = font1.render('YOU WIN!', True, (255, 255, 255)) # CoanaeM KapTuHky c 6enbim TekcToM ‘YOU WIN!"
lose = font1.render('YOU LOSE!', True, (180, 0, 0)) # CoanaeM KapTMHKy c KpacHbim TeKcTom ‘YOU LOSE!"

font2 = font.Font(None, 36) # Co3aaem upnT nomeHbue (pasmep 36) ana cdeTa u xu3Hel

# ohoBan Myablka

mixer.init() # Bknouaem MHcTpyMeHt ana pa6oTb co 3Bykom
mixer.music.load("space.ogg") # 3arpyxaem 中oHoBylo My3ablky wa 中aiina

mixer.music.play() # 3anyckaem 中oHoBy Myabky，uTo6b oHa wrpana

fire_sound = mixer.Sound('fire.ogg') # 3arpyxaem KopoTKyi 3ByK BblcTpena B nepemeHHyi

# HaM HyxHbI Takywe KapTWHHKW (COxpaHAeM Ha3BaHnA daiinoB B nepeMeHHble ANA yno6cTBa) :
img_back = "galaxy.jpg" # oH urpbl (Kocmoc)

img_bullet = "bullet.png" # nyna

img_hero = "rocket.png" # rnaBHeiii repo (pakeTa)
img_enemy = "ufo.png" # spar (HMO)

img_ast = "asteroid.png" # npenatctene (actepona)

score = 0 # MepemenHaa ana nogcueta c6uTHIx Kopabnei (Haw cueT)

goal = 20 # CTonbKo Kopa6ne HyxHO c6uTb，uTo6b BbwrpaTb

lost = 0 # MepemeHHaa nna noncueTa nponyueHHbix BparoB (yneTenu 3a 3KpaH)
max_lost = 10 # Ecnm nponyctum cTonbko Bparos — npourpaem

life = 3 # Konwuecteo xn3aHe Hawero kopa6na

# KNacc-poguTenb ANA npyrwx cnpaiiToe (6a30BaA 3aroTOBKa ANA BCex OObeKTOB Ha 3kpaHhe)
class GameSprite(sprite.Sprite):
# KOHCTpykTOp knacca (HacTpoiiku，KkoTopue NpMMeHAWTCA npw cosnahww o6bekTa)
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed) :
# BulableaewM BcTpoeHhblif koHcTpykTop U3 pygame，JyTo6b o6bekT NpaBUNbHO pa6oTan
        sprite.Sprite.__init__(self)

# 3arpyxaeM KapTuHky o6bekTa Mm MeHAeM ee paaMep Ha size_x M size_y
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed # 3anaeM ckopocTs AnBWXeHWR oO6bekTa

# nionyuaeM HeBugumeli npamoyronbHuK (pamMKy) BOKpyr KapTMHKM, YTOGbI OTCNEXUBaTb CTONKHOBeHMA
        self.rect = self.image.get_rect()

        self.rect.x = player_x # CTaBuM pamky Ha HyXxHyW noawuwo no ropuzoHTann (X)

        self.rect.y = player_y # CTaBuM pamky Ha HyxHyI no3nuwmo no BepTuKanu (Y)

# meToa, oTpucosbieaiouni repon Ha oKHe

    def reset(self):
    # Pucyem KapTWHHKY O6beKTa Ha 3kpahe B TeX KOOpAMHaTax, rae ceiiuac HaxOAMTCA ero paMKa
        window.blit(self.image, (self.rect.x, self.rect.y))

    # Knacc rnasHoro urpoKa (Haw Kopa6nb), oH 6epeT Bce ceoiicTea ma GameSprite
class Player(GameSprite):
# MeTOR ANA ynpaBneHuA Kopabnem cTpenkamu KnaBuaTypbl
    def update(self):
        keys = key.get_pressed() # Monyuaem cnucok Bcex HaxaTBIX KnaBwu MpAMo ceiiuac
# Ecaw Hakata cTpenka B/IEBO u Mbl He ynepnmwmcb B MeBbIi Kpait 3kpaha (x > 5)
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed # JIsuraem Kopa6nb Beneeo (ywmehbuaem X)
        # Ecaw Hakata cTpenka BMPABO wm Mbl He ynepnwncb B npaBbiii Kpai (yunTbIBaA wupuHy kopa6na 80)
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed # JIsuraem kopa6nb snpaso (ysennuneaem X)

# meTog “Bbictpen” (co3gaem nyn B TOM MecTe, rge cejuac HaxonwMTCH urpoK)
    def fire(self):
    # Co3naeM nynW: no UeHTpy Hauero Kopa6nA, Ha ypoBHe ero Bepxywku. CKOpocTb oTpwuaTenbHan，JuTo6bl neTenaBBepXx.
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet) # Jo6asnaem nynw Be o6uy rpynny nynmb

    # Knacc Bpara (HO), Toxe 6epeT ceolictea wa GameSprite
class Enemy(GameSprite):
# 中BWKeHwe Bpara
    def update(self):
        self.rect.y += self.speed # Bpar nanaeT BHu3 (ysenuuneaem Y Ha ero ckopocTb)
        global lost # YkasbiBaem, uTO 6ynew U3MeHAT rno6anbHy nepemenHyw lost (nponyweHHbIe)
# Mcde3aaeT，ecnm
        if self.rect.y > win_height:
            self.rect.x = randint(80,win_height - 80)
            self.rect.y = 0
            lost = lost + 1


# knacc nyan
class Bullet(GameSprite):
# gpwxeHne nynn
    def update(self):
        self.rect.y += self.speed # nlyna netut (Y meHAeTCA B 3aBMCHMOCTH OT CKOpocTH, y Hac OHa MnHycoBanyBHa4uNT neTHT Beepx)
# cueszaeT, ecnn yneTuT 3a BepxHuif Kpali akpana
        if self.rect.y < 0:
            self.kill() # ynanneM nymio wa mrpel，uTo6bl He TpaTHTb pecypcbl KoMNbIoTepa

# Co3anaeM OKouKo urpbl

win_width = 700 # 3aqaem wupuyy oKHa

win_height = 500 # 3agaem BblcoTy oKHa

display.set_caption("Shooter") # Muuem Ha3BaHve urptl B 3aronoBKe OKHa

window = display.set_mode((win_width, win_height)) # Camo coanaHwe okHa c 3afaHHbimMn pasmepamn

background = transform.scale(image.load(img_back), (win_width, win_height)) # 3arpyxaem oH W pactarneaem ero HaBeck 3akpaH

# co3gaem rnaBHoro repoa
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10) # Kaptuyka, X, Y, wupua, BbicoTa, CkKOpocTb

# co3naHwe rpynnbl BparoB

monsters = sprite.Group() # Co3gqaem cneunanbHy rpynny ana MOHcTpoB

for i in range(1, 6): # Unkn nostoputca 5 paa (coanaem 5 Bparos)
# Co3gaem MoHcTpa co cnyuaiihoi no3uumel X cBepxy akpaka co cayuaitHol ckopocTbh
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster) # ho6aenneM mouctpa B rpynny

# co3gaHve rpynnbl acTepownoB (npenatcteui)

asteroids = sprite.Group() # Co3gaem rpynny ana actepongos

for i in range(1, 3): # CoanaewM 2 acTepowna
# Co3maem acTepown co cnydaiihoii no3awuwei X u cnyyaiHo cKOpocTbW
    asteroid = Enemy(img_ast, randint(30, win_width - 30), -40, 80, 50, randint(1, 7))
    asteroids.add(asteroid) # Jo6asnaem acTepown B rpynny

    bullets = sprite.Group() # Co3qaem nyctyw rpynny ana nynb, cima onM 6ynyT no6aBnnTPCH npw cTpenb6e

# nepemenHaa “urpa 3akoHdunacb"

finish = False # Moxa False - urpa wget. Ecnm cTaHeT True - ocTavasnueaem pBmKeHna
# OCHOBHOM UMKN Mrpbl:

run = True # 3Ta nepeMeHHah nepxwT OKHO OTKpbITBIM

rel_time = False # Onar: nepe3apaxaemca Mbl celiuac wan HeT
num_fire = 0 # CueTuuk BblcTpenoe (ckonbko nynb BbinycTunu nonpan)

# 3anyckaem rnaBHblf 6eckoHeuHaii unkn wrpul
while run:

# nepeOupaem sce co6siTHA, KOTOpsIe npowcxonnT B oKHe (HaxaTMA KNABMUL, KAMKM MBUIKM)
    for e in event.get():
    # Co6uTue HaxaTuh Ha KpecTHK (3akpbrue okHa)
        if e.type == QUIT:
            run = False # Beixoqum Ma Unkna，Wrpa 3akpoeTca
    # coOsitue HaxkaTMA Ha KHonky KnaBuaTypbl
        elif e.type == KEYDOWN:
            if e.key == K_SPACE: # Ecnw Haxann MPOBEN
    # npoBepheM，JTO MbI BbICTpenunu MeHbue 5 pa3 M ceiiuac He WMneT nepe3apHhnka
                if num_fire < 5 and rel_time == False:
                    num_fire = num_fire + 1 # Yeenuuneaem cueTunK BucTpenoe
                    fire_sound.play() # Urpaem 3ByK BucTpena
                    ship.fire() # BblsbeaeM MeTon cTpenb6b y Kopa6na (cosnaeM nyno)

# ecnu Cnenanm 5 BblcTpenoB nu nepe3aphnka ele He Hadanacb

                if num_fire >= 5 and rel_time == False :
                    last_time = timer() # 3anommHaem TouHoe Bpema Hadana nepe3apankn
                    rel_time = True # BkniouaeM pexum nepesapankn (cTpennTb Henb3A)

# ecm urpa He oKoHYeHa (HMKTO He Bbwrpan HM He npourpan)
    if not finish:

# pucyem 中oH HaunHan c neBoro BepxHero yrna (0, 0)
        window.blit(background, (0,0))

        # gaem komaHay BCeM O6beKTaM npocdwTaTbP CBOM HoBble KOOPAMHaTbI
        ship.update() # newuraeM kopa6nb，ecnmm HaxaTb KHONKK
        monsters.update() # newraem Bcex MOHCTpoB BHy3
        asteroids.update() # nenraeM Bce acTepownbl BHU3
        bullets.update() # fjsuraem sce nynm BBepx

        # pucyem o6bekTb B HX HoBblx KOOpANHaTaX

        ship.reset() # Pucyem Kopa6nb

        monsters.draw(window) # Pucyem Bcex MOHCTpoB wa rpynna Ha okhe
        asteroids.draw(window) # Pucyem Bce acTepownbl ma rpynne
        bullets.draw(window) # Pucyem Bce nynm wa rpynnel

    # noruKa nepezapaaku
        if rel_time == True: # Ecan Bknodeh pexnm nepezapagkn
            now_time = timer() # Y3Haem, Kakoe epema ceiuac

            if now_time - last_time < 3: # Ecnw c Hadana nepesapaaKu npouno MEHbUE 3 ceKyHa


                reload = font2.render('Wait, reload...', 1, (150, 0, 0)) # Coagaem TekcT “nonoxknTe，nepe3apRnka”
                window.blit(reload, (260, 460)) # nioka3blBaeM 3TOT TeKkCT BHW3ay 3kpaha
            else: # Ecnw 3 cekyHnbl yxe npouno
                num_fire = 0  # C6pacbleaeM cueTunk nynb Ha 8 (o6olima nonha)
                rel_time = False # BblknmouaeM pexnm nepesapagku (MOxXHO CHOBa cTpennTb)

            # npoBepka cTonKHoBeHMit nynb c MoHcTpaMw
            # (True, True oshauaeT，uTo npw KacaHww ymanuTcA W MOHCTp, Mw nyna)
                collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
        # 3TOT KOM cpa6aTblBaeT ANA Kaxgoro cO6uToro MOHCTpa
            score = score + 1 # Jlaem urpoky 1 ouko
        # Coanaem HoBoro MOHCTpa Ha CaMOM Bepxy，JdTo6b ux Bcerna 6bmo 5 uTyKk
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

    # (3akommentuposanult cTapbii KyCoK Kona, KOTOpEIli paHbue oTeedan 3a MrHOBeHHE npour ps)
    if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False) or lost >= max_lost:
        finish = True # npourpanu, cTaBum don u 6onbHe He ynpaennew cnpaiitamn.
        window.blit(lose, (200, 200))

    # nposepaem, spezanca mm Haw kopa6nb Bo Bpara wnwm acTepown
    if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False):
    # Ecnm spezanca, ymanaem Toro MoHcTpa (True B KoHUe)
        sprite.spritecollide(ship, monsters, True)
    # Yoanaem TOT acTepoua, B KOTOpbIA BpeZanucb
        sprite.spritecollide(ship, asteroids, True)
        life = life -1 # OTHwmaem onHy xn3Hb y Hauero Kopa6na

    # nposepaem ycnogna MPOMFPBILIA

    if life == 0 or lost >= max_lost: # Ecaw 3akoHumnucb xu3HH WI nponycTwunw cnmukow mhoro
        finish = True # OcTahaenmeaeM urpy (3anpeuaeM newnraTbcH)
        window.blit(lose, (200, 200)) # Pucyem Hannwmcb YOU LOSE no ueHTpy

    # nposepaem ycnoewe BBIMTPBILIA
    if score >= goal: # Ecnw Ha6pann HyxHbie ouKn (20)
        finish = True # OcTaHasnueaem urpy
        window.blit(win, (200, 200)) # Pucyem Hagnucb YOU WIN no ueHTpy

    # nonroToBKa TekcTa Ana cueTa Ha 3kpaHe
    text = font2.render("Cuet: "+ str(score), 1, (255, 255, 255))
    window.blit(text, (10, 20)) # Pucyem cueT B neBoM BepxHem yray

    # nonroToBKa TekcTa ANA nponyuleHHbix Kopabned Ha SKpaHe
    text_lose = font2.render("Mponyuevo: " + str(lost), 1, (255, 255, 255))
    window.blit(text_lose, (10, 50)) # Pucyem konmuecTBO nponyueHhHblx non cqeToM

    # MeHheM UBeT CdeTJWKa xN3HeEM B 3aBMCMMOCTM OT UX OCTaTKa

    if life == 3:
        life_color = (0, 150, 0) # 3enenbii ueeT (Bece oTnmuho)
    if life == 2:
        life_color = (150, 150, 0) # Kents ueeT (ocTopoxHo)
    if life == 1:
        life_color = (150, 0, 0) # Kpachaii uset (octanca onmh uahc)

    # BeiBogum Upy x“3HeEA B NpaBoM BepxHeM yrAy HYXHbIM UBeTOM
        text_life = font2.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))

        display.update() # O6HoBnaem akpah，uTo6b nokaaaTb BCe, YTO Mbl HapHcoBann

    # 6oHyc: aBTOMaTHUeCKMA nepeaanyck Mrpau，ecnw Mbl Npourpann wnw Bbwmrpanm (finish == True)
    else:
        finish = False # CHoBa paspeuaeM urpe pa6oTaTb
        score = 0 # O6nynaem cueT
        lost = 0 # O6nynaem nponyweHHex
        num_fire = 0 # 06HynneM cueTUnk BblcTpenoB
        life = 3 # BoccTaHapnueaem xn3HM
    # Ounujaem Bce nynm c 3akpaHa
    for b in bullets:
        b.kill()
    # Ounujaem BCex cTapblx MoHcTpoB
    for m in monsters:
        m.kill()
    # Ounujaem Bce cTapble acTepownbl
    for a in asteroids:
        a.kill()

    time.delay(3000) # Xnem 3 cekyHab (3000 MummmcekyHhna)，JdTo6b wmrpok ycnen npounTaTe Hannwcb
    no6eppl/nopaxeHua

    # 3aHoBo co3qaem 5 Bparoe

    for i in range(1, 6):
        monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
        monsters.add(monster)

    # 3aHoBo co3naeM 2 acTepouna

    for i in range(1, 3):
        asteroid = Enemy(img_ast, randint(30, win_width - 30), -40, 80, 50, randint(1, 7))
        asteroids.add(asteroid)

    time.delay(50) # RenaeM ManeHbky naysy (50 munnncekyHa), UTObs urpa He una CAMWKOM 6bcTpo M He neperpyxanaKomnbwTep
