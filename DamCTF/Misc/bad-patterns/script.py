#!/usr/bin python3

def decode_bad_pattern(s):
    string_size = len(s)
    res = ""
    for i in range(0, string_size, 5):
        res += chr(ord(s[i]) - 0)
        res += chr(ord(s[i+1]) - 1)
        res += chr(ord(s[i+2]) - 2)
        res += chr(ord(s[i+3]) - 3)
        res += chr(ord(s[i+4]) - 4)
    return res


def encode_bad_pattern(s):
    string_size = len(s)
    res = ""
    for i in range(0, string_size, 5):
        res += chr(ord(s[i]) + 0)
        res += chr(ord(s[i+1]) + 1)
        res += chr(ord(s[i+2]) + 2)
        res += chr(ord(s[i+3]) + 3)
        res += chr(ord(s[i+4]) + 4)
    return res

print(encode_bad_pattern("bagelarenotwholewheatsometimes"))

#flag: dam{bbihpasgqstxjrpexjhettqpitjohw}


print(decode_bad_pattern("Lpthq jrvym!frpos\"vmt!cpit-\"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu\"oebpth$eu\"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp\"oebptlw okvm vv#eljsxmp!g{$eb\"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf\"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo\"svojfhrt-\"vynu\"lr dwota!sxm phimcjc#hetguynu\"pslmkw$aokp$ie\"hwt!ndfoswp2"))
