import rclpy 
from rclpy.node import Node 
import random 
from std_msgs.msg import UInt32


class GodNode(Node): 
    def __init__(self,name): 
        super().__init__(name) 
        self.get_logger().info("初始化成功!") 
       
        self.diceGame=self.create_publisher(UInt32,"chilem",10)
        self.dice=self.create_publisher(UInt32,"meichi",10)
        timer_period = 2 
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