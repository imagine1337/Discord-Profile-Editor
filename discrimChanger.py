import time,requests

token='' #put token here or pass into editProfile function later on
url='https://discord.com/api/v9/users/@me'

def editProfile(discrim,username,password,token=token):
    requests.patch(url,headers={'Authorization':token},data={'discriminator':discrim,'password':password,'username':username})

for i in range(9999):
    time.sleep(43200) #43200 seconds in a day
    editProfile(i,'username','password')
