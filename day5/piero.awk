#!/usr/bin/env awk -f
BEGIN{id_max=0}
{
    n=split($1,code,"");l_min=0;l_max=127;for(i=1;i<=7;i++){c=l_min+int((l_max-l_min)/2);if(code[i]=="B"){l_min=c+1}else{l_max=c}}; r_min=0;r_max=7;for(i=8;i<=n;i++){s=r_min+int((r_max-r_min)/2);if(code[i]=="R"){r_min=s+1}else{r_max=s}}; id_tmp=l_max*8+r_max; if(id_tmp>id_max){id_max=id_tmp}
}
END{print "Max ID is:",id_max}
