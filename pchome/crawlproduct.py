# -*- coding: utf-8 -*-
import requests
import re, json
res = requests.get('http://24h.pchome.com.tw/prod/DGAZ5T-19005EITY')
res2 = requests.get('http://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/DGAZ5T-19005EITY-000&fields=Seq,Id,Name,Nick,Store,PreOrdDate,SpeOrdDate,Price,Discount,Pic,Weight,ISBN,Qty,Bonus,isBig,isSpec,isCombine,isDiy,isRecyclable,isCarrier,isMedical,isBigCart,isSnapUp,isDescAndIntroSync&_callback=jsonp_prod?_callback=jsonp_prod')
res2 = requests.get('http://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/DGAZ5T-19005EITY-000&fields=Price&_callback=jsonp_prod?_callback=jsonp_prod')
print res2.text.encode('utf-8')
m = re.match('.*jsonp_prod\((.*?)\);.*', res2.text.encode('utf-8'))
print json.loads(m.group(1)).values()[0]['Price']['P']