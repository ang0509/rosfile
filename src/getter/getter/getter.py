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

int main() {
    int num1, num2;
    
    
    std::cout << "请输入两个整数：" << std::endl;
    std::cin >> num1 >> num2;
    
    // 计算并输出结果
    std::cout << "数字 " << num1 << " 和 " << num2 << " 的和为：" << num1 + num2 << std::endl;
    std::cout << "数字 " << num1 << " 和 " << num2 << " 的差为：" << num1 - num2 << std::endl;
    std::cout << "数字 " << num1 << " 和 " << num2 << " 的乘积为：" << num1 * num2 << std::endl;
    
    // 判断除数是否为0，避免除以0的错误
    if (num2 != 0) {
        std::cout << "数字 " << num1 << " 除以 " << num2 << " 的商为：" << num1 / num2 << std::endl;
    } else {
        std::cout << "除数不能为0！" << std::endl;
    }
    
    return 0;
}