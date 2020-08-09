import json
import facebook
ACCESS_TOKEN="EAAI07tdEVqYBAOZBj6DV9M9pahRwxRoZChr27K6ZC3oW8WEJdohO2k8AJZCyxaX2KVj5fDfdnkcaUYUxByYRubLHTFhIrFLnQvrGcQ2HDZA8ni1rndF8SGVKCJxv0DXjLsM2kugdhzFLKO104EFzbf1o0EScXVZCvj2IVPwVHWT3ZCYBT6vtYX1IkQkXzMCFOGjopwSEP7AZAxoeTT3RZALUhFZCtDdYCB5hQRygX8YNHa6QZDZD"


def main():
    token = ACCESS_TOKEN
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me',fields='first_name,friends')
    profile1=graph.get_object('me',fields='hometown')
    #print("Printing profile")
    print(type(profile))
    print(json.dumps(profile,indent=4))
    print(json.dumps(profile1,indent=4))
    print(profile.keys())
    print(profile['friends']['data'])
   # print(type(json.dumps(profile, indent=4)))
if __name__=='__main__':
    main()

    
