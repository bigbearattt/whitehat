I happen to get this text, but it seems to be encrypted. Decrypt it and find the hidden flag.
"HJXAJY GPHTPR HPL P CPBDG APGTCTV SCP CPXRXIXADE DWL LTGWIGTKD TWI CPBDG RXAQJETG SCP STWHXAQPIHT TWI TAJG UD TWI HGDGTEBT. GPHTPR STHJ TWI HBTAQDGE SCP HEXWHSGPW UD TWI SDXGTE DI TIPTGR HXW CLD TBTGEJH APRXIXADE SCP NGPIXAXB GTLDE. VPAU HX TWI GPTN IPWI GPHPTR HPL CGDQ. CPBDG GDGTEBT HJXAJY GPHTPR HX STSGPVTG HP TCD UD TWI IHDB AJUGTLDE SCP AJUHHTRRJH HGTSPTA CX TWI NGDIHXW UD TWI SAGDL. HXW TUXA SCP HXW ICTADXK WIPTS TKPW CTTQ NATSXL STIPGQTATR CX TGJIPGTIXA SCP BAXU."

- Nhận xét:
+ Có 1 ciphertext, khá dài -> mã hóa 1 bảng thế.
- Sử dụng tool http://quipqiup.com/ -> ta thấy hiện lên 1 số từ như 'and', 'was', ... Có vẻ như hướng này là đúng.
- Ta sẽ phân tích bằng tay. Sử dụng 1 số trang phân tích frequency như http://www.counton.org/explorer/codebreaking/frequency-analysis.php
+ Chữ 'T' tiwr lệ lớn nhất với 11.2% ==> 'T' = 'e'
+ Ctrl+H với 'T' -> thấy có nhiều cụm 'TWI' ==> 'TWI' = 'the'. Có vể như các từ đang bị đảo ngược lại. 

cipher = "HJXAJY GPHTPR HPL P CPBDG APGTCTV SCP CPXRXIXADE DWL LTGWIGTKD TWI CPBDG RXAQJETG SCP STWHXAQPIHT TWI TAJG UD TWI HGDGTEBT. GPHTPR STHJ TWI HBTAQDGE SCP HEXWHSGPW UD TWI SDXGTE DI TIPTGR HXW CLD TBTGEJH APRXIXADE SCP NGPIXAXB GTLDE. VPAU HX TWI GPTN IPWI GPHPTR HPL CGDQ. CPBDG GDGTEBT HJXAJY GPHTPR HX STSGPVTG HP TCD UD TWI IHDB AJUGTLDE SCP AJUHHTRRJH HGTSPTA CX TWI NGDIHXW UD TWI SAGDL. HXW TUXA SCP HXW ICTADXK WIPTS TKPW CTTQ NATSXL STIPGQTATR CX TGJIPGTIXA SCP BAXU."
cipher = cipher.lower() #Nên để cipher dạng chữ thường cho dễ nhìn, khi thay thế bằng chữ hoa sẽ nổi bật hơn, vd "t" -> "E"
# print cipher 
list = cipher.split()  #Chia đoạn text thành các từ, list là danh sách các từ
print list 
reverse = '' #Xâu chứa các word đã bị đảo
for i in list:
	if i[-1] == '.': #Với các từ hết câu, ta chỉnh sao cho đảo ngược với dấu chấm ở cuối
		i = i[::-1] 
		reverse += i[1:] + ". "
	else: 
		reverse += i[::-1] + " "
print reverse

- Ta có reverse = "yjaxjh rpthpg lph p gdbpc vtctgpa pcs edaxixrxpc lwd dktgiwgtl iwt gdbpc gtejqaxr pcs thipqaxhwts iwt gjat du iwt tbetgdgh. rpthpg jhts iwt egdqatbh pcs wpgshwxeh du iwt etgxds id rgtpit wxh dlc hjegtbt edaxixrpa pcs bxaxipgn edltg. uapv xh iwt ntpg iwpi rtphpg lph qdgc. gdbpc tbetgdg yjaxjh rpthpg xh gtvpgsts ph dct du iwt bdhi edltguja pcs hjrrthhuja atpstgh xc iwt wxhidgn du iwt ldgas. wxh axut pcs wxh kxdatci stpiw wpkt qttc lxstan rtatqgpits xc axitgpijgt pcs uxab."
- Ném vào http://quipqiup.com/, chọn chế độ satistics, có ngay đoạn văn sau:
"ulius caesar was a roman general and politician who overthrew the roman republic and established the rule of the emperors. 
caesar used the problems and hardships of the period to create his own supreme political and military power. 
flag is the year that ceasar was born. roman emperor julius caesar is regarded as one of the most powerful and successful 
leaders in the history of the world. his life and his violent death have been widely celebrated in literature and film."

- Vậy flag là năm sinh của Caesar, là năm 100 TCN (100 BC). Thử lần lượt cuối cùng flag là 100
WhiteHat{310b86e0b62b828562fc91c7be5380a992b2786a}
