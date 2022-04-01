from blagues_api import *

blagues = BlaguesAPI("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzA4MDA2NDc4ODA3Njk1NDUwIiwibGltaXQiOjEwMCwia2V5IjoiR05RYlg5Ujk0YW1EZkRZeHFLMHFnMzZ4TTRIT040cEZjUE5JWHZoam40czRiUjBoTTgiLCJjcmVhdGVkX2F0IjoiMjAyMi0wMy0zMFQxNDozMDoyNCswMDowMCIsImlhdCI6MTY0ODY1MDYyNH0.-EIfexJJHJIoIvbyT3ZCPMqqakp36RQ8gHGB5XwAO8Q")

blague = ""
joke = ""
answer = ""
async def dev_joke():
    global blague
    blague = await blagues.random_categorized(BlagueType.DEV)
    global joke
    joke = str(blague.joke)
    global answer
    answer = str(blague.answer)
    print(joke)
    print(answer)
    return()
