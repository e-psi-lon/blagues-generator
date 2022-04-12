const blagues = new BlaguesAPI("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzA4MDA2NDc4ODA3Njk1NDUwIiwibGltaXQiOjEwMCwia2V5IjoiR05RYlg5Ujk0YW1EZkRZeHFLMHFnMzZ4TTRIT040cEZjUE5JWHZoam40czRiUjBoTTgiLCJjcmVhdGVkX2F0IjoiMjAyMi0wMy0zMFQxNDozMDoyNCswMDowMCIsImlhdCI6MTY0ODY1MDYyNH0.-EIfexJJHJIoIvbyT3ZCPMqqakp36RQ8gHGB5XwAO8Q");

async function normal() {
    var blague = await blagues.randomCategorized(blagues.categories.GLOBAL);
    console.log(blague.joke)
};

async function dev() {
    document.write("dev")
};

async function beauf() {
    document.write("beauf")
};

async function dark() {
    document.write("dark")
};

async function limit() {
    document.write("limit")
};

async function blondes() {
    document.write("blondes")
};

async function random() {
    document.write("random")
}