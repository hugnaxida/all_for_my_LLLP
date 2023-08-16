import sys

import switch
import qingshu
import notification
import photo_out


address = "D:\\OneDrive - 知行汽车科技(苏州)股份有限公司\\Desktop\\程序for_my_LLLP\\photo_story"
address_2="D:\\OneDrive - 知行汽车科技(苏州)股份有限公司\\Desktop\\程序for_my_LLLP\\image"
arg1 = ''#输入的图片的地址
arg2 = ''#输出的图片的地址
arg3 = ''
arg4=''
def main():
    global arg1, arg2, arg3,arg4
    arg1 = "D:\\OneDrive - 知行汽车科技(苏州)股份有限公司\\Desktop\\程序for_my_LLLP\\photo_story"
    arg2 = "D:\\OneDrive - 知行汽车科技(苏州)股份有限公司\\Desktop\\程序for_my_LLLP\\image"
    arg3 = ""
    arg4 = "sys.argv[4]"
    #print(arg1,arg2,arg3,arg4)
    print("~~~~~~~~~~~~~~~~~~~程序开始---------------")
#pyinstaller --onefile main.py
def photo_story(arg1,arg2):
    photo_list = photo_out.get_photo(arg1)
    txt_list = photo_out.get_love(arg1)
    photo_out.output_photo(photo_list,txt_list,arg2)

if __name__ == '__main__':
    main()
    flog1=0
    flog_pass=1
    print("当你打开这个的时候，老生常谈的问题就要来了，请问你在不在想我啊\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True and flog_pass==1:
        user_input = input("请输入A或B：其中A代表在想我，B代表非常的想，要抱抱\n")
        if user_input == 'A' or user_input == 'B':
            switch.doing(user_input)
            notification.show_complete_message("啊啊，我也在想你啊，好想你啊，我滴小宝宝")
            break  # 输入合规，退出循环
        else:
            if flog1==1:
                print("再给你好多次回答问题的机会~\n")
            if flog1 == 3:
                print("故意的还是不小心的？\n")
            if flog1 == 5:
                print("输错五次了，快快快再输错四次有个小惊喜哦~~\n")
            if flog1 == 9:
                print("你已经尝试9次错误了啊喂，不过作为一点点安慰，带你看看你曾经看过的小情书吧：\n")
                print(qingshu.qingshu1)
                print("哈哈哈，我知道你是不好意思说在想我，其实是在想我的对吧，那么我们就进行下一项吧\n")
                flog_pass=0
                break
            flog1+=1
            print("宝宝你这样说话就很不对哦，快点重新说~")
    user_input = input("我亲爱的玲子酱，请输出任意，来欣赏接下来的项目~~~~~~~~~~~~~~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"~~~当前到达的是相册会议集部分:（咳咳，咳咳）容我介绍以下制作这个部分的灵感由来----------一个悠闲地午后（指摸鱼）~~~\n~~~闲来无事的我打开了相册，翻看我们之前的故事，我觉得可以用一种方式把这些故事记录下来，所以我就萌发了这种想法~~~\n~~~所以请你欣赏接下来的html，请在{arg2}下找到my_love_to_liling.html，然后打开它，没错，就是打开它~~~")
    photo_story(arg1, arg2)
    notification.show_complete_message("~请你记住你看完的感谢，一会要考~~~~~")
    str_photo=input("如果你查看完毕，请输入任意值，进入下一个项目")
