package main

import (
	"io/ioutil"
	"math/rand"
	"net/http"
	"path"
)

var imagesDir = "./images"

func getRandomImage() string {
	files, _ := ioutil.ReadDir(imagesDir)
	picked := files[rand.Intn(len(files))]
	return path.Join(imagesDir, picked.Name())
}

func main() {

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Cache-Control", "no-cache, no-store")
		http.ServeFile(w, r, getRandomImage())
	})

	http.ListenAndServe(":5000", nil)
}
