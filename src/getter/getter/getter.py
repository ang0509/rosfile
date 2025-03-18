import rclpy 
from rclpy.node import Node 
from std_msgs.msg import UInt32 
class getterNode(Node): 
    def __init__(self,name): 
        super().__init__(name) 
        self.get_logger().info("getterNode初始化成功!") 
        self.getDiceNum=self.create_subscription(UInt32,"chilem",self.getDiceNum_callback,10)
    def getDiceNum_callback(self,diceNum): 
        self.get_logger().info("数字是：%d" % diceNum.data) 
        
       
def main(args=None): 
        rclpy.init(args=args) 
        node=getterNode("getter")
        rclpy.spin(node) 
        rclpy.shutdown() 
     