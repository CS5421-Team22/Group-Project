

# 1.Overview
This module is to convert a Python dictionary into a tree.

Each node of the tree can return its parent/child/sibling/value. 



# 2. Get Started

## (1) Prepare

   prepare a dictionary as following:
   
   ```python
   sample1 = {'genres': {'genre': ['Pop', 'World']}}
   
   sample2 = {'library':{ 
                        'album': 
                                [

                                    {
                                     'title': 'Bua Hati',
                                     'artists': {'artist': [{'name': 'Anang Ashanty', 'country': 'Indonesia'},
                                                            {'name': 'Kris Dayanti', 'country': 'Indonesia'}]},
                                     'songs': {'song': [ {'title': 'Timang-Timang', 'duration': '5:13'},
                                                         {'title': 'Miliki Diriku', 'duration': '5:35'},
                                                         {'title': 'Bua Hati', 'duration': '5:07'}]},
                                     'genres': {'genre': ['Pop', 
                                                          'World']},
                                     'year': 1998},

                                    {'title': 'Separuh Jiwaku Pergi',
                                     'artists': {'artist': {'name': 'Anang Ashanty', 'country': 'Indonesia'}},
                                     'songs': {'song': [ {'title': 'Separuh Jiwaku Pergi', 'duration': '5:00'},
                                                         {'title': 'Belajarlah Untuk Cinta', 'duration': '5:23'},
                                                         {'title': 'Hujanpun Menangis', 'duration': '4:17'}]},
                                     'genres': {'genre': ['Pop', 
                                                          'World']},
                                     'year': 1998}
                                ]
                        }
  ```
  
 ## (2) Build tree
  
    Pass your input data into the buildTree(data) function, and it will return the root node of the tree.
     
     
    root1 = buildTree(sample1)
    root2 = builTree(sample2)
