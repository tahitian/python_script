import re

r = '__IDFA__'
s = 'http://v.admaster.com.cn/i/a114801,b2891188,c3861,i0,m202,8a2,8b1,0a__OS__,0c__IMEI__,0d__AndroidID__,0e__DUID__,n__MAC__,o__IDFA__,z__IDFA__,f__IP__,t__TS__,r__TERM__,l__LBS__,h'
result = re.sub(r, 'AAAA', s)
print(result)