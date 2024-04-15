import requests
import time

# from bs4 import BeautifulSoup

headers = {
    'Cookie': '_lxsdk_cuid=18c82021149c8-0240fa2c885894-4c657b58-1fa400-18c82021149c8; _lxsdk=18c82021149c8-0240fa2c885894-4c657b58-1fa400-18c82021149c8; _hc.v=9cb82820-0c75-830f-2116-edcc971ecb30.1702988223; WEBDFPID=7601303uwzy05w761u7vy7uyx1wvwyw681x179782w697958uz5ww8vx-2018348225069-1702988222124SKAEOYUfd79fef3d01d5e9aadc18ccd4d0c95073796; fspop=test; s_ViewType=10; qruuid=9e138a3e-c24e-407a-be13-d2457088a065; dper=7889ad538b3ba4548e75e058199f8927359dfb18123b308ae5003f061d1692858658c4823c1f89e4c6b2ae49dc730bc8dfa8cf3bf0f8a4ce93bdc0b1fe6d7383; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1702988532,1703248547; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1703248561; _lxsdk_s=18c9185241c-efa-c4d-892%7C%7C48',
    'Host': 'www.dianping.com',
    'Referer': 'https://account.dianping.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}

res = requests.get(
    """https://www.dianping.com/ajax/json/shopDynamic/allReview?shopId=H7ItoOm0xHuvGTkO&cityId=23&shopType=10&tcv=qo767wnn8n&_token=eJx1T01vgkAQ%2FS977QZ2YZevpAdarUILtrJFo%2FGAqEBWPsoCapv%2B966JPfTQZJL33sy8l5kv0Ho74GCEEMEQDPsWOAArSDEABJ2QExPpGrEp0ShFEKR%2FejpG0rRt4xFw1pZNoUm0zbUxl3qNqW5AyyAbeKPY2ECNyLrueHIF5F3XCEdVT6eTsiuSqimqTEnrUhV53ahT0%2BvqWYnO036YMD6TJ%2F1ryJOC172a5hgBGV8yGS%2BR3zC5YferA%2FmnzBNFVkm2988sEkR8HOaBYO%2BXWIgh4rwThR5G6BherPMLi8ftp8gGN2hIOe0X9HWoJsc5OfoJzTVmZlY8es66aPuGQuw1L6kesOLS2uMqZHwZLXz%2FsHrqk21JyyW9i1f0kT%2B4bss8270H3z%2B9h3Vg&uuid=813aab66-9351-8660-8ebd-accfc559dc32.1702906167&platform=1&partner=150&optimusCode=10&originUrl=https%3A%2F%2Fwww.dianping.com%2Fshop%2FH7ItoOm0xHuvGTkO&yodaReady=h5&csecplatform=4&csecversion=2.3.1&mtgsig=%7B%22a1%22%3A%221.1%22%2C%22a2%22%3A1703249543104%2C%22a3%22%3A%22wv79u886w9u55uvv18z585949u42xu0181x2w8v59yx979581x5u79xw%22%2C%22a5%22%3A%22PGpcCNjzd7YkhYLuRRpe6I%3D%3D%22%2C%22a6%22%3A%22hs1.4aOG4x69iuIGtADfqn9IKcSwYFNB1T7M66QyjStcoD30O0oguxB5oGft4samHCb3kAASyUhsdJtKb1H3NBHHkhg%3D%3D%22%2C%22x0%22%3A4%2C%22d1%22%3A%22cffc779bc4ddce406396cb790b21b9d4%22%7D""",
    headers=headers)

data = res.json()
ls = data["reviewAllDOList"]
# print(type(ls))
dd = ls[0]
aa = str(dd["reviewDataVO"]["reviewData"]["reviewBody"])
# print(aa)
bb = aa.replace("<br />", "\n")
print(bb)
# print(type(dd))
# dd["reviewBody"]
# print(data)
