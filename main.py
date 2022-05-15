# # 这是一个示例 Python 脚本。
#
# # 按 Shift+F10 执行或将其替换为您的代码。
# # 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#
#
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('lmx')
#
# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


x = np.linspace(-110,110,50)
print(type(x))
y1 = x**2
y2 = x
y3 = -y1
y4 = x*8
x0 = 10
y0 = x0*8
# plt.figure()   #开始绘图1，括号内可指定num=2，注明图像名字
# plt.plot(x,y1)

plt.figure(num=11,figsize=(8,5))    #开始绘图1，括号内可指定num=2，注明图像名字


plt.xlim((-110,110)) #x坐标标尺
plt.ylim((-110,110)) #Y坐标标尺
plt.ylabel('This is Y') #Y坐标轴标号
plt.xlabel('This is X')
ticks_X = np.linspace(-110,110,10)
plt.xticks(ticks_X)
plt.yticks([-110,-50,0,50,110],['very bad','bad',r'$normal \beta$','good',r'$very\ \alpha$']) # $内容$，采用流线英文表示，添加r为

#设置坐标轴位置 gca:get current axis

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('axes',0.5))   #outward, axes
ax.spines['left'].set_position(('data',0))

#图例legend
plt.plot(x,y2,label='差') #在图中画线1
plt.plot(x,y1,color="red",linewidth=2.0,linestyle="--",label='良') #在图中画线1
plt.plot(x,y3,color="green",linewidth=2.0,linestyle="--",label='优') #在图中画线1
plt.scatter(x0,y0,s=50,color='b')#输出为单独的点
plt.plot([x0,x0],[y0,0],'k--',lw='2')
plt.plot([x0,0],[y0,y0],'k--',lw='2')
plt.annotate('x*8=%s'%y0,xy=(x0,y0),xycoords='data',xytext=(-30,30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle = '->',connectionstyle='arc3,rad=.2'))


plt.legend(labels=['aaa','bbb'],loc='best')


plt.figure()
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(X,Y)   #FOR COLOR
plt.scatter(X,Y,s=75,c=T,alpha=0.5)

plt.xlim((-1,1))

plt.figure(num=99)

Z = 12
A = np.arange(Z)
B1 = (1-A/float(Z))*np.random.uniform(0.5,1,Z)
B2 = (1-A/float(Z))*np.random.uniform(0.5,1,Z)

plt.bar(A,B1,facecolor='#9999ff',edgecolor='black')

plt.bar(A,-B2,facecolor='#ff9999',edgecolor='black')

for x,y in zip(A,B1):
    plt.text(x+0,y+0.05,'%.2f'%y,ha='center',va='bottom')

for x,y in zip(A,B2):
    plt.text(x+0,-y-0.05,'%.2f'%y,ha='center',va='top')




def f(x,y):
    h = (1-x/2+x**5+y*2)*np.exp(-x**2,-y**2)
    return h

q =256
x = np.linspace(-3,3,q)
y = np.linspace(-3,3,q)
X,Y = np.meshgrid(x,y)



plt.figure(num=77)
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)

L = plt.contour(X,Y,f(X,Y),8,colors='black',wideline=0.5)
print(type(L))
plt.clabel(L,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())

ifg = plt.figure()
ax =Axes3D(ifg)

J = np.arange(-4,4,0.25)
P = np.arange(-4,4,0.25)

J,P = np.meshgrid(J,P)
R = np.sqrt(J**2+P**2)
Z = np.sin(R)

#画3D图
ax.plot_surface(J,P,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
plt.ylabel('This is Y') #Y坐标轴标号
plt.xlabel('This is X')
ax.contourf(J,P,Z,zdir='z',offset=-2,cmap='rainbow')  #等高面，z方向
ax.contour(J,P,Z,zdir='x',offset=-4,cmap='rainbow')   #等高线，x方向
ax.contourf(J,P,Z,zdir='y',offset=-4,cmap='rainbow')   #等高线，x方向
ax.set_zlim(-2,2)











plt.show()













plt.show() #将绘制的图像显示出来



#
# if __name__ == '__main__':
#     print_hi('lmx')