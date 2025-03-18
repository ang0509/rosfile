import rclpy #导入ros的客户端库，必备步骤
from rclpy.node import Node #rclpy.node是ros客户端库自带的Node类，用于创建节点
from std_msgs.msg import UInt32 #ros2的std_msgs数据接口
class getterNode(Node): #采用面向对象(OOP)的方式建立node；定义了一个PlayerNode的类，继承rclpy.node中的Node；
    def __init__(self,name): #定义初始化方法；或者叫构造函数。。(构造函数是个人的理解，源自C++)
        super().__init__(name) #调用父类初始化，需要传入参数name，通常name是实例化的Node的名称，即节点名字；比如本例子中节点名字是 God
        self.get_logger().info("getterNode初始化成功!") #get_logger().info是rclpy.node中的方法；
        #在这里意思是，当这个PlayerNode节点实例化的时候，输出一句日志；
        self.getDiceNum=self.create_subscription(UInt32,"chilem",self.getDiceNum_callback,10)
        #create_subscription是创建订阅者的命令
            #第一个参数是数据类型 
            #第二个是Topic(话题)名字，需要与发布者发布的Topic名称完全一致！！
            #第三个参数是回调函数，函数里面一般写收到消息后需要执行的操作！本例子中，收到消息后，回调getDiceNum_calback函数，将收到的消息显示出来
            #第四个参数是消息队列长度
    def getDiceNum_callback(self,diceNum): #订阅者 收到消息后的回调函数
        self.get_logger().info("数字是：%d" % diceNum.data) #将收到的骰子数值显示出来
        
        #注意diceNum是一个UInt32的类，需要用.data来取到其数值。跟C/C++ uint32用法不一样！
def main(args=None): #main函数，程序执行的主入口
        rclpy.init(args=args) # 初始化客户端库，必备步骤
        node=getterNode("getter") # 新建节点对象，必备步骤；传入player，将playerNode实例化
        rclpy.spin(node) # spin循环节点,保持节点运行，检测是否收到退出指令（Ctrl+C），必备步骤
        rclpy.shutdown() # 关闭客户端库，必备步骤aa