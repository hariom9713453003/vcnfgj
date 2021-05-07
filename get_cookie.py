import requests

url = "https://aprtacitizen.epragathi.org:8443/dl/aadhaarOtp";
header = {
	"Accept" : "application/json, text/plain, */*",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "aprtacitizen.epragathi.org:8443",
        "Origin": "https://aprtacitizen.epragathi.org",
        "Referer": "https://aprtacitizen.epragathi.org",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36" 
	}
param = {"postData": {
            "mimeType": "application/json;charset=UTF-8",
            "text":{"encHmac":"dU2b/ubN97dG5RFUKWgjBOmFttUKG1EOjVzFOOJWcQ00Fsn9//svTsdYBUWxcc3R","encryptedPid":"MjAyMC0wNy0wM1QyMToxODoyOK7jjVNG0G9TR+8Hf4vGok07G66JQPh3l8yAH5OmMT/9gewb4IVvh61bt0S/d4qIf5znWKq11jBCx1mHsva5ol1zEGDrdK/nPGxxrvpDBxWeM/Kl5jeoYWKh8pFVZCc74iVaf+SM+N8VK7q9zXAQi+yMx/AoYl786assVBN1RIX3YBeQOzSj06vzibyi2pigTtC3SS8pv4JR2Q0Kcak51nOFUf+fQnh67GCj63xXuZ4s9Sz1fZXxNXi+YutznpFY2O//sZAFCkDzq1upfDUuWoeUmjoU2t9P7UiVEiFCFjKc+JHgLWceDtP0stoEL9znZI1/gIhGSA0+S/sd/n7pjyg2Bl8PorzL3tCRqBiOAQXKkch1t4uf3QOUQ3k6WkvnPJnA0E7kIFUMkPuEaEj5QWyoFjoUWKF9AS5L0F9x5AOyMNKk9lKuc/hFzIYiFEedbcLje+tOmaQ22qPoEPYg60y/GHQjBgXNWYx8WR8F3E5UUqEkzERKQKpUrKtLLDkIXAEfIDFUlCNFEfmIzZIvyGSPOe8ODcyyII5lR/CG5w+6X+eS6AvhPYb/6FttKTKzsYuLFfuQjcDheS0Gz4AG93sYsLbrcT4hvbJ1XEIbNRYkteO3CllClOMv5dpm0z2vhfpjMLrx66erLRDbEI3qh51kmqB92VLUAGVMMxa9rUD8TyXB+FRYtXGKcBuflTEO3cUJKjy4S5VLeRIrIQ0Q4yISQiF4OEQlZR1UAEIUw5IeGEfM5D/mCd1evbgV3ZzqE1blldD+LN/YsjYP8y/X1/tcFk85vkR4SSa+/Y+LPQm+ar9OEgWPGadnXXOetG+B9hzD1okkGvHUKknUuV/pL7z+tTsUtaj6U6m1WCOENq+2JpcPcAf/37dbsZmFkUo5RqcXzcP4VbMU8rfhWco9buMcFIbZX30U28836n5sky4UmjHKo3VJ0tzKCbGjuuv3Z2dumwsA7+0/l0aWmz6IDm4gFZ5DlDeqMQCR+PyzBI952P+S+qxjYftL2+zKnBCDm1mUvKxa2ZE6sr7Bvt+/c6bOvwqSIY8vjmP6+aaVpS4uui5XTyALD9RcCBDjUrLjoKFGiRq3wEPmYohtvYf/fmX1o6sbxee4++CoaamWWSeUMpy5LFA4iVlqQBA1tJRMC7bJhhwdSMd3svRolRzsSObW2m5Osnn1gOlbJ2iDKXArw5X+YExuKz891Zto/Urcwfpf3Eu3m+7W2wrzCtmyQ5OkH/HY8sc07usDBLQ5pOKBcjYptgZNCQPLC04qycgNOi7q1ev2zvoLohUDV8hjuoQ86VIUB9X4j6LX8Vxm/OToCuaL24V0IQ9r5hCO1CEoPQXZ91Nz75Cx8Qw6PBMAyw5ufK6evRXqVrhzWm2ObtIG+cNZIwW35ACgv3zUFSGumXpDRw==","encSessionKey":"DzMo+p4dId2/5PjSDDRLdnfR2XQnsOQpSlWw4U57wcb2kS0JCP+YmkoMlwHCNoKTiLcgSIfMOP7tVdUCtlx/7OuncuNPm7eLHi1RZwYlyEN4GQsxpk6LdWjgDkf42fcaUrAt3W4umjhqkZqAmBPpgEYBd79C6UyVA7JHABqFKGn947pWuMzyHUvzGpkNmUzhWdyFk5Cu4xuFtiUfPiFVMeScnWmJ7uept1csQDtvKYcTvXapUfv8AoCEquHcnNEjj68TRVWOLgpma7eZJpPi7qZGPUkgu6ScuBZDlBkxrIBrdqnojivu8scp1+qxPrWgV8kvYraG3du0FYXy/mu86A==","serialnumber":"0578989","udc":"0578989","dpId":"MANTRA.MSIPL","rdsId":"MANTRA.WIN.001","rdsVer":"1.0.1","mi":"MFS100","mc":"MIIEFjCCAv6gAwIBAgIDHoSAMA0GCSqGSIb3DQEBCwUAMIHpMSowKAYDVQQDEyFEUyBNYW50cmEgU29mdGVjaCBJbmRpYSBQdnQgTHRkIDUxTTBLBgNVBDMTREIgMjAzIFNoYXBhdGggSGV4YSBvcHBvc2l0ZSBHdWphcmF0IEhpZ2ggQ291cnQgUyBHIEhpZ2h3YXkgQWhtZWRhYmFkMRIwEAYDVQQJEwlBaG1lZGFiYWQxEDAOBgNVBAgTB0d1amFyYXQxEjAQBgNVBAsTCVRlY2huaWNhbDElMCMGA1UEChMcTWFudHJhIFNvZnRlY2ggSW5kaWEgUHZ0IEx0ZDELMAkGA1UEBhMCSU4wHhcNMjAwNjI5MDQxODA2WhcNMjAwNzI5MDQzMzAyWjCBsDElMCMGA1UEAxMcTWFudHJhIFNvZnRlY2ggSW5kaWEgUHZ0IEx0ZDEeMBwGA1UECxMVQmlvbWV0cmljIE1hbnVmYWN0dXJlMQ4wDAYDVQQKEwVNU0lQTDESMBAGA1UEBxMJQUhNRURBQkFEMRAwDgYDVQQIEwdHVUpBUkFUMQswCQYDVQQGEwJJTjEkMCIGCSqGSIb3DQEJARYVc3VwcG9ydEBtYW50cmF0ZWMuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu+tiXrNgA8YNiCkRjnerDA3pvDAUeYuSwnbZJ6t4oL/824XuInCb5guQebrwbA253lWhbx/5OxHLNUF5bv8142qkgu5LBgItCPCopjIohFw/R9jd8HhCXdFXVTpl8Nio2wPBvKSAVnDBZF7w/YHdNG3Sl3/RmFYmH7RCWB55NetPsyUms/gKXsQNMVUda8TqZ4YattfJa2ivBXjb9y6GDppRZkBc9E338xgbJgcfKbe61Dawt3YY15WBiGgs4+sJgyxmTr4VB4hvp9jh/lt2oa2ltp3UGmwH6+snt0/NHVcfIL0hUK+po7r22t+/BrPKDmTBLfIftL0nmfkoThJXywIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQBQnlMs5VxGiOSlIjvG5D91PeTOHyWsCYiLBlktae/EVMwe3Vrq7R4iZayOWfhSzZeUfgk6PunTa7FD/d6ivd9ElxIFgbW6rtzO38xqgQxD+49VHYkO1OToQoDTIXhZ/0zdbmsPRuOB+1VFc/gBoS1Shc872IbgTKPm0zAzFBZ5Wt/Md5SHMiFui6gwm+dWpfIFmmW8JFZaR3zWSchQW6XukIyCrDkjzYZV1S31zRWnTsXbx7daN4QgxcN2m7JRaqMmTkxHUyVYieZqYfkMufWxFFOKYAwphoyWYTUJtfC/d00ChvA6kwlDnI06EeqOcXNfZJuvNYV7IqHn7Z5P95kb","dc":"db321da2-269c-4ffb-aa54-dfa81f7df3f6","timeStamp":"2020-07-03T21:18:28","crt":"2020/07/03 21:18:28.047","tid":"UKC:20200703211828421","ci":"20221021","attemptType":"1FA","authType":"EKYC","idType":"A","uid_num":"574983865976"}}}

res = requests.post(url, headers=header, json=param)
print(res.text)
