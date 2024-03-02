import pygame,time,sys,random
pygame.init()
pygame.display.set_caption("垃圾分类")
sc = pygame.display.set_mode((1280,720))
tb = pygame.image.load(".\\tb.ico").convert_alpha()
pygame.display.set_icon(tb)
shuju = int(open(".\\file\\shuju.txt","r",encoding="utf-8").read())
beijing = pygame.image.load(".\\picture\\beijing.jpg")
chuyulaji = pygame.image.load(".\\picture\\chuyulaji.png")
youhailaji = pygame.image.load(".\\picture\\youhailaji.png")
kehuishoulaji = pygame.image.load(".\\picture\\kehuishoulaji.png")
qitalaji = pygame.image.load(".\\picture\\qitalaji.png")
zuigaodefen = pygame.image.load(".\\picture\\zuigaodefen.png")
kaishiyouxi = pygame.image.load(".\\picture\\kaishiyouxi.png")
chuti = pygame.image.load(".\\picture\\chuti.png")
fhzy = pygame.image.load(".\\picture\\fhzy.png")
dg = pygame.image.load(".\\picture\\dg.png")
cc = pygame.image.load(".\\picture\\cc.png")
zd = pygame.image.load(".\\picture\\zd.jpg")
zhengqui = pygame.mixer.Sound(".\\music\\zhengqui.wav")
cuowu = pygame.mixer.Sound(".\\music\\cuowu.wav")
timu = ["废纸","玻璃","塑料","金属","布料","菜叶","蛋壳","剩饭","果皮","蛋壳","茶渣","骨头","电池","含汞","废药","油漆","砖瓦陶瓷","渣土","卫生间废纸"]
font = pygame.font.Font(".\\msyh.ttc",60)
old_time = int(time.time())
new_time = int(time.time())
fenshu = shuju
jifenqi = 0
you_win = 0
count_down = 5
fruits_num = 0
zhongzhi = True
while zhongzhi:
    sc.blit(beijing,(0,0)) 
    sc.blit(kaishiyouxi,(465,350))
    sc.blit(zuigaodefen,(390,50))
    if fenshu >= 10:
        fenshu_text = font.render("最高记录:"+str(fenshu),True,(255,0,0))
    if fenshu < 10:
        fenshu_text = font.render("最高记录:0"+str(fenshu),True,(255,0,0))
    sc.blit(fenshu_text,(470,85))
    pygame.display.update()
    panduan = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            zhongzhi=False
            pygame.init()
        x,y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
             if 465 < x < 815 and 370 < y < 520:
                while zhongzhi:                  
                    suijixuanti = random.randint(0,18)
                    qeurentimu = timu[suijixuanti]
                    panduan = 0
                    while zhongzhi:
                        time_text = font.render(str(count_down),True,(255,0,0))
                        old_time = new_time
                        new_time = int(time.time())
                        if new_time - old_time == 1:
                            count_down -= 1
                            if count_down < 1:
                                panduan = -1
                        sc.blit(beijing,(0,0))
                        sc.blit(chuti,(0,70))
                        chutit = font.render("该物品是什么垃圾："+str(qeurentimu),True,(255,0,0))
                        sc.blit(chutit,(250,105))
                        sc.blit(youhailaji,(265,400))
                        sc.blit(kehuishoulaji,(465,400))
                        sc.blit(chuyulaji,(665,400))
                        sc.blit(qitalaji,(865,400))
                        sc.blit(time_text,(10,0))
                        jfq = font.render("当前得分："+str(jifenqi),True,(255,0,0))
                        sc.blit(jfq,(450,-5))
                        pygame.display.update()
                        if time_text == 1:
                            panduan = -1
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.display.quit()
                                zhongzhi=False
                                pygame.init()
                            x,y=pygame.mouse.get_pos()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if 265 < x < 415 and 400 < y < 600:
                                    if 12 <= suijixuanti <= 15:
                                        sc.blit(dg,(285,300))    
                                        panduan = 1
                                        jifenqi += 1
                                    else:
                                        panduan = -1
                                        sc.blit(cc,(285,300))
                                if 465 < x < 615 and 400 < y < 600:
                                    if 0<= suijixuanti <=4:
                                        sc.blit(dg,(485,300))
                                        panduan = 1
                                        jifenqi += 1
                                    else:
                                        panduan = -1
                                        sc.blit(cc,(485,300))
                                if 665 < x < 815 and 400 < y < 600:
                                    if 5 <= suijixuanti <= 11:
                                        sc.blit(dg,(685,300))
                                        panduan = 1
                                        jifenqi += 1
                                    else:
                                        panduan = -1
                                        sc.blit(cc,(685,300))
                                if 865 < x < 1015 and 400 < y < 600:
                                    if 16 <= suijixuanti <= 18:
                                        sc.blit(dg,(885,300))
                                        panduan = 1
                                        jifenqi += 1
                                    else:
                                        panduan = -1
                                        sc.blit(cc,(885,300))                           
                        if panduan == -1:                        
                            if 12 <= suijixuanti <= 15:
                                sc.blit(dg,(285,300))                                           
                            if 0<= suijixuanti <=4:
                                sc.blit(dg,(485,300))                                               
                            if 5 <= suijixuanti <= 11:
                                sc.blit(dg,(685,300))                                                                     
                            if 16 <= suijixuanti <= 18:
                                sc.blit(dg,(885,300))                                  
                            sc.blit(chuti,(0,70))
                            sc.blit(zd,(0,0)) 
                            chutit = font.render("本次得分："+str(jifenqi),True,(255,0,0))
                            sc.blit(chutit,(450,105))
                            sc.blit(fhzy,(1100,620))                   
                            pygame.display.update()
                            cuowu.play()
                            while zhongzhi:
                                if jifenqi > shuju:
                                    cx=open(r".\\file\\shuju.txt","w",encoding="utf-8")
                                    cx.write(str(jifenqi))
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.display.quit()
                                        zhongzhi=False
                                        pygame.init()
                                    x,y = pygame.mouse.get_pos()
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if 1100 < x < 1250 and 620 < y < 690:
                                            zhongzhi=False                                                              
                        if panduan == 1:
                            pygame.display.update()     
                            zhengqui.play()
                            count_down=5
                            time.sleep(2)                                                   
                            break        
