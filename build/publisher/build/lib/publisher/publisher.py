import rclpy #导入ros的客户端库，必备步骤
from rclpy.node import Node #rclpy.node是ros客户端库自带的Node类，用于创建节点
import random #导入random库产生随机数，来模拟掷骰子的结果
from std_msgs.msg import UInt32 #插入std_msgs中的UInt32数据类型


class GodNode(Node): #采用面向对象(OOP)的方式建立node；定义了一个GodNode的类，继承rclpy.node中的Node；
    def __init__(self,name): #定义初始化方法；或者叫构造函数。。(构造函数是个人的理解，源自C++)
        super().__init__(name) #调用父类初始化，需要传入参数name，通常name是实例化的Node的名称，即节点名字；比如本例子中节点名字是 God
        self.get_logger().info("初始化成功!") #get_logger().info是rclpy.node中的方法；
        #在这里意思是，当这个GodNode节点实例化的时候，输出一句日志；
        self.diceGame=self.create_publisher(UInt32,"chilem",10)
        self.dice=self.create_publisher(UInt32,"meichi",10)
        #利用create_publisher命令创建一个发布者，话题是：diceGame，发布者，订阅者话题一致才能通信。
            #第一个参数是发布内容的类型，这里发布的是一个骰子数，范围1~6，可以选择 Uint32；
            #注意UInt32不是python自带的数据类型，而是ros2中std_msgs.msg中的数据类型
            #第二个参数是内容发布到的一个Topic的名字，即内容发布到diceGame这个Topic上，
            #第三个参数10是消息队列长度
        timer_period = 2 #2s的定时间隔
        self.timer = self.create_timer(timer_period, self.diceGame_callback) 
        self.timer2 = self.create_timer(timer_period, self.dice_callback)
    def diceGame_callback(self): 
        diceNum=UInt32() 
        diceNum.data=random.randint(1,100) 
        self.diceGame.publish(diceNum)
        self.get_logger().info("成功发布") 
    def dice_callback(self): 
        dice=UInt32() 
        dice.data=random.randint(1,100) 
        self.dice.publish(dice)   
        self.get_logger().info("成功发布!") 
def main(args=None): 
        rclpy.init(args=args)
        node=GodNode("God") 
        rclpy.spin(node) 
        rclpy.shutdown() 