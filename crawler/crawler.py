# -*- coding: utf-8 -*-  

#  shanghai mail site: http://www.kuaidi100.com/network/net_31_all_all_256.htm

cityname = '上海';
cityid = 31;

pagefrom = 1
pageto = 5

urlformat = "http://www.kuaidi100.com/network/net_%d_all_all_%d.htm"

def formaturl(url_format,cityid,pageno):
  return url_format % (cityid,pageno)

for page in  range(pagefrom,pageto):
  print formaturl(urlformat,cityid,page)
