# # ---------------api for fetching products--------------

# #-----------Main Page URL--------------
# # https://www.walmart.ca/browse/toys/10011
# # -------------------------------------
# # -------------- Categories fetching ------------------------
# # //*[@class="eaue1ee0 css-xhyxqw elkyjhv0"]
#
#
# # https://www.walmart.ca/api/bsp/fetch-products
#
# # ---------------payloads--------------
# payload = json.dumps({
#   "products": [
#     {
#       "sku_id": "10264234",
#       "product_id": "6000119591291"
#     },
#     {
#       "sku_id": "6000200262140",
#       "product_id": "6000200262139",
#       "isSponsored": True,
#       "criteoSellerId": "0",
#       "sponsoredClickBeacon": "//b.da.us.criteo.com/rm?rm_e=yNb0UWhCnanfiKRwbgCvENpT0d_seLtcPxwUxbjIgeQKOIuqTYh9uYYHTQN4Hp7uwyJ2Ei3lNPgYgQ02UGDfHXizv-0yf4U93XhPRtlZLm76b0ZrEpsLQk6k7fQmd56yJcM3qrne6q0qTuHep9Fq0VhRkvE4WIJKo5-txLn0ULqEhXbe7QGB0nsyKDhxNHdPgJA9s_d7S882CD9to7lExmEJ_5yof0sA9ZrNdY8IVofmdZ03lUuIvVCw6paq8p_kkH-i6EQosAAC_6vf_Z3MvF4TYRJFQiJ5PdPJqqeDhMcc_O9OQ-h4tBjlxIhK1AwXKlz_qTso373NAIPkw1_ni1h82S9oYsNZ2cqzl4d5vzzOtaC-tVdSZmlf_2e8Ri4d&ev=4",
#       "sponsoredViewBeacon": "//b.da.us.criteo.com/rm?rm_e=4_WL8uHqGRaJ5bPHfvHCeKYVpJgPvSRzbQyFqdvjsiqjxdHhPGcRThxTK0GA1BqStvZe1FWY6Ysy5JeAgdIiOJ-Y5v7oX4ROFaEiWn3JPwkNmcybuEA9uxncEecC4d0G6lY41M9G1qUYDz4jC5-jext4EXtFDNtxNtc15V18ivKPOZi9q3oPOagWOrEPnOJtfZqvsGnekC_WA2jwsF3hCLhJF5dx7vOh0DMI0UjcwIJloEm1ThhSKnPwSB-9PxGB8ySScEywwtbaxR0rz60qdMpH4I1OK4eKZIZhjxytmMHtgP3iXM8K3D0nIUYmhwbMxcADsBf_w3mxff0wodEwKWJCvD4DoSF-AxFbmfqJj7A&ev=4",
#       "sponsoredURL": "//b.da.us.criteo.com/rm?dest=https%3a%2f%2fwww.walmart.ca%2fen%2fip%2fskywalker-trampolines-60-round-mini-bouncer-trampoline-with-enclosure-blue%2f6000200262139&sig=1-3aPf6zItBTO9pjgZcbzhgcSmdpSowgXU1Q8EbhJ3NCs&rm_e=GiAkyDy7isXqKvCzg_jaMik1PUG_RxWDyT8rPQ9BydejAquyUi3noNz3SLKqGi-6mLWvOmP9maFS6tQnBxv7TAlAB2ammXOYGcQLuEKp78hqM84uYUbwM1IT2_XB0_YYPVOs0zYI3MFUZscknwZexz4t1iAiJz5B_BtheOkBEVDKlT4SlYEf9vV1fHIzpbdSvE9R7Z_5pAtbdZFygHiPUFmPoyKvjWl3oU0nk1nG5lA7Rss8Gtm2JVyYihx7gZ87mdL-TzPOBgY-B6nhMNEBbLEQuxMVpVuke4RLPuU_RwHMNXINepdFPyQw2bQPBkYX5jY__NTgVDgnn6Dr0OgCX9f9d2jv430qP_ulg5IEEc2i85qvbbCv5c8rS5ma8vSV&ev=4"
#     },
#     {
#       "sku_id": "6000205419296",
#       "product_id": "6000205419295"
#     },
#     {
#       "sku_id": "3GO5THQPX9GZ",
#       "product_id": "PRD3GO5THQPX9GZ"
#     },
#     {
#       "sku_id": "6000204655510",
#       "product_id": "6000204655509",
#       "isSponsored": True,
#       "criteoSellerId": "0",
#       "sponsoredClickBeacon": "//b.da.us.criteo.com/rm?rm_e=oRlKpkJGqxTHhwhDLvh8sn1nZlsPmM2LW69_flaiosKIHFULGqxzzV38wDpJg4-Xkd3gvUoEvWoxGL-7zpWFefTxTmmN4DU9b_lOC2-rDE2v9ARWSRpDuT5hOnrsE5qzCFt5po7iAlgeENHKOR9aC_n5LTxUWmcZ2QXLYbuezTDWllmVAnnYUe2-xVTh-_prW8KUfi-a-lDSdqePw3I6hNuN9UIci7O0qaeffz5mzsQLSBYHM6WszW09nX_LrOCgMlBVtk5M6DEedPbWTNHdWO0hYdHlKF6vlLJeRx-KD1EaitbfOmi65lZIGwXGjmrx0X9Rg_AM1jIkLlP7JeTOV3s1HrUbcRURCAOXInFlGY25XUyQPi9bFzOTY4W99ts7&ev=4",
#       "sponsoredViewBeacon": "//b.da.us.criteo.com/rm?rm_e=_jCEO1IFKZ5X0q1L1dmv04tIKZDoPDV61SIXtpCYQbQzyxL7zQU4yMCA6OkqEgW76GNCbV9sa7ynWXigrTqP08PkvV0A3JErUO50NAHgQlGDqcdpqt2Sf2x0a0T4T2NexzEAWgaw50IOP0OlE8KVhywNQz2Fci5UNk0uXeFSzF0ZVHpS0DjUA4tBrz3U2VqYoAJemIsCGLTSMcrjBnQCOY6cE-wkcqHgnbIt3Yag8KYNvaSHzJvpCK5gt_-8ca3RL1exv5-TW4NYzFNZ7evYko3AKotqqlxjEn5quyNb3N_zGc8KpSVD74WnsjmFYey4xgkapRH0xRj4iRyDwxAkrPN5D9qCpFivn0GQw6dYxsE&ev=4",
#       "sponsoredURL": "//b.da.us.criteo.com/rm?dest=https%3a%2f%2fwww.walmart.ca%2fen%2fip%2fnew-bright-143-scale-rc-bigfoot-monster-truck-set-with-ramp-multi-color%2f6000204655509&sig=1-eGVw9lvgaq6-kHdSZOtwhAUTKQv3RtejvH5MfsOlckI&rm_e=QkC5gpvj3diBS5jiQjaQH17VSwN_5pI9numUgDJa7qsPGjUly9i6a8kAnUBdQaWlG_5QBHgj6Hj8TvWaaG2jscNluMzPGrcbZZWcMPVsvcouqMDSVh0Ca7CX4zUKEBx-TZLRr2_1wEUuZmrT9uE3x6uQ-wQiJGFO3igT257AAsPtbtUs892hx--m72rDT4fcpTEDSB0MEClcHuQV-s7wVvEugsLfYDLNiQhu8J2d4DTRfIHpUO0YnGcA7lRhUrrapgy5aK1EfIHXgES9vGEUYd7W_59QYb-JD6V7l7vlK5wnJ9VSsZxq_wosrGuawisKz4d1_-OKUrIDFfAQzo2Z129SpPIOMhMaxkeax1pTloto0vlvlLcfmQ8vEfhJ7VzQ&ev=4"
#     },
#     {
#       "sku_id": "6000205419811",
#       "product_id": "6000205419810"
#     },
#     {
#       "sku_id": "6000198018066",
#       "product_id": "6000198018065"
#     },
#     {
#       "sku_id": "6000195528762",
#       "product_id": "6000195528761",
#       "isSponsored": True,
#       "criteoSellerId": "0",
#       "sponsoredClickBeacon": "//b.da.us.criteo.com/rm?rm_e=XBp2j998iXef08Ap14bLKquX8vJO4cEHi0aAfSxFuiukpUxgrA03EttIk3m5q_zcI8t8u7ox4HTszi_Y0gjXCZOzuEfcxHvDtLNU_LxfbZ8XK1MDfROZ9E57rw9RiUq7s7_xzjJGNjAWB7fV5mAAQ-hKfUGCc7WEwuAhjMA4K0XzYfeZfgkeWEmZmkIsSDSMGZZL6x9iPUw4-KJCP8GgUCmAPOB7Mwwm0COWRhGkJDzDd5frxtRYxgxbihsk6Kc3fkuBQ50s-vd4f9QjdcvVz9RrLl1Hy43vLhdvMxd09h7czst4TXtuECHBw-491ZL8krZp5QK0xrq6VrGnvvbZdakKnHWb_CBO-kaQBVjU4FYaZ30xOKB_JHqyO3A8xf-6&ev=4",
#       "sponsoredViewBeacon": "//b.da.us.criteo.com/rm?rm_e=eOqoNEX6UKLM-B0jbRQLEgX3OZ5svUmGUfQ4ZCvKY3QYs-oxvT5gimZpiQxI_amT989fPzqvr_Xr_VjbZlOUFYSNX_ARsa_qXJLXCzFKi-vSYjkwGtuyelqKyfEYaqLoBgL5fizHtFIXISIfIifzqSbTzy34LKN86g98f3eNFzpxbvRZiXZ1i7ysIzEp5bLCOhiMQ6-5kD1vzrqB-877qQtPXvXV6vquN3FUUmapicZI4uWky9VSsqkV9RI-vmLqABHgbcIedHbKjQnPTKKMYAD6bHg0HyvBHjA2CyYL6TeZjLQdn4BrLzKrZQTDrVA9l0E71KE-lKs2LV85lhgYIvn01LKpXU7dehhUDH47Bg8&ev=4",
#       "sponsoredURL": "//b.da.us.criteo.com/rm?dest=https%3a%2f%2fwww.walmart.ca%2fen%2fip%2ffisher-price-laugh-and-learn-sis-remote-playset-french-edition-multi%2f6000195528761&sig=1-nq1XNEoPDZ71bE2l1ROyxe1i3euafNpY8yMtgxBQZBc&rm_e=iayte7aST7z0UOWiRxOYDI90pdNlLUiXNQcOrKvWHahkI_C4X8DKlpK8o-nIUYf_qB9_YMj3nWcepWgB61279iU73njhx9riFgiqTayRYfOCBclrPqbruq5Cxza3uJMNYf57iksUWRZM5jdELPwR9R5bQJeQ4JAzgVsefX2WuBUsJfmWZdArYrqXe13JGG6JKFeh5I1V4-iOzWZ4vno8vEbA_FC9U_KYWXiuZIeonCILYdmJdOAgO0GWo7XGEnwYYd9aqH-c5HMk72-spClkm9_NhvhPyhCrOSU2qv4bN0abz2fxVNJvga52rdF23DaUFwO35WvWXtpaDqDTCuQ6R6hW1V9Y71FjjDXYMsFnyvbKm7c_ebIJU9bhu7SLbazq&ev=4"
#     },
#     {
#       "sku_id": "6000206669372",
#       "product_id": "6000206669371"
#     },
#     {
#       "sku_id": "6000206711388",
#       "product_id": "6000206711387"
#     },
#     {
#       "sku_id": "6000187721596",
#       "product_id": "6000187721595"
#     },
#     {
#       "sku_id": "6000198714445",
#       "product_id": "6000198714444"
#     },
#     {
#       "sku_id": "6000195398896",
#       "product_id": "6000195398895"
#     },
#     {
#       "sku_id": "6000206616172",
#       "product_id": "6000206616171"
#     },
#     {
#       "sku_id": "6000198018886",
#       "product_id": "6000198018885"
#     },
#     {
#       "sku_id": "6000205428703",
#       "product_id": "6000205428702"
#     },
#     {
#       "sku_id": "6000199052998",
#       "product_id": "6000199052997"
#     },
#     {
#       "sku_id": "6000202816644",
#       "product_id": "6000202816643"
#     },
#     {
#       "sku_id": "6000196696785",
#       "product_id": "6000196696784"
#     },
#     {
#       "sku_id": "6000196459247",
#       "product_id": "6000196459246"
#     },
#     {
#       "sku_id": "6000205450122",
#       "product_id": "6000205450121"
#     },
#     {
#       "sku_id": "6000197568349",
#       "product_id": "6000197568348"
#     },
#     {
#       "sku_id": "6000200728410",
#       "product_id": "6000200728409"
#     },
#     {
#       "sku_id": "6000201727459",
#       "product_id": "6000201727458"
#     },
#     {
#       "sku_id": "10188512",
#       "product_id": "6000078877044"
#     },
#     {
#       "sku_id": "6000192599606",
#       "product_id": "6000192599605"
#     },
#     {
#       "sku_id": "6000206669366",
#       "product_id": "6000206669365"
#     },
#     {
#       "sku_id": "6000197625495",
#       "product_id": "6000197625494"
#     },
#     {
#       "sku_id": "6000204335452",
#       "product_id": "6000204335451"
#     },
#     {
#       "sku_id": "6000205420054",
#       "product_id": "6000205420053"
#     },
#     {
#       "sku_id": "6000205647630",
#       "product_id": "6000205647629"
#     },
#     {
#       "sku_id": "6000206747274",
#       "product_id": "6000206747273"
#     },
#     {
#       "sku_id": "6000205484716",
#       "product_id": "6000205484715"
#     },
#     {
#       "sku_id": "11UXE8NYCPEK",
#       "product_id": "PRD11UXE8NYCPEK"
#     },
#     {
#       "sku_id": "6000205240787",
#       "product_id": "6000205240786"
#     },
#     {
#       "sku_id": "4WHJ9KW68FLF",
#       "product_id": "1QFYEBQ18KAO"
#     },
#     {
#       "sku_id": "6I1P9AETNP6O",
#       "product_id": "PRD6I1P9AETNP6O"
#     },
#     {
#       "sku_id": "6000205566137",
#       "product_id": "6000205566136"
#     },
#     {
#       "sku_id": "6000206315386",
#       "product_id": "6000206315385"
#     },
#     {
#       "sku_id": "6000196696793",
#       "product_id": "6000196696792"
#     },
#     {
#       "sku_id": "5BCXH5N2I9V7",
#       "product_id": "PRD5BCXH5N2I9V7"
#     },
#     {
#       "sku_id": "73EA321TTAW2",
#       "product_id": "PRD73EA321TTAW2"
#     },
#     {
#       "sku_id": "6000202422203",
#       "product_id": "6000202422202"
#     },
#     {
#       "sku_id": "6000206514812",
#       "product_id": "6000206514811"
#     },
#     {
#       "sku_id": "6000200599176",
#       "product_id": "6000200599175"
#     },
#     {
#       "sku_id": "4UK6JFOT21ZL",
#       "product_id": "PRD4UK6JFOT21ZL"
#     },
#     {
#       "sku_id": "6000200613564",
#       "product_id": "6000200613563"
#     }
#   ],
#   "lang": "en"
# })
#
# # ---------------headers--------------
#
#
# headers = {
#   'authority': 'www.walmart.ca',
#   'accept': 'application/json',
#   'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#   'content-type': 'application/json',
#   'cookie': 'deliveryCatchment=1061; walmart.nearestPostalCode=L5V2N6; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; walmart.nearestLatLng="43.60822,-79.69387"; userSegment=50-percent; vtc=TCbjYc0dcz1gjlkzjAPUuI; walmart.id=ee196ffb-a43e-459e-8864-f9a9ec399d2e; _gcl_au=1.1.1224370931.1688655842; _ga=GA1.2.1430749466.1688655844; _gid=GA1.2.28620286.1688655844; s_ecid=MCMID%7C04611159140574387780942481365272090971; kndctr_C4C6370453309C960A490D44_AdobeOrg_identity=CiYwNDYxMTE1OTE0MDU3NDM4Nzc4MDk0MjQ4MTM2NTI3MjA5MDk3MVIPCK2-7d2SMRgBKgRJUkwx8AGtvu3dkjE=; _scid=43fb8521-6d07-45c0-9588-265ecf878adf; _pxvid=5c804495-1c0e-11ee-a22c-94f29ca95557; _sctr=1%7C1688583600000; wmt.c=0; DYN_USER_ID=d281b476-c76e-4e40-a973-c4e54ca7c221; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4x440yDZOTOKXfabw5y0wClWZc8uwnCofoZXbgdc8Wg1DvT3/L30ukhY9Csw6G/WwruRUiL8XWW4LgIvqa6IFImpE9Q3WXwDa5FgvP7/bgJgF+tZHhaD+2qI6q2PBzNRVj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0/w+p+K/WjzuYPePvMUDmNzgKO891whEejdvzQcYsAftTdC0GD+nVo3z789gPVCszb/SoGFgAYL9DGZ8K45WCXDCcb9mgycy9jtT1uIyOBHYf8XczTynrpo9lYjtyESE1EaEj+FZRs1wfVGuoIo0cBxS6b2DXsFBiTsbeVYiiN2UqC/BHIiytsv610gg9Ws5TtMIBWDogSu1BWWsXSTY5NdtfWbPEEu7KJ458IAhMgl0r1eX9YGQ0laieVMoEr348=; LT=1688655867643; _cs_c=0; NEXT_GEN.ENABLED=1; cookiePolicy=true; salsify_session_id=9a8ba3cb-c9f3-4936-88bf-55f8d3d75898; localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJjaXR5IjoiTWlzc2lzc2F1Z2EiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhFQVJUTEFORCwgTUlTU0lTU0FVR0EsT04iLCJmdWxmaWxsbWVudFN0b3JlSWQiOiIxMDYxIiwiZnVsZmlsbG1lbnRUeXBlIjoiSU5TVE9SRV9QSUNLVVAifQ==; headerType=whiteGM; ENV=ak-eus-t1-prod; bstc=Qe5J-ZtiQKbxT3039K1cRM; xpa=12TNt|18laY|1iNRR|20jZP|4Kq-Y|5sfML|ALEbn|AvWMt|J5Q2f|KX9zf|KxDCx|OAQpG|OCyta|PdYAO|Qligk|RxMsL|S2NR7|S9Aer|Sek64|VUeER|Zsz8o|cGOTQ|cMouF|fTP7G|gUGfp|jE0bf|qRHgs|uAQc6|uk0R3; exp-ck=12TNt118laY11iNRR120jZP15sfML1ALEbn3J5Q2f1KxDCx1OAQpG1PdYAO1Qligk1RxMsL1S2NR73S9Aer4Sek643VUeER1Zsz8o1cGOTQ1fTP7G1gUGfp1uk0R31; ak_bmsc=96E9558817FC534F32F2D9387240C1D7~000000000000000000000000000000~YAAQP/V0aPb2uyuJAQAAvXsTLxRBjmVfKR0Clk7ZchtlGmeAR1vfoTFymAcg1zWI78hUkNjnnanLpXrh15JPth8cB6VSLMujJDda9ujckUhc+7ToCAe6uwq3sHWcw9jfyTPJ/C4K8YWg/s08F0DLnlCeon1TQKor/1+8ON8/Hw41+PeE4PkyA9vUQgu2Yb/Sldi1rCz+FToDFe9kqcvLEkLP0ZUj2rBs8qKDV5KWy1KmRLX8DSkVOVijj9qyvsgDyIRI0ExIrSGksLsu1TX66e/J9BXiTAsuIZHbxJle9vxK8BFJmRLbeO5FHJ1i3Em5TvLxPdfPy8CGnXfD07ramt8q8//5P8/4dB6LGEY9vNoPp1GqZwXvy2gAP6SfxL6Gm7VlEzmUGGTZgw==; pxcts=fde0acae-1c90-11ee-9ab8-4c4a5a446169; xpm=1%2B1688711952%2BTCbjYc0dcz1gjlkzjAPUuI~%2B0; cartId=1ad01a8b-6e71-4286-ba3e-bd2aa3585135; s_visit=1; _pin_unauth=dWlkPU5tWXpOVEJtWVdRdE5EazFOQzAwTlRVd0xUazFPVFl0TWpRek5UTTNNV1F5WldNMw; kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster=irl1; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19545%7CMCMID%7C04611159140574387780942481365272090971%7CMCAAMLH-1689316761%7C3%7CMCAAMB-1689316761%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1688719161s%7CNONE%7CvVersion%7C5.2.0%7CMCAID%7CNONE; s_cc=true; crl8.fpcuid=a09d30a0-a4fd-4bd9-83eb-4de6cb85eb36; BVBRANDID=0d4957ce-7b73-4c6f-a39c-acb286014e65; BVBRANDSID=11501155-23ac-465d-8e6c-050cdaec5ea3; BVImplmain_site=2036; s_sq=%5B%5BB%5D%5D; WM.USER_STATE=GUEST|Guest; _scid_r=43fb8521-6d07-45c0-9588-265ecf878adf; _pxff_idp_c=1,s; authDuration={"lat":"1688713785912000","lt":"1688713785912000"}; cto_bundle=Vz9zv19SMG9peE1tMTJhNUFoY3ZXSDNmN1NuR0YlMkJQWWtBUWt3YjRlN082JTJGOTRPQ3Rxa2VoNmpPQlhGeWpKZTRGMWJ4WjV6UWR4NmlBSVI0OHV2cVhFMDBZNG9LZVczM3JyZmhOMVZmeDFpbkV2cWFjQVFORm1yT010c0VSdU9SJTJGR2FQVktld05hbXlrQ3BCNlZJQ3oySDFFJTJCdyUzRCUzRA; _cs_cvars=%7B%221%22%3A%5B%22appName%22%2C%22product-page%22%5D%7D; _cs_id=e1ac95a1-0405-a9ec-92cd-bb393f01aa8c.1688655868.2.1688713787.1688711960.1.1722819868293; _cs_s=12.0.0.1688715587381; _uetsid=592bd7a01c0e11eebdd5938be8b1ef9f; _uetvid=592c90e01c0e11eea099f9a48ce269bf; _px3=001042e684c91d5116177c427a1010dfc485468d9b90c63ca2ca3f30b759eac4:aWMwJvxb/tYPeqRG97szKi7Iv+zGYGf+/OaE6SZaQFKTxcKfE7OvUlzXn7dLwEbQZ7zOvVOzDR6IbtlNgI5kIA==:1000:RwWQ9v7FkQDeCkaRQ7HF2HR/sbFJI8ULOrtx+Ntate5VOR3k29JwMITGeFJ5KvhhjXY3Mg8mW3KY9Jvjz5E4K6iF1Nv9XmYYNA1/FmrEXKh4m/rH4JBmFym994M86AQsCIg+MVXgWzeJjJ7UsdiTtYrcBfs98TYtLhzUUvwe5NPXtoT+7fFVxkmOL6GU84HkzHSXzU0bNaDbxSb8YtiQCw==; s_gnr=1688713787844-Repeat; _cs_mk_aa=0.6059639934075765_1688713787849; gpv_Page=Product%3AEasy-Bake%20Ultimate%20Oven%20Creative%20Baking%20Toy; TS010110a1=017329b029365c978af2d421ae640b1daab4a374ece687206027f2a9f5c9e7eea9a5866d97ca98dd728bec8f0a0599d0908f1eeff9; TS01ea8d4c=017329b029365c978af2d421ae640b1daab4a374ece687206027f2a9f5c9e7eea9a5866d97ca98dd728bec8f0a0599d0908f1eeff9; TS0180da25=017329b029365c978af2d421ae640b1daab4a374ece687206027f2a9f5c9e7eea9a5866d97ca98dd728bec8f0a0599d0908f1eeff9; _gat=1; _pxde=0882507318c39b844d8e838a60d48f906dc84bd9063973c49490c130c2d15f65:eyJ0aW1lc3RhbXAiOjE2ODg3MTM3OTAyMDR9; seqnum=101; TSe62c5f0d027=08fe841b0aab200095884a464df7a8a91bb41f436e486726b012459d995c56c3f893dd07089453bb08dda4cfbe113000d146bc6430bcbf7120507434105ee3f09aad5b57a853da140ba90ac01ba9654dfd535505764e65fcc45fbac682f29367; bm_sv=C539FA3234838D58E5984A2B7EF90AA5~YAAQP/V0aDl0vSuJAQAAN5gvLxSpJ6pKfVhbWrT22VLI1S06XcIS5bcUhAjaw6nIwngAu9QLNU1UcTCuaUHZDdvrmhP/579V2G53DdxG+asUY9OA73JsLocsQp+6hOYZzIUfD0Sp89LRY59JfGoB2STNoxmo/gnnVcU8nXMtqnS6Ee2Fo7ZTiROyp0AkJD+zXmqspRAWBfe7l1nEtzHE7J//OPGS68rPlBVRJqTNnnXLUsRCTkyfukkHfn0a+g47Ig==~1; ENV=ak-eus-t1-prod; TS0180da25=0195ed57a9279d259c7ed6befab709fc5041db9364b52632367f6113b681ab1b6ac891e19d9286cd8ec69dd3b3460f79b2d9539a0c; TS01ea8d4c=0195ed57a9279d259c7ed6befab709fc5041db9364b52632367f6113b681ab1b6ac891e19d9286cd8ec69dd3b3460f79b2d9539a0c; bm_sv=C539FA3234838D58E5984A2B7EF90AA5~YAAQP/V0aA2LvyuJAQAA6PtmLxT1JENJG1i3VFCe0SuMhTe5V0HlcmJWoR+B9AarVbKNBqdbt7va+uIuUHYqUIETpTYT0dx+LY+QuHz9uD8LRquEMyWRTpacjJXiKABOOsRLJ9z3CPkZZ0Pibt6QDVJ6AVfapJ5/xKZWQpCFoKepZlzhyj3nF2lTrESyAhpbfx13A+SRfKXtvGpRMpVpYAPdr31n7UCA8I+3sR60W1Xjgo2n7MxH5iqB9n8JwmFBgg==~1; bstc=Qe5J-ZtiQKbxT3039K1cRM; exp-ck=12TNt118laY11iNRR120jZP15sfML1ALEbn3J5Q2f1KxDCx1OAQpG1PdYAO1Qligk1RxMsL1S2NR73S9Aer4Sek643VUeER1Zsz8o1cGOTQ1fTP7G1gUGfp1uk0R31; seqnum=102; vtc=TCbjYc0dcz1gjlkzjAPUuI; xpa=12TNt|18laY|1iNRR|20jZP|4Kq-Y|5sfML|ALEbn|AvWMt|J5Q2f|KX9zf|KxDCx|OAQpG|OCyta|PdYAO|Qligk|RxMsL|S2NR7|S9Aer|Sek64|VUeER|Zsz8o|cGOTQ|cMouF|fTP7G|gUGfp|jE0bf|qRHgs|uAQc6|uk0R3; xpm=0%2B1688717425%2BTCbjYc0dcz1gjlkzjAPUuI~%2B0; TS010110a1=0195ed57a9279d259c7ed6befab709fc5041db9364b52632367f6113b681ab1b6ac891e19d9286cd8ec69dd3b3460f79b2d9539a0c; TSe62c5f0d027=08414a864dab2000e79e9a53754d2fb524bf1a6df0c6326b1688b136720fa2b305b47c9c7611c05508d1813ea411300044ecb063361b95c75c08697f4daf05a46751dca57c5c08b13492a55c854be7a9363bb735acc478aa93dc37f69a97169e; walmart.nearestLatLng="43.60822,-79.69387"; walmart.nearestPostalCode=L5V2N6',
#   'origin': 'https://www.walmart.ca',
#   'referer': 'https://www.walmart.ca/browse/toys/10011',
#   'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-origin',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#   'wm_qos.correlation_id': '963acda5-02b-1892f15b9c163f,963acda5-02b-1892f15b9c1e4f,963acda5-02b-1892f15b9c1e4f'
# }
# # ----------------Price Offer ----------------
# # https://www.walmart.ca/api/product-page/v4/price-offer
# payload = json.dumps({
#   "fsa": "L5V",
#   "availabilityStoreId": "1061",
#   "lang": "en",
#   "experience": "whiteGM",
#   "pricingStoreId": "1061",
#   "geoAddress": {
#     "deliveryAddress": {
#       "zipCode": "L5V2N6",
#       "countryCode": "CA"
#     },
#     "pickupStoreAddresses": [
#       {
#         "nodeId": "1061",
#         "nodeType": "STORE"
#       }
#     ],
#     "deliveryStoreAddresses": [
#       {
#         "nodeId": "1061",
#         "nodeType": "STORE"
#       }
#     ]
#   },
#   "products": [
#     {
#       "productId": "6000206747273",
#       "skuIds": [
#         "6000206747274"
#       ]
#     }
#   ]
# })
#
# # ----Fetch UPC DATA---

# https://www.walmart.ca/en/ip/barbie-the-movie-ken-doll-wearing-pastel-striped-beach-matching-set-multi/6000206747274

url = "https://api.bazaarvoice.com/data/reviews.json?resource=reviews&action=REVIEWS_N_STATS&filter=productid%3Aeq%3A6000204591217&filter=contentlocale%3Aeq%3Aen_CA%2Cen_GB%2Cen_US%2Cen_CA&filter=isratingsonly%3Aeq%3Afalse&filter_reviews=contentlocale%3Aeq%3Aen_CA%2Cen_GB%2Cen_US%2Cen_CA&include=authors%2Cproducts&filteredstats=reviews&Stats=Reviews&limit=12&offset=0&sort=submissiontime%3Adesc&passkey=e6wzzmz844l2kk3v6v7igfl6i&apiversion=5.5&displaycode=2036-en_ca"

payload = {}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.walmart.ca',
    'Pragma': 'no-cache',
    'Referer': 'https://www.walmart.ca/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
