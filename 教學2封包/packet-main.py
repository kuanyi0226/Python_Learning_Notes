#主程式
import geometry.point #引入封包名.模組名
result=geometry.point.distance(3,4) #使用封包名.模組名.函式名
print("距離",result)

import geometry.line
result=geometry.line.slope(1,2,3,4)
print("斜率",result)

import geometry.line as line #把geometry.line別名成line
result=line.slope(1,2,3,4) #後面只能用別名，否則會出錯
