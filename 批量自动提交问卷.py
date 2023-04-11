# from concurrent.futures import ThreadPoolExecutor
# from ssl import Options
#
# from selenium import webdriver
import random  # 用于产生随机数
import time  # 用于延时
from selenium.webdriver.common.by import By      #导入By包进行元素定位
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# selenium基本配置

#实例化一个启动参数对象
chrome_options = Options()
#添加启动参数
chrome_options.add_argument(
    'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"')  # 添加请求头
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# 防止被识别
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])     #设置开发者模式启动


# chrome_options.add_experimental_option('useAutomationExtension', False)    # 关闭selenium对chrome driver的自动控制
#chrome_options.maximize_window()      # 网页最大化
#chrome_options.add_argument('headless')    #设置浏览器以无界面方式运行

browser = webdriver.Chrome(options=chrome_options)     #设置驱动程序，启动浏览器  （实现以特定参数启动）
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})       #用来执行Chrome开发这个工具命令


def run():          # 定义方法
    browser.get('https://www.wjx.cn/vm/tudzFW9.aspx')        # 获取问卷信息

    # 问题1的点击 （性别）
    randomId = random.randint(1, 2)       # 随机数 随机点击按钮
    #js实现方式
    js = "document.getElementById(\"q1_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)         #使用js实现点击的效果（调用js方法，同时执行javascript脚本）
    js = "document.getElementById(\"q1_" + str(randomId) + "\").click()"
    browser.execute_script(js)         #使用js实现点击的效果（调用js方法，同时执行javascript脚本）
    # 延时 太快会被检测是脚本
    time.sleep(0.1)

    # 问题2    （年龄）
    randomId = random.randint(2, 4)   # 随机数，5个多选框 随机点击
    # 两种js实现方式
    js = "document.getElementById(\"q2_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q2_" + str(randomId) + "\").click()"    # 拼接字符串的方式 js找到对应id 点击按钮
    browser.execute_script(js)
    # 延时
    time.sleep(0.1)

    # 问题3      （职业）
    randomId = random.randint(1, 1)  # 随机数
    # 两种js实现方式
    js = "document.getElementById(\"q3_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q3_" + str(randomId) + "\").click()"    # 拼接字符串的方式 js找到对应id 点击按钮
    browser.execute_script(js)
    # 延时
    time.sleep(0.1)

    # 问题4    （类型）
    randomId = random.randint(1, 1)  # 随机数
    # 两种js实现方式
    js = "document.getElementById(\"q4_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q4_" + str(randomId) + "\").click()"    # 拼接字符串的方式 js找到对应id 点击按钮
    browser.execute_script(js)
    # 延时
    time.sleep(0.1)

    # 问题5     （途径）
    randomId = random.randint(1, 1)  # 随机数（选多少个）
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 6)
        # 两种js实现方式
        js = "document.getElementById(\"q5_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q5_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)

    # 问题6   （是否支持）
    randomId = random.randint(1, 2)  # 随机数 随机点击按钮
    # 两种js实现方式
    js = "document.getElementById(\"q6_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q6_" + str(randomId) + "\").click()"    # 使用js实现点击的效果
    browser.execute_script(js)
    # 延时 太快会被检测是脚本
    time.sleep(0.1)

    # 问题7    （是否加入其他）
    randomId = random.randint(1, 2)  # 随机数 随机点击按钮
    # 两种js实现方式
    js = "document.getElementById(\"q7_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q7_" + str(randomId) + "\").click()"    # 使用js实现点击的效果
    browser.execute_script(js)
    # 延时 太快会被检测是脚本
    time.sleep(0.1)


    # 问题8    （负责的工作）
    randomId = random.randint(1, 5)  #
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 5)
        # 两种js实现方式
        js = "document.getElementById(\"q8_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q8_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)

    # 问题9   （时长）
    randomId = random.randint(1, 4)
    # 两种js实现方式
    js = "document.getElementById(\"q9_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q9_" + str(randomId) + "\").click()"
    browser.execute_script(js)
    time.sleep(0.1)

    # 问题10        （宣传工作）
    randomId = random.randint(1, 2)  #
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 4)
        # 两种js实现方式
        js = "document.getElementById(\"q10_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q10_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)


    # 问题11   （主要问题）
    randomId = random.randint(1, 3)  #
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 5)
        # 两种js实现方式
        js = "document.getElementById(\"q11_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q11_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)


    # 问题12   （解决方案）
    block = ["多照顾居民情绪", "找负责人沟通", "时刻想着自己是党员","保持心态平衡","上报组织","想办法解决","耐心劝说","耐心","招其他志愿者帮忙","与基层干部商讨","找居委会解决"]  # 随机输入
    randomId = random.randint(0, 10)
    browser.find_element_by_id("q12").send_keys(block[randomId])
    time.sleep(0.1)


    # 问题13   （核酸方式）
    randomId = random.randint(1, 4)  # 单选
    # 两种js实现方式
    js = "document.getElementById(\"q13_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q13_" + str(randomId) + "\").click()"
    browser.execute_script(js)
    time.sleep(0.1)

    # 问题14   （主要因素）
    randomId = random.randint(1, 3)  #
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 4)
        # 两种js实现方式
        js = "document.getElementById(\"q14_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q14_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)

    # 问题15   (力量)
    randomId = random.randint(1, 2)  #
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 5)
        # 两种js实现方式
        js = "document.getElementById(\"q15_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q15_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)

    # 问题16   （作用）
    randomId = random.randint(1, 2)  #
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 4)
        # 两种js实现方式
        js = "document.getElementById(\"q16_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q16_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)

    # 问题17   （组织）
    randomId = random.randint(1, 3)  # 单选
    # 两种js实现方式
    js = "document.getElementById(\"q17_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q17_" + str(randomId) + "\").click()"
    browser.execute_script(js)
    time.sleep(0.1)

    # 问题18   （原因）
    randomId = random.randint(1, 3)  #
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 5)
        # 两种js实现方式
        js = "document.getElementById(\"q18_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q18_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)

    # 问题19   （改进）
    # randomId = random.randint(1, 4)  # 单选
    # js = "document.getElementById(\"q18_" + str(randomId) + "\").click()"
    # browser.execute_script(js)
    # time.sleep(1)
    randomId = random.randint(1, 2)  #
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 4)
        # 两种js实现方式
        js = "document.getElementById(\"q19_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q19_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)

    # 问题20   （优点）
    randomId = random.randint(1, 2)  #
    for i in range(1, randomId + 1):  # 循环 实现多选效果
        randomId1 = random.randint(1, 5)
        # 两种js实现方式
        js = "document.getElementById(\"q20_" + str(randomId1) + "\").checked = true"
        browser.execute_script(js)
        js = "document.getElementById(\"q20_" + str(randomId1) + "\").click()"
        browser.execute_script(js)
        # 延时
    time.sleep(0.1)

    # 问题21   （召集）
    randomId = random.randint(1, 3)  # 单选
    # 两种js实现方式
    js = "document.getElementById(\"q21_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q21_" + str(randomId) + "\").click()"
    browser.execute_script(js)
    time.sleep(0.1)


    # 问题22   （能力）
    randomId = random.randint(1, 4)  # 单选
    # 两种js实现方式
    js = "document.getElementById(\"q22_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q22_" + str(randomId) + "\").click()"
    browser.execute_script(js)
    time.sleep(0.1)


    # 问题23   （是否懈怠）
    randomId = random.randint(2, 3)  # 单选
    # 两种js实现方式
    js = "document.getElementById(\"q23_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q23_" + str(randomId) + "\").click()"
    browser.execute_script(js)
    time.sleep(0.1)

    # 问题24   （打分）
    randomId = random.randint(8, 10)  # 单选
    # 两种js实现方式
    js = "document.getElementById(\"q24_" + str(randomId) + "\").checked = true"
    browser.execute_script(js)
    js = "document.getElementById(\"q24_" + str(randomId) + "\").click()"
    browser.execute_script(js)
    time.sleep(0.1)


    # 问题25
    block = ["多招志愿者","物资供应方面","多与居民做好沟通","沟通","多宣传防疫知识","减少志愿者工作量","无","多发口罩","多和居民沟通","发挥党员作用","增加核酸检测医护人员"]  # 随机输入
    randomId = random.randint(0, 10)
    browser.find_element_by_id("q25").send_keys(block[randomId])
    time.sleep(0.1)


    #submit
    # browser.find_element_by_xpath("//input[@value='提交']").click()
    # time.sleep(0.5)
    # # 模拟点击智能验证按钮
    # # 先点确认
    # browser.find_element_by_xpath("//button[text()='确认']").click()
    # time.sleep(0.5)
    # # 再点智能验证提示框，进行智能验证
    # browser.find_element_by_xpath("//div[@id='captcha']").click()

    #点击提交
    submit = browser.find_element_by_xpath("//*[@id='ctlNext']")
    submit.click()
    time.sleep(0.5)


    # 模拟点击智能验证按钮
    # 先点确认
    browser.find_element(By.XPATH,"//button[text()='确认']").click()
    time.sleep(1)
    # 再点智能验证提示框，进行智能验证
    browser.find_element_by_xpath("//div[@id='captcha']").click()



if __name__ == "__main__":
    # for i in range(10):
    #     run()
    #     time.sleep(5)  # 避免提交过快 会出现验证
    run()




