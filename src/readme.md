Python source codes for the project.


How to use:


first, run the getResult.py

then:

```python
data = {'library': {'album': [{'title': 'Bua Hati', 'artists': {'artist': [{'name': 'Anang Ashanty', 'country': 'Indonesia'}, 
{'name': 'Kris Dayanti', 'country': 'Indonesia'}]}, 'songs': {'song': [{'title': 'Timang-Timang', 'duration': '5:13'}, 
{'title': 'Miliki Diriku', 'duration': '5:35'}, {'title': 'Bua Hati', 'duration': '5:07'}]}, 'genres': {'genre': ['Pop', 'World']}, 'year': 1998}, 
{'title': 'Separuh Jiwaku Pergi', 'artists': {'artist': {'name': 'Anang Ashanty', 'country': 'Indonesia'}}, 
'songs': {'song': [{'title': 'Separuh Jiwaku Pergi', 'duration': '5:00'}, {'title': 'Belajarlah Untuk Cinta', 'duration': '5:23'}, 
{'title': 'Hujanpun Menangis', 'duration': '4:17'}]}, 'genres': {'genre': ['Pop', 'World']}, 'year': 1998}]}}

print(getResult(data,"//title")
```
