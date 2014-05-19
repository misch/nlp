#!/usr/bin/python
import re
import collections

input_string = "ODQSOCL OW GIU BOEE QRROHOCS QV GIUR KIA QF Q DQCQSLR WIR ICL IW CQFQF EIYQE YIDJUVLR FGFVLDF GIU SLV OCVI GIUR IWWOYL IC VXQV DICPQG DIRCOCS VI WOCP VXL JXICLF ROCSOCS LHLRG YQEELR OF Q POFVRQUSXV YICWUFLP CQFQ BIRMLR QCP LHLRG YQEELR QFFURLF GIU VXQV XOF IR XLR WOEL IR QYYIUCVOCS RLYIRP IR RLFLQRYX JRIKLYV LHLRG ICL IW BXOYX OF DOFFOCS WRID VXL YIDJUVLR FGFVLD OF QAFIEUVLEG HOVQE"

input_list = list(input_string)

count = collections.Counter()
for letter in input_list:
    count[letter] += 1

print(count)

output_list = input_list
output_string = "".join(output_list)
print(input_string)
print(output_string)


