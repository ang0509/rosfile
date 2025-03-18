import rclpy 
from rclpy.node import Node 
from std_msgs.msg import UInt32 
class PlayerNode(Node): 
    def __init__(self,name): 
        super().__init__(name)
        self.get_logger().info("PlayerNode初始化成功!") 
        self.getDiceNum=self.create_subscription(UInt32,"meichi",self.getDice_callback,10)
    def getDice_callback(self,dice): 
        self.get_logger().info("数字是：%d" % dice.data) 
        
def main(args=None):
        rclpy.init(args=args) 
        node=PlayerNode("player") 
        rclpy.spin(node) 
        rclpy.shutdown() 