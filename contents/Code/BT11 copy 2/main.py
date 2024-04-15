# 
#! Máy  Tìm dấu cách trong một xâu
dau_vao = "▷aaaa⊔aaa"
vi_tri = 2
bat_dau = "q0"
ket_thuc = "h"


danh_sach_bang_luat = map(tuple,
                [
("q0", "a",  "q0","left" ),
("q0", "⊔",  "q0","left" ),
("q0", "▷",  "q1","right" ),



("q1", "a",  "q1","right" ),
("q1", "⊔",  "h","⊔" ),
("q1", "▷",  "q1","right" ),



 







 



                ]
                )
# ========================== 
bang_chuyen = list(dau_vao)
trang_thai = bat_dau
#
#
#
bang_luat = dict(((trang_thai_hien_tai, ki_tu_hien_tai), ( trang_thai_moi,ki_tu_moi)) for (trang_thai_hien_tai, ki_tu_hien_tai, trang_thai_moi, ki_tu_moi) in danh_sach_bang_luat)

from colorama import Fore,init
init(autoreset=True)

while True:
    print("⊢M", '\t', end=" ")
    print("(", '\t', end=" ")
    print(trang_thai, '\t', end=" ")
    print(",", '\t', end=" ")
    for i, v in enumerate(bang_chuyen):
        if i == vi_tri:
            print(Fore.RED + "%s" % (v,), end=" ")
        else:
            print(v, end=" ")
    print()

 



    if trang_thai == ket_thuc: break


    if (trang_thai, bang_chuyen[vi_tri]) not in bang_luat: break
    
    (  trang_thai_moi,ki_tu_moi) = bang_luat [(trang_thai, bang_chuyen[vi_tri])]

    if ki_tu_moi  == 'left':
        if vi_tri > 0: vi_tri -= 1
        else: bang_chuyen.insert(0, "⊔")
    elif ki_tu_moi == 'right':
        vi_tri += 1
        if vi_tri >= len(bang_chuyen): bang_chuyen.append("⊔")
    else:
        bang_chuyen[vi_tri]=ki_tu_moi 
    trang_thai = trang_thai_moi
    