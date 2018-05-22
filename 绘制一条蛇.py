import  turtle
def draw_snake(rad,angle,len,neckrad):#rad表示运行的园的半径，angle表示爬行的弧度值，
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)#表示先前爬行的距离，也等价于turtle.forward函数
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
def main ():
    turtle.setup(1300,800,0,0)#四个参数分别是宽，高，以及左上角的坐标
    pythonsize = 30#此为蛇的宽度
    turtle.pensize(pythonsize)
    turtle.pencolor('blue')
    # turtle.pencolor('#3B9909')#这个是与屏幕的颜色一致的
    turtle.seth(-40)#此为运动方向，角度值，0表示向东，90北，180西，270南，负号表示相反的方向
    draw_snake(40,80,5,pythonsize/2)
main()
#绘制一条蟒蛇,以后的python版本中除了半径，角度还多一个速度
# 所以后续的版本注意输入三个参数
#此例子中def定义了两个函数
#此程序中调用了turtle函数


var a=lambda a:a+ 2;

print a(2);


