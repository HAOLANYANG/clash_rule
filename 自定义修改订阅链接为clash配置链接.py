def translate(sub: str) -> str:
    sub_tmp = sub
    sub_tmp = sub_tmp.replace(":", "%3A").replace("/", "%2F").replace("?", "%3F").replace("=", "%3D")
    options = [
        "1 dler.io (推荐稳定)",
        "2 品云 (稳定)",
        "3 边缘 (稳定)",
        "4 xeton.dev (稳定)",
        "5 猫熊 (稳定)"
    ]
    options_str = "\n".join(options)  #使用join函数 设置指定元素为\n换行符，将列表连接起来


    print(f"请选择订阅转换托管API：(输入数字选择1-5)\n{options_str}")



    while True:
        choice = input("请选择订阅转换托管API：(输入数字选择1-5)\n")
        if not choice.isdigit():
            print("请输入一个数字")
        elif not (1 <= int(choice) <= 5):
            print("请输入一个1-5的数字")
        else:
            break

    choice = int(choice)



    api_option = {
        1:"https://api.dler.io/sub?target=clash&url=",
        2:"https://sub.id9.cc/sub?target=clash&url=",
        3:"https://pub-api-1.bianyuan.xyz/sub?target=clash&url=",
        4:"https://sub.xeton.dev/sub?target=clash&url=",
        5:"https://sub.maoxiongnet.com/sub?target=clash&url="
    }

    config_options = "&insert=false&config=peizhiwenjian&emoji=true&list=false&udp=true&tfo=true&scv=false&fdn=false&sort=false"


    sub = api_option[choice] + sub_tmp + config_options

    print(sub)
    return sub



def pzwj(sub : str) -> str:
    options = [
        "1.HOLAND 私人定制 beta版 (与github同步) (推荐)",
        "2.HOLAND 私人定制 stable版 (与github同步) (推荐)",
        "3.ACL4SSR_Online_Mini 精简版(与Github同步)",
        "4.ACL4SSR_Online 默认版 分组比较全(与Github同步)",
        "5.ACL4SSR_Online_Full 全分组 重度用户使用(与Github同步)",
        "6.ACL4SSR_Online_Full_MultiMode.ini 全分组 多模式 重度用户使用(与Github同步)",
        "7.ACL4SSR 本地 默认版 分组比较全"
    ]

    options_str = "\n".join(options)

    print(f"请选择远程配置规则:(请输入数字1-7)\n{options_str}")


    while True:
        choice = input("请选择远程配置（输入数字1-7）：")
        if not choice.isdigit():
            print("请输入一个数字")
        elif not (1 <= int(choice) <= 7):
            print("请输入一个1-7的数字")
        else:
            break

    choice = int(choice)

    pzwj_option = {
        1:"https://raw.githubusercontent.com/HAOLANYANG/clash_rule/main/HOLAND_rule_beta.ini",
        2:"https://raw.githubusercontent.com/HAOLANYANG/clash_rule/main/HOLAND_rule_stable.ini",
        3:"https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini.ini",
        4:"https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online.ini",
        5:"https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Full.ini",
        6:"https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini.ini",
        7:"https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR.ini"
    }


    sub = sub.replace("peizhiwenjian",pzwj_option[choice])


    print(sub)
    return sub



print("该脚本的作用是将订阅链接转化为clash可用的url链接")
sub = translate(sub = input("请输入你的订阅链接："))
sub = pzwj(sub)
