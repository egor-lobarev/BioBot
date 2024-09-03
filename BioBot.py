# 1 - название аминокислоты; 2 - полярная/неполярная; 3 - молярная масса
data = [["His",1,155.16,"CAU","CAC"],
      ["Gln ",1,146.15,"CAA","CAG"],
      ["Pro ",0,115.13,"CCU","CCC","CCA","CCG"],
      ["Arg ",1,174.2,"CGU","CGC","CGA","CGG","AGA","AGG"],
      ["Leu ",0,131.18,"CUU","CUC","CUA","CUG","UUA","UUG"],
      ["Asp ",1,133.1,"GAU","GAC"],
      ["Glu ",1,147.13,"GAA","GAG"],
      ["Ala ",0,89.09,"GCU","GCC","GCA","GCG"],
      ["Gly ",0,75.07,"GGU","GGC","GGA","GGG"],
      ["Val ",0,117.15,"GUU","GUC","GUA","GUG"],
      ["Tyr ",1,181.19,"UAU","UAC","GCA","GCG"],
      ["Ser ",1,105.09,"UCU","UCC","UCA","UCG","AGU","AGC"],
      ["Cys ",1,121.15,"UGU","UGC"],
      ["Trp ",0,204.23,"UGG"],
      ["Phe ",0,165.19,"UUU","UUC"],
      ["Asn ",1,132.12,"AAC","AAU"],
      ["Lys ",1,146.19,"AAA","AAG"],
      ["Thr ",1,119.12,"ACU","ACC","ACA","ACG"],
      ["Ile ",0,131.18,"AUU","AUC","AUA"]]
print("ДНК вводится строчными или прописными латинскими буквами")
dna=input("Input DNA code ").upper()
def bio(dna):
    dna=dna.upper()
    code=""
    a, aug, stp, M, stat=0, 0, 0, 0, []
    for h in range(len(dna)):
        if dna[h]=="G":
            code+="C"
        elif dna[h]=="A":
            code+="U"
        elif dna[h]=="T":
            code+="A"
        elif dna[h]=="C":
            code+="G"
        else:
            a=1
    #print(code)
    #####check
    if a==1:
        return "Код содержит недопустимые символы"
    if a!=1:
        for ko in range(0,len(code),3):
            st=code[ko:ko+3]
            if st=="AUG":
                aug+=1
            elif st=="UAA" or st=="UAG" or st=="UGA":
                stp+=1
        if aug>stp:
            return "Ошибка: Старт кодонов больше, чем стоп кодонов"
            a=1
        elif aug==0 and stp==0:
            return "Ошибка: В коде нет старт и стоп кодонов"
            a=1
        elif stp==0:
            return "Ошибка: В коде нет стоп кодонов"
            a=1
        elif aug==0:
            return "Ошибка: В коде нет старт кодонов"
            a=1
    #######
    if a!=1:
        #print("RNA code:",code)
        i=0
        while i<len(code):
         amin=""
         temp=""
         while temp!="AUG":
            temp=code[i:i+3]
            i+=1
         amin="Met "
         stat.append(0)
         i=i-1
         while temp!="UAG" and temp!="UAA" and temp!="UGA" and (i<len(code)):
            i=i+3
            temp=code[i:i+3]
            for h in range(19):
                for z in range(len(data[h])):
                     if data[h][z]==temp:
                        amin+=data[h][0]
                        M+=data[h][2]
                        if data[h][1]==1:
                           stat.append(1)
                        else:
                           stat.append(0)
         M-=(len(stat)-1)*18
         pl = str(round((stat.count(1)/len(stat))*100,1))+'%'
         npl = str(round((stat.count(0)/len(stat))*100,1))+'%'
         return "Код РНК: "+code+"\nАминокислота(ы):"+amin+"\nВ белке "+pl+" полярных аминоксилот, и "+npl+" неполярных аминокислот."+"\nМолярная масса белка = "+str(M)+"г/моль"
#print(bio('tacgggcctaatcttatt'.upper()))
print("Аминокислота(ы):");print(amin) 
print("В белке",pl,"полярных аминоксилот, и\n"+str(npl)," неполярных аминокислот.")
print("Молярная масса белка =",M,"г/моль")
#fef=input()
