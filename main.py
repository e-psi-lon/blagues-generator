from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from blagues_api import *


blagues = BlaguesAPI(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzA4MDA2NDc4ODA3Njk1NDUwIiwibGltaXQiOjEwMCwia2V5IjoiR05RYlg5Ujk0YW1EZkRZeHFLMHFnMzZ4TTRIT040cEZjUE5JWHZoam40czRiUjBoTTgiLCJjcmVhdGVkX2F0IjoiMjAyMi0wMy0zMFQxNDozMDoyNCswMDowMCIsImlhdCI6MTY0ODY1MDYyNH0.-EIfexJJHJIoIvbyT3ZCPMqqakp36RQ8gHGB5XwAO8Q")


class Blague(Widget):
    joke = ObjectProperty(None)
    answer = ObjectProperty(None)
    joke = "Blague ici"
    answer = "Réponse là"

    async def GLOBAL(self):
        blague = await blagues.random_categorized(BlagueType.GLOBAL)
        self.joke.text = await blague.joke
        self.answer.text = await blague.answer
        return
        
    async def DEV(self):
        blague = await blagues.random_categorized(BlagueType.DEV)
        self.joke.text = await blague.joke
        self.answer.text = await blague.answer
        return
    
    async def BEAUF(self):
        blague = await blagues.random_categorized(BlagueType.BEAUF)
        self.joke.text = blague.joke
        self.answer.text = blague.answer
        return

    async def DARK(self):
        blague = await blagues.random_categorized(BlagueType.DARK)
        self.joke.text = await blague.joke
        self.answer.text = await blague.answer
        return

    async def LIMIT(self):
        blague = await blagues.random_categorized(BlagueType.LIMIT)
        self.joke.text = blague.joke
        self.answer.text = blague.answer
        return

    async def BLONDES(self):
        blague = await blagues.random_categorized(BlagueType.BLONDES)
        self.joke.text = await blague.joke
        self.answer.text = await blague.answer
        return

    async def RANDOM(self):
        blague = await blagues.random
        self.joke.text = await blague.joke
        self.answer.text = await blague.answer
        return


class BlaguesApp(App):
    def build(self):
        app = Blague()
        return app


if __name__ == '__main__':
    BlaguesApp().run()
