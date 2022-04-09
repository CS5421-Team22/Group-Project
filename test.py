library = {'library': {'album': [{'title': 'Bua Hati', 'artists': {'artist': [{'name': 'Anang Ashanty', 'country': 'Indonesia'}, {'name': 'Kris Dayanti', 'country': 'Indonesia'}]}, 'songs': {'song': [{'title': 'Timang-Timang', 'duration': '5:13'}, {'title': 'Miliki Diriku', 'duration': '5:35'}, {'title': 'Bua Hati', 'duration': '5:07'}]}, 'genres': {'genre': ['Pop', 'World']}, 'year': 1998}, {'title': 'Separuh Jiwaku Pergi', 'artists': {'artist': {'name': 'Anang Ashanty', 'country': 'Indonesia'}}, 'songs': {'song': [{'title': 'Separuh Jiwaku Pergi', 'duration': '5:00'}, {'title': 'Belajarlah Untuk Cinta', 'duration': '5:23'}, {'title': 'Hujanpun Menangis', 'duration': '4:17'}]}, 'genres': {'genre': ['Pop', 'World']}, 'year': 1997}]}}
# simple predicate: =
getResult(library, "/child::album[child::title = 'Bua Hati']")
# simple predictate: <=
getResult(library, "/child::album[child::year <= 1997]")
# simple predicate: >=
getResult(library, "/child::album[child::year >= 1998]")
# simple predicate: <
getResult(library, "/child::album[child::year >= 1998]")
# simple predicate: !=
getResult(library, "/child::album[child::year != 1998]")
# complex predicate: or
getResult(library, "/child::album/child::songs/child::song[child::duration = '5:00' or child::duration = '5:23']")
# complex predicate: and
getResult(library, "/child::album/child::songs/child::song[child::duration = '5:00' and child::title = 'Separuh Jiwaku Pergi']")
# complex predicate: combination of or & and
getResult(library, "/child::album/child::songs/child::song[child::title = 'Bua Hati' and child::duration = '5:07' or child::title = 'Separuh Jiwaku Pergi'")

# parent
getResult(library, "/child::album[child::title = 'Bua Hati']/child::title/parent::album")
# sibling
getResult(library, "/child::album[child::title = 'Bua Hati']/child::title/sibling::artists")
# descendant
getResult(library, "/child::album/descendant::title")
# ancestor
getResult(library, "/child::album/descendant::title/ancestor::album")